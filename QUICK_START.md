# ResumeFit - Quick Reference

## 🚀 Getting Started in 3 Steps

```bash
# Step 1: Install dependencies
pip install -r requirements.txt

# Step 2: Run the app
streamlit run app.py

# Step 3: Open http://localhost:8501 in your browser
```

## 📋 What Gets Extracted

| Category | Examples |
|----------|----------|
| **👤 Personal Info** | Name, Email, Phone, LinkedIn, GitHub |
| **💼 Skills** | Python, Java, React, AWS, Docker, Machine Learning |
| **🎓 Education** | Degrees, Universities, Years, Fields of Study |
| **💻 Experience** | Job Titles, Companies, Dates, Descriptions |

## 🎯 Supported File Formats

- ✅ PDF (`.pdf`)
- ✅ DOCX (`.docx`)

## 📥 Export Formats

- 📄 **JSON** - Structured data for applications
- 📊 **CSV** - Spreadsheet format for analysis
- 📝 **Text** - Human-readable formatted output

## 🧪 Quick Test

```bash
python test_parser.py
```

This will:
1. Parse a sample resume
2. Extract all information
3. Display results
4. Save to `outputs/` directory

## 📊 Expected Results

For a typical resume, you should get:
- **15-25 skills** extracted
- **1-3 education** entries
- **2-5 work experiences**
- **Complete contact** information

## 🔧 Troubleshooting

### Problem: spaCy model not found
**Solution:**
```bash
pip install https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-3.7.1/en_core_web_sm-3.7.1-py3-none-any.whl
```

### Problem: Module not found
**Solution:**
```bash
pip install -r requirements.txt
```

### Problem: Streamlit won't start
**Solution:**
```bash
# Make sure you're in the project directory
cd /workspaces/ResumeFit
streamlit run app.py
```

## 💡 Tips for Best Results

1. **Use well-structured resumes** - Clear sections improve accuracy
2. **Standard section headers** - "Experience", "Education", "Skills"
3. **Text-based PDFs** - Scanned images won't work
4. **Standard formats** - ATS-friendly resumes work best

## 📁 Project Files Overview

```
📦 ResumeFit
├── 🎯 app.py                    # Run this to start the app
├── 📁 parser/                   # Core parsing logic
├── 📁 test_resumes/             # Sample resumes for testing
├── 📁 outputs/                  # Parsed results saved here
├── 🧪 test_parser.py            # Test script
├── 📋 requirements.txt          # Dependencies list
└── 📖 README.md                 # Documentation
```

## 🎨 UI Features

### Upload Tab
- Drag & drop or click to upload
- Shows file info (name, size, type)
- Parse button to start extraction

### Results Tab
- Summary statistics cards
- Personal information display
- Skills as interactive tags
- Education entries (expandable)
- Work experience (expandable)

### Export Tab
- JSON download button
- Text download button
- Preview before downloading
- Timestamp in filenames

## 🔍 Skills Categories

The parser recognizes 100+ skills across:
- Programming Languages
- Web Frameworks
- Databases
- Cloud Platforms
- ML/AI Tools
- DevOps Tools
- Soft Skills

## 📈 Accuracy Tips

**High Accuracy Resumes:**
- ✅ Clear section headers
- ✅ Standard formatting
- ✅ Bullet points for experience
- ✅ Dates in standard format

**May Have Issues:**
- ❌ Heavily formatted/designed resumes
- ❌ Scanned images
- ❌ Non-standard section names
- ❌ Tables within tables

## 🎓 Sample Resume Formats

Check `test_resumes/` for examples:
1. Software Engineer resume
2. Data Scientist resume
3. Frontend Developer resume
4. DevOps Engineer resume
5. Full Stack Developer resume

## 🌐 Running the App

Once you run `streamlit run app.py`, you'll see:

```
You can now view your Streamlit app in your browser.

Local URL: http://localhost:8501
Network URL: http://192.168.x.x:8501
```

## 📞 Need Help?

1. Check `SETUP.md` for detailed setup
2. Read `README.md` for full documentation
3. Run test script: `python test_parser.py`
4. Review `IMPLEMENTATION_SUMMARY.md` for features

## ✅ Checklist Before First Use

- [ ] Python 3.8+ installed
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] spaCy model downloaded
- [ ] Test script runs successfully
- [ ] Streamlit app starts without errors

---

**Ready to parse resumes?** Run `streamlit run app.py` and start uploading!
