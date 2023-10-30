from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = load_model(r"C:\Data\Projet CODE\Code Python\DataCamp Code\data\ressources\H5\Test\keras_model.h5",
                   compile=False)

# Load the labels
class_names = open(r"C:\Data\Projet CODE\Code Python\DataCamp Code\data\ressources\H5\Test\labels.txt").readlines()

# Create the array of the right shape to feed into the keras model
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Update the image path here
image_path = r"C:\Data\Projet CODE\Code Python\DataCamp Code\data\autre_images\0\MicrosoftTeams-image2.png"
image = Image.open(image_path).convert("RGB")

# Redimensionnement pour conserver l'aspect et recadrage pour obtenir une taille de 224x224
size = (224, 224)
image = ImageOps.fit(image, size, Image.Resampling.LANCZOS)

# Convert the image to a numpy array
image_array = np.asarray(image)

# Normalize the image
normalized_image_array = (image_array.astype(np.float32) / 127.5) - 1

# Load the image into the array
data[0] = normalized_image_array

# Run the prediction
prediction = model.predict(data)
index = np.argmax(prediction)
class_name = class_names[index]
confidence_score = prediction[0][index]

# Print prediction and confidence score
print("Class:", class_name.strip(), end="")  # Using strip() to remove any leading/trailing whitespace or newline
print("\nConfidence Score:", confidence_score)
