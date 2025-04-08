from http.server import SimpleHTTPRequestHandler, HTTPServer

class CSPHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        # CSP: 같은 출처와 trusted.com만 iframe 삽입 허용
        self.send_header("Content-Security-Policy", "frame-ancestors 'self' https://trusted.com")
        super().end_headers()

# 서버 실행
if __name__ == "__main__":
    server = HTTPServer(("localhost", 8000), CSPHandler)
    print("CSP 서버 실행 중: http://localhost:8000")
    server.serve_forever()
