import os
import json
from pathlib import Path
from urllib import response
from dotenv import load_dotenv
from groq import Groq
from pypdf import PdfReader



load_dotenv()
my_api_key = os.getenv("GROQ_API_KEY")

if not my_api_key:
    raise ValueError("GROQ_API_KEY environment variable set nhi hai ulluu.")

client= Groq(api_key=my_api_key)

model="openai/gpt-oss-120b"




def extract_text_from_pdf(pdf_path):
    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        text += page.extract_text() or ""

    return text



from pydantic import BaseModel

class Resume(BaseModel):
    candidate_name:str
    email:str
    skills:list[str]
    education:str
    



schema =Resume.model_json_schema()


#HR requirements ko bhi schema me define kr skte hai
class JobRequirements(BaseModel):
    required_skills: list[str]


job_schema=JobRequirements.model_json_schema()

response_format={
    
    "type": "json_object"
}

def extract_structured_data(text, schema, instruction):
    system_prompt = f"""
    {instruction}

    Return the result according to this schema
    and in JSON format:

    {schema}
    """

    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": text
        }
    ]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        response_format={"type": "json_object"},
        temperature=0
    )

    return json.loads(response.choices[0].message.content)


text=extract_text_from_pdf("ResumeKatherin.pdf")


resume_data = extract_structured_data(
    text,
    schema,
    """
    Extract candidate_name, email, skills, and education from the resume.
    """
)

resume = Resume(**resume_data)



# # #inko aage pass kr skte hai 
# print(resume.candidate_name)
# print(resume.email)
# print(resume.skills)
# print(resume.education)


print("####################################################")




def read_job_description(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return file.read()

    
hr_text = read_job_description("jd.txt")

# job_data extract krenge ab structured form me 

job_data = extract_structured_data(
    hr_text,
    job_schema,
    """
    Extract only concrete technical skills from the job description.

    Do not include broad categories such as Backend Development
    or Database Systems.
    Do not invent skills that are not explicitly mentioned.
    """
)

job_requirements = JobRequirements(**job_data)

def calculate_match_score(resume_skills, required_skills):
    matched_skills=[skill for skill in resume_skills
                 if skill in required_skills]

    missing_skills=[skill for skill in required_skills
                    if skill not in resume_skills]

    score=len(matched_skills)/len(required_skills)*100

    
    return {
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "score": score
    }







def normalize_skills(skills):
    prompt = f"""
    Normalize the following technical skills into standard names.

    Rules:
    - Return only a JSON array.
    - Keep the meaning unchanged.
    - Merge common variations into one standard name.
    - Do not add skills that are not present.

    Skills:
    {skills}
    """

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )
    print("LLM RESPONSE:")
    print(response.choices[0].message.content)
    normalized_skills = json.loads(response.choices[0].message.content)

    return normalized_skills


normalized_resume_skills = normalize_skills(resume.skills)

normalized_required_skills = normalize_skills(
    job_requirements.required_skills
)
result=calculate_match_score(normalized_resume_skills, normalized_required_skills)
# print(result)

# print(type(result))
final_result = {
    "candidate_name": resume.candidate_name,
    "matched_skills": result["matched_skills"],
    "missing_skills": result["missing_skills"],
    "score": result["score"]
}

final_output = json.dumps(final_result, indent=2)

print(final_output)


#Homework 
# :Take a resume in pdf or word
#  have HR give you a list of requirements
#  extract them 
# match them 
#generate a score and give a final output in json format