import cv2

# Load pre-trained face detection model from OpenCV
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Initialize video capture from default camera (index 0)
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame from the webcam
    ret, frame = cap.read()

    # Exit the loop if the frame is not captured correctly
    if not ret:
        print("Failed to capture video frame.")
        break

    # Convert the captured frame to grayscale (required for face detection)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(30, 30)
    )

    # Loop over the detected faces and apply a blur to each
    for (x, y, w, h) in faces:
        # Extract the face region
        face_region = frame[y:y + h, x:x + w]

        # Apply Gaussian blur to the detected face region
        blurred_face = cv2.GaussianBlur(face_region, (99, 99), 30)

        # Replace the original face region with the blurred version
        frame[y:y + h, x:x + w] = blurred_face

    # Display the resulting frame with blurred faces
    cv2.imshow('Face Blur by Mishhka.s', frame)

    # Break the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Exiting...")
        break

# Release the video capture and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()
