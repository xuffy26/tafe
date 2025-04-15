from flask import Flask, request, jsonify
from PIL import Image
import io
import base64
from parts_classifier import classify_image

app = Flask(__name__)

@app.route('/identify-part', methods=['POST'])
def identify_part():
    data = request.get_json()

    if not data or 'image_base64' not in data:
        return jsonify({'status': 'error', 'message': 'Missing image_base64 field'}), 400

    try:
        image_bytes = base64.b64decode(data['image_base64'])
        image = Image.open(io.BytesIO(image_bytes))

        part = classify_image(image)

        return jsonify({
            'status': 'success',
            'part_name': part['name'],
            'description': part['description'],
            'common_issues': part['common_issues']
        })

    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(port=5000)
