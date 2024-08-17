from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Helper function to trigger a Conductor workflow
def trigger_workflow(workflow_name, data):
    url = 'http://127.0.0.1:5000/'
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

@app.route('/rfq', methods=['POST'])
def rfq():
    rfq_data = request.json.get('rfq')
    workflow_result = trigger_workflow("rfq_workflow", {"rfq": rfq_data})
    response = workflow_result.get('output', 'Failed to process RFQ.')
    return jsonify({'response': response})

@app.route('/ioi', methods=['POST'])
def ioi():
    ioi_data = request.json.get('ioi')
    workflow_result = trigger_workflow("ioi_workflow", {"ioi": ioi_data})
    response = workflow_result.get('output', 'Failed to process IOI.')
    return jsonify({'response': response})

@app.route('/settlement', methods=['POST'])
def settlement():
    settlement_data = request.json.get('settlement')
    workflow_result = trigger_workflow("settlement_workflow", {"settlement": settlement_data})
    response = workflow_result.get('output', 'Failed to process settlement.')
    return jsonify({'response': response})

@app.route('/data-distribution', methods=['POST'])
def data_distribution():
    data_dist_data = request.json.get('data_distribution')
    workflow_result = trigger_workflow("data_distribution_workflow", {"data_distribution": data_dist_data})
    response = workflow_result.get('output', 'Failed to process data distribution.')
    return jsonify({'response': response})

if __name__ == "__main__":
    app.run(debug=True)
