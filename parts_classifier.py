import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image

# Dictionary of known parts
PARTS_DB = {
    "fuel_pump": {
        "name": "Fuel Pump",
        "description": "Supplies fuel from the tank to the engine.",
        "common_issues": "Leakage, low pressure, engine misfire."
    },
    "bevel_gear": {
        "name": "Bevel Gear",
        "description": "Used in the front axle for torque transfer.",
        "common_issues": "Grinding noise, wear, steering issues."
    },
    "air_filter": {
        "name": "Air Filter",
        "description": "Prevents dust from entering the engine.",
        "common_issues": "Clogging, engine underperformance."
    }
}

# Load the trained Keras model once
MODEL_PATH = "model.h5"  # Update if needed
model = load_model(MODEL_PATH)

# Ensure class names match the model's output
CLASS_NAMES = list(PARTS_DB.keys())

def classify_image(pil_image):
    """
    Classifies a PIL image and returns part info from PARTS_DB.
    """
    # Preprocess image to match model input
    image = pil_image.resize((224, 224))  # Match input shape of your model
    image = img_to_array(image) / 255.0   # Normalize pixel values
    image = np.expand_dims(image, axis=0)

    # Predict using model
    prediction = model.predict(image)

    predicted_index = int(np.argmax(prediction[0]))
    label = CLASS_NAMES[predicted_index]

    # Return the corresponding part info
    part_info = PARTS_DB.get(label, {
        "name": "Unknown Part",
        "description": "This part is not in the database.",
        "common_issues": "No known issues."
    })

    return part_info
