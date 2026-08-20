import pandas as pd


# =====================================================
# 20 STUDENT DATA
# =====================================================

data = {

    # ---------------- STUDENT NAME ----------------

    "Student_Name": [
        "Arun",
        "Bala",
        "Divya",
        "Harini",
        "Kavin",
        "Meena",
        "Naveen",
        "Priya",
        "Rahul",
        "Sanjay",
        "Sneha",
        "Surya",
        "Varun",
        "Vishnu",
        "Yamini",
        "Keerthana",
        "Dinesh",
        "Anitha",
        "Gokul",
        "Nithya"
    ],


    # ---------------- REGISTER NUMBER ----------------

    "Register_Number": [
        1001,
        1002,
        1003,
        1004,
        1005,
        1006,
        1007,
        1008,
        1009,
        1010,
        1011,
        1012,
        1013,
        1014,
        1015,
        1016,
        1017,
        1018,
        1019,
        1020
    ],


    # ---------------- DEPARTMENT ----------------

    "Department": [
        "CSE",
        "ECE",
        "EEE",
        "IT",
        "MECH",
        "CIVIL",
        "AIDS",
        "AIML",
        "CSE",
        "ECE",
        "EEE",
        "IT",
        "MECH",
        "CIVIL",
        "AIDS",
        "AIML",
        "CSE",
        "ECE",
        "EEE",
        "IT"
    ],


    # ---------------- ATTENDANCE ----------------

    "Attendance": [
        95,
        88,
        76,
        65,
        92,
        58,
        81,
        72,
        45,
        89,
        67,
        94,
        52,
        78,
        85,
        48,
        91,
        62,
        70,
        97
    ],


    # ---------------- INTERNAL MARK ----------------

    "Internal": [
        92,
        85,
        78,
        62,
        90,
        55,
        82,
        70,
        42,
        87,
        65,
        95,
        48,
        75,
        84,
        45,
        89,
        60,
        68,
        96
    ],


    # ---------------- ASSIGNMENT MARK ----------------

    "Assignment": [
        95,
        88,
        80,
        65,
        93,
        58,
        85,
        74,
        40,
        90,
        68,
        96,
        50,
        78,
        87,
        42,
        92,
        64,
        72,
        98
    ],


    # ---------------- EXAM MARK ----------------

    "Exam": [
        94,
        86,
        75,
        60,
        91,
        52,
        80,
        71,
        38,
        88,
        63,
        97,
        45,
        76,
        83,
        40,
        90,
        58,
        69,
        95
    ],


    # ---------------- PERFORMANCE ----------------

    "Performance": [
        "Good",
        "Good",
        "Good",
        "Average",
        "Good",
        "Poor",
        "Good",
        "Average",
        "Poor",
        "Good",
        "Average",
        "Good",
        "Poor",
        "Average",
        "Good",
        "Poor",
        "Good",
        "Average",
        "Average",
        "Good"
    ]
}


# =====================================================
# CREATE DATAFRAME
# =====================================================

df = pd.DataFrame(data)


# =====================================================
# SAVE CSV FILE
# =====================================================

df.to_csv(
    "dataset.csv",
    index=False
)


# =====================================================
# DISPLAY DATA
# =====================================================

print("\n==========================================")
print("       STUDENT DATASET CREATED")
print("==========================================")

print(df.to_string(index=False))

print("\n==========================================")
print("Total Students :", len(df))
print("CSV File       : dataset.csv")
print("==========================================")

print("\nDataset created successfully!")