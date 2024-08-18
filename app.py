from flask import Flask, render_template, request, jsonify
import requests
import os

app = Flask(__name__)

# Function to trigger the Conductor workflow
def trigger_workflow(workflow_name, data):
    url = os.getenv('CONDUCTOR_URL')  # Get the URL from environment variable
    if url is None:
        raise ValueError("CONDUCTOR_URL environment variable not set")
    
    payload = {
        "name": workflow_name,
        "input": data
    }
    response = requests.post(url, json=payload)
    return response.json()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/kyc', methods=['POST'])
def kyc():
    kyc_data = request.json.get('kyc')
    workflow_result = trigger_workflow("kyc_workflow", {"kyc": kyc_data})
    response = workflow_result.get('output', 'Failed to process KYC.')
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True)
