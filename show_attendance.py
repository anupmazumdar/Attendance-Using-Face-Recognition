import pandas as pd
from glob import glob
import os
import tkinter
import csv
import tkinter as tk
from tkinter import *

def subjectchoose(text_to_speech):
    def calculate_attendance():
        Subject = tx.get()
        if Subject=="":
            t='Please enter the subject name.'
            text_to_speech(t)
    
        filenames = glob(
            f"Attendance\\{Subject}\\{Subject}*.csv"
        )
        df = [pd.read_csv(f) for f in filenames]
        newdf = df[0]
        for i in range(1, len(df)):
            newdf = newdf.merge(df[i], how="outer")
        newdf.fillna(0, inplace=True)
        newdf["Attendance"] = 0
        for i in range(len(newdf)):
            newdf["Attendance"].iloc[i] = str(int(round(newdf.iloc[i, 2:-1].mean() * 100)))+'%'
            #newdf.sort_values(by=['Enrollment'],inplace=True)
        newdf.to_csv(f"Attendance\\{Subject}\\attendance.csv", index=False)

        root = tkinter.Tk()
        root.title("Attendance of "+Subject)
        root.configure(background="#000000")
        cs = f"Attendance\\{Subject}\\attendance.csv"
        with open(cs) as file:
            reader = csv.reader(file)
            r = 0

            for col in reader:
                c = 0
                for row in col:

                    label = tkinter.Label(
                        root,
                        width=10,
                        height=1,
                        fg="#00FFFF",
                        font=("Segoe UI", 15, "bold"),
                        bg="#000000",
                        text=row,
                        relief=tkinter.RIDGE,
                    )
                    label.grid(row=r, column=c)
                    c += 1
                r += 1
        root.mainloop()
        print(newdf)

    subject = Tk()
    # windo.iconbitmap("AMS.ico")
    subject.title("Subject...")
    subject.geometry("580x320")
    subject.resizable(0, 0)
    subject.configure(background="#000000")
    # subject_logo = Image.open("UI_Image/0004.png")
    # subject_logo = subject_logo.resize((50, 47), Image.ANTIALIAS)
    # subject_logo1 = ImageTk.PhotoImage(subject_logo)
    titl = tk.Label(subject, bg="#000000", relief=RIDGE, bd=10, font=("Segoe UI", 30))
    titl.pack(fill=X)
    # l1 = tk.Label(subject, image=subject_logo1, bg="#000000",)
    # l1.place(x=100, y=10)
    titl = tk.Label(
        subject,
        text="Which Subject of Attendance?",
        bg="#000000",
        fg="#39FF14",
        font=("Segoe UI", 25, "bold"),
    )
    titl.place(x=50, y=15)

    def Attf():
        sub = tx.get()
        if sub == "":
            t="Please enter the subject name!!!"
            text_to_speech(t)
        else:
            os.startfile(
            f"Attendance\\{sub}"
            )


    attf = tk.Button(
        subject,
        text="Check Sheets",
        command=Attf,
        bd=7,
        font=("Segoe UI", 14, "bold"),
        bg="#000000",
        fg="#00FFFF",
        height=2,
        width=15,
        relief=RIDGE,
    )
    attf.place(x=300, y=180)

    sub = tk.Label(
        subject,
        text="Enter Subject",
        width=12,
        height=1,
        bg="#000000",
        fg="#00FFFF",
        bd=5,
        relief=RIDGE,
        font=("Segoe UI", 18, "bold"),
    )
    sub.place(x=40, y=105)

    tx = tk.Entry(
        subject,
        width=18,
        bd=5,
        bg="#000000",
        fg="#00FFFF",
        relief=RIDGE,
        font=("Segoe UI", 22, "bold"),
        insertbackground="#00FFFF"
    )
    tx.place(x=230, y=105)

    fill_a = tk.Button(
        subject,
        text="View Attendance",
        command=calculate_attendance,
        bd=7,
        font=("Segoe UI", 14, "bold"),
        bg="#000000",
        fg="#00FFFF",
        height=2,
        width=15,
        relief=RIDGE,
    )
    fill_a.place(x=80, y=180)
    subject.mainloop()
