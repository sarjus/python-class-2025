import cv2
# Read the image
image = cv2.imread("kerala.png")

# Flip the image horizontally
flipped_image = cv2.flip(image, 1)

# Display flipped image
cv2.imshow("Original Image", image)
cv2.imshow("Flipped Image", flipped_image)

cv2.waitKey(0)
cv2.destroyAllWindows()
