import random

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

def classify_image(image_data):
    # Simulated part recognition (replace with AI model later)
    return random.choice(list(PARTS_DB.values()))
