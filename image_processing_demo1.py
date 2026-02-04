'''
In OpenCV, displaying an image is a three-step process:
loading the image, creating a window to show it,
and using a "wait" function to keep the window open.
Without the wait function, the window would close instantly
after opening.
Here is the standard implementation to display both the
original and the grayscale version.
'''
import cv2

# 1. Load the image from your directory
# By default, OpenCV loads images in BGR format
image = cv2.imread('kerala.png')

# 2. Convert the image to Grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 3. Display the original color image
cv2.imshow('Original Color Image', image)

# 4. Display the grayscale version in a separate window
cv2.imshow('Grayscale Image', gray_image)

# 5. The 'waitKey' function is crucial.
# It pauses the script and waits for a key press (0 means wait infinitely)
cv2.waitKey(0)

# 6. Cleanup: Closes all windows created by OpenCV
cv2.destroyAllWindows()