# code for extracting student images from video
# (Neary)  
# task : write code for extracting student images from student video in order to do face recognition project more accurately 
# when scaning student faces

import cv2
import os
import glob

# --- CONFIGURATION ---
INPUT_FOLDER = "student_videos"
OUTPUT_PARENT_FOLDER = "student_images"
# ---------------------

def batch_extract_frames():
    # Target video formats (handles .mp4, .avi, .mov, .mkv)
    video_extensions = ('*.mp4', '*.avi', '*.mov', '*.mkv')
    video_files = []
    
    # Find all videos in the input folder
    for ext in video_extensions:
        video_files.extend(glob.glob(os.path.join(INPUT_FOLDER, ext)))
        
    if not video_files:
        print(f"No videos found in '{INPUT_FOLDER}'. Please make sure your videos are there!")
        return

    print(f"Found {len(video_files)} videos. Starting batch extraction...")

    # Process each video one by one
    for video_path in video_files:
        # Get just the name of the file without the folder path or extension
        video_name = os.path.splitext(os.path.basename(video_path))[0]
        
        # Create a unique output subfolder for this specific video
        video_output_dir = os.path.join(OUTPUT_PARENT_FOLDER, f"{video_name}_frames")
        if not os.path.exists(video_output_dir):
            os.makedirs(video_output_dir)
            
        print(f"\nProcessing: {os.path.basename(video_path)} -> Saving to: {video_output_dir}")
        
        # Open the video
        cap = cv2.VideoCapture(video_path)
        frame_count = 0
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break # End of video
                
            # Save the frame
            frame_name = os.path.join(video_output_dir, f"frame_{frame_count:04d}.jpg")
            cv2.imwrite(frame_name, frame)
            frame_count += 1
            
        cap.release()
        print(f"Finished! Extracted {frame_count} frames.")

    print("\n==========================================")
    print("All videos have been processed successfully!")
    print("==========================================")

if __name__ == "__main__":
    batch_extract_frames()

