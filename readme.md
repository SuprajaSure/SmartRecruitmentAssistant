# 💼 Smart Recruitment Assistant

An AI-powered recruitment system that predicts whether a candidate is suitable for hiring using Machine Learning. The application helps recruiters screen candidates efficiently by generating hiring predictions, hiring scores, candidate rankings, and recruitment analytics through an interactive Streamlit dashboard.

---

## 📌 Project Overview

The Smart Recruitment Assistant is designed to automate the initial candidate screening process. Instead of manually evaluating every applicant, recruiters can enter candidate information or upload a dataset, and the application predicts whether a candidate should be selected.

The project uses a **Random Forest Classifier** trained on candidate information such as education, technical skills, internships, projects, certifications, aptitude, communication, and experience.

---

## ✨ Features

- 🤖 AI-Based Hiring Prediction
- 📊 Hiring Score Generation
- 🏆 Candidate Ranking
- 📁 Upload Candidate Dataset (CSV)
- 📈 Interactive Analytics Dashboard
- 📉 Recruitment Data Visualization
- 💾 Download Ranked Candidates
- ⚡ User-Friendly Streamlit Interface

---

## 🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Plotly
- Joblib

---

## 📂 Project Structure

```
Smart-Recruitment-Assistant/
│
├── app.py
├── predict.py
├── train_model.py
├── generate_dataset.py
├── candidates.csv
├── hiring_model.pkl
├── label_encoders.pkl
├── README.md
```

---

## 📊 Dataset Features

The model predicts hiring decisions using the following candidate attributes:

- Age
- Gender
- Degree
- CGPA
- Python Skill
- Java Skill
- SQL Skill
- Power BI Skill
- Excel Skill
- Internships
- Projects
- Certifications
- Aptitude Score
- Communication Score
- Experience

Target Variable:

- Selected (1 = Selected, 0 = Rejected)

---

## 🧠 Machine Learning Model

Algorithm Used:

**Random Forest Classifier**

Evaluation Metrics:

- Accuracy
- Precision
- Recall
- F1 Score
- Confusion Matrix
- Classification Report

---

## 📱 Application Modules

### 🏠 Home

Displays project information and key features.

### 👤 Predict Candidate

Allows recruiters to enter candidate details and receive:

- Hiring Score
- Hiring Prediction
- Candidate Category

### 📂 Upload Dataset

Upload a CSV file to preview candidate information and view basic dataset statistics.

### 📊 Analytics Dashboard

Provides interactive visualizations including:

- Selected vs Rejected Candidates
- CGPA Distribution
- Aptitude Distribution
- Communication Distribution
- Technical Skills Distribution
- Candidate Ranking

---

# 🚀 Installation

## 1. Clone the Repository

```bash
git clone https://github.com/yourusername/Smart-Recruitment-Assistant.git

cd Smart-Recruitment-Assistant
```

---

## 2. Create a Virtual Environment (Recommended)

### Windows

```bash
python -m venv venv
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install streamlit pandas numpy scikit-learn plotly joblib
```

---

# ▶️ Running the Project

## Step 1: Generate the Dataset (Optional)

```bash
python generate_dataset.py
```

---

## Step 2: Train the Machine Learning Model

```bash
python train_model.py
```

This creates:

- hiring_model.pkl
- label_encoders.pkl

---

## Step 3: Test the Prediction Module (Optional)

```bash
python predict.py
```

---

## Step 4: Launch the Streamlit Application

If your main file is named **app.py**

```bash
streamlit run app.py
```

If your file is still named **app.py**

```bash
streamlit run "app.py"
```

---

# 💻 Complete Command Sequence

```bash
python -m venv venv

venv\Scripts\activate

pip install streamlit pandas numpy scikit-learn plotly joblib

python generate_dataset.py

python train_model.py

python predict.py

streamlit run app.py
```

---

## 📈 Output

The application provides:

- Candidate Selection Prediction
- Hiring Score
- Candidate Category
- Recruitment Analytics Dashboard
- Candidate Ranking
- Download Ranked Candidate List

---

## 🔮 Future Enhancements

- Resume Parsing using OCR
- Resume PDF Upload
- Interview Recommendation System
- Explainable AI (SHAP/LIME)
- Candidate Resume Matching using NLP
- Recruiter Login Authentication
- Cloud Deployment
- Email Notifications

---

## 👩‍💻 Author

**Supraja Sure**

B.Tech Computer Science Engineering (Artificial Intelligence & Machine Learning)

---

## 📄 License

This project is developed for educational and academic purposes only.