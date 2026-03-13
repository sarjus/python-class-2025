import cv2

# Read the image
image = cv2.imread("kerala.png")

# Rotate image by 90 degrees clockwise
rotated_image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)

# Display rotated image
cv2.imshow("Original Image", image)
cv2.imshow("Rotated Image", rotated_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
