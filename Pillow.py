from PIL import Image

# Open the image
image = Image.open("hot.png")

# Get current size
width, height = image.size

# Set new width (e.g., reduce by 50%)
new_width = width // 2

# Maintain an aspect ratio
new_height = int((new_width / width) * height)

# Resize the image
resized_image = image.resize((new_width, new_height), Image.LANCZOS)  # LANCZOS is recommended

# Save resized image
resized_image.save("hot_resized.png")

print("Image width reduced and saved as 'hot_resized.png'")
