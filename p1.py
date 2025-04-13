from flask import Flask, jsonify, request
import requests

app = Flask(__name__)

# Replace this with your real API endpoint & key
YOUR_API_KEY = "your_api_key_here"
API_URL = "https://your-api.com/generate-joke"

@app.route('/get_joke', methods=['POST'])
def get_joke():
    try:
        # Example payload - change according to your real API
        payload = {
            "prompt": "Tell me an engineering joke.",
            "max_tokens": 50
        }
        headers = {
            "Authorization": f"Bearer {YOUR_API_KEY}",
            "Content-Type": "application/json"
        }

        # Make the external API call
        response = requests.post(API_URL, headers=headers, json=payload)
        response.raise_for_status()
        result = response.json()

        joke = result.get("joke") or result.get("choices", [{}])[0].get("text", "No joke found.")

        return jsonify({"joke": joke})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)

