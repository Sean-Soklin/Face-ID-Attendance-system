# Write a Python preprocessing script for a face recognition attendance system. 
# The script should scan a student_images folder where each student has their own subfolder of images (e.g., John_Doe_frames). 
# For each student, clean the folder name into a readable student name, then load only every 15th image to reduce processing time. 
# Convert each image to RGB, generate a face encoding using the face_recognition library, and store the encoding together with the student's name.
# Skip any images that cannot be processed or do not contain a detectable face. After processing all students, 
# save all face encodings and names into an encodings.pickle file using pickle so the main attendance program can load them quickly 
# without re-encoding every image.


print("Test")