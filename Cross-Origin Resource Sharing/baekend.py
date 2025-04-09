from flask import Flask, request, make_response

app = Flask(__name__)

@app.route("/api/data", methods=["GET", "POST", "OPTIONS"])
def data():
    # OPTIONS 요청: 사전요청(preflight)
    if request.method == "OPTIONS":
        response = make_response()
        response.headers["Access-Control-Allow-Origin"] = "http://localhost:8000"
        response.headers["Access-Control-Allow-Methods"] = "GET, POST, OPTIONS"
        response.headers["Access-Control-Allow-Headers"] = "Content-Type"
        return response

    # 실제 요청
    response = make_response("✅ 실제 응답: 서버가 CORS 허용 중")
    response.headers["Access-Control-Allow-Origin"] = "http://localhost:8000"
    return response

if __name__ == "__main__":
    app.run(port=9000)
