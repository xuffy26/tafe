from flask import Flask, request, jsonify
from PIL import Image, UnidentifiedImageError
import io
import base64
from parts_classifier import classify_image

app = Flask(__name__)

@app.route('/identify-part', methods=['POST'])
def identify_part():
    try:
        data = request.get_json()
        if not data or 'image_base64' not in data:
            return jsonify({
                'status': 'error',
                'message': 'Missing "image_base64" field in JSON request body.'
            }), 400

        # Decode the image from base64
        try:
            image_bytes = base64.b64decode(data['image_base64'])
            image = Image.open(io.BytesIO(image_bytes)).convert("RGB")
        except (base64.binascii.Error, UnidentifiedImageError):
            return jsonify({
                'status': 'error',
                'message': 'Invalid image data provided.'
            }), 400

        # Classify the image
        try:
            part = classify_image(image)
        except Exception as e:
            return jsonify({
                'status': 'error',
                'message': f'Error during classification: {str(e)}'
            }), 500

        return jsonify({
            'status': 'success',
            'part_name': part['name'],
            'description': part['description'],
            'common_issues': part['common_issues']
        })

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': f'Unexpected error: {str(e)}'
        }), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
