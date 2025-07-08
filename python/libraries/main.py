#  -*- coding: UTF-8 -*-

# MindPlus
# Python
from learn import webcam_predict_confidence
from learn import capture_webcam_image
from learn import webcam_predict_label
from learn import send_prediction_data
from learn import load_custom_model


camera_id = 1
image = capture_webcam_image(camera_id)
# This block captures an image from the webcam and saves it to:
# Windows: C:\Users\{your user name}\webcam_images
# MacOS: /Users/{your user name}/webcam_images
# Linux: /home/{your user name}/webcam_images
model_path = "https://github.com/MASTSummerSchool/MAST-AI/raw/refs/heads/main/models/mobilenet_NOME_v1.h5"
model = load_custom_model(model_path)
# This block loads a custom trained model from:
# Local files: ~/models/model.keras
# URLs: https://github.com/user/repo/raw/main/model.keras
# Downloaded models cached in: ~/models/cache/
classes = ["aqualy","calcolatrice_casio","bicchiere","iphone13","mouse_wireless","pennarello_giotto","persona","webcam_box"]
label = webcam_predict_label(model, camera_id, classes)
# Capture + predict: returns only label (string)
# Use pre-loaded model object for efficiency
# Use Mind+ list blocks to create class_names list
confidence = webcam_predict_confidence(model, camera_id, classes)
# Capture + predict: returns only confidence (float 0.0-1.0)
# Use pre-loaded model object for efficiency
# Use Mind+ list blocks to create class_names list
send_api_url = "https://api.example.com/predict"
response = send_prediction_data(image, label, confidence, send_api_url)
# Sends JSON with base64 image, label, confidence to REST API
# Returns API response or error information
# Includes timestamp and automatic error handling
print(response)
