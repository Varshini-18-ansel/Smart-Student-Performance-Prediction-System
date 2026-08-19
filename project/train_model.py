import pandas as pd
import pickle

from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


# ==========================================
# ACTIVITY 2 - DATA LOADING
# ==========================================

df = pd.read_csv("dataset.csv")

print("Dataset Loaded Successfully!")
print(df)


# ==========================================
# ACTIVITY 3 - DATA CLEANING
# ==========================================

print("\nMissing Values:")
print(df.isnull().sum())

# Remove missing values
df = df.dropna()

# Remove duplicate records
df = df.drop_duplicates()

print("\nData Types:")
print(df.dtypes)


# ==========================================
# CONVERT PERFORMANCE INTO NUMBERS
# ==========================================

encoder = LabelEncoder()

df["Performance"] = encoder.fit_transform(
    df["Performance"]
)


# ==========================================
# ACTIVITY 4 - MODEL TRAINING
# ==========================================

X = df[
    [
        "Attendance",
        "Internal_Mark",
        "Assignment_Mark",
        "Study_Hours"
    ]
]

y = df["Performance"]


# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create Logistic Regression model
model = LogisticRegression(
    max_iter=1000
)


# Train model
model.fit(X_train, y_train)

print("\nModel Training Completed!")


# ==========================================
# ACTIVITY 5 - MODEL EVALUATION
# ==========================================

y_pred = model.predict(X_test)

accuracy = accuracy_score(
    y_test,
    y_pred
)

print("\nModel Accuracy:")
print(accuracy * 100, "%")


# ==========================================
# ACTIVITY 6 - PREDICTION
# ==========================================

# New student details
new_student = [[
    85,   # Attendance
    80,   # Internal Mark
    85,   # Assignment Mark
    4     # Study Hours
]]


prediction = model.predict(
    new_student
)


# Convert number back to Performance
result = encoder.inverse_transform(
    prediction
)

print("\nNew Student Prediction:")
print(result[0])


# ==========================================
# ACTIVITY 7 - SAVE MODEL
# ==========================================

with open("model.pkl", "wb") as file:
    pickle.dump(model, file)


with open("encoder.pkl", "wb") as file:
    pickle.dump(encoder, file)


print("\nModel saved successfully!")
print("model.pkl created!")
print("encoder.pkl created!")