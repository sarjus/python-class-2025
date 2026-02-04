#Python program to Python Shrink an Image by a Given Factor
import cv2

def shrink_image(image, factor):
    """
    Shrinks the given image by the specified factor.

    Parameters:
    image  : Input image
    factor : Shrinking factor (e.g., 2, 3, 4)

    Returns:
    A new image that is smaller by the given factor
    """

    # Get original dimensions
    height, width = image.shape[:2]

    # Calculate new dimensions
    new_width = width // factor
    new_height = height // factor

    # Resize the image
    shrunk_image = cv2.resize(image, (new_width, new_height))

    return shrunk_image
# Read the image
img = cv2.imread("kerala.png")

# Shrink the image by a factor of 2
small_img = shrink_image(img, 2)

# Display the images
cv2.imshow("Original Image", img)
cv2.imshow("Shrunk Image", small_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
