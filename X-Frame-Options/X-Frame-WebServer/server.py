from http.server import SimpleHTTPRequestHandler, HTTPServer

class MyHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # 🔐 이 줄이 핵심입니다!
        # self.send_header("X-Frame-Options", "DENY")
        self.send_header("X-Frame-Options", "SAMEORIGIN")
        # self.send_header("X-Frame-Options", "ALLOW-FROM https://trusted.com")
        super().end_headers()

# 서버 실행
if __name__ == "__main__":
    # HTTPServer(server_address, RequestHandlerClass)
    # RequestHandlerClass : 요청을 처리할 방식(=응답할 로직)을 정의하는 클래스
    server = HTTPServer(("localhost", 8000), MyHandler)
    print("서버 실행 중: http://localhost:8000")
    server.serve_forever()
