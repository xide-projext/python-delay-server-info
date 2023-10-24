import http.server
import socketserver
import time
import socket
def get_container_id():
    with open('/proc/self/cgroup', 'rt') as ifh:
        for line in ifh:
            fields = line.strip().split('/')
            if len(fields) > 1:
                return fields[-1]
    return None

class MyHttpRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

        # # 현재 서버의 IP 주소 얻기
        # host_name = socket.gethostname()
        # host_ip = socket.gethostbyname(host_name)

        # 현재 컨테이너의 ID 얻기
        container_id = get_container_id()

        # 현재 시간 얻기
        current_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

        # 5초 지연
        time.sleep(5)

        # HTML 응답 구성
        response = f"""
        <html>
        <body>
            <p>Container ID: {container_id}</p>
            <p>Current Time: {current_time}</p>
        </body>
        </html>
        """
        
        self.wfile.write(response.encode('utf-8'))

# 8080 포트로 서버 실행
with socketserver.TCPServer(("", 8080), MyHttpRequestHandler) as httpd:
    print("serving at port", 8080)
    httpd.serve_forever()
