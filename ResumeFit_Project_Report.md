# ResumeFit: Smart Resume Parser
## Project Report

---

### **Introduction**

In today's digital recruitment landscape, processing large volumes of resumes manually is time-consuming and inefficient. ResumeFit addresses this challenge by providing an intelligent resume parsing system that automatically extracts structured information from unstructured resume documents. The system leverages Natural Language Processing (NLP) and pattern matching techniques to identify and extract key information such as personal details, skills, educational background, and work experience from PDF and DOCX resume files. This automated solution significantly reduces manual effort in resume screening processes and enables better candidate data management.

### **Abstract**

ResumeFit is a Python-based smart resume parser that transforms unstructured resume documents into structured, machine-readable data. The system employs PyMuPDF and python-docx libraries for document parsing, spaCy for Natural Language Processing, and regex patterns for information extraction. The application features an intuitive Streamlit web interface that allows users to upload resumes, view extracted information in real-time, and export results in multiple formats (JSON, CSV, and formatted text). The parser successfully identifies personal information (name, email, phone, social profiles), technical and soft skills (100+ skills database), educational qualifications (degrees, institutions, years), and professional experience (job titles, companies, dates, descriptions). Initial testing demonstrates high accuracy on well-structured resumes, with an average processing time of under 5 seconds per document.

### **Tools Used**

The project utilizes the following technologies and libraries:

- **Python 3.12**: Core programming language
- **Streamlit 1.29.0**: Web-based user interface framework
- **PyMuPDF 1.23.8**: PDF text extraction and processing
- **python-docx 1.1.0**: Microsoft Word document parsing
- **spaCy 3.7.2**: Natural Language Processing and Named Entity Recognition
- **Pandas 2.1.4**: Data manipulation and CSV export functionality
- **Regex**: Pattern matching for structured information extraction
- **NumPy & OpenPyXL**: Supporting libraries for data processing

### **Steps Involved in Building the Project**

**Phase 1: Text Extraction Module**
Implemented document parsing functionality to extract raw text from PDF files using PyMuPDF's `fitz` library and DOCX files using python-docx. The module handles both file paths and upload streams, with comprehensive error handling and logging.

**Phase 2: Text Preprocessing**
Developed preprocessing algorithms to clean extracted text by removing extra whitespace, normalizing line breaks, and filtering non-printable characters. Implemented section detection using regex patterns to identify common resume sections (Summary, Experience, Education, Skills) and extract contact information (email, phone numbers, LinkedIn, GitHub profiles).

**Phase 3: Information Extraction**
Created the core analyzer module using spaCy's NLP capabilities and regex patterns. Built a comprehensive skills database covering programming languages, web technologies, databases, cloud platforms, ML/AI tools, and soft skills. Implemented pattern-based extractors for education (degrees, institutions, years, fields) and work experience (job titles, companies, dates, descriptions).

**Phase 4: Data Organization and Export**
Developed export functionality supporting multiple output formats. Implemented JSON export for structured data, CSV export with separate files for main information, education, and experience sections, and formatted text display for human readability.

**Phase 5: User Interface Development**
Built an interactive Streamlit web application with three main sections: Upload & Parse (file upload and processing), Results (interactive display with statistics and expandable sections), and Export (download options). Implemented real-time progress indicators, summary statistics cards, and responsive design for mobile compatibility.

**Phase 6: Testing and Validation**
Created five comprehensive sample resumes covering different roles (Software Engineer, Data Scientist, Frontend Developer, DevOps Engineer, Full Stack Developer). Developed automated testing script and validated extraction accuracy. Successfully tested the system with various resume formats and structures.

### **Conclusion**

ResumeFit successfully demonstrates the practical application of Natural Language Processing and pattern matching techniques in automating resume information extraction. The system effectively processes both PDF and DOCX formats, achieving high accuracy in extracting structured data from well-formatted resumes. The intuitive web interface makes the tool accessible to non-technical users, while the multiple export formats ensure integration flexibility with existing recruitment systems. Future enhancements could include batch processing capabilities, advanced machine learning models for improved accuracy, integration with Applicant Tracking Systems (ATS), and support for additional document formats. The project establishes a solid foundation for automated resume processing and demonstrates significant potential for reducing manual effort in recruitment workflows. With over 100 skills in its database and comprehensive extraction algorithms, ResumeFit represents a valuable tool for modern talent acquisition processes.

---

**Project Repository**: https://github.com/soumya3969/ResumeFit  
**Date**: December 11, 2025  
**Status**: Successfully Implemented and Tested
