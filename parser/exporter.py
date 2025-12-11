"""
Export Module
Handles exporting parsed resume data to JSON and CSV formats.
"""

import json
import pandas as pd
from typing import Dict, List
from datetime import datetime
import os
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def export_to_json(data: Dict, output_path: str = None, filename: str = None) -> str:
    """
    Export parsed resume data to JSON format.
    
    Args:
        data: Dictionary containing parsed resume data
        output_path: Directory to save the file
        filename: Name of the output file
        
    Returns:
        Path to the saved JSON file
    """
    if output_path is None:
        output_path = "outputs"
    
    # Create output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)
    
    # Generate filename if not provided
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        name = data.get('name', 'resume').replace(' ', '_')
        filename = f"{name}_{timestamp}.json"
    
    filepath = os.path.join(output_path, filename)
    
    try:
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        
        logger.info(f"Successfully exported to JSON: {filepath}")
        return filepath
    except Exception as e:
        logger.error(f"Error exporting to JSON: {str(e)}")
        raise


def export_to_csv(data: Dict, output_path: str = None, filename: str = None) -> str:
    """
    Export parsed resume data to CSV format.
    Creates separate CSV files for different sections.
    
    Args:
        data: Dictionary containing parsed resume data
        output_path: Directory to save the file
        filename: Base name of the output files
        
    Returns:
        Path to the main CSV file
    """
    if output_path is None:
        output_path = "outputs"
    
    # Create output directory if it doesn't exist
    os.makedirs(output_path, exist_ok=True)
    
    # Generate filename if not provided
    if filename is None:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        name = data.get('name', 'resume').replace(' ', '_')
        filename = f"{name}_{timestamp}"
    
    try:
        # Main info CSV
        main_info = {
            'Name': [data.get('name', 'N/A')],
            'Email': [data.get('contact_info', {}).get('email', 'N/A')],
            'Phone': [data.get('contact_info', {}).get('phone', 'N/A')],
            'LinkedIn': [data.get('contact_info', {}).get('linkedin', 'N/A')],
            'GitHub': [data.get('contact_info', {}).get('github', 'N/A')],
            'Skills': [', '.join(data.get('skills', []))],
        }
        main_df = pd.DataFrame(main_info)
        main_filepath = os.path.join(output_path, f"{filename}_main.csv")
        main_df.to_csv(main_filepath, index=False, encoding='utf-8')
        logger.info(f"Exported main info to: {main_filepath}")
        
        # Education CSV
        if data.get('education'):
            edu_df = pd.DataFrame(data['education'])
            edu_filepath = os.path.join(output_path, f"{filename}_education.csv")
            edu_df.to_csv(edu_filepath, index=False, encoding='utf-8')
            logger.info(f"Exported education to: {edu_filepath}")
        
        # Experience CSV
        if data.get('experience'):
            exp_df = pd.DataFrame(data['experience'])
            exp_filepath = os.path.join(output_path, f"{filename}_experience.csv")
            exp_df.to_csv(exp_filepath, index=False, encoding='utf-8')
            logger.info(f"Exported experience to: {exp_filepath}")
        
        return main_filepath
    except Exception as e:
        logger.error(f"Error exporting to CSV: {str(e)}")
        raise


def format_for_display(data: Dict) -> str:
    """
    Format parsed data for readable display.
    
    Args:
        data: Dictionary containing parsed resume data
        
    Returns:
        Formatted string for display
    """
    output = []
    
    # Header
    output.append("=" * 60)
    output.append("RESUME ANALYSIS RESULTS")
    output.append("=" * 60)
    output.append("")
    
    # Name
    if data.get('name'):
        output.append(f"📋 NAME: {data['name']}")
        output.append("")
    
    # Contact Info
    if data.get('contact_info'):
        output.append("📞 CONTACT INFORMATION:")
        contact = data['contact_info']
        if contact.get('email'):
            output.append(f"  • Email: {contact['email']}")
        if contact.get('phone'):
            output.append(f"  • Phone: {contact['phone']}")
        if contact.get('linkedin'):
            output.append(f"  • LinkedIn: {contact['linkedin']}")
        if contact.get('github'):
            output.append(f"  • GitHub: {contact['github']}")
        output.append("")
    
    # Skills
    if data.get('skills'):
        output.append(f"💼 SKILLS ({len(data['skills'])} found):")
        for skill in data['skills']:
            output.append(f"  • {skill}")
        output.append("")
    
    # Education
    if data.get('education'):
        output.append(f"🎓 EDUCATION ({len(data['education'])} entries):")
        for i, edu in enumerate(data['education'], 1):
            output.append(f"  {i}. {edu.get('degree', 'N/A')}")
            if edu.get('institution'):
                output.append(f"     Institution: {edu['institution']}")
            if edu.get('field'):
                output.append(f"     Field: {edu['field']}")
            if edu.get('year'):
                output.append(f"     Year: {edu['year']}")
            output.append("")
    
    # Experience
    if data.get('experience'):
        output.append(f"💻 WORK EXPERIENCE ({len(data['experience'])} entries):")
        for i, exp in enumerate(data['experience'], 1):
            output.append(f"  {i}. {exp.get('title', 'N/A')}")
            if exp.get('company'):
                output.append(f"     Company: {exp['company']}")
            if exp.get('start_date') and exp.get('end_date'):
                output.append(f"     Duration: {exp['start_date']} - {exp['end_date']}")
            elif exp.get('date'):
                output.append(f"     Date: {exp['date']}")
            if exp.get('description'):
                desc = exp['description'][:200] + "..." if len(exp['description']) > 200 else exp['description']
                output.append(f"     Description: {desc}")
            output.append("")
    
    output.append("=" * 60)
    
    return '\n'.join(output)


def create_summary_stats(data: Dict) -> Dict:
    """
    Create summary statistics from parsed resume data.
    
    Args:
        data: Dictionary containing parsed resume data
        
    Returns:
        Dictionary with summary statistics
    """
    stats = {
        'total_skills': len(data.get('skills', [])),
        'education_count': len(data.get('education', [])),
        'experience_count': len(data.get('experience', [])),
        'has_contact_info': bool(data.get('contact_info')),
        'has_name': bool(data.get('name')),
    }
    
    return stats
