import joblib
import pandas as pd

# -----------------------------
# Load Model
# -----------------------------
model = joblib.load("hiring_model.pkl")

label_encoders = joblib.load("label_encoders.pkl")

# -----------------------------
# Candidate Category
# -----------------------------
def get_category(score):

    if score >= 90:
        return "Excellent"

    elif score >= 80:
        return "Strong"

    elif score >= 65:
        return "Average"

    else:
        return "Needs Improvement"


# -----------------------------
# Predict Function
# -----------------------------
def predict_candidate(
    age,
    gender,
    degree,
    cgpa,
    python,
    java,
    sql,
    powerbi,
    excel,
    internships,
    projects,
    certifications,
    aptitude,
    communication,
    experience
):

    # Encode categorical values
    gender = label_encoders["Gender"].transform([gender])[0]
    degree = label_encoders["Degree"].transform([degree])[0]

    candidate = pd.DataFrame([[
        age,
        gender,
        degree,
        cgpa,
        python,
        java,
        sql,
        powerbi,
        excel,
        internships,
        projects,
        certifications,
        aptitude,
        communication,
        experience
    ]],
    columns=[
        "Age",
        "Gender",
        "Degree",
        "CGPA",
        "Python",
        "Java",
        "SQL",
        "PowerBI",
        "Excel",
        "Internships",
        "Projects",
        "Certifications",
        "Aptitude",
        "Communication",
        "Experience"
    ])

    prediction = model.predict(candidate)[0]

    probability = model.predict_proba(candidate)[0][1]

    hiring_score = round(probability * 100, 2)

    category = get_category(hiring_score)

    result = "Selected" if prediction == 1 else "Rejected"

    return {
        "Hiring Score": hiring_score,
        "Prediction": result,
        "Category": category
    }


# -----------------------------
# Example
# -----------------------------
if __name__ == "__main__":

    result = predict_candidate(
        age=22,
        gender="Female",
        degree="B.Tech AIML",
        cgpa=8.7,
        python=1,
        java=1,
        sql=1,
        powerbi=1,
        excel=1,
        internships=2,
        projects=5,
        certifications=3,
        aptitude=88,
        communication=85,
        experience=1
    )

    print(result)