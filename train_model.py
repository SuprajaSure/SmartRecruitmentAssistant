import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

# -----------------------------
# Load Dataset
# -----------------------------
df = pd.read_csv("candidates.csv")

print("Dataset Loaded Successfully")
print(df.head())

# -----------------------------
# Encode Categorical Columns
# -----------------------------
label_encoders = {}

categorical_columns = ["Gender", "Degree"]

for col in categorical_columns:
    le = LabelEncoder()
    df[col] = le.fit_transform(df[col])
    label_encoders[col] = le

# -----------------------------
# Features and Target
# -----------------------------
X = df.drop(columns=["Name", "Selected"])

y = df["Selected"]

# -----------------------------
# Train Test Split
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42,
    stratify=y
)

# -----------------------------
# Random Forest Model
# -----------------------------
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

# -----------------------------
# Predictions
# -----------------------------
y_pred = model.predict(X_test)

# -----------------------------
# Evaluation
# -----------------------------
print("\n========== MODEL PERFORMANCE ==========\n")

print("Accuracy : ", round(accuracy_score(y_test, y_pred) * 100, 2), "%")

print("Precision:", round(precision_score(y_test, y_pred), 3))

print("Recall   :", round(recall_score(y_test, y_pred), 3))

print("F1 Score :", round(f1_score(y_test, y_pred), 3))

print("\nConfusion Matrix")

print(confusion_matrix(y_test, y_pred))

print("\nClassification Report\n")

print(classification_report(y_test, y_pred))

# -----------------------------
# Save Model
# -----------------------------
joblib.dump(model, "hiring_model.pkl")

joblib.dump(label_encoders, "label_encoders.pkl")

print("\nModel Saved Successfully!")

# -----------------------------
# Feature Importance
# -----------------------------
importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\n========== FEATURE IMPORTANCE ==========\n")

print(importance)