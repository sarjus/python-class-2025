from skimage import io, color
import matplotlib.pyplot as plt


original_image = io.imread('kerala.png')

height, width, channels = original_image.shape
print(f"Image loaded with height: {height}, width: {width}, and channels: {channels}")

gray_image = color.rgb2gray(original_image )

plt.figure(figsize=(10, 5))

# Show the Original Image on the left
plt.subplot(1, 2, 1) # (1 row, 2 columns, position 1)
plt.imshow(original_image )
plt.title("Actual Color Image")
plt.axis('off') # Hide the X and Y numbers/axis

# Show the Grayscale Image on the right
plt.subplot(1, 2, 2) # (1 row, 2 columns, position 2)
plt.imshow(gray_image, cmap='gray') # 'cmap' tells it to use Black & White colors
plt.title("Grayscale Image")
plt.axis('off')

# Display everything on the screen
plt.show()