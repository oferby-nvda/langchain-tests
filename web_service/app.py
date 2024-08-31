from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/message', methods=['POST'])
def handle_message():
    # Get the JSON data from the request
    data = request.get_json()

    # Check if 'message' is in the data
    if 'message' in data:
        # Extract the message
        message = data['message']
        
        # Create a response
        response = {
            'message': f'You sent: {message}'
        }
    else:
        # If 'message' is not found, return an error response
        response = {
            'error': 'No message found in request'
        }

    # Return the response as JSON
    return jsonify(response)

if __name__ == '__main__':
    # Run the app on localhost:5000
    app.run(host='0.0.0.0', port=5000, debug=True)