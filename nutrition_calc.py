from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from dotenv import load_dotenv
import base64
import os

# load api key from .env file
load_dotenv()

app = Flask(__name__)
client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400
        
    file = request.files['image']
    image_base64 = base64.b64encode(file.read()).decode("utf-8")

    try:
        response = client.responses.create(
            model="gpt-4.1",
            input=[{
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": "Identify the food and return ONLY valid JSON with keys: name, calories, protein, carbs, fat, and recipes (an array of 3 recipe objects with name and instructions)."
                    },
                    {
                        "type": "input_image",
                        "image_url": f"data:image/jpeg;base64,{image_base64}"
                    }
                ]
            }]
        )
        return jsonify({'result': response.output_text})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)