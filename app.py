from flask import Flask, request, jsonify

app = Flask(__name__)

# 스마트폰이 보내주는 메시지를 잠시 저장할 공간
message_store = []

# 스마트폰이 메시지를 보내면 받아주는 주소 (/api/log)
@app.route('/api/log', methods=['POST'])
def save_log():
    data = request.json
    message_store.append(data)
    print(f"메시지 수신됨: {data}")
    return jsonify({"status": "success"})

# 서버가 잘 켜져 있는지 확인용 페이지
@app.route('/')
def home():
    print("서버가 정상 작동 중입니다.")
    return "카카오톡 봇 서버 작동 중!"

if __name__ == '__main__':
    # 컴퓨터 내부에서 테스트하기 위한 로컬 서버 실행
    app.run(host='0.0.0.0', port=5000)
