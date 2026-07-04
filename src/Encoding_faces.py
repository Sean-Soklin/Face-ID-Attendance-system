import os
import pickle
import numpy as np
from PIL import Image
import face_recognition

IMAGE_PATH = 'student_images'
OUTPUT_FILE = 'encodings.pickle'

known_face_encodings = []
known_face_names = []

print("Starting FAST optimization: Encoding student faces...")

for folder_name in os.listdir(IMAGE_PATH):
    folder_path = os.path.join(IMAGE_PATH, folder_name)
    
    if os.path.isdir(folder_path):
        clean_name = folder_name[:-7] if folder_name.lower().endswith('_frames') else folder_name
        student_name = clean_name.replace('_', ' ').replace('-', ' ').strip().title()
        
        # Get a sorted list of all images in the folder
        all_images = sorted([f for f in os.listdir(folder_path) if f.endswith(('.jpg', '.jpeg', '.png'))])
        
        # FIX: Only pick every 15th frame (e.g., frame 0, frame 15, frame 30...)
        sampled_images = all_images[::15] 
        
        print(f"Processing {len(sampled_images)} selected frames for: {student_name} (Skipped the rest)")
        
        for filename in sampled_images:
            image_path = os.path.join(folder_path, filename)
            try:
                pil_img = Image.open(image_path).convert('RGB')
                image = np.array(pil_img)
                encodings = face_recognition.face_encodings(image)
                
                if len(encodings) > 0:
                    known_face_encodings.append(encodings[0])
                    known_face_names.append(student_name)
            except Exception:
                pass

# Save the mathematical data to disk
with open(OUTPUT_FILE, 'wb') as f:
    pickle.dump({"encodings": known_face_encodings, "names": known_face_names}, f)

print(f"\nDone! Saved {len(known_face_names)} optimized variants to '{OUTPUT_FILE}'.")
