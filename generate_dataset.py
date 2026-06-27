import pandas as pd
import numpy as np
import random

np.random.seed(42)
random.seed(42)

names = [
    "Rahul","Priya","Amit","Sneha","Rohan","Anjali","Kiran","Arjun",
    "Meera","Vikram","Neha","Suresh","Pooja","Varun","Akash","Divya",
    "Nikhil","Harsha","Sai","Kavya","Ritika","Aditya","Shreya",
    "Manoj","Keerthi","Ashwin","Bhavana","Tarun","Anusha","Yash"
]

degrees = [
    "B.Tech CSE",
    "B.Tech AIML",
    "B.Tech IT",
    "BCA",
    "MCA",
    "B.Sc Computer Science"
]

genders = [
    "Male",
    "Female"
]

rows = []

for i in range(500):

    name = random.choice(names) + " " + random.choice(
        ["Kumar","Reddy","Sharma","Patel","Gupta","Naidu","Rao"]
    )

    age = random.randint(20,30)

    gender = random.choice(genders)

    degree = random.choice(degrees)

    cgpa = round(np.random.uniform(5.5,9.9),2)

    python = random.randint(0,1)

    java = random.randint(0,1)

    sql = random.randint(0,1)

    powerbi = random.randint(0,1)

    excel = random.randint(0,1)

    internships = random.randint(0,3)

    projects = random.randint(1,8)

    certifications = random.randint(0,6)

    aptitude = random.randint(40,100)

    communication = random.randint(45,100)

    experience = random.randint(0,3)

    score = (
        cgpa*7 +
        python*8 +
        java*5 +
        sql*8 +
        powerbi*6 +
        excel*5 +
        internships*6 +
        projects*3 +
        certifications*2 +
        aptitude*0.4 +
        communication*0.3 +
        experience*8
    )

    selected = 1 if score >= 120 else 0

    rows.append([
        name,
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
        experience,
        selected
    ])

columns = [
    "Name",
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
    "Experience",
    "Selected"
]

df = pd.DataFrame(rows, columns=columns)

df.to_csv("candidates.csv", index=False)

print("Dataset Generated Successfully!")
print(df.head())
print()
print(df["Selected"].value_counts())