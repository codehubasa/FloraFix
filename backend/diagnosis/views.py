import os
import numpy as np
import json
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render

# -------------------
# Load ML model & class names once
# -------------------
MODEL_PATH = os.path.join(settings.BASE_DIR, "ml_models", "plant_disease_final.keras")
CLASS_NAMES_PATH = os.path.join(settings.BASE_DIR, "ml_models", "class_names.json")

model = load_model(MODEL_PATH)

with open(CLASS_NAMES_PATH, "r") as f:
    CLASS_NAMES = json.load(f)

if isinstance(CLASS_NAMES, dict):
    CLASS_NAMES = list(CLASS_NAMES.values())

# -------------------
# Helper for preprocessing
# -------------------
def preprocess_image(img_path, target_size=(128, 128)):  # ✅ match model input
    img = image.load_img(img_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0
    return img_array

# -------------------
# Main View
# -------------------
def index(request):
    result = None
    confidence = None
    uploaded_image_url = None

    if request.method == "POST" and request.FILES.get("plantImage"):
        # Save uploaded image
        image_file = request.FILES["plantImage"]
        fs = FileSystemStorage()
        filename = fs.save(image_file.name, image_file)
        uploaded_image_path = fs.path(filename)
        uploaded_image_url = fs.url(filename)

        # Predict
        img_array = preprocess_image(uploaded_image_path)
        predictions = model.predict(img_array)
        predicted_class = np.argmax(predictions[0])
        confidence = round(100 * np.max(predictions[0]), 2)
        result = CLASS_NAMES[predicted_class]

    return render(request, "diagnosis/diagnose.html", {
        "result": result,
        # "confidence": confidence,
        "uploaded_image_url": uploaded_image_url,
    })
