# AI-Based Resume Screening System (HR vs Student Matching)

## 📌 Project Overview

The **AI-Based Resume Screening System** is a web application that helps automate the resume screening process for recruiters.
Instead of manually reviewing hundreds of resumes, the system uses **Natural Language Processing (NLP)** and **Cosine Similarity** to compare resumes and determine how well a candidate matches the HR's requirements.

The system allows:

* **HR (Admin)** to upload a reference resume representing the desired job profile.
* **Students (Candidates)** to upload their resumes.
* The system automatically **compares student resumes with the HR resume**, calculates a **matching percentage**, and identifies the **top candidate**.

The application also provides **visual analytics (charts and graphs)** to make the results easier to understand.

---

# 🎯 Objectives

* Reduce manual effort in resume screening.
* Automatically match candidate resumes with job requirements.
* Rank candidates based on similarity score.
* Identify the **top candidate recommended for interview**.

---

# 👥 User Roles

## 1️⃣ HR (Admin)

* Register and login.
* Upload the **reference resume** (job requirement resume).
* View candidate comparison results.

## 2️⃣ Student (Candidate)

* Register and login.
* Upload one or more resumes.
* System compares student resumes with HR resume.

---

# ⚙️ Features

## 🔐 Authentication

* Single page **Login + Registration**
* Role-based users:

  * HR
  * Student
* Secure password storage using **hashing**

---

## 📤 Resume Upload System

* HR uploads **reference resume**
* Students upload their resumes
* Supports **PDF resumes**

---

## 🤖 AI Resume Analysis

The system performs:

1. **Resume text extraction**
2. **NLP processing**
3. **Skill extraction**
4. **Similarity scoring**

---

## 📊 Candidate Matching

Each student resume is compared with the HR resume using:

**Cosine Similarity**

The system calculates:


Matching Percentage


Example:


HR Resume vs Student Resume

Yuvaraj_resume.pdf → 89%
Abishek_resume.pdf → 76%
Rahul_resume.pdf → 68%


---

## 🏆 Top Candidate Recommendation

If multiple resumes are uploaded, the system finds the highest score:


Top Candidate: Yuvaraj (89% match)
Recommended for Interview


Below that, it displays **all candidate scores**.

---

## 📈 Data Visualization

The results page displays:

### 1️⃣ Pie Chart

Shows:


Match Percentage vs Remaining Percentage


### 2️⃣ Bar Graph

Displays comparison of all candidate scores.

---

## 🎨 UI Features

* Swiss-style modern UI
* Background images
* Professional dashboard design
* Green analytics theme
* Responsive layout

---

# 🧠 Technologies Used

### Backend

* Python
* Flask

### AI / NLP

* spaCy
* Cosine Similarity
* PyMuPDF (Resume text extraction)

### Database

* SQLite

### Frontend

* HTML
* CSS
* JavaScript
* Chart.js

---

# 📂 Project Folder Structure


ai_resume_screening
│
├── app.py
├── create_db.py
├── requirements.txt
│
├── instance
│   └── database.db
│
├── uploads
│   ├── resumes
│   └── hr_resume
│
├── app
│
│   ├── routes
│   │   ├── auth_routes.py
│   │   ├── resume_routes.py
│
│   ├── services
│   │   ├── resume_parser.py
│   │   ├── nlp_engine.py
│
│   ├── templates
│   │   ├── base.html
│   │   ├── login.html
│   │   ├── dashboard.html
│   │   ├── upload.html
│   │   └── results.html
│
│   └── static
│       ├── css
│       │   └── style.css
│       ├── images
│       └── js
│
└── README.md


---

# 🔄 System Workflow

### Step 1

HR registers and logs into the system.

### Step 2

HR uploads a **reference resume**.

### Step 3

HR logs out.

### Step 4

Students register and log in.

### Step 5

Students upload resumes.

### Step 6

The system compares student resumes with HR resume.

### Step 7

System calculates similarity scores.

### Step 8

Results page displays:

* Top candidate
* Candidate ranking
* Charts

---

# 📊 Example Output


Resume Matching Result

Top Candidate: Yuvaraj (89% match)
Recommended for Interview

All Resume Results

1 Yuvaraj_resume.pdf   89%
2 Abishek_resume.pdf   76%
3 Rahul_resume.pdf     68%


Charts displayed:

* Pie Chart (Match %)
* Bar Chart (Candidate ranking)

---

# ▶️ How to Run the Project

## 1️⃣ Clone or download the project


git clone <repository>


---

## 2️⃣ Create Virtual Environment


python -m venv venv


Activate:


venv\Scripts\activate


---

## 3️⃣ Install Dependencies


pip install -r requirements.txt


---

## 4️⃣ Create Database


python create_db.py


---

## 5️⃣ Run Application


python app.py


---

## 6️⃣ Open Browser


http://127.0.0.1:5000


---

# 🧪 Testing Scenario

### HR

1. Register as **HR**
2. Login
3. Upload HR resume
4. Logout

### Student

1. Register as **Student**
2. Login
3. Upload multiple resumes
4. System compares resumes and shows results

---

# 🚀 Future Improvements

Possible upgrades:

* AI **Skill Gap Analyzer**
* Resume **Keyword Matching**
* **AI Job Description Generator**
* **Top Candidate Leaderboard**
* Recruiter **Analytics Dashboard**
* Email notification to shortlisted candidates

---

# 📌 Conclusion

The **AI-Based Resume Screening System** simplifies the recruitment process by automatically analyzing resumes and identifying the most suitable candidates.

It reduces manual screening effort and provides **data-driven insights for HR decision-making**.

-> HR Register

<img width="1920" height="1080" alt="Screenshot 2026-03-08 140606" src="https://github.com/user-attachments/assets/750abba8-bf02-4c5f-80cd-68a997a0e405" />

-> HR login

<img width="1920" height="1080" alt="Screenshot 2026-03-08 140652" src="https://github.com/user-attachments/assets/55ef0b67-3459-4cae-80ab-59d32da9a8f4" />

-> Student login

<img width="1920" height="1080" alt="Screenshot 2026-03-08 140719" src="https://github.com/user-attachments/assets/97f09813-f93c-4d9d-9f03-b694592671f0" />

-> Dashboard

<img width="1920" height="1080" alt="Screenshot 2026-03-08 140741" src="https://github.com/user-attachments/assets/822f193a-6c7d-48e9-862b-1607767de1c5" />

-> File Uploading

<img width="1920" height="1080" alt="Screenshot 2026-03-08 140838" src="https://github.com/user-attachments/assets/cde0a195-c283-4a76-9a79-8b77a5f70e52" />

-> Final Result with Comparision

https://github.com/user-attachments/assets/40577fa9-c0ae-45e1-bbf7-f58f2f2fc94d







