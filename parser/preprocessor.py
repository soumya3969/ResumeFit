"""
Text Preprocessing Module
Cleans and preprocesses extracted resume text for better parsing.
"""

import re
import string
from typing import Dict, List


def clean_text(text: str) -> str:
    """
    Clean raw text by removing extra whitespace, special characters, etc.
    
    Args:
        text: Raw text extracted from resume
        
    Returns:
        Cleaned text
    """
    if not text:
        return ""
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text)
    
    # Remove non-printable characters but keep newlines
    text = ''.join(char for char in text if char.isprintable() or char == '\n')
    
    # Normalize line breaks
    text = re.sub(r'\n\s*\n', '\n\n', text)
    
    # Strip leading/trailing whitespace
    text = text.strip()
    
    return text


def normalize_whitespace(text: str) -> str:
    """
    Normalize whitespace in text.
    
    Args:
        text: Input text
        
    Returns:
        Text with normalized whitespace
    """
    return re.sub(r'\s+', ' ', text).strip()


def remove_urls(text: str) -> str:
    """
    Remove URLs from text.
    
    Args:
        text: Input text
        
    Returns:
        Text with URLs removed
    """
    url_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    return re.sub(url_pattern, '', text)


def extract_sections(text: str) -> Dict[str, str]:
    """
    Split resume text into common sections.
    
    Args:
        text: Preprocessed resume text
        
    Returns:
        Dictionary with section names as keys and section content as values
    """
    sections = {}
    
    # Common section headers (case-insensitive)
    section_patterns = {
        'personal_info': r'(?:personal\s+(?:information|details)|contact|profile)',
        'summary': r'(?:summary|objective|profile|about)',
        'experience': r'(?:experience|employment|work\s+history|professional\s+experience)',
        'education': r'(?:education|academic|qualification)',
        'skills': r'(?:skills|technical\s+skills|competencies|expertise)',
        'projects': r'(?:projects|portfolio)',
        'certifications': r'(?:certifications?|licenses?|awards?)',
        'languages': r'(?:languages?)',
    }
    
    # Try to identify section boundaries
    lines = text.split('\n')
    current_section = 'header'
    section_content = {current_section: []}
    
    for line in lines:
        line_lower = line.lower().strip()
        
        # Check if line is a section header
        matched_section = None
        for section_name, pattern in section_patterns.items():
            if re.search(pattern, line_lower) and len(line.split()) <= 5:
                matched_section = section_name
                break
        
        if matched_section:
            current_section = matched_section
            if current_section not in section_content:
                section_content[current_section] = []
        else:
            if current_section not in section_content:
                section_content[current_section] = []
            section_content[current_section].append(line)
    
    # Join content for each section
    sections = {k: '\n'.join(v).strip() for k, v in section_content.items() if v}
    
    return sections


def extract_contact_info(text: str) -> Dict[str, str]:
    """
    Extract contact information from resume text.
    
    Args:
        text: Resume text
        
    Returns:
        Dictionary with contact information
    """
    contact_info = {}
    
    # Email pattern
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    if emails:
        contact_info['email'] = emails[0]
    
    # Phone pattern (various formats)
    phone_pattern = r'(?:\+\d{1,3}[-.\s]?)?\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}'
    phones = re.findall(phone_pattern, text)
    if phones:
        contact_info['phone'] = phones[0]
    
    # LinkedIn pattern
    linkedin_pattern = r'(?:linkedin\.com/in/|linkedin\.com/profile/)([a-zA-Z0-9-]+)'
    linkedin = re.search(linkedin_pattern, text, re.IGNORECASE)
    if linkedin:
        contact_info['linkedin'] = linkedin.group(0)
    
    # GitHub pattern
    github_pattern = r'(?:github\.com/)([a-zA-Z0-9-]+)'
    github = re.search(github_pattern, text, re.IGNORECASE)
    if github:
        contact_info['github'] = github.group(0)
    
    return contact_info


def preprocess_resume_text(text: str) -> Dict[str, any]:
    """
    Main preprocessing function that cleans text and extracts sections.
    
    Args:
        text: Raw resume text
        
    Returns:
        Dictionary containing cleaned text, sections, and contact info
    """
    # Clean the text
    cleaned_text = clean_text(text)
    
    # Extract sections
    sections = extract_sections(cleaned_text)
    
    # Extract contact information
    contact_info = extract_contact_info(cleaned_text)
    
    return {
        'cleaned_text': cleaned_text,
        'sections': sections,
        'contact_info': contact_info
    }
