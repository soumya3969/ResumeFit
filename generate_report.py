"""
Generate PDF Report for ResumeFit Project
"""

from reportlab.lib.pagesizes import letter, A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak
from reportlab.lib.enums import TA_JUSTIFY, TA_CENTER, TA_LEFT
from datetime import datetime

def create_report():
    """Generate the ResumeFit project report as PDF."""
    
    # Create PDF document
    filename = "ResumeFit_Project_Report.pdf"
    doc = SimpleDocTemplate(filename, pagesize=letter,
                           topMargin=0.5*inch, bottomMargin=0.5*inch,
                           leftMargin=0.75*inch, rightMargin=0.75*inch)
    
    # Container for elements
    elements = []
    
    # Define styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=18,
        textColor='#1f77b4',
        spaceAfter=6,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Heading2'],
        fontSize=12,
        textColor='#666666',
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    heading_style = ParagraphStyle(
        'CustomHeading',
        parent=styles['Heading2'],
        fontSize=11,
        textColor='#1f77b4',
        spaceAfter=6,
        spaceBefore=6,
        fontName='Helvetica-Bold'
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['BodyText'],
        fontSize=9,
        alignment=TA_JUSTIFY,
        spaceAfter=8,
        leading=12
    )
    
    small_style = ParagraphStyle(
        'SmallText',
        parent=styles['BodyText'],
        fontSize=8,
        alignment=TA_CENTER,
        textColor='#666666'
    )
    
    # Title
    elements.append(Paragraph("ResumeFit: Smart Resume Parser", title_style))
    elements.append(Paragraph("Project Report", subtitle_style))
    elements.append(Spacer(1, 0.1*inch))
    
    # Introduction
    elements.append(Paragraph("Introduction", heading_style))
    intro_text = """In today's digital recruitment landscape, processing large volumes of resumes manually is 
    time-consuming and inefficient. ResumeFit addresses this challenge by providing an intelligent resume parsing 
    system that automatically extracts structured information from unstructured resume documents. The system leverages 
    Natural Language Processing (NLP) and pattern matching techniques to identify and extract key information such as 
    personal details, skills, educational background, and work experience from PDF and DOCX resume files. This automated 
    solution significantly reduces manual effort in resume screening processes and enables better candidate data management."""
    elements.append(Paragraph(intro_text, body_style))
    
    # Abstract
    elements.append(Paragraph("Abstract", heading_style))
    abstract_text = """ResumeFit is a Python-based smart resume parser that transforms unstructured resume documents 
    into structured, machine-readable data. The system employs PyMuPDF and python-docx libraries for document parsing, 
    spaCy for Natural Language Processing, and regex patterns for information extraction. The application features an 
    intuitive Streamlit web interface that allows users to upload resumes, view extracted information in real-time, and 
    export results in multiple formats (JSON, CSV, and formatted text). The parser successfully identifies personal 
    information (name, email, phone, social profiles), technical and soft skills (100+ skills database), educational 
    qualifications (degrees, institutions, years), and professional experience (job titles, companies, dates, descriptions). 
    Initial testing demonstrates high accuracy on well-structured resumes, with an average processing time of under 5 seconds 
    per document."""
    elements.append(Paragraph(abstract_text, body_style))
    
    # Tools Used
    elements.append(Paragraph("Tools Used", heading_style))
    tools_text = """The project utilizes the following technologies and libraries: 
    <b>Python 3.12</b> (Core programming language), 
    <b>Streamlit 1.29.0</b> (Web-based user interface framework), 
    <b>PyMuPDF 1.23.8</b> (PDF text extraction and processing), 
    <b>python-docx 1.1.0</b> (Microsoft Word document parsing), 
    <b>spaCy 3.7.2</b> (Natural Language Processing and Named Entity Recognition), 
    <b>Pandas 2.1.4</b> (Data manipulation and CSV export functionality), 
    <b>Regex</b> (Pattern matching for structured information extraction), and 
    <b>NumPy &amp; OpenPyXL</b> (Supporting libraries for data processing)."""
    elements.append(Paragraph(tools_text, body_style))
    
    # Steps Involved
    elements.append(Paragraph("Steps Involved in Building the Project", heading_style))
    
    steps = [
        ("<b>Phase 1: Text Extraction Module</b>", 
         "Implemented document parsing functionality to extract raw text from PDF files using PyMuPDF's fitz library and DOCX files using python-docx. The module handles both file paths and upload streams, with comprehensive error handling and logging."),
        
        ("<b>Phase 2: Text Preprocessing</b>", 
         "Developed preprocessing algorithms to clean extracted text by removing extra whitespace, normalizing line breaks, and filtering non-printable characters. Implemented section detection using regex patterns to identify common resume sections and extract contact information."),
        
        ("<b>Phase 3: Information Extraction</b>", 
         "Created the core analyzer module using spaCy's NLP capabilities and regex patterns. Built a comprehensive skills database covering programming languages, web technologies, databases, cloud platforms, ML/AI tools, and soft skills. Implemented pattern-based extractors for education and work experience."),
        
        ("<b>Phase 4: Data Organization and Export</b>", 
         "Developed export functionality supporting multiple output formats. Implemented JSON export for structured data, CSV export with separate files for main information, education, and experience sections, and formatted text display for human readability."),
        
        ("<b>Phase 5: User Interface Development</b>", 
         "Built an interactive Streamlit web application with three main sections: Upload &amp; Parse, Results, and Export. Implemented real-time progress indicators, summary statistics cards, and responsive design for mobile compatibility."),
        
        ("<b>Phase 6: Testing and Validation</b>", 
         "Created five comprehensive sample resumes covering different roles. Developed automated testing script and validated extraction accuracy. Successfully tested the system with various resume formats and structures.")
    ]
    
    for title, description in steps:
        step_text = f"{title} {description}"
        elements.append(Paragraph(step_text, body_style))
    
    # Conclusion
    elements.append(Paragraph("Conclusion", heading_style))
    conclusion_text = """ResumeFit successfully demonstrates the practical application of Natural Language Processing 
    and pattern matching techniques in automating resume information extraction. The system effectively processes both PDF 
    and DOCX formats, achieving high accuracy in extracting structured data from well-formatted resumes. The intuitive web 
    interface makes the tool accessible to non-technical users, while the multiple export formats ensure integration 
    flexibility with existing recruitment systems. Future enhancements could include batch processing capabilities, advanced 
    machine learning models for improved accuracy, integration with Applicant Tracking Systems (ATS), and support for 
    additional document formats. The project establishes a solid foundation for automated resume processing and demonstrates 
    significant potential for reducing manual effort in recruitment workflows. With over 100 skills in its database and 
    comprehensive extraction algorithms, ResumeFit represents a valuable tool for modern talent acquisition processes."""
    elements.append(Paragraph(conclusion_text, body_style))
    
    # Footer
    elements.append(Spacer(1, 0.2*inch))
    footer_text = f"""<b>Project Repository:</b> https://github.com/soumya3969/ResumeFit<br/>
    <b>Date:</b> December 11, 2025<br/>
    <b>Status:</b> Successfully Implemented and Tested"""
    elements.append(Paragraph(footer_text, small_style))
    
    # Build PDF
    doc.build(elements)
    print(f"✓ PDF report generated successfully: {filename}")
    return filename

if __name__ == "__main__":
    create_report()
