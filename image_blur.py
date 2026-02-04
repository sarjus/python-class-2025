#Python program to blur an image using OpenCV
import cv2

# Read the image
image = cv2.imread("kerala.png")

# Apply Gaussian Blur
# (15, 15) is the kernel size – higher values mean more blur
blurred_image = cv2.GaussianBlur(image, (15, 15), 0)

# Save the blurred image
cv2.imwrite("blurred_output.jpg", blurred_image)

# Display the original and blurred images
cv2.imshow("Original Image", image)
cv2.imshow("Blurred Image", blurred_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
