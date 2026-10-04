import os
from flask import Flask, request, jsonify

app = Flask(__name__)
message_store = []

@app.route('/api/log', methods=['POST'])
def save_log():
    data = request.json
    message_store.append(data)
    print(f"메시지 수신됨: {data}")
    return jsonify({"status": "success"})

@app.route('/')
def home():
    return "카카오톡 봇 서버 작동 중!"

if __name__ == '__main__':
    # Render가 지정해주는 포트를 동적으로 가져오도록 수정
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
