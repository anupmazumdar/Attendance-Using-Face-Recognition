
# Face based attendance system using python and openCV

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)                 
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/) 

### What steps you have to follow?
- Download or clone my repository to your device.
- Type `pip install -r requirements.txt` in command prompt (this will install required packages for the project).
- Create a `TrainingImage` folder in your project folder.
- Open `attendance.py` and `automaticAttendance.py`, and change all paths according to your system.
- Run `attendance.py` file.

### Project flow & explanation
- After you run the project, you have to register your face so the system can identify you. Click on "Register new student".
- After clicking, a small window will pop up where you have to enter your ID and name, then click on the `Take Image` button.
- After clicking `Take Image`, a camera window will pop up and detect your face, taking up to 50 images (you can change this number) that will be stored in the `TrainingImage` folder. The more images you provide to the system, the better it will perform at recognizing your face.
- Then click on the `Train Image` button. It will train the model and convert all images into numeric format so the computer can understand. We are training the images so that next time you show the same face to the computer, it will easily identify it.
- This will take some time (depending on your system).
- After training the model, click on `Automatic Attendance`. You have to enter the subject name, and then the system can fill attendance by detecting your face using the trained model.
- It will create a `.csv` file for every subject you enter and separate each `.csv` file according to the subject.
- You can view the attendance after clicking `View Attendance` button. It will display records in tabular format.

### Screenshots

### Simple UI
![Simple UI](Project%20Snap/1.png)

### While taking Image
![Screenshot (103)](Project%20Snap/9.png)

### While taking Attendance
![Screenshot (91)](Project%20Snap/9.png)

### Attendance in tabular format 
![Attendance Records](Project%20Snap/9.png)

### Just follow me and Star⭐ my repository!
