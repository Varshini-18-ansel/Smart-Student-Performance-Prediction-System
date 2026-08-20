import tkinter as tk
from tkinter import messagebox
import pandas as pd
import os

from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestClassifier


# =========================================================
# FILE NAMES
# =========================================================

CSV_FILE = "dataset.csv"
EXCEL_FILE = "student_analysis.xlsx"


# =========================================================
# LOAD DATASET
# =========================================================

try:

    data = pd.read_csv(CSV_FILE)

except FileNotFoundError:

    messagebox.showerror(
        "File Error",
        "dataset.csv not found!\n\n"
        "Place dataset.csv in the same folder as ui.py"
    )

    raise SystemExit


# =========================================================
# CHECK COLUMNS
# =========================================================

required_columns = [
    "Student_Name",
    "Register_Number",
    "Department",
    "Attendance",
    "Internal",
    "Assignment",
    "Exam",
    "Performance"
]

for column in required_columns:

    if column not in data.columns:

        messagebox.showerror(
            "Dataset Error",
            f"Missing column:\n{column}"
        )

        raise SystemExit


# =========================================================
# ML FEATURES
# =========================================================

X = data[
    [
        "Department",
        "Attendance",
        "Internal",
        "Assignment",
        "Exam"
    ]
]

y = data["Performance"]


# =========================================================
# PREPROCESSING
# =========================================================

preprocessor = ColumnTransformer(

    transformers=[

        (
            "department",
            OneHotEncoder(
                handle_unknown="ignore"
            ),
            ["Department"]
        ),

        (
            "numbers",
            "passthrough",
            [
                "Attendance",
                "Internal",
                "Assignment",
                "Exam"
            ]
        )
    ]
)


# =========================================================
# RANDOM FOREST MODEL
# =========================================================

model = Pipeline(

    steps=[

        (
            "preprocessor",
            preprocessor
        ),

        (
            "classifier",
            RandomForestClassifier(
                n_estimators=100,
                random_state=42
            )
        )
    ]
)


# =========================================================
# TRAIN MODEL
# =========================================================

model.fit(X, y)

print("Random Forest Model Trained Successfully")


# =========================================================
# MAIN WINDOW
# =========================================================

root = tk.Tk()

root.title(
    "Student Performance Prediction"
)

root.geometry(
    "650x850"
)

root.configure(
    bg="white"
)


# =========================================================
# VALIDATION FUNCTIONS
# =========================================================

def validate_name(new_value):

    if new_value == "":
        return True

    return new_value.replace(
        " ", ""
    ).isalpha()


def validate_register(new_value):

    if new_value == "":
        return True

    return new_value.isdigit()


def validate_department(new_value):

    if new_value == "":
        return True

    return new_value.replace(
        " ", ""
    ).isalpha()


def validate_mark(new_value):

    if new_value == "":
        return True

    try:

        value = float(new_value)

        return 0 <= value <= 100

    except ValueError:

        return False


# =========================================================
# VALIDATION COMMANDS
# =========================================================

vcmd_name = (
    root.register(validate_name),
    "%P"
)

vcmd_register = (
    root.register(validate_register),
    "%P"
)

vcmd_department = (
    root.register(validate_department),
    "%P"
)

vcmd_mark = (
    root.register(validate_mark),
    "%P"
)


# =========================================================
# HEADER
# =========================================================

header = tk.Frame(
    root,
    bg="#6A1B9A"
)

header.pack(
    fill="x",
    padx=15,
    pady=10
)

tk.Label(
    header,
    text="STUDENT PERFORMANCE PREDICTION",
    font=("Arial", 16, "bold"),
    bg="#6A1B9A",
    fg="white"
).pack(
    pady=12
)


# =========================================================
# STUDENT INFORMATION
# =========================================================

student_frame = tk.LabelFrame(
    root,
    text="Student Information",
    font=("Arial", 11, "bold"),
    bg="#EDE7F6",
    fg="#6A1B9A",
    padx=15,
    pady=8
)

student_frame.pack(
    fill="x",
    padx=15,
    pady=5
)


