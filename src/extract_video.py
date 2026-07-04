# code for extracting student images from video 

import cv2
import os
import glob

INPUT_FOLDER = "student_videos"
OUTPUT_PARENT_FOLDER = "student_images"

def batch_extract_frames():
    video_extensions = ('*.mp4', '*.avi', '*.mov', '*.mkv')
    video_files = []
    
    for ext in video_extensions:
        video_files.extend(glob.glob(os.path.join(INPUT_FOLDER, ext)))
        
    if not video_files:
        print(f"No videos found in '{INPUT_FOLDER}'. Please make sure your videos are there!")
        return

    print(f"Found {len(video_files)} videos. Starting batch extraction...")

    for video_path in video_files:
        video_name = os.path.splitext(os.path.basename(video_path))[0]
        
        video_output_dir = os.path.join(OUTPUT_PARENT_FOLDER, f"{video_name}_frames")
        if not os.path.exists(video_output_dir):
            os.makedirs(video_output_dir)
            
        print(f"\nProcessing: {os.path.basename(video_path)} -> Saving to: {video_output_dir}")
        
        cap = cv2.VideoCapture(video_path)
        frame_count = 0
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break 
                
            frame_name = os.path.join(video_output_dir, f"frame_{frame_count:04d}.jpg")
            cv2.imwrite(frame_name, frame)
            frame_count += 1
            
        cap.release()
        print(f"Finished! Extracted {frame_count} frames.")


if __name__ == "__main__":
    batch_extract_frames()

