
project title: Face-ID-Attendance-system
group 3

Name of all group members:
Ly Sivpinh
Chorn Chan Nimol
Pon Sokunneary
Sean Soklin
Prithy Monynich
Chea Moniveasna
Nhem Monity
Proeung Sokleaph
Soun Ariya

Description 
The Face-ID Attendance System is a Python-based application that automatically records student attendance using facial recognition technology. Instead of manually taking attendance, 
the system detects and recognizes registered students' faces through a webcam and marks their attendance automatically.

Prerequisites & Installation: 
For the project we need to install these libraries 
opencv-python == 4.13.0.92
face-recognition == 1.3.0
dlib == 20.0.1  (python 3.12)
numpy == 2.4.2
use python version 3.8-3.11 with these versions we don’t have to install dlib. However  if we use python 3.12 dlib is required

Where to install these libraries:

We can install python on the official python website.
- opencv-python: can be installed directly through your terminal with comand promt :
  'pip install opencv-python' for windows and 'pip3 install opencv-python' for macos.
- face recognition: can be installed directly through your terminal with pip.
  prompt: 'pip install face_recognition' for windows and 'pip3 install face_recognition' for macos.
- dlib: in case you are using python version (3.12) you need to install C++ compiler in your vs code first then you can prompt pip to install dlib.
  prompt: 'pip install dlib' for windows. If it doesn't work you can prompt it to install cmake first: 'pip install cmake'.
  For macos you have to command terminal to install Apple's command-line developer tools first 'xcode-select --install'. Then you need a tool called homebrew to easily grab compiler tool. To do that you use this bash: /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)". once your homebrew is ready you can command: 'brew install cmake'. Once it's ready you can now download dlib with pip: 'pip3 install dlib'.
- numpy: can be installed directly through your terminal with pip.
  prompt: 'pip install numpy' for windows and 'pip3 install numpy' for macos.


How to Run: Clear, step-by-step instructions on how to execute your code.
-Install all the libraries in your computer
-Open vs code created a new folder
-Create a folder name student_videos and store all your student videos in there put it in vs code folder
-Copy all the .py files ( extract_video.py  , main.py , encoding_faces.py )
-Run extract_video.py file , the system will now extract each student frame from videos than save it into student_images folder
-Run encoding_faces.py , the system will now convert images into numerical this might takes lots of time
-Run main.py every time you want to take attendance. 
-Let the student stand in front of the camera if the face matches it will display the student name on screen and mark them present , if not it will display unknown.







