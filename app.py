from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/check', methods=['POST'])
def check_website():
    data = request.get_json()
    url = data.get('url')
    if not url:
        return jsonify({'status': False, 'error': 'No URL provided'}), 400

    try:
        response = requests.get(url, timeout=5)
        is_up = response.status_code == 200
        return jsonify({'status': is_up, 'url': url})
    except requests.RequestException:
        return jsonify({'status': False, 'url': url})

if __name__ == '__main__':
    app.run()