# Student Name

tk.Label(
    student_frame,
    text="Student Name",
    bg="#EDE7F6"
).grid(
    row=0,
    column=0,
    padx=8,
    pady=5,
    sticky="w"
)

student_name = tk.Entry(
    student_frame,
    width=25,
    validate="key",
    validatecommand=vcmd_name
)

student_name.grid(
    row=0,
    column=1,
    padx=8,
    pady=5
)


# Register Number

tk.Label(
    student_frame,
    text="Register Number",
    bg="#EDE7F6"
).grid(
    row=1,
    column=0,
    padx=8,
    pady=5,
    sticky="w"
)

reg_no = tk.Entry(
    student_frame,
    width=25,
    validate="key",
    validatecommand=vcmd_register
)

reg_no.grid(
    row=1,
    column=1,
    padx=8,
    pady=5
)


# Department

tk.Label(
    student_frame,
    text="Department",
    bg="#EDE7F6"
).grid(
    row=2,
    column=0,
    padx=8,
    pady=5,
    sticky="w"
)

department = tk.Entry(
    student_frame,
    width=25,
    validate="key",
    validatecommand=vcmd_department
)

department.grid(
    row=2,
    column=1,
    padx=8,
    pady=5
)


# =========================================================
# ACADEMIC INFORMATION
# =========================================================

academic_frame = tk.LabelFrame(
    root,
    text="Academic Information",
    font=("Arial", 11, "bold"),
    bg="#EDE7F6",
    fg="#6A1B9A",
    padx=15,
    pady=8
)

academic_frame.pack(
    fill="x",
    padx=15,
    pady=5
)


# Attendance

tk.Label(
    academic_frame,
    text="Attendance (%)",
    bg="#EDE7F6"
).grid(
    row=0,
    column=0,
    padx=8,
    pady=5,
    sticky="w"
)

attendance = tk.Entry(
    academic_frame,
    width=25,
    validate="key",
    validatecommand=vcmd_mark
)

attendance.grid(
    row=0,
    column=1,
    padx=8,
    pady=5
)


# Internal

tk.Label(
    academic_frame,
    text="Internal Mark",
    bg="#EDE7F6"
).grid(
    row=1,
    column=0,
    padx=8,
    pady=5,
    sticky="w"
)

internal = tk.Entry(
    academic_frame,
    width=25,
    validate="key",
    validatecommand=vcmd_mark
)

internal.grid(
    row=1,
    column=1,
    padx=8,
    pady=5
)


# Assignment

tk.Label(
    academic_frame,
    text="Assignment Mark",
    bg="#EDE7F6"
).grid(
    row=2,
    column=0,
    padx=8,
    pady=5,
    sticky="w"
)

assignment = tk.Entry(
    academic_frame,
    width=25,
    validate="key",
    validatecommand=vcmd_mark
)

assignment.grid(
    row=2,
    column=1,
    padx=8,
    pady=5
)


# Exam

tk.Label(
    academic_frame,
    text="Exam Mark",
    bg="#EDE7F6"
).grid(
    row=3,
    column=0,
    padx=8,
    pady=5,
    sticky="w"
)

exam = tk.Entry(
    academic_frame,
    width=25,
    validate="key",
    validatecommand=vcmd_mark
)

exam.grid(
    row=3,
    column=1,
    padx=8,
    pady=5
)


# =========================================================
# RESULT VARIABLES
# =========================================================

prediction = tk.StringVar(
    value=""
)

risk = tk.StringVar(
    value=""
)

recommendation = tk.StringVar(
    value=""
)


# =========================================================
# CALCULATE / PREDICT
# =========================================================

