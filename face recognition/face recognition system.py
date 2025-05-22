
# # pip install cmake
# # pip install face_recognition
# # pip install opencv-python

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



suraj_image = face_recognition.load_image_file("suraj sharma.png")
suraj_encoding = face_recognition.face_encodings(suraj_image)[0]

vedansh_image = face_recognition.load_image_file("vedansh.png")
vedansh_encoding = face_recognition.face_encodings(vedansh_image)[0]

uday_image = face_recognition.load_image_file("uday.png")
uday_encoding = face_recognition.face_encodings(uday_image)[0]

known_face_encodings = [
    swarnlata_encoding, lakshita_encoding, salonimourya_encoding,
     suraj_encoding, vedansh_encoding, uday_encoding
]
known_face_names = [
    "Swarnlata Raje", "Lakshita Temare", "Saloni Mourya", "Suraj Sharma", "Vedansh", "Uday Choubey"
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

        # Default to "Not in Class" for unrecognized faces
        name = "Not in Class"
        if matches[best_match_index]:
            name = known_face_names[best_match_index]

            # Mark attendance for recognized students
            if name in students:
                students.remove(name)
                current_time = datetime.now().strftime("%H:%M:%S")
                lnwriter.writerow([name, current_time])

        # Draw rectangle and label around the face
        top, right, bottom, left = [v * 4 for v in face_location]  # Scale back to original size
        color = (0, 255, 0) if name != "Not in Class" else (0, 0, 255)  # Green for recognized, Red for unrecognized
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        cv2.putText(
            frame, name, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX,
            0.8, color, 2
        )

    # Display the video frame
     cv2.imshow("Attendance", frame)

    # Exit loop on pressing 'z'
     if cv2.waitKey(1) & 0xFF == ord("z"):
        break


# Release resources
video_capture.release()
cv2.destroyAllWindows()



# import face_recognition
# import cv2
# import numpy as np
# import csv
# from datetime import datetime

# video_capture = cv2.VideoCapture(0)
# # import/load non faces
# # encoding of images =images are converted into numbers in such a way so that they are easy to compare
# swarnlata_image = face_recognition.load_image_file("image.png")
# # it will make the encoding of swarnlata face
# swarnlata_encoding = face_recognition.face_encodings(swarnlata_image)[0]

# lakshita_image = face_recognition.load_image_file("lakshita.png")
# lakshita_encoding = face_recognition.face_encodings(lakshita_image)[0]

# salonimourya_image = face_recognition.load_image_file("saloni mourya.png")
# salonimourya_encoding = face_recognition.face_encodings(salonimourya_image)[0]

# salonigurjar_image = face_recognition.load_image_file("saloni gurjar.png")
# salonigurjar_encoding = face_recognition.face_encodings(salonigurjar_image)[0]

# suraj_image = face_recognition.load_image_file("suraj sharma.png")
# suraj_encoding = face_recognition.face_encodings(suraj_image)[0]

# vedansh_image = face_recognition.load_image_file("vedansh.png")
# vedansh_encoding = face_recognition.face_encodings(vedansh_image)[0]

# uday_image = face_recognition.load_image_file("uday.png")
# uday_encoding = face_recognition.face_encodings(uday_image)[0]

# known_face_encodings = [swarnlata_encoding,lakshita_encoding,salonimourya_encoding,salonigurjar_encoding,suraj_encoding,vedansh_encoding,uday_encoding]
# known_face_names = ["Swarnlata Raje","Lakshita Temare","Saloni Mourya","Saloni Gurjar","Suraj Sharma","vedansh","Uday Choubey"]

# # list of expected students
# students = known_face_names.copy()

# # # another list by name face location
# # face_locations = []
# # face_encodings = []

# # Get the curent dat and time
# # here datetime is (inbuilt) function

# now = datetime.now()
# current_date = now.strftime("%Y-%m-%d_%H-%M-%S") #here strf formate the time (hour,Minute,second)

# # make a csv writter
# with open(f"{current_date}.csv","w+",newline="") as f:
#   lnwriter = csv.writer(f)

# # creating an infinite while loop
# while True:
#     # here _(underscore) and frame are the two arguments
#     # _ == video captured successfully, we need a frame to capture the video ie a person
#     _, frame = video_capture.read()
#     # we resize the frame
#     small_frame = cv2.resize(frame,(0,0),fx =0.25,fy=0.25)
#     # converted into bgr2rgb
#     rgb_small_frame = cv2.cvtColor(small_frame , cv2.COLOR_BGR2RGB)

# #     RECOGNIZE FACES
#     face_locations = face_recognition.face_locations(rgb_small_frame)
#     face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)


#     for face_encoding in face_encodings:
#         matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
#         # it gives you the idea of the similarity of the face from encoded face
#         face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
#         # it gives you the index match of the face in minimum distance
#         best_match_index = np.argmin(face_distances)


#         name ="Unknown"  #additional added
#         if (matches[best_match_index]):
#             name = known_face_names[best_match_index]

         


#     #Add the text if a person is present
#     if name in known_face_names:
#         font = cv2.FONT_HERSHEY_SIMPLEX
#         # here bottomLeftCornerOfText is a variable
#         bottomLeftCornerOfText = (10,100)
#         fontScale = 1.5
#         fontColor = (255,0,0)
#         thickness = 3
#         lineType = 2
#         cv2.putText(frame,name +"present",bottomLeftCornerOfText , font, fontScale ,fontColor , thickness , lineType)


             
#         # if name in students:
#         #     # remove expected student bcz they are already present
#         #     students.remove(name)
#         #     current_time = now.strftime("%H-%M-%S")
#         #     lnwriter.writerow([name,current_time])


#     cv2.imshow("Attendence",frame)
#     # it will break when we use z
#     # it is bitwise so we use single &
#     if cv2.waitkey(1) & 0xFF == ord("z"):
#         break

# video_capture.release()
# cv2.destroyAllWindows()
# f.close()
