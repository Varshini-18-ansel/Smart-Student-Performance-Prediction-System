import tkinter as tk
from tkinter import messagebox
import joblib


# =====================================================
# LOAD TRAINED MODEL
# =====================================================

try:

    model = joblib.load("model.pkl")
    encoder = joblib.load("encoder.pkl")

except FileNotFoundError:

    model = None
    encoder = None


# =====================================================
# MAIN WINDOW
# =====================================================

root = tk.Tk()

root.title(
    "Student Performance Prediction"
)

root.geometry(
    "650x800"
)

root.configure(
    bg="white"
)


# =====================================================
# VALIDATION FUNCTIONS
# =====================================================

def validate_name(value):

    if value == "":
        return True

    if value.replace(" ", "").isalpha():
        return True

    messagebox.showerror(
        "Invalid Input",
        "Student Name must contain letters only."
    )

    return False


def validate_register(value):

    if value == "":
        return True

    if value.isdigit():
        return True

    messagebox.showerror(
        "Invalid Input",
        "Register Number must contain numbers only."
    )

    return False


def validate_department(value):

    if value == "":
        return True

    if value.replace(" ", "").isalpha():
        return True

    messagebox.showerror(
        "Invalid Input",
        "Department must contain letters only."
    )

    return False


def validate_mark(value):

    if value == "":
        return True

    try:

        number = float(value)

    except ValueError:

        messagebox.showerror(
            "Invalid Input",
            "Please enter numbers only."
        )

        return False

    if number < 0 or number > 100:

        messagebox.showerror(
            "Invalid Input",
            "Mark must be between 0 and 100."
        )

        return False

    return True


# =====================================================
# VALIDATION COMMANDS
# =====================================================

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


# =====================================================
# HEADER
# =====================================================

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


# =====================================================
# STUDENT INFORMATION
# =====================================================

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
    pady=6,
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
    pady=6
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
    pady=6,
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
    pady=6
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
    pady=6,
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
    pady=6
)


# =====================================================
# ACADEMIC INFORMATION
# =====================================================

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
    pady=6,
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
    pady=6
)


# Internal Mark

tk.Label(
    academic_frame,
    text="Internal Mark",
    bg="#EDE7F6"
).grid(
    row=1,
    column=0,
    padx=8,
    pady=6,
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
    pady=6
)


# Assignment Mark

tk.Label(
    academic_frame,
    text="Assignment Mark",
    bg="#EDE7F6"
).grid(
    row=2,
    column=0,
    padx=8,
    pady=6,
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
    pady=6
)


# Exam Mark

tk.Label(
    academic_frame,
    text="Exam Mark",
    bg="#EDE7F6"
).grid(
    row=3,
    column=0,
    padx=8,
    pady=6,
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
    pady=6
)


# =====================================================
# RESULT VARIABLES
# =====================================================

prediction = tk.StringVar()

risk = tk.StringVar()

recommendation = tk.StringVar()


# =====================================================
# PREDICTION FUNCTION
# =====================================================

def calculate():

    # Check model

    if model is None:

        messagebox.showerror(
            "Model Not Found",
            "model.pkl not found.\n\n"
            "First run:\n"
            "python train_model.py"
        )

        return


    # Student Name

    if student_name.get().strip() == "":

        messagebox.showerror(
            "Missing Information",
            "Please enter Student Name."
        )

        student_name.focus()

        return


    # Register Number

    if reg_no.get().strip() == "":

        messagebox.showerror(
            "Missing Information",
            "Please enter Register Number."
        )

        reg_no.focus()

        return


    # Department

    if department.get().strip() == "":

        messagebox.showerror(
            "Missing Information",
            "Please enter Department."
        )

        department.focus()

        return


    # Attendance

    if attendance.get().strip() == "":

        messagebox.showerror(
            "Missing Information",
            "Please enter Attendance."
        )

        attendance.focus()

        return


    # Internal

    if internal.get().strip() == "":

        messagebox.showerror(
            "Missing Information",
            "Please enter Internal Mark."
        )

        internal.focus()

        return


    # Assignment

    if assignment.get().strip() == "":

        messagebox.showerror(
            "Missing Information",
            "Please enter Assignment Mark."
        )

        assignment.focus()

        return


    # Exam

    if exam.get().strip() == "":

        messagebox.showerror(
            "Missing Information",
            "Please enter Exam Mark."
        )

        exam.focus()

        return


    # =================================================
    # CONVERT INPUTS
    # =================================================

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
            "Please enter valid numbers."
        )

        return


    # =================================================
    # FOUR INPUT FEATURES
    # =================================================

    input_data = [[
        att,
        internal_mark,
        assignment_mark,
        exam_mark
    ]]


    # =================================================
    # RANDOM FOREST PREDICTION
    # =================================================

    try:

        predicted_value = model.predict(
            input_data
        )[0]

        result = encoder.inverse_transform(
            [predicted_value]
        )[0]

    except Exception as error:

        messagebox.showerror(
            "Prediction Error",
            str(error)
        )

        return


    # =================================================
    # DISPLAY RESULT
    # =================================================

    result = str(result).strip().lower()


    if result == "good":

        prediction.set(
            "Good Performance"
        )

        risk.set(
            "Low Risk"
        )

        recommendation.set(
            "Keep up the good performance."
        )


    elif result == "average":

        prediction.set(
            "Average Performance"
        )

        risk.set(
            "Medium Risk"
        )

        recommendation.set(
            "Improve your academic performance."
        )


    elif result == "poor":

        prediction.set(
            "Poor Performance"
        )

        risk.set(
            "High Risk"
        )

        recommendation.set(
            "Need immediate improvement."
        )


    else:

        prediction.set(
            result.title()
        )

        risk.set(
            "Monitor"
        )

        recommendation.set(
            "Continue monitoring academic performance."
        )


# =====================================================
# CLEAR FUNCTION
# =====================================================

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


# =====================================================
# BUTTONS
# =====================================================

button_frame = tk.Frame(
    root,
    bg="white"
)

button_frame.pack(
    pady=10
)


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


# =====================================================
# RESULT FRAME
# =====================================================

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
    pady=6,
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
    pady=6
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
    pady=6,
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
    pady=6
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
    pady=6,
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
    pady=6
)


# =====================================================
# RUN APPLICATION
# =====================================================

root.mainloop()