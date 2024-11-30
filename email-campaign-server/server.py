import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify
from flask_cors import CORS
from linkedin_processor import LinkedinProcessor
from product_processor import ProductProcessor

# Create a Flask app instance
app = Flask(__name__)
CORS(app)

# Instantiate the LinkedinProcessor with your OpenAI API key
# os.environ['OPENAI_API_KEY'] = 
# openai_api_key = os.getenv("OPENAI_API_KEY")

# Load environment variables from .env file
load_dotenv()

# Access the API key
openai_api_key = os.getenv("OPENAI_API_KEY")

linkedin_processor = LinkedinProcessor(api_key=openai_api_key, linkedin="")
product_processor = ProductProcessor(api_key=openai_api_key, message="")

# API to process job description
@app.route('/process_linkedin', methods=['POST'])
def process_linkedin():
    data = request.json
    linkedin = data.get('linkedin', '')
    linkedin_processor.linkedin = linkedin
    result = linkedin_processor.process_linkedin()
    return jsonify(result)

# API to process product information
@app.route('/product_info', methods=['POST'])
def process_product_info():
    data = request.json
    message = data.get('message', '')
    product_processor.message = message
    result = product_processor.call_openai()
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
