# Main code for attendance project
# libiary 
import cv2
import face_recognition
import numpy as np
import pickle
import time

# face encoding
ENCODINGS_FILE = 'encodings.pickle'
try:
    with open(ENCODINGS_FILE, "rb") as file:
        data = pickle.load(file)

    known_face_encodings = data["encodings"]
    known_face_names = data["names"]

except FileNotFoundError:
    print("Error: encodings.pickle file not found.")
    sys.exit()

already_logged = set()

# camera and face recognition
print("Opening camera to Scan attendance !")
print("Press n on Keyboard to exit")

WINDOW_NAME = 'Scanning faces for attendance'
video_capture = cv2.VideoCapture(0, cv2.CAP_DSHOW)
video_capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
video_capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 360)

cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)
cv2.resizeWindow(WINDOW_NAME, 640, 360)
time.sleep(1.5)

while True:
    ret, frame = video_capture.read()
    if not ret or frame is None:
        continue

    try:
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for face_encoding, face_location in zip(face_encodings, face_locations):
            name = "Unknown"

            if len(known_face_encodings) > 0:
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                
                if face_distances[best_match_index] < 0.38:
                    name = known_face_names[best_match_index]
                    
                    if name not in already_logged:
                        already_logged.add(name)
                        print(f" {name} is presented")

            top, right, bottom, left = [coord * 4 for coord in face_location]
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, name, (left + 6, bottom - 6), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 1)

    except Exception:
        pass

    cv2.imshow(WINDOW_NAME, frame)
    if cv2.waitKey(1) & 0xFF == ord('n'):
        break

video_capture.release()
cv2.destroyAllWindows()
