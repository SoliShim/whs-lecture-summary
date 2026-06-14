def build_computer_architecture_1_lectures(code_block, screen_figure, image_figure):
    ca01 = "컴퓨터 구조 1-01-강의-목차"
    ca01_intro = screen_figure(
        "computer-architecture-1",
        ca01,
        1,
        "컴퓨터 구조 I 강의 시작",
        "이현재 멘토가 WhiteHat School 컴퓨터 구조 기초 과정을 시작하며, 이 과목이 보안·개발 학습을 위한 기초 구조 감각을 만드는 수업임을 안내한다.",
    )
    ca01_outline = screen_figure(
        "computer-architecture-1",
        ca01,
        3,
        "컴퓨터 구조 I 강의 목차",
        "강의는 컴퓨터 시스템 개요, 데이터 표현, 중앙처리장치(CPU), 메모리, 입출력 시스템의 다섯 주제로 구성된다.",
    )
    ca02 = "컴퓨터 구조 1-02-컴퓨터-시스템-개요"
    ca02_title = screen_figure(
        "computer-architecture-1",
        ca02,
        1,
        "컴퓨터 시스템의 개요",
        "2강은 컴퓨터가 무엇인지 정의하고, 컴퓨터의 형태와 구성요소, 역사, CPU 아키텍처 이름을 연결해서 설명한다.",
    )
    ca02_definition_wiki = screen_figure(
        "computer-architecture-1",
        ca02,
        3,
        "위키 기반 컴퓨터 정의",
        "컴퓨터를 전산기, 프로그램 가능한 전자적 기계 장치, 정보의 입력·처리·출력 장치로 설명하는 일반적인 정의를 먼저 살펴본다.",
    )
    ca02_definition_chatgpt = screen_figure(
        "computer-architecture-1",
        ca02,
        6,
        "쉽게 풀어쓴 컴퓨터 정의",
        "강사는 컴퓨터를 '데이터를 처리하고 명령에 따라 작업을 수행하는 전자 장치'로 잡고, 여기에 프로그램 가능성이 더해져야 일반적인 컴퓨터에 가까워진다고 설명한다.",
    )
    ca02_types = screen_figure(
        "computer-architecture-1",
        ca02,
        13,
        "컴퓨터의 다양한 형태",
        "슈퍼컴퓨터, 메인프레임, 미니컴퓨터·서버, 데스크톱, 노트북, 태블릿, 스마트폰, 임베디드 시스템처럼 컴퓨터는 목적과 규모에 따라 다양하다.",
    )
    ca02_embedded = screen_figure(
        "computer-architecture-1",
        ca02,
        20,
        "특수 목적 시스템 예시",
        "EPS 같은 특수 목적 시스템은 범용 PC와 달리 특정 기능과 환경에 맞춰 최적화된 컴퓨터 시스템으로 볼 수 있다.",
    )
    ca02_components = screen_figure(
        "computer-architecture-1",
        ca02,
        21,
        "CPU, 메모리, 입출력 장치",
        "데스크톱 컴퓨터를 기준으로 보면 CPU는 명령을 해석·실행하고, 메모리는 데이터를 저장하며, 입출력 장치는 컴퓨터와 외부 세계를 연결한다.",
    )
    ca02_danawa = screen_figure(
        "computer-architecture-1",
        ca02,
        26,
        "PC 부품 견적 화면으로 보는 구성요소",
        "PC 견적 화면의 CPU, 메인보드, RAM, 저장 장치 같은 항목을 직접 보면 컴퓨터 시스템 구성요소가 실제 부품과 연결된다.",
    )
    ca02_arch_keywords = screen_figure(
        "computer-architecture-1",
        ca02,
        32,
        "역사를 이해하기 위한 핵심 키워드",
        "x86, ARM, 폰 노이만, Apple Silicon, CISC, RISC 같은 단어는 CPU와 프로그램 호환성을 이해할 때 반복해서 등장한다.",
    )
    ca02_vscode_arch = screen_figure(
        "computer-architecture-1",
        ca02,
        36,
        "다운로드 페이지의 아키텍처 선택",
        "Visual Studio Code 다운로드 화면의 x64, x86, Arm64 선택지는 실행할 CPU 아키텍처에 맞는 프로그램 빌드가 다르다는 사실을 보여 준다.",
    )
    ca02_history = screen_figure(
        "computer-architecture-1",
        ca02,
        41,
        "컴퓨터 구조 역사 흐름",
        "튜링 머신, ENIAC, 폰 노이만 구조, 트랜지스터, 마이크로프로세서, RISC, 멀티코어, ARM, Apple M1로 이어지는 큰 흐름을 연표처럼 훑는다.",
    )
    ca02_x86_chip = screen_figure(
        "computer-architecture-1",
        ca02,
        61,
        "8086에서 이어진 x86 계열",
        "x86이라는 이름은 Intel 8086 계열에서 출발했고, 실무 다운로드 화면에서는 보통 32비트 프로그램 선택지로 자주 만난다.",
    )
    ca03_title = image_figure(
        "../../../../assets/generated/computer-architecture-1/lesson-03/ca1-l03-0001.jpg",
        "데이터 표현 강의 시작",
        "3강은 컴퓨터가 0과 1로 데이터를 표현하는 방식, 비트와 바이트, 정수와 실수 표현, 오버플로우 사례를 다룬다.",
    )
    ca03_transistor_bit = image_figure(
        "../../../../assets/generated/computer-architecture-1/lesson-03/ca1-l03-0002.jpg",
        "트랜지스터에서 1비트로",
        "트랜지스터의 on/off 상태를 1과 0으로 해석하고, 이 한 칸의 0 또는 1을 1bit로 본다.",
    )
    ca03_byte = image_figure(
        "../../../../assets/generated/computer-architecture-1/lesson-03/ca1-l03-0019.jpg",
        "8bit는 1byte",
        "0과 1 하나가 bit이고, 8개의 bit가 모이면 파일 크기와 메모리 크기를 이야기하는 기본 단위인 byte가 된다.",
    )
    ca03_units = image_figure(
        "../../../../assets/generated/computer-architecture-1/lesson-03/ca1-l03-0020.jpg",
        "SI 단위와 IEC 단위",
        "KB, MB, GB는 1000배 단위로, KiB, MiB, GiB는 1024배 단위로 계산한다는 차이를 표로 정리한다.",
    )
    ca03_binary_85 = image_figure(
        "../../../../assets/generated/computer-architecture-1/lesson-03/ca1-l03-0043.jpg",
        "이진수 자리값과 85",
        "01010101에서 켜진 자리의 2의 거듭제곱 값을 더해 64 + 16 + 4 + 1 = 85가 되는 과정을 보여 준다.",
    )
    ca03_char_type = image_figure(
        "../../../../assets/generated/computer-architecture-1/lesson-03/ca1-l03-0047.jpg",
        "자료형과 char의 크기",
        "C 언어의 char는 1byte이고, 같은 8bit라도 signed인지 unsigned인지에 따라 표현 범위가 달라진다.",
    )
    ca03_fixed_point = image_figure(
        "../../../../assets/generated/computer-architecture-1/lesson-03/ca1-l03-0063.jpg",
        "고정소수점 방식",
        "소수점 위치를 고정하고 정수 부분과 소수 부분을 나눠 해석하면, 소수 부분은 2^-1, 2^-2처럼 작아지는 자리값을 가진다.",
    )
    ca03_float_range = image_figure(
        "../../../../assets/generated/computer-architecture-1/lesson-03/ca1-l03-0068.jpg",
        "자료형별 표현 범위",
        "자료형마다 bit 공간을 부호, 지수, 가수 등으로 어떻게 나누느냐에 따라 표현 가능한 범위가 크게 달라진다.",
    )
    ca03_float_layout = image_figure(
        "../../../../assets/generated/computer-architecture-1/lesson-03/ca1-l03-0080.jpg",
        "지수부와 유효숫자로 바뀌는 표현",
        "부동소수점은 지수부와 유효숫자 부분을 나눠 더 넓은 범위의 실수를 표현한다.",
    )
    ca03_overflow_255 = image_figure(
        "../../../../assets/generated/computer-architecture-1/lesson-03/ca1-l03-0083.jpg",
        "8bit가 모두 켜진 255",
        "부호 없는 8bit에서 모든 bit가 1이면 255가 되며, 여기서 1을 더하면 표현 가능한 범위를 넘어선다.",
    )
    ca03_overflow_prompt = image_figure(
        "../../../../assets/generated/computer-architecture-1/lesson-03/ca1-l03-0099.jpg",
        "오버플로우의 잘못된 표현",
        "표현 범위를 넘은 값은 0처럼 돌아가거나 음수처럼 보이는 등 자료형 해석 방식에 따라 잘못된 결과가 될 수 있다.",
    )
    ca03_youtube_overflow = image_figure(
        "../../../../assets/generated/computer-architecture-1/lesson-03/ca1-l03-0102.jpg",
        "강남스타일과 YouTube 조회 수 제한",
        "강남스타일 조회 수가 기존 YouTube view limit을 넘은 사례는 정수 표현 범위와 오버플로우가 실제 서비스 문제로 이어질 수 있음을 보여 준다.",
    )
    ca04 = "컴퓨터 구조 1-04-중앙처리장치-CPU"
    ca04_title = screen_figure(
        "computer-architecture-1",
        ca04,
        1,
        "중앙처리장치(CPU) 강의 시작",
        "4강은 CPU 자체를 외우기보다, 컴퓨터가 프로그램을 실행하는 과정을 따라가며 CPU의 역할을 이해하는 방식으로 진행된다.",
    )
    ca04_execution_flow = screen_figure(
        "computer-architecture-1",
        ca04,
        2,
        "소스 코드에서 기계어까지",
        "사람이 작성한 소스 코드는 어셈블리어에 가까운 중간 표현을 거쳐, CPU가 해석하는 기계어와 바이너리로 바뀐다.",
    )
    ca04_hello_code = screen_figure(
        "computer-architecture-1",
        ca04,
        13,
        "Hello World C 코드",
        "강의는 가장 단순한 C 프로그램을 예로 들어, 짧은 소스 코드도 실제 실행 전에는 어셈블리어와 기계어로 바뀐다는 점을 보여 준다.",
    )
    ca04_assembly_listing = screen_figure(
        "computer-architecture-1",
        ca04,
        16,
        "어셈블리어로 바뀐 코드",
        "C 코드가 컴파일되면 사람이 보기에는 난해하지만 CPU 명령어에 가까운 어셈블리어 형태가 나타난다.",
    )
    ca04_mov_instruction = screen_figure(
        "computer-architecture-1",
        ca04,
        18,
        "mov destination, source",
        "mov 명령은 source의 데이터를 destination으로 복사하는 대표적인 어셈블리 명령으로 소개된다.",
    )
    ca04_machine_code = screen_figure(
        "computer-architecture-1",
        ca04,
        24,
        "기계어와 16진수 덤프",
        "최종 바이너리는 사람이 읽기 어려운 바이트의 나열이며, 보통 16진수 덤프와 어셈블리 매핑으로 확인한다.",
    )
    ca04_fde = screen_figure(
        "computer-architecture-1",
        ca04,
        40,
        "Fetch, Decode, Execute",
        "CPU의 기본 실행 과정은 명령어를 가져오고, 해독하고, 실행하는 세 단계로 설명된다.",
    )
    ca04_extended_cycle = screen_figure(
        "computer-architecture-1",
        ca04,
        47,
        "Memory Access와 Write-back",
        "실제 명령 실행은 메모리 접근과 결과 저장 단계를 포함해 더 세밀하게 나눠 볼 수 있다.",
    )
    ca04_optimizations = screen_figure(
        "computer-architecture-1",
        ca04,
        55,
        "CPU 실행 최적화 아이디어",
        "파이프라이닝, 분기 예측, 명령어 병렬처리는 CPU가 실행 사이클을 더 효율적으로 쓰기 위한 대표적인 아이디어다.",
    )
    ca04_execution_diagram = screen_figure(
        "computer-architecture-1",
        ca04,
        59,
        "CPU와 메모리가 프로그램을 실행하는 그림",
        "메모리에 놓인 명령어와 데이터가 버스를 통해 CPU로 오가고, CPU가 가져오기·해석·실행·저장을 반복한다.",
    )
    ca04_cisc_risc = screen_figure(
        "computer-architecture-1",
        ca04,
        80,
        "CISC와 RISC 비교",
        "CPU마다 명령어 집합이 다르고, 이를 크게 복잡한 명령어 집합과 단순화한 명령어 집합의 관점으로 비교할 수 있다.",
    )
    ca04_cpu_structure = screen_figure(
        "computer-architecture-1",
        ca04,
        95,
        "CPU 내부 구조",
        "Control Unit, ALU, Registers, CPU Interconnection이 명령 해석, 연산, 임시 저장, 내부 연결을 담당한다.",
    )
    ca04_multicore = screen_figure(
        "computer-architecture-1",
        ca04,
        103,
        "멀티코어 컴퓨터 구조",
        "하나의 프로세서 안에 여러 코어를 담으면 여러 실행 단위를 병렬로 활용할 수 있다.",
    )
    ca05 = "컴퓨터 구조 1-05-메모리-메모리와-시스템"
    ca05_title = screen_figure(
        "computer-architecture-1",
        ca05,
        1,
        "메모리와 시스템 강의 시작",
        "5강은 메모리를 실행 중인 프로그램의 명령어, 데이터, 중간 결과가 저장되는 공간으로 보고 디버거와 시스템 해킹 관점까지 연결한다.",
    )
    ca05_role = screen_figure(
        "computer-architecture-1",
        ca05,
        2,
        "메모리의 역할",
        "메모리는 실행 중인 프로그램, 중간 결과, 다양한 데이터를 저장하는 공간이라는 정의에서 강의가 시작된다.",
    )
    ca05_vscode_debug = screen_figure(
        "computer-architecture-1",
        ca05,
        4,
        "VS Code 디버거와 변수 상태",
        "중단점에서 멈춘 순간 Locals 창에 x, y, z 값이 표시되고, 아직 실행되지 않은 대입문 때문에 쓰레기값을 관찰할 수 있다.",
    )
    ca05_gdb_disassemble = screen_figure(
        "computer-architecture-1",
        ca05,
        23,
        "GDB disassemble main",
        "GDB의 disassemble 명령은 main 함수의 기계어를 어셈블리어 형태로 풀어 보여 주며, 주소와 명령어가 함께 표시된다.",
    )
    ca05_gdb_registers = screen_figure(
        "computer-architecture-1",
        ca05,
        31,
        "GDB 레지스터 확인",
        "break main, run 이후 info register로 eax, esp, ebp, eip 같은 레지스터 값을 확인하는 화면이다.",
    )
    ca05_gdb_memory_formats = screen_figure(
        "computer-architecture-1",
        ca05,
        38,
        "GDB 메모리 표현 방식",
        "같은 주소의 값을 8진수, 16진수, 10진수, 2진수처럼 다른 형식으로 표현할 수 있음을 보여 준다.",
    )
    ca05_big_endian = screen_figure(
        "computer-architecture-1",
        ca05,
        43,
        "빅 엔디안 저장 순서",
        "0x12345678에서 큰 자리 바이트 0x12가 낮은 주소에 먼저 저장되는 방식을 도식으로 보여 준다.",
    )
    ca05_little_endian = screen_figure(
        "computer-architecture-1",
        ca05,
        47,
        "리틀 엔디안 저장 순서",
        "0x12345678에서 작은 자리 바이트 0x78이 낮은 주소에 먼저 저장되어 디버거에서 값이 거꾸로 보일 수 있다.",
    )
    ca05_ram_rom = screen_figure(
        "computer-architecture-1",
        ca05,
        72,
        "RAM과 ROM 비교",
        "RAM은 읽기·쓰기 가능하고 휘발성이며, ROM은 읽기 중심이고 비휘발성이라는 차이를 표로 정리한다.",
    )
    ca05_hierarchy = screen_figure(
        "computer-architecture-1",
        ca05,
        87,
        "메모리 계층 구조",
        "CPU 레지스터, 캐시, 메인 메모리, 디스크 저장 장치로 내려갈수록 용량은 커지고 싸지지만 접근 시간은 느려진다.",
    )
    ca06 = "컴퓨터 구조 1-06-입출력-시스템"
    ca06_title = screen_figure(
        "computer-architecture-1",
        ca06,
        1,
        "입출력 시스템 강의 시작",
        "마지막 강의는 컴퓨터와 외부 세계를 연결하는 입출력 시스템을 버스, 포트, USB, 인터럽트, DMA 순서로 설명한다.",
    )
    ca06_bus = screen_figure(
        "computer-architecture-1",
        ca06,
        4,
        "시스템 버스 구조",
        "CPU, 메모리, 입출력 장치가 control bus, address bus, data bus를 통해 연결되는 구조를 보여 준다.",
    )
    ca06_ports = screen_figure(
        "computer-architecture-1",
        ca06,
        8,
        "여러 입출력 포트",
        "USB Type-A, Ethernet, HDMI, DisplayPort, USB-C, Thunderbolt, Lightning 등 다양한 물리 포트를 한 화면에 정리한다.",
    )
    ca06_usb_connectors = screen_figure(
        "computer-architecture-1",
        ca06,
        27,
        "USB 커넥터의 범용성",
        "Universal Serial Bus는 주변 기기를 쉽게 연결하기 위한 범용 직렬 버스이며, 여러 형태의 USB 커넥터가 함께 소개된다.",
    )
    ca06_udev = screen_figure(
        "computer-architecture-1",
        ca06,
        40,
        "리눅스 udev 장치 관리자",
        "udev는 Linux 커널용 장치 관리자이며, /dev 장치 노드와 장치 추가·제거 이벤트 처리와 연결된다.",
    )
    ca06_usb_if = screen_figure(
        "computer-architecture-1",
        ca06,
        62,
        "USB-IF class code",
        "USB-IF의 class code 표에서는 Base Class 08h를 Mass Storage 장치로 정의하는 식으로 장치 종류를 표준화한다.",
    )
    ca06_usb_ids = screen_figure(
        "computer-architecture-1",
        ca06,
        72,
        "usb.ids의 vendor/device 정보",
        "usb.ids에는 vendor ID와 device ID가 제조사와 장치 이름으로 매핑되어 있어, USB 장치 식별에 활용할 수 있다.",
    )
    ca06_interrupt_cycle = screen_figure(
        "computer-architecture-1",
        ca06,
        80,
        "인터럽트 사이클",
        "CPU가 Fetch와 Execute를 반복하는 중간에 interrupt를 확인하고 처리한 뒤 원래 흐름으로 돌아가는 구조를 보여 준다.",
    )
    ca06_dma = screen_figure(
        "computer-architecture-1",
        ca06,
        99,
        "DMA 전송 구조",
        "DMA가 없을 때는 CPU가 입출력 데이터 이동을 직접 처리하지만, DMA를 쓰면 컨트롤러가 메모리와 장치 사이 전송을 맡아 CPU 부담을 줄인다.",
    )
    ca06_wrapup = screen_figure(
        "computer-architecture-1",
        ca06,
        106,
        "컴퓨터 구조 I 강의 마무리",
        "강의 마지막에는 CPU, 메모리, 입출력의 기본 원리를 이해하면 개발과 보안 학습 모두에 도움이 된다고 정리한다.",
    )

    return [
        {
            "id": "1-1",
            "title": "강의 목차와 학습 방향",
            "transcript_title": "강의 목차",
            "subtitle": "컴퓨터 구조 I는 컴퓨터의 의미, 데이터 표현, CPU, 메모리, 입출력 시스템을 넓게 훑는 기초 과목이다.",
            "tags": ["오리엔테이션", "학습 범위", "컴퓨터 구조"],
            "objectives": [
                "이현재 멘토가 어떤 관점에서 컴퓨터 구조 기초를 설명하는지 이해한다.",
                "컴퓨터 구조 I에서 다루는 다섯 가지 큰 주제를 순서대로 파악한다.",
                "이 과목이 깊은 전공 이론보다 앞으로의 보안·개발 학습을 위한 기초 감각을 만드는 강의임을 이해한다.",
            ],
            "sections": [
                {
                    "heading": "멘토 소개와 강의 분위기",
                    "body": """
                    <p>강의는 이현재 멘토의 소개로 시작한다. 멘토는 알렙이라는 회사에서 약 3년 동안 보안 제품을 개발하고 있다고 설명한다. 이 과목은 컴퓨터 구조를 아주 깊은 전공 과목처럼 끝까지 파고드는 수업이라기보다, 앞으로 개발이나 보안을 배울 때 반드시 마주치는 기본 개념을 학생 눈높이에 맞춰 넓게 훑는 수업이다.</p>
                    """ + ca01_intro + """
                    <p>멘토는 “편하게 들어도 된다”고 강조한다. 다양한 배경의 학생들이 들을 수 있기 때문에 너무 세부적인 하드웨어 회로 이론으로 들어가기보다는, 최소한 알고 있어야 할 핵심 개념을 골라 설명하겠다는 취지다. 부족하거나 더 궁금한 부분은 이후 멘토에게 질문하면 된다고 안내한다.</p>
                    <p>따라서 이 강의록을 읽을 때도 각 부품의 세부 회로를 모두 외우려 하기보다, 앞으로 시스템 해킹, 리버싱, 운영체제, C 언어를 공부할 때 계속 만날 단어들을 먼저 익숙하게 만드는 데 초점을 두면 된다.</p>
                    """,
                },
                {
                    "heading": "과목의 다섯 가지 큰 흐름",
                    "body": """
                    <p>컴퓨터 구조 I는 다섯 덩어리로 진행된다. 처음에는 컴퓨터가 무엇인지부터 시작하고, 그 다음 컴퓨터가 데이터를 어떻게 표현하는지, CPU가 명령을 어떻게 처리하는지, 메모리가 어떤 역할을 하는지, 마지막으로 입출력 시스템이 컴퓨터와 외부 세계를 어떻게 연결하는지를 다룬다.</p>
                    """ + ca01_outline + """
                    <table>
                      <thead><tr><th>순서</th><th>주제</th><th>강의에서 잡는 핵심 질문</th></tr></thead>
                      <tbody>
                        <tr><td>1</td><td>컴퓨터란 무엇인가</td><td>컴퓨터를 단순한 기계가 아니라 명령에 따라 작업하는 전자 장치로 이해한다.</td></tr>
                        <tr><td>2</td><td>데이터 표현</td><td>0과 1, 비트와 바이트, 정수와 실수, 오버플로우를 이해한다.</td></tr>
                        <tr><td>3</td><td>CPU</td><td>프로그램이 명령어가 되고 CPU가 Fetch, Decode, Execute를 반복하는 흐름을 이해한다.</td></tr>
                        <tr><td>4</td><td>메모리</td><td>프로그램 실행 중 데이터와 명령어가 저장되고 이동하는 방식을 이해한다.</td></tr>
                        <tr><td>5</td><td>입출력 시스템</td><td>키보드, 마우스, USB, 버스, 포트, 인터럽트처럼 외부와 연결되는 구조를 이해한다.</td></tr>
                      </tbody>
                    </table>
                    """,
                },
                {
                    "heading": "왜 넓게 훑는가",
                    "body": """
                    <p>멘토는 이 과목에서 모든 세부 내용을 다 가르치려 하기보다, 앞으로 배우게 될 C 언어, 어셈블리어, 시스템 해킹, 리버싱, 운영체제 수업에서 다시 등장할 단어들을 미리 익숙하게 만드는 것을 목표로 삼는다. 예를 들어 CPU, 메모리, 레지스터, 명령어, 버스, 인터럽트 같은 단어는 처음 들으면 낯설지만, 이후 실습에서 반복적으로 등장한다.</p>
                    <div class="callout">이 강의의 핵심 태도는 “지금 완벽히 외우기”가 아니라 “나중에 다시 만났을 때 겁먹지 않도록 큰 그림을 잡기”다.</div>
                    """,
                },
                {
                    "heading": "학생이 잡아야 할 학습 전략",
                    "body": """
                    <p>이 과목은 암기식 목록으로만 보면 지루해질 수 있다. 강의 흐름을 따라가며 “프로그램이 실행되려면 어떤 부품이 어떤 순서로 관여하는가”를 계속 떠올리는 것이 좋다. 데이터는 메모리에 있고, CPU는 명령을 가져와 해석하고 실행하며, 입출력 장치는 외부에서 신호를 주거나 결과를 보여 준다.</p>
                    <div class="diagram">
                      <div><span class="node-title">데이터</span><p>0과 1로 표현된다.</p></div>
                      <span class="arrow">→</span>
                      <div><span class="node-title">메모리</span><p>명령어와 데이터를 저장한다.</p></div>
                      <span class="arrow">→</span>
                      <div><span class="node-title">CPU</span><p>명령을 해석하고 실행한다.</p></div>
                      <span class="arrow">→</span>
                      <div><span class="node-title">입출력</span><p>외부 세계와 연결한다.</p></div>
                    </div>
                    """,
                },
            ],
            "checks": [
                "컴퓨터 구조 I에서 다루는 다섯 주제를 순서대로 말할 수 있는가?",
                "이 강의가 깊은 회로 이론보다 기초 개념의 큰 그림을 잡는 수업이라는 점을 이해했는가?",
                "CPU, 메모리, 입출력 장치가 이후 보안·개발 학습에서 왜 반복적으로 등장하는지 설명할 수 있는가?",
            ],
        },
        {
            "id": "1-2",
            "title": "컴퓨터 시스템 개요",
            "subtitle": "컴퓨터를 명령에 따라 데이터를 처리하는 전자 장치로 보고, 시스템 구성 요소와 역사적 흐름을 연결한다.",
            "tags": ["컴퓨터 정의", "시스템 구성", "CPU 아키텍처"],
            "objectives": [
                "컴퓨터를 단순한 데스크톱이 아니라 다양한 형태의 programmable 전자 장치로 이해한다.",
                "CPU, 메모리, 입출력 장치가 컴퓨터 시스템의 기본 구성 요소임을 설명한다.",
                "x86, x64, ARM, 폰 노이만 구조 같은 단어가 왜 실무와 보안 학습에서 중요한지 이해한다.",
            ],
            "sections": [
                {
                    "heading": "컴퓨터란 무엇인가",
                    "body": """
                    """ + ca02_title + """
                    <p>강의는 “컴퓨터라고 하면 무엇이 떠오르는가”라는 질문에서 시작한다. 어떤 사람은 책상 위의 검은 데스크톱 본체를 떠올리고, 어떤 사람은 서버실의 큰 장비를 떠올리고, 어떤 사람은 손 안의 스마트폰을 떠올린다. 강사는 이 모든 것이 컴퓨터라는 이름으로 묶일 수 있지만, 정확히 무엇을 기준으로 컴퓨터라고 부르는지 먼저 잡아야 한다고 설명한다.</p>
                    """ + ca02_definition_wiki + """
                    <p>일반적인 정의를 찾으면 컴퓨터는 전산기, 전자적 기계 장치, 프로그램을 사용해 정보를 입력·처리·출력하는 장치로 설명된다. 하지만 이런 설명만으로는 처음 듣는 학생에게 잘 와닿지 않을 수 있다. 그래서 강사는 더 짧게, 컴퓨터를 <strong>데이터를 처리하고, 명령에 따라 작업을 수행하는 전자 장치</strong>로 설명한다.</p>
                    """ + ca02_definition_chatgpt + """
                    <p>여기서 중요한 키워드는 세 가지다. 첫째, 데이터를 처리한다. 둘째, 명령에 따라 작업한다. 셋째, 전자 장치다. 여기에 조금 더 정확히 말하면 <strong>프로그래밍 가능성</strong>, 즉 여러 프로그램이나 명령을 바꿔 가며 수행할 수 있다는 점이 들어가야 한다.</p>
                    <p>아날로그 시계나 단순 디지털 시계를 떠올리면 이 정의의 경계가 보인다. 시계도 어떤 의미에서는 시간이라는 데이터를 처리하고 표시하지만, 일반적으로 우리가 말하는 컴퓨터처럼 여러 프로그램을 바꿔 실행하는 장치라고 보기는 어렵다. 그래서 강의는 “명령에 따라 동작하는 전자 장치”라는 설명에 더해, 실제 컴퓨터는 <strong>다른 프로그램도 실행할 수 있는 범용성</strong>을 가져야 한다는 감각을 잡게 한다.</p>
                    """,
                },
                {
                    "heading": "컴퓨터의 종류",
                    "body": """
                    <p>컴퓨터는 데스크톱 하나만 의미하지 않는다. 슈퍼컴퓨터, 메인프레임, 미니컴퓨터 또는 서버, 데스크톱, 노트북, 태블릿, 스마트폰, 임베디드 시스템까지 모두 컴퓨터의 범주에서 생각할 수 있다. 강의에서는 앞으로 설명할 기본 구조를 데스크톱 컴퓨터를 기준으로 잡겠다고 말한다.</p>
                    """ + ca02_types + """
                    <table>
                      <thead><tr><th>종류</th><th>강의에서의 의미</th></tr></thead>
                      <tbody>
                        <tr><td>슈퍼컴퓨터</td><td>매우 큰 계산 능력을 가진 특수 목적의 고성능 컴퓨터다.</td></tr>
                        <tr><td>메인프레임</td><td>대규모 조직에서 많은 작업을 안정적으로 처리하는 큰 시스템으로 이해하면 된다.</td></tr>
                        <tr><td>서버·미니컴퓨터</td><td>여러 사용자의 요청을 처리하거나 특정 서비스를 제공하는 컴퓨터다.</td></tr>
                        <tr><td>데스크톱·노트북</td><td>일반 사용자가 가장 쉽게 떠올리는 개인용 컴퓨터다.</td></tr>
                        <tr><td>태블릿·스마트폰</td><td>휴대성을 중심으로 발전한 컴퓨터다. 스마트폰도 컴퓨터의 한 종류로 볼 수 있다.</td></tr>
                        <tr><td>임베디드 시스템</td><td>POS 장비나 전용 보안 제품처럼 특정 기능에 맞춰 최적화된 컴퓨터다.</td></tr>
                      </tbody>
                    </table>
                    """ + ca02_embedded + """
                    <p>스마트폰은 극단적으로 휴대성을 강조한 컴퓨터이고, 임베디드 시스템은 특정 목적에 맞춰 설계된 컴퓨터다. 멘토는 본인이 개발하는 보안 제품도 이런 특수 목적 시스템에 최적화되는 경우가 있다고 말한다. 이 말은 컴퓨터 구조가 단지 PC 조립 지식이 아니라, 제품이 어떤 환경에서 어떤 제약을 가지고 동작하는지 이해하는 데도 연결된다는 뜻이다.</p>
                    """,
                },
                {
                    "heading": "컴퓨터 시스템의 기본 구성",
                    "body": """
                    <p>데스크톱을 기준으로 보면 컴퓨터 시스템은 크게 <strong>CPU</strong>, <strong>메모리</strong>, <strong>입출력 장치</strong>로 나눌 수 있다. CPU는 명령어를 해석하고 실행한다. 메모리는 데이터와 명령어, 실행 중간 결과를 저장한다. 입출력 장치는 사용자가 명령을 입력하거나 결과를 확인하게 해 준다.</p>
                    """ + ca02_components + """
                    <div class="diagram three-col">
                      <div><span class="node-title">CPU</span><p>명령어를 해석하고 실행하는 중심 장치</p></div>
                      <div><span class="node-title">메모리</span><p>명령어, 데이터, 실행 결과를 저장하는 공간</p></div>
                      <div><span class="node-title">입출력 장치</span><p>키보드, 마우스, 모니터, USB처럼 외부와 연결되는 장치</p></div>
                    </div>
                    """ + ca02_danawa + """
                    <p>멘토는 실제 부품을 익히는 방법으로 PC 견적 사이트를 둘러보는 것을 추천한다. CPU, 메인보드, RAM, 저장 장치 같은 항목을 직접 보다 보면 컴퓨터 구조의 단어가 현실의 부품과 연결된다. 조립 컴퓨터 견적을 한 번 짜 보면 “어떤 부품이 있어야 컴퓨터가 되는가”가 더 쉽게 보인다. 다만 그렇게 공부하다 보면 주변 사람이 컴퓨터 견적을 부탁할 수 있다는 농담도 덧붙인다.</p>
                    """,
                },
                {
                    "heading": "컴퓨터 역사 흐름을 보는 이유",
                    "body": """
                    <p>강의는 계산 장치의 역사 전체를 자세히 외우라고 하지는 않는다. 중요한 것은 역사 속에서 지금도 쓰이는 단어들이 생겼다는 점이다. 계산의 필요에서 출발해 기계식 장치, 전자식 장치, 컴퓨터의 등장, 웹의 발전, 스마트폰과 모바일 혁명으로 이어지는 큰 흐름만 잡으면 된다.</p>
                    """ + ca02_arch_keywords + """
                    <p>특히 강사는 역사 설명이 필요한 이유를 다운로드 화면과 연결한다. <code>x86</code>, <code>x64</code>, <code>ARM64</code> 같은 선택지는 단순한 파일 이름이 아니라 CPU 아키텍처와 프로그램 호환성을 의미한다. CPU마다 해석할 수 있는 명령어 체계가 다르기 때문에, 프로그램도 실행할 대상 아키텍처에 맞게 빌드되어야 한다.</p>
                    """ + ca02_vscode_arch + """
                    <p>2차 세계대전 시기의 암호 해독과 자동 계산 요구가 컴퓨터 발전을 크게 밀어붙였다는 이야기도 나온다. 튜링 머신 계열의 개념을 비롯해 ENIAC, 폰 노이만 구조, 트랜지스터, 마이크로프로세서, RISC, 멀티코어, ARM, Apple M1 같은 흐름으로 이어진다. 강사는 연도를 외우는 것보다 이런 이름들이 어떤 맥락에서 이어졌는지 보는 것이 중요하다고 말한다.</p>
                    """ + ca02_history + """
                    <div class="timeline compact">
                      <div><strong>계산 필요</strong><p>사람의 계산을 기계가 대신하게 하려는 시도</p></div>
                      <div><strong>전자식 컴퓨터</strong><p>전쟁과 암호, 과학 계산 요구로 발전</p></div>
                      <div><strong>폰 노이만 구조</strong><p>프로그램과 데이터를 같은 메모리에 저장하는 현대 컴퓨터의 기본 구조</p></div>
                      <div><strong>트랜지스터</strong><p>0과 1을 표현하는 스위치로 디지털 회로의 기반이 됨</p></div>
                      <div><strong>마이크로프로세서와 멀티코어</strong><p>CPU가 작고 강력해지고, 여러 코어를 한 칩에 담게 됨</p></div>
                    </div>
                    """,
                },
                {
                    "heading": "폰 노이만 구조와 트랜지스터",
                    "body": """
                    <p>폰 노이만 구조는 이 강의에서 반드시 기억해야 할 이름이다. 현대 컴퓨터 구조의 바탕이며, 데이터와 프로그램을 같은 메모리에 저장한다는 생각이 핵심이다. 멘토는 폰 노이만을 “컴퓨터의 아버지”로 기억해도 좋다고 말한다.</p>
                    <p>트랜지스터는 0과 1을 표현하는 스위치처럼 이해하면 된다. 전기가 통하면 1, 통하지 않으면 0처럼 생각할 수 있고, 이 0과 1의 조합으로 디지털 회로와 논리 회로가 만들어진다. 뒤 강의의 데이터 표현, CPU 명령, 메모리 저장 방식도 결국 이 0과 1 위에 올라간다.</p>
                    <p>마이크로프로세서는 CPU를 하나의 칩으로 집적하는 흐름이고, RISC와 CISC는 명령어 집합을 설계하는 철학의 차이를 가리킨다. 멀티코어는 한 칩 안에 여러 코어를 넣어 동시에 더 많은 일을 처리하려는 발전 방향이다. ARM과 Apple Silicon은 저전력·고효율 아키텍처 흐름을 이해할 때 계속 등장한다.</p>
                    """,
                },
                {
                    "heading": "x86, x64, ARM을 알아야 하는 이유",
                    "body": """
                    <p>프로그램을 다운로드할 때 x86, x64, ARM64 같은 선택지가 보이는 이유는 CPU 아키텍처가 다르기 때문이다. CPU마다 해석할 수 있는 명령어 체계가 다르므로, 같은 프로그램이라도 어떤 CPU에서 실행할 것인지에 따라 빌드가 달라질 수 있다.</p>
                    <ul>
                      <li><strong>x86</strong>은 Intel 8086 계열에서 출발한 이름이다. 실무에서는 32비트 프로그램을 가리키는 말로 자주 보인다.</li>
                      <li><strong>x64</strong>는 64비트 환경을 가리키는 말로 자주 사용된다. 현재 일반 PC에서는 64비트가 흔하다.</li>
                      <li><strong>ARM</strong>은 스마트폰과 저전력 장치에서 강하게 성장했고, Apple M1 같은 Apple Silicon도 ARM 계열 흐름으로 이해할 수 있다.</li>
                    </ul>
                    <p>멘토는 Apple M1을 예로 들며 전력 효율, 배터리, 성능 측면에서 인상적이었다고 말한다. 같은 전기를 주었을 때 더 많은 일을 할 수 있으면 노트북 배터리가 오래가고, 발열과 성능 면에서도 장점이 생긴다. 또 예전 Intel Mac에서는 Boot Camp로 Windows를 설치하기 쉬웠지만, Apple Silicon으로 넘어오면서 CPU 아키텍처 차이 때문에 호환성 문제가 생겼고, Rosetta 같은 번역 계층이 중요해졌다고 설명한다.</p>
                    """,
                },
                {
                    "heading": "보안 학습에서 32비트 환경을 만나는 이유",
                    "body": """
                    <p>현대 시스템은 대부분 64비트지만, 보안 학습에서는 x86 또는 32비트 환경을 자주 만난다. 오래된 운영체제나 가상 머신, 디버깅 실습, 리버싱 입문 자료가 32비트 기준으로 만들어진 경우가 많기 때문이다.</p>
                    """ + ca02_x86_chip + """
                    <p>멘토는 최신 기술이 많은 것을 추상화하고 편하게 만들어 주지만, 처음 원리를 배울 때는 예전 32비트 환경이 더 단순해서 학습하기 좋은 면이 있다고 설명한다. 따라서 x86이라는 단어를 보면 단순히 “옛날 것”이라고 넘기지 말고, 보안 실습에서 자주 쓰이는 학습 환경으로 이해하면 된다.</p>
                    <p>이 강의의 결론은 컴퓨터 시스템 개요를 “정의, 형태, 구성요소, 역사, 아키텍처 이름”으로 연결해 기억하는 것이다. 나중에 다른 수업에서 VM 구성, x86 실습, ARM64 다운로드, CPU 명령어, 메모리 구조가 나오면 이 강의의 큰 그림을 다시 떠올리면 된다.</p>
                    """,
                },
            ],
            "checks": [
                "컴퓨터의 정의에서 데이터 처리, 명령 수행, 전자 장치, 프로그래밍 가능성을 설명할 수 있는가?",
                "CPU, 메모리, 입출력 장치의 역할을 구분할 수 있는가?",
                "폰 노이만 구조가 왜 현대 컴퓨터 구조의 핵심인지 말할 수 있는가?",
                "x86, x64, ARM64 선택지가 프로그램 다운로드 페이지에 나오는 이유를 설명할 수 있는가?",
                "보안 실습에서 32비트 환경을 자주 쓰는 이유를 이해했는가?",
            ],
        },
        {
            "id": "1-3",
            "title": "데이터 표현",
            "subtitle": "컴퓨터가 0과 1로 숫자, 문자, 정수, 실수, 프로그램의 상태를 표현하는 방식을 이해한다.",
            "tags": ["비트와 바이트", "정수 표현", "오버플로우"],
            "objectives": [
                "비트, 바이트, 단위 체계가 실제 파일 크기와 메모리 감각에 어떻게 연결되는지 이해한다.",
                "정수와 실수가 같은 비트 공간을 서로 다른 약속으로 해석한다는 점을 설명한다.",
                "오버플로우가 왜 발생하고 보안·개발에서 왜 중요한지 이해한다.",
            ],
            "sections": [
                {
                    "heading": "0과 1에서 시작하는 데이터",
                    "body": """
                    """ + ca03_title + """
                    <p>컴퓨터의 데이터 표현은 결국 0과 1에서 시작한다. 트랜지스터는 전기 신호를 켜고 끄는 스위치처럼 동작한다. 강사는 트랜지스터를 “전기 신호를 넣었다 뺐다 해 주는 on/off 장치”로 설명하고, 켜져 있으면 1, 꺼져 있으면 0으로 해석한다고 말한다.</p>
                    """ + ca03_transistor_bit + """
                    <p>이 하나의 0 또는 1을 <strong>비트(bit)</strong>라고 한다. 메모리나 저장 공간 어딘가에 0과 1의 덩어리가 놓이면, 컴퓨터는 그 덩어리를 숫자, 문자, 명령어, 주소, 상태값 등으로 해석한다. 중요한 것은 0과 1 자체가 처음부터 “숫자”나 “명령”으로 태어나는 것이 아니라, 사람이 정한 약속과 프로그램의 해석 방식에 따라 의미가 달라진다는 점이다.</p>
                    <p>0과 1이 중요한 이유는 논리 연산으로 이어지기 때문이다. AND, OR, NOT 같은 논리 연산은 참과 거짓을 다루고, 컴퓨터 회로는 이런 논리 연산을 조합해 복잡한 작업을 수행한다. 강의에서는 철학이나 논리학의 명제처럼, 참과 거짓으로 정리할 수 있는 문제는 컴퓨터가 처리할 수 있는 문제로 바뀔 수 있다고 설명한다.</p>
                    <div class="diagram three-col">
                      <div><span class="node-title">트랜지스터</span><p>전기 신호의 켜짐과 꺼짐</p></div>
                      <div><span class="node-title">비트</span><p>0 또는 1 하나의 정보</p></div>
                      <div><span class="node-title">논리 연산</span><p>AND, OR, NOT으로 조건을 처리</p></div>
                    </div>
                    """,
                },
                {
                    "heading": "논리와 AI에 대한 강의의 관점",
                    "body": """
                    <p>멘토는 컴퓨터가 명확한 논리 문제를 잘 풀지만, 인간의 모든 문제를 컴퓨터가 해결할 수 있다고 보지는 않는다고 말한다. 만약 어떤 비논리적 문제를 컴퓨터가 풀었다면, 그 문제는 결국 컴퓨터가 다룰 수 있는 논리 문제로 재구성된 것이라고 설명한다.</p>
                    <p>이 관점은 AI 이야기로 이어진다. ChatGPT 같은 도구가 등장했지만 개발자가 사라진다고 겁먹기보다는, AI를 보조자나 동료처럼 활용하는 태도가 필요하다고 말한다. 이 부분은 데이터 표현 강의의 직접 계산 내용은 아니지만, 컴퓨터가 무엇을 할 수 있고 무엇을 하기 어려운지 생각해 보게 하는 사담이다.</p>
                    """,
                },
                {
                    "heading": "비트, 바이트, 저장 단위",
                    "body": """
                    <p>비트가 쌓이면 바이트가 된다. 강의에서는 이유를 깊게 파고들기보다, 우선 <strong>8비트가 모이면 1바이트</strong>라는 약속을 잡고 시작한다. 바이트는 파일 크기, 메모리 크기, 네트워크 데이터 크기를 이야기할 때 가장 자주 만나는 기본 단위다.</p>
                    """ + ca03_byte + """
                    <p>바이트가 커지면 KB, MB, GB, TB, PB, EB, ZB, YB 같은 단위로 올라간다. 시험이나 자격증에서는 KB, MB, GB가 약 1000배씩 커진다고 설명하는 경우가 많지만, 컴퓨터 내부에서는 2의 10승인 1024를 기준으로 계산하는 경우가 많다. 강의에서는 10의 3승과 2의 10승이 비슷하다는 감각을 잡으라고 설명한다.</p>
                    """ + ca03_units + """
                    <table>
                      <thead><tr><th>단위</th><th>대략적인 감각</th><th>강의에서 강조한 포인트</th></tr></thead>
                      <tbody>
                        <tr><td>bit</td><td>0 또는 1 하나</td><td>가장 작은 정보 단위</td></tr>
                        <tr><td>Byte</td><td>8 bits</td><td>문자, 숫자, 파일 크기를 이야기할 때 기본 단위</td></tr>
                        <tr><td>KB/MB/GB</td><td>실제 파일 크기에서 자주 보는 단위</td><td>1000배 또는 1024배 감각을 함께 기억</td></tr>
                        <tr><td>TB 이상</td><td>대용량 저장 장치, 서버, 데이터 분야에서 자주 등장</td><td>일상에서는 TB까지 자주 체감</td></tr>
                      </tbody>
                    </table>
                    <p>문자 하나가 항상 1바이트인 것은 아니다. 인코딩에 따라 한 글자가 1바이트일 수도 있고, 2바이트나 3바이트 이상일 수도 있다. 강사는 “몇 천 줄짜리 소스 코드 파일의 크기가 어느 정도일까” 같은 질문도 이런 단위 감각으로 추론할 수 있다고 말한다. 한 줄의 글자 수와 인코딩 크기, 줄 수를 대략 곱하면 파일 크기를 어림할 수 있다.</p>
                    <p>소스 코드 파일은 보통 생각보다 작고, 영상 파일은 훨씬 크다. 실행 파일이나 보안 제품 바이너리도 목적에 따라 크기가 중요하다. 특히 특수 목적 시스템에 들어가는 보안 제품은 가볍게 만들어야 하므로, 데이터 크기와 표현 단위를 아는 것이 실무 감각과도 연결된다.</p>
                    """,
                },
                {
                    "heading": "이진수와 16진수",
                    "body": """
                    <p>정수는 비트 자리에 2의 거듭제곱 값을 배치해 표현한다. 가장 오른쪽 비트는 2의 0승, 그 다음은 2의 1승, 그 다음은 2의 2승처럼 올라간다. 해당 자리의 비트가 1이면 그 값을 더하고, 0이면 더하지 않는다.</p>
                    """ + ca03_binary_85 + """
                    <p>강의 화면의 예시는 <code>01010101</code>이다. 켜진 자리만 더하면 <code>2^6 + 2^4 + 2^2 + 2^0</code>이고, 이것은 <code>64 + 16 + 4 + 1 = 85</code>가 된다. 이처럼 0과 1의 나열은 각 자리의 약속을 알면 10진수 값으로 바꿀 수 있다.</p>
                    <p>하지만 이진수는 길어지면 사람이 읽기 어렵다. 그래서 컴퓨터 구조, 디버거, 리버싱, 메모리 분석에서는 <strong>16진수</strong>를 자주 사용한다. 16진수 한 자리는 4비트를 깔끔하게 표현할 수 있으므로 긴 이진수를 훨씬 짧게 보여 준다.</p>
                    <table>
                      <thead><tr><th>표현</th><th>예</th><th>의미</th></tr></thead>
                      <tbody>
                        <tr><td>2진수</td><td><code>0101 0101</code></td><td>비트 단위로 정확하지만 길다.</td></tr>
                        <tr><td>10진수</td><td><code>85</code></td><td>사람이 일상적으로 읽기 쉽다.</td></tr>
                        <tr><td>16진수</td><td><code>0x55</code></td><td>비트 묶음을 짧게 표현해 디버깅에 편하다.</td></tr>
                      </tbody>
                    </table>
                    """,
                },
                {
                    "heading": "정수, 부호, 2의 보수",
                    "body": """
                    <p>C 언어의 <code>char</code>는 보통 1바이트 크기다. 그런데 1바이트는 8비트이므로 단순히 양수만 표현하면 0부터 255까지 표현할 수 있다. 하지만 <code>signed char</code>처럼 부호가 있는 자료형은 음수도 표현해야 하므로, 한 비트를 부호를 나타내는 용도로 사용한다.</p>
                    """ + ca03_char_type + """
                    <p>강의는 여기서 “왜 -128부터 127까지인가”, “왜 128이 아닌가”라는 질문을 던진다. 핵심은 같은 비트라도 어떤 약속으로 해석하느냐에 따라 의미가 달라진다는 점이다. 음수 표현에서는 2의 보수 개념이 등장한다. 간단히 말하면 비트를 뒤집고 1을 더하는 방식으로 음수를 표현한다.</p>
                    <p>맨 앞자리를 부호 비트(sign bit)로 쓰면, 이 비트가 0일 때는 양수, 1일 때는 음수로 해석할 수 있다. 반대로 <code>unsigned</code> 자료형처럼 부호 비트를 쓰지 않으면 모든 비트를 양수 크기를 나타내는 데 사용할 수 있다. 그래서 같은 1바이트라도 <code>signed char</code>와 <code>unsigned char</code>의 범위가 달라진다.</p>
                    <table>
                      <thead><tr><th>자료형 감각</th><th>해석 방식</th><th>결과 범위 예시</th></tr></thead>
                      <tbody>
                        <tr><td><code>unsigned char</code></td><td>모든 비트를 양수 크기에 사용</td><td>0부터 255</td></tr>
                        <tr><td><code>signed char</code></td><td>부호와 크기, 2의 보수 규칙으로 해석</td><td>-128부터 127</td></tr>
                      </tbody>
                    </table>
                    <p>중요한 것은 비트 자체가 “숫자”, “부호”, “문자”로 태어나는 것이 아니라는 점이다. 사람이 자료형이라는 약속을 정하고, 컴퓨터와 프로그램이 그 약속대로 같은 비트 묶음을 해석한다. 이 감각은 나중에 메모리 덤프, 바이너리 분석, CTF 문제를 볼 때 계속 필요하다.</p>
                    """,
                },
                {
                    "heading": "고정소수점과 부동소수점",
                    "body": """
                    <p>정수와 실수도 같은 비트 공간을 서로 다르게 해석하는 대표적인 예다. 고정소수점은 정수부와 소수부의 위치를 고정해 두고 값을 표현한다. 소수부는 2의 -1승, 2의 -2승처럼 작은 자리로 내려간다.</p>
                    """ + ca03_fixed_point + """
                    <p>부동소수점은 소수점 위치가 움직인다. 지수부가 소수점의 위치를 정하고, 가수부 또는 유효숫자 부분이 실제 중요한 숫자들을 담는다. 그래서 큰 수와 작은 수를 비교적 넓은 범위로 표현할 수 있지만, 모든 실수를 정확히 표현하는 것은 아니다.</p>
                    """ + ca03_float_range + ca03_float_layout + """
                    <div class="diagram two-col">
                      <div><span class="node-title">고정소수점</span><p>정수부와 소수부의 칸을 미리 고정한다.</p></div>
                      <div><span class="node-title">부동소수점</span><p>지수와 가수로 소수점 위치를 유연하게 표현한다.</p></div>
                    </div>
                    <p>강사는 수학적 세부 공식까지 모두 외우라고 하지는 않는다. 대신 “이 비트 칸들을 어떻게 나누고 해석하느냐에 따라 표현 범위가 달라진다”는 점을 기억하라고 말한다. 정수만 필요한 값인지, 실수가 필요한 값인지, 음수가 필요한지, 어느 정도 범위까지 필요한지를 생각해야 적절한 자료형을 고를 수 있다.</p>
                    <p>이 설명은 TypeScript 같은 언어의 타입 개념과도 연결된다. JavaScript나 Python처럼 타입을 강하게 드러내지 않는 언어를 먼저 배우면 숫자가 알아서 처리되는 것처럼 보이지만, 실제로는 메모리와 표현 방식의 문제가 뒤에 있다. 타입을 명시하면 값의 범위와 의미를 더 분명히 만들 수 있다.</p>
                    """,
                },
                {
                    "heading": "오버플로우와 언더플로우",
                    "body": """
                    <p>오버플로우는 자료형이 표현할 수 있는 범위를 넘어섰을 때 발생한다. 부호 없는 8비트가 모두 켜져 있으면 값은 255다. 이 상태에서 1을 더하면 8비트 공간 안에는 256을 담을 칸이 없으므로 값이 돌아가거나, 자료형에 따라 전혀 다른 값처럼 보일 수 있다.</p>
                    """ + ca03_overflow_255 + """
                    <p>강사는 다섯 자리 숫자 칸에 <code>99999</code>가 들어 있는데 1을 더하는 비유를 든다. 자릿수를 더 만들 수 없다면 고정된 칸 안에서는 다시 0처럼 보일 수 있다. 부호 있는 자료형에서는 부호 비트 해석 때문에 음수로 바뀌는 것처럼 보일 수도 있다.</p>
                    """ + ca03_overflow_prompt + """
                    """ + code_block("""
                    #include <stdio.h>
                    #include <limits.h>

                    int main(void) {
                        int value = INT_MAX;
                        printf("%d\\n", value);
                        printf("%d\\n", value + 1);  // 표현 범위를 넘어서는 예
                        return 0;
                    }
                    """) + """
                    <p>강의에서는 C로 최대값에 1을 더해 보거나, <code>char</code> 변수를 반복문에서 증가시켜 보며 직접 확인해 보라고 권한다. 오버플로우는 단순한 숫자 실수가 아니라 보안 취약점과도 연결될 수 있기 때문에 중요하다.</p>
                    """ + ca03_youtube_overflow + """
                    <p>멘토는 YouTube의 “강남스타일” 조회 수가 32비트 정수 범위를 넘어 문제가 생겼다는 유명한 사례도 언급한다. 조회 수처럼 계속 증가하는 값을 너무 작은 자료형에 담으면 언젠가 최대값을 넘어선다. 그 결과 마이너스처럼 표시되거나 잘못된 값이 될 수 있어, YouTube는 더 큰 자료형으로 조회 수 표현 방식을 바꾸었다고 설명한다.</p>
                    <p>정확한 숫자를 모두 외울 필요는 없지만, 32비트 signed int의 최대값이 약 21억, 즉 <code>2,147,483,647</code>이라는 감각은 개발과 CTF, 보안 문제에서 자주 도움이 된다. 언더플로우라는 표현도 나오지만, 이 강의에서는 우선 “표현 가능한 범위를 넘어섰다”는 오버플로우 개념을 중심으로 이해하면 된다.</p>
                    <p>정리하면 데이터 표현은 트랜지스터의 0과 1에서 시작해 bit, byte, KB/MB/GB 단위로 커지고, 자료형이라는 약속을 통해 정수·실수·부호·소수점·범위를 해석하는 과정이다. 이 약속을 잘못 이해하면 프로그램 버그가 되고, 범위를 넘어서면 오버플로우처럼 보안 문제로도 이어질 수 있다.</p>
                    """,
                },
            ],
            "checks": [
                "8비트가 1바이트라는 점과 KB, MB, GB가 커지는 감각을 설명할 수 있는가?",
                "왜 2진수보다 16진수가 디버깅에서 편한지 말할 수 있는가?",
                "signed char와 unsigned char의 범위가 다른 이유를 설명할 수 있는가?",
                "고정소수점과 부동소수점의 차이를 큰 그림으로 설명할 수 있는가?",
                "오버플로우가 왜 단순 계산 오류를 넘어 보안 문제로 이어질 수 있는지 이해했는가?",
            ],
        },
        {
            "id": "1-4",
            "title": "중앙처리장치(CPU)",
            "transcript_title": "중앙처리장치 CPU",
            "subtitle": "소스 코드가 기계어가 되고, CPU가 명령을 가져와 해석하고 실행하는 과정을 중심으로 CPU를 이해한다.",
            "tags": ["CPU", "명령어 사이클", "CISC/RISC"],
            "objectives": [
                "소스 코드, 어셈블리어, 기계어의 관계를 설명한다.",
                "CPU의 Fetch, Decode, Execute 흐름과 확장된 실행 단계를 이해한다.",
                "CISC, RISC, 레지스터, ALU, 멀티코어 개념이 프로그램 실행과 어떻게 연결되는지 파악한다.",
            ],
            "sections": [
                {
                    "heading": "왜 CPU를 프로그램 실행 과정으로 배우는가",
                    "body": """
                    """ + ca04_title + """
                    <p>멘토는 CPU를 컴퓨터의 “꽃”처럼 표현한다. CPU를 이해하려면 먼저 프로그램이 실행되는 과정을 봐야 한다. 이 흐름은 컴퓨터 구조뿐 아니라 리버스 엔지니어링, 어셈블리어, 시스템 해킹, 운영체제 수업에서 계속 다시 나온다.</p>
                    <p>강사는 C 언어를 처음 배울 때 <code>printf</code>로 화면에 문구만 찍히는 것이 왜 중요한지 잘 와닿지 않았다고 말한다. 그런데 내가 작성한 코드가 실제로 어떤 명령어가 되고 CPU에서 어떻게 실행되는지 알게 되면, C가 왜 컴퓨터 공부의 기초로 자주 등장하는지 이해하기 쉬워진다.</p>
                    <p>리버싱은 이 흐름을 거꾸로 따라가는 작업이다. 완성된 바이너리를 보고 기계어를 해석하고, 기계어를 어셈블리어로 바꾸고, 어셈블리어를 보며 원래 프로그램의 의도를 추정한다. 그래서 CPU 강의의 출발점은 부품 이름 암기가 아니라 <strong>프로그램 실행 과정</strong>이다.</p>
                    """,
                },
                {
                    "heading": "소스 코드에서 기계어까지",
                    "body": """
                    <p>사람이 읽기 쉬운 C 소스 코드는 컴파일 과정을 거치며 어셈블리어에 가까운 형태를 지나고, 최종적으로 CPU가 해석할 수 있는 기계어 또는 바이너리가 된다. 강의에서는 컴파일러, 링커 같은 세부 단계가 있지만 지금은 큰 흐름을 잡는 것이 중요하다고 설명한다.</p>
                    """ + ca04_execution_flow + """
                    <div class="diagram">
                      <div><span class="node-title">Source Code</span><p>C처럼 사람이 읽기 쉬운 코드</p></div>
                      <span class="arrow">→</span>
                      <div><span class="node-title">Assembly</span><p>CPU 명령어에 가까운 사람이 읽을 수 있는 표현</p></div>
                      <span class="arrow">→</span>
                      <div><span class="node-title">Machine Code</span><p>CPU가 해석하는 0과 1의 명령</p></div>
                    </div>
                    <p>위쪽에 있을수록 사람에게 가까운 high-level language이고, 아래쪽에 있을수록 기계에 가까운 low-level language다. 강의는 이 흐름을 C 언어 예시로 설명한다. 가장 단순한 <code>Hello</code> 출력 프로그램도 CPU가 바로 읽는 형태가 아니며, 실행 전에는 여러 단계의 변환을 거친다.</p>
                    """ + ca04_hello_code + """
                    """ + code_block("""
                    #include <stdio.h>

                    int main()
                    {
                        printf("HELLO \\n");
                        return 0;
                    }
                    """) + """
                    <p>이 짧은 코드가 컴파일되면 화면처럼 어셈블리어 형태가 나타난다. 처음 보면 난해하지만, 이 어셈블리어는 CPU 명령어 집합에 훨씬 가까운 표현이다.</p>
                    """ + ca04_assembly_listing + """
                    <p>예를 들어 <code>mov</code> 명령은 source 값을 destination으로 옮기는 명령으로 이해하면 된다. destination과 source에는 레지스터, 메모리 주소, 상수 등이 올 수 있다.</p>
                    """ + ca04_mov_instruction + """
                    """ + code_block("""
                    mov destination, source  ; source의 데이터를 destination으로 복사
                    mov w8, #0               ; ARM 계열 예시: w8 레지스터에 상수 0을 넣는 형태
                    mov eax, 10              ; x86 계열 예시: eax 레지스터에 10을 넣는다
                    """, "asm") + """
                    <p>강사는 이 명령을 꼭 기억하라고 말한다. CPU는 기계어를 읽고, 그 기계어에 대응하는 명령어를 찾고, 그 명령어가 요구하는 일을 한다. <code>mov</code>라면 source 값을 읽어 destination에 복사하는 식이다.</p>
                    """ + ca04_machine_code + """
                    <p>기계어는 사람이 직접 읽기 어려워서 보통 16진수 형태로 확인한다. 이 16진수 기계어가 CPU 아키텍처의 명령어 표에 따라 어셈블리 명령으로 해석된다. 같은 바이트라도 어떤 CPU 아키텍처의 명령어 집합으로 해석하느냐에 따라 의미가 달라질 수 있다.</p>
                    """,
                },
                {
                    "heading": "명령어 사이클: Fetch, Decode, Execute",
                    "body": """
                    <p>CPU가 하는 가장 기본적인 일은 <strong>Fetch</strong>, <strong>Decode</strong>, <strong>Execute</strong>의 반복이다. Fetch는 명령어를 가져오는 단계, Decode는 가져온 명령어가 무엇인지 해석하는 단계, Execute는 실제로 명령을 수행하는 단계다.</p>
                    """ + ca04_fde + """
                    <div class="timeline compact">
                      <div><strong>Fetch</strong><p>메모리에서 다음 명령어를 가져온다.</p></div>
                      <div><strong>Decode</strong><p>명령어가 어떤 동작을 의미하는지 해석한다.</p></div>
                      <div><strong>Execute</strong><p>해석한 명령을 실제로 실행한다.</p></div>
                    </div>
                    <p>멘토는 CPU가 이 점에서 “바보이면서 천재적”이라고 표현한다. CPU가 할 수 있는 일은 정해진 명령을 가져오고 해석하고 실행하는 것뿐이지만, 그것을 엄청나게 빠르게 반복하기 때문이다. 그래서 컴퓨터는 복잡한 일을 하는 것처럼 보이지만, 바닥에서는 이 단순한 사이클이 엄청난 속도로 반복되고 있다.</p>
                    <p>GHz 같은 클럭 수치는 초당 얼마나 많은 사이클을 처리할 수 있는지와 연결된다. 물론 현대 CPU 성능은 클럭만으로 결정되지 않지만, “1초에 이 명령어 사이클이 얼마나 많이 도는가”라는 감각을 잡는 데는 도움이 된다.</p>
                    """,
                },
                {
                    "heading": "확장된 CPU 실행 단계",
                    "body": """
                    <p>기본 세 단계만으로 설명하기 부족할 때는 실행 단계를 더 나눠서 본다. 강의에서는 Fetch, Decode, Execute에 더해 <strong>Memory Access</strong>와 <strong>Write Back</strong>을 언급한다. 예를 들어 <code>mov</code> 명령 하나를 수행하려 해도 source 값을 읽고, destination 위치를 확인하고, 결과를 다시 저장해야 할 수 있다.</p>
                    """ + ca04_extended_cycle + """
                    <div class="timeline">
                      <div><strong>Fetch</strong><p>명령어를 가져온다.</p></div>
                      <div><strong>Decode</strong><p>명령어와 피연산자를 해석한다.</p></div>
                      <div><strong>Execute</strong><p>연산을 수행한다.</p></div>
                      <div><strong>Memory Access</strong><p>필요하면 메모리를 읽거나 쓴다.</p></div>
                      <div><strong>Write Back</strong><p>결과를 레지스터나 메모리에 반영한다.</p></div>
                    </div>
                    <p>Memory Access는 명령 실행 중 필요한 값이 메모리나 레지스터 어디에 있는지 읽는 과정이다. Write Back은 연산 결과를 다시 레지스터나 메모리에 반영하는 과정이다. 즉 CPU는 단순히 계산만 하는 것이 아니라, 필요한 값을 가져오고 결과를 저장하는 흐름까지 계속 반복한다.</p>
                    <p>문제는 CPU가 매우 빠른 데 비해 메모리 접근은 상대적으로 느리다는 점이다. 강사는 프로그램 실행 중 시간이 많이 걸리는 지점으로 메모리 접근을 언급하고, 뒤에서 배우는 메모리 계층 구조와 캐시가 이 병목을 줄이기 위해 중요해진다고 연결한다.</p>
                    """,
                },
                {
                    "heading": "CPU 성능을 높이는 생각들",
                    "body": """
                    <p>CPU는 단순히 클럭만 높이는 방향으로 발전하지 않는다. 강의에서는 파이프라이닝, 분기 예측, 명령어 수준 병렬성 같은 개념을 언급한다. 지금 단계에서 세부 구현을 외울 필요는 없지만, CPU가 놀지 않게 만들고 다음에 필요한 작업을 미리 준비하려는 최적화라고 이해하면 된다.</p>
                    """ + ca04_optimizations + """
                    <ul>
                      <li><strong>파이프라이닝</strong>: 한 명령의 모든 단계가 끝날 때까지 기다리지 않고, 서로 다른 명령의 다른 단계를 겹쳐 처리한다.</li>
                      <li><strong>분기 예측</strong>: 반복문이나 조건문에서 다음에 어디로 갈지 예측해 미리 준비한다.</li>
                      <li><strong>명령어 수준 병렬성</strong>: 서로 영향을 주지 않는 명령들을 가능한 한 동시에 처리하려는 방향이다.</li>
                    </ul>
                    <p>파이프라이닝은 한 명령의 Fetch, Decode, Execute, Memory Access, Write Back을 모두 끝낸 뒤 다음 명령을 시작하는 대신, 서로 다른 명령의 다른 단계를 겹쳐서 처리하려는 생각이다. 분기 예측은 <code>for</code>문처럼 다음 흐름을 예상할 수 있는 경우에 CPU가 다음에 갈 방향을 미리 준비하는 방식으로 이해하면 된다.</p>
                    """ + ca04_execution_diagram + """
                    <p>그림처럼 메모리에 명령어가 쌓여 있고, CPU는 그 명령을 버스라는 연결 통로를 통해 가져와 해석하고 실행한다. 필요한 데이터도 가져오고, 연산 결과도 다시 저장한다. 이 반복이 빨라야 프로그램이 빠르게 실행된다.</p>
                    <p>멘토는 웹 개발이나 앱 개발을 하더라도 성능 문제가 생기면 결국 메모리 접근, CPU 작업, 입출력 병목을 생각하게 된다고 말한다. 그래서 컴퓨터 구조 지식은 특정 분야에만 갇힌 지식이 아니다.</p>
                    """,
                },
                {
                    "heading": "리버싱과 보안 관점",
                    "body": """
                    <p>프로그램은 실행되기 위해 반드시 CPU가 이해할 수 있는 형태의 명령을 남긴다. 그래서 완성된 프로그램을 분석해 어떤 명령어가 있는지 확인하고, 그 의미를 거꾸로 추적하는 리버스 엔지니어링이 가능하다.</p>
                    <p>강사는 소스 코드 레벨에서 취약점이 보일 때도 있지만, 디버깅하면서 특정 값이 어디에서 잘못 들어갔는지 따라가야 하는 경우가 많다고 설명한다. 이때 어셈블리어와 레지스터, 메모리 상태를 보며 프로그램이 실제로 어떤 명령을 실행했는지 확인하게 된다.</p>
                    <p>방어자는 패킹, 압축, 난독화 같은 기법으로 분석을 어렵게 만들 수 있다. 하지만 프로그램이 실행되어야 하는 이상 CPU가 읽을 수 있는 명령은 어딘가에 남아야 한다. 결국 완전히 읽을 수 없게 만드는 것은 어렵고, 보안의 목표는 “절대 뚫리지 않게 만들기”보다 공격자가 분석하는 데 드는 시간과 비용을 크게 늘리는 것에 가깝다.</p>
                    <div class="callout">리버싱 관점에서 프로그램 실행 과정은 “소스 코드 → 어셈블리어 → 기계어”를 거꾸로 따라가는 지도다.</div>
                    """,
                },
                {
                    "heading": "CISC와 RISC",
                    "body": """
                    <p>CPU 아키텍처마다 명령어 집합이 다르다. 어떤 CPU가 어떤 명령을 이해하는지에 따라 실행 가능한 프로그램이 달라진다. 그래서 프로그램 다운로드 페이지에서 x86, x64, ARM 같은 선택지가 나타난다.</p>
                    """ + ca04_cisc_risc + """
                    <p>강의에서는 Apple Silicon과 Boot Camp 예시도 다시 연결한다. 예전 Intel Mac에서는 Windows가 Intel 계열 CPU를 대상으로 설계되어 있어 Boot Camp로 설치하기 쉬웠지만, M1 이후 Apple Silicon은 ARM 계열 흐름에 가까워 기존 Intel용 프로그램과 호환성 문제가 생겼다. 이를 보완하기 위해 Rosetta처럼 Intel용 프로그램을 Apple Silicon에서 실행할 수 있게 번역해 주는 계층이 필요했다.</p>
                    <table>
                      <thead><tr><th>구분</th><th>강의의 설명</th><th>이해 포인트</th></tr></thead>
                      <tbody>
                        <tr><td>CISC</td><td>Complex Instruction Set Computer</td><td>복잡하고 많은 명령어를 가진다. 하나의 명령이 더 큰 일을 할 수 있어 프로그래머에게 편할 수 있다.</td></tr>
                        <tr><td>RISC</td><td>Reduced Instruction Set Computer</td><td>명령어 수를 줄이고 단순화한다. 한 동작을 더 작은 명령 여러 개로 나눌 수 있지만, 단순하고 효율적인 구현을 노린다.</td></tr>
                      </tbody>
                    </table>
                    <p>비유하자면 CISC는 “나가서 문 열어”처럼 복합적인 일을 한 명령에 담는 방향이고, RISC는 “일어나라, 오른쪽으로 돌아라, 걸어라, 손잡이를 잡아라, 돌려라”처럼 더 작은 단계로 쪼개는 방향에 가깝다. 전통적으로 CISC는 복잡하고 느리며, RISC는 단순하고 빠르다는 식으로 배웠지만, 현대 CPU는 둘 다 매우 발전해서 단순 비교만으로 우열을 말하기 어렵다.</p>
                    <p>ARM은 RISC 흐름에서 강력하게 성장했고, 스마트폰과 저전력 장치, Apple Silicon을 이해할 때 중요한 이름이다. 강사는 과거에는 Intel 계열 CPU가 강하게 자리 잡고 있었지만, ARM과 Apple Silicon이 커지면서 CPU 시장의 축이 넓어졌다고 설명한다.</p>
                    """,
                },
                {
                    "heading": "CPU 내부 구성",
                    "body": """
                    <p>CPU 내부는 크게 제어 장치, ALU, 레지스터, CPU 내부 연결 구조로 생각할 수 있다. 제어 장치는 명령의 흐름을 조정하고, ALU는 산술 및 논리 연산을 수행한다. 레지스터는 CPU 안에 있는 아주 작고 빠른 저장 공간이다.</p>
                    """ + ca04_cpu_structure + """
                    <table>
                      <thead><tr><th>구성 요소</th><th>역할</th></tr></thead>
                      <tbody>
                        <tr><td>Control Unit</td><td>명령어 흐름을 제어하고 필요한 동작을 지시한다.</td></tr>
                        <tr><td>ALU</td><td>덧셈, 뺄셈, 곱셈, 나눗셈, AND, OR, XOR 같은 산술·논리 연산을 처리한다.</td></tr>
                        <tr><td>Registers</td><td>CPU가 바로 사용할 값을 임시로 담는 매우 빠른 저장 공간이다.</td></tr>
                        <tr><td>Interconnection</td><td>CPU 내부 구성 요소가 데이터를 주고받는 연결 통로다.</td></tr>
                      </tbody>
                    </table>
                    <p>Control Unit은 “이번 기계어가 어떤 명령인가”를 해석하고 필요한 흐름을 조정한다. ALU는 Arithmetic and Logic Unit으로, 산술 연산과 논리 연산을 담당한다. 레지스터는 명령 실행 중 값을 잠깐 보관하는 CPU 내부의 빠른 저장 공간이며, Interconnection은 이 구성 요소들이 데이터를 주고받는 내부 통로다.</p>
                    <p>멘토는 ALU를 특히 기억하면 좋다고 말한다. CPU가 엄청난 일을 하는 것처럼 보여도, 내부에서는 비트를 놓고 AND, OR, XOR 같은 논리 연산과 덧셈·뺄셈 같은 산술 연산을 빠르게 반복한다. 곱셈도 2의 거듭제곱과 관련된 경우 비트 시프트로 빠르게 처리할 수 있다는 식의 감각을 언급한다. 결국 CPU 내부 연산은 비트와 논리 연산의 조합으로 이어진다.</p>
                    """,
                },
                {
                    "heading": "싱글코어와 멀티코어",
                    "body": """
                    <p>지금까지의 설명은 하나의 코어가 명령을 실행하는 그림에 가깝다. 하지만 하드웨어가 발전하면서 하나의 프로세서 안에 여러 코어를 넣을 수 있게 되었다. 한 코어를 하나의 CPU처럼 생각하면, 멀티코어 프로세서는 여러 실행 단위를 한 칩 안에 담은 구조로 볼 수 있다.</p>
                    """ + ca04_multicore + """
                    <p>싱글코어는 하나의 실행 단위가 명령어 사이클을 반복하는 구조로 생각하면 된다. 멀티코어는 이런 코어가 여러 개 들어 있어 여러 작업을 나누어 처리할 수 있는 구조다. 프로세서는 보통 이런 코어들과 캐시, 제어 구조 등을 포함한 물리적인 칩 전체를 가리키는 말로 이해하면 된다.</p>
                    <p>마무리에서 멘토는 프로그램 실행 과정이 가장 중요하다고 다시 강조한다. 나중에 운영체제나 시스템 해킹을 배우면 C 소스 코드가 어셈블리어와 기계어로 어떻게 나뉘는지 직접 보게 될 수 있다. 명령어 셋을 주고 사람이 직접 CPU처럼 해석해 보는 과제를 만날 수도 있다.</p>
                    <p>이 과정이 재미있다면 시스템 해커 쪽이 잘 맞을 가능성이 있고, 재미가 없더라도 CPU가 어떤 방식으로 프로그램을 실행하는지 아는 것은 성능 문제와 보안 문제를 이해하는 데 도움이 된다. 이 강의의 핵심은 CPU 구조의 모든 세부 회로를 외우는 것이 아니라, <strong>소스 코드가 기계어가 되고 CPU가 명령어 사이클로 실행한다</strong>는 큰 흐름을 붙잡는 것이다.</p>
                    """,
                },
            ],
            "checks": [
                "C 소스 코드가 어셈블리어와 기계어로 바뀌는 흐름을 설명할 수 있는가?",
                "Fetch, Decode, Execute 세 단계를 정확히 말할 수 있는가?",
                "Memory Access와 Write Back이 왜 필요한지 예시로 설명할 수 있는가?",
                "패킹과 난독화가 분석을 완전히 불가능하게 만드는 것이 아니라 비용을 높이는 기법이라는 점을 이해했는가?",
                "CISC와 RISC의 큰 차이를 설명할 수 있는가?",
                "ALU, 레지스터, 제어 장치의 역할을 구분할 수 있는가?",
            ],
        },
        {
            "id": "1-5",
            "title": "메모리와 시스템",
            "transcript_title": "메모리 메모리와 시스템",
            "subtitle": "메모리를 디버거로 관찰하고, 엔디안, RAM과 ROM, 메모리 계층 구조를 시스템 해킹 관점까지 연결한다.",
            "tags": ["메모리", "디버거", "엔디안"],
            "objectives": [
                "메모리가 명령어, 데이터, 중간 결과를 저장하는 공간임을 이해한다.",
                "디버거와 중단점을 통해 실행 중 메모리와 레지스터 상태를 관찰하는 흐름을 설명한다.",
                "리틀 엔디안, 빅 엔디안, RAM과 ROM, 메모리 계층 구조가 왜 중요한지 파악한다.",
            ],
            "sections": [
                {
                    "heading": "메모리는 무엇을 저장하는가",
                    "body": """
                    """ + ca05_title + """
                    <p>메모리는 실행 중인 프로그램의 명령어, 명령어에 사용되는 데이터, 실행 중간 결과를 저장하는 공간이다. CPU 강의에서 본 것처럼 CPU는 명령어를 가져와 해석하고 실행하는데, 그 명령어와 데이터가 놓이는 주요 공간이 메모리다.</p>
                    """ + ca05_role + """
                    <p>하드웨어적으로 메모리는 트랜지스터와 회로 위에 존재하지만, 프로그래머가 그 물리 구조를 눈으로 직접 확인하기는 어렵다. 대신 소프트웨어 관점에서는 메모리를 볼 수 있다. 이때 쓰는 도구가 <strong>디버거</strong>다. 디버거는 프로그램이 멈춘 특정 시점의 변수 값, 메모리 주소, 레지스터 상태를 보여 준다.</p>
                    <p>멘토는 C 언어가 메모리를 보기 좋은 언어라고 설명한다. 파이썬이나 자바스크립트도 디버거를 붙일 수 있지만, C는 메모리 주소와 값, 포인터, 변수 배치가 비교적 직접적으로 드러난다. 그래서 시스템 해킹, 어셈블리어, 디버깅 입문에서 C가 자주 쓰인다.</p>
                    <p>강사는 managed language와 unmanaged language의 차이도 짧게 언급한다. 메모리를 직접 다루고 관리하는 언어일수록 메모리 주소와 값의 변화를 직접 관찰하기 쉽다. C는 자료도 많고 실습 예제가 많아 메모리와 디버거를 처음 익히기에 적합하다고 설명한다.</p>
                    <div class="callout">핵심은 “메모리는 눈에 보이지 않는 하드웨어”이면서 동시에 “디버거로 관찰할 수 있는 프로그램 실행의 현장”이라는 점이다.</div>
                    """,
                },
                {
                    "heading": "중단점과 쓰레기값",
                    "body": """
                    <p>디버거를 사용할 때 중요한 개념이 <strong>중단점</strong>, 즉 breakpoint다. 프로그램이 실행되는 흐름 중 어디에서 멈출지 지정하면, 디버거는 그 시점의 변수 값, 메모리 값, 레지스터 상태를 보여 준다. 문제가 생긴 지점을 좁혀 가려면 어디서 멈출지 정하는 감각이 중요하다.</p>
                    """ + ca05_vscode_debug + """
                    <p>화면의 예시에서는 VS Code 디버거가 중단점에서 멈춰 있고, 왼쪽 Locals 창에 <code>x</code>, <code>y</code>, <code>z</code> 값이 보인다. 코드에는 <code>int x = 0;</code>이 있지만, 노란 실행 위치가 아직 그 줄을 실행하기 전이므로 <code>x</code>에는 의도하지 않은 값이 표시될 수 있다. 이런 값을 강의에서는 <strong>쓰레기값</strong>이라고 설명한다.</p>
                    """ + code_block("""
                    #include <stdio.h>

                    int main()
                    {
                        int x = 0;
                        int y;
                        char z = 'a';
                        printf("HELLO ! \\n");

                        return 0;
                    }
                    """) + """
                    <p>메모리는 처음부터 모두 0으로 정돈되어 있는 공간이 아니다. 이전에 쓰이던 값이나 의미 없는 데이터가 남아 있을 수 있다. 그래서 변수를 선언한 뒤 사용하기 전에 원하는 값으로 초기화해야 한다. 디버거에서 한 줄씩 실행해 보면, 특정 라인이 지나간 뒤 <code>x</code>가 0으로 바뀌고, <code>z</code>에 <code>'a'</code>가 들어가는 과정을 직접 볼 수 있다.</p>
                    <p>이 경험을 해 보면 “왜 초기화가 필요한가”를 문법 암기가 아니라 메모리 상태로 이해하게 된다. 프로그램이 의도와 다르게 동작할 때도 마찬가지다. 어느 순간 어떤 값이 잘못 들어갔는지 확인하고, 그 값이 왜 바뀌었는지 거꾸로 따라가면 원인을 좁힐 수 있다.</p>
                    """,
                },
                {
                    "heading": "GDB와 메모리 관찰",
                    "body": """
                    <p>멘토는 GDB 같은 디버거를 예로 든다. GDB에서는 명령어 단위로 프로그램을 멈추고, 어셈블리어, 메모리 주소, 레지스터 값을 확인할 수 있다. <code>disassemble</code>은 기계어를 사람이 읽을 수 있는 어셈블리어 형태로 거꾸로 풀어 보여 주는 명령으로 이해하면 된다.</p>
                    """ + ca05_gdb_disassemble + """
                    """ + code_block("""
                    break main       # main 함수에 중단점 설정
                    run              # 프로그램 실행
                    disassemble main # main 함수의 어셈블리 확인
                    info registers   # 레지스터 상태 확인
                    x/16x $esp       # 특정 주소 주변 메모리를 16진수로 확인
                    """, "bash") + """
                    <p>화면의 <code>disassemble main</code> 결과를 보면 왼쪽에는 <code>0x08048374</code> 같은 메모리 주소가 있고, 오른쪽에는 <code>push %ebp</code>, <code>mov %esp,%ebp</code>, <code>sub $0x8,%esp</code> 같은 어셈블리 명령이 있다. “이 주소에는 이런 명령어가 저장되어 있다”는 사실을 디버거가 보여 주는 것이다.</p>
                    <p>어셈블리에서 <code>push ebp</code> 같은 명령이 보일 수 있다. 강의에서는 자세히 설명하지 않지만, 함수 스택 프레임, 함수 실행 과정, 프로로그와 에필로그를 배울 때 매우 중요한 패턴이라고 언급한다. 함수가 시작될 때 기준점을 잡고, 함수가 끝날 때 원래 상태로 돌아가기 위한 규칙이 있기 때문이다.</p>
                    """ + ca05_gdb_memory_formats + """
                    <p>GDB는 같은 메모리 값을 여러 형식으로 보여 줄 수 있다. 화면에서는 <code>x/o</code>로 8진수, <code>x/x</code>로 16진수, <code>x/u</code>로 부호 없는 10진수, <code>x/t</code>로 2진수 표현을 확인한다. 명령어를 모두 외울 필요는 없지만, “디버거는 특정 주소의 값을 원하는 형식으로 표현해 볼 수 있다”는 기능을 기억해 두면 된다.</p>
                    """,
                },
                {
                    "heading": "레지스터와 CPU 가까이 있는 메모리",
                    "body": """
                    <p>레지스터는 CPU 안에 있는 아주 작은 메모리로 생각하면 된다. CPU와 RAM은 속도와 거리 면에서 차이가 크기 때문에, CPU는 매번 멀리 있는 RAM에서 값을 가져오기보다 아주 가까운 레지스터와 캐시를 활용한다.</p>
                    """ + ca05_gdb_registers + """
                    <p>GDB에서 레지스터 값을 보면 CPU가 지금 어떤 값을 들고 명령을 처리하는지 확인할 수 있다. 화면에는 <code>eax</code>, <code>ecx</code>, <code>edx</code>, <code>esp</code>, <code>ebp</code>, <code>eip</code> 같은 레지스터가 보인다. <code>eip</code>는 현재 실행 위치와 연결되고, <code>ebp</code>는 베이스 포인터로 함수 실행 과정에서 기준점 역할을 한다.</p>
                    <p>강사는 이 단계에서 레지스터 각각의 역할을 모두 외우라고 하지는 않는다. 대신 나중에 시스템 해킹, 어셈블리어, 함수 스택 프레임을 배울 때 “CPU 안의 작은 저장 공간을 디버거로 볼 수 있다”는 감각을 다시 떠올리면 된다.</p>
                    """,
                },
                {
                    "heading": "리틀 엔디안과 빅 엔디안",
                    "body": """
                    <p>엔디안은 여러 바이트로 이루어진 데이터를 메모리에 어떤 순서로 저장하고 읽을지에 대한 약속이다. 사람이 왼쪽에서 오른쪽으로 <code>12 34 56 78</code>을 읽는 것과, 컴퓨터가 낮은 주소부터 어떤 바이트를 먼저 저장하는지는 다를 수 있다.</p>
                    """ + ca05_big_endian + """
                    <p><strong>빅 엔디안(Big Endian)</strong>은 큰 자리 바이트, 즉 MSB가 낮은 주소에 먼저 저장되는 방식이다. 예를 들어 <code>0x12345678</code>을 저장하면 낮은 주소부터 <code>0x12</code>, <code>0x34</code>, <code>0x56</code>, <code>0x78</code> 순서로 놓인다. 사람이 숫자를 읽는 방향과 비교적 비슷해 보인다.</p>
                    """ + ca05_little_endian + """
                    <p><strong>리틀 엔디안(Little Endian)</strong>은 작은 자리 바이트, 즉 LSB가 낮은 주소에 먼저 저장되는 방식이다. 같은 <code>0x12345678</code>이 낮은 주소부터 <code>0x78</code>, <code>0x56</code>, <code>0x34</code>, <code>0x12</code>처럼 보일 수 있다. 그래서 디버거에서 값을 보면 사람이 입력한 순서와 반대로 보이는 느낌을 받을 수 있다.</p>
                    <table>
                      <thead><tr><th>방식</th><th>저장 감각</th><th>강의에서의 포인트</th></tr></thead>
                      <tbody>
                        <tr><td>빅 엔디안</td><td>큰 자리 바이트가 낮은 주소에 먼저 저장된다.</td><td>네트워크 통신에서 순서를 맞추는 약속으로 자주 언급된다.</td></tr>
                        <tr><td>리틀 엔디안</td><td>작은 자리 바이트가 낮은 주소에 먼저 저장된다.</td><td>x86 계열 실습에서 자주 마주치며, 디버거에서 값이 거꾸로 보일 수 있다.</td></tr>
                      </tbody>
                    </table>
                    <p>예를 들어 사람이 <code>ABCD</code>라고 입력했다고 해서 메모리에서 항상 같은 순서로 보이는 것은 아니다. 리틀 엔디안 환경에서는 바이트 단위 저장 순서가 사람이 기대한 순서와 다르게 보일 수 있다. C 언어 입출력 프로그램을 만들고 디버거로 실제 메모리를 한 번만 확인해 보면 이 감각이 빠르게 잡힌다고 설명한다.</p>
                    <p>강사는 빅 엔디안이 네트워크에서 자주 쓰인다고 덧붙인다. 서로 다른 컴퓨터가 통신할 때 한쪽은 뒤에서부터 읽고 다른 쪽은 앞에서부터 읽으면 값 해석이 어긋날 수 있으므로, 통신에서는 순서를 맞추는 약속이 필요하다.</p>
                    """,
                },
                {
                    "heading": "엔디안이 시스템 해킹에서 중요한 이유",
                    "body": """
                    <p>시스템 해킹에서는 사용자가 입력한 값이 메모리에 어떤 순서로 저장되는지 알아야 한다. 강의에서는 셸코드라는 단어를 소개한다. 셸코드는 특정 프로그램이나 셸을 실행시키기 위해 만든 기계어 조각이라고 이해하면 된다. 취약한 프로그램의 입력 칸에 특정 바이트열을 넣어 의도한 코드가 실행되게 만드는 흐름을 나중에 배우게 된다.</p>
                    <p>버퍼 오버플로우는 입력값이 버퍼의 크기를 넘어 주변 메모리를 덮어쓰는 현상이다. 단순히 “입력을 많이 넣으면 해킹된다”가 아니라, 어떤 주소의 어떤 데이터가 오염되고, 그 오염된 값을 이용해 실행 흐름을 바꾸는지가 핵심이다. 이때 사람이 읽는 순서와 컴퓨터가 저장하는 순서를 혼동하면 원하는 주소나 값을 제대로 만들 수 없다.</p>
                    <div class="diagram">
                      <div><span class="node-title">입력값</span><p>사용자가 긴 문자열이나 바이트열을 넣는다.</p></div>
                      <span class="arrow">→</span>
                      <div><span class="node-title">메모리 덮어쓰기</span><p>버퍼를 넘어 주변 데이터가 바뀐다.</p></div>
                      <span class="arrow">→</span>
                      <div><span class="node-title">실행 흐름 조작</span><p>주소, 셸코드, 레지스터 상태를 이용한다.</p></div>
                    </div>
                    <p>강사는 “입력값이 넘치면 메모리가 덮인다”는 말을 더 구체적으로 이해해야 한다고 강조한다. 메모리가 덮인다는 것은 특정 주소에 있던 데이터가 오염된다는 뜻이고, 이 오염을 이용해 원하는 명령이나 주소로 실행 흐름을 돌릴 수 있는지가 시스템 해킹의 중요한 출발점이다.</p>
                    <p>멘토는 나중에 스택, 힙, BSS, 데이터 영역을 배우면 이 구조가 퍼즐처럼 맞춰진다고 설명한다. 어떤 영역은 명령어가 있고, 어떤 영역은 데이터가 있고, 어떤 영역은 사용자가 접근할 수 있으며, 어떤 영역은 보호된다. 결국 시스템 해킹은 메모리를 보고, 조작 가능한 영역을 찾고, 원하는 실행 흐름을 구성하는 작업이다.</p>
                    """,
                },
                {
                    "heading": "RAM과 ROM",
                    "body": """
                    <p>메모리라고 하면 가장 먼저 RAM과 ROM이 나온다. 멘토는 가장 큰 차이를 <strong>휘발성</strong>과 <strong>비휘발성</strong>으로 설명한다. RAM은 전원이 꺼지면 내용이 사라지는 임시 저장 공간이고, ROM은 읽기 중심의 비휘발성 저장 공간으로 설명된다.</p>
                    """ + ca05_ram_rom + """
                    <table>
                      <thead><tr><th>구분</th><th>성격</th><th>강의에서의 설명</th></tr></thead>
                      <tbody>
                        <tr><td>RAM</td><td>휘발성, 읽기·쓰기 가능</td><td>프로그램 실행 중 임시로 데이터를 올려 두는 공간이다.</td></tr>
                        <tr><td>ROM</td><td>비휘발성, 읽기 중심</td><td>전원이 꺼져도 유지되는 저장 성격을 가진다.</td></tr>
                      </tbody>
                    </table>
                    <p>휘발성은 불편해 보이지만 중요하다. 프로그램이 잘못된 상태가 되었을 때 전원을 끄고 다시 시작하면 실행 중 상태가 초기화된다. 매번 잘못된 데이터를 영원히 들고 있는 것보다, 실행 환경을 새로 시작할 수 있다는 점이 장점이 된다. 반대로 전원이 꺼져도 유지되어야 하는 데이터는 비휘발성 저장 장치에 있어야 한다.</p>
                    <p>강의에서는 RAM, DRAM, SRAM, ROM, Flash, PROM, EPROM 같은 이름도 자격증 시험에서 나올 수 있으니 한 번쯤 기억해 두라고 말한다. 깊은 전자공학 수준으로 들어가기보다, 읽기·쓰기 가능 여부, 속도, 휘발성, 제품 예시, 용도 차이를 표처럼 정리해 두면 된다.</p>
                    """,
                },
                {
                    "heading": "메모리 계층 구조",
                    "body": """
                    <p>CPU에 가까운 저장 공간일수록 빠르고 비싸며 용량이 작다. CPU에서 멀어질수록 느리지만 싸고 용량이 커진다. 이 구조를 메모리 계층 구조라고 한다. 강의에서는 CPU 레지스터, 캐시 메모리, 메인 메모리(RAM), 저장 장치(SSD/HDD), 더 느린 보조 저장 매체 순서로 설명한다.</p>
                    """ + ca05_hierarchy + """
                    <table>
                      <thead><tr><th>계층</th><th>위치와 성격</th><th>특징</th></tr></thead>
                      <tbody>
                        <tr><td>레지스터</td><td>CPU 내부</td><td>가장 빠르지만 매우 작다.</td></tr>
                        <tr><td>캐시</td><td>CPU 가까이</td><td>RAM에서 자주 쓸 데이터를 미리 가져와 둔다.</td></tr>
                        <tr><td>RAM</td><td>메인 메모리</td><td>실행 중인 프로그램과 데이터를 올려 둔다.</td></tr>
                        <tr><td>SSD/HDD</td><td>저장 장치</td><td>프로그램과 파일을 비교적 큰 용량으로 보관한다.</td></tr>
                      </tbody>
                    </table>
                    <p>RAM 1TB가 SSD 1TB보다 훨씬 비싼 이유도 이 계층 구조로 이해할 수 있다. CPU가 너무 빠르기 때문에, 느린 저장 장치에서 매번 데이터를 가져오면 CPU가 기다리게 된다. 그래서 실행할 프로그램은 저장 장치에서 RAM으로 올라오고, RAM의 일부는 캐시에 미리 들어가며, CPU는 레지스터로 값을 가져와 빠르게 처리한다.</p>
                    <div class="diagram">
                      <div><span class="node-title">SSD/HDD</span><p>프로그램과 파일 보관</p></div>
                      <span class="arrow">→</span>
                      <div><span class="node-title">RAM</span><p>실행 중 데이터 적재</p></div>
                      <span class="arrow">→</span>
                      <div><span class="node-title">Cache</span><p>자주 쓸 데이터 미리 준비</p></div>
                      <span class="arrow">→</span>
                      <div><span class="node-title">Register</span><p>CPU가 즉시 사용할 값</p></div>
                    </div>
                    <p>계층 구조가 필요한 이유는 CPU가 너무 빠르기 때문이다. CPU가 명령을 다 처리했는데 RAM이나 저장 장치에서 데이터가 아직 도착하지 않으면 CPU는 기다리게 된다. 그래서 하드디스크나 SSD에 있는 프로그램 전체를 매번 직접 읽지 않고, 실행할 프로그램을 RAM으로 올리고, 자주 쓸 데이터는 캐시에 미리 가져오며, CPU는 레지스터에 값을 넣고 빠르게 처리한다.</p>
                    <p>이 구조는 성능뿐 아니라 경제성과 관리 측면에서도 유리하다. 모든 저장 공간을 레지스터처럼 빠르게 만들면 너무 비싸고 용량도 작아진다. 반대로 모든 저장 공간을 디스크처럼 크게만 만들면 CPU가 계속 기다린다. RAM이 부족하면 RAM을 늘리고, 저장 공간이 부족하면 SSD나 HDD를 늘리는 식으로 계층별 역할이 나뉘는 것도 이 구조 덕분이다.</p>
                    """,
                },
            ],
            "checks": [
                "디버거의 중단점이 왜 필요한지 설명할 수 있는가?",
                "초기화되지 않은 변수에 쓰레기값이 들어갈 수 있는 이유를 이해했는가?",
                "GDB에서 어셈블리, 레지스터, 메모리 주소를 볼 수 있다는 점을 설명할 수 있는가?",
                "리틀 엔디안과 빅 엔디안의 차이를 말할 수 있는가?",
                "버퍼 오버플로우와 셸코드 설명에서 엔디안이 왜 중요한지 이해했는가?",
                "RAM과 ROM, 메모리 계층 구조의 핵심 차이를 설명할 수 있는가?",
            ],
        },
        {
            "id": "1-6",
            "title": "입출력 시스템",
            "subtitle": "버스, 포트, USB, 인터럽트, DMA를 통해 컴퓨터가 외부 장치와 통신하는 방식을 이해한다.",
            "tags": ["입출력", "USB", "인터럽트"],
            "objectives": [
                "입출력 시스템을 컴퓨터와 외부 세계를 연결하는 구조로 이해한다.",
                "버스, 포트, USB 장치 식별, udev 실무 사례를 강의 흐름대로 정리한다.",
                "하드웨어 인터럽트, 소프트웨어 인터럽트, DMA가 CPU 동작과 성능에 어떤 영향을 주는지 설명한다.",
            ],
            "sections": [
                {
                    "heading": "입출력 시스템의 의미",
                    "body": """
                    """ + ca06_title + """
                    <p>입출력 시스템은 컴퓨터와 외부 세계를 연결하는 시스템이다. 키보드와 마우스는 입력 장치이고, 모니터는 출력 장치이며, USB 메모리나 여러 주변 장치도 입출력 시스템과 연결된다. 강의는 단순히 장치를 꽂고 빼는 이야기에서 끝나지 않고, 버스, 포트, USB 규격, 인터럽트, DMA까지 이어진다.</p>
                    <div class="diagram three-col">
                      <div><span class="node-title">입력</span><p>키보드, 마우스, USB 장치의 신호</p></div>
                      <div><span class="node-title">컴퓨터 내부</span><p>CPU, 메모리, 버스, 운영체제</p></div>
                      <div><span class="node-title">출력</span><p>모니터, 파일 저장, 외부 장치 응답</p></div>
                    </div>
                    """,
                },
                {
                    "heading": "버스: 데이터가 오가는 통로",
                    "body": """
                    <p>버스는 CPU, 메모리, 장치들 사이에서 데이터와 신호가 오가는 통로다. 강의에서는 컨트롤 버스, 어드레스 버스, 데이터 버스를 언급한다. 각각은 제어 신호, 주소 정보, 실제 데이터를 전달하는 역할로 이해하면 된다.</p>
                    """ + ca06_bus + """
                    <table>
                      <thead><tr><th>버스</th><th>역할</th><th>기억할 점</th></tr></thead>
                      <tbody>
                        <tr><td>Control Bus</td><td>읽기, 쓰기, 인터럽트 같은 제어 신호 전달</td><td>장치가 무엇을 해야 하는지 알려 주는 흐름</td></tr>
                        <tr><td>Address Bus</td><td>어느 위치의 데이터를 다룰지 주소 전달</td><td>CPU가 메모리나 장치의 특정 위치를 지정할 때 필요</td></tr>
                        <tr><td>Data Bus</td><td>실제 데이터 전달</td><td>명령어와 데이터가 이동하는 통로</td></tr>
                      </tbody>
                    </table>
                    <p>CPU가 명령어를 가져오고 데이터를 읽고 쓰려면 어느 주소를 볼지, 어떤 데이터를 옮길지, 지금 읽기인지 쓰기인지 같은 정보가 필요하다. 버스는 이런 흐름을 나누어 전달하는 통로로 볼 수 있다. 멘토는 버스라는 단어를 자주 쓰지는 않더라도, “어떤 버스를 통해 데이터가 전송된다”는 식의 표현을 이해할 수 있도록 개념만 잡으면 된다고 말한다.</p>
                    """,
                },
                {
                    "heading": "포트와 케이블",
                    "body": """
                    <p>포트는 컴퓨터와 외부 장치를 연결하는 인터페이스다. 대표적으로 USB 포트, HDMI 포트, 이더넷 포트, 디스플레이 포트 등이 있다. 멘토는 보안 제품에서 USB 관련 작업을 하고 있어 포트 종류를 구분하는 지식이 실무에서 도움이 된다고 말한다.</p>
                    """ + ca06_ports + """
                    <table>
                      <thead><tr><th>포트</th><th>강의에서의 설명</th></tr></thead>
                      <tbody>
                        <tr><td>USB-A</td><td>오래 널리 쓰인 직사각형 USB 단자다.</td></tr>
                        <tr><td>USB-C</td><td>앞뒤 구분 없이 꽂기 쉽고, 충전·데이터·화면 출력까지 폭넓게 쓰이는 흐름으로 설명된다.</td></tr>
                        <tr><td>Lightning</td><td>Apple 장치에서 쓰이던 단자로, USB-C 통합 흐름과 함께 변화하고 있다고 설명한다.</td></tr>
                        <tr><td>Ethernet</td><td>유선 네트워크를 연결할 때 쓰는 포트다. 네트워크 설정에서 이더넷이라는 단어를 보게 된다.</td></tr>
                        <tr><td>DP/HDMI</td><td>모니터나 그래픽 카드와 연결되는 영상 출력 포트로 설명된다. 실제 기능은 장치와 버전에 따라 확인해야 한다.</td></tr>
                      </tbody>
                    </table>
                    <p>강의에서는 과거 Android 5핀, USB-A, Apple Lightning처럼 단자가 달라 불편했던 경험을 이야기한다. USB-C가 보급되면서 양쪽 끝이 같은 케이블로 충전, 데이터 전송, 화면 출력까지 처리하는 경우가 많아졌고, iPhone 15부터 USB-C가 들어가는 흐름도 언급한다.</p>
                    <p>핵심은 포트 이름만 외우는 것이 아니라, 포트마다 규격과 버전이 있고 전송 속도, 안정성, 지원 기능이 달라질 수 있다는 점이다. HDMI, DisplayPort, Thunderbolt, USB-C도 모양만 보고 모든 기능을 단정하기보다 장치와 케이블의 버전을 함께 확인해야 한다.</p>
                    """,
                },
                {
                    "heading": "USB의 의미와 범용성",
                    "body": """
                    <p>USB는 Universal Serial Bus의 약자다. 강의에서 강조하는 핵심은 주변 기기를 쉽게 연결하게 만든 범용 단자라는 점이다. 웹캠, 게임 컨트롤러, 스마트폰, USB 메모리 등 매우 다양한 장치가 USB로 연결된다.</p>
                    """ + ca06_usb_connectors + """
                    <p>USB는 “범용”이라는 이름 그대로 주변 기기를 쉽게 연결하기 위해 만들어진 규격이다. 강사는 회사에서 USB 관련 테스트를 하며 웹캠, 게임 컨트롤러, 스마트폰, 저장 장치 등 정말 다양한 기기가 USB로 연결된다는 점을 체감했다고 말한다.</p>
                    <p>예전에는 5핀, USB-A, Lightning처럼 단자 종류가 달라 불편했지만, USB-C가 보급되면서 양쪽 끝이 같은 케이블 하나로 여러 장치를 연결하는 경험이 많아졌다. 멘토는 USB가 너무 일반적인 주제라 쉽게 지나갈 수 있지만, 실제 실무에서는 장치 종류를 판별하고 정책을 적용해야 하는 중요한 대상이 될 수 있다고 말한다.</p>
                    """,
                },
                {
                    "heading": "실무 사례: 리눅스에서 USB 장치 이벤트 받기",
                    "body": """
                    <p>멘토는 본인이 맡은 업무 사례를 공유한다. 어떤 보안 장비에 USB가 꽂히면, 단순히 “USB가 들어왔다”가 아니라 어떤 종류의 장치가 들어왔는지 알아야 했다. Windows에서는 장치 관리자나 탐색기 UI로 쉽게 볼 수 있지만, UI가 없는 리눅스 환경에서는 명령과 시스템 이벤트를 직접 다뤄야 한다.</p>
                    <p>리눅스에서는 커널이 많은 일을 한다. 메모리 관리, 디스크 공간 할당, 장치 관리 같은 작업이 커널과 연결된다. 리눅스는 많은 것을 파일로 간주하므로 장치도 파일처럼 다뤄지고, 장치가 추가되거나 제거될 때 이벤트가 발생한다.</p>
                    """ + ca06_udev + """
                    <p>이때 <strong>udev</strong>는 리눅스의 장치 관리자 역할을 한다. 장치가 꽂히면 udev 계열 시스템이나 라이브러리를 통해 이벤트를 받을 수 있고, 프로그램은 그 이벤트를 바탕으로 “입력됨”, “해제됨” 같은 상태를 알 수 있다.</p>
                    """ + code_block("""
                    USB 장치 연결
                        ↓
                    커널이 장치 이벤트 감지
                        ↓
                    udev 또는 libudev가 이벤트 전달
                        ↓
                    보안 제품이 장치 종류와 시간을 기록
                    """, "text") + """
                    <p>시간은 이벤트가 발생한 시각을 찍으면 되지만, 더 중요한 것은 어떤 장치가 꽂혔는지 판별하는 일이다. 포렌식이나 사고 분석에서는 마지막으로 꽂힌 USB가 무엇인지, 언제 꽂혔는지가 중요한 단서가 될 수 있다.</p>
                    """,
                },
                {
                    "heading": "USB 장치 식별: 클래스와 USB IDs",
                    "body": """
                    <p>USB 장치에는 자신을 판별할 수 있는 값들이 들어 있다. USB 규격에서는 base class, subclass, protocol 같은 값을 이용해 장치 종류를 구분한다. 예를 들어 특정 값이면 Mass Storage Device, 즉 저장 장치로 판단하기로 약속할 수 있다.</p>
                    """ + ca06_usb_if + """
                    <p>또 USB IDs처럼 벤더와 디바이스 정보를 모아 둔 자료를 활용하면 제조사와 장치 종류를 더 자세히 알 수 있다. 강의에서는 어떤 값이 있으면 삼성전자 장비로 판단하고, 그 아래 특정 디바이스 값으로 프린터인지 MP3인지 구분할 수 있다는 식의 예를 든다.</p>
                    """ + ca06_usb_ids + """
                    <table>
                      <thead><tr><th>정보</th><th>의미</th></tr></thead>
                      <tbody>
                        <tr><td>Class/Subclass/Protocol</td><td>장치가 저장 장치인지, 입력 장치인지 같은 큰 종류를 판별한다.</td></tr>
                        <tr><td>Vendor ID</td><td>제조사를 식별하는 값이다.</td></tr>
                        <tr><td>Device ID</td><td>제조사 안에서 특정 장치 모델을 식별하는 값이다.</td></tr>
                        <tr><td>Interface 정보</td><td>하나의 장치가 제공하는 기능 단위를 더 자세히 구분할 수 있다.</td></tr>
                      </tbody>
                    </table>
                    <p>예를 들어 <code>04e8</code> 같은 vendor 값이 Samsung Electronics를 가리키고, 그 아래 device 값에 따라 프린터, MP3 플레이어, 카메라, 저장 장치처럼 더 구체적인 장치를 구분할 수 있다. 정리하면, 장치가 꽂히는 이벤트를 받고, 그 장치에 들어 있는 식별 정보를 읽고, 표준화된 규격과 ID 테이블을 이용해 종류를 분류하면 보안 제품에서 원하는 정책이나 기록 기능을 만들 수 있다.</p>
                    """,
                },
                {
                    "heading": "인터럽트",
                    "body": """
                    <p>입출력 시스템에서 가장 중요한 개념으로 멘토는 인터럽트를 꼽는다. 인터럽트는 CPU가 기존 명령을 실행하는 중간에 외부나 내부에서 우선 처리해야 할 일이 끼어드는 신호로 이해하면 된다. USB를 꽂거나 키보드를 누르거나 마우스를 클릭하는 행동은 하드웨어 인터럽트와 연결된다.</p>
                    """ + ca06_interrupt_cycle + """
                    <div class="timeline compact">
                      <div><strong>기존 실행</strong><p>CPU가 명령을 가져오고 해석하고 실행한다.</p></div>
                      <div><strong>인터럽트 발생</strong><p>장치나 시스템이 우선 처리할 신호를 보낸다.</p></div>
                      <div><strong>인터럽트 처리</strong><p>정해진 처리 루틴을 실행한다.</p></div>
                      <div><strong>복귀</strong><p>원래 하던 작업으로 돌아간다.</p></div>
                    </div>
                    <p>그림처럼 CPU는 Fetch Cycle과 Execute Cycle을 반복하다가 interrupt가 enabled된 상태에서 인터럽트 여부를 확인하고, 필요하면 interrupt processing을 수행한다. 처리가 끝나면 원래 하던 작업으로 돌아온다. 오래된 컴퓨터에서 장치를 꽂았을 때 잠깐 멈추거나 버벅이는 경험은 이런 입출력 처리와 연결해 생각할 수 있다.</p>
                    """,
                },
                {
                    "heading": "하드웨어 인터럽트와 소프트웨어 인터럽트",
                    "body": """
                    <p>하드웨어 인터럽트는 외부 장치가 CPU에게 특정 처리를 요청할 때 발생하는 신호다. 키보드 입력, 마우스 클릭, USB 연결, 장치 상태 변화 같은 것이 여기에 해당한다.</p>
                    <p>소프트웨어 인터럽트는 프로그램 내부에서 중요한 시스템 기능을 요청할 때 등장한다. 강의에서는 시스템 콜이라는 단어를 연결해 소개한다. 시스템 콜은 사용자 프로그램이 커널의 기능을 요청하는 통로로, 시스템 해킹에서는 이 흐름이 중요하게 다뤄질 수 있다.</p>
                    <p>멘토는 지금 단계에서는 단어만 기억해도 충분하다고 말한다. 나중에 <code>int</code> 명령, 시스템 콜 번호, 사용자 영역과 커널 영역 전환, IPC, 시그널 같은 개념을 배우면 “이때 말한 소프트웨어 인터럽트가 이런 의미였구나” 하고 연결하면 된다.</p>
                    """,
                },
                {
                    "heading": "DMA",
                    "body": """
                    <p>DMA는 Direct Memory Access의 약자다. CPU를 거치지 않고 메모리와 입출력 장치 사이에서 데이터를 직접 전송하는 방식으로 이해하면 된다. 핵심은 CPU 부하를 줄일 수 있다는 점이다.</p>
                    """ + ca06_dma + """
                    <p>기존 방식처럼 입출력 연산마다 CPU가 계속 개입하면 CPU가 자기 일을 하다가 자주 멈추고 장치 처리에 시간을 써야 한다. DMA를 사용하면 특정 데이터 전송은 전용 장치나 컨트롤러가 맡고, CPU는 더 중요한 연산에 집중할 수 있다. 그래서 전체 시스템 성능을 높이는 데 도움이 된다.</p>
                    <div class="diagram two-col">
                      <div><span class="node-title">CPU 개입 방식</span><p>입출력 데이터 이동마다 CPU가 자주 관여한다.</p></div>
                      <div><span class="node-title">DMA 방식</span><p>장치와 메모리가 직접 데이터를 주고받아 CPU 부담을 줄인다.</p></div>
                    </div>
                    """,
                },
                {
                    "heading": "과목 마무리",
                    "body": """
                    """ + ca06_wrapup + """
                    <p>강의는 컴퓨터 구조 기초 전체를 마무리하며, 컴퓨터가 복잡해 보이지만 가장 밑으로 내려가면 단순한 원리들이 쌓여 있다고 정리한다. CPU가 명령을 가져오고 해석하고 실행하는 과정, 메모리가 데이터를 더 빨리 가져오도록 계층화되는 이유, 입출력 장치가 인터럽트와 DMA를 통해 시스템과 연결되는 이유를 이해하면 더 깊은 학습으로 갈 수 있다.</p>
                    <p>이 지식은 개발과 보안 양쪽에서 모두 쓰인다. 개발자는 메모리 최적화와 성능 문제를 생각할 수 있고, 보안 쪽으로 가면 프로그램 실행 과정, 어셈블리어, 메모리 조작을 바탕으로 시스템 해킹의 원리를 상상할 수 있다. 멘토는 더 궁금한 부분을 메모해 두고 질문하면 도와주겠다고 말하며 강의를 마무리한다.</p>
                    """,
                },
            ],
            "checks": [
                "버스의 세 종류와 역할을 구분할 수 있는가?",
                "USB가 Universal Serial Bus이며 주변 장치를 쉽게 연결하는 범용 규격이라는 점을 설명할 수 있는가?",
                "리눅스에서 udev가 장치 이벤트를 다루는 역할을 한다는 점을 이해했는가?",
                "USB class, vendor ID, device ID가 장치 식별에 어떻게 쓰이는지 설명할 수 있는가?",
                "하드웨어 인터럽트와 소프트웨어 인터럽트의 차이를 말할 수 있는가?",
                "DMA가 CPU 부하를 줄이는 이유를 설명할 수 있는가?",
            ],
        },
    ]
