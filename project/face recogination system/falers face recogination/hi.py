import cv2

# Load the face cascade classifier (change path if needed)
face_cascade = cv2.CascadeClassifier("C:/Users/adity/AppData/Local/Programs/Python/Python312/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")

# Initialize video capture
video_capture = cv2.VideoCapture(0)

# Check if video capture is successful
if not video_capture.isOpened():
    print("Error opening video capture device!")
    exit()

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    # Check if frame is read correctly
    if not ret:
        print("Error reading frame!")
        break

    # Convert to grayscale (optional)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (32, 255, 255), 2)

    # Display the resulting frame
    frame = cv2.flip(frame, 1)
    
    cv2.imshow('Video Live', frame)

    # Exit on 'a' key press
    if cv2.waitKey(1) == ord('a'):
        break

# Release resources
video_capture.release()
cv2.destroyAllWindows()
