from openai import OpenAI
from dotenv import load_dotenv
import base64
import os

# load api key from .env file
load_dotenv()

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# Conver image to base64
# Base64 encodes binary data into ASCII text for safe transmission.
def encode_image(path):
    with open(path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")

# Update image path to your local image file
image_base64 = encode_image("flamegrapes2.jpg")

response = client.responses.create(

    model="gpt-4.1",

    input=[{

        "role": "user",

        "content": [

            {

                "type": "input_text",

                "text": "Identify the food and return JSON with calories, protein, carbs, fat, and 3 recipes."

            },

            {

                "type": "input_image",

                "image_url": f"data:image/jpeg;base64,{image_base64}"

            }

        ]

    }]

)

print(response.output_text)