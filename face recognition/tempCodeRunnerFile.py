import face_recognition
import cv2
import numpy as np
import csv
from datetime import datetime

# Initialize video capture
video_capture = cv2.VideoCapture(0)

# Load and encode images
swarnlata_image = face_recognition.load_image_file("image.png")
swarnlata_encoding = face_recognition.face_encodings(swarnlata_image)[0]

lakshita_image = face_recognition.load_image_file("lakshita.png")
lakshita_encoding = face_recognition.face_encodings(lakshita_image)[0]

salonimourya_image = face_recognition.load_image_file("saloni mourya.png")
salonimourya_encoding = face_recognition.face_encodings(salonimourya_image)[0]

salonigurjar_image = face_recognition.load_image_file("saloni gurjar.png")
salonigurjar_encoding = face_recognition.face_encodings(salonigurjar_image)[0]

suraj_image = face_recognition.load_image_file("suraj sharma.png")
suraj_encoding = face_recognition.face_encodings(suraj_image)[0]

vedansh_image = face_recognition.load_image_file("vedansh.png")
vedansh_encoding = face_recognition.face_encodings(vedansh_image)[0]

uday_image = face_recognition.load_image_file("uday.png")
uday_encoding = face_recognition.face_encodings(uday_image)[0]

known_face_encodings = [
    swarnlata_encoding, lakshita_encoding, salonimourya_encoding,
    salonigurjar_encoding, suraj_encoding, vedansh_encoding, uday_encoding
]
known_face_names = [
    "Swarnlata Raje", "Lakshita Temare", "Saloni Mourya",
    "Saloni Gurjar", "Suraj Sharma", "Vedansh", "Uday Choubey"
]

# List of students for attendance
students = known_face_names.copy()

# Get current date and time for CSV filename
now = datetime.now()
current_date = now.strftime("%Y-%m-%d_%H-%M-%S")

# Create CSV file for attendance
with open(f"{current_date}.csv", "w+", newline="") as f:
    lnwriter = csv.writer(f)

    while True:
        _, frame = video_capture.read()
        # Resize frame for faster processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)

        # Find face locations and encodings
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for face_encoding, face_location in zip(face_encodings, face_locations):
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)

            name = "Unknown"
            if matches[best_match_index]:
                name = known_face_names[best_match_index]

                if name in students:
                    students.remove(name)
                    current_time = datetime.now().strftime("%H:%M:%S")
                    lnwriter.writerow([name, current_time])

            # Draw rectangle and label around the face
            top, right, bottom, left = [v * 4 for v in face_location]  # Scale back to original size
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.putText(
                frame, f"{name} Present", (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX,
                0.8, (255, 0, 0), 2
            )

        # Display the video frame
        cv2.imshow("Attendance", frame)

        # Exit loop on pressing 'z'
        if cv2.waitKey(1) & 0xFF == ord("z"):
            break

# Release resources
video_capture.release()
cv2.destroyAllWindows()
