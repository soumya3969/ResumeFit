"""
Resume Analyzer Module
Extracts structured information (skills, education, experience) using spaCy and regex.
"""

import re
import spacy
from typing import Dict, List, Optional
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class ResumeAnalyzer:
    """
    Main class for analyzing and extracting structured information from resumes.
    """
    
    def __init__(self):
        """Initialize the analyzer with spaCy model."""
        try:
            self.nlp = spacy.load("en_core_web_sm")
            logger.info("Loaded spaCy model successfully")
        except OSError:
            logger.error("spaCy model not found. Please run: python -m spacy download en_core_web_sm")
            raise
        
        # Common skills database (can be expanded)
        self.common_skills = {
            'programming': ['python', 'java', 'javascript', 'c++', 'c#', 'ruby', 'php', 
                          'swift', 'kotlin', 'go', 'rust', 'typescript', 'r', 'matlab'],
            'web': ['html', 'css', 'react', 'angular', 'vue', 'node.js', 'django', 
                   'flask', 'fastapi', 'express', 'spring', 'asp.net', 'rest api'],
            'database': ['sql', 'mysql', 'postgresql', 'mongodb', 'redis', 'oracle', 
                        'sqlite', 'cassandra', 'dynamodb'],
            'cloud': ['aws', 'azure', 'gcp', 'docker', 'kubernetes', 'terraform', 
                     'jenkins', 'ci/cd'],
            'ml_ai': ['machine learning', 'deep learning', 'tensorflow', 'pytorch', 
                     'scikit-learn', 'keras', 'nlp', 'computer vision', 'opencv'],
            'tools': ['git', 'github', 'gitlab', 'jira', 'confluence', 'slack', 
                     'visual studio', 'vscode', 'intellij'],
            'soft_skills': ['leadership', 'communication', 'teamwork', 'problem solving',
                          'critical thinking', 'time management', 'agile', 'scrum']
        }
        
        # Flatten skills for easy searching
        self.all_skills = []
        for category, skills in self.common_skills.items():
            self.all_skills.extend(skills)
    
    def extract_name(self, text: str) -> Optional[str]:
        """
        Extract candidate name from resume text.
        Usually the first line or first PERSON entity.
        
        Args:
            text: Resume text
            
        Returns:
            Extracted name or None
        """
        # Try to get from first few lines
        lines = text.split('\n')
        for line in lines[:5]:
            line = line.strip()
            if line and len(line.split()) <= 4 and len(line) < 50:
                # Check if it looks like a name (not email, phone, etc.)
                if not re.search(r'@|http|www|\d{3}[-.]?\d{3}[-.]?\d{4}', line.lower()):
                    return line
        
        # Try using spaCy NER
        doc = self.nlp(text[:500])  # Process first 500 chars
        for ent in doc.ents:
            if ent.label_ == "PERSON":
                return ent.text
        
        return None
    
    def extract_skills(self, text: str) -> List[str]:
        """
        Extract skills from resume text using pattern matching.
        
        Args:
            text: Resume text
            
        Returns:
            List of identified skills
        """
        text_lower = text.lower()
        found_skills = []
        
        # Search for each skill in the text
        for skill in self.all_skills:
            # Use word boundaries to avoid partial matches
            pattern = r'\b' + re.escape(skill.lower()) + r'\b'
            if re.search(pattern, text_lower):
                # Preserve original capitalization of skill
                found_skills.append(skill.title())
        
        # Remove duplicates and sort
        found_skills = sorted(list(set(found_skills)))
        
        logger.info(f"Extracted {len(found_skills)} skills")
        return found_skills
    
    def extract_education(self, text: str) -> List[Dict[str, str]]:
        """
        Extract education information from resume text.
        
        Args:
            text: Resume text
            
        Returns:
            List of education entries
        """
        education = []
        
        # Common degree patterns
        degree_patterns = [
            r'(?:bachelor|b\.?s\.?|b\.?a\.?|b\.?tech|b\.?e\.?)',
            r'(?:master|m\.?s\.?|m\.?a\.?|m\.?tech|m\.?e\.?|mba)',
            r'(?:phd|ph\.?d\.?|doctorate)',
            r'(?:associate|a\.?s\.?|a\.?a\.?)',
            r'(?:diploma|certificate)'
        ]
        
        # Fields of study
        fields_pattern = r'(?:computer science|engineering|business|arts|science|mathematics|physics|chemistry|biology|economics|finance|marketing|management)'
        
        lines = text.split('\n')
        
        for i, line in enumerate(lines):
            line_lower = line.lower()
            
            # Check if line contains degree information
            for degree_pattern in degree_patterns:
                if re.search(degree_pattern, line_lower):
                    entry = {'degree': line.strip()}
                    
                    # Try to find field of study
                    field_match = re.search(fields_pattern, line_lower)
                    if field_match:
                        entry['field'] = field_match.group(0).title()
                    
                    # Try to find year (look in current and next few lines)
                    year_pattern = r'(?:19|20)\d{2}'
                    for j in range(i, min(i+3, len(lines))):
                        year_match = re.search(year_pattern, lines[j])
                        if year_match:
                            entry['year'] = year_match.group(0)
                            break
                    
                    # Try to find university/institution
                    if i > 0:
                        prev_line = lines[i-1].strip()
                        if prev_line and len(prev_line) > 5:
                            entry['institution'] = prev_line
                    elif i < len(lines) - 1:
                        next_line = lines[i+1].strip()
                        if next_line and len(next_line) > 5 and not re.search(year_pattern, next_line):
                            entry['institution'] = next_line
                    
                    education.append(entry)
                    break
        
        logger.info(f"Extracted {len(education)} education entries")
        return education
    
    def extract_experience(self, text: str) -> List[Dict[str, str]]:
        """
        Extract work experience from resume text.
        
        Args:
            text: Resume text
            
        Returns:
            List of experience entries
        """
        experiences = []
        
        # Common job title keywords
        job_titles = [
            'engineer', 'developer', 'programmer', 'analyst', 'scientist',
            'manager', 'director', 'consultant', 'specialist', 'architect',
            'lead', 'senior', 'junior', 'intern', 'associate', 'coordinator'
        ]
        
        # Date patterns
        date_pattern = r'(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.?\s+\d{4}|(?:19|20)\d{2}'
        
        lines = text.split('\n')
        
        for i, line in enumerate(lines):
            line_lower = line.lower()
            
            # Check if line contains job title
            for title in job_titles:
                if title in line_lower:
                    entry = {'title': line.strip()}
                    
                    # Try to find dates (look in current and next few lines)
                    dates = []
                    for j in range(max(0, i-1), min(i+3, len(lines))):
                        date_matches = re.findall(date_pattern, lines[j], re.IGNORECASE)
                        dates.extend(date_matches)
                    
                    if len(dates) >= 2:
                        entry['start_date'] = dates[0]
                        entry['end_date'] = dates[1]
                    elif len(dates) == 1:
                        entry['date'] = dates[0]
                    
                    # Try to find company (usually before or after title)
                    if i > 0:
                        prev_line = lines[i-1].strip()
                        if prev_line and len(prev_line) > 3 and not re.search(date_pattern, prev_line):
                            entry['company'] = prev_line
                    elif i < len(lines) - 1:
                        next_line = lines[i+1].strip()
                        if next_line and len(next_line) > 3 and not re.search(date_pattern, next_line):
                            entry['company'] = next_line
                    
                    # Collect description (next few lines until empty line or new section)
                    description_lines = []
                    for j in range(i+1, min(i+10, len(lines))):
                        desc_line = lines[j].strip()
                        if not desc_line or any(keyword in desc_line.lower() for keyword in job_titles):
                            break
                        if not re.search(date_pattern, desc_line):
                            description_lines.append(desc_line)
                    
                    if description_lines:
                        entry['description'] = ' '.join(description_lines)
                    
                    experiences.append(entry)
                    break
        
        logger.info(f"Extracted {len(experiences)} experience entries")
        return experiences
    
    def analyze(self, text: str, sections: Optional[Dict[str, str]] = None) -> Dict[str, any]:
        """
        Main analysis function that extracts all information from resume.
        
        Args:
            text: Resume text
            sections: Pre-extracted sections (optional)
            
        Returns:
            Dictionary containing all extracted information
        """
        logger.info("Starting resume analysis")
        
        result = {
            'name': self.extract_name(text),
            'skills': [],
            'education': [],
            'experience': []
        }
        
        # Extract skills from full text or skills section
        if sections and 'skills' in sections:
            result['skills'] = self.extract_skills(sections['skills'])
        else:
            result['skills'] = self.extract_skills(text)
        
        # Extract education from education section or full text
        if sections and 'education' in sections:
            result['education'] = self.extract_education(sections['education'])
        else:
            result['education'] = self.extract_education(text)
        
        # Extract experience from experience section or full text
        if sections and 'experience' in sections:
            result['experience'] = self.extract_experience(sections['experience'])
        else:
            result['experience'] = self.extract_experience(text)
        
        logger.info("Completed resume analysis")
        return result
