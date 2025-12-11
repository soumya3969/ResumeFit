"""
ResumeFit - Smart Resume Parser
Streamlit Web Application
"""

import streamlit as st
import os
from datetime import datetime
import json

# Import parser modules
from parser.extractor import extract_text
from parser.preprocessor import preprocess_resume_text
from parser.analyzer import ResumeAnalyzer
from parser.exporter import export_to_json, export_to_csv, format_for_display, create_summary_stats


# Page configuration
st.set_page_config(
    page_title="ResumeFit - Smart Resume Parser",
    page_icon="📄",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        text-align: center;
        color: #666;
        margin-bottom: 2rem;
    }
    .stat-box {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        text-align: center;
    }
    .stat-number {
        font-size: 2rem;
        font-weight: bold;
        color: #1f77b4;
    }
    .stat-label {
        font-size: 0.9rem;
        color: #666;
    }
    </style>
""", unsafe_allow_html=True)


def initialize_session_state():
    """Initialize session state variables."""
    if 'parsed_data' not in st.session_state:
        st.session_state.parsed_data = None
    if 'analyzer' not in st.session_state:
        try:
            st.session_state.analyzer = ResumeAnalyzer()
        except Exception as e:
            st.error(f"Error initializing analyzer: {str(e)}")
            st.info("Please make sure spaCy model is installed: `python -m spacy download en_core_web_sm`")
            st.stop()


def main():
    """Main application function."""
    
    initialize_session_state()
    
    # Header
    st.markdown('<h1 class="main-header">📄 ResumeFit</h1>', unsafe_allow_html=True)
    st.markdown('<p class="sub-header">Smart Resume Parser - Extract structured information from resumes</p>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Options")
        
        st.subheader("About")
        st.info("""
        **ResumeFit** extracts:
        - 👤 Personal Information
        - 💼 Skills
        - 🎓 Education
        - 💻 Work Experience
        
        **Supported formats:** PDF, DOCX
        """)
        
        st.subheader("Instructions")
        st.markdown("""
        1. Upload a resume file
        2. Wait for processing
        3. View extracted data
        4. Download results
        """)
    
    # Main content
    tab1, tab2, tab3 = st.tabs(["📤 Upload & Parse", "📊 Results", "💾 Export"])
    
    with tab1:
        st.header("Upload Resume")
        
        uploaded_file = st.file_uploader(
            "Choose a resume file",
            type=['pdf', 'docx'],
            help="Upload a PDF or DOCX resume file"
        )
        
        if uploaded_file is not None:
            # Display file info
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("File Name", uploaded_file.name)
            with col2:
                st.metric("File Size", f"{uploaded_file.size / 1024:.2f} KB")
            with col3:
                file_type = uploaded_file.name.split('.')[-1].upper()
                st.metric("File Type", file_type)
            
            st.divider()
            
            # Parse button
            if st.button("🔍 Parse Resume", type="primary", use_container_width=True):
                with st.spinner("Extracting and analyzing resume..."):
                    try:
                        # Step 1: Extract text
                        st.info("Step 1/4: Extracting text from file...")
                        file_type = uploaded_file.name.split('.')[-1].lower()
                        text = extract_text(uploaded_file, file_type)
                        
                        if not text:
                            st.error("Failed to extract text from the file. Please check the file format.")
                            st.stop()
                        
                        # Step 2: Preprocess
                        st.info("Step 2/4: Preprocessing text...")
                        preprocessed = preprocess_resume_text(text)
                        
                        # Step 3: Analyze
                        st.info("Step 3/4: Analyzing resume content...")
                        parsed_data = st.session_state.analyzer.analyze(
                            preprocessed['cleaned_text'],
                            preprocessed['sections']
                        )
                        
                        # Add contact info to parsed data
                        parsed_data['contact_info'] = preprocessed['contact_info']
                        
                        # Step 4: Complete
                        st.info("Step 4/4: Finalizing results...")
                        st.session_state.parsed_data = parsed_data
                        
                        st.success("✅ Resume parsed successfully!")
                        st.balloons()
                        
                    except Exception as e:
                        st.error(f"Error parsing resume: {str(e)}")
                        st.exception(e)
    
    with tab2:
        st.header("Parsed Results")
        
        if st.session_state.parsed_data is None:
            st.info("👆 Please upload and parse a resume first.")
        else:
            data = st.session_state.parsed_data
            
            # Summary statistics
            st.subheader("📈 Summary")
            col1, col2, col3, col4 = st.columns(4)
            
            with col1:
                st.markdown(f"""
                <div class="stat-box">
                    <div class="stat-number">{len(data.get('skills', []))}</div>
                    <div class="stat-label">Skills Found</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col2:
                st.markdown(f"""
                <div class="stat-box">
                    <div class="stat-number">{len(data.get('education', []))}</div>
                    <div class="stat-label">Education Entries</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col3:
                st.markdown(f"""
                <div class="stat-box">
                    <div class="stat-number">{len(data.get('experience', []))}</div>
                    <div class="stat-label">Work Experiences</div>
                </div>
                """, unsafe_allow_html=True)
            
            with col4:
                has_contact = "✅" if data.get('contact_info') else "❌"
                st.markdown(f"""
                <div class="stat-box">
                    <div class="stat-number">{has_contact}</div>
                    <div class="stat-label">Contact Info</div>
                </div>
                """, unsafe_allow_html=True)
            
            st.divider()
            
            # Detailed results
            col1, col2 = st.columns(2)
            
            with col1:
                # Personal Info
                st.subheader("👤 Personal Information")
                if data.get('name'):
                    st.write(f"**Name:** {data['name']}")
                
                if data.get('contact_info'):
                    contact = data['contact_info']
                    if contact.get('email'):
                        st.write(f"**Email:** {contact['email']}")
                    if contact.get('phone'):
                        st.write(f"**Phone:** {contact['phone']}")
                    if contact.get('linkedin'):
                        st.write(f"**LinkedIn:** {contact['linkedin']}")
                    if contact.get('github'):
                        st.write(f"**GitHub:** {contact['github']}")
                
                st.divider()
                
                # Skills
                st.subheader("💼 Skills")
                if data.get('skills'):
                    # Display as tags
                    skills_html = " ".join([f'<span style="background-color: #e0e0e0; padding: 0.3rem 0.6rem; margin: 0.2rem; border-radius: 0.3rem; display: inline-block;">{skill}</span>' for skill in data['skills']])
                    st.markdown(skills_html, unsafe_allow_html=True)
                else:
                    st.info("No skills found")
            
            with col2:
                # Education
                st.subheader("🎓 Education")
                if data.get('education'):
                    for i, edu in enumerate(data['education'], 1):
                        with st.expander(f"Education {i}: {edu.get('degree', 'N/A')[:50]}"):
                            for key, value in edu.items():
                                st.write(f"**{key.title()}:** {value}")
                else:
                    st.info("No education information found")
                
                st.divider()
                
                # Experience
                st.subheader("💻 Work Experience")
                if data.get('experience'):
                    for i, exp in enumerate(data['experience'], 1):
                        with st.expander(f"Experience {i}: {exp.get('title', 'N/A')[:50]}"):
                            for key, value in exp.items():
                                if key == 'description' and len(str(value)) > 200:
                                    st.write(f"**{key.title()}:** {value[:200]}...")
                                else:
                                    st.write(f"**{key.title()}:** {value}")
                else:
                    st.info("No work experience found")
    
    with tab3:
        st.header("Export Data")
        
        if st.session_state.parsed_data is None:
            st.info("👆 Please upload and parse a resume first.")
        else:
            data = st.session_state.parsed_data
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.subheader("📄 JSON Format")
                st.write("Export as structured JSON file")
                
                # Create JSON download
                json_str = json.dumps(data, indent=2, ensure_ascii=False)
                st.download_button(
                    label="⬇️ Download JSON",
                    data=json_str,
                    file_name=f"resume_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json",
                    mime="application/json",
                    use_container_width=True
                )
                
                # Preview
                with st.expander("Preview JSON"):
                    st.json(data)
            
            with col2:
                st.subheader("📊 Text Format")
                st.write("Export as formatted text")
                
                # Create text download
                text_output = format_for_display(data)
                st.download_button(
                    label="⬇️ Download Text",
                    data=text_output,
                    file_name=f"resume_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt",
                    mime="text/plain",
                    use_container_width=True
                )
                
                # Preview
                with st.expander("Preview Text"):
                    st.text(text_output)
            
            st.divider()
            st.info("💡 Tip: JSON format is better for programmatic access, while text format is more human-readable.")


if __name__ == "__main__":
    main()
