# ResumeIQ 🎯

**AI-powered resume and job description matching system**

ResumeIQ analyzes a candidate's resume against a job description, extracts relevant information using an LLM, normalizes technical skills, and calculates a transparent skill-match score.

## ✨ Features

- 📄 **PDF Resume Parsing** — Extracts text from PDF resumes using `pypdf`
- 🤖 **AI-Powered Information Extraction** — Uses Groq LLM to extract structured candidate and job information
- 🧩 **Structured Data Validation** — Uses Pydantic models for reliable data handling
- 🔧 **Skill Normalization** — Converts variations such as `React.js` / `React` and `REST APIs` / `REST API` into standardized skill names
- 🎯 **Skill Matching** — Identifies matched and missing skills using deterministic Python logic
- 📊 **Match Score** — Calculates the percentage of required skills present in the candidate's resume
- 📦 **JSON Output** — Generates structured results suitable for further processing or integration

## 🔄 How It Works

```text
Resume PDF
    ↓
PDF Text Extraction
    ↓
Groq LLM
    ↓
Structured Resume Data
    ↓
Skill Normalization
    ↓
Skill Matching ← Job Description
    ↓
Matched Skills + Missing Skills
    ↓
Match Score
    ↓
JSON Output
```

## 🛠️ Tech Stack

| Technology | Purpose |
|------------|---------|
| Python | Core application logic |
| Groq LLM | Resume and job description extraction |
| Pydantic | Structured data validation |
| pypdf | PDF text extraction |
| JSON | Structured output |
| uv | Python project and dependency management |
| Git & GitHub | Version control |

## 📁 Project Structure

```text
ResumeIQ/
│
├── Resumematcher.py       # Main application
├── jd.txt                 # Sample job description
├── README.md              # Project documentation
├── pyproject.toml         # Project configuration
├── uv.lock                # Locked dependencies
├── .gitignore             # Ignored files and secrets
└── .python-version        # Python version configuration
```

> Personal resume files and environment variables are excluded from the repository using `.gitignore`.

## ⚙️ Setup

### 1. Clone the repository

```bash
git clone https://github.com/katherin915/ResumeIQ.git
cd ResumeIQ
```

### 2. Install dependencies

This project uses `uv` for dependency management.

```bash
uv sync
```

### 3. Configure the Groq API key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key
```

The `.env` file is intentionally excluded from Git using `.gitignore`.

### 4. Add a resume

Place a PDF resume in the project directory and update the file path in:

```python
text = extract_text_from_pdf("your_resume.pdf")
```

### 5. Add a job description

Update `jd.txt` with the job requirements you want to evaluate.

### 6. Run the application

```bash
uv run python Resumematcher.py
```

## 📊 Matching Logic

ResumeIQ uses deterministic Python logic for the final comparison rather than asking the LLM to calculate the score.

### Matched Skills

Skills present in both the resume and job requirements:

```python
matched_skills = [
    skill for skill in resume_skills
    if skill in required_skills
]
```

### Missing Skills

Required skills that are not present in the resume:

```python
missing_skills = [
    skill for skill in required_skills
    if skill not in resume_skills
]
```

### Match Score

```text
Match Score = (Matched Skills / Required Skills) × 100
```

For example:

```text
6 matched skills
6 required skills

6 / 6 × 100 = 100%
```

## 🧠 Design Approach

ResumeIQ separates **AI-based understanding** from **deterministic application logic**.

### LLM handles:

- Resume information extraction
- Job requirement extraction
- Skill normalization

### Python handles:

- Skill comparison
- Missing skill detection
- Match score calculation
- Final JSON generation

This makes the final score transparent and reproducible rather than relying on an LLM-generated score.

## 📤 Example Output

```json
{
  "candidate_name": "Candidate Name",
  "matched_skills": [
    "Python",
    "SQL",
    "FastAPI",
    "REST API",
    "MongoDB",
    "Git"
  ],
  "missing_skills": [],
  "score": 100.0
}
```

## 🚀 Future Improvements

- [ ] Support `.docx` resumes
- [ ] Support multiple resumes for batch screening
- [ ] Add recruiter-friendly web interface
- [ ] Add experience and education matching
- [ ] Add weighted skill scoring
- [ ] Generate personalized skill-gap recommendations
- [ ] Store candidate results in a database
- [ ] Add resume ranking for multiple candidates
- [ ] Add downloadable candidate reports

## 🎓 Learning Outcomes

This project demonstrates practical experience with:

- LLM API integration
- Prompt engineering
- Structured LLM outputs
- Pydantic data models
- PDF processing
- Data normalization
- Deterministic matching algorithms
- JSON serialization
- Environment variable management
- Git and GitHub workflows

## 👩‍💻 Author

**Katherin Pandey**

B.Tech CSE (AI/ML)  
Galgotias College of Engineering and Technology

---

⭐ If you found this project interesting, feel free to explore the repository and build upon it.