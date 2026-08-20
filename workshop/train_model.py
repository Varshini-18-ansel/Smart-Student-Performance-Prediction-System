import pandas as pd
import joblib

from sklearn.ensemble import RandomForestClassifier


# =====================================================
# FILE
# =====================================================

CSV_FILE = "dataset.csv"
MODEL_FILE = "model.pkl"


# =====================================================
# FEATURES
# EXACTLY 4 INPUT FEATURES
# =====================================================

FEATURES = [
    "Attendance",
    "Internal",
    "Assignment",
    "Exam"
]

TARGET = "Performance"


# =====================================================
# READ DATASET
# =====================================================

data = pd.read_csv(CSV_FILE)


# =====================================================
# CHECK COLUMNS
# =====================================================

required_columns = FEATURES + [TARGET]

for column in required_columns:

    if column not in data.columns:

        raise ValueError(
            f"Missing column in dataset: {column}"
        )


# =====================================================
# INPUT AND OUTPUT
# =====================================================

X = data[FEATURES]

y = data[TARGET]


# =====================================================
# RANDOM FOREST
# =====================================================

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)


# =====================================================
# TRAIN
# =====================================================

model.fit(X, y)


# =====================================================
# SAVE MODEL
# =====================================================

joblib.dump(model, MODEL_FILE)


# =====================================================
# OUTPUT
# =====================================================

print("-----------------------------------")
print("MODEL TRAINING SUCCESSFUL")
print("-----------------------------------")

print("Algorithm : Random Forest")

print("Features  :")
print("1. Attendance")
print("2. Internal")
print("3. Assignment")
print("4. Exam")

print("\nTarget:")
print("Performance")

print("\nClasses:")
print(model.classes_)

print("\nModel saved as:", MODEL_FILE)

print("-----------------------------------")