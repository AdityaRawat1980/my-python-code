import cv2
import win64gui, win64api  # For checking operating system

# Load the face cascade classifier (change path if needed)
face_cascade = cv2.CascadeClassifier("C:/Users/adity/AppData/Local/Programs/Python/Python312/Lib/site-packages/cv2/data/haarcascade_frontalface_default.xml")

# Initialize video capture
video_capture = cv2.VideoCapture(0)

# Check if video capture is successful
if not video_capture.isOpened():
    print("Error opening video capture device!")
    exit()

def on_window_close(window_name):  # Function for window close event
    global running  # Assuming a global variable to control loop
    running = False

cv2.namedWindow('Video Live')  # Create the window with a name
cv2.setMouseCallback('Video Live', on_window_close)  # Set the callback

running = True
while running:
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

    # Flip the frame horizontally to remove mirror effect
    frame = cv2.flip(frame, 1)

    # Display the resulting frame
    cv2.imshow('Video Live', frame)

    # Handle fullscreen toggle (assuming Esc key for simplicity)
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # Esc key for fullscreen toggle (replace with desired key)
        # Check OpenCV version for fullscreen support
        if int(cv2.__version__.major) >= 3 and int(cv2.__version__.minor) >= 2:
            cv2.toggleFullscreen('Video Live')  # Use built-in method (OpenCV 3.2+)
        else:
            # Use platform-specific approach for older OpenCV versions
            if platform.system() == 'Windows':
                import win64gui, win64api
                toggle_fullscreen(window_name='Video Live')
            elif platform.system() == 'Darwin':  # macOS
                import appscript
                toggle_fullscreen(window_name='Video Live')
            else:
                print("Fullscreen toggle not supported on your platform or OpenCV version.")

# Release resources
video_capture.release()
cv2.destroyAllWindows()

# Define toggle_fullscreen function for Windows (if needed)
def toggle_fullscreen(window_name):
    hwnd = win64gui.FindWindow(None, window_name)
    style = win64gui.GetWindowLong(hwnd, win64api.GWL_STYLE)
    if style & win64con.WS_MAXIMIZE:
        win64gui.SetWindowLong(hwnd, win64api.GWL_STYLE, style & ~win32con.WS_MAXIMIZE)
        win32gui.ShowWindow(hwnd, win64con.SW_NORMAL)
    else:
        win32gui.SetWindowLong(hwnd, win32api.GWL_STYLE, style | win32con.WS_MAXIMIZE)
        win32gui.ShowWindow(hwnd, win32con.SW_MAXIMIZE)

# Define toggle_fullscreen function for macOS (if needed)
def toggle_fullscreen(window_name):
    apps = appscript.apps.list()
    for app in apps:
        if app.name == 'Video Live':  # Replace with your window title
            windows = app.windows
            for window in windows:
                if window.title == window_name:
                    window.toggle_full_screen()
                    break
            break
