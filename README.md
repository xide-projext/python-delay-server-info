# Python Delay Server Info
5초 지연 응답을 하는 웹 서버

## Run server
```
python-delay-server-info git:(14-week) ✗ python3.10 main.py                 
serving at port 8080
127.0.0.1 - - [24/Oct/2023 09:36:39] "GET / HTTP/1.1" 200 -
```

## Verify
```
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