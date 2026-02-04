from PIL import Image

# 1. Open the image file
# Pillow automatically detects the file format (PNG, JPG, etc.)
img = Image.open('kerala.png')

# 2. Convert to Grayscale
# The 'L' mode stands for "Luminance" (8-bit pixels, black and white)
gray_img = img.convert('L')

# 3. Display the image
# This opens the image in your computer's default photo viewer
img.show(title="Original Image")
gray_img.show(title="Grayscale Image")

# 4. (Optional) Save the result
gray_img.save('output_gray.jpg')