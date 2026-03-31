
# Face based attendance system using python and openCV

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)                 
[![Python 3.9](https://img.shields.io/badge/python-3.9-blue.svg)](https://www.python.org/downloads/release/python-390/) 

### What steps you have to follow?
- Download or clone my Repository to your device
- type `pip install -r requirements.txt` in command prompt (this will install required packages for the project)
- Create a `TrainingImage` folder in a project folder.
- open `attendance.py` and `automaticAttendance.py`, change all the paths according to your system
- Run `attendance.py` file

### Project flow & explanation
- After you run the project you have to register your face so that system can identify you, so click on register new student
- After you click a small window will pop up in that you have to enter your ID and name and then click on `Take Image` button
- After clicking `Take Image` button A camera window will pop up and it will detect your Face and take upto 50 Images (you can change the number of Images it can take) and stored in the folder named `TrainingImage`. The more you give the system images, the better it will perform while recognising the face.
- Then you have to click on `Train Image` button. It will train the model and convert all the Images into numeric format so that computer can understand. We are training the images so that next time when we will show the same face to the computer it will easily identify the face.
- It will take some time (depends on your system).
- After training model click on `Automatic Attendance`, you have to enter the subject name and then it can fill attendance by your face using our trained model.
- It will create `.csv` file for every subject you enter and separate every `.csv` file according to the subject.
- You can view the attendance after clicking `View Attendance` button. It will show record in tabular format.

### Screenshots

### Simple UI
<img src='Project Snap/1.png'>

### While taking Image
![Screenshot (103)](Project%20Snap/9.png)

### While taking Attendance
![Screenshot (91)](Project%20Snap/9.png)

### Attendance in tabular format 
<img src='Project Snap/9.png'>

## Just follow me and Star⭐ my repository
