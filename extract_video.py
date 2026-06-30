# code for extracting student images from video

import cv2  # OpenCV library for video reading and image saving operations
import os  # Standard library to interact with the file system (directories, paths, file listings)

VIDEO_FOLDER = 'student_videos' # folder contain student video
IMAGE_FOLDER = 'student images'  # folder where the extrac students images face will be store

# load all videos in the video folder that end with the '.MOV' 
video_files = [f for f in os.listdir(VIDEO_FOLDER) if f.endswith(('.MOV'))]

print("Processing student videos")
# Loop through each .MOV video file 
for video in video_files:
    # Extract the student's name from videos file name
    student_name = os.path.splitext(video_file)[0]
    # file path
    video_path = os.path.join(VIDEO_FOLDER, video_file)
    # read student video file
    cap = cv2.VideoCapture(video_path)
    frame_count = 0  # Counter to keep track of the total number of frames processed so far
    saved_count = 0  # Counter to track how many image frames have been successfully saved
    
    sample_rate = 10  # Configuration: Save 1 frame out of every 10 frames to skip consecutive duplicates
    max_images = 5   # Configuration: Stop processing the video once 5 total images have been saved
    
    # Run the loop as long as the video file is successfully open and we haven't reached our 5-image limit
    while cap.isOpened() and saved_count < max_images:
        ret, frame = cap.read()
        # If the video has ended or cannot be read properly, break out of the frame processing loop
        if not ret:
            break
            
        # Check if the current frame index is exactly divisible by the sample rate (every 10th frame)
        if frame_count % sample_rate == 0:
            # Construct a unique image file name using the student name and the saved image index counter
            output_name = f"{student_name}_{saved_count}.jpg"
            # Combine the image directory path with the newly generated filename
            output_path = os.path.join(IMAGE_FOLDER, output_name)
            
            # Physically write and save the current video frame as a compressed JPEG file 
            cv2.imwrite(output_path, frame)
            saved_count += 1  # Increment the counter of successfully saved images
            
        frame_count += 1  # Increment the master frame counter to evaluate the next frame sequence
        
    # Close the video file reader and free up system resources for this specific video
    cap.release()
    # Print a progress message transforming underscores to spaces and capitalizing the name (e.g., 'John Doe')
    print(f"Extracted {saved_count} face angles for: {student_name.replace('_', ' ').title()}")

print("Extract all students face from video completed")