def calculate():

    # Check name

    if student_name.get().strip() == "":

        messagebox.showerror(
            "Missing Information",
            "Please enter Student Name."
        )

        student_name.focus()

        return


    # Check register number

    if reg_no.get().strip() == "":

        messagebox.showerror(
            "Missing Information",
            "Please enter Register Number."
        )

        reg_no.focus()

        return


    # Check department

    if department.get().strip() == "":

        messagebox.showerror(
            "Missing Information",
            "Please enter Department."
        )

        department.focus()

        return


    # Check attendance

    if attendance.get().strip() == "":

        messagebox.showerror(
            "Missing Information",
            "Please enter Attendance."
        )

        attendance.focus()

        return


    # Check internal

    if internal.get().strip() == "":

        messagebox.showerror(
            "Missing Information",
            "Please enter Internal Mark."
        )

        internal.focus()

        return


    # Check assignment

    if assignment.get().strip() == "":

        messagebox.showerror(
            "Missing Information",
            "Please enter Assignment Mark."
        )

        assignment.focus()

        return


    # Check exam

    if exam.get().strip() == "":

        messagebox.showerror(
            "Missing Information",
            "Please enter Exam Mark."
        )

        exam.focus()

        return


    # Convert marks

    try:

        att = float(
            attendance.get()
        )

        internal_mark = float(
            internal.get()
        )

        assignment_mark = float(
            assignment.get()
        )

        exam_mark = float(
            exam.get()
        )

    except ValueError:

        messagebox.showerror(
            "Invalid Input",
            "Please enter valid marks."
        )

        return


    # =====================================================
    # NEW STUDENT INPUT
    # =====================================================

    new_student = pd.DataFrame(

        {
            "Department": [
                department.get().strip()
            ],

            "Attendance": [
                att
            ],

            "Internal": [
                internal_mark
            ],

            "Assignment": [
                assignment_mark
            ],

            "Exam": [
                exam_mark
            ]
        }
    )


    # =====================================================
    # RANDOM FOREST PREDICTION
    # =====================================================

    result = model.predict(
        new_student
    )[0]


    prediction.set(
        result + " Performance"
    )


    # Risk + Recommendation

    if result == "Good":

        risk.set(
            "Low Risk"
        )

        recommendation.set(
            "Keep up the good performance"
        )


    elif result == "Average":

        risk.set(
            "Medium Risk"
        )

        recommendation.set(
            "Improve your academic performance"
        )


    else:

        risk.set(
            "High Risk"
        )

        recommendation.set(
            "Need immediate improvement"
        )


    print(
        "Prediction:",
        prediction.get()
    )


# =========================================================
# SAVE
# =========================================================

def save_student():

    # Calculate first

    if prediction.get() == "":

        messagebox.showerror(
            "Save Error",
            "Please click Calculate first."
        )

        return


    try:

        # =================================================
        # CREATE NEW ROW
        # =================================================

        new_row = pd.DataFrame(

            [
                {

                    "Student_Name":
                        student_name.get().strip(),

                    "Register_Number":
                        reg_no.get().strip(),

                    "Department":
                        department.get().strip(),

                    "Attendance":
                        float(
                            attendance.get()
                        ),

                    "Internal":
                        float(
                            internal.get()
                        ),

                    "Assignment":
                        float(
                            assignment.get()
                        ),

                    "Exam":
                        float(
                            exam.get()
                        ),

                    "Performance":
                        prediction.get().replace(
                            " Performance",
                            ""
                        )
                }
            ]
        )


        # =================================================
        # READ ORIGINAL CSV
        # =================================================

        old_data = pd.read_csv(
            CSV_FILE
        )


        # =================================================
        # ADD NEW STUDENT AT LAST
        # =================================================

        final_data = pd.concat(

            [
                old_data,
                new_row
            ],

            ignore_index=True
        )


        # =================================================
        # SAVE BACK TO CSV
        # =================================================

        final_data.to_csv(

            CSV_FILE,

            index=False
        )


        # =================================================
        # SAVE SAME DATA TO EXCEL
        # =================================================

        final_data.to_excel(

            EXCEL_FILE,

            index=False
        )


        messagebox.showinfo(

            "Saved Successfully",

            "New student added successfully!\n\n"

            "CSV updated:\n"
            "dataset.csv\n\n"

            "Excel created/updated:\n"
            "student_analysis.xlsx"
        )


        print(
            "New student saved successfully."
        )


    except PermissionError:

        messagebox.showerror(

            "File Error",

            "Please close dataset.csv or\n"
            "student_analysis.xlsx if opened."
        )


    except Exception as e:

        messagebox.showerror(

            "Save Error",

            str(e)
        )


