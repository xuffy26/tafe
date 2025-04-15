import random
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np

# Simulate PARTS_DB
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

# Example model loading (replace with actual model)
model = load_model('path_to_your_model.h5')

def classify_image(image_data):
    # Preprocess image (resize, normalize, etc.)
    img = image.load_img(image_data, target_size=(224, 224))  # Example size for a pre-trained model
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array /= 255.0  # Normalize if needed
    
    # Model inference
    predictions = model.predict(img_array)
    
    # Assuming predictions are class labels (e.g., 0, 1, 2)
    predicted_label = np.argmax(predictions, axis=1)[0]
    
    # Map label to part in PARTS_DB (replace with actual mapping logic)
    part_keys = list(PARTS_DB.keys())
    predicted_part = PARTS_DB[part_keys[predicted_label]]
    
    return predicted_part
