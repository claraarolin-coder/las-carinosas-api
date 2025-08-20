#my-api-victims

The purpose of this API is to manage victim and case records using FastAPI and MongoDB.  

- Programming Language: Python 3.11
- Web Framework:FastAPI
- Database: MongoDB Atlas
- Version Control: Git + GitHub

Structure of the API
main.py # Entry point of the API
database.py 
requirements.txt # List of Python dependencies

models
- victim.py
- case.py

- schemas
- victim.py
  ─ case.py

- routes
- victim.py
  ─ case.py

API Endpoints
Victims
- "GET /victims" – Retrieve all victims
- "POST /victims" – Add a new victim

Cases
- "GET /cases" – Retrieve all cases
- "POST /cases" – Add a new case

Run locally:
   ```bash
   git clone https://github.com/claraarolin-coder/las-carinosas-api.git
   cd las-carinosas-api
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
http://localhost:8000/docs




