# ResumeFit - Smart Resume Parser

A Python-based resume parser that extracts structured information (skills, education, experience) from PDF and DOCX resumes using NLP and pattern matching.

## Features

- 📄 Extract text from PDF and DOCX resumes
- 🔍 Parse skills, education, and work experience
- 🎯 Clean and preprocess resume text
- 📊 Export results to JSON and CSV
- 🖥️ User-friendly Streamlit interface

## Installation

1. Clone the repository:
```bash
git clone https://github.com/soumya3969/ResumeFit.git
cd ResumeFit
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Download spaCy language model:
```bash
python -m spacy download en_core_web_sm
```

## Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

Then:
1. Upload a resume (PDF or DOCX)
2. View extracted information
3. Download results as JSON or CSV

## Project Structure

```
ResumeFit/
├── app.py                  # Streamlit UI
├── parser/
│   ├── __init__.py
│   ├── extractor.py       # Text extraction from files
│   ├── preprocessor.py    # Text cleaning
│   ├── analyzer.py        # Information extraction
│   └── exporter.py        # Export to JSON/CSV
├── test_resumes/          # Sample resumes for testing
├── outputs/               # Parsed results
├── requirements.txt
└── README.md
```

## Technologies Used

- **Python 3.8+**
- **Streamlit** - Web UI
- **PyMuPDF** - PDF parsing
- **python-docx** - DOCX parsing
- **spaCy** - NLP and entity recognition
- **pandas** - Data manipulation and export

## License

MIT License
