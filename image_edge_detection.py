import cv2

# Read the colour image
image = cv2.imread("image_sample.png")

# Convert the colour image to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Canny edge detection
edges = cv2.Canny(gray_image, 100, 200)

# Display the original and edge-detected images
cv2.imshow("Original Colour Image", image)
cv2.imshow("Edge Detected Image", edges)

cv2.waitKey(0)
cv2.destroyAllWindows()
