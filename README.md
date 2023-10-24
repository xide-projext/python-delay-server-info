# Python Delay Server Info
5초 지연 응답을 하는 웹 서버

## Run server 
```sh
python-delay-server-info git:(14-week) ✗ python3.10 main.py                 
serving at port 8080
127.0.0.1 - - [24/Oct/2023 09:36:39] "GET / HTTP/1.1" 200 -
```

## Verify
```sh
python-delay-server-info git:(14-week) ✗ curl localh
ost:8080

<html>
<body>
    <p>Server IP: 192.168.123.103</p>
    <p>Current Time: 2023-10-24 09:36:39</p>
</body>
</html>
%             
```

---

## Build server with Docker
```sh
docker build -t delay-server-demo .
[+] Building 58.0s (10/10) 
```

## Run server with Docker
```sh
docker run -it -p 8080:8080  delay-server-demo
```

## Verify
```sh
python-delay-server-info git:(main) ✗ curl localhost:8080

        <html>
        <body>
            <p>Server IP: 172.17.0.2</p>
            <p>Current Time: 2023-10-24 00:42:03</p>
        </body>
        </html>
        %                                   
```

---
