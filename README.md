# ResumeIQ – AI Resume Matcher

ResumeIQ is an AI-powered resume screening and candidate ranking system that analyzes a job description against multiple resumes and generates an explainable match score for each candidate.

It uses an LLM to extract structured information from job descriptions and resumes, evaluates candidate-job compatibility, and automatically ranks candidates based on their match scores.

## Features

* 📄 Supports multiple **PDF and DOCX resumes**
* 🧠 AI-powered resume parsing using **Groq LLM**
* 💼 Automatic **job description analysis**
* 🔍 Extracts required and preferred skills, education, experience, and responsibilities
* 👤 Extracts candidate information, skills, education, experience, projects, and certifications
* ⚖️ AI-based resume-to-job matching
* 📊 Generates an overall **match score from 0–100**
* 🔎 Identifies matching and missing important skills
* 🏆 Automatically ranks candidates based on their scores
* 📋 Displays the **Top 2** and **Lowest 2** candidates
* 🧩 Uses Pydantic models for structured and validated data
* 📦 Supports both PDF and DOCX document parsing

## Tech Stack

* **Python**
* **Groq LLM API**
* **Pydantic**
* **pypdf**
* **python-docx**
* **python-dotenv**
* **uv** for dependency and environment management

## Project Structure

```text
ResumeIQ/
│
├── resumeiq.py
├── jd.txt
├── resumes/
│   └── .gitkeep
├── README.md
├── pyproject.toml
├── uv.lock
└── .gitignore
```

## How It Works

```text
Job Description
       ↓
AI Job Description Parser
       ↓
Required / Preferred Skills
Education / Experience / Responsibilities
       ↓
Multiple Resumes
       ↓
PDF / DOCX Text Extraction
       ↓
AI Resume Parser
       ↓
Structured Candidate Information
       ↓
Resume ↔ Job Matching
       ↓
Match Score + Matching Details
       ↓
Candidate Ranking
       ↓
Top 2 / Lowest 2 Candidates
```

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/katherin915/ResumeIQ.git
cd ResumeIQ
```

### 2. Install dependencies

Make sure Python 3.11+ and `uv` are installed.

```bash
uv sync
```

### 3. Add your Groq API key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_api_key_here
```

Do not commit your `.env` file or expose your API key publicly.

## Adding a Job Description

Open:

```text
jd.txt
```

Replace its contents with the job description you want to analyze.

You can use a job description from any company or role.

## Adding Resumes

Place the resumes you want to screen inside:

```text
resumes/
```

Supported formats:

```text
.pdf
.docx
```

For example:

```text
resumes/
├── candidate1.pdf
├── candidate2.pdf
├── candidate3.docx
└── candidate4.pdf
```

Personal resume files are ignored by Git through `.gitignore` and should not be uploaded to the public repository.

## Run the Project

From the project directory:

```bash
uv run python resumeiq.py
```

ResumeIQ will process all supported resumes in the `resumes/` directory and compare them against the job description in `jd.txt`.

## Example Output

```text
Top 2 candidates

Candidate A - 91.5 %
{
    "matching_skills": [...],
    "missing_important_skills": [...],
    "experience_requirement_met": true,
    "verdict": "Strong match"
}

Candidate B - 84.0 %
{
    ...
}

LOWEST 2 CANDIDATES

Candidate D - 62.5 %
Candidate E - 48.0 %
```

## Key Components

### Job Description Parser

The system uses an LLM to convert an unstructured job description into structured information such as:

* Role
* Required skills
* Preferred skills
* Minimum experience
* Education requirements
* Responsibilities

### Resume Parser

ResumeIQ extracts meaningful information from resumes even when different resumes use different section headings.

It identifies:

* Candidate name
* Email
* Phone
* Education
* Experience
* Skills
* Projects
* Certifications

### Candidate Matching

Each parsed resume is compared against the job requirements.

The system evaluates:

* Skill compatibility
* Important missing skills
* Experience requirements
* Overall candidate-job compatibility

A match score between **0 and 100** is generated for every candidate.

### Candidate Ranking

After processing all resumes, candidates are sorted by their match score.

The system displays:

* 🏆 Top 2 candidates
* 📉 Lowest 2 candidates

This makes the project useful as a basic automated resume screening and candidate prioritization tool.

## Security

* API keys are stored using environment variables.
* `.env` files are excluded from Git.
* Personal PDF/DOCX resumes inside `resumes/` are excluded from Git.
* Do not upload confidential candidate information to a public repository.

## Future Improvements

* Web-based interface for uploading resumes and job descriptions
* Resume ranking dashboard
* CSV/JSON export of candidate results
* More detailed scoring breakdown
* Batch processing optimization
* Support for additional document formats
* Authentication and secure resume storage

## Author

**Katherin Pandey**

B.Tech CSE (AI/ML) | 2027

GitHub: https://github.com/katherin915

---

⭐ If you find this project useful, consider giving the repository a star.
