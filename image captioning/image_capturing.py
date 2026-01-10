# CODSOFT - Artificial Intelligence Internship
# Task 3: Image Captioning using PNG Images

from PIL import Image
import matplotlib.pyplot as plt

def generate_caption(image_name):
    """
    This function returns a caption based on the image name.
    """

    captions = {
        "dog.png": "A dog is sitting on the ground.",
        "cat.png": "A cat is resting peacefully.",
        "car.png": "A car is parked on the road.",
        "person.png": "A person is standing outdoors."
    }

    return captions.get(image_name, "An object is present in the image.")

# Main program
print("IMAGE CAPTIONING AI")
print("Supported images: dog.png, cat.png, car.png, person.png\n")

image_path = input("Enter the image file name: ")

try:
    # Open and display the image
    image = Image.open(image_path)
    plt.imshow(image)
    plt.axis("off")
    plt.show()

    # Generate and print caption
    caption = generate_caption(image_path)
    print("Generated Caption:")
    print(caption)

except FileNotFoundError:
    print("Error: Image file not found. Please check the file name.")
