import cv2
import numpy as np

# Define variables for window width and height
window_width = 720
window_height = 512

# Create a VideoCapture object to capture video from the webcam
cap = cv2.VideoCapture(1)

# Check if the webcam is opened successfully
if not cap.isOpened():
    print("Unable to open the webcam")
    exit()

# Create a window to display the video
cv2.namedWindow("Webcam", cv2.WINDOW_NORMAL)
cv2.resizeWindow("Webcam", window_width, window_height)

# def detect_color(frame):
#     # Convert the frame to the HSV color space
#     hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#     # Define the lower and upper thresholds for red color
#     lower_red = np.array([0, 100, 100])
#     upper_red = np.array([10, 255, 255])

#     # Define the lower and upper thresholds for green color
#     lower_green = np.array([50, 100, 100])
#     upper_green = np.array([70, 255, 255])

#     # Create masks for red and green color ranges
#     red_mask = cv2.inRange(hsv_frame, lower_red, upper_red)
#     green_mask = cv2.inRange(hsv_frame, lower_green, upper_green)

#     # Apply the masks to the frame
#     red_result = cv2.bitwise_and(frame, frame, mask=red_mask)
#     green_result = cv2.bitwise_and(frame, frame, mask=green_mask)

#     # Check if red or green color is detected
#     if cv2.countNonZero(red_mask) > 0:
#         cv2.putText(frame, "Red Detected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
#     elif cv2.countNonZero(green_mask) > 0:
#         cv2.putText(frame, "Green Detected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

#     return frame

def draw_bounding_box(frame, mask, color):
    # Find contours of the detected color
    contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Draw bounding boxes around the contours
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        cv2.rectangle(frame, (x, y), (x + w, y + h), color, 2)

    return frame

def detect_color(frame):
    # Convert the frame to the HSV color space
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Define the lower and upper thresholds for red color
    lower_red = np.array([0, 100, 100])
    upper_red = np.array([10, 255, 255])

    # Define the lower and upper thresholds for green color
    lower_green = np.array([50, 100, 100])
    upper_green = np.array([70, 255, 255])

    # Create masks for red and green color ranges
    red_mask = cv2.inRange(hsv_frame, lower_red, upper_red)
    green_mask = cv2.inRange(hsv_frame, lower_green, upper_green)

    # Apply the masks to the frame
    red_result = cv2.bitwise_and(frame, frame, mask=red_mask)
    green_result = cv2.bitwise_and(frame, frame, mask=green_mask)

    # Draw bounding boxes around the detected colors
    frame = draw_bounding_box(frame, red_mask, (0, 255, 255))  # Yellow color for red detection
    frame = draw_bounding_box(frame, green_mask, (0, 255, 255))  # Yellow color for green detection

    # Check if red or green color is detected
    if cv2.countNonZero(red_mask) > 0:
        cv2.putText(frame, "Red Detected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
    elif cv2.countNonZero(green_mask) > 0:
        cv2.putText(frame, "Green Detected", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    return frame

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # If the frame was not read successfully, exit the loop
    if not ret:
        break

    # Perform color detection on the frame
    frame = detect_color(frame)

    # Display the frame in the "Webcam" window
    cv2.imshow("Webcam", frame)

    # Wait for the 'q' key to be pressed or the window to be closed to exit the loop
    if cv2.waitKey(1) == ord('q') or cv2.getWindowProperty("Webcam", cv2.WND_PROP_VISIBLE) < 1:
        break

# Release the VideoCapture object and close the window
cap.release()
cv2.destroyAllWindows()
