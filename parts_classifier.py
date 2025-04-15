import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image

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

# Load your trained Keras model (HDF5 file)
model = load_model("model.h5")  # <-- Replace with your actual model path
CLASS_NAMES = list(PARTS_DB.keys())  # Should match your model classes

def classify_image(pil_image):
    # Preprocess image (resize & normalize)
    image = pil_image.resize((224, 224))  # Match the input size of your model
    image = img_to_array(image) / 255.0
    image = np.expand_dims(image, axis=0)

    # Predict
    prediction = model.predict(image)
    predicted_index = np.argmax(prediction[0])
    label = CLASS_NAMES[predicted_index]

    return PARTS_DB[label]
