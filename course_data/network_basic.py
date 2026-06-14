def build_network_basic_lectures(code_block, screen_figure):
    udp_client = code_block(
        """
        from socket import * # 해당 모듈을 통해 소켓 생성

        serverName = 'hostname'
        serverPort = 12000

        clientSocket = socket(AF_INET, SOCK_DGRAM) # client socket 생성, IPv4, UDP

        message = Input('Input lowercase sentence:')

        clientSocket.sendto(message.encode(), (serverName, serverPort))

        # 패킷 데이터, 패킷 출발지 주소 할당
        modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

        print(modifiedMessage.decode())

        # 소켓 닫기
        clientSocket.close()
        """,
        "python",
    )
    udp_server = code_block(
        """
        from socket import *

        serverPort = 12000
        serverSocket = socket(AF_INET, SOCK_DGRAM)

        # 12000 포트 번호를 소켓 할당
        serverSocket.bind(('', serverPort))

        print("The server is ready to receive")

        while True:
            # 데이터, 패킷 출발지 주소 저장
            message, clientAddress = serverSocket.recvfrom(2048)

            modifiedMessage = message.decode().upper()

            serverSocket.sendto(modifiedMessage.encode(), clientAddress)
        """,
        "python",
    )
    tcp_client = code_block(
        """
        from socket import *

        serverName = 'servername'
        serverPort = 12000

        # IPv4, TCP 소켓 명시
        clientSocket = socket(AF_INET, SOCK_STREAM)

        # 데이터를 보내기 전 TCP connection이 먼저 이루어져야 한다. (3-way handshake)
        clientSocket.connect((serverName, serverPort))

        sentence = raw_input('Input lowercase sentence:')
        clientSocket.send(sentence.encode())

        modifiedSentence = clientSocket.recv(1024)
        print('From Server: ', modifiedSentence.decode())

        clientSocket.close() # 연결 종료
        """,
        "python",
    )
    tcp_server = code_block(
        """
        from socket import *

        serverPort = 12000
        serverSocket = socket(AF_INET, SOCK_STREAM) # TCP 소켓 생성

        serverSocket.bind(('', serverPort))

        serverSocket.listen(1) # 클라이언트가 문을 두드리기를 기다린다.
        print('The server is ready to receive')

        while True:
            # client가 TCP 연결 요청을 하면, accept()로 연결 소켓 생성
            connectionSocket, addr = serverSocket.accept()
            sentence = connectionSocket.recv(1024).decode()
            capitalizedSentence = sentence.upper()
            connectionSocket.send(capitalizedSentence.encode())

            connectionSocket.close() # 응답을 보내고 연결 소켓을 닫는다.
        """,
        "python",
    )
    http_request_example = code_block(
        """
        POST /whitehat HTTP/2
        Host: www.kitribob.kr
        User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)
        Accept: text/html;
        Accept-Language: ko-KR,ko;
        Connection: close

        form%5Bmember_Id%5D=hello&password=pwnhyo
        """,
        "http",
    )
    http_response_example = code_block(
        """
        HTTP/2 200 OK
        Content-Type: text/html; charset=UTF-8
        Content-Length: 29
        Server: Apache
        Cache-Control: no-store, no-cache, must-revalidate
        Vary: Accept-Encoding

        {"code":1024,"msg":"wub119."}
        """,
        "http",
    )
    wireshark_http_request = code_block(
        """
        GET / HTTP/1.1
        Host: pwnhyo.kr:8080
        Connection: keep-alive
        Cache-Control: max-age=0
        Upgrade-Insecure-Requests: 1
        User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
        Accept-Encoding: gzip, deflate
        Accept-Language: ko,en;q=0.9,en-US;q=0.8
        """,
        "http",
    )
    wireshark_http_response = code_block(
        """
        HTTP/1.1 200 OK
        Date: Mon, 04 Sep 2023 07:34:31 GMT
        Server: Apache/2.4.41 (Ubuntu)
        Content-Length: 22
        Keep-Alive: timeout=5, max=100
        Connection: Keep-Alive
        Content-Type: text/html; charset=UTF-8

        <h1>80 port test</h1>
        """,
        "http",
    )
    wireshark_tcp_stream = code_block(
        """
        GET / HTTP/1.1
        Host: pwnhyo.kr:8080
        Connection: keep-alive
        Cache-Control: max-age=0
        Upgrade-Insecure-Requests: 1
        User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36 Edg/116.0.1938.69
        Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
        Accept-Encoding: gzip, deflate
        Accept-Language: ko,en;q=0.9,en-US;q=0.8

        HTTP/1.1 200 OK
        Date: Mon, 04 Sep 2023 07:34:31 GMT
        Server: Apache/2.4.41 (Ubuntu)
        Content-Length: 22
        Keep-Alive: timeout=5, max=100
        Connection: Keep-Alive
        Content-Type: text/html; charset=UTF-8

        <h1>80 port test</h1>
        """,
        "http",
    )

    nb01 = "네트워크 기초-01-네트워크와-인터넷-기초"
    nb01_outline = screen_figure(
        "network-basic",
        nb01,
        3,
        "네트워크 기초 과목 전체 목차",
        "강의는 네트워크와 인터넷 기초에서 시작해 TCP/IP 계층, 데이터 링크·네트워크·트랜스포트·응용 계층, 와이어샤크 실습, 소켓 프로그래밍으로 이어진다.",
    )
    nb01_network_security = screen_figure(
        "network-basic",
        nb01,
        11,
        "보안 학습에서 네트워크 지식이 필요한 이유",
        "해킹은 대부분 네트워크를 통해 정보 탈취나 시스템 침입을 수행하므로 기본 이해, 공격 벡터 파악, 방어 전략 수립에 네트워크 지식이 필요하다.",
    )
    nb01_attack_scenarios = screen_figure(
        "network-basic",
        nb01,
        15,
        "네트워크 관련 공격 시나리오",
        "MITM, ARP Spoofing, DDoS, Wireless attack처럼 네트워크 자체를 노리는 공격과 SQL Injection, RCE처럼 네트워크를 거치는 공격이 함께 존재한다.",
    )
    nb01_network_definition = screen_figure(
        "network-basic",
        nb01,
        23,
        "네트워크와 컴퓨터 네트워크의 정의",
        "네트워크는 여러 객체가 연결되어 정보를 교환하는 구조이고, 컴퓨터 네트워크는 컴퓨터 기기들이 연결되어 정보를 공유하는 시스템이다.",
    )
    nb01_lan_wan = screen_figure(
        "network-basic",
        nb01,
        27,
        "LAN과 WAN의 관계",
        "LAN은 제한된 영역의 근거리 네트워크이고, WAN은 여러 LAN이 도시·국가·대륙 단위로 확장되어 연결된 네트워크다.",
    )
    nb01_packet_route = screen_figure(
        "network-basic",
        nb01,
        31,
        "패킷과 경로",
        "데이터는 segment 단위로 나뉘고 header가 붙어 packet으로 전달되며, 패킷이 목적지까지 거쳐 가는 일련의 링크와 스위치를 route 또는 path라고 부른다.",
    )
    nb01_isp = screen_figure(
        "network-basic",
        nb01,
        35,
        "ISP와 인터넷 접속 구조",
        "ISP는 end system에게 가정용 접속, 고속 LAN, 이동통신 같은 네트워크 접속을 제공하고 하위 ISP는 국가·국제 상위 ISP를 통해 서로 연결된다.",
    )
    nb01_protocol = screen_figure(
        "network-basic",
        nb01,
        39,
        "프로토콜의 의미",
        "프로토콜은 메시지 형식, 순서, 전송과 수신 시 수행할 작업을 정한 통신 규약이며 TCP, IP, HTTP, 802.11 등이 대표 예다.",
    )
    nb01_tcp_ip = screen_figure(
        "network-basic",
        nb01,
        43,
        "TCP와 IP",
        "TCP는 데이터 전송의 제어와 관리를 담당하고, IP는 라우터와 end system 사이에서 송수신되는 패킷 포맷과 라우팅 역할을 담당한다.",
    )
    nb02 = "네트워크 기초-02-프로토콜-계층-구조"
    nb02_layer_model = screen_figure(
        "network-basic",
        nb02,
        3,
        "계층 구조와 Service Model",
        "인터넷 프로토콜 스택은 Application, Transport, Network, Link, Physical의 5계층으로 설명되며, 각 계층은 상위 계층에 서비스를 제공하고 하위 계층 서비스를 사용한다.",
    )
    nb02_physical = screen_figure(
        "network-basic",
        nb02,
        7,
        "Physical Layer",
        "물리 계층의 단위는 bit이며, 프레임 내부의 각 비트를 꼬임쌍선이나 단일 모드 광케이블 같은 실제 전송 매체를 통해 다음 노드로 이동시킨다.",
    )
    nb02_link = screen_figure(
        "network-basic",
        nb02,
        11,
        "Data Link Layer",
        "데이터 링크 계층의 단위는 frame이며, 전체 프레임을 한 네트워크 요소에서 이웃 네트워크 요소로 이동시킨다.",
    )
    nb02_network = screen_figure(
        "network-basic",
        nb02,
        13,
        "Network Layer",
        "네트워크 계층은 IP 계층이라고도 하며, datagram을 단위로 한 호스트에서 다른 호스트까지 최적 경로를 선택하고 전송한다.",
    )
    nb02_transport = screen_figure(
        "network-basic",
        nb02,
        17,
        "Transport Layer",
        "전송 계층은 segment를 단위로 클라이언트와 서버의 애플리케이션 계층 메시지를 전달하며, 대표 프로토콜로 TCP와 UDP가 있다.",
    )
    nb02_application = screen_figure(
        "network-basic",
        nb02,
        21,
        "Application Layer",
        "응용 계층은 message를 단위로 네트워크 애플리케이션 간 정보를 교환하며 HTTP, SMTP, FTP 같은 프로토콜을 사용한다.",
    )
    nb02_encapsulation = screen_figure(
        "network-basic",
        nb02,
        23,
        "캡슐화",
        "기존 메시지에 송수신에 필요한 header가 계층별로 붙으면서 message, segment, packet 또는 datagram, frame으로 감싸져 내려간다.",
    )
    nb03 = "네트워크 기초-03-데이터-링크-계층"
    nb03_nodes_links = screen_figure(
        "network-basic",
        nb03,
        3,
        "링크 계층 소개: 노드와 링크",
        "노드는 링크 계층 프로토콜을 실행하는 호스트, 라우터, 스위치, AP 같은 장치이고, 링크는 인접한 노드를 연결하는 통신 채널이다.",
    )
    nb03_services = screen_figure(
        "network-basic",
        nb03,
        7,
        "링크 계층이 제공하는 서비스",
        "링크 계층은 framing, link access, 신뢰적 전달, 오류 검출과 정정 서비스를 제공하며 하드웨어와 소프트웨어의 조합으로 구현된다.",
    )
    nb03_mac = screen_figure(
        "network-basic",
        nb03,
        11,
        "링크 계층 주소체계와 MAC 주소",
        "스위치는 IP 주소 체계를 쓰지 않고 링크 계층 고유 주소인 MAC 주소를 사용하며, broadcast address는 FF-FF-FF-FF-FF-FF로 모든 어댑터에게 보낸다.",
    )
    nb03_arp = screen_figure(
        "network-basic",
        nb03,
        19,
        "ARP: IP 주소에서 MAC 주소 찾기",
        "ARP는 네트워크 계층 주소와 링크 계층 주소 사이를 변환해 IP 주소를 가진 호스트의 MAC 주소를 알아내는 프로토콜이다.",
    )
    nb03_other_subnet = screen_figure(
        "network-basic",
        nb03,
        23,
        "다른 서브넷으로 데이터그램을 보낼 때",
        "목적지 호스트가 같은 서브넷에 없으면 최종 호스트의 MAC 주소로 바로 보내는 것이 아니라 라우터 인터페이스의 MAC 주소로 전달한다.",
    )
    nb03_ethernet_frame = screen_figure(
        "network-basic",
        nb03,
        31,
        "Ethernet 프레임 구조",
        "Ethernet 프레임은 목적지 MAC, 출발지 MAC, type, data, CRC 등을 포함하고 data 필드에는 IP 데이터그램이 운반된다.",
    )
    nb03_ethernet_unreliable = screen_figure(
        "network-basic",
        nb03,
        35,
        "Ethernet의 비연결형·비신뢰적 서비스",
        "Ethernet은 CRC로 프레임을 검사하지만 응답이나 부정 확인 응답을 보내지 않고, 실패한 프레임은 폐기한다.",
    )
    nb03_switch_router = screen_figure(
        "network-basic",
        nb03,
        39,
        "링크 계층 스위치와 라우터 비교",
        "스위치는 MAC 주소를 사용하는 2계층 패킷 교환기이고, 라우터는 네트워크 계층 주소를 사용하는 3계층 패킷 교환기다.",
    )
    nb04 = "네트워크 기초-04-네트워크-계층"
    nb04_overview = screen_figure(
        "network-basic",
        nb04,
        7,
        "Network Layer 개요",
        "네트워크 계층은 IP 계층이라고도 하며, datagram을 단위로 한 호스트에서 다른 호스트까지 최적 경로를 선택하고 전송한다.",
    )
    nb04_host_to_host = screen_figure(
        "network-basic",
        nb04,
        11,
        "호스트 대 호스트 전달",
        "네트워크 계층은 H1의 전송 계층 segment를 추출해 H2의 네트워크 계층을 거쳐 전송 계층까지 전달하는 역할을 한다.",
    )
    nb04_planes = screen_figure(
        "network-basic",
        nb04,
        15,
        "라우터의 데이터 평면과 제어 평면",
        "데이터 평면은 입력 링크에서 출력 링크로 datagram을 전달하고, 제어 평면은 로컬 포워딩과 라우터별 포워딩을 다룬다.",
    )
    nb04_best_effort = screen_figure(
        "network-basic",
        nb04,
        19,
        "인터넷 네트워크 계층의 최선형 서비스",
        "인터넷 네트워크 계층은 순서, 전달, 지연, 최소 대역폭을 보장하지 않는 best-effort service를 제공한다.",
    )
    nb04_ipv4_datagram = screen_figure(
        "network-basic",
        nb04,
        27,
        "IPv4 데이터그램 포맷",
        "IPv4 데이터그램은 보통 20byte 헤더를 가지며 version, header length, type of service, datagram length, TTL, checksum, source/destination IP, data 필드를 포함한다.",
    )
    nb04_subnet = screen_figure(
        "network-basic",
        nb04,
        31,
        "서브넷과 IP 주소",
        "모든 호스트와 라우터는 IP 데이터그램을 송수신하기 위해 IP 주소가 필요하고, 서브넷은 IP 네트워크를 더 작고 관리하기 쉬운 부분으로 나눈 것이다.",
    )
    nb04_class_address = screen_figure(
        "network-basic",
        nb04,
        35,
        "IPv4 클래스 주소체계",
        "클래스 주소체계는 필요한 호스트 IP 개수에 따라 네트워크 영역과 호스트 영역의 크기를 다르게 할당한다.",
    )
    nb04_nat_dhcp = screen_figure(
        "network-basic",
        nb04,
        39,
        "Broadcast, NAT, DHCP",
        "broadcast 주소는 같은 서브넷의 모든 호스트에게 전달하고, NAT는 하나의 공용 IP로 여러 사설 IP가 통신하게 하며, DHCP는 IP 주소와 관련 설정을 자동으로 할당한다.",
    )
    nb04_ipv6 = screen_figure(
        "network-basic",
        nb04,
        43,
        "IPv6",
        "IPv6는 IPv4 주소 공간 고갈에 대응해 128bit 주소, 간소화된 40byte 고정 헤더, flow labeling을 제공한다.",
    )
    nb05 = "네트워크 기초-05-트랜스포트-계층"
    nb05_overview = screen_figure(
        "network-basic",
        nb05,
        7,
        "Transport Layer 개요",
        "전송 계층은 application message에 transport-layer header를 붙여 segment를 만들고, TCP와 UDP를 대표 프로토콜로 사용한다.",
    )
    nb05_process = screen_figure(
        "network-basic",
        nb05,
        11,
        "프로세스 간 논리적 통신",
        "네트워크 계층이 host-to-host 통신을 제공한다면, 전송 계층은 서로 다른 호스트의 프로세스 사이에 process-to-process logical communication을 제공한다.",
    )
    nb05_multiplexing = screen_figure(
        "network-basic",
        nb05,
        19,
        "다중화와 역다중화",
        "목적지 전송 계층은 네트워크 계층에서 받은 segment를 socket으로 전달하며, 각 socket은 port number로 식별된다.",
    )
    nb05_udp_header = screen_figure(
        "network-basic",
        nb05,
        23,
        "UDP와 UDP header",
        "UDP는 unreliable, connectionless transport protocol이며, source port, dest port, length, checksum으로 구성된 8byte 헤더를 사용한다.",
    )
    nb05_udp_tradeoffs = screen_figure(
        "network-basic",
        nb05,
        27,
        "UDP의 장점과 단점",
        "UDP는 애플리케이션 제어, 연결 설정 생략, 상태 정보 없음, 작은 헤더 때문에 빠르지만 congestion control을 제공하지 않는다.",
    )
    nb05_tcp_header = screen_figure(
        "network-basic",
        nb05,
        35,
        "TCP와 TCP header",
        "TCP는 reliable data transfer, connection-oriented service, flow control, congestion control을 제공하며 sequence number와 acknowledgement number를 핵심 필드로 사용한다.",
    )
    nb05_mss_mtu = screen_figure(
        "network-basic",
        nb05,
        43,
        "MSS와 MTU",
        "MSS는 TCP segment에 담을 수 있는 최대 application data 크기이며, 보통 MTU에서 IP header와 TCP header를 뺀 값으로 계산한다.",
    )
    nb05_seq_ack = screen_figure(
        "network-basic",
        nb05,
        47,
        "Sequence number와 acknowledgement number",
        "Sequence number는 segment의 첫 번째 byte stream 번호이고, acknowledgement number는 상대에게서 기대하는 다음 byte의 sequence number다.",
    )
    nb05_timeout = screen_figure(
        "network-basic",
        nb05,
        59,
        "신뢰성, retransmission timeout, RTT",
        "TCP는 손실 segment를 찾기 위해 timeout과 재전송을 사용하며, timeout은 왕복 시간인 RTT보다 조금 더 크게 잡아야 한다.",
    )
    nb05_three_way = screen_figure(
        "network-basic",
        nb05,
        63,
        "TCP 3-way handshake",
        "TCP 연결 시작은 client SYN, server SYN/ACK, client ACK의 세 단계로 이루어지고, 세 번째 메시지부터 payload가 포함될 수 있다.",
    )
    nb05_four_way = screen_figure(
        "network-basic",
        nb05,
        67,
        "TCP 4-way termination",
        "TCP 연결 종료는 FIN, ACK, FIN, ACK 흐름으로 진행되며, 연결이 끝나면 호스트의 버퍼와 메모리 같은 자원이 회수된다.",
    )
    nb05_tcp_udp = screen_figure(
        "network-basic",
        nb05,
        70,
        "TCP와 UDP의 차이",
        "TCP는 연결형, 상태 저장, 바이트 스트림, 순서 보장, 신뢰성, handshake와 flow control을 제공하고, UDP는 비연결형, stateless, datagram 기반, 빠른 전송을 제공한다.",
    )
    nb06 = "네트워크 기초-06-애플리케이션-계층"
    nb06_network_apps = screen_figure(
        "network-basic",
        nb06,
        7,
        "네트워크 애플리케이션 구조",
        "네트워크 애플리케이션은 서로 다른 위치의 end system에서 동작하며 network를 통해 통신하고, 대표 구조로 client-server와 peer-to-peer가 있다.",
    )
    nb06_client_p2p = screen_figure(
        "network-basic",
        nb06,
        11,
        "Client-server와 P2P 구조 비교",
        "Client-server 구조는 항상 동작하는 server와 고정 IP 주소를 전제로 하고, P2P 구조는 peer들이 직접 통신하며 자기 확장성과 비용 효율성을 가진다.",
    )
    nb06_socket = screen_figure(
        "network-basic",
        nb06,
        15,
        "프로세스 간 통신과 소켓",
        "Socket은 host의 application layer와 transport layer 사이의 interface이며, process가 네트워크를 통해 message를 교환하는 출입구 역할을 한다.",
    )
    nb06_http_features = screen_figure(
        "network-basic",
        nb06,
        19,
        "HTTP의 stateless와 connectionless 특성",
        "HTTP는 여러 resource를 송수신하기 위한 application layer protocol이며, stateless와 connectionless 특성을 가진다.",
    )
    nb06_http_request = screen_figure(
        "network-basic",
        nb06,
        27,
        "HTTP request message 구조",
        "HTTP 요청 메시지는 시작줄, header, body로 구성되고 시작줄에는 method, path, HTTP version이 들어간다.",
    )
    nb06_http_response = screen_figure(
        "network-basic",
        nb06,
        39,
        "HTTP response message 구조",
        "HTTP 응답 메시지는 상태줄, header, body로 구성되고 상태줄에는 protocol version, status code, status text가 들어간다.",
    )
    nb06_https = screen_figure(
        "network-basic",
        nb06,
        47,
        "HTTP와 HTTPS",
        "HTTP는 암호화되지 않은 메시지가 노출될 수 있지만, HTTPS는 HTTP에 암호화를 더해 sniffing 상황에서도 기밀성을 보장한다.",
    )
    nb06_dns_lookup = screen_figure(
        "network-basic",
        nb06,
        51,
        "DNS: 호스트 이름을 IP 주소로 변환",
        "DNS는 사용자가 입력한 host name을 router와 host가 처리할 수 있는 IP address로 변환해 주는 application layer service다.",
    )
    nb06_dns_hierarchy = screen_figure(
        "network-basic",
        nb06,
        59,
        "계층적·분산 DNS 서버 구조",
        "DNS는 단일 중앙집중형 데이터베이스의 장애와 과부하 문제를 피하기 위해 root, TLD, authoritative DNS server 계층으로 전 세계에 분산된다.",
    )
    nb07 = "네트워크 기초-07-와이어샤크-실습-패킷-분석"
    nb07_intro = screen_figure(
        "network-basic",
        nb07,
        7,
        "Wireshark와 패킷 캡처의 목적",
        "Wireshark는 호스트에서 발생하는 네트워크 패킷을 캡처하고 분석하는 도구이며 공격자의 sniffing, 방어자의 침해사고 대응과 포렌식 모두에 쓰일 수 있다.",
    )
    nb07_install = screen_figure(
        "network-basic",
        nb07,
        11,
        "공식 다운로드와 캡처 인터페이스 선택",
        "공식 홈페이지에서 운영체제에 맞는 버전을 설치하고, 실행 후 Wi-Fi 같은 실제 통신 인터페이스를 선택해 캡처를 시작한다.",
    )
    nb07_http_filter = screen_figure(
        "network-basic",
        nb07,
        23,
        "HTTP display filter 적용",
        "캡처 후 display filter에 http를 입력하면 GET / HTTP/1.1 request와 HTTP/1.1 200 OK response처럼 HTTP 통신만 모아 볼 수 있다.",
    )
    nb07_request = screen_figure(
        "network-basic",
        nb07,
        27,
        "HTTP GET request 세부 항목",
        "Request packet 158에는 Host, Connection, Cache-Control, Upgrade-Insecure-Requests, User-Agent, Accept, Accept-Encoding, Accept-Language와 Full request URI가 보인다.",
    )
    nb07_response = screen_figure(
        "network-basic",
        nb07,
        31,
        "HTTP 200 OK response 세부 항목",
        "Response packet 165에는 Date, Server: Apache/2.4.41 (Ubuntu), Content-Length: 22, Keep-Alive, Connection, Content-Type과 request frame 연결 정보가 보인다.",
    )
    nb07_body = screen_figure(
        "network-basic",
        nb07,
        35,
        "Response body와 브라우저 렌더링",
        "Wireshark의 Line-based text data에는 <h1>80 port test</h1>가 보이고, 브라우저 화면에도 같은 문장이 H1 요소로 렌더링된다.",
    )
    nb07_layer_stack = screen_figure(
        "network-basic",
        nb07,
        39,
        "Frame, Ethernet, IPv4, TCP, HTTP 계층 구조",
        "하나의 HTTP response packet 안에서 Frame, Ethernet II, Internet Protocol Version 4, Transmission Control Protocol, Hypertext Transfer Protocol이 순서대로 보인다.",
    )
    nb07_ipv4 = screen_figure(
        "network-basic",
        nb07,
        47,
        "IPv4 헤더 필드",
        "IPv4 header는 version, header length, differentiated services field, total length, identification, TTL, protocol, checksum, source address, destination address를 포함한다.",
    )
    nb07_tcp = screen_figure(
        "network-basic",
        nb07,
        55,
        "TCP 헤더와 포트·순서 번호",
        "Response TCP segment는 source port 8080, destination port 62378, sequence number 1, acknowledgement number 478, payload length 226을 보여 준다.",
    )
    nb07_payload = screen_figure(
        "network-basic",
        nb07,
        59,
        "TCP payload 안의 HTTP message",
        "TCP payload 영역을 선택하면 byte pane에서 HTTP/1.1 200 OK header와 <h1>80 port test</h1> body가 TCP data로 실려 있음을 확인할 수 있다.",
    )
    nb07_stream = screen_figure(
        "network-basic",
        nb07,
        64,
        "Follow TCP Stream",
        "Follow TCP Stream은 하나의 TCP 연결에서 오간 HTTP request와 response를 대화 흐름처럼 이어서 보여 준다.",
    )
    nb07_ip_filter = screen_figure(
        "network-basic",
        nb07,
        67,
        "서버 IP 기준 display filter",
        "ip.addr == 122.46.96.85 필터를 적용하면 해당 서버와 오간 SYN, SYN/ACK, ACK, HTTP request, HTTP response 패킷을 함께 볼 수 있다.",
    )
    nb07_flow_graph = screen_figure(
        "network-basic",
        nb07,
        71,
        "Flow Graph에서 보는 TCP 3-way handshake",
        "Statistics의 Flow Graph에서 Limit to display filter를 켜면 SYN, SYN/ACK, ACK 이후 GET / HTTP/1.1과 HTTP/1.1 200 OK가 이어지는 흐름을 확인할 수 있다.",
    )
    nb08 = "네트워크 기초-08-소켓-프로그래밍"
    nb08_socket_intro = screen_figure(
        "network-basic",
        nb08,
        3,
        "소켓 프로그래밍의 이해",
        "소켓은 호스트의 애플리케이션과 트랜스포트 계층 사이의 인터페이스이며, 이 강의는 client/server 애플리케이션을 UDP와 TCP socket으로 만드는 흐름을 다룬다.",
    )
    nb08_udp_flow = screen_figure(
        "network-basic",
        nb08,
        7,
        "UDP socket programming 흐름",
        "UDP에서는 server와 client가 각각 socket(AF_INET, SOCK_DGRAM)을 만들고, client가 server IP와 port를 담은 datagram을 보내며 server는 client address로 응답한다.",
    )
    nb08_udp_client = screen_figure(
        "network-basic",
        nb08,
        11,
        "UDPClient.py 코드",
        "UDP client는 clientSocket을 만들고 message를 입력받아 sendto로 serverName/serverPort에 보내며, recvfrom으로 응답과 serverAddress를 받는다.",
    )
    nb08_udp_server = screen_figure(
        "network-basic",
        nb08,
        15,
        "UDPServer.py 코드",
        "UDP server는 12000번 port에 bind한 뒤 while True에서 recvfrom으로 message와 clientAddress를 받고, 대문자로 변환한 뒤 sendto로 돌려준다.",
    )
    nb08_tcp_concept = screen_figure(
        "network-basic",
        nb08,
        19,
        "TCP socket programming 개념",
        "TCP client는 welcome socket의 IP와 port를 통해 연결을 만들고, server는 connection socket을 생성해 여러 client와 신뢰성 있는 연결을 제공한다.",
    )
    nb08_tcp_flow = screen_figure(
        "network-basic",
        nb08,
        23,
        "TCP socket programming 흐름",
        "Server는 socket 생성 후 accept로 incoming connection을 기다리고, client는 connect로 TCP connection setup을 완료한 뒤 request와 reply를 주고받는다.",
    )
    nb08_tcp_client = screen_figure(
        "network-basic",
        nb08,
        25,
        "TCPClient.py 코드",
        "TCP client는 socket(AF_INET, SOCK_STREAM)을 만들고 connect로 3-way handshake를 먼저 수행한 뒤 send, recv, close 순서로 동작한다.",
    )
    nb08_tcp_server = screen_figure(
        "network-basic",
        nb08,
        27,
        "TCPServer.py 코드",
        "TCP server는 SOCK_STREAM socket을 bind/listen한 뒤 accept로 connectionSocket을 만들고, recv, upper, send, close 순서로 응답한다.",
    )

    return [
        {
            "id": "1-1",
            "title": "네트워크와 인터넷 기초",
            "subtitle": "네트워크가 왜 보안 학습의 기반인지 이해하고, 인터넷·패킷·ISP·프로토콜·TCP/IP의 큰 그림을 잡는다.",
            "tags": ["네트워크 개요", "인터넷", "보안"],
            "objectives": [
                "네트워크 지식이 해킹, 방어, 포렌식, 취약점 분석에 필요한 이유를 설명한다.",
                "LAN, WAN, 인터넷, 호스트, 패킷, 패킷 스위치, 경로, ISP의 의미를 구분한다.",
                "프로토콜이 통신 규칙이며 TCP/IP가 인터넷의 핵심 프로토콜 묶음임을 이해한다.",
            ],
            "sections": [
                {
                    "heading": "멘토 소개와 과목 방향",
                    "body": f"""
                    <p>강의는 이효민 멘토의 소개로 시작한다. 멘토는 BoB 9기 취약점 분석 트랙 Best 10 수료생이며, 고려대학교 사이버국방 관련 전공에서 공부하고 있고, CYKor 해킹 동아리 부회장 역할을 맡고 있다고 설명한다. 주 관심사는 offensive security, 해킹 기술, 최근의 AI 모델 공격이다.</p>
                    <p>네트워크 기초 과목은 보안을 공부할 때 반드시 필요한 TCP/IP 기반 네트워크 지식을 실용적으로 정리하는 수업이다. 강의의 기준 교재로는 <strong>Computer Networking: A Top-Down Approach 8판</strong>이 언급된다. 다만 이 수업은 모든 네트워크 이론 모델을 깊게 다루기보다, 실제 패킷 분석과 네트워크 프로그래밍에서 자주 마주치는 TCP/IP 계층 모델을 중심으로 진행된다.</p>
                    {nb01_outline}
                    <div class="timeline">
                      <div><strong>1</strong><p>네트워크와 인터넷 기초를 이해한다.</p></div>
                      <div><strong>2</strong><p>프로토콜 계층 구조와 TCP/IP 모델을 이해한다.</p></div>
                      <div><strong>3-6</strong><p>데이터 링크, 네트워크, 트랜스포트, 응용 계층을 차례로 본다.</p></div>
                      <div><strong>7</strong><p>Wireshark로 실제 패킷을 분석한다.</p></div>
                      <div><strong>8</strong><p>TCP/UDP 소켓 프로그래밍으로 서버와 클라이언트를 구현한다.</p></div>
                    </div>
                    <p>강사는 네트워크 이론에는 여러 모델과 설명 방식이 있지만, 이 강의에서는 보안 실습에 바로 연결되는 TCP/IP 레이어 모델을 중심으로 다룬다고 설명한다. 따라서 학생은 각 개념을 단순 암기하기보다 “나중에 패킷을 볼 때 어디에 해당하는가”, “공격자가 어느 계층을 건드리는가”라는 관점으로 읽으면 좋다.</p>
                    """,
                },
                {
                    "heading": "왜 네트워크가 보안의 기반인가",
                    "body": f"""
                    <p>멘토는 현대 사회가 네트워크로 이루어져 있다고 설명한다. 인터넷 뱅킹 앱, 소셜 네트워크 서비스, 웹 서비스, 모바일 앱처럼 일상에서 사용하는 대부분의 서비스가 네트워크를 통해 동작한다. 따라서 네트워크 시스템이 위협을 받으면 개인정보 유출, 기업의 금전적 손실, 서비스 마비 같은 심각한 결과가 발생할 수 있다.</p>
                    <p>해킹도 네트워크와 분리해서 생각하기 어렵다. 정보 탈취, 시스템 침입, 원격 취약점 공격, 방어 전략 수립이 모두 네트워크 통신 흐름을 기반으로 한다. 그래서 네트워크를 이해한다는 것은 단순히 인터넷이 연결되는 방식을 아는 것이 아니라, 취약점이 어디에서 생기고 공격자가 어떤 통로로 접근하며 방어자가 무엇을 관찰해야 하는지 이해하는 일이다.</p>
                    {nb01_network_security}
                    <p>슬라이드는 네트워크 지식이 필요한 이유를 세 단계로 정리한다. 첫째, 네트워크 기본 이해가 필요하다. 해킹은 대부분 네트워크를 통해 정보를 탈취하거나 시스템에 침입한다. 둘째, 공격 벡터를 파악해야 한다. 네트워크에는 프로토콜 자체의 취약점, 설정 실수, 신뢰 관계 문제처럼 다양한 취약점이 존재한다. 셋째, 방어 전략 수립이 가능해야 한다. 네트워크 흐름을 알아야 어떤 지점에서 모니터링하고 차단할지 결정할 수 있다.</p>
                    <table>
                      <thead><tr><th>공격 유형</th><th>강의에서의 설명</th><th>학습 포인트</th></tr></thead>
                      <tbody>
                        <tr><td>MITM</td><td>공격자가 통신 중간에 위치해 패킷을 감청하거나 도청한다.</td><td>평문 통신, 인증, 암호화의 중요성을 이해한다.</td></tr>
                        <tr><td>ARP spoofing</td><td>ARP 프로토콜 동작을 조작해 기대와 다른 네트워크 흐름을 만든다.</td><td>링크 계층 주소 변환과 신뢰 모델을 이해한다.</td></tr>
                        <tr><td>DDoS</td><td>대량의 트래픽이나 부하로 서버와 네트워크를 마비시킨다.</td><td>가용성, 트래픽 처리, 방어 전략을 이해한다.</td></tr>
                        <tr><td>무선 네트워크 공격</td><td>Wi-Fi 사용이 보편화되면서 무선 구간 보안도 중요해졌다.</td><td>유선뿐 아니라 무선 매체도 공격면임을 기억한다.</td></tr>
                      </tbody>
                    </table>
                    """,
                },
                {
                    "heading": "네트워크를 거쳐 일어나는 공격",
                    "body": f"""
                    <p>네트워크 자체를 직접 공격하는 경우도 있지만, 네트워크를 통로로 삼아 애플리케이션 취약점을 공격하는 경우도 많다. 강의에서는 이후 수업에서 다룰 클라이언트 사이드 공격, 서버 사이드 공격, 웹 애플리케이션 공격을 예로 든다. SQL injection 같은 웹 공격은 HTTP 요청을 통해 서버 애플리케이션으로 전달되고, 비디오 플레이어·데스크톱 프로그램·모바일 앱의 RCE 취약점도 네트워크로 입력을 받아 발생할 수 있다.</p>
                    {nb01_attack_scenarios}
                    <p>직접적인 네트워크 공격에는 MITM Attack, ARP Spoofing, DDoS, Wireless attack이 있다. MITM은 공격자가 통신 중간에 위치해 패킷을 감청하거나 조작하는 공격이다. ARP Spoofing은 ARP 프로토콜 동작을 속여 원래 기대한 흐름과 다른 경로로 트래픽이 가게 만든다. DDoS는 네트워크 트래픽과 시스템 부하를 과도하게 발생시켜 서비스를 마비시키는 공격이다. 무선 네트워크 공격은 Wi-Fi 같은 무선 구간이 보편화되면서 중요해진 영역이다.</p>
                    <p>사례로는 2009년 7월 7일 국내 주요 정부기관, 포털, 은행 사이트가 마비된 7.7 DDoS 공격이 언급된다. 또 Stuxnet은 이란 핵시설 같은 물리 시스템을 노린 공격 사례로 소개된다. 이 두 사례는 네트워크 공격이 단순한 화면 오류를 넘어 사회 기반 시설과 실제 물리 시스템에도 영향을 줄 수 있음을 보여 준다.</p>
                    <div class="callout">강의의 결론은 명확하다. 보안을 공부하려면 네트워크를 “인터넷 연결 설정” 정도가 아니라 공격과 방어가 실제로 지나가는 경로로 이해해야 한다.</div>
                    """,
                },
                {
                    "heading": "네트워크, LAN, WAN, 인터넷",
                    "body": f"""
                    <p>네트워크라는 단어는 컴퓨터에만 쓰이지 않는다. 사람, 기기, 시스템, 조직이 서로 연결되어 정보를 주고받는 구조를 넓게 네트워크라고 부른다. 택배 시스템, 인간관계망도 넓은 의미의 네트워크가 될 수 있다. 이 과목에서 다루는 컴퓨터 네트워크는 여러 컴퓨팅 장치가 서로 연결되어 정보를 공유하는 시스템이다.</p>
                    {nb01_network_definition}
                    <table>
                      <thead><tr><th>용어</th><th>의미</th><th>강의에서의 감각</th></tr></thead>
                      <tbody>
                        <tr><td>LAN</td><td>Local Area Network</td><td>물리적·논리적으로 제한된 영역의 근거리 네트워크다.</td></tr>
                        <tr><td>WAN</td><td>Wide Area Network</td><td>여러 LAN이 연결되어 도시, 국가, 대륙 규모로 커진 네트워크다.</td></tr>
                        <tr><td>인터넷</td><td>network of networks</td><td>전 세계의 수많은 네트워크와 컴퓨팅 장치가 연결된 거대한 네트워크다.</td></tr>
                        <tr><td>호스트·엔드 시스템</td><td>통신의 끝점</td><td>PC, 스마트폰, 서버처럼 데이터를 보내고 받는 종단 장치다.</td></tr>
                      </tbody>
                    </table>
                    {nb01_lan_wan}
                    <p>LAN은 집, 학교, 회사의 한 구역처럼 물리적 또는 논리적으로 제한된 영역 안의 네트워크다. WAN은 이런 LAN들이 더 넓게 연결된 형태로, 도시와 국가, 대륙 간 연결까지 포함한다. 슬라이드의 그림처럼 작은 LAN들이 더 큰 WAN 구조의 일부가 되고, 그 WAN들이 연결되면서 인터넷이라는 더 큰 구조가 만들어진다.</p>
                    <p>인터넷이라는 이름은 1973년에 명명되었다고 강의에서 설명한다. 인터넷은 오래된 기술처럼 느껴지지만, 그 이름 자체는 50여 년의 역사 속에서 빠르게 발전했고 그동안 해킹 기술과 방어 기술도 함께 고도화되었다.</p>
                    """,
                },
                {
                    "heading": "패킷, 스위치, 경로, ISP",
                    "body": f"""
                    <p>패킷은 송신 엔드 시스템에서 수신 엔드 시스템으로 보내지는 데이터 단위다. 큰 데이터를 한 번에 통째로 보내지 않고, 세그먼트 같은 작은 단위로 나눈 뒤 헤더를 붙여 전송한다. 목적지에서는 이 조각들을 다시 조립해 원래 데이터를 복원한다.</p>
                    {nb01_packet_route}
                    <p>패킷 스위치는 도착한 패킷을 광케이블, 구리선 같은 출력 통신 링크로 전달하는 장비다. 패킷이 어떤 장비를 거쳐 목적지까지 가는 전체 흐름을 경로, route, path라고 부른다. 이후 네트워크 계층에서 이 경로를 선택하는 라우팅이 중요한 개념으로 다시 등장한다.</p>
                    {nb01_isp}
                    <p>인터넷이 전 세계 규모로 연결되려면 ISP, 즉 Internet Service Provider가 필요하다. 국내 예로는 LG U+, SKT, KT 같은 사업자를 들 수 있다. 가정과 회사는 지역 또는 국가 ISP에 연결되고, 이 ISP들은 다시 상위 티어 ISP와 연결되어 더 넓은 인터넷을 구성한다.</p>
                    <div class="diagram">
                      <div><span class="node-title">가정·회사 네트워크</span><p>사용자 호스트와 공유기</p></div>
                      <span class="arrow">→</span>
                      <div><span class="node-title">지역·국가 ISP</span><p>KT, SKT, LG U+ 같은 접속망</p></div>
                      <span class="arrow">→</span>
                      <div><span class="node-title">상위 ISP</span><p>국가와 대륙을 잇는 더 큰 망</p></div>
                      <span class="arrow">→</span>
                      <div><span class="node-title">인터넷</span><p>네트워크들의 네트워크</p></div>
                    </div>
                    """,
                },
                {
                    "heading": "프로토콜과 TCP/IP",
                    "body": f"""
                    <p>프로토콜은 서로 다른 컴퓨터와 디지털 장치가 통신하기 위해 지켜야 하는 규칙이다. 어떤 메시지를 어떤 형식으로 보내고, 받는 쪽은 그것을 어떻게 해석하며, 응답은 어떻게 보내야 하는지를 미리 정해 둔 약속이라고 이해하면 된다. HTTP, TCP/IP, 802.11 같은 이름이 모두 프로토콜 또는 프로토콜 묶음의 예다.</p>
                    {nb01_protocol}
                    <p>이 과목에서는 TCP/IP를 중심으로 다룬다. TCP는 데이터 전송의 제어와 관리를 담당하는 전송 계층 프로토콜이고, IP는 네트워크와 네트워크 사이에서 패킷이 어떤 경로로 전달될지 라우팅하는 핵심 프로토콜이다. 실제 인터넷 시스템 대부분이 TCP/IP를 기반으로 움직이기 때문에, 이 구조를 이해하는 것이 이후 패킷 분석과 소켓 프로그래밍의 출발점이 된다.</p>
                    {nb01_tcp_ip}
                    <p>TCP는 Transmission Control Protocol로, 데이터가 신뢰성 있게 전달되도록 전송 제어와 관리를 담당한다. IP는 Internet Protocol로, 라우터와 엔드 시스템 사이에서 송수신되는 패킷 포맷과 경로 전달을 다룬다. 강사는 이 두 프로토콜이 인터넷에서 가장 중요한 프로토콜이며, 이후 강의에서 TCP/IP 계층 구조를 자세히 다룰 것이라고 예고한다.</p>
                    """,
                },
            ],
            "checks": [
                "네트워크를 모르면 MITM, ARP spoofing, DDoS 같은 공격을 이해하기 어려운 이유를 설명할 수 있는가?",
                "LAN, WAN, 인터넷의 차이를 예시와 함께 말할 수 있는가?",
                "패킷, 패킷 스위치, 경로, ISP가 인터넷 통신에서 어떤 역할을 하는지 정리할 수 있는가?",
                "프로토콜이 단순한 이름이 아니라 통신 규칙이라는 점을 이해했는가?",
            ],
        },
        {
            "id": "1-2",
            "title": "프로토콜 계층 구조",
            "subtitle": "복잡한 네트워크 통신을 TCP/IP 계층 모델로 나누어 보고, 각 계층의 단위와 캡슐화 흐름을 이해한다.",
            "tags": ["TCP/IP 모델", "계층화", "캡슐화"],
            "objectives": [
                "계층 구조가 복잡한 네트워크를 단순화하는 서비스 모델임을 설명한다.",
                "물리, 링크, 네트워크, 전송, 응용 계층의 역할과 데이터 단위를 연결한다.",
                "메시지에서 세그먼트, 데이터그램, 프레임으로 이어지는 캡슐화 흐름을 이해한다.",
            ],
            "sections": [
                {
                    "heading": "왜 계층 구조로 나누는가",
                    "body": f"""
                    <p>네트워크 흐름을 하나의 거대한 과정으로 보면 너무 복잡하다. 그래서 강의는 네트워크를 계층 구조로 나누어 이해한다. 계층 구조는 크고 복잡한 시스템을 잘 정의된 부분으로 나누어, 각 부분이 어떤 역할을 하는지 따로 논의할 수 있게 해 준다. 네트워크에서는 이를 서비스 모델이라고도 부른다.</p>
                    <p>슬라이드는 이 단순화의 의미를 두 가지로 잡아 준다. 첫째, 한 계층의 구현이 변하더라도 시스템의 나머지 부분은 그대로 유지될 수 있다. 둘째, 각 계층은 상위 계층에게 제공하는 서비스에 관심을 갖고, 자기 계층의 동작을 수행할 때는 아래 계층의 서비스를 사용한다. 그래서 계층 구조는 단순한 그림이 아니라 네트워크 기능을 나누어 설계하고 설명하는 기준이다.</p>
                    {nb02_layer_model}
                    <p>예를 들어 응용 계층은 브라우저나 프로그램에서 나온 메시지를 만들지만, 직접 랜선 위로 비트를 밀어 넣지는 않는다. 전송 계층은 메시지를 프로세스 간 전달 가능한 단위로 만들고, 네트워크 계층은 호스트 간 경로를 다루며, 링크 계층은 이웃 네트워크 요소로 프레임을 보내고, 물리 계층은 실제 매체로 비트를 보낸다. 상위 계층은 아래 계층이 제공하는 서비스를 믿고 자기 역할에 집중한다.</p>
                    <div class="callout">핵심 문장: 상위 계층은 하위 계층의 서비스를 사용하고, 각 계층은 자기 계층의 규칙과 데이터 단위를 가진다.</div>
                    """,
                },
                {
                    "heading": "TCP/IP 5계층 모델",
                    "body": """
                    <p>강의에서는 인터넷 프로토콜 스택, TCP/IP 레이어를 기준으로 설명한다. TCP/IP는 4계층으로 묶어 설명하기도 하지만, 여기서는 물리 계층을 따로 둔 5계층 흐름으로 이해하면 된다. 물리 계층은 비트 전달만 담당하므로 링크 계층과 묶어 말하는 경우도 있다.</p>
                    <table>
                      <thead><tr><th>계층</th><th>대표 단위</th><th>역할</th><th>예시 프로토콜·기술</th></tr></thead>
                      <tbody>
                        <tr><td>응용 계층</td><td>message</td><td>브라우저나 프로그램이 네트워크로 보낼 메시지를 만든다.</td><td>HTTP, SMTP, FTP</td></tr>
                        <tr><td>전송 계층</td><td>segment</td><td>프로세스 간 메시지 전달 서비스를 제공한다.</td><td>TCP, UDP</td></tr>
                        <tr><td>네트워크 계층</td><td>datagram</td><td>호스트에서 호스트까지의 경로를 선택하고 전달한다.</td><td>IP</td></tr>
                        <tr><td>데이터 링크 계층</td><td>frame</td><td>한 네트워크 요소에서 이웃 네트워크 요소로 프레임을 보낸다.</td><td>Ethernet, ARP</td></tr>
                        <tr><td>물리 계층</td><td>bit</td><td>RJ45 케이블, 구리선, 광케이블 같은 매체로 비트를 이동시킨다.</td><td>전송 매체</td></tr>
                      </tbody>
                    </table>
                    <p>이 표에서 가장 중요하게 봐야 할 것은 계층 이름과 데이터 단위의 연결이다. 응용 계층은 message, 전송 계층은 segment, 네트워크 계층은 datagram 또는 packet, 데이터 링크 계층은 frame, 물리 계층은 bit를 다룬다. 강사는 이 단위들이 뒤에서 설명할 캡슐화 때문에 계속 더해지고 감싸지는 구조라고 미리 강조한다.</p>
                    """,
                },
                {
                    "heading": "계층별 역할 자세히 보기",
                    "body": f"""
                    <p>물리 계층은 비트 단위 정보를 실제 전송 매체로 보내는 가장 낮은 계층이다. 우리가 랜선이라고 부르는 RJ45 케이블, 구리선, 광케이블 같은 매체를 통해 링크 계층 프레임을 구성하는 각 비트가 다음 노드로 이동한다.</p>
                    {nb02_physical}
                    <p>데이터 링크 계층은 프레임을 사용한다. 이 계층은 한 네트워크에서 이웃 네트워크 요소로 프레임을 이동시키며, 어떤 링크 계층 프로토콜을 쓰는지에 따라 제공 서비스가 달라진다. 네트워크 계층은 자기 단위인 데이터그램을 링크 계층에게 내려 보내고, 링크 계층은 그것을 프레임 안에 담아 다음 네트워크 요소로 전달한다.</p>
                    {nb02_link}
                    <p>네트워크 계층은 데이터그램을 사용하며, 한 호스트에서 다른 호스트까지 데이터가 가는 최적 경로를 선택한다. 그래서 라우팅과 깊게 연결된다. 강사는 이 계층을 IP 계층이라고도 부른다고 설명한다. 현재 인터넷의 모든 주요 요소는 IP 프로토콜을 수행하며, 상위 계층인 전송 계층의 segment를 운반한다.</p>
                    {nb02_network}
                    <p>전송 계층은 TCP와 UDP를 사용해 클라이언트와 서버의 애플리케이션 프로세스 사이에서 메시지를 주고받게 한다. TCP는 연결 지향형 서비스를 제공하고, 목적지로의 메시지 전달 보장과 흐름 제어를 포함한다. 또 긴 메시지를 짧은 메시지로 나누고, 혼잡 제어 기능을 제공한다. 반면 UDP는 비연결형 서비스를 제공하며 신뢰성, 흐름 제어, 혼잡 제어를 제공하지 않는다고 강의에서 정리한다.</p>
                    {nb02_transport}
                    <p>응용 계층은 브라우저나 프로그램이 직접 사용하는 계층이다. 웹사이트에 접속하거나 프로그램이 네트워크로 데이터를 보내려 할 때, 응용 계층은 message라는 단위의 데이터를 생성한다. 이 메시지를 실제로 전달하기 위해서는 하위 계층들의 서비스가 필요하다. 대표적인 응용 계층 프로토콜은 HTTP, SMTP, FTP다.</p>
                    {nb02_application}
                    """,
                },
                {
                    "heading": "캡슐화",
                    "body": f"""
                    <p>각 계층의 데이터 단위가 다른 이유는 캡슐화 때문이다. 강사는 “기존의 메시지에서 송수신에 필요한 Header를 붙여서 캡슐화한다”고 설명한다. 즉 데이터가 아래 계층으로 내려갈수록 기존 데이터 앞에 해당 계층이 해석할 헤더가 붙고, 그 결과 새로운 계층 단위가 된다.</p>
                    {nb02_encapsulation}
                    <p>응용 계층에서 메시지가 만들어지면 전송 계층은 여기에 전송 계층 헤더를 붙여 세그먼트를 만든다. 네트워크 계층은 세그먼트에 IP 헤더를 붙여 데이터그램을 만든다. 강의에서는 packet과 datagram을 거의 같은 의미로 언급하지만, 이후 설명에서는 네트워크 계층 단위를 datagram이라고 부르겠다고 정리한다. 링크 계층은 데이터그램에 링크 계층 헤더를 붙여 프레임을 만든다. 마지막으로 물리 계층은 프레임을 비트로 바꾸어 실제 매체를 통해 전송한다.</p>
                    <div class="diagram">
                      <div><span class="node-title">Message</span><p>응용 계층 데이터</p></div>
                      <span class="arrow">→</span>
                      <div><span class="node-title">Segment</span><p>전송 계층 헤더 추가</p></div>
                      <span class="arrow">→</span>
                      <div><span class="node-title">Datagram</span><p>IP 헤더 추가</p></div>
                      <span class="arrow">→</span>
                      <div><span class="node-title">Frame</span><p>링크 계층 헤더 추가</p></div>
                      <span class="arrow">→</span>
                      <div><span class="node-title">Bits</span><p>물리 매체로 전송</p></div>
                    </div>
                    <p>강의는 캡슐화를 꼭 이해해야 한다고 강조한다. 이후 Wireshark 실습에서 Frame, Ethernet, IPv4, TCP, HTTP가 층층이 보이는 이유가 바로 이 캡슐화 구조이기 때문이다.</p>
                    """,
                },
                {
                    "heading": "캡슐화 핵심 정리",
                    "body": """
                    <p>네트워크 계층 구조를 볼 때는 각 계층의 이름보다 데이터가 어떤 단위로 감싸지며 내려가는지를 먼저 잡는 것이 중요하다. Wireshark에서 여러 프로토콜이 층층이 보이는 이유도 이 캡슐화 구조 때문이다.</p>
                    """,
                },
            ],
            "checks": [
                "계층 구조를 서비스 모델이라고 부르는 이유를 설명할 수 있는가?",
                "각 계층의 데이터 단위가 message, segment, datagram, frame, bit로 달라지는 이유를 말할 수 있는가?",
                "캡슐화 과정을 위에서 아래로 순서대로 설명할 수 있는가?",
                "Wireshark에서 여러 프로토콜 계층이 겹쳐 보이는 이유를 이해했는가?",
            ],
        },
        {
            "id": "1-3",
            "title": "데이터 링크 계층",
            "subtitle": "프레임, MAC 주소, ARP, Ethernet, 스위치의 역할을 통해 근거리 네트워크에서 이웃 노드로 전달되는 과정을 이해한다.",
            "tags": ["데이터 링크", "MAC", "ARP"],
            "objectives": [
                "노드와 링크의 의미를 이해하고, 링크 계층이 프레임을 이웃 네트워크 요소로 전달하는 계층임을 설명한다.",
                "MAC 주소, broadcast address, ARP, TTL, plug and play의 관계를 정리한다.",
                "Ethernet 프레임, CRC, 스위치의 buffering·filtering·forwarding, 라우터와의 차이를 이해한다.",
            ],
            "sections": [
                {
                    "heading": "노드와 링크",
                    "body": f"""
                    <p>데이터 링크 계층을 이해하려면 먼저 노드와 링크를 구분해야 한다. 노드는 링크 계층 프로토콜을 실행하는 장치다. 사용자의 호스트, 라우터, 스위치, AP 같은 장비가 모두 노드가 될 수 있다. 링크는 이런 노드들이 모인 네트워크 요소에서 이웃 네트워크 요소로 이동하는 연결이다.</p>
                    <p>이전 강의에서 링크 계층은 한 네트워크에서 이웃 네트워크로 데이터를 전송하는 계층이라고 했다. 상위 계층인 네트워크 계층에서 내려온 데이터그램은 링크 계층에서 프레임이라는 더 큰 단위로 캡슐화된다. 즉 링크 계층의 기본 단위는 프레임이다.</p>
                    {nb03_nodes_links}
                    <p>슬라이드의 네트워크 그림은 여러 네트워크 그룹이 링크로 연결되어 있는 구조를 보여 준다. 강사는 오른쪽 그림을 가리키며 여러 네트워크 그룹이 간선, 즉 링크를 통해 이어진다고 설명한다. 데이터 링크 계층의 관점에서는 전체 인터넷을 한 번에 보는 것이 아니라, “현재 네트워크 요소에서 이웃 네트워크 요소로 어떻게 프레임을 넘기는가”가 핵심이다.</p>
                    <div class="diagram">
                      <div><span class="node-title">네트워크 계층</span><p>IP 데이터그램을 내려 보낸다.</p></div>
                      <span class="arrow">→</span>
                      <div><span class="node-title">링크 계층</span><p>프레임으로 캡슐화한다.</p></div>
                      <span class="arrow">→</span>
                      <div><span class="node-title">이웃 노드</span><p>다음 네트워크 요소로 전달한다.</p></div>
                    </div>
                    """,
                },
                {
                    "heading": "링크 계층 서비스",
                    "body": f"""
                    <p>링크 계층은 여러 서비스를 제공한다. 첫째, 프레임화다. 네트워크 계층에서 내려온 데이터그램을 링크 계층 단위인 프레임으로 감싼다. 둘째, 링크 액세스다. 링크 계층 프로토콜은 링크 위에서 프레임을 어떻게 전송할지 규칙을 정하고, 네트워크끼리 통신할 수 있게 링크 접속을 수행한다.</p>
                    <p>셋째, 신뢰적 전달 서비스도 제공할 수 있다. 후반부에서 TCP도 신뢰적 전달을 제공한다고 배우지만, 링크 계층의 신뢰적 전달은 오류가 발생한 링크 구간에서 정정이나 재전송을 수행하는 의미로 설명된다. 넷째, 오류 검출과 정정이다. 상위 계층에서 내려온 데이터그램에 오류가 있다면 그대로 전달할 필요가 없기 때문에, 링크 계층은 낮은 계층에서 오류를 확인한다.</p>
                    {nb03_services}
                    <p>링크 계층은 2계층이고 하드웨어와 가까운 낮은 계층이므로, 하드웨어와 소프트웨어가 조합되어 구현된다고 이해하면 된다.</p>
                    """,
                },
                {
                    "heading": "스위치와 MAC 주소",
                    "body": f"""
                    <p>스위치는 링크 계층의 패킷 교환기라고 볼 수 있다. 이때 스위치는 네트워크 계층의 IP 주소 체계를 사용하지 않는다. 계층 구조에서는 각 계층이 독립적으로 구성되어야 하며, 각 계층은 자기 주소 체계를 가져야 하기 때문이다. 링크 계층에서 사용하는 주소가 MAC 주소다.</p>
                    <p>MAC 주소는 호스트나 라우터의 네트워크 인터페이스가 갖는 주소다. 하나의 컴퓨터나 라우터에도 여러 네트워크 인터페이스가 있을 수 있고, 각 인터페이스는 자기 MAC 주소를 가진다. 프레임을 수신한 어댑터는 프레임 안의 목적지 MAC 주소를 검사해 이 프레임이 자기에게 온 것인지 판단한다.</p>
                    {nb03_mac}
                    <table>
                      <thead><tr><th>항목</th><th>설명</th></tr></thead>
                      <tbody>
                        <tr><td>MAC 주소</td><td>링크 계층 주소다. 일반적으로 6바이트로 구성된다.</td></tr>
                        <tr><td>목적지 MAC</td><td>프레임을 받을 인터페이스를 가리킨다.</td></tr>
                        <tr><td>출발지 MAC</td><td>프레임을 보낸 인터페이스를 가리킨다.</td></tr>
                        <tr><td>broadcast address</td><td>모든 비트가 1인 주소, 표기상 FF:FF:FF:FF:FF:FF로 모든 어댑터에게 보내는 데 쓰인다.</td></tr>
                      </tbody>
                    </table>
                    """,
                },
                {
                    "heading": "ARP: IP 주소에서 MAC 주소 찾기",
                    "body": f"""
                    <p>네트워크 계층 주소는 IP 주소이고, 링크 계층 주소는 MAC 주소다. 두 주소 체계는 계층이 다르기 때문에 서로 독립적이다. 하지만 실제로 프레임을 보내려면 목적지 또는 다음 홉의 MAC 주소가 필요하다. 그래서 상위 계층에서 내려온 IP 주소에 대응되는 MAC 주소를 구해야 하며, 이 작업을 수행하는 프로토콜이 ARP다.</p>
                    <p>ARP는 같은 서브넷 안에서 IP 주소에 해당하는 MAC 주소를 알아낸다. 이 매핑은 영원히 유지되지 않는다. 강의에서 언급된 TTL, Time To Live는 이 매핑을 언제 삭제하거나 갱신해야 하는지와 관련된 시간 개념이다. 또한 ARP는 관리자가 하나하나 직접 구성하지 않아도 자동으로 구축되므로 plug and play 성격을 가진다고 설명된다.</p>
                    {nb03_arp}
                    <p>강사는 “IP 주소를 가진 호스트의 MAC 주소를 알아내야 한다”는 문장을 ARP의 핵심으로 강조한다. 같은 서브넷 안에서 A가 C에게 데이터그램을 보내려면 IP 주소만으로는 링크 계층 프레임을 만들 수 없다. 링크 계층은 MAC 주소를 보고 프레임을 전달하므로, IP와 MAC의 대응 관계를 알아내는 과정이 반드시 필요하다.</p>
                    <div class="callout">같은 서브넷 안에서는 ARP로 상대 IP에 대응하는 MAC 주소를 찾을 수 있지만, 다른 서브넷의 최종 호스트 MAC 주소를 로컬 ARP로 직접 알아낼 수는 없다.</div>
                    """,
                },
                {
                    "heading": "다른 서브넷으로 보낼 때",
                    "body": f"""
                    <p>강의는 서로 다른 서브넷에 있는 노드끼리 통신하는 경우도 다룬다. 예를 들어 111.111.111.111 쪽 호스트가 222.222.222.222 쪽 다른 서브넷 호스트로 데이터를 보내려 한다고 하자. 로컬 서브넷 안에는 목적지 호스트의 MAC 주소가 없기 때문에 ARP로 그 최종 MAC 주소를 바로 구할 수 없다.</p>
                    {nb03_other_subnet}
                    <p>이때 송신 호스트는 프레임을 라우터 인터페이스의 MAC 주소로 보낸다. 라우터가 네트워크 계층에서 다음 경로를 판단하고, 목적지 쪽 서브넷에 맞는 링크 계층 전달을 이어 간다. 즉 다른 서브넷으로 가는 첫 프레임의 목적지 MAC은 최종 서버의 MAC이 아니라 기본 게이트웨이 또는 라우터 인터페이스의 MAC이 된다.</p>
                    """,
                },
                {
                    "heading": "Ethernet 프레임",
                    "body": f"""
                    <p>오늘날 Ethernet은 가장 중요한 LAN 기술로 소개된다. 인터넷이 전 세계 네트워킹을 논하는 개념이라면, Ethernet은 근거리 네트워크에서 이웃 네트워크 요소로 값을 전송하는 대표 기술이다.</p>
                    {nb03_ethernet_frame}
                    <table>
                      <thead><tr><th>필드</th><th>역할</th></tr></thead>
                      <tbody>
                        <tr><td>Destination address</td><td>목적지 MAC 주소가 들어간다.</td></tr>
                        <tr><td>Source address</td><td>출발지 MAC 주소가 들어간다.</td></tr>
                        <tr><td>Type</td><td>상위 네트워크 계층 프로토콜이 무엇인지 나타낸다. 예를 들어 IPv4를 구분한다.</td></tr>
                        <tr><td>Data</td><td>상위 계층에서 내려온 IP 데이터그램을 싣는다.</td></tr>
                        <tr><td>CRC</td><td>오류 검출을 위한 값이다.</td></tr>
                      </tbody>
                    </table>
                    <p>Data 필드에는 상위 네트워크 계층의 IP 데이터그램이 들어간다. 강의는 Data 크기를 46바이트에서 1500바이트로 설명하고, 이보다 크면 단편화가 진행될 수 있다고 언급한다. Destination address와 Source address에는 앞에서 배운 목적지·출발지 MAC 주소가 들어가며, Type 필드는 IP 같은 상위 네트워크 계층 프로토콜 종류를 나타낸다.</p>
                    {nb03_ethernet_unreliable}
                    <p>Ethernet은 비연결형이고 비신뢰적인 서비스를 제공한다. CRC로 오류를 검사하지만, 성공 응답이나 실패 응답을 보내지 않는다. 실패하면 프레임을 폐기한다. 이더넷 자체는 재전송 여부나 새로운 데이터그램 여부를 구분하지 않으며, 필요한 신뢰성은 상위 전송 계층의 TCP 같은 프로토콜이 담당할 수 있다.</p>
                    """,
                },
                {
                    "heading": "스위치의 buffering, filtering, forwarding",
                    "body": f"""
                    <p>스위치는 프레임을 전달할 때 전송 속도와 수신 용량 차이를 처리해야 한다. 입력되는 프레임이 처리 가능한 용량을 넘으면 패킷 손실이 발생할 수 있으므로, 어느 정도 수용하기 위한 버퍼를 가진다.</p>
                    <p>또 스위치는 filtering과 forwarding을 수행한다. Filtering은 받은 프레임을 폐기할지 판단하는 동작이고, forwarding은 프레임을 어느 인터페이스로 내보낼지 결정해 실제로 전송하는 동작이다.</p>
                    <table>
                      <thead><tr><th>장비</th><th>계층</th><th>주소 체계</th><th>역할</th></tr></thead>
                      <tbody>
                        <tr><td>스위치</td><td>2계층, 데이터 링크</td><td>MAC 주소</td><td>프레임을 이웃 네트워크 요소로 전달한다.</td></tr>
                        <tr><td>라우터</td><td>3계층, 네트워크</td><td>IP 주소</td><td>패킷이 목적지 호스트까지 갈 경로를 결정한다.</td></tr>
                      </tbody>
                    </table>
                    {nb03_switch_router}
                    <p>강의의 마지막 그림은 응용 계층 메시지가 스위치를 통해 링크 계층에서 이동하고, 라우터가 네트워크 계층 라우팅을 책임진 뒤 수신 호스트로 전달되는 흐름을 보여 준다.</p>
                    """,
                },
            ],
            "checks": [
                "노드와 링크를 네트워크 장비 예시로 설명할 수 있는가?",
                "IP 주소와 MAC 주소가 서로 다른 계층의 주소인 이유를 이해했는가?",
                "ARP가 같은 서브넷에서 어떤 문제를 해결하는지 말할 수 있는가?",
                "Ethernet이 비연결형·비신뢰적이라는 말과 TCP의 신뢰성이 어떻게 공존하는지 설명할 수 있는가?",
                "스위치와 라우터의 계층, 주소, 역할 차이를 구분할 수 있는가?",
            ],
        },
        {
            "id": "1-4",
            "title": "네트워크 계층",
            "subtitle": "IP 계층이 데이터그램을 이용해 호스트 대 호스트 전달과 라우팅을 수행하는 방식을 이해한다.",
            "tags": ["IP", "라우팅", "IPv4"],
            "objectives": [
                "네트워크 계층이 호스트 대 호스트 전달과 라우팅을 담당한다는 점을 이해한다.",
                "데이터 평면과 제어 평면, 최선형 서비스, IPv4 데이터그램 포맷을 설명한다.",
                "IP 주소, 서브넷, 클래스 주소 체계, broadcast, NAT, DHCP, IPv6의 의미를 정리한다.",
            ],
            "sections": [
                {
                    "heading": "네트워크 계층의 위치",
                    "body": f"""
                    <p>앞 강의에서 데이터 링크 계층은 근거리 네트워크에서 한 네트워크 요소가 이웃 네트워크 요소로 프레임을 전달하는 계층이라고 배웠다. 데이터 링크 계층은 MAC 주소를 사용한다. 이번 강의에서 다루는 네트워크 계층은 그 위의 3계층이며, 흔히 IP 계층이라고도 부른다.</p>
                    <p>네트워크 계층의 단위는 데이터그램이다. 이 계층은 한 호스트에서 다른 호스트로 데이터가 갈 때 어떤 경로를 선택하고 어떻게 전송할지 다룬다. 쉽게 말하면 라우팅을 수행한다. 상위 전송 계층에서 내려온 세그먼트를 데이터그램 안에 담아 운반하는 역할을 한다.</p>
                    {nb04_overview}
                    <p>강사는 계층을 계속 비교하며 설명한다. 데이터 링크 계층은 네트워크 계층의 데이터그램을 프레임에 담아 이웃 네트워크 요소로 전달하고, 네트워크 계층은 전송 계층의 segment를 운반해 출발 호스트에서 목적 호스트까지 보내는 역할을 한다. 따라서 네트워크 계층을 이해할 때는 “IP 주소를 기반으로 목적 호스트까지 어떤 경로로 보낼 것인가”를 중심에 두면 된다.</p>
                    <div class="diagram">
                      <div><span class="node-title">데이터 링크</span><p>이웃 네트워크 요소로 프레임 전달</p></div>
                      <span class="arrow">→</span>
                      <div><span class="node-title">네트워크</span><p>호스트 대 호스트 데이터그램 전달</p></div>
                      <span class="arrow">→</span>
                      <div><span class="node-title">전송</span><p>프로세스 대 프로세스 세그먼트 전달</p></div>
                    </div>
                    """,
                },
                {
                    "heading": "호스트 대 호스트 전달",
                    "body": f"""
                    <p>강의는 H1과 H2라는 두 호스트 예시로 네트워크 계층의 역할을 설명한다. H1의 전송 계층에서 내려온 세그먼트를 H2의 네트워크 계층까지 전달하고, 다시 H2의 전송 계층으로 올려 주는 것이 네트워크 계층의 큰 역할이다. 그래서 데이터 링크가 이웃 노드 간 전달이라면, 네트워크 계층은 호스트 대 호스트 전달을 담당한다고 이해하면 된다.</p>
                    {nb04_host_to_host}
                    <p>이 구분은 뒤 강의까지 계속 반복된다. 링크 계층은 가까운 한 홉, 네트워크 계층은 출발 호스트에서 목적 호스트까지, 전송 계층은 그 위에서 프로그램 또는 프로세스끼리 통신하는 논리적 연결을 담당한다.</p>
                    """,
                },
                {
                    "heading": "데이터 평면과 제어 평면",
                    "body": f"""
                    <p>네트워크 계층은 데이터 평면과 제어 평면으로 나누어 볼 수 있다. 데이터 평면은 데이터그램을 실제로 전달하는 과정과 IP 프로토콜 관련 내용을 다룬다. 제어 평면은 어떤 라우팅 알고리즘을 사용하고 어떻게 포워딩할지 같은 내용을 다룬다.</p>
                    {nb04_planes}
                    <p>이 강의에서는 자세한 라우팅 알고리즘이나 제어 평면 내용은 깊게 다루지 않는다. 멘토는 패킷 분석과 해킹에 필요한 네트워크 기초를 목표로 하므로, IP 프로토콜을 이해하는 데 초점을 맞춘다고 설명한다.</p>
                    """,
                },
                {
                    "heading": "가능한 서비스와 인터넷의 최선형 서비스",
                    "body": f"""
                    <p>네트워크 계층은 이론적으로 여러 서비스를 제공할 수 있다. 출발지에서 목적지까지 패킷 도착을 보장하는 보장된 전달, 일정 지연 제한 안의 도착 보장, 보낸 순서대로 도착하는 순서 패킷 전달, 최소 대역 보장, 기밀성 제공 같은 모델을 생각할 수 있다.</p>
                    <p>하지만 실제 인터넷 네트워크 계층은 이런 모든 보장을 제공하지 않고 <strong>최선형 서비스(best-effort service)</strong>를 제공한다. 패킷이 보낸 순서대로 도착할 것을 보장하지 않고, 목적지까지 전달될 것도 보장하지 않으며, 종단 시스템 간 지연이나 최소 대역폭도 보장하지 않는다.</p>
                    {nb04_best_effort}
                    <p>그럼에도 인터넷은 최선형 서비스만으로 충분히 좋은 성능을 내는 것으로 입증되어 왔다고 강의는 설명한다. 단순한 구조는 실시간 애플리케이션이나 성능이 중요한 네트워크에서 오히려 장점이 될 수 있다.</p>
                    """,
                },
                {
                    "heading": "IPv4 데이터그램",
                    "body": f"""
                    <p>IP 프로토콜을 이해하기 위해 강의는 IPv4 데이터그램 포맷을 소개한다. IPv4 데이터그램은 보통 20바이트 헤더를 가지며, 옵션이 있으면 길이가 달라질 수 있다. 헤더에는 출발지 IP, 목적지 IP, 체크섬, 데이터그램 길이, Type of Service 같은 필드가 들어간다. 데이터 필드에는 상위 전송 계층의 세그먼트가 담긴다.</p>
                    {nb04_ipv4_datagram}
                    <table>
                      <thead><tr><th>필드</th><th>의미</th></tr></thead>
                      <tbody>
                        <tr><td>Source IP</td><td>데이터그램을 보낸 호스트의 IP 주소다.</td></tr>
                        <tr><td>Destination IP</td><td>데이터그램이 도착해야 할 호스트의 IP 주소다.</td></tr>
                        <tr><td>Checksum</td><td>비트 오류를 탐지하는 데 사용된다.</td></tr>
                        <tr><td>Type of Service</td><td>서비스 유형이나 처리 우선순위와 관련된 정보를 담는다.</td></tr>
                        <tr><td>Total length</td><td>데이터그램 전체 길이를 나타낸다.</td></tr>
                        <tr><td>Data</td><td>전송 계층 세그먼트가 들어간다.</td></tr>
                      </tbody>
                    </table>
                    <p>슬라이드의 포맷은 32비트 폭으로 배열되어 있으며, Version, Header length, Type of service, Datagram length, 16-bit identifier, Flags, Fragmentation offset, Time-to-live, Upper-layer protocol, Header checksum, Source IP address, Destination IP address, Options, Data가 차례로 보인다. 강의에서는 특히 checksum을 비트 오류 탐지와 연결하고, Type of Service를 세그먼트가 요구하는 서비스 성격을 명시하는 필드로 설명한다.</p>
                    <p>모든 호스트와 라우터는 IP 데이터그램을 송수신할 수 있어야 하므로 IP 주소를 가진다.</p>
                    """,
                },
                {
                    "heading": "IP 주소, 서브넷, 클래스",
                    "body": f"""
                    <p>IPv4 주소는 32비트 길이를 가지며, 보통 4개의 바이트를 점으로 구분한 형식으로 쓴다. 서브넷은 IP 네트워크를 더 작고 관리하기 쉬운 부분으로 나눈 것이다. 강의의 그림에서는 여러 서브넷이 라우터로 연결된 형태가 설명된다.</p>
                    {nb04_subnet}
                    <p>강의는 IPv4의 클래스 주소 체계도 설명한다. 필요한 호스트 IP 개수에 따라 네트워크 영역과 호스트 영역의 크기를 다르게 할당하는 방식이다. 가정용 네트워크에서 자주 보는 192.168.0.1 같은 주소는 C 클래스 사설망 감각과 연결해 이해할 수 있다. C 클래스는 B 클래스보다 호스트 영역이 작고, 대학교나 기업처럼 더 많은 호스트가 필요한 곳에서는 더 큰 주소 영역이 필요할 수 있다.</p>
                    {nb04_class_address}
                    <table>
                      <thead><tr><th>개념</th><th>설명</th></tr></thead>
                      <tbody>
                        <tr><td>네트워크 영역</td><td>어느 네트워크에 속하는지 나타낸다.</td></tr>
                        <tr><td>호스트 영역</td><td>그 네트워크 안의 개별 장치를 구분한다.</td></tr>
                        <tr><td>IP broadcast</td><td>255.255.255.255처럼 서브넷의 모든 호스트에게 전달하겠다는 목적 주소다.</td></tr>
                      </tbody>
                    </table>
                    """,
                },
                {
                    "heading": "NAT, DHCP, IPv6",
                    "body": f"""
                    <p><strong>NAT, Network Address Translation</strong>는 하나의 공용 IP 주소를 사용해 사설 네트워크 안의 여러 사설 IP 주소가 외부와 통신할 수 있게 하는 주소 변환 체계로 설명된다. IPv4 주소 고갈 문제를 완화하는 데 중요한 기술이다.</p>
                    <p><strong>DHCP, Dynamic Host Configuration Protocol</strong>은 IP 주소를 수동으로 하나하나 지정하지 않고, 네트워크에 접속한 장치에게 동적으로 IP 주소를 할당하는 프로토콜이다. 공유기나 조직 네트워크에서 장치가 자동으로 IP를 받는 흐름을 떠올리면 된다.</p>
                    {nb04_nat_dhcp}
                    <p>IPv4 주소 공간 고갈 문제는 오래전부터 논의되어 왔고, 이를 해결하기 위해 IPv6가 개발되었다. IPv4가 32비트 주소를 쓰는 것과 달리 IPv6는 128비트 주소를 사용한다. 또 헤더를 간소화하고 flow labeling 같은 흐름 처리 개념을 포함한다. 다만 강의에서는 IPv6가 수용되고 있지만 아직 IPv4만큼 널리 전환되지는 않았다고 설명한다.</p>
                    {nb04_ipv6}
                    <p>IPv6 슬라이드는 Source address와 Destination address가 각각 128비트로 확장된 구조를 보여 준다. 또 Traffic class, Flow label, Payload length, Next hdr, Hop limit 같은 필드가 있으며, 강사는 IPv6가 40바이트 고정 헤더를 사용해 헤더를 간소화했다고 설명한다.</p>
                    """,
                },
            ],
            "checks": [
                "네트워크 계층이 데이터 링크 계층과 다르게 호스트 대 호스트 전달을 담당한다는 점을 설명할 수 있는가?",
                "인터넷 네트워크 계층이 최선형 서비스를 제공한다는 말의 의미를 이해했는가?",
                "IPv4 데이터그램 헤더에서 출발지 IP, 목적지 IP, 체크섬이 어떤 역할을 하는지 말할 수 있는가?",
                "서브넷, NAT, DHCP, IPv6가 IPv4 주소 운영과 어떤 관련이 있는지 정리할 수 있는가?",
            ],
        },
        {
            "id": "1-5",
            "title": "트랜스포트 계층",
            "subtitle": "응용 프로그램 메시지를 프로세스 대 프로세스로 전달하는 TCP·UDP·QUIC, 포트, 세그먼트, 신뢰성, handshake를 정리한다.",
            "tags": ["TCP", "UDP", "세그먼트"],
            "objectives": [
                "전송 계층이 프로세스 간 논리적 통신을 제공한다는 점을 이해한다.",
                "다중화와 역다중화, 소켓과 포트 번호의 역할을 설명한다.",
                "UDP와 TCP의 구조, 장단점, MSS, sequence number, acknowledgement number, handshake를 정리한다.",
            ],
            "sections": [
                {
                    "heading": "전송 계층의 위치",
                    "body": f"""
                    <p>5강은 앞 강의의 계층 복습에서 시작한다. 데이터 링크 계층은 하나의 로컬 네트워크 안에서 frame을 이웃 네트워크 요소로 옮기는 역할을 했고, 네트워크 계층은 transport segment를 datagram으로 캡슐화해 한 host에서 다른 host까지 전달하고 route를 선택하는 역할을 했다. 전송 계층은 이 네트워크 계층 위에서 동작하며, 실제 응용 프로그램이 만든 메시지를 프로세스 단위로 전달하는 계층이다.</p>
                    {nb05_overview}
                    <p>슬라이드의 단위는 <strong>segment</strong>다. 브라우저, 게임, 메신저, 서버 프로그램 같은 application process가 만든 message가 전송 계층으로 내려오면, 여기에 transport-layer header가 붙어 segment가 된다. 이 segment가 아래 네트워크 계층으로 내려가 datagram에 담기고, 다시 링크 계층 frame에 담겨 실제 네트워크를 지나간다.</p>
                    <p>강사는 전송 계층의 대표 프로토콜로 <strong>TCP</strong>와 <strong>UDP</strong>를 제시한다. TCP는 연결 지향형이고 신뢰성 있는 전송, 흐름 제어, 혼잡 제어, segmentation을 제공한다. UDP는 더 가볍고 연결 설정이 없으며 빠르지만, 신뢰성·흐름 제어·혼잡 제어를 기본으로 제공하지 않는다. 이 차이는 이후 패킷 분석과 네트워크 프로그래밍에서 계속 기준점이 된다.</p>
                    """,
                },
                {
                    "heading": "프로세스 간 논리적 통신",
                    "body": f"""
                    <p>전송 계층을 이해할 때 가장 중요한 표현은 <strong>process-to-process logical communication</strong>이다. 네트워크 계층은 host-to-host logical communication을 제공한다. 즉, 호스트 A에서 호스트 B까지 패킷이 갈 수 있게 해 준다. 하지만 한 호스트 안에는 브라우저, 게임 클라이언트, 백그라운드 서비스, 서버 데몬처럼 여러 프로세스가 동시에 실행된다. 전송 계층은 그중 어떤 프로세스와 어떤 프로세스가 통신하는지를 구분해 준다.</p>
                    {nb05_process}
                    <p>슬라이드에서는 하위 계층이 제공하는 서비스를 이용하지만, 애플리케이션 입장에서는 서로 다른 host의 process가 직접 연결된 것처럼 보인다고 설명한다. 그래서 전송 계층의 통신은 실제 물리적 직접 연결이 아니라 <strong>논리적 연결</strong>이다. 중간에는 라우터, 링크, 네트워크 계층, 데이터 링크 계층이 있지만, 개발자와 사용자는 대개 process 사이의 데이터 흐름으로 바라본다.</p>
                    <p>강의는 TCP와 UDP 외에 <strong>QUIC</strong>도 함께 언급한다. QUIC은 Google Chrome 등에서 활용되는 범용 목적의 전송 계층 프로토콜로 소개되며, UDP 기반 위에 신뢰성·연결 관리 같은 기능을 올려 TCP와 UDP의 장점을 조합하려는 방향으로 이해하면 된다. 이 강의의 중심은 TCP와 UDP지만, QUIC 언급은 현대 웹 트래픽이 전통적인 TCP만으로 설명되지 않을 수 있음을 보여 준다.</p>
                    """,
                },
                {
                    "heading": "소켓, 포트, 다중화와 역다중화",
                    "body": f"""
                    <p>목적지 호스트에 segment가 도착하면, 전송 계층은 네트워크 계층으로부터 그 segment를 받아 올바른 socket으로 전달한다. socket은 application process와 전송 계층 사이에 있는 통신 출입구다. 강사는 socket을 애플리케이션과 transport/network layer 사이의 중간 인터페이스처럼 설명한다.</p>
                    {nb05_multiplexing}
                    <p>여기서 <strong>port number</strong>가 등장한다. 한 host 안에는 여러 socket이 있을 수 있고, 전송 계층은 port number를 이용해 어느 socket으로 데이터를 전달해야 하는지 식별한다. 예를 들어 웹 서버, SSH 서버, DNS 서버가 같은 호스트에서 동시에 동작할 수 있는 이유는 전송 계층이 포트 번호로 프로세스의 통신 출입구를 구분하기 때문이다.</p>
                    <table>
                      <thead><tr><th>용어</th><th>의미</th></tr></thead>
                      <tbody>
                        <tr><td>소켓</td><td>애플리케이션과 전송 계층 사이의 통신 출입구다.</td></tr>
                        <tr><td>포트 번호</td><td>호스트 안에서 어떤 프로세스 또는 소켓으로 전달할지 구분하는 식별자다.</td></tr>
                        <tr><td>역다중화, demultiplexing</td><td>들어온 segment를 port number 등을 기준으로 알맞은 socket에 나누어 전달하는 과정이다.</td></tr>
                        <tr><td>다중화, multiplexing</td><td>여러 socket에서 나온 데이터를 전송 계층이 모아 segment로 만들고 아래 네트워크 계층으로 내려보내는 과정이다.</td></tr>
                      </tbody>
                    </table>
                    <p>강의의 그림은 receiving host에서 transport layer가 segment를 받아 socket으로 넘기는 모습을 보여 준다. 이 흐름이 역다중화다. 반대로 송신 측에서는 여러 process가 만든 데이터를 transport layer가 받아 하나의 네트워크 계층 인터페이스로 내려보내므로 다중화가 일어난다. 전송 계층이 process-to-process 전달을 맡는다는 말은 결국 이 socket과 port number 처리까지 포함한다.</p>
                    """,
                },
                {
                    "heading": "UDP",
                    "body": f"""
                    <p><strong>UDP, User Datagram Protocol</strong>은 간소화된 전송 계층 프로토콜이다. 강의에서는 UDP를 <strong>unreliable</strong>, <strong>connectionless</strong> protocol이라고 정리한다. 즉, TCP처럼 연결을 먼저 맺지 않고, 데이터를 보낸 뒤 수신 확인·재전송·순서 보장을 전송 계층이 책임지지 않는다.</p>
                    {nb05_udp_header}
                    <p>그렇다고 UDP가 아무 역할도 하지 않는 것은 아니다. UDP는 전송 계층의 기본 기능인 multiplexing과 demultiplexing을 제공한다. 또한 <strong>checksum</strong> 필드를 통해 segment 안의 bit error를 검출할 수 있다. 슬라이드의 UDP header는 source port, dest port, length, checksum 네 필드로 구성되어 있고, 각 필드는 16bit다. 그래서 UDP header는 총 8byte로 매우 작다.</p>
                    <table>
                      <thead><tr><th>UDP 필드</th><th>역할</th></tr></thead>
                      <tbody>
                        <tr><td>source port</td><td>송신 측 socket 또는 process를 식별하는 데 사용된다.</td></tr>
                        <tr><td>dest port</td><td>수신 측 host 안에서 어느 socket으로 보낼지 구분한다.</td></tr>
                        <tr><td>length</td><td>UDP header와 data를 포함한 UDP segment의 길이를 나타낸다.</td></tr>
                        <tr><td>checksum</td><td>전송 중 bit error가 생겼는지 검출하는 데 사용된다.</td></tr>
                      </tbody>
                    </table>
                    <p>UDP는 실시간성이 중요한 애플리케이션에서 자주 언급된다. 스트리밍, 음성·영상 통화, 게임처럼 조금의 손실보다 지연이 더 치명적인 경우에는 TCP식 재전송과 순서 보장이 오히려 불리할 수 있다. 이런 경우 애플리케이션이 필요한 보정만 직접 구현하고, 전송 계층은 가볍게 가져가는 설계가 가능하다.</p>
                    {nb05_udp_tradeoffs}
                    <p>슬라이드의 장점은 네 가지로 정리된다. 첫째, application layer에서 보낼 데이터와 보낼 시점을 더 세밀하게 제어할 수 있다. 둘째, connection establishment가 없어 handshake 지연이 없다. 셋째, connection state를 유지하지 않으므로 서버가 많은 클라이언트를 상대할 때 부담이 작다. 넷째, TCP header가 보통 20byte인 것과 비교해 UDP header는 8byte라 header overhead가 작다.</p>
                    <p>단점도 분명하다. 강의는 <strong>congestion control이 없다</strong>는 점을 강조한다. 네트워크가 감당할 수 없을 정도로 패킷이 쏟아질 때 UDP 자체는 속도를 줄이거나 네트워크 혼잡을 완화하는 기능을 제공하지 않는다. 그래서 UDP의 빠름과 단순함은 장점이지만, 보안·장애 분석 관점에서는 트래픽 폭주와 서비스 품질 문제를 함께 떠올려야 한다.</p>
                    """,
                },
                {
                    "heading": "TCP",
                    "body": f"""
                    <p><strong>TCP, Transmission Control Protocol</strong>은 UDP와 반대로 신뢰성 있는 데이터 전송과 연결 지향형 서비스를 제공한다. 강사는 TCP가 수신 여부 확인, 재전송, packet 순서 유지에 sequence number와 acknowledgement number를 사용한다고 설명한다. 데이터를 그냥 던지는 것이 아니라, 상대가 받았는지 확인하고 필요하면 다시 보내며, byte stream의 순서를 유지한다는 점이 핵심이다.</p>
                    {nb05_tcp_header}
                    <p>TCP는 데이터를 보내기 전에 <strong>handshake</strong>로 연결을 설정한다. 연결이 수립된 상태에서 양쪽 process가 데이터를 주고받는다. 또한 TCP는 <strong>flow control</strong>과 <strong>congestion control</strong>을 제공한다. flow control은 송신자와 수신자 사이의 packet 수를 조절해 수신 측이 감당하지 못하는 상황을 줄이는 기능이고, congestion control은 네트워크 내부 packet 수를 조절해 네트워크 overflow를 방지하는 기능이다.</p>
                    <table>
                      <thead><tr><th>필드·개념</th><th>역할</th></tr></thead>
                      <tbody>
                        <tr><td>source port</td><td>보낸 프로세스의 소켓 식별에 쓰인다.</td></tr>
                        <tr><td>destination port</td><td>받는 프로세스의 소켓 식별에 쓰인다.</td></tr>
                        <tr><td>sequence number</td><td>세그먼트에 담긴 첫 번째 바이트의 스트림 번호다.</td></tr>
                        <tr><td>acknowledgement number</td><td>상대에게 다음에 받고 싶은 바이트 번호를 알려 주는 기대값이다.</td></tr>
                        <tr><td>receive window</td><td>수신 측이 받을 수 있는 양을 알려 flow control에 사용된다.</td></tr>
                        <tr><td>flags</td><td>SYN, ACK, FIN 같은 제어 bit로 연결 시작·응답·종료 흐름을 표현한다.</td></tr>
                        <tr><td>checksum</td><td>segment 오류 검출에 사용된다.</td></tr>
                        <tr><td>data</td><td>응용 계층 메시지가 들어간다.</td></tr>
                      </tbody>
                    </table>
                    <p>슬라이드의 TCP header 그림은 source port와 dest port 아래에 sequence number, acknowledgement number가 크게 놓여 있음을 보여 준다. 이 두 필드는 뒤에서 배우는 신뢰성 있는 전송의 중심이다. header length, receive window, internet checksum, urgent data pointer, options, data 영역도 함께 표시되어 TCP가 UDP보다 훨씬 많은 상태와 제어 정보를 다룬다는 점을 확인할 수 있다.</p>
                    """,
                },
                {
                    "heading": "MSS, MTU, segmentation",
                    "body": f"""
                    <p>전송해야 할 application data가 크면 한 TCP segment에 모두 담을 수 없다. TCP는 데이터를 여러 segment로 나누는데, 이때 한 segment의 payload 영역에 담을 수 있는 최대 application data 크기를 <strong>MSS, Maximum Segment Size</strong>라고 한다. 슬라이드의 표기처럼 MSS는 header를 포함한 TCP segment 전체 크기가 아니라, application data에 대한 최대 크기다.</p>
                    {nb05_mss_mtu}
                    <p>MSS를 결정하는 중요한 요소가 <strong>MTU, Maximum Transmission Unit</strong>이다. 강의에서는 MTU를 로컬 송신 host가 전송할 수 있는 가장 큰 링크 계층 frame 길이로 설명한다. 네트워크 경로 중 MTU가 서로 다른 구간이 있으면, 그 경로에서 사용할 수 있는 더 작은 MTU를 기준으로 MSS를 조정하기도 한다.</p>
                    <p>기본 계산은 <strong>MSS = MTU - TCP/IP header</strong>다. 슬라이드 예시는 MTU가 1500byte이고 TCP/IP header가 40byte이면 MSS가 1460byte가 된다고 보여 준다. 이 40byte는 보통 IPv4 header 20byte와 TCP header 20byte를 합친 값으로 이해하면 된다. 따라서 TCP가 50,000byte 같은 큰 데이터를 보내야 한다면, MSS 단위로 잘라 여러 segment를 만든 뒤 sequence number로 각 조각의 위치를 관리한다.</p>
                    """,
                },
                {
                    "heading": "Sequence와 acknowledgement",
                    "body": f"""
                    <p>TCP는 byte stream을 기준으로 데이터를 관리한다. <strong>Sequence number</strong>는 어떤 segment에 들어 있는 첫 번째 byte가 전체 byte stream에서 몇 번째 위치인지 나타낸다. 예를 들어 데이터 스트림이 500,000byte이고 MSS를 1,000byte로 가정하면, segment는 총 500개로 구성된다. 첫 번째 segment는 0번 byte부터, 두 번째 segment는 1,000번 byte부터 시작하는 식으로 번호가 붙는다.</p>
                    {nb05_seq_ack}
                    <p><strong>Acknowledgement number</strong>는 상대방에게서 기대하는 다음 byte의 sequence number다. 슬라이드 오른쪽 예시에서 Host A가 Host B에게 <code>Seq=42, ACK=79, data='C'</code>를 보낸다. 이것은 A가 보내는 데이터가 byte stream의 42번 위치에서 시작하며, 동시에 A는 B에게서 다음으로 79번 byte를 기대하고 있다는 뜻이다.</p>
                    <p>B가 A의 <code>'C'</code>를 받으면, B는 A에게 <code>Seq=79, ACK=43, data='C'</code>를 보낸다. 여기서 ACK=43은 A가 보낸 42번 byte를 받았으므로 다음에는 43번 byte를 기대한다는 의미다. 마지막으로 A는 B의 응답을 받고 <code>Seq=43, ACK=80</code> 흐름으로 이어 간다. 강의의 핵심은 ACK가 “방금 받은 번호”가 아니라 <strong>다음에 받고 싶은 번호</strong>라는 점이다.</p>
                    <p>이 구조 덕분에 TCP는 순서를 유지하고, 누락된 부분을 찾고, 같은 데이터가 중복되어 들어왔는지 판단할 수 있다. 따라서 sequence number와 acknowledgement number는 TCP의 신뢰성을 설명할 때 반드시 함께 이해해야 한다.</p>
                    """,
                },
                {
                    "heading": "신뢰성, timeout, RTT",
                    "body": f"""
                    <p>TCP가 제공하는 신뢰성 있는 데이터 전송은 “중복이 없고 순서가 유지되는 것”을 보장하는 방향으로 설명된다. 이를 위해 TCP는 ACK, sequence number, 재전송을 함께 사용한다. segment를 보냈는데 일정 시간 안에 ACK를 받지 못하면, TCP는 해당 segment가 손실되었을 가능성이 있다고 판단하고 다시 전송할 수 있다.</p>
                    {nb05_timeout}
                    <p>슬라이드에서는 이 메커니즘을 <strong>retransmission timeout</strong>이라고 부른다. timeout 값은 연결의 왕복 시간인 <strong>RTT, Round Trip Time</strong>보다 조금 더 커야 한다. RTT는 송신 측에서 segment를 전송한 시점부터 그 segment에 대한 긍정 확인 응답, 즉 ACK를 받을 때까지 걸리는 시간이다.</p>
                    <p>timeout이 RTT보다 작으면 정상적으로 돌아오는 ACK도 너무 늦었다고 오해해 불필요한 재전송이 발생한다. 반대로 timeout이 지나치게 크면 실제 손실이 발생했을 때 복구가 늦어진다. 강의에서는 TCP가 손실 segment를 발견하기 위해 timeout/재전송 메커니즘을 사용한다는 점과, timeout을 RTT보다 조금 크게 잡아야 한다는 점을 핵심으로 잡으면 된다.</p>
                    """,
                },
                {
                    "heading": "TCP 3-way handshake와 4-way termination",
                    "body": f"""
                    <p>TCP는 connection-oriented protocol이기 때문에 데이터를 본격적으로 보내기 전에 연결을 먼저 설정한다. 이 연결 시작 과정이 <strong>3-way handshake</strong>다. 강의에서는 client host와 server host 사이의 세 메시지를 순서대로 설명한다.</p>
                    {nb05_three_way}
                    <ol>
                      <li><strong>Client → Server:</strong> 연결 요청을 보낸다. SYN bit가 1이고, client initial sequence number를 담아 <code>syn=1, seq=a</code> 형태가 된다.</li>
                      <li><strong>Server → Client:</strong> 서버가 응답한다. 서버도 SYN bit를 1로 켜고 자기 sequence number를 담으며, 클라이언트의 요청을 확인하기 위해 <code>ack=a+1</code>을 보낸다. 즉 <code>syn=1, seq=b, ack=a+1</code>이다.</li>
                      <li><strong>Client → Server:</strong> 클라이언트가 연결 완료를 알린다. 이때 SYN bit는 0으로 내려가고, <code>seq=a+1, ack=b+1</code> 흐름이 된다. 강의에서는 세 번째 메시지에는 payload가 포함될 수 있다고 덧붙인다.</li>
                    </ol>
                    <p>연결을 닫을 때는 <strong>4-way termination</strong>, 또는 4-way handshake로 종료한다. 시작과 달리 종료는 두 프로세스 중 어느 쪽이든 먼저 시작할 수 있다. 한쪽이 더 이상 보낼 데이터가 없다는 뜻으로 FIN을 보내고, 상대가 ACK로 확인한 뒤, 상대도 FIN을 보내고 마지막 ACK를 받으면 연결이 닫힌다.</p>
                    {nb05_four_way}
                    <ol>
                      <li><strong>Client → Server:</strong> 연결 종료 요청을 보낸다. FIN bit가 1이다.</li>
                      <li><strong>Server → Client:</strong> 서버가 요청을 확인하며 ACK를 보낸다.</li>
                      <li><strong>Server → Client:</strong> 서버도 연결 종료 요청을 보낸다. FIN bit가 1이다.</li>
                      <li><strong>Client → Server:</strong> 클라이언트가 마지막 ACK를 보내 종료를 확인한다.</li>
                    </ol>
                    <p>슬라이드는 종료 뒤 timed wait과 closed 상태를 함께 보여 준다. 강사는 연결이 끝나면 host의 자원, 예를 들어 buffer와 memory가 회수된다고 설명한다. 따라서 TCP 연결은 단순히 패킷 몇 개를 주고받는 절차가 아니라, 양쪽 host가 연결 상태와 자원을 관리하는 과정이다.</p>
                    """,
                },
                {
                    "heading": "TCP와 UDP를 구분해야 하는 이유",
                    "body": f"""
                    <p>마지막 슬라이드는 TCP와 UDP의 차이를 한 장으로 비교한다. 강의는 이 차이를 정확히 아는 것이 네트워크 프로그래밍과 보안 취약점 분석에서 매우 중요하다고 강조한다. 같은 “데이터 전송”처럼 보여도, TCP와 UDP는 연결을 맺는 방식, 상태를 저장하는 방식, 순서와 신뢰성을 보장하는 방식이 전혀 다르다.</p>
                    {nb05_tcp_udp}
                    <table>
                      <thead><tr><th>항목</th><th>TCP</th><th>UDP</th></tr></thead>
                      <tbody>
                        <tr><td>연결 방식</td><td>Connected, handshake 후 통신</td><td>Connectionless, handshake 없음</td></tr>
                        <tr><td>상태 관리</td><td>State memory를 유지한다.</td><td>Stateless에 가깝다.</td></tr>
                        <tr><td>데이터 모델</td><td>Byte stream 기반</td><td>Packet/datagram 기반</td></tr>
                        <tr><td>순서 보장</td><td>Ordered data delivery</td><td>No sequence guarantee</td></tr>
                        <tr><td>신뢰성</td><td>Reliable, ACK와 재전송을 사용</td><td>Lossy, 오류 packet은 버려질 수 있음</td></tr>
                        <tr><td>제어</td><td>Flow control과 congestion control 제공</td><td>기본 flow control·congestion control 없음</td></tr>
                        <tr><td>속도와 용도</td><td>상대적으로 느리지만 안정적이고 point-to-point 통신에 적합</td><td>상대적으로 빠르고 multicast 같은 형태를 지원할 수 있음</td></tr>
                        <tr><td>보안 계층 예</td><td>SSL/TLS가 주로 TCP 위에서 동작한다.</td><td>DTLS처럼 datagram 환경을 위한 보안 방식이 쓰인다.</td></tr>
                      </tbody>
                    </table>
                    <p>패킷 분석을 할 때 TCP라면 SYN, ACK, FIN, sequence number, retransmission, window 같은 단서를 봐야 한다. UDP라면 연결 상태보다 port, datagram 단위, checksum, 손실 허용 여부, 애플리케이션이 자체적으로 구현한 신뢰성 여부를 봐야 한다. 그래서 강의의 결론은 단순한 암기가 아니라 “어떤 프로토콜 위에서 동작하는 서비스인지 먼저 구분하라”는 실무적인 기준으로 이해하면 된다.</p>
                    """,
                },
            ],
            "checks": [
                "전송 계층이 호스트 대 호스트가 아니라 프로세스 대 프로세스 통신을 제공한다는 점을 설명할 수 있는가?",
                "다중화와 역다중화가 포트 번호와 어떻게 연결되는지 이해했는가?",
                "UDP가 빠른 이유와 위험한 이유를 모두 말할 수 있는가?",
                "TCP의 sequence number와 acknowledgement number가 신뢰성에 어떻게 기여하는지 설명할 수 있는가?",
                "TCP 연결 설정과 종료 과정을 단계별로 말할 수 있는가?",
            ],
        },
        {
            "id": "1-6",
            "title": "애플리케이션 계층",
            "subtitle": "네트워크 애플리케이션 구조, 클라이언트-서버와 P2P, HTTP 요청·응답, HTTPS, DNS를 정리한다.",
            "tags": ["HTTP", "HTTPS", "DNS"],
            "objectives": [
                "응용 계층이 하위 계층 서비스 위에서 네트워크 애플리케이션 메시지를 만든다는 점을 이해한다.",
                "클라이언트-서버 구조와 P2P 구조의 차이를 설명한다.",
                "HTTP request/response, method, path, header, body, status code, HTTPS, DNS의 의미를 정리한다.",
            ],
            "sections": [
                {
                    "heading": "응용 계층까지 올라오기",
                    "body": f"""
                    <p>6강은 TCP/IP 계층 구조 복습으로 시작한다. 데이터 링크 계층은 근거리 네트워크에서 frame을 이웃 네트워크 요소로 전달했고, 네트워크 계층은 IP와 datagram을 통해 host-to-host 전달과 routing을 담당했다. 전 강의의 전송 계층은 TCP와 UDP를 통해 application process 사이의 process-to-process logical communication을 가능하게 했다.</p>
                    <p>이제 마지막으로 올라오는 계층이 <strong>application layer</strong>다. 응용 계층은 웹 브라우저, 서버 프로그램, 메신저, 게임 클라이언트처럼 사용자가 직접 마주치는 네트워크 프로그램의 message를 다룬다. 하지만 응용 계층이 독립적으로 모든 통신을 처리하는 것은 아니다. 강사는 다시 한 번 <strong>각 상위 계층은 하위 계층의 service와 function에 의존한다</strong>고 강조한다.</p>
                    {nb06_network_apps}
                    <p>따라서 application layer를 배울 때도 아래 계층을 함께 떠올려야 한다. HTTP message는 응용 계층에서 만들어지지만, 실제 전송은 socket을 통해 transport layer로 내려가고, TCP/UDP segment, IP datagram, link-layer frame을 거쳐 네트워크로 나간다. 이 관점이 있어야 뒤의 Wireshark 실습에서 패킷을 계층별로 읽을 수 있다.</p>
                    """,
                },
                {
                    "heading": "네트워크 애플리케이션 구조",
                    "body": f"""
                    <p>네트워크 애플리케이션은 서로 다른 위치의 end system에서 동작하면서 network를 통해 통신하는 프로그램이다. 강의에서는 대표 구조를 <strong>client-server</strong>와 <strong>P2P, Peer-to-Peer</strong>로 나눈다. 웹사이트처럼 우리가 흔히 쓰는 서비스는 대부분 client-server 구조이고, 토렌트 같은 서비스는 P2P 구조의 대표 예시로 설명된다.</p>
                    {nb06_client_p2p}
                    <table>
                      <thead><tr><th>구조</th><th>설명</th><th>예시·특징</th></tr></thead>
                      <tbody>
                        <tr><td>Client-server</td><td>항상 동작하는 server가 있고, client라는 다른 host들이 server에 service request를 보낸다.</td><td>웹사이트 대부분. client끼리는 직접 통신하지 않고, server는 고정 IP 주소를 가져야 한다.</td></tr>
                        <tr><td>P2P</td><td>peer라고 부르는 간헐적으로 연결된 host 쌍들이 server를 거치지 않고 직접 통신한다.</td><td>토렌트가 대표 예시다. 항상 켜진 infrastructure server 의존이 적고, 자기 확장성과 비용 효율성이 있다.</td></tr>
                      </tbody>
                    </table>
                    <p>강사는 이 구조 이해가 이후 client-side attack과 server-side attack을 이해하는 데 중요하다고 말한다. 어떤 요청이 client에서 시작되는지, server가 어떤 응답을 주는지, 취약점이 browser 쪽 로직에서 발생하는지 server 쪽 처리에서 발생하는지 구분해야 웹 보안과 네트워크 분석이 가능해진다.</p>
                    """,
                },
                {
                    "heading": "프로세스 통신과 소켓",
                    "body": f"""
                    <p>네트워크 애플리케이션의 실제 통신 주체는 process다. client process와 server process는 컴퓨터 네트워크를 통해 application-layer message를 교환한다. 이 process 간 통신을 가능하게 하는 메커니즘이 바로 앞 강의에서 배운 transport layer다.</p>
                    {nb06_socket}
                    <p>슬라이드의 그림은 host 또는 server 위에 process가 있고, 그 아래에 socket, 다시 그 아래에 TCP with buffers and variables가 있는 구조를 보여 준다. application developer가 직접 제어하는 부분은 주로 process와 socket 위쪽이고, transport protocol의 buffer와 variable 처리는 operating system이 담당한다.</p>
                    <p><strong>Socket</strong>은 host의 application layer와 transport layer 사이의 interface다. 브라우저가 HTTP message를 만든다고 해서 브라우저가 네트워크 전체를 직접 다루는 것이 아니다. 애플리케이션은 socket을 통해 transport layer에 데이터를 넘기고, TCP/UDP는 port number와 연결 상태 등을 이용해 올바른 process와 통신하게 해 준다.</p>
                    """,
                },
                {
                    "heading": "HTTP의 특성",
                    "body": f"""
                    <p><strong>HTTP, Hypertext Transfer Protocol</strong>은 여러 resource를 송수신하기 위한 application layer protocol이다. 강사는 HTTP가 현대 생활을 크게 바꿨다고 설명한다. 뉴스 확인, 웹 게임, 영화, Netflix, Discord 같은 서비스가 웹 기술 위에서 동작하고, 웹 해킹과 패킷 분석에서도 HTTP 이해가 기본이 된다.</p>
                    {nb06_http_features}
                    <p>HTTP의 첫 번째 특성은 <strong>stateless, 무상태성</strong>이다. 서버가 두 요청 사이의 상태나 정보를 기본적으로 유지하지 않는다는 뜻이다. 그런데 실제 웹사이트에서는 로그인 상태, 장바구니, 사용자 식별이 유지된다. 이는 HTTP 자체가 상태를 기억해서가 아니라, <strong>cookie</strong>와 server-side <strong>session</strong> 같은 별도 메커니즘을 붙여 구현하기 때문이다.</p>
                    <p>두 번째 특성은 <strong>connectionless, 비연결성</strong>이다. 요청한 resource에 대한 응답이 끝나면 연결이 끊어지는 성격으로 설명된다. 슬라이드의 그림처럼 하나의 web document가 page.html, image.png, video.mp4, ads.jpg, layout.css 같은 여러 resource를 필요로 하면 브라우저는 필요한 resource를 각각 요청하고 응답을 받아 화면을 구성한다.</p>
                    <div class="callout">핵심: HTTP message 자체는 상태를 기억하지 않는다. 로그인 유지처럼 “상태가 있는 것처럼 보이는 기능”은 cookie와 session 같은 추가 장치로 만든다.</div>
                    """,
                },
                {
                    "heading": "HTTP request",
                    "body": f"""
                    <p>HTTP request는 client가 server에 어떤 작업을 요청하는 message다. 강의 슬라이드는 요청 메시지를 세 부분으로 나눈다. 첫째는 <strong>시작줄</strong>, 둘째는 <strong>header</strong>, 셋째는 필요할 때 붙는 <strong>body</strong>다.</p>
                    {nb06_http_request}
                    <table>
                      <thead><tr><th>구성 요소</th><th>의미</th></tr></thead>
                      <tbody>
                        <tr><td>method</td><td>GET, POST처럼 어떤 방식의 요청인지 나타낸다. 슬라이드 예시는 POST다.</td></tr>
                        <tr><td>path</td><td>서버 안의 어떤 경로에 접근할지 나타낸다. 예시에서는 /whitehat이다.</td></tr>
                        <tr><td>version</td><td>HTTP/2처럼 프로토콜 버전을 나타낸다.</td></tr>
                        <tr><td>Host</td><td>어떤 서버 주소로 요청을 보낼지 나타낸다.</td></tr>
                        <tr><td>User-Agent</td><td>브라우저와 운영체제 등 client 환경 정보를 담는다.</td></tr>
                        <tr><td>Accept / Accept-Language</td><td>client가 받을 수 있는 content type과 선호 언어를 알린다.</td></tr>
                        <tr><td>body</td><td>POST 요청처럼 server에 보낼 데이터를 담는다.</td></tr>
                      </tbody>
                    </table>
                    {http_request_example}
                    <p>슬라이드의 예시는 <code>POST /whitehat HTTP/2</code>로 시작한다. 이는 HTTP/2 버전으로 <code>/whitehat</code> path에 POST 방식 요청을 보낸다는 뜻이다. header에는 Host, User-Agent, Accept, Accept-Language, Connection이 들어 있고, 빈 줄 아래 body에는 form 데이터가 들어간다.</p>
                    <p>강의에서는 GET과 POST의 감각도 함께 설명한다. 브라우저 주소창에 URL을 입력해 resource를 가져오는 동작은 보통 GET으로 이해할 수 있고, 로그인 폼처럼 사용자가 값을 입력해 서버로 보내는 동작은 POST 예시와 연결된다. 보안 분석에서는 method, path, header, body 중 어디에 민감 정보나 공격 payload가 들어가는지 확인해야 한다.</p>
                    """,
                },
                {
                    "heading": "HTTP response",
                    "body": f"""
                    <p>HTTP response는 server가 client에게 보내는 응답 message다. request와 마찬가지로 header와 body를 가지지만, 첫 줄은 요청의 시작줄이 아니라 <strong>상태줄</strong>이다. 상태줄은 protocol version, status code, status text로 구성된다.</p>
                    {nb06_http_response}
                    <table>
                      <thead><tr><th>상태 코드</th><th>의미</th></tr></thead>
                      <tbody>
                        <tr><td>200 OK</td><td>정상적으로 처리되어 응답이 왔다는 뜻이다.</td></tr>
                        <tr><td>404 Not Found</td><td>서버에서 해당 path를 찾을 수 없다는 뜻이다.</td></tr>
                        <tr><td>500 Internal Server Error</td><td>서버 내부 오류가 발생했다는 뜻이다.</td></tr>
                      </tbody>
                    </table>
                    {http_response_example}
                    <p>슬라이드 예시의 상태줄은 <code>HTTP/2 200 OK</code>다. 정상 응답이며, header에는 <code>Content-Type</code>, <code>Content-Length</code>, <code>Server</code>, <code>Cache-Control</code>, <code>Vary</code> 같은 정보가 들어간다. 빈 줄 아래 body에는 요청한 정보가 들어가며, 예시에서는 JSON 형태의 응답이 보인다.</p>
                    <p>브라우저가 웹페이지를 보여 줄 때는 response body에 담긴 HTML, CSS, JavaScript, image 같은 resource를 해석해 화면을 만든다. 따라서 HTTP response를 읽을 수 있으면 서버가 무엇을 보냈고, 브라우저가 무엇을 렌더링했는지 추적할 수 있다.</p>
                    """,
                },
                {
                    "heading": "HTTP, HTTPS, 보안",
                    "body": f"""
                    <p>강의는 HTTP가 네트워크 관점에서 왜 위험할 수 있는지 설명한다. HTTP는 암호화되지 않은 message를 요청하고 응답받기 때문에, 중간에서 packet을 sniffing할 수 있는 공격자가 있으면 request와 response의 내용이 그대로 노출될 수 있다. 로그인 과정에서 ID와 password가 HTTP 평문으로 오간다면 그 값도 읽힐 수 있다.</p>
                    {nb06_https}
                    <p><strong>HTTPS, Hypertext Transfer Protocol Secure</strong>는 HTTP에 암호화를 더한 확장으로 설명된다. HTTP가 평문에 가까운 내용을 보여 주는 것과 달리, HTTPS는 암호화된 데이터가 흐르므로 중간에서 보더라도 의미 있는 내용을 쉽게 알아낼 수 없다. 슬라이드의 왼쪽은 HTTP message가 사람이 읽을 수 있는 형태로 보이고, 오른쪽은 HTTPS traffic이 알아보기 어려운 byte stream처럼 보이는 차이를 보여 준다.</p>
                    <p>강사는 이 차이를 <strong>기밀성 보장</strong>과 연결한다. 물론 HTTPS만으로 모든 보안 문제가 사라지는 것은 아니지만, 네트워크 중간자 관점의 sniffing으로부터 내용이 노출되는 문제를 줄이는 기본 방어선이다. 그래서 실제 서비스 분석에서는 URL이 <code>http://</code>인지 <code>https://</code>인지, 그리고 어떤 구간이 암호화되어 있는지 먼저 확인해야 한다.</p>
                    """,
                },
                {
                    "heading": "DNS",
                    "body": f"""
                    <p>응용 계층 프로토콜은 HTTP만 있는 것이 아니다. 강의에서는 HTTP 다음으로 <strong>DNS, Domain Name System</strong>를 소개한다. 우리가 웹사이트에 접속할 때 보통 IP 주소를 직접 입력하지 않고 <code>https://www.kitribob.kr/</code> 같은 host name을 입력한다. 하지만 router와 host가 실제로 처리하기 쉬운 식별자는 IP address다.</p>
                    {nb06_dns_lookup}
                    <p>DNS는 host name을 IP address로 변환해 주는 service다. 브라우저가 어떤 사이트에 접근하려 하면 먼저 DNS server에게 해당 host name의 IP 주소를 묻는다. DNS server가 예를 들어 <code>www.example.com → 12.45.56.67</code> 같은 응답을 돌려주면, 브라우저는 그 IP address를 이용해 web server에 접속하고 HTTP request를 보낸다.</p>
                    <p>강사는 host name이 사람이 기억하고 제공하기에는 편하지만, 길이가 가변적이고 라우터가 직접 처리하기 어렵기 때문에 네트워크 내부에서는 IP address가 필요하다고 설명한다. 따라서 DNS는 사람이 쓰는 이름과 네트워크가 쓰는 주소 사이를 연결하는 필수 응용 계층 서비스다.</p>
                    {nb06_dns_hierarchy}
                    <p>DNS를 하나의 중앙집중형 database로만 만들면 서버 고장이나 traffic 과부하가 전체 인터넷 문제로 이어질 수 있다. 그래서 DNS는 많은 server를 사용하고, 이들을 계층 형태로 구성해 전 세계에 분산한다. 슬라이드의 구조처럼 Root DNS servers 아래에 <code>.com</code>, <code>.org</code>, <code>.edu</code> 같은 TLD DNS servers가 있고, 그 아래에 facebook.com, amazon.com, pbs.org, nyu.edu, umass.edu 같은 domain별 DNS servers가 연결된다.</p>
                    """,
                },
                {
                    "heading": "TCP/IP 모델과 OSI 7계층",
                    "body": """
                    <p>강의 마무리에서는 TCP/IP 계층 구조를 다시 강조한다. 지금까지 데이터 링크, 네트워크, 트랜스포트, 애플리케이션 계층을 차례로 보았고, 각 계층의 역할과 단위를 기억해야 한다. 데이터 링크 계층은 frame, 네트워크 계층은 datagram, 전송 계층은 segment, 응용 계층은 message를 중심으로 이해하면 된다.</p>
                    <p>OSI 7계층도 네트워크 학습에서 자주 언급되지만, 멘토는 패킷 분석과 프로그래밍에서 직접 다루기 좋은 TCP/IP layer를 기준으로 설명했다고 말한다. 더 깊게 공부하고 싶다면 OSI 7계층도 따로 찾아보면 좋지만, 이 강의에서는 다음 실습을 위해 TCP/IP 5계층의 흐름을 정확히 잡는 것이 우선이다. 다음 강의에서는 Wireshark로 실제 HTTP packet을 캡처하며 지금까지 배운 계층 구조를 눈으로 확인한다.</p>
                    """,
                },
            ],
            "checks": [
                "클라이언트-서버 구조와 P2P 구조의 차이를 설명할 수 있는가?",
                "HTTP가 무상태성을 가진다는 말과 로그인 유지가 가능한 이유를 함께 설명할 수 있는가?",
                "GET과 POST의 차이를 request 구조와 연결해 말할 수 있는가?",
                "HTTP response의 상태 코드 200, 404, 500을 구분할 수 있는가?",
                "DNS가 도메인 이름과 IP 주소 사이에서 어떤 역할을 하는지 이해했는가?",
            ],
        },
        {
            "id": "1-7",
            "title": "와이어샤크 실습 패킷 분석",
            "subtitle": "Wireshark로 HTTP 패킷을 캡처하고 Frame, Ethernet, IPv4, TCP, HTTP 계층과 3-way handshake를 직접 확인한다.",
            "tags": ["Wireshark", "패킷 분석", "3-way handshake"],
            "objectives": [
                "Wireshark의 목적과 공격·방어 관점의 활용을 이해한다.",
                "HTTP request/response를 필터링하고 각 계층 헤더를 분석한다.",
                "Follow TCP Stream, ip.addr 필터, Flow Graph로 TCP 3-way handshake를 확인한다.",
            ],
            "sections": [
                {
                    "heading": "Wireshark를 쓰는 이유",
                    "body": f"""
                    <p>7강은 지금까지 배운 TCP/IP 5계층을 실제 패킷 화면에서 확인하는 실습이다. 앞 강의들에서는 Ethernet, IPv4, TCP, HTTP를 각각 이론적으로 배웠다. 이번에는 브라우저가 HTTP 서버에 접속할 때 실제로 어떤 패킷이 오가고, 그 패킷 안에 계층별 header와 payload가 어떻게 들어가는지 Wireshark로 직접 본다.</p>
                    {nb07_intro}
                    <p><strong>Wireshark</strong>는 호스트 장치에서 발생하는 네트워크 패킷을 캡처하고 분석할 수 있는 도구다. 강사는 이 도구가 공격과 방어 양쪽에서 모두 중요하다고 설명한다. 공격자 관점에서는 네트워크 공격 이후 sniffing으로 오가는 값을 관찰할 수 있고, 방어자 관점에서는 침해사고 대응, 트래픽 분석, 포렌식에서 실제 증거를 읽는 데 사용할 수 있다.</p>
                    <p>따라서 이 실습의 목표는 단순히 버튼을 눌러 보는 것이 아니다. 학생은 HTTP request/response를 찾고, 각 패킷의 Frame, Ethernet, IPv4, TCP, HTTP 계층을 펼쳐 보며, 마지막에는 TCP 3-way handshake가 HTTP 데이터 전송보다 먼저 일어난다는 사실까지 확인해야 한다.</p>
                    """,
                },
                {
                    "heading": "설치와 인터페이스 선택",
                    "body": f"""
                    <p>Wireshark는 <code>wireshark.org</code> 공식 홈페이지에서 Windows, macOS, Linux용 설치 파일을 받을 수 있다. 강의 화면에서는 macOS ARM 환경을 예로 들며, 다운로드 페이지에는 Windows x64 installer, macOS Arm disk image, macOS Intel disk image 등이 함께 보인다.</p>
                    {nb07_install}
                    <p>설치 후 실행하면 먼저 어떤 <strong>network interface</strong>를 캡처할지 선택한다. 강사는 현재 Wi-Fi로 인터넷에 연결되어 있기 때문에 Wi-Fi 인터페이스를 선택한다. 이 단계가 중요한 이유는 패킷은 특정 네트워크 인터페이스를 통해 오가기 때문이다. 유선 LAN, Wi-Fi, 가상 어댑터가 함께 있는 환경에서는 잘못된 인터페이스를 고르면 원하는 통신이 보이지 않을 수 있다.</p>
                    <p>캡처를 시작하면 TCP, QUIC 등 수많은 프로토콜 패킷이 계속 표시된다. Chrome 기반 브라우저를 쓰면 QUIC 패킷도 많이 보일 수 있다. 실제 분석에서는 전체 패킷을 모두 읽는 것이 아니라, 원하는 통신만 골라 보기 위해 display filter를 적극적으로 사용한다.</p>
                    """,
                },
                {
                    "heading": "HTTP 사이트 접속과 필터",
                    "body": f"""
                    <p>실습에서는 HTTPS가 적용되지 않은 HTTP 서버에 접속한다. HTTPS 통신은 암호화되어 있으므로 중간에서 패킷을 보더라도 HTTP 본문을 그대로 읽기 어렵다. 그래서 강사는 자신의 테스트 서버인 <code>pwnhyo.kr:8080</code>에 접속해 HTTP가 평문으로 어떻게 보이는지 보여 준다.</p>
                    {nb07_http_filter}
                    <p>진행 순서는 다음과 같다. 먼저 Wireshark 캡처를 시작하고, 브라우저에서 <code>pwnhyo.kr:8080</code>에 접속한다. 브라우저에는 <strong>80 port test</strong>라는 간단한 페이지가 뜬다. 그 다음 캡처를 멈추고 display filter 입력창에 <code>http</code>를 넣으면 HTTP 통신만 남는다.</p>
                    <p>필터 결과에는 핵심 패킷 두 개가 보인다. 첫 번째는 client <code>192.168.45.145</code>가 server <code>122.46.96.85</code>로 보낸 <code>GET / HTTP/1.1</code> request이고, 두 번째는 server가 client로 돌려준 <code>HTTP/1.1 200 OK (text/html)</code> response다. 이 두 줄만으로도 “브라우저가 요청했고, 서버가 HTML을 정상 응답했다”는 흐름을 파악할 수 있다.</p>
                    """,
                },
                {
                    "heading": "HTTP request 분석",
                    "body": f"""
                    <p>필터 결과에서 request packet 158을 선택하면 아래 packet detail 영역에 계층별 정보가 펼쳐진다. HTTP 부분에는 요청 시작줄인 <code>GET / HTTP/1.1</code>이 있고, 그 아래에 여러 header가 이어진다.</p>
                    {nb07_request}
                    <p>이 요청은 브라우저 주소창으로 URL에 접속한 것이므로 <strong>GET</strong> 요청이다. <code>/</code>는 서버의 루트 경로를 의미하고, <code>HTTP/1.1</code>은 사용한 HTTP 버전이다. 강사는 GET 요청이기 때문에 빈 줄 아래에 별도 HTTP body가 없다고 설명한다.</p>
                    <table>
                      <thead><tr><th>request 요소</th><th>실습에서 확인하는 의미</th></tr></thead>
                      <tbody>
                        <tr><td>GET</td><td>브라우저가 URL로 서버 자원을 요청했다.</td></tr>
                        <tr><td>/</td><td>서버의 루트 path에 접근했다.</td></tr>
                        <tr><td>Host: pwnhyo.kr:8080</td><td>요청 대상 host와 port를 나타낸다.</td></tr>
                        <tr><td>Connection: keep-alive</td><td>요청 후 연결을 바로 끊지 않고 재사용할 수 있음을 나타낸다.</td></tr>
                        <tr><td>User-Agent</td><td>접속한 운영체제와 브라우저 환경을 나타낸다.</td></tr>
                        <tr><td>Accept / Accept-Encoding / Accept-Language</td><td>받을 수 있는 문서 형식, 압축 방식, 선호 언어를 서버에 알려 준다.</td></tr>
                        <tr><td>Full request URI</td><td><code>http://pwnhyo.kr:8080/</code>로 요청했음을 보여 준다.</td></tr>
                      </tbody>
                    </table>
                    {wireshark_http_request}
                    <p><code>User-Agent</code>는 특히 실무에서 자주 확인한다. 강사는 이 header가 접속한 디바이스 환경을 나타내며, 모바일과 노트북에서 웹사이트 화면이 다르게 보이는 것도 이런 client 환경 정보와 관련된다고 설명한다. 보안 분석에서는 request method, path, Host, header, body 중 어디에 공격 payload나 민감 정보가 들어가는지 확인해야 한다.</p>
                    """,
                },
                {
                    "heading": "HTTP response 분석",
                    "body": f"""
                    <p>Response packet 165는 server <code>122.46.96.85</code>가 client <code>192.168.45.145</code>로 보낸 응답이다. HTTP response의 첫 줄은 <code>HTTP/1.1 200 OK</code>다. 이는 HTTP/1.1 버전으로 정상 처리 응답을 보냈다는 뜻이다.</p>
                    {nb07_response}
                    <p>Response header에는 응답 시각인 <code>Date</code>, 서버 프로그램 정보인 <code>Server: Apache/2.4.41 (Ubuntu)</code>, 본문 길이인 <code>Content-Length: 22</code>, 연결 유지 정책인 <code>Keep-Alive: timeout=5, max=100</code>, 본문 형식인 <code>Content-Type: text/html; charset=UTF-8</code>가 들어 있다.</p>
                    {nb07_body}
                    {wireshark_http_response}
                    <p>빈 줄 아래의 response body에는 <code>&lt;h1&gt;80 port test&lt;/h1&gt;</code>라는 HTML 코드가 들어 있다. 브라우저는 이 body를 해석해 화면에 큰 제목 형태의 <strong>80 port test</strong>를 보여 준다. 즉 Wireshark에서 보는 HTTP response body와 브라우저가 렌더링한 화면은 서로 같은 데이터의 다른 표현이다.</p>
                    """,
                },
                {
                    "heading": "Frame, Ethernet, IPv4, TCP, HTTP",
                    "body": f"""
                    <p>HTTP response packet을 펼치면 Wireshark packet detail에 <strong>Frame, Ethernet II, Internet Protocol Version 4, Transmission Control Protocol, Hypertext Transfer Protocol</strong>이 차례로 보인다. 강사는 이 화면이 지금까지 배운 계층별 캡슐화를 그대로 보여 준다고 설명한다.</p>
                    {nb07_layer_stack}
                    <p>Frame은 데이터 링크 계층에서 네트워크 요소로 전달되는 전체 단위다. Ethernet II는 링크 계층 header로, source MAC과 destination MAC, 그리고 상위 계층 type을 담는다. IPv4는 네트워크 계층 datagram header이고, TCP는 전송 계층 segment header이며, HTTP는 응용 계층 message다.</p>
                    <table>
                      <thead><tr><th>Wireshark 항목</th><th>확인할 내용</th></tr></thead>
                      <tbody>
                        <tr><td>Frame 165</td><td>292 bytes on wire, 292 bytes captured, interface en0처럼 캡처 전체 정보를 보여 준다.</td></tr>
                        <tr><td>Ethernet II</td><td>Src MAC <code>0c:96:cd:cb:c0:27</code>, Dst MAC <code>bc:d0:74:42:2b:d2</code>와 type IPv4를 보여 준다.</td></tr>
                        <tr><td>IPv4</td><td>Src IP <code>122.46.96.85</code>, Dst IP <code>192.168.45.145</code>, TTL, total length, protocol TCP를 보여 준다.</td></tr>
                        <tr><td>TCP</td><td>Src port <code>8080</code>, Dst port <code>62378</code>, sequence number, acknowledgement number, payload length를 보여 준다.</td></tr>
                        <tr><td>HTTP</td><td><code>HTTP/1.1 200 OK</code> header와 HTML body를 보여 준다.</td></tr>
                      </tbody>
                    </table>
                    <div class="callout">핵심: HTTP message가 TCP segment의 payload가 되고, TCP segment가 IP datagram의 payload가 되며, IP datagram이 Ethernet frame의 payload가 된다. 이것이 캡슐화다.</div>
                    """,
                },
                {
                    "heading": "Ethernet과 IPv4 헤더 관찰",
                    "body": f"""
                    <p>Ethernet header는 일반적으로 14byte로 설명된다. 6byte destination MAC address, 6byte source MAC address, 그리고 상위 계층 protocol type으로 구성된다. 강의 화면에서는 <code>Type: IPv4 (0x0800)</code>이 보이므로 Ethernet frame의 payload가 IPv4 datagram이라는 뜻이다.</p>
                    {nb07_ipv4}
                    <p>IPv4 header에서는 특히 source address와 destination address를 확인해야 한다. 지금 선택한 패킷은 서버가 클라이언트에게 보내는 response이므로 source address는 server IP인 <code>122.46.96.85</code>, destination address는 client IP인 <code>192.168.45.145</code>다.</p>
                    <p>또한 <code>Protocol: TCP (6)</code>는 이 IPv4 datagram 안에 TCP segment가 들어 있다는 의미다. <code>Time to Live: 50</code>은 패킷이 네트워크에서 무한히 돌지 않도록 하는 제한값이고, <code>Total Length: 278</code>은 IPv4 datagram 전체 길이를 나타낸다. Header checksum은 header 비트 오류를 확인하기 위한 값이다.</p>
                    """,
                },
                {
                    "heading": "TCP 헤더와 HTTP payload",
                    "body": f"""
                    <p>TCP는 process-to-process logical communication을 제공한다. 그래서 TCP header에서 가장 먼저 봐야 할 값은 port다. 서버에서 클라이언트로 오는 response packet에서는 서버가 source가 되므로 <code>Source Port: 8080</code>이 보이고, 클라이언트 쪽 임시 수신 port가 <code>Destination Port: 62378</code>로 보인다.</p>
                    {nb07_tcp}
                    <p>같은 TCP row에는 <code>Seq: 1</code>, <code>Ack: 478</code>, <code>Len: 226</code>이 표시된다. Sequence number와 acknowledgement number는 TCP가 신뢰적인 연결과 확인 응답을 제공하는 핵심 필드다. <code>Len: 226</code>은 이 TCP segment가 실제 데이터 payload를 226byte 싣고 있다는 뜻이다.</p>
                    {nb07_payload}
                    <p>Wireshark에서 TCP payload 부분을 선택하면 아래 byte pane 오른쪽에 사람이 읽을 수 있는 HTTP 문자열이 보인다. 즉 <code>HTTP/1.1 200 OK</code>, <code>Server: Apache/2.4.41 (Ubuntu)</code>, <code>Content-Length: 22</code>, <code>&lt;h1&gt;80 port test&lt;/h1&gt;</code>가 모두 TCP payload로 들어 있다. 이 장면이 “HTTP는 TCP 위에서 동작한다”는 말을 실제 패킷 단위로 증명한다.</p>
                    """,
                },
                {
                    "heading": "IP 필터와 Follow TCP Stream",
                    "body": f"""
                    <p>HTTP 필터는 HTTP request와 response를 빠르게 찾을 때 좋다. 하지만 TCP handshake나 ACK처럼 HTTP가 아닌 연결 제어 패킷까지 함께 보려면 서버 IP 기준으로 필터링해야 한다. 강의 화면의 서버 IP는 <code>122.46.96.85</code>이므로 display filter는 다음처럼 쓴다.</p>
                    {nb07_ip_filter}
                    {code_block("ip.addr == 122.46.96.85", "text")}
                    <p>이 필터를 적용하면 해당 서버와 오간 모든 IP packet이 보인다. 목록에는 <code>[SYN]</code>, <code>[SYN, ACK]</code>, <code>[ACK]</code> 같은 TCP 연결 설정 패킷과 <code>GET / HTTP/1.1</code>, <code>HTTP/1.1 200 OK</code> 같은 HTTP 패킷이 함께 표시된다.</p>
                    {nb07_stream}
                    <p>HTTP packet을 우클릭해 <strong>Follow TCP Stream</strong>을 선택하면 하나의 TCP 연결에서 오간 request와 response를 대화 흐름처럼 볼 수 있다. 이 화면은 packet list와 packet detail을 따로 펼치지 않아도, 실제 애플리케이션 데이터가 어떤 순서로 오갔는지 빠르게 확인하게 해 준다.</p>
                    {wireshark_tcp_stream}
                    """,
                },
                {
                    "heading": "Flow Graph와 3-way handshake",
                    "body": f"""
                    <p>TCP는 데이터를 보내기 전에 연결을 설정한다. 강의에서는 <code>ip.addr == 122.46.96.85</code> 필터를 적용한 상태에서 <strong>Statistics → Flow Graph</strong>를 열고, <strong>Limit to display filter</strong>를 체크해 해당 서버와의 통신 흐름만 그래프로 본다.</p>
                    {nb07_flow_graph}
                    <p>Flow Graph에서는 client <code>192.168.45.145</code>와 server <code>122.46.96.85</code> 사이의 화살표가 시간순으로 그려진다. HTTP request가 바로 먼저 가는 것이 아니라, 그 전에 TCP 연결 설정 과정이 먼저 나타난다.</p>
                    <div class="diagram">
                      <div><span class="node-title">SYN</span><p>client가 server에게 “연결 설정을 하겠다”고 요청한다.</p></div>
                      <span class="arrow">→</span>
                      <div><span class="node-title">SYN/ACK</span><p>server가 “요청을 확인했고 연결을 수락한다”고 응답한다.</p></div>
                      <span class="arrow">→</span>
                      <div><span class="node-title">ACK</span><p>client가 다시 확인 응답을 보내 연결 설정을 완료한다.</p></div>
                      <span class="arrow">→</span>
                      <div><span class="node-title">HTTP</span><p>연결이 열린 뒤 GET request와 200 OK response가 오간다.</p></div>
                    </div>
                    <p>강사는 실습자가 자기 화면에서 3-way handshake가 다르게 보일 수도 있다고 말한다. 브라우저가 이미 서버와 연결을 수립해 둔 상태라면 새 HTTP 요청 앞에 handshake가 안 보일 수 있다. 이 경우 브라우저를 닫았다가 다시 열고, 캡처를 새로 시작한 뒤 서버에 접속하면 연결 설정부터 관찰하기 쉽다.</p>
                    """,
                },
                {
                    "heading": "실습의 결론",
                    "body": """
                    <p>이번 실습에서 확인한 것은 세 가지다. 첫째, 브라우저가 HTTP 서버에 접속하면 client가 <code>GET / HTTP/1.1</code> request를 보내고 server가 <code>HTTP/1.1 200 OK</code> response를 돌려준다. 둘째, 그 HTTP message는 TCP segment, IPv4 datagram, Ethernet frame 안에 계층적으로 캡슐화되어 전달된다. 셋째, TCP는 HTTP 데이터를 보내기 전에 SYN, SYN/ACK, ACK의 3-way handshake로 연결을 먼저 만든다.</p>
                    <p>패킷 분석을 할 때는 payload만 보는 것으로 끝내면 안 된다. Ethernet의 MAC 주소, IPv4의 source/destination address와 TTL, TCP의 port·sequence·acknowledgement number, HTTP의 header와 body를 함께 읽어야 한다. 그래야 프로토콜 분석, 침해사고 대응, 포렌식, 취약점 분석에서 실제 네트워크 증거를 올바르게 해석할 수 있다.</p>
                    <p>다음 강의에서는 이 네트워크 흐름을 보는 단계에서 한 걸음 더 나아가, TCP와 UDP socket programming으로 client-server 통신을 직접 구현한다.</p>
                    """,
                },
            ],
            "checks": [
                "Wireshark에서 HTTP 패킷만 보기 위해 어떤 display filter를 쓰는지 기억하는가?",
                "HTTP request와 response에서 각각 어떤 정보를 확인할 수 있는가?",
                "Frame, Ethernet, IPv4, TCP, HTTP가 캡슐화 구조와 어떻게 대응되는지 설명할 수 있는가?",
                "TCP 3-way handshake를 Flow Graph에서 SYN, SYN/ACK, ACK 순서로 확인할 수 있는가?",
            ],
        },
        {
            "id": "1-8",
            "title": "소켓 프로그래밍",
            "subtitle": "UDP와 TCP 소켓으로 클라이언트-서버 애플리케이션을 구현하는 기본 흐름을 이해한다.",
            "tags": ["Socket", "UDP 프로그래밍", "TCP 프로그래밍"],
            "objectives": [
                "소켓이 애플리케이션과 전송 계층 사이의 통신 출입구라는 점을 설명한다.",
                "UDP 소켓 프로그래밍의 비연결형 흐름과 sendto/recvfrom 구조를 이해한다.",
                "TCP 소켓 프로그래밍의 welcome socket, connect, listen, accept, connection socket 흐름을 이해한다.",
            ],
            "sections": [
                {
                    "heading": "소켓 프로그래밍의 목적",
                    "body": f"""
                    <p>마지막 강의는 <strong>socket programming</strong>으로 client/server 애플리케이션을 어떻게 만드는지 소개한다. 우리가 사용하는 대부분의 애플리케이션은 네트워크를 거치며, 내부에서는 TCP 또는 UDP 기반 소켓을 통해 데이터를 주고받는다.</p>
                    {nb08_socket_intro}
                    <p>소켓은 호스트의 application layer와 transport layer 사이의 인터페이스다. 애플리케이션은 소켓에 데이터를 넣고, transport layer는 TCP나 UDP 규칙에 맞춰 segment 또는 datagram을 처리한다. 강의에서는 소켓 유형을 크게 <strong>UDP socket</strong>과 <strong>TCP socket</strong>으로 나누어 본다.</p>
                    <p>이 강의의 목표는 완성된 대규모 서버 프로그램을 만드는 것이 아니라, 네트워크 애플리케이션의 최소 구조를 이해하는 것이다. 즉 server와 client가 각각 socket을 만들고, 어떤 함수로 데이터를 보내고 받으며, TCP에서는 왜 연결 설정이 먼저 필요한지를 파악하는 데 집중한다.</p>
                    """,
                },
                {
                    "heading": "UDP 소켓 프로그래밍 흐름",
                    "body": f"""
                    <p>UDP는 비연결형 프로토콜이다. 데이터를 보내기 전에 TCP처럼 handshake로 연결을 설정하지 않는다. Sender는 각 packet에 destination IP와 port를 붙여 보내고, receiver는 수신된 packet에서 보낸 사람의 IP와 port를 추출한다.</p>
                    {nb08_udp_flow}
                    <p>그림에서 server와 client는 각각 socket을 연다. 이때 UDP socket은 <code>socket(AF_INET, SOCK_DGRAM)</code>으로 만든다. <code>AF_INET</code>은 IPv4를 의미하고, <code>SOCK_DGRAM</code>은 UDP datagram socket을 의미한다.</p>
                    <div class="diagram">
                      <div><span class="node-title">서버 소켓</span><p>UDP socket 생성 후 port bind</p></div>
                      <span class="arrow">←</span>
                      <div><span class="node-title">클라이언트</span><p>서버 IP와 port로 datagram 전송</p></div>
                      <span class="arrow">→</span>
                      <div><span class="node-title">응답</span><p>서버가 client address로 datagram 반환</p></div>
                    </div>
                    <p>Client는 message를 datagram으로 만들어 server IP와 port로 보낸다. Server는 UDP segment를 읽고, 처리 결과를 다시 client address와 port로 보낸다. Client는 응답을 받은 뒤 할 일을 마치면 socket을 닫는다. 흐름은 간단하지만 UDP는 신뢰성을 제공하지 않기 때문에 전송 데이터가 손실될 수 있다는 점을 함께 기억해야 한다.</p>
                    """,
                },
                {
                    "heading": "UDP client 예시",
                    "body": f"""
                    <p>강의 화면의 UDP client는 Python <code>socket</code> 모듈을 사용한다. <code>serverName</code>에는 server host name 또는 IP가 들어가고, <code>serverPort</code>에는 12000이 들어간다. 그 다음 <code>clientSocket = socket(AF_INET, SOCK_DGRAM)</code>으로 IPv4 기반 UDP socket을 생성한다.</p>
                    {nb08_udp_client}
                    {udp_client}
                    <p><code>sendto</code>는 UDP에서 중요한 함수다. TCP처럼 먼저 연결된 상대가 있는 것이 아니므로, 보낼 message와 함께 목적지인 <code>(serverName, serverPort)</code>를 매번 넘겨 준다. <code>recvfrom(2048)</code>은 server의 응답 data와 그 응답이 온 server address를 함께 반환한다. 마지막으로 client는 <code>clientSocket.close()</code>로 socket을 닫는다.</p>
                    """,
                },
                {
                    "heading": "UDP server 예시",
                    "body": f"""
                    <p>UDP server도 마찬가지로 <code>socket(AF_INET, SOCK_DGRAM)</code>으로 UDP socket을 만든다. Server는 client가 찾아올 수 있도록 특정 port를 socket에 묶어야 하므로 <code>serverSocket.bind(('', serverPort))</code>를 호출한다. 강의 예시는 12000번 port를 사용한다.</p>
                    {nb08_udp_server}
                    {udp_server}
                    <p>Server는 <code>while True</code> 반복문 안에서 계속 client 요청을 기다린다. <code>recvfrom(2048)</code>은 client가 보낸 message와 client address를 함께 반환한다. Server는 message를 decode한 뒤 <code>upper()</code>로 대문자로 바꾸고, <code>sendto</code>를 이용해 같은 client address로 다시 보낸다. UDP server는 연결을 유지하지 않으므로 매 요청에서 sender address를 함께 다루는 구조가 된다.</p>
                    """,
                },
                {
                    "heading": "TCP 소켓 프로그래밍 흐름",
                    "body": f"""
                    <p>TCP는 UDP와 달리 데이터를 주고받기 전에 연결이 수립되어야 한다. Server에는 client의 연결 요청을 기다리는 <strong>welcome socket</strong>이 열려 있고, client는 server IP와 port로 “연결하고 싶다”고 요청한다. 이 과정에서 TCP 3-way handshake가 수행된다.</p>
                    {nb08_tcp_concept}
                    <p>연결이 수립되면 server는 welcome socket과 별개의 <strong>connection socket</strong>을 생성한다. 실제 data 송수신은 이 connection socket을 통해 이루어진다. Welcome socket은 계속 열려 있으므로 server는 다음 client의 연결 요청도 받을 수 있다.</p>
                    {nb08_tcp_flow}
                    <p>이 구조 덕분에 server는 여러 client와 통신할 수 있고, 각 client는 source port 등으로 구분된다. TCP는 client-server 사이에 신뢰성 있는 연결을 제공하며, 연결 설정 이후에는 byte stream 형태로 데이터를 주고받는다.</p>
                    <table>
                      <thead><tr><th>요소</th><th>역할</th></tr></thead>
                      <tbody>
                        <tr><td>welcome socket</td><td>서버가 클라이언트 연결 요청을 기다리는 소켓이다.</td></tr>
                        <tr><td>connect</td><td>클라이언트가 서버와 TCP connection을 만들기 위해 호출한다.</td></tr>
                        <tr><td>listen</td><td>서버가 연결 요청을 받을 준비를 한다.</td></tr>
                        <tr><td>accept</td><td>연결 요청을 받아 connection socket을 만든다.</td></tr>
                        <tr><td>connection socket</td><td>연결된 client와 실제 데이터를 주고받는 소켓이다.</td></tr>
                      </tbody>
                    </table>
                    """,
                },
                {
                    "heading": "TCP client 예시",
                    "body": f"""
                    <p>TCP client는 UDP client와 마찬가지로 server name과 server port를 지정하지만, socket type이 다르다. <code>socket(AF_INET, SOCK_STREAM)</code>은 IPv4 기반 TCP socket을 의미한다. UDP의 <code>SOCK_DGRAM</code>과 달리 TCP는 <code>SOCK_STREAM</code>을 사용한다.</p>
                    {nb08_tcp_client}
                    {tcp_client}
                    <p>가장 중요한 차이는 <code>clientSocket.connect((serverName, serverPort))</code>다. TCP는 데이터를 보내기 전에 연결이 먼저 이루어져야 하므로, 이 connect 호출에서 TCP connection setup, 즉 3-way handshake가 수행된다. 그 다음에는 <code>send</code>로 데이터를 보내고, <code>recv(1024)</code>로 server response를 받는다. 통신이 끝나면 client socket을 닫는다.</p>
                    """,
                },
                {
                    "heading": "TCP server 예시",
                    "body": f"""
                    <p>TCP server는 먼저 <code>serverSocket = socket(AF_INET, SOCK_STREAM)</code>으로 TCP socket을 만든다. 그 다음 <code>bind</code>로 12000번 port에 server socket을 묶고, <code>listen(1)</code>으로 client가 문을 두드리기를 기다린다.</p>
                    {nb08_tcp_server}
                    {tcp_server}
                    <p>Client가 TCP 연결 요청을 보내면 <code>serverSocket.accept()</code>가 호출되고, 이때 <code>connectionSocket</code>이 만들어진다. Server는 이 connection socket에서 <code>recv(1024)</code>로 문장을 받고, <code>upper()</code>로 대문자로 바꾼 뒤 <code>send</code>로 돌려준다. 마지막에 닫는 것은 welcome socket이 아니라 해당 client와 통신하던 connection socket이다.</p>
                    """,
                },
                {
                    "heading": "UDP와 TCP 구현 차이",
                    "body": """
                    <table>
                      <thead><tr><th>구분</th><th>UDP</th><th>TCP</th></tr></thead>
                      <tbody>
                        <tr><td>연결 설정</td><td>없다.</td><td>connect와 3-way handshake가 있다.</td></tr>
                        <tr><td>전송 함수 감각</td><td>sendto/recvfrom으로 주소를 함께 다룬다.</td><td>연결 후 send/recv로 통신한다.</td></tr>
                        <tr><td>서버 구조</td><td>bind 후 반복적으로 datagram을 읽는다.</td><td>listen 후 accept로 connection socket을 만든다.</td></tr>
                        <tr><td>신뢰성</td><td>기본 제공하지 않는다.</td><td>신뢰성 있는 전송을 제공한다.</td></tr>
                        <tr><td>종료</td><td>클라이언트가 할 일을 마치면 socket을 닫는다.</td><td>통신이 끝난 connection socket을 닫고 welcome socket은 계속 유지할 수 있다.</td></tr>
                      </tbody>
                    </table>
                    """,
                },
                {
                    "heading": "과목 마무리",
                    "body": """
                    <p>강의는 네트워크 기초 과목 전체를 마무리한다. 지금까지 네트워크가 어떻게 흘러가는지, TCP/IP 계층 구조와 각 계층의 원리, 실제 패킷 분석, 기본적인 소켓 프로그래밍 흐름을 배웠다. 멘토는 이 내용이 앞으로 해킹 공부, 포렌식, 다양한 보안 진로에 도움이 되기를 바란다고 말한다.</p>
                    <p>오프라인 강의에서는 더 심화된 내용을 다룰 예정이므로, 온라인 강의에서 다룬 계층 구조, HTTP, TCP/UDP, Wireshark, socket programming을 개인적으로 복습하고 오프라인에서 더 실습해 보자고 안내하며 마무리한다.</p>
                    """,
                },
            ],
            "checks": [
                "UDP client/server가 연결 설정 없이 datagram을 주고받는 흐름을 설명할 수 있는가?",
                "Python socket에서 AF_INET과 SOCK_DGRAM이 무엇을 의미하는지 기억하는가?",
                "TCP server에서 welcome socket과 connection socket이 왜 구분되는지 말할 수 있는가?",
                "TCP client가 데이터를 보내기 전에 connect를 호출해야 하는 이유를 이해했는가?",
                "UDP와 TCP 소켓 프로그래밍의 함수 흐름 차이를 표 없이도 설명할 수 있는가?",
            ],
        },
    ]
