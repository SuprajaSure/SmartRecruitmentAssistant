import streamlit as st
import pandas as pd
import plotly.express as px
import joblib

from predict import predict_candidate

# ---------------------------------------------------
# Page Configuration
# ---------------------------------------------------

st.set_page_config(
    page_title="Smart Recruitment Assistant",
    page_icon="💼",
    layout="wide"
)

# ---------------------------------------------------
# Title
# ---------------------------------------------------

st.title("💼 Smart Recruitment Assistant")
st.markdown("### AI Powered Candidate Screening System")

st.write("---")

# ---------------------------------------------------
# Sidebar
# ---------------------------------------------------

menu = st.sidebar.radio(
    "Navigation",
    [
        "Home",
        "Predict Candidate",
        "Upload Dataset",
        "Analytics Dashboard"
    ]
)

# ---------------------------------------------------
# HOME PAGE
# ---------------------------------------------------

if menu == "Home":

    st.header("Welcome")

    st.write("""
The Smart Recruitment Assistant is an AI-powered hiring support system.

It helps recruiters:

- Predict candidate selection
- Generate hiring scores
- Rank applicants
- Analyze recruitment trends
- Reduce manual screening effort

This project uses a Random Forest Machine Learning model.
""")

    st.subheader("Project Features")

    col1, col2 = st.columns(2)

    with col1:

        st.success("✔ Hiring Prediction")

        st.success("✔ Hiring Score")

        st.success("✔ Candidate Ranking")

        st.success("✔ HR Analytics")

    with col2:

        st.success("✔ Machine Learning")

        st.success("✔ Interactive Dashboard")

        st.success("✔ CSV Upload")

        st.success("✔ Data Visualization")

# ---------------------------------------------------
# PREDICT CANDIDATE
# ---------------------------------------------------

elif menu == "Predict Candidate":

    st.header("Predict Candidate")

    col1, col2 = st.columns(2)

    with col1:

        age = st.number_input(
            "Age",
            18,
            40,
            22
        )

        gender = st.selectbox(
            "Gender",
            ["Male", "Female"]
        )

        degree = st.selectbox(
            "Degree",
            [
                "B.Tech CSE",
                "B.Tech AIML",
                "B.Tech IT",
                "BCA",
                "MCA",
                "B.Sc Computer Science"
            ]
        )

        cgpa = st.slider(
            "CGPA",
            5.0,
            10.0,
            8.0
        )

        aptitude = st.slider(
            "Aptitude Score",
            0,
            100,
            70
        )

        communication = st.slider(
            "Communication Score",
            0,
            100,
            70
        )

    with col2:

        python = st.selectbox(
            "Python",
            [0,1]
        )

        java = st.selectbox(
            "Java",
            [0,1]
        )

        sql = st.selectbox(
            "SQL",
            [0,1]
        )

        powerbi = st.selectbox(
            "Power BI",
            [0,1]
        )

        excel = st.selectbox(
            "Excel",
            [0,1]
        )

        internships = st.slider(
            "Internships",
            0,
            5,
            1
        )

        projects = st.slider(
            "Projects",
            0,
            10,
            3
        )

        certifications = st.slider(
            "Certifications",
            0,
            10,
            2
        )

        experience = st.slider(
            "Experience (Years)",
            0,
            5,
            0
        )

    if st.button("Predict Hiring"):

        result = predict_candidate(
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
        )

        st.write("---")

        col1, col2, col3 = st.columns(3)

        with col1:

            st.metric(
                "Hiring Score",
                f"{result['Hiring Score']}%"
            )

        with col2:

            st.metric(
                "Prediction",
                result["Prediction"]
            )

        with col3:

            st.metric(
                "Category",
                result["Category"]
            )# ---------------------------------------------------
# UPLOAD DATASET
# ---------------------------------------------------

elif menu == "Upload Dataset":

    st.header("📂 Upload Candidate Dataset")

    uploaded_file = st.file_uploader(
        "Upload CSV File",
        type=["csv"]
    )

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        st.success("Dataset Uploaded Successfully!")

        st.subheader("Dataset Preview")

        st.dataframe(df)

        st.subheader("Dataset Information")

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric(
                "Total Candidates",
                len(df)
            )

        with col2:
            st.metric(
                "Columns",
                len(df.columns)
            )

        with col3:

            if "Selected" in df.columns:

                st.metric(
                    "Selected Candidates",
                    int(df["Selected"].sum())
                )

# ---------------------------------------------------
# ANALYTICS DASHBOARD
# ---------------------------------------------------

elif menu == "Analytics Dashboard":

    st.header("📊 Recruitment Analytics Dashboard")

    uploaded_file = st.file_uploader(
        "Upload Candidate Dataset",
        type=["csv"]
    )

    if uploaded_file is not None:

        df = pd.read_csv(uploaded_file)

        st.subheader("Dataset Preview")

        st.dataframe(df.head())

        st.write("---")

        # ------------------------
        # Hiring Status Pie Chart
        # ------------------------

        if "Selected" in df.columns:

            pie = px.pie(
                df,
                names="Selected",
                title="Selected vs Rejected Candidates"
            )

            st.plotly_chart(
                pie,
                use_container_width=True
            )

        # ------------------------
        # CGPA Distribution
        # ------------------------

        if "CGPA" in df.columns:

            fig = px.histogram(
                df,
                x="CGPA",
                nbins=20,
                title="CGPA Distribution"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        # ------------------------
        # Aptitude Distribution
        # ------------------------

        if "Aptitude" in df.columns:

            fig = px.histogram(
                df,
                x="Aptitude",
                nbins=20,
                title="Aptitude Score Distribution"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        # ------------------------
        # Communication Distribution
        # ------------------------

        if "Communication" in df.columns:

            fig = px.histogram(
                df,
                x="Communication",
                nbins=20,
                title="Communication Score Distribution"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        # ------------------------
        # Skills Chart
        # ------------------------

        skills = [
            "Python",
            "Java",
            "SQL",
            "PowerBI",
            "Excel"
        ]

        skill_count = {}

        for skill in skills:

            if skill in df.columns:

                skill_count[skill] = df[skill].sum()

        skill_df = pd.DataFrame({

            "Skill": skill_count.keys(),

            "Candidates": skill_count.values()

        })

        fig = px.bar(
            skill_df,
            x="Skill",
            y="Candidates",
            title="Technical Skills Distribution"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        # ------------------------
        # Candidate Ranking
        # ------------------------

        st.subheader("🏆 Candidate Ranking")

        if "Selected" in df.columns:

            df["Hiring Score"] = (
                df["CGPA"]*7
                + df["Python"]*8
                + df["Java"]*5
                + df["SQL"]*8
                + df["PowerBI"]*6
                + df["Excel"]*5
                + df["Internships"]*6
                + df["Projects"]*3
                + df["Certifications"]*2
                + df["Aptitude"]*0.4
                + df["Communication"]*0.3
                + df["Experience"]*8
            )

            df = df.sort_values(
                by="Hiring Score",
                ascending=False
            )

            df.insert(
                0,
                "Rank",
                range(1, len(df)+1)
            )

            st.dataframe(
                df[
                    [
                        "Rank",
                        "Name",
                        "Hiring Score",
                        "Selected"
                    ]
                ]
            )

            csv = df.to_csv(
                index=False
            ).encode("utf-8")

            st.download_button(

                "📥 Download Ranked Candidates",

                csv,

                "ranked_candidates.csv",

                "text/csv"

            )