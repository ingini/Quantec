1. 도커 툴박스 설치
2. docker run hello-world 로 실행 잘되는지 확인
3. docker search centos:7
4. docker pull centos:7.2.1511 , centos:7(library/centos) - docker run -i -t --name centos7 centos:7 , docker exec -i -t centos7 /bin/bash
5. docker images 확인
centos container 최초실행
6. docker run- i -t -p 8081:80 --name NginxServer centos:7.2.1511 /bin/bash
7. exit
centos container 시작/종료
8. docker top NginxServer
container 조회
9. docker ps -a       (a를 빼면 실행중인 container 만 조회)
container 재실행
10. docker exec -i -t NginxServer /bin/bash
#최초실행시와 동일한 container id(a9003c86085a)로 접속한 것을 확인할 수 있습니다.


확인작업
os 확인 : grep . /etc/*-release

container 종료시 작업 유지여부 확인 
1. mkdir /home/test1  (container 접속후 디렉토리 생성)
2. ll/ home
container 종료후 다시 접속하여 디렉토리가 그대로 남아있는지 확인
1. exit
2. docker stop NginxServer
3. docker start NginxServer
4. docker exec -i -t NginxServer /bin/bash

PORT 오픈 확인
Container에서 아래와 같이 python에서 제공하는 SimpleHTTPServer를 실행합니다. 80 port를 오픈하는 명령어입니다.
1. python -m SimpleHTTPServer 80

yum update -y

도커에서 centos7 접속
docker exec -i -t NginxServer /bin/bash
docker exec -i -t centos7 /bin/bash








