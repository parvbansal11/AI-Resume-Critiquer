AI Resume Critiquer – Smart Resume Analyzer

Overview

The AI Resume Critiquer is a simple and interactive web application that helps users improve their resumes using Artificial Intelligence. Users can upload a PDF or TXT file, and the system instantly provides feedback on clarity, structure, skills, readability, and job-role relevance. This project demonstrates practical integration of Python, Streamlit, and OpenAI GPT models.

⸻

Features

	•	Upload resumes in PDF or TXT format
	•	AI-powered feedback using OpenAI GPT
	•	Evaluates clarity, skills, experience, and structure
	•	Highlights areas of improvement
	•	Simple and user-friendly interface built with Streamlit
	•	Secure API key handling through environment variables

⸻

Tech Stack

	•	Python 3.x
	•	Streamlit
	•	OpenAI API
	•	PyPDF2
	•	python-dotenv
	•	VS Code

⸻

Project Structure

AI-Resume-Critiquer/
│── app.py
│── requirements.txt
│── README.md
└── project file

⸻

How to Run Locally

1. Clone the repository

git clone https://github.com/parvbansal11/AI-Resume-Critiquer.git
cd AI-Resume-Critiquer

2. Create a virtual environment

python -m venv venv
source venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Add your OpenAI API key

Create a .env file and add:

OPENAI_API_KEY=your-key-here

5. Run the app

streamlit run app.py

⸻

Developer
Parv Bansal

⸻

Future Enhancements

	•	Resume scoring system
	•	Job description matching
	•	Support for DOCX files
	•	ATS optimization suggestions
	•	AI-generated resume templates
