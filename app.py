import cv2

# Use 0 or 1 depending on your system. If OBS is the only camera, use 0.
cap = cv2.VideoCapture(1)  # Change the index if needed

if not cap.isOpened():
    print("Error: Could not open video stream from OBS Virtual Camera.")
else:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Display the frame
        cv2.imshow('OBS Virtual Camera Feed', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release resources
cap.release()
cv2.destroyAllWindows()
