""" FLASK """ 
import os
from flask import Flask, request, jsonify
import tensorflow as tf
from tensorflow.python.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
import uuid

# Load the model
model_path = 'models/model.h5'  # Update with the path to your model
loaded_model = load_model(model_path)

# Function to preprocess image
def preprocess_image(image_path, target_size=(150, 150)):
    img = image.load_img(image_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0  # Rescale to [0, 1]
    return img_array

# Get class labels
base_dir = 'data'
train_dir = os.path.join(base_dir, 'train')
class_labels = sorted(os.listdir(train_dir))

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    # Save the uploaded file to a location
    upload_path = 'uploaded_image.jpg'
    file.save(upload_path)

    # Preprocess the image
    img_array = preprocess_image(upload_path)

    # Make prediction
    prediction = loaded_model.predict(img_array)
    predicted_class = np.argmax(prediction, axis=1)[0]
    class_name = class_labels[predicted_class]

    # Generate UUID
    uniqueId = uuid.uuid4().hex
    
    # Return JSON response
    return jsonify({
        requestId: uniqueId,
        data: {
            'class': class_name
        }
    })

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
