# CODSOFT - Artificial Intelligence Internship
# Task 5: Face Detection using Haar Cascade

import cv2
import os

cascade_path = "haarcascade_frontalface_default.xml"

# Check cascade file
if not os.path.exists(cascade_path):
    print("❌ Haar Cascade file not found!")
    exit()

face_cascade = cv2.CascadeClassifier(cascade_path)

# Check if cascade loaded
if face_cascade.empty():
    print("❌ Failed to load Haar Cascade file.")
    exit()

image_path = input("Enter image file name (example: faceimage.png): ").strip()
image = cv2.imread(image_path)

if image is None:
    print("❌ Error: Image not found.")
else:
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)

    print("Faces detected:", len(faces))

    cv2.imshow("Face Detection", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
