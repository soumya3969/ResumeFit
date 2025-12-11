"""
Test Script for Resume Parser
Tests the parser with sample resumes and generates reports.
"""

import os
import sys
from parser.extractor import extract_text
from parser.preprocessor import preprocess_resume_text
from parser.analyzer import ResumeAnalyzer
from parser.exporter import export_to_json, export_to_csv, format_for_display


def test_resume_parser():
    """Test the resume parser with sample resumes."""
    
    print("=" * 70)
    print("RESUMEFIT - RESUME PARSER TEST")
    print("=" * 70)
    print()
    
    # Initialize analyzer
    try:
        print("Initializing analyzer...")
        analyzer = ResumeAnalyzer()
        print("✓ Analyzer initialized successfully")
        print()
    except Exception as e:
        print(f"✗ Error initializing analyzer: {str(e)}")
        print("Please run: python -m spacy download en_core_web_sm")
        return
    
    # Test with sample text resume
    print("Testing with sample resume text...")
    print("-" * 70)
    
    sample_resume = """
    John Doe
    Email: john.doe@email.com
    Phone: +1-555-123-4567
    LinkedIn: linkedin.com/in/johndoe
    GitHub: github.com/johndoe
    
    PROFESSIONAL SUMMARY
    Experienced Software Engineer with 5+ years in full-stack development
    
    SKILLS
    Python, Java, JavaScript, React, Node.js, Django, Flask
    AWS, Docker, Kubernetes, Git, SQL, MongoDB
    Machine Learning, TensorFlow, scikit-learn
    
    WORK EXPERIENCE
    
    Senior Software Engineer
    Tech Company Inc.
    Jan 2020 - Present
    - Led development of cloud-based applications
    - Managed team of 5 developers
    - Implemented CI/CD pipelines using Jenkins and Docker
    
    Software Engineer
    StartUp Corp
    Jun 2018 - Dec 2019
    - Developed RESTful APIs using Django and Flask
    - Built responsive web interfaces with React
    - Optimized database queries improving performance by 40%
    
    EDUCATION
    
    Master of Science in Computer Science
    Stanford University
    2016 - 2018
    
    Bachelor of Science in Computer Science
    University of California, Berkeley
    2012 - 2016
    
    CERTIFICATIONS
    AWS Certified Solutions Architect
    Certified Kubernetes Administrator
    """
    
    try:
        # Preprocess
        print("1. Preprocessing text...")
        preprocessed = preprocess_resume_text(sample_resume)
        print(f"   ✓ Found {len(preprocessed['sections'])} sections")
        print(f"   ✓ Extracted contact info: {list(preprocessed['contact_info'].keys())}")
        print()
        
        # Analyze
        print("2. Analyzing resume content...")
        parsed_data = analyzer.analyze(
            preprocessed['cleaned_text'],
            preprocessed['sections']
        )
        parsed_data['contact_info'] = preprocessed['contact_info']
        
        print(f"   ✓ Name: {parsed_data['name']}")
        print(f"   ✓ Skills found: {len(parsed_data['skills'])}")
        print(f"   ✓ Education entries: {len(parsed_data['education'])}")
        print(f"   ✓ Experience entries: {len(parsed_data['experience'])}")
        print()
        
        # Display results
        print("3. Parsed Results:")
        print("-" * 70)
        print(format_for_display(parsed_data))
        print()
        
        # Export
        print("4. Exporting results...")
        json_path = export_to_json(parsed_data, output_path="outputs", filename="test_sample.json")
        print(f"   ✓ Exported to JSON: {json_path}")
        
        csv_path = export_to_csv(parsed_data, output_path="outputs", filename="test_sample")
        print(f"   ✓ Exported to CSV: {csv_path}")
        print()
        
        print("=" * 70)
        print("TEST COMPLETED SUCCESSFULLY!")
        print("=" * 70)
        print()
        print("Next steps:")
        print("1. Install dependencies: pip install -r requirements.txt")
        print("2. Download spaCy model: python -m spacy download en_core_web_sm")
        print("3. Run the app: streamlit run app.py")
        print("4. Upload your own resumes to test!")
        
    except Exception as e:
        print(f"✗ Error during testing: {str(e)}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    test_resume_parser()
