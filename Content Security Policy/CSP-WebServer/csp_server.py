from http.server import HTTPServer, SimpleHTTPRequestHandler

class CSPHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # ⛔ 여기에서 iframe 삽입 제한
        # 같은 origin이나 네이버에서 iframe을 삽입하는것을 허용한다.
        self.send_header("Content-Security-Policy", "frame-ancestors 'self' https://www.naver.com")
        super().end_headers()

# 서버 시작
if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), CSPHandler)
    print("✅ CSP 웹 서버 실행 중: http://localhost:8000")
    server.serve_forever()
