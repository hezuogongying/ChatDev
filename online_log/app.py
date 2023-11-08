import logging
import requests
import os
import json
from flask import Flask, send_from_directory, request, jsonify
import argparse

app = Flask(__name__, static_folder='static')
app.logger.setLevel(logging.ERROR)
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
messages = []
port = []

def send_msg(role, text):
    try:
        data = {"role": role, "text": text}
        response = requests.post(f"http://127.0.0.1:{port[-1]}/send_message", json=data)
    except:
        logging.info("flask app.py did not start for online log")

# BWX_ADD
def baidu_translate(text, termIds=''):
    access_token = get_baidu_token()['access_token']
    url = f"https://aip.baidubce.com/rpc/2.0/mt/texttrans/v1?access_token={access_token}"
    # 判断text是否包含中文
    if text.isascii():
        to_lang = "zh"
    else:
        to_lang = "en"
    payload = {
        "from": "auto",
        "to": to_lang,
        "q": text
    }
    if termIds:
        payload['termIds'] = termIds
    headers = {'Content-Type': 'application/json'}
    # Send request
    response = requests.post(url, params=payload, headers=headers).json()
    if 'error_code' in response:
        print(response)
    else:
        result = response['result']['trans_result']
        result = [i['dst'] for i in result]
        result = ''.join(result)
    return result

@app.route("/en2zh", methods=["POST"])
def translate():
    try:
        text = request.get_json().get('text')
        translated_text = baidu_translate(text)
        with open('baidu_response.json', 'a+', encoding='utf8') as f:
            json.dump(translated_text, f)
        return jsonify({'translatedText': translated_text})
    except Exception as e:
        app.logger.error(f"Error occurred: {e}")
        return jsonify({'error': str(e)}), 500

# BWX_END
@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@app.route("/chain_visualizer")
def chain_visualizer():
    return send_from_directory("static", "chain_visualizer.html")


@app.route("/replay")
def replay():
    return send_from_directory("static", "replay.html")


@app.route("/get_messages")
def get_messages():
    return jsonify(messages)


@app.route("/send_message", methods=["POST"])
def send_message():
    data = request.get_json()
    role = data.get("role")
    text = data.get("text")

    avatarUrl = find_avatar_url(role)

    message = {"role": role, "text": text, "avatarUrl": avatarUrl}
    messages.append(message)
    return jsonify(message)


def find_avatar_url(role):
    role = role.replace(" ", "%20")
    avatar_filename = f"avatars/{role}.png"
    avatar_url = f"/static/{avatar_filename}"
    return avatar_url


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='argparse')
    parser.add_argument('--port', type=int, default=8000, help="port")
    args = parser.parse_args()
    port.append(args.port)
    print(f"Please visit http://127.0.0.1:{port[-1]}/ for the front-end display page. \nIn the event of a port conflict, please modify the port argument (e.g., python3 app.py --port 8012).")
    app.run(host='0.0.0.0', debug=True, port=port[-1])