# =========================================================
# CLEAR
# =========================================================

def clear():

    student_name.delete(
        0,
        tk.END
    )

    reg_no.delete(
        0,
        tk.END
    )

    department.delete(
        0,
        tk.END
    )

    attendance.delete(
        0,
        tk.END
    )

    internal.delete(
        0,
        tk.END
    )

    assignment.delete(
        0,
        tk.END
    )

    exam.delete(
        0,
        tk.END
    )


    prediction.set("")

    risk.set("")

    recommendation.set("")


# =========================================================
# BUTTONS
# =========================================================

button_frame = tk.Frame(
    root,
    bg="white"
)

button_frame.pack(
    pady=8
)


# Calculate

tk.Button(

    button_frame,

    text="Calculate",

    width=12,

    bg="#6A1B9A",

    fg="white",

    font=("Arial", 10, "bold"),

    command=calculate

).pack(

    side="left",

    padx=5
)


# SAVE BUTTON

tk.Button(

    button_frame,

    text="Save",

    width=12,

    bg="#4CAF50",

    fg="white",

    font=("Arial", 10, "bold"),

    command=save_student

).pack(

    side="left",

    padx=5
)


# Clear

tk.Button(

    button_frame,

    text="Clear",

    width=12,

    bg="#D8BFE8",

    fg="#6A1B9A",

    font=("Arial", 10, "bold"),

    command=clear

).pack(

    side="left",

    padx=5
)


# Exit

tk.Button(

    button_frame,

    text="Exit",

    width=12,

    bg="#6A1B9A",

    fg="white",

    font=("Arial", 10, "bold"),

    command=root.destroy

).pack(

    side="left",

    padx=5
)


# =========================================================
# RESULT FRAME
# =========================================================

result_frame = tk.LabelFrame(

    root,

    text="Prediction Results",

    font=("Arial", 11, "bold"),

    bg="#EDE7F6",

    fg="#6A1B9A",

    padx=15,

    pady=10

)

result_frame.pack(

    fill="x",

    padx=15,

    pady=5
)


# Prediction

tk.Label(

    result_frame,

    text="Prediction",

    bg="#EDE7F6",

    font=("Arial", 10, "bold")

).grid(

    row=0,

    column=0,

    padx=8,

    pady=5,

    sticky="w"
)


tk.Label(

    result_frame,

    textvariable=prediction,

    bg="white",

    fg="#6A1B9A",

    font=("Arial", 10, "bold"),

    width=30,

    anchor="w"

).grid(

    row=0,

    column=1,

    padx=8,

    pady=5
)


# Risk

tk.Label(

    result_frame,

    text="Risk Level",

    bg="#EDE7F6",

    font=("Arial", 10, "bold")

).grid(

    row=1,

    column=0,

    padx=8,

    pady=5,

    sticky="w"
)


tk.Label(

    result_frame,

    textvariable=risk,

    bg="white",

    fg="#6A1B9A",

    font=("Arial", 10, "bold"),

    width=30,

    anchor="w"

).grid(

    row=1,

    column=1,

    padx=8,

    pady=5
)


# Recommendation

tk.Label(

    result_frame,

    text="Recommendation",

    bg="#EDE7F6",

    font=("Arial", 10, "bold")

).grid(

    row=2,

    column=0,

    padx=8,

    pady=5,

    sticky="nw"
)


tk.Label(

    result_frame,

    textvariable=recommendation,

    bg="white",

    fg="#6A1B9A",

    font=("Arial", 10, "bold"),

    width=30,

    height=2,

    anchor="nw",

    justify="left",

    wraplength=220

).grid(

    row=2,

    column=1,

    padx=8,

    pady=5
)


# =========================================================
# RUN
# =========================================================

root.mainloop()