import cv2
import numpy as np
import time

# Capture the video feed from the webcam
cap = cv2.VideoCapture(0)

# Give the camera time to warm up
time.sleep(2)

# Capture the background in the beginning for a few seconds
for i in range(30):
    ret, background = cap.read()

# Flip the background image
background = np.flip(background, axis=1)

# Define the range of blue color in HSV
lower_blue = np.array([94, 80, 2])
upper_blue = np.array([126, 255, 255])

while(cap.isOpened()):
    ret, img = cap.read()
    
    if not ret:
        break
    
    # Flip the image for consistency
    img = np.flip(img, axis=1)
    
    # Convert the image from BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    
    # Create a mask to detect blue color
    mask1 = cv2.inRange(hsv, lower_blue, upper_blue)

    # Refine the mask using morphological operations
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_DILATE, np.ones((3, 3), np.uint8))

    # Create an inverse mask to segment the person
    mask2 = cv2.bitwise_not(mask1)

    # Segment the person out of the frame using mask2
    res1 = cv2.bitwise_and(img, img, mask=mask2)

    # Segment the background using mask1
    res2 = cv2.bitwise_and(background, background, mask=mask1)

    # Combine the two results to get the final output
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

    # Display the final output
    cv2.imshow("Invisibility Cloak", final_output)

    # Break the loop when 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close windows
cap.release()
cv2.destroyAllWindows()