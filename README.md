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

1. create Dockerfile
https://hub.docker.com/_/python


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

## load testing with K6
```sh
brew install k6 # for Mac
choco install k6 # for Windows
```


## run load test
```sh
# create loadtest.k6.js
k6 run loadtest.k6.js 

          /\      |‾‾| /‾‾/   /‾‾/   
     /\  /  \     |  |/  /   /  /    
    /  \/    \    |     (   /   ‾‾\  
   /          \   |  |\  \ |  (‾)  | 
  / __________ \  |__| \__\ \_____/ .io

  execution: local
     script: loadtest.k6.js
     output: -

  scenarios: (100.00%) 1 scenario, 1 max VUs, 10m30s max duration (incl. graceful stop):
           * default: 1 iterations for each of 1 VUs (maxDuration: 10m0s, gracefulStop: 30s)


     data_received..................: 284 B 28 B/s
     data_sent......................: 80 B  7.989081322556462 B/s
     http_req_blocked...............: avg=1.07ms min=1.07ms med=1.07ms max=1.07ms p(90)=1.07ms p(95)=1.07ms
     http_req_connecting............: avg=239µs  min=239µs  med=239µs  max=239µs  p(90)=239µs  p(95)=239µs 
     http_req_duration..............: avg=5.01s  min=5.01s  med=5.01s  max=5.01s  p(90)=5.01s  p(95)=5.01s 
       { expected_response:true }...: avg=5.01s  min=5.01s  med=5.01s  max=5.01s  p(90)=5.01s  p(95)=5.01s 
     http_req_failed................: 0.00% ✓ 0                   ✗ 1  
     http_req_receiving.............: avg=5s     min=5s     med=5s     max=5s     p(90)=5s     p(95)=5s    
     http_req_sending...............: avg=75µs   min=75µs   med=75µs   max=75µs   p(90)=75µs   p(95)=75µs  
     http_req_tls_handshaking.......: avg=0s     min=0s     med=0s     max=0s     p(90)=0s     p(95)=0s    
     http_req_waiting...............: avg=7.22ms min=7.22ms med=7.22ms max=7.22ms p(90)=7.22ms p(95)=7.22ms
     http_reqs......................: 1     0.099864/s
     iteration_duration.............: avg=10.01s min=10.01s med=10.01s max=10.01s p(90)=10.01s p(95)=10.01s
     iterations.....................: 1     0.099864/s
     vus............................: 1     min=1                 max=1
     vus_max........................: 1     min=1                 max=1


running (00m10.0s), 0/1 VUs, 1 complete and 0 interrupted iterations
default ✓ [========================] 1 VUs  00m10.0s/10m0s  1/1 iters, 1 per VU
```


--- 

## create script by chrome extention
https://k6.io/docs/test-authoring/create-tests-from-recordings/using-the-browser-recorder/

1. install chrome extention
2. record start
3. load localhost:8080
4. record stop
5. export HAR file
6. convert HAR to k6 script
7. run k6 script

```sh
npm install -g har-to-k6
har-to-k6  new-recording_95235.har -o loadtest.k6.fromHAR.js
k6 run loadtest.k6.fromHAR.js 
```

---

## run load test with 5 users
```sh
time for i in range{1..5}; do curl http://0.0.0.0:8080;done
```

## run load test with 5 users in parallel
```sh
for i in {1..6}; do
    time curl http://0.0.0.0:8080 &
done

--- 

## run multi instance in docker swarm
https://labs.play-with-docker.com/

```sh

docker swarm init --advertise-addr 192.168.0.8
vi main.py
python main.py
vi Dockerfile
docker build -t delay-server-demo .
vi Dockerfile 
docker build -t delay-server-demo .
docker create service delay-server-demo  
docker images
docker create service delay-server-demo  
```

---

## Push custom image to docker hub
```sh
docker login
docker build --tag martinhong/delay-demo:v4 .
docker build --platform linux/amd64 --tag martinhong/delay-demo:v4 . # for M1 Mac
docker image push martinhong/delay-demo:v4
```

## Run custom image in docker swarm
```sh
docker service create   --name my-web-demo   --publish published=8080,target=8080   --replicas 2   martinhong/delay-demo:v4
docker service ls
docker service ps my-web-demo
curl localhost:8080

## Load test with 5 users in sequence and in parallel
```sh
time for i in range{1..5}; do curl http://0.0.0.0:8080;done; time

for i in {1..6}; do
    time curl http://0.0.0.0:8080 &
done

```


# tip
```sh
history | cut -c 8-
```