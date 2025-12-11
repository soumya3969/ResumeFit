# Setup and Installation Guide

## Quick Start

Follow these steps to get ResumeFit up and running:

### 1. Install Python Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- streamlit (Web UI)
- PyMuPDF (PDF parsing)
- python-docx (DOCX parsing)
- spacy (NLP)
- pandas (Data manipulation)
- And other required packages

### 2. Download spaCy Language Model

```bash
python -m spacy download en_core_web_sm
```

This downloads the English language model needed for NLP analysis.

### 3. Run the Application

```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

### 4. Test the Parser (Optional)

Run the test script to verify everything works:

```bash
python test_parser.py
```

## Usage

1. **Upload Resume**: Click "Browse files" and select a PDF or DOCX resume
2. **Parse**: Click "Parse Resume" to extract information
3. **View Results**: See extracted skills, education, and experience
4. **Export**: Download results as JSON or formatted text

## Project Structure

```
ResumeFit/
├── app.py                      # Main Streamlit application
├── parser/                     # Core parsing modules
│   ├── __init__.py
│   ├── extractor.py           # Text extraction (PDF/DOCX)
│   ├── preprocessor.py        # Text cleaning
│   ├── analyzer.py            # Information extraction
│   └── exporter.py            # Export to JSON/CSV
├── test_resumes/              # Sample resumes for testing
│   ├── sample_resume_1.md
│   ├── sample_resume_2.md
│   ├── sample_resume_3.md
│   ├── sample_resume_4.md
│   └── sample_resume_5.md
├── outputs/                   # Parsed results (auto-created)
├── test_parser.py            # Test script
├── requirements.txt          # Python dependencies
└── README.md                 # Documentation
```

## Features Implemented

✅ **Text Extraction**
- PDF parsing using PyMuPDF
- DOCX parsing using python-docx
- Handles both file paths and uploaded files

✅ **Text Preprocessing**
- Text cleaning and normalization
- Section extraction (Experience, Education, Skills)
- Contact information extraction (email, phone, LinkedIn, GitHub)

✅ **Information Extraction**
- Name extraction
- Skills identification (100+ common skills database)
- Education parsing (degrees, institutions, years)
- Experience parsing (job titles, companies, dates)
- Uses spaCy for NLP and regex for pattern matching

✅ **Data Export**
- JSON format (structured data)
- CSV format (tabular data)
- Formatted text display
- Multiple export options

✅ **Web Interface**
- Clean, modern Streamlit UI
- File upload functionality
- Real-time parsing
- Interactive results display
- Download buttons for exports

## Troubleshooting

### spaCy Model Not Found
```
Error: Can't find model 'en_core_web_sm'
```
**Solution:** Run `python -m spacy download en_core_web_sm`

### Import Errors
```
ModuleNotFoundError: No module named 'streamlit'
```
**Solution:** Run `pip install -r requirements.txt`

### PDF Parsing Issues
- Ensure PDF is text-based (not scanned image)
- Try converting PDF to DOCX and retry

### Low Accuracy
- Parser works best with well-structured resumes
- Clear section headers improve accuracy
- Standard resume formats give better results

## Testing

### Test with Sample Resumes

The `test_resumes/` directory contains 5 sample resumes:
1. Software Engineer
2. Data Scientist
3. Frontend Developer
4. DevOps Engineer
5. Full Stack Developer

To test with these:
1. Convert .md files to PDF/DOCX (see test_resumes/README.md)
2. Upload through the web interface
3. Compare extracted data with original

### Automated Testing

```bash
python test_parser.py
```

This runs the parser on sample text and displays results.

## Customization

### Adding More Skills

Edit `parser/analyzer.py` and add skills to the `common_skills` dictionary:

```python
self.common_skills = {
    'programming': ['python', 'java', 'your_skill'],
    # ... add more
}
```

### Improving Extraction Patterns

Modify regex patterns in:
- `parser/preprocessor.py` - for contact info and sections
- `parser/analyzer.py` - for education and experience

### Changing UI Theme

Edit custom CSS in `app.py`:

```python
st.markdown("""
    <style>
    .main-header {
        color: #your_color;
    }
    </style>
""", unsafe_allow_html=True)
```

## Performance Tips

- First run may be slow (loading spaCy model)
- Subsequent parses are faster
- Large files (>10MB) may take longer
- Close browser tabs when not in use

## Next Steps

1. ✅ Basic setup complete
2. 📤 Test with your own resumes
3. 🔧 Customize skills database
4. 🚀 Deploy to cloud (optional)
5. 📊 Integrate with ATS or database

## Support

For issues or questions:
- Check the troubleshooting section
- Review code comments in parser modules
- Test with sample resumes first
- Ensure all dependencies are installed

## License

MIT License - feel free to use and modify!
