import tkinter as tk
from tkinter import messagebox

# MAIN WINDOW 

root = tk.Tk()
root.title("Student Performance Prediction")
root.geometry("650x750")
root.configure(bg="white")

# HEADER 

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
).pack(pady=12)


# STUDENT INFORMATION 

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


tk.Label(
    student_frame,
    text="Student Name",
    bg="#EDE7F6"
).grid(row=0, column=0, padx=8, pady=5, sticky="w")

student_name = tk.Entry(
    student_frame,
    width=25
)

student_name.grid(
    row=0,
    column=1,
    padx=8,
    pady=5
)


tk.Label(
    student_frame,
    text="Register Number",
    bg="#EDE7F6"
).grid(row=1, column=0, padx=8, pady=5, sticky="w")

reg_no = tk.Entry(
    student_frame,
    width=25
)

reg_no.grid(
    row=1,
    column=1,
    padx=8,
    pady=5
)


tk.Label(
    student_frame,
    text="Department",
    bg="#EDE7F6"
).grid(row=2, column=0, padx=8, pady=5, sticky="w")

department = tk.Entry(
    student_frame,
    width=25
)

department.grid(
    row=2,
    column=1,
    padx=8,
    pady=5
)


#  ACADEMIC INFORMATION

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


tk.Label(
    academic_frame,
    text="Attendance (%)",
    bg="#EDE7F6"
).grid(row=0, column=0, padx=8, pady=5, sticky="w")

attendance = tk.Entry(
    academic_frame,
    width=25
)

attendance.grid(
    row=0,
    column=1,
    padx=8,
    pady=5
)


tk.Label(
    academic_frame,
    text="Internal Mark",
    bg="#EDE7F6"
).grid(row=1, column=0, padx=8, pady=5, sticky="w")

internal = tk.Entry(
    academic_frame,
    width=25
)

internal.grid(
    row=1,
    column=1,
    padx=8,
    pady=5
)


tk.Label(
    academic_frame,
    text="Assignment Mark",
    bg="#EDE7F6"
).grid(row=2, column=0, padx=8, pady=5, sticky="w")

assignment = tk.Entry(
    academic_frame,
    width=25
)

assignment.grid(
    row=2,
    column=1,
    padx=8,
    pady=5
)


# ================= RESULT VARIABLES =================

prediction = tk.StringVar(value="")
risk = tk.StringVar(value="")
recommendation = tk.StringVar(value="")


# CALCULATE

def calculate():

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
            "Please enter Attendance Percentage."
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


    # Convert values

    try:

        att = float(attendance.get())
        internal_mark = float(internal.get())
        assignment_mark = float(assignment.get())

    except ValueError:

        messagebox.showerror(
            "Invalid Input",
            "Please enter numbers only."
        )

        return


    # Range validation

    if att < 0 or att > 100:

        messagebox.showerror(
            "Invalid Input",
            "Attendance must be between 0 and 100."
        )

        attendance.focus()
        return


    if internal_mark < 0 or internal_mark > 100:

        messagebox.showerror(
            "Invalid Input",
            "Internal Mark must be between 0 and 100."
        )

        internal.focus()
        return


    if assignment_mark < 0 or assignment_mark > 100:

        messagebox.showerror(
            "Invalid Input",
            "Assignment Mark must be between 0 and 100."
        )

        assignment.focus()
        return


    # AVERAGE

    average = (
        att +
        internal_mark +
        assignment_mark
    ) / 3


    #  PREDICTION 

    if average >= 75:

        prediction.set("Good Performance")
        risk.set("Low Risk")
        recommendation.set(
            "Keep up the good performance"
        )

    elif average >= 50:

        prediction.set("Average Performance")
        risk.set("Medium Risk")
        recommendation.set(
            "Improve your academic performance"
        )

    else:

        prediction.set("Poor Performance")
        risk.set("High Risk")
        recommendation.set(
            "Need immediate improvement"
        )


# CLEAR 

def clear():

    student_name.delete(0, tk.END)
    reg_no.delete(0, tk.END)
    department.delete(0, tk.END)

    attendance.delete(0, tk.END)
    internal.delete(0, tk.END)
    assignment.delete(0, tk.END)

    prediction.set("")
    risk.set("")
    recommendation.set("")


# BUTTONS 

button_frame = tk.Frame(
    root,
    bg="white"
)

button_frame.pack(pady=8)


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


# PREDICTION RESULTS 

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
root.mainloop()