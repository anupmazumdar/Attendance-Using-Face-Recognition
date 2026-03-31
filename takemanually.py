import tkinter as tk
from tkinter import Message, Text
import os, cv2
import shutil
import csv
import numpy as np
from PIL import ImageTk, Image
import pandas as pd
import datetime
import time
import tkinter.ttk as tkk
import tkinter.font as font

ts = time.time()
Date = datetime.datetime.fromtimestamp(ts).strftime("%Y_%m_%d")
timeStamp = datetime.datetime.fromtimestamp(ts).strftime("%H:%M:%S")
Time = datetime.datetime.fromtimestamp(ts).strftime("%H:%M:%S")
Hour, Minute, Second = timeStamp.split(":")
d = {}
index = 0
####GUI for manually fill attendance
def manually_fill():
    global sb
    sb = tk.Tk()
    sb.iconbitmap("AMS.ico")
    sb.title("Enter subject name...")
    sb.geometry("580x320")
    sb.configure(background="#000000")

    def err_screen_for_subject():
        def ec_delete():
            ec.destroy()

        global ec
        ec = tk.Tk()
        ec.geometry("300x100")
        ec.iconbitmap("AMS.ico")
        ec.title("Warning!!")
        ec.configure(background="#000000")
        tk.Label(
            ec,
            text="Please enter subject name!!!",
            fg="#EF5350",
            bg="#000000",
            font=("Segoe UI", 16, "bold"),
        ).pack()
        tk.Button(
            ec,
            text="OK",
            command=ec_delete,
            fg="#00FFFF",
            bg="#112222",
            width=9,
            height=1,
            activebackground="#FF0000",
            font=("Segoe UI", 15, "bold"),
        ).place(x=90, y=50)

    def fill_attendance():

        ##Create table for Attendance
        global subb
        subb = SUB_ENTRY.get()

        if subb == "":
            err_screen_for_subject()
        else:
            sb.destroy()
            MFW = tk.Tk()
            MFW.iconbitmap("AMS.ico")
            MFW.title("Manually attendance of " + str(subb))
            MFW.geometry("880x470")
            MFW.configure(background="#000000")

            def del_errsc2():
                errsc2.destroy()

            def err_screen1():
                global errsc2
                errsc2 = tk.Tk()
                errsc2.geometry("330x100")
                errsc2.iconbitmap("AMS.ico")
                errsc2.title("Warning!!")
                errsc2.configure(background="#000000")
                tk.Label(
                    errsc2,
                    text="Please enter Student & Enrollment!!!",
                    fg="#EF5350",
                    bg="#000000",
                    font=("Segoe UI", 16, "bold"),
                ).pack()
                tk.Button(
                    errsc2,
                    text="OK",
                    command=del_errsc2,
                    fg="#00FFFF",
                    bg="#112222",
                    width=9,
                    height=1,
                    activebackground="#FF0000",
                    font=("Segoe UI", 15, "bold"),
                ).place(x=90, y=50)

            def testVal(inStr, acttyp):
                if acttyp == "1":  # insert
                    if not inStr.isdigit():
                        return False
                return True

            ENR = tk.Label(
                MFW,
                text="Enter Enrollment",
                width=15,
                height=2,
                fg="#00FFFF",
                bg="#0B192C",
                font=("Segoe UI", 15, "bold"),
            )
            ENR.place(x=30, y=100)

            STU_NAME = tk.Label(
                MFW,
                text="Enter Student name",
                width=15,
                height=2,
                fg="#00FFFF",
                bg="#0B192C",
                font=("Segoe UI", 15, "bold"),
            )
            STU_NAME.place(x=30, y=200)

            global ENR_ENTRY
            ENR_ENTRY = tk.Entry(
                MFW,
                width=20,
                validate="key",
                bg="#050505",
                fg="#EF5350",
                font=("Segoe UI", 23, "bold"),
                insertbackground="#00FFFF"
            )
            ENR_ENTRY["validatecommand"] = (ENR_ENTRY.register(testVal), "%P", "%d")
            ENR_ENTRY.place(x=290, y=105)

            def remove_enr():
                ENR_ENTRY.delete(first=0, last=22)

            STUDENT_ENTRY = tk.Entry(
                MFW, width=20, bg="#050505", fg="#EF5350", font=("Segoe UI", 23, "bold"), insertbackground="#00FFFF"
            )
            STUDENT_ENTRY.place(x=290, y=205)

            def remove_student():
                STUDENT_ENTRY.delete(first=0, last=22)

            ####get important variable

            def enter_data_DB():
                global index
                global d
                ENROLLMENT = ENR_ENTRY.get()
                STUDENT = STUDENT_ENTRY.get()
                if ENROLLMENT == "":
                    err_screen1()
                elif STUDENT == "":
                    err_screen1()
                else:
                    if index == 0:
                        d = {
                            index: {"Enrollment": ENROLLMENT, "Name": STUDENT, Date: 1}
                        }
                        index += 1
                        ENR_ENTRY.delete(0, "end")
                        STUDENT_ENTRY.delete(0, "end")
                    else:
                        d[index] = {"Enrollment": ENROLLMENT, "Name": STUDENT, Date: 1}
                        index += 1
                        ENR_ENTRY.delete(0, "end")
                        STUDENT_ENTRY.delete(0, "end")
                    # TODO implement CSV code
                print(d)

            def create_csv():
                df = pd.DataFrame(d)
                csv_name = (
                    "Attendance(Manually)/"
                    + subb
                    + "_"
                    + Date
                    + "_"
                    + Hour
                    + "-"
                    + Minute
                    + "-"
                    + Second
                    + ".csv"
                )
                import os
                if not os.path.exists("Attendance(Manually)"):
                    os.makedirs("Attendance(Manually)")
                df.to_csv(csv_name)
                O = "CSV created Successfully"
                Notifi.configure(
                    text=O,
                    bg="#112222",
                    fg="#00FFFF",
                    width=33,
                    font=("Segoe UI", 19, "bold"),
                )
                Notifi.place(x=180, y=380)
                """import csv
                import tkinter

                root = tkinter.Tk()
                root.title("Attendance of " + subb)
                root.configure(background="#000000")
                with open(csv_name, newline="") as file:
                    reader = csv.reader(file)
                    r = 0

                    for col in reader:
                        c = 0
                        for row in col:
                            # i've added some styling
                            label = tkinter.Label(
                                root,
                                width=13,
                                height=1,
                                fg="#00FFFF",
                                font=("Segoe UI", 13, "bold"),
                                bg="#112222",
                                text=row,
                                relief=tkinter.RIDGE,
                            )
                            label.grid(row=r, column=c)
                            c += 1
                        r += 1
                root.mainloop()"""

            Notifi = tk.Label(
                MFW,
                text="CSV created Successfully",
                bg="#112222",
                fg="#00FFFF",
                width=33,
                height=2,
                font=("Segoe UI", 19, "bold"),
            )

            c1ear_enroll = tk.Button(
                MFW,
                text="Clear",
                command=remove_enr,
                fg="#00FFFF",
                bg="#1A3636",
                width=10,
                height=1,
                activebackground="#FF0000",
                font=("Segoe UI", 15, "bold"),
            )
            c1ear_enroll.place(x=690, y=100)

            c1ear_student = tk.Button(
                MFW,
                text="Clear",
                command=remove_student,
                fg="#00FFFF",
                bg="#1A3636",
                width=10,
                height=1,
                activebackground="#FF0000",
                font=("Segoe UI", 15, "bold"),
            )
            c1ear_student.place(x=690, y=200)

            DATA_SUB = tk.Button(
                MFW,
                text="Enter Data",
                command=enter_data_DB,
                fg="#00FFFF",
                bg="#112222",
                width=20,
                height=2,
                activebackground="#FF0000",
                font=("Segoe UI", 15, "bold"),
            )
            DATA_SUB.place(x=170, y=300)

            MAKE_CSV = tk.Button(
                MFW,
                text="Convert to CSV",
                command=create_csv,
                fg="#00FFFF",
                bg="#330000",
                width=20,
                height=2,
                activebackground="#FF0000",
                font=("Segoe UI", 15, "bold"),
            )
            MAKE_CSV.place(x=570, y=300)
            # TODO remove check sheet
            def attf():
                import subprocess

                subprocess.Popen(
                    r'explorer /select,"C:/Users/patel/OneDrive/Documents/E/FBAS/Attendance(Manually)"'
                )

            attf = tk.Button(
                MFW,
                text="Check Sheets",
                command=attf,
                fg="#00FFFF",
                bg="#112222",
                width=12,
                height=1,
                activebackground="#FF0000",
                font=("Segoe UI", 14, "bold"),
            )
            attf.place(x=730, y=410)

            MFW.mainloop()

    SUB = tk.Label(
        sb,
        text="Enter Subject",
        width=12,
        height=1,
        fg="#00FFFF",
        bg="#000000",
        bd=5,
        relief=tk.RIDGE,
        font=("Segoe UI", 18, "bold"),
    )
    SUB.place(x=20, y=105)

    global SUB_ENTRY

    SUB_ENTRY = tk.Entry(
        sb, width=18, bd=5, bg="#050505", fg="#EF5350", font=("Segoe UI", 22, "bold"), insertbackground="#00FFFF"
    )
    SUB_ENTRY.place(x=230, y=105)

    fill_manual_attendance = tk.Button(
        sb,
        text="Fill Attendance",
        command=fill_attendance,
        fg="#00FFFF",
        bg="#000000",
        width=15,
        height=2,
        bd=7,
        relief=tk.RIDGE,
        activebackground="#FF0000",
        font=("Segoe UI", 14, "bold"),
    )
    fill_manual_attendance.place(x=195, y=180)
    sb.mainloop()
