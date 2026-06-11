def build_os_basic_lectures(code_block):
    return [
        {
            "id": "1-1",
            "title": "강의 개요",
            "subtitle": "운영체제 기초 과목이 OS 개념에서 리눅스 설치, CLI, 계정·권한, 패키지, 서비스, 서버, 배시, 모니터링으로 이어지는 흐름을 잡는다.",
            "tags": ["과목 소개", "리눅스", "CLI"],
            "objectives": [
                "운영체제 기초 과목의 전체 학습 범위를 파악한다.",
                "리눅스와 우분투를 설치하고 CLI 중심으로 다룰 준비를 한다.",
                "이 과목이 GUI 사용법보다 실무형 터미널 사용 능력을 만드는 강의임을 이해한다.",
            ],
            "sections": [
                {
                    "heading": "과목의 출발점",
                    "body": """
                    <p>강의는 박수현 멘토의 운영체제 기초 과정 소개로 시작한다. 첫 시간은 본격적인 실습보다 전체 강의가 어떤 순서로 진행되는지 확인하는 오리엔테이션이다. 운영체제가 무엇인지, 어떤 유형이 있는지, 운영체제가 무엇을 해 주는지부터 살펴본 뒤, 대표적인 운영체제 중 하나인 리눅스를 중심으로 진행한다.</p>
                    <p>리눅스에는 다양한 배포판이 있고, 그중 이 수업에서는 우분투를 사용한다. 우분투는 학습 자료와 설치 방법이 많고, 초보자가 접근하기 쉬운 배포판이기 때문에 이후 모든 실습의 기준 환경으로 잡는다.</p>
                    """,
                },
                {
                    "heading": "설치와 실습 환경",
                    "body": """
                    <p>학생들이 사용하는 개인 PC에는 보통 Windows가 설치되어 있다. 수업을 위해 기존 Windows를 지우고 우분투를 설치할 수는 없으므로, 강의는 VirtualBox 같은 가상 환경에 우분투를 설치하는 방식으로 진행된다. MacBook, 특히 M1·M2 기반 Mac 사용자는 VirtualBox 사용이 어렵기 때문에 클라우드 환경이나 다른 하이퍼바이저를 간단히 대안으로 언급한다.</p>
                    <div class="callout">강의의 기본 실습 방향은 “내 PC의 기존 운영체제는 유지하고, 가상 머신 안에 우분투를 설치해서 안전하게 연습한다”이다.</div>
                    """,
                },
                {
                    "heading": "GUI와 CLI",
                    "body": """
                    <p>우분투를 설치한 뒤에는 GUI와 CLI를 모두 본다. GUI는 Windows처럼 마우스로 클릭하며 창을 열고 프로그램을 실행하는 그래픽 환경이다. 하지만 실무 서버 환경에서는 GUI가 없는 경우가 많고, 원격에서 터미널로 접속해 명령어를 입력하는 CLI 환경을 훨씬 더 많이 사용한다.</p>
                    <p>그래서 이 과목의 핵심은 CLI와 셸을 익히는 데 있다. 터미널은 흔히 검은 배경에 흰 글씨가 나오는 화면으로 생각하면 되고, 사용자는 이 셸에 명령어를 입력해 파일, 디렉토리, 사용자 계정, 권한, 패키지, 서비스 등을 다룬다.</p>
                    <table>
                      <thead><tr><th>환경</th><th>강의에서의 의미</th></tr></thead>
                      <tbody>
                        <tr><td>GUI</td><td>그래픽 사용자 인터페이스. 마우스와 아이콘 중심으로 리눅스를 Windows처럼 다룬다.</td></tr>
                        <tr><td>CLI</td><td>명령어 기반 인터페이스. 실무 서버와 보안 실습에서 반드시 익혀야 한다.</td></tr>
                        <tr><td>Bash</td><td>수업에서 기본으로 사용할 대표적인 리눅스 셸이다.</td></tr>
                      </tbody>
                    </table>
                    """,
                },
                {
                    "heading": "전체 강의 흐름",
                    "body": """
                    <div class="timeline">
                      <div><strong>OS와 리눅스</strong><p>운영체제, 리눅스, 우분투의 의미를 잡는다.</p></div>
                      <div><strong>설치</strong><p>VirtualBox와 클라우드 환경에서 우분투를 준비한다.</p></div>
                      <div><strong>사용법</strong><p>GUI를 가볍게 보고, CLI에서 파일과 디렉토리를 다룬다.</p></div>
                      <div><strong>관리</strong><p>계정, 권한, 패키지, 데몬 서비스를 관리한다.</p></div>
                      <div><strong>운영</strong><p>서버 프로그램, 개발 환경, 배시 스크립트, 모니터링으로 확장한다.</p></div>
                    </div>
                    """,
                },
            ],
            "checks": [
                "운영체제 기초 과목이 어떤 순서로 진행되는지 설명할 수 있는가?",
                "왜 기존 PC를 지우지 않고 가상 머신에 우분투를 설치하는지 이해했는가?",
                "GUI보다 CLI를 더 중요하게 다루는 이유를 말할 수 있는가?",
            ],
        },
        {
            "id": "1-2",
            "title": "운영체제란 무엇인가, 리눅스란, 우분투란",
            "transcript_title": "운영체제란 무엇인가 리눅스란 우분투란",
            "subtitle": "운영체제를 하드웨어와 애플리케이션 사이의 시스템 소프트웨어로 이해하고, 리눅스와 우분투의 위치를 정리한다.",
            "tags": ["운영체제", "Linux", "Ubuntu"],
            "objectives": [
                "운영체제가 하드웨어 관리와 응용 소프트웨어 실행을 돕는 시스템 소프트웨어임을 이해한다.",
                "리눅스 커널, GNU 도구, 배포판의 관계를 설명한다.",
                "우분투의 버전, LTS, GA, HWE 같은 용어를 학습 맥락에서 이해한다.",
            ],
            "sections": [
                {
                    "heading": "운영체제의 역할",
                    "body": """
                    <p>운영체제는 사용자가 원하는 애플리케이션 소프트웨어가 하드웨어 위에서 원활하게 동작하도록 도와주는 시스템 소프트웨어다. 사용자는 웹브라우저, 워드 프로세서, 파워포인트, 포토샵, 영상 편집 프로그램 같은 응용 프로그램을 쓰고 싶어 한다. 그 아래에서 CPU, 메모리, 디스크, 그래픽 카드, 프린터, 네트워크 장치 같은 하드웨어를 직접 다루는 부담을 줄여 주는 것이 운영체제다.</p>
                    <p>운영체제는 시스템 하드웨어를 관리하고, 응용 소프트웨어를 실행하기 위해 하드웨어를 추상화하며, 공통 시스템 서비스를 제공한다. 스마트폰, 스마트 TV, 셋톱박스, 자율주행차, ATM처럼 다양한 하드웨어에도 각자 목적에 맞는 운영체제가 들어간다.</p>
                    """,
                },
                {
                    "heading": "하드웨어 추상화와 시스템 서비스",
                    "body": """
                    <p>응용 프로그램 개발자가 매번 SSD인지 HDD인지, C 드라이브인지 D 드라이브인지, 그래픽 카드가 어떤 모델인지 직접 다루면 개발이 지나치게 복잡해진다. 운영체제는 이런 하드웨어 차이를 추상화해서 파일 시스템, 화면 출력, 네트워크 통신, 프로세스 실행 같은 공통 인터페이스로 제공한다.</p>
                    <table>
                      <thead><tr><th>운영체제 기능</th><th>강의에서의 설명</th></tr></thead>
                      <tbody>
                        <tr><td>프로세서 관리</td><td>여러 프로그램이 동시에 실행되는 것처럼 보이도록 CPU 사용을 조정한다.</td></tr>
                        <tr><td>파일 관리</td><td>파일 저장, 읽기, 디렉토리 구조를 제공한다.</td></tr>
                        <tr><td>네트워크 관리</td><td>유선랜, Wi-Fi, 블루투스, LTE, 5G 같은 통신을 응용 프로그램이 쓰게 한다.</td></tr>
                        <tr><td>장치 관리</td><td>디스플레이, 프린터, 입력 장치 같은 하드웨어를 응용 프로그램과 연결한다.</td></tr>
                      </tbody>
                    </table>
                    """,
                },
                {
                    "heading": "가상 머신과 클라우드",
                    "body": """
                    <p>요즘에는 운영체제를 물리 하드웨어에만 직접 설치하지 않는다. VirtualBox, VMware, QEMU 같은 하이퍼바이저 위에 여러 운영체제를 설치할 수 있고, 이런 가상화된 하드웨어를 많은 사용자가 범용적으로 빌려 쓰는 환경이 클라우드다. 이 강의는 운영체제를 직접 다루기 위해 가상 머신을 만들고 그 안에 우분투를 설치하는 흐름으로 이어진다.</p>
                    <div class="diagram">
                      <div><span class="node-title">물리 하드웨어</span><p>CPU, 메모리, 디스크, 네트워크</p></div>
                      <span class="arrow">→</span>
                      <div><span class="node-title">하이퍼바이저</span><p>VirtualBox, VMware, QEMU</p></div>
                      <span class="arrow">→</span>
                      <div><span class="node-title">가상 OS</span><p>Windows, Ubuntu, 여러 Linux 배포판</p></div>
                    </div>
                    """,
                },
                {
                    "heading": "리눅스와 배포판",
                    "body": """
                    <p>리눅스는 좁게는 커널을 의미하지만, 실제 사용자가 만나는 리눅스 환경은 커널만으로 이루어지지 않는다. GNU 도구, 셸, 패키지 관리자, 데스크톱 환경, 설정 파일, 기본 유틸리티가 함께 묶여 배포판 형태로 제공된다. 우분투, 데비안, 페도라, 민트, 오픈수세, 만자로 같은 이름은 모두 이런 배포판을 가리킨다.</p>
                    <p>강의에서는 우분투가 2004년에 등장한 뒤 빠르게 인기를 얻었고, 오랫동안 대표적인 리눅스 배포판으로 자리 잡았다고 설명한다. 현재는 다른 배포판들도 인기를 얻지만, 우분투는 여전히 자료가 많고 학습 환경으로 쓰기 좋다.</p>
                    """,
                },
                {
                    "heading": "우분투 버전과 용어",
                    "body": """
                    <p>우분투에는 18.04, 20.04, 22.04처럼 버전 번호가 있다. 강의에서는 모든 명령어와 화면을 맞추기 위해 우분투 20.04를 기준으로 진행한다. 최신 버전을 쓰지 않는 이유는 수업 자료와 실습 환경을 일관되게 유지하기 위해서다.</p>
                    <table>
                      <thead><tr><th>용어</th><th>의미</th></tr></thead>
                      <tbody>
                        <tr><td>LTS</td><td>Long Term Support. 장기 지원 버전으로 안정적인 운영 환경에 적합하다.</td></tr>
                        <tr><td>GA</td><td>General Availability. 일반 사용자에게 정식 배포되는 버전이라는 의미로 여러 소프트웨어에서 쓰인다.</td></tr>
                        <tr><td>HWE</td><td>Hardware Enablement. 새 하드웨어 지원을 보강하는 흐름으로 이해하면 된다.</td></tr>
                      </tbody>
                    </table>
                    """,
                },
            ],
            "checks": [
                "운영체제가 하드웨어를 추상화한다는 말을 예시로 설명할 수 있는가?",
                "가상 머신과 클라우드가 운영체제 학습에 왜 등장하는지 이해했는가?",
                "리눅스 커널과 리눅스 배포판의 차이를 구분할 수 있는가?",
                "우분투 20.04를 기준으로 실습하는 이유를 설명할 수 있는가?",
            ],
        },
        {
            "id": "1-3",
            "title": "리눅스 설치하기: 가상머신 및 클라우드",
            "transcript_title": "리눅스 설치하기 가상머신 및 클라우드",
            "subtitle": "VirtualBox 기반 우분투 설치 절차와 가상 디스크, ISO, 네트워크 어댑터, Mac·클라우드 대안을 정리한다.",
            "tags": ["VirtualBox", "Ubuntu 설치", "클라우드"],
            "objectives": [
                "하이퍼바이저와 가상 머신의 관계를 설명한다.",
                "VirtualBox에서 우분투 20.04를 설치할 때 필요한 CPU, 메모리, 디스크, ISO 설정을 이해한다.",
                "NAT, 브리지, 내부 네트워크, 호스트 전용 어댑터의 차이를 큰 그림으로 파악한다.",
            ],
            "sections": [
                {
                    "heading": "왜 가상 머신에 설치하는가",
                    "body": """
                    <p>운영체제는 하드웨어를 제어하는 시스템 소프트웨어이므로, 원래는 물리 PC에 직접 설치한다. 하지만 학습 목적으로 기존 Windows나 macOS를 지우고 리눅스를 설치할 수는 없다. 그래서 하드웨어를 가상화해 여러 OS를 설치할 수 있게 도와주는 하이퍼바이저를 사용한다.</p>
                    <p>강의에서는 VirtualBox를 기본 도구로 사용한다. VMware는 오랜 역사를 가진 강력한 상용 하이퍼바이저이고, Hyper-V는 Windows Pro 이상에서 사용할 수 있으며, WSL도 엄밀히는 Windows 안의 가상화 기술 위에서 리눅스 환경을 제공한다. 하지만 수업에서는 오픈소스이고 접근하기 쉬운 VirtualBox를 기준으로 진행한다.</p>
                    """,
                },
                {
                    "heading": "가상 머신 생성과 디스크 설정",
                    "body": """
                    <p>VirtualBox에서 새 가상 머신을 만들 때 CPU 코어 수, 메모리 크기, 디스크 크기와 디스크 파일 형식을 정한다. 초급 과정에서는 복잡한 옵션을 깊게 다루지 않고 기본값을 따라가도 된다. 다만 디스크를 만들 때 동적 할당과 고정 크기의 차이는 기억해야 한다.</p>
                    <table>
                      <thead><tr><th>옵션</th><th>설명</th><th>강의의 기준</th></tr></thead>
                      <tbody>
                        <tr><td>동적 할당</td><td>처음부터 전체 용량을 차지하지 않고 필요할 때 커진다.</td><td>교육용 환경에서는 일반적으로 무리가 없다.</td></tr>
                        <tr><td>고정 크기</td><td>처음부터 정한 용량을 실제 파일로 확보한다.</td><td>과거 HDD 환경에서는 성능상 유리할 수 있었다.</td></tr>
                        <tr><td>VDI</td><td>VirtualBox 기본 디스크 이미지 형식이다.</td><td>다른 하이퍼바이저 호환성이 필요 없으면 기본값으로 충분하다.</td></tr>
                      </tbody>
                    </table>
                    """,
                },
                {
                    "heading": "ISO와 설치 과정",
                    "body": """
                    <p>가상 머신의 하드웨어 설정을 마치면 아직 운영체제가 설치된 것은 아니다. 우분투 ISO 이미지를 가상 CD-ROM에 넣어야 한다. 이는 물리 PC에 설치 CD나 USB를 꽂고 부팅하는 것과 같은 의미다. 강의 자료의 화면에는 다른 버전이 보일 수 있지만, 실제 수업 기준은 우분투 20.04다.</p>
                    <p>설치 과정에서는 사용자 이름과 패스워드를 만들고, 설치가 끝나면 “installation medium을 제거하라”는 안내가 나올 수 있다. 가상 CD를 뺐다고 알려 주는 의미로 엔터를 치면 재부팅되고, 이후 로그인 화면이 뜨면 설치가 완료된 것이다.</p>
                    """,
                },
                {
                    "heading": "업데이트와 종료 방식",
                    "body": """
                    <p>설치 직후 우분투가 새 버전으로 업그레이드할 것인지 묻거나 패키지 업데이트를 제안할 수 있다. 강의에서는 수업 환경을 20.04로 유지하기 위해 새 배포판으로 업그레이드하지 말라고 설명한다. 교육용 가상 머신에서는 자동 업데이트를 너무 자주 켜 두면 실습할 때마다 업데이트가 돌아 느려질 수 있으므로 최소화하는 것도 권장한다.</p>
                    <p>가상 머신을 끌 때도 강제로 전원을 끄는 것과 정상 종료는 다르다. 강제 종료는 물리 PC의 전원 플러그를 뽑는 것과 비슷해서 작업 중 데이터가 손상될 수 있다. 전원 버튼 신호 보내기나 운영체제 안의 종료 메뉴를 통해 graceful shutdown을 하는 것이 안정적이다.</p>
                    """,
                },
                {
                    "heading": "VirtualBox 네트워크와 Mac·클라우드 대안",
                    "body": """
                    <p>VirtualBox 네트워크 어댑터에는 NAT, 브리지, 내부 네트워크, 호스트 전용 어댑터, NAT 네트워크 같은 여러 모드가 있다. 온라인 강의에서는 기본 NAT를 사용해도 충분하지만, 오프라인 실습에서는 공격자와 방어자 같은 시나리오를 구성하기 위해 여러 가상 머신과 네트워크 모드를 조합할 수 있다.</p>
                    <table>
                      <thead><tr><th>모드</th><th>의미</th></tr></thead>
                      <tbody>
                        <tr><td>NAT</td><td>게스트 OS가 외부 인터넷을 사용할 수 있게 하는 기본 모드다.</td></tr>
                        <tr><td>브리지</td><td>게스트가 실제 네트워크에 직접 붙은 장비처럼 동작한다.</td></tr>
                        <tr><td>내부 네트워크</td><td>가상 머신끼리만 통신하는 실습망을 만들 때 쓴다.</td></tr>
                        <tr><td>호스트 전용</td><td>호스트 OS에서 게스트 OS로 접속하기 위한 망을 만들 때 쓴다.</td></tr>
                      </tbody>
                    </table>
                    <p>M1·M2 Mac에서는 VirtualBox 지원이 안정적이지 않을 수 있어 UTM, VMware Fusion, Parallels 같은 대안을 검토할 수 있다. 정말 아무 환경도 없다면 클라우드 프리티어에서 Ubuntu Server 20.04, 예를 들어 EC2 t2.micro 같은 최소 사양을 사용할 수도 있지만, 클라우드 자체는 별도 수업 범위이므로 여기서는 필요한 만큼만 언급한다.</p>
                    """,
                },
            ],
            "checks": [
                "하이퍼바이저가 무엇이고 왜 필요한지 설명할 수 있는가?",
                "VirtualBox에서 ISO를 넣는 것이 물리 CD를 넣는 것과 같은 의미임을 이해했는가?",
                "동적 할당과 고정 크기 디스크의 차이를 설명할 수 있는가?",
                "NAT와 호스트 전용 어댑터가 각각 어떤 상황에 쓰이는지 말할 수 있는가?",
            ],
        },
        {
            "id": "1-4",
            "title": "리눅스 GUI 환경 다루기 및 CLI 환경 이해하기",
            "transcript_title": "리눅스 GUI 환경 다루기 및 CLI 환경 이해하기",
            "subtitle": "우분투 GNOME GUI를 가볍게 익히고, 실무에서 CLI와 터미널이 중요한 이유를 이해한다.",
            "tags": ["GUI", "CLI", "GNOME"],
            "objectives": [
                "GUI와 CLI의 차이, 서버 실무에서 CLI가 중요한 이유를 설명한다.",
                "우분투 GNOME 환경의 메뉴바, 런처, 시스템 트레이, 기본 앱을 파악한다.",
                "터미널을 여는 방법과 GUI/CLI 설치 방식의 차이를 이해한다.",
            ],
            "sections": [
                {
                    "heading": "GUI와 서버 실무",
                    "body": """
                    <p>GUI는 Graphical User Interface의 약자로, Windows처럼 마우스로 아이콘을 클릭하고 창을 움직이며 프로그램을 실행하는 환경이다. 우리가 설치한 우분투 데스크톱에도 가상의 모니터가 있고, 그 위에서 GUI를 사용할 수 있다.</p>
                    <p>하지만 실제 업무 환경의 서버는 데이터센터 랙에 들어 있고, 보통 모니터를 직접 연결해 작업하지 않는다. 원격 터미널로 접속해 CLI에서 명령어를 입력하는 방식이 일반적이다. Ubuntu Server는 GUI를 기본 제공하지 않는 경우가 많고, 불필요한 X Window를 설치하면 용량과 자원을 낭비할 수 있다.</p>
                    """,
                },
                {
                    "heading": "GNOME 데스크톱 이해",
                    "body": """
                    <p>우분투 데스크톱은 기본적으로 GNOME 데스크톱 환경을 사용한다. KDE 같은 다른 데스크톱 환경으로 바꿀 수도 있지만, 수업에서는 기본값인 GNOME을 기준으로 본다. GNOME은 메뉴바, 런처, 시스템 트레이 배치가 Windows와 다르므로 처음에는 낯설 수 있다.</p>
                    <ul>
                      <li>런처는 좌측에 있는 앱 실행 영역으로, Windows의 작업 표시줄처럼 생각할 수 있다.</li>
                      <li>시스템 트레이는 우측 상단에 있고, 네트워크·전원·키보드 같은 상태를 다룬다.</li>
                      <li>GNOME에서는 앱의 메뉴가 창 안이 아니라 상단 메뉴바 쪽에 나타나는 경우가 있어 익숙해질 필요가 있다.</li>
                    </ul>
                    """,
                },
                {
                    "heading": "기본 애플리케이션과 한글 입력",
                    "body": """
                    <p>우분투에는 Firefox가 기본 웹브라우저로 들어 있다. Chrome을 쓰고 싶다면 별도로 설치해야 한다. Firefox에서 네이버 같은 사이트에 접속해 보고, 한영 전환이 되는지도 확인한다. 한글 키보드가 설정되어 있으면 한글과 영문을 함께 입력할 수 있으므로, 불필요한 영문 입력기를 제거해도 된다.</p>
                    <p>음악·동영상 플레이어, LibreOffice 같은 오피스 프로그램, Ubuntu Software 앱도 둘러본다. LibreOffice는 Word, Excel, PowerPoint와 비슷한 문서 작업을 할 수 있고 DOCX, XLSX 같은 XML 기반 파일 형식도 열 수 있다. 다만 세부 폰트, 애니메이션, 레이아웃은 완벽히 호환되지 않을 수 있다.</p>
                    """,
                },
                {
                    "heading": "GUI에서 소프트웨어 설치",
                    "body": """
                    <p>Chrome을 설치할 때는 웹에서 Ubuntu용 Chrome 패키지를 다운로드할 수 있다. 우분투는 데비안 계열이므로 <code>.deb</code> 패키지를 받는다. 파일을 더블클릭해 설치할 수도 있고, 백그라운드에서 조용히 설치되어 진행 상태가 잘 보이지 않을 수 있다.</p>
                    <p>GUI 설치가 잘 안 되거나 CLI로 설치하고 싶다면 터미널을 열어 다운로드 위치로 이동한 뒤 <code>dpkg</code>를 사용할 수 있다. 이 흐름은 뒤의 패키지 설치 강의에서 더 자세히 다룬다.</p>
                    """ + code_block("""
                    cd ~/Downloads
                    sudo dpkg -i google-chrome-stable_current_amd64.deb
                    """, "bash") + """
                    """,
                },
                {
                    "heading": "터미널과 원격 접속 준비",
                    "body": """
                    <p>터미널은 단축키 <code>Ctrl + Alt + T</code>로 열거나, 바탕화면 우클릭, 앱 검색에서 실행할 수 있다. 강의자는 화면을 크게 보여 주기 위해 SSH 원격 접속 환경을 준비하지만, 학생들은 우분투 GUI 안의 터미널에서 실습해도 된다.</p>
                    <p>이후 수업을 위해 OpenSSH Server를 설치할 수 있다는 점도 예고한다. 지금 당장 모든 학생이 따라 할 필요는 없고, 명령어 화면을 크게 보여 주기 위한 강의자의 환경 구성으로 이해하면 된다.</p>
                    """ + code_block("""
                    sudo apt install openssh-server
                    """, "bash") + """
                    """,
                },
            ],
            "checks": [
                "GUI와 CLI의 차이를 서버 실무 관점에서 설명할 수 있는가?",
                "GNOME의 런처와 시스템 트레이 위치를 이해했는가?",
                "우분투에서 Chrome을 설치할 때 `.deb` 패키지를 쓰는 이유를 설명할 수 있는가?",
                "터미널을 여는 방법과 강의자가 SSH 환경을 쓰는 이유를 이해했는가?",
            ],
        },
        {
            "id": "1-5",
            "title": "리눅스 기초 명령어",
            "subtitle": "CLI에서 파일, 디렉토리, 경로, 복사·이동·삭제, 매뉴얼, 편집기를 다루는 기본 명령어를 익힌다.",
            "tags": ["CLI 명령어", "파일 시스템", "Vim"],
            "objectives": [
                "터미널에서 현재 위치, 파일 목록, 숨김 파일, 파일 내용을 확인하는 명령어를 사용한다.",
                "파일과 디렉토리를 생성·삭제·이동·복사하는 기본 명령어를 이해한다.",
                "man, vimtutor, nano를 통해 스스로 도움말과 편집기를 익히는 방법을 안다.",
            ],
            "sections": [
                {
                    "heading": "목록 보기와 숨김 파일",
                    "body": """
                    <p>CLI에서 가장 먼저 익히는 것은 현재 위치와 파일 목록을 보는 일이다. <code>ls</code>는 현재 디렉토리의 파일을 보여 주고, <code>ls -l</code>은 긴 형식으로 권한, 소유자, 크기, 시간 정보를 함께 보여 준다. <code>ls -al</code>은 숨김 파일까지 보여 준다.</p>
                    <p>리눅스에서 숨김 파일은 이름이 점(<code>.</code>)으로 시작한다. <code>.hello.txt</code>는 <code>hello.txt</code>를 숨긴 것이 아니라 완전히 다른 파일이며, 점으로 시작하기 때문에 기본 목록에 보이지 않을 뿐이다. <code>.</code>은 현재 디렉토리, <code>..</code>은 상위 디렉토리를 의미한다.</p>
                    """ + code_block("""
                    pwd
                    ls
                    ls -l
                    ls -al
                    clear
                    """, "bash") + """
                    """,
                },
                {
                    "heading": "파일 만들기와 내용 보기",
                    "body": """
                    <p><code>touch</code>는 원래 파일의 수정 시간을 현재 시간으로 바꾸는 명령이다. 하지만 파일이 없으면 새 파일을 만들기 때문에 실무에서는 빈 파일을 만들 때도 자주 쓴다. <code>cat</code>은 파일 내용을 화면에 출력한다.</p>
                    """ + code_block("""
                    touch hello.txt
                    touch test1 test2 test3
                    touch .hello.txt
                    cat /etc/passwd
                    """, "bash") + """
                    <p>시스템 파일을 지우려 하거나 민감한 파일을 건드리면 권한 때문에 실패할 수 있다. 이 경험을 통해 리눅스에는 사용자와 권한이 있고, 권한이 시스템을 보호한다는 점을 느끼게 된다.</p>
                    """,
                },
                {
                    "heading": "디렉토리 만들기와 삭제",
                    "body": """
                    <p><code>mkdir</code>은 디렉토리를 만들고, <code>rmdir</code>은 빈 디렉토리를 삭제한다. 디렉토리 안에 파일이 있으면 <code>rmdir</code>로 삭제되지 않는다. 많은 파일과 하위 디렉토리를 한 번에 지우려면 <code>rm -r</code>을 사용할 수 있지만 매우 위험하므로 주의해야 한다.</p>
                    """ + code_block("""
                    mkdir dir1
                    mkdir dir2 dir3
                    mkdir dir1/sub1
                    mkdir -p dir2/sub1
                    rmdir dir3
                    rm -r dir2
                    """, "bash") + """
                    """,
                },
                {
                    "heading": "경로 이동과 특수 경로",
                    "body": """
                    <p><code>cd</code>는 Change Directory의 약자다. <code>cd dir1</code>로 하위 디렉토리에 들어가고, <code>cd ..</code>으로 상위 디렉토리로 올라간다. <code>~</code>는 홈 디렉토리, <code>-</code>는 직전에 있었던 디렉토리를 의미한다.</p>
                    """ + code_block("""
                    cd dir1
                    cd ..
                    cd ../..
                    cd ~
                    cd -
                    cd /etc
                    cd /var/log
                    cd
                    """, "bash") + """
                    <p>강의는 터미널에서 원하는 경로로 자유롭게 이동하는 연습을 반드시 해 보라고 강조한다. 리눅스 CLI를 쓸 때 경로 감각이 없으면 모든 실습이 어려워진다.</p>
                    """,
                },
                {
                    "heading": "복사, 이동, 파일 속성, 매뉴얼",
                    "body": """
                    <p><code>cp</code>는 파일을 복사하고, <code>mv</code>는 파일을 이동하거나 이름을 바꾼다. <code>file</code>은 대상이 텍스트 파일인지, 디렉토리인지, 실행 파일인지, 심볼릭 링크인지 같은 속성을 알려 준다. 명령어 옵션을 모두 외울 수 없기 때문에 <code>man</code>으로 매뉴얼을 보는 습관이 중요하다.</p>
                    """ + code_block("""
                    cp hello.txt hello2.txt
                    cp hello.txt dir1/
                    mv hello2.txt renamed.txt
                    file hello.txt
                    man ls
                    man file
                    man man
                    """, "bash") + """
                    """,
                },
                {
                    "heading": "편집기 숙제: Vim과 Nano",
                    "body": """
                    <p>강의 마지막 숙제는 편집기를 익히는 것이다. GUI가 없는 서버에서도 파일을 수정할 수 있어야 하므로 Vim 또는 Nano 같은 터미널 편집기를 알아야 한다. Vim은 기능이 강력하지만 처음에는 어렵기 때문에 <code>vimtutor</code>를 따라 하라고 권한다. Nano는 비교적 단순하고, 화면 아래에 <code>^O</code>, <code>^X</code>처럼 단축키 안내가 나오는데 여기서 <code>^</code>는 Control 키를 의미한다.</p>
                    """ + code_block("""
                    sudo apt install vim
                    vimtutor
                    nano memo.txt
                    # nano: Ctrl+O 저장, Ctrl+X 종료
                    """, "bash") + """
                    """,
                },
            ],
            "checks": [
                "숨김 파일이 점으로 시작한다는 점과 `ls -al`의 의미를 설명할 수 있는가?",
                "`touch`, `cat`, `mkdir`, `rmdir`, `rm -r`의 역할을 구분할 수 있는가?",
                "`cd ..`, `cd ~`, `cd -`가 각각 어디로 이동하는지 이해했는가?",
                "명령어 옵션을 모를 때 `man`을 찾아볼 수 있는가?",
                "Vim과 Nano를 왜 배워야 하는지 설명할 수 있는가?",
            ],
        },
        {
            "id": "1-6",
            "title": "사용자 계정 권한 관리",
            "transcript_title": "사용자 계정 권한 관리",
            "subtitle": "리눅스의 멀티유저 철학, root와 sudo, 계정 파일, 사용자 관리, 권한 비트, chmod와 chown을 정리한다.",
            "tags": ["root", "sudo", "권한"],
            "objectives": [
                "리눅스에서 사용자와 관리자가 분리되는 이유를 이해한다.",
                "`/etc/passwd`, `/etc/shadow`, UID, GID, 그룹의 의미를 설명한다.",
                "파일 권한 rwx, umask, chmod, chown의 기본 사용법을 이해한다.",
            ],
            "sections": [
                {
                    "heading": "리눅스의 멀티유저 철학",
                    "body": """
                    <p>Windows는 개인용 PC에서 출발했기 때문에 초기에는 사용자 권한 개념이 약했다. 반면 Linux는 Unix 철학을 이어받아 여러 사람이 하나의 시스템을 동시에 사용하는 환경을 전제로 한다. 아무나 프로그램을 설치하고 삭제하고 재부팅하면 시스템 전체에 장애가 생길 수 있으므로, 사용자와 관리자를 구분한다.</p>
                    <p>리눅스의 최상위 관리자는 <strong>root</strong> 또는 super user다. root는 거의 모든 권한을 행사할 수 있으므로 매우 신중하게 사용해야 한다. 우분투는 초보자의 root 남용을 막기 위해 root 직접 로그인을 기본적으로 막고, 필요할 때 <code>sudo</code>로 관리자 권한을 빌려 쓰는 방식을 사용한다.</p>
                    """,
                },
                {
                    "heading": "내가 누구인지 확인하기",
                    "body": """
                    <p><code>whoami</code>는 현재 사용자를 알려 주고, <code>id</code>는 UID, GID, 소속 그룹을 보여 준다. 우분투 설치 때 만든 첫 계정은 일반 사용자이지만 sudo, adm, cdrom, netdev 같은 여러 그룹에 속해 있어 필요한 관리 작업을 할 수 있다.</p>
                    """ + code_block("""
                    whoami
                    id
                    groups
                    sudo id
                    """, "bash") + """
                    <p>핵심은 “사용자로서의 나”와 “관리자로서 권한을 빌린 나”를 구분하는 것이다. 모든 명령 앞에 습관적으로 sudo를 붙이는 것은 좋지 않다. 정말 관리자 권한이 필요한 작업인지 먼저 생각해야 한다.</p>
                    """,
                },
                {
                    "heading": "계정 정보 파일",
                    "body": """
                    <p>리눅스의 계정 정보는 주로 <code>/etc/passwd</code>와 <code>/etc/shadow</code>에 저장된다. <code>/etc/passwd</code>는 사용자 이름, UID, GID, 홈 디렉토리, 로그인 셸 같은 기본 정보를 담는다. <code>/etc/shadow</code>는 암호 해시와 암호 정책 정보를 담기 때문에 일반 사용자가 읽을 수 없다.</p>
                    <p>강의에서는 shadow 파일 안의 날짜 숫자가 1970년 1월 1일 UTC를 기준으로 며칠이 지났는지 나타내는 값이라고 설명한다. 패스워드는 평문이 아니라 해시 값으로 저장되고, 패스워드가 잠긴 계정은 로그인할 수 없도록 표시된다.</p>
                    """ + code_block("""
                    cat /etc/passwd
                    sudo cat /etc/shadow
                    """, "bash") + """
                    """,
                },
                {
                    "heading": "사용자 생성과 삭제",
                    "body": """
                    <p>사용자 계정은 관리자만 만들 수 있다. 임의 사용자가 마음대로 계정을 만들면 백도어 계정을 만들거나 퇴사 후에도 접근 경로를 남길 수 있기 때문이다. <code>adduser</code>로 계정을 만들고, <code>deluser</code>로 계정을 삭제한다. 계정을 삭제해도 기본적으로 홈 디렉토리는 남을 수 있는데, 퇴사자의 작업 파일을 백업해야 할 수 있기 때문이다.</p>
                    """ + code_block("""
                    sudo adduser user2
                    cat /etc/passwd
                    sudo passwd user2
                    sudo chage -l user2
                    sudo deluser user2
                    """, "bash") + """
                    <p><code>passwd</code>는 실제 암호를 바꾸는 명령이고, <code>chage</code>는 암호 만료일, 사용 기간 같은 정책을 관리하는 명령이다. 실무에서는 로컬 계정보다 LDAP이나 Active Directory 같은 외부 인증 체계를 쓰는 경우도 많지만, 기본 원리는 반드시 알아야 한다.</p>
                    """,
                },
                {
                    "heading": "권한 비트와 umask",
                    "body": """
                    <p>리눅스 파일에는 소유자(owner), 그룹(group), 기타 사용자(other)에 대한 권한이 있다. 권한은 읽기(read), 쓰기(write), 실행(execute)으로 나뉘고 각각 <code>r</code>, <code>w</code>, <code>x</code>로 표현된다.</p>
                    <table>
                      <thead><tr><th>숫자</th><th>권한</th><th>의미</th></tr></thead>
                      <tbody>
                        <tr><td>4</td><td>r</td><td>읽기</td></tr>
                        <tr><td>2</td><td>w</td><td>쓰기</td></tr>
                        <tr><td>1</td><td>x</td><td>실행 또는 디렉토리 진입</td></tr>
                      </tbody>
                    </table>
                    <p>파일의 기본 권한은 보통 666에서 umask를 빼고, 디렉토리의 기본 권한은 777에서 umask를 뺀 값으로 만들어진다. 예를 들어 umask가 002이면 파일은 664, 디렉토리는 775 성격으로 생성된다.</p>
                    """ + code_block("""
                    umask
                    touch hello2.txt
                    mkdir testdir
                    ls -l
                    """, "bash") + """
                    """,
                },
                {
                    "heading": "chmod, chown, chgrp",
                    "body": """
                    <p><code>chmod</code>는 권한을 바꾼다. 숫자로 <code>777</code>, <code>700</code>, <code>755</code>처럼 줄 수도 있고, 문자로 <code>u+x</code>, <code>g-rw</code>처럼 줄 수도 있다. 이 부분은 정보보안기사 같은 시험에도 자주 나오므로 반드시 익혀야 한다.</p>
                    <p><code>chown</code>은 파일 소유자를 바꾸고, <code>chgrp</code>는 그룹을 바꾼다. 다만 실무에서는 <code>chown user:group file</code>처럼 chown으로 소유자와 그룹을 함께 바꾸는 경우가 많다. 남의 소유로 파일을 마음대로 바꾸면 책임 회피나 악성 파일 은닉 문제가 생길 수 있으므로 관리자 권한이 필요하다.</p>
                    """ + code_block("""
                    chmod 777 hello.txt
                    chmod 700 hello.txt
                    chmod u+x hello.txt
                    chmod g-rw hello.txt
                    sudo chown user2:user2 hello.txt
                    """, "bash") + """
                    <p>강의는 특수 권한에 대해서도 언급하지만, 기초반에서는 자세히 다루지 않는다. 나중에 SUID, SGID, sticky bit를 배우면 umask 앞쪽의 한 자리와 연결해서 이해하면 된다.</p>
                    """,
                },
            ],
            "checks": [
                "리눅스에서 root를 직접 쓰지 않고 sudo를 쓰는 이유를 설명할 수 있는가?",
                "`/etc/passwd`와 `/etc/shadow`의 차이를 말할 수 있는가?",
                "UID, GID, 그룹의 의미를 이해했는가?",
                "rwx 권한과 4, 2, 1 숫자 표현을 계산할 수 있는가?",
                "`chmod`, `chown`, `umask`가 각각 무엇을 하는지 설명할 수 있는가?",
            ],
        },
        {
            "id": "1-7",
            "title": "패키지 설치",
            "subtitle": "패키지와 패키지 관리자, apt와 dpkg, 저장소, 업데이트·업그레이드·삭제의 차이를 정리한다.",
            "tags": ["apt", "dpkg", "패키지 관리"],
            "objectives": [
                "패키지가 배포판 환경에 맞게 미리 컴파일되어 제공되는 소프트웨어 묶음임을 이해한다.",
                "apt update, install, remove, purge, autoremove, upgrade의 차이를 설명한다.",
                "Ubuntu 저장소의 main, universe, restricted, multiverse와 보안 업데이트의 의미를 파악한다.",
            ],
            "sections": [
                {
                    "heading": "패키지가 필요한 이유",
                    "body": """
                    <p>리눅스에서는 과거에 소프트웨어를 소스 코드로 받아 직접 컴파일해 쓰는 일이 흔했다. 하지만 배포판과 커널, 라이브러리 버전, 의존성이 너무 다양하기 때문에 일반 사용자가 매번 컴파일하고 문제를 해결하기는 어렵다. 그래서 배포판을 만드는 회사나 커뮤니티가 해당 배포판 환경에 맞게 미리 컴파일해 서버에 올려 둔 소프트웨어 묶음이 패키지다.</p>
                    <p>데비안·우분투 계열은 <code>.deb</code> 패키지를 사용하고, 레드햇 계열은 <code>.rpm</code> 패키지를 사용한다. 우분투에서는 apt와 dpkg를 통해 패키지를 설치하고 관리한다.</p>
                    """,
                },
                {
                    "heading": "apt와 dpkg의 관계",
                    "body": """
                    <p><code>apt</code>는 Advanced Package Tool로, 저장소에서 패키지 목록을 가져오고 의존성을 계산해 설치를 편하게 해 주는 상위 도구다. 실제 <code>.deb</code> 파일을 로컬에 설치하는 낮은 단계에서는 <code>dpkg</code>가 관여한다. 오래된 자료에서는 <code>apt-get</code>도 많이 보이는데, 강의에서는 apt가 더 상위의 편한 도구라고 설명한다.</p>
                    """ + code_block("""
                    sudo apt update
                    sudo apt install vim
                    sudo apt install tree
                    sudo dpkg -i package-name.deb
                    """, "bash") + """
                    """,
                },
                {
                    "heading": "삭제, 정리, 의존성",
                    "body": """
                    <p><code>apt remove</code>는 실행 파일 중심으로 삭제하지만 설정 파일과 데이터 파일은 남길 수 있다. 업그레이드나 재설치를 고려하면 설정을 남겨 두는 것이 유용할 때가 있기 때문이다. 반대로 더 이상 쓰지 않을 패키지를 깨끗하게 지우려면 <code>apt purge</code>를 사용한다.</p>
                    <p>패키지는 혼자 설치되지 않고 여러 의존 패키지를 함께 설치한다. A 패키지를 설치하며 B, C, D가 같이 설치되었더라도, 나중에 A만 지웠다고 B, C, D를 즉시 지우면 다른 패키지 G가 B나 D를 쓰고 있을 수 있다. 더 이상 어떤 패키지도 참조하지 않는 의존 패키지를 정리하는 명령이 <code>apt autoremove</code>다.</p>
                    """ + code_block("""
                    sudo apt remove nginx
                    sudo apt purge nginx
                    sudo apt autoremove
                    """, "bash") + """
                    """,
                },
                {
                    "heading": "저장소와 업데이트",
                    "body": """
                    <p><code>apt update</code>는 실제 프로그램을 새 버전으로 바꾸는 것이 아니라, 저장소의 패키지 목록과 URL 정보를 로컬에 갱신하는 명령이다. 실제 패키지를 업그레이드하려면 <code>apt upgrade</code>를 사용한다. 업그레이드 가능한 목록은 <code>apt list --upgradable</code>로 확인할 수 있다.</p>
                    <table>
                      <thead><tr><th>저장소</th><th>의미</th></tr></thead>
                      <tbody>
                        <tr><td>main</td><td>Canonical이 공식적으로 유지하는 핵심 저장소</td></tr>
                        <tr><td>universe</td><td>커뮤니티가 유지하는 저장소</td></tr>
                        <tr><td>restricted</td><td>장치 드라이버처럼 벤더가 관리하는 성격의 저장소</td></tr>
                        <tr><td>multiverse</td><td>공식 지원 밖의 소프트웨어가 포함될 수 있는 저장소</td></tr>
                      </tbody>
                    </table>
                    """ + code_block("""
                    sudo apt update
                    apt list --upgradable
                    sudo apt upgrade
                    """, "bash") + """
                    """,
                },
                {
                    "heading": "설정 파일과 잠금 문제",
                    "body": """
                    <p>GUI의 Software & Updates에서 보이는 저장소 설정은 CLI에서는 <code>/etc/apt/</code> 아래 설정 파일로 볼 수 있다. <code>sources.list</code>와 관련 파일들이 저장소 정보를 담고, <code>apt update</code>를 실행하면 <code>/var</code> 아래 캐시 파일들이 갱신된다.</p>
                    <p>가끔 apt install을 실행했는데 lock 관련 오류가 날 수 있다. 이는 백그라운드에서 다른 업데이트 프로세스가 apt를 사용 중이라는 뜻이다. 기다리면 해결되는 경우가 많지만, 정말 필요한 경우 어떤 프로세스가 잠금을 잡고 있는지 찾아 강제로 종료할 수도 있다. 다만 초급 단계에서는 위험할 수 있으므로 원리를 이해하고 신중하게 접근한다.</p>
                    """,
                },
                {
                    "heading": "배포판 업그레이드와 실습",
                    "body": """
                    <p>우분투 16.04에서 18.04, 18.04에서 20.04처럼 배포판 자체를 올릴 때는 release upgrade 계열 명령을 사용한다. 한 번에 여러 LTS 버전을 건너뛰는 것이 아니라 단계적으로 올리는 것이 기본이다. 하지만 수업 환경은 20.04를 유지해야 하므로 실습 중에는 배포판 업그레이드를 하지 않는다.</p>
                    <p>실습에서는 OpenSSH Server, Vim, Tree 같은 패키지를 설치하며 apt install의 흐름을 확인한다. <code>-y</code> 옵션은 의존 패키지 설치 여부를 묻는 질문에 자동으로 yes를 선택하게 한다.</p>
                    """ + code_block("""
                    sudo apt install -y openssh-server
                    sudo apt install vim
                    sudo apt install tree
                    tree
                    """, "bash") + """
                    """,
                },
            ],
            "checks": [
                "패키지가 소스 코드 직접 컴파일을 대신해 주는 이유를 설명할 수 있는가?",
                "`apt update`와 `apt upgrade`의 차이를 말할 수 있는가?",
                "`remove`, `purge`, `autoremove`의 차이를 구분할 수 있는가?",
                "main, universe, restricted, multiverse 저장소의 의미를 이해했는가?",
                "apt 잠금 오류가 왜 발생할 수 있는지 설명할 수 있는가?",
            ],
        },
        {
            "id": "1-8",
            "title": "데몬서비스 관리",
            "transcript_title": "데몬서비스 관리",
            "subtitle": "systemd, systemctl, journalctl을 통해 리눅스 데몬 서비스를 시작·중지·상태확인·자동시작 관리하는 방법을 익힌다.",
            "tags": ["systemd", "systemctl", "Nginx"],
            "objectives": [
                "데몬 서비스와 systemd의 역할을 이해한다.",
                "systemctl의 start, stop, restart, status, enable, disable을 구분한다.",
                "Nginx 예제로 서비스 상태와 웹 응답을 확인한다.",
            ],
            "sections": [
                {
                    "heading": "데몬 서비스와 systemd",
                    "body": """
                    <p>리눅스에는 사용자가 직접 실행한 프로그램 외에도 백그라운드에서 계속 동작하는 서비스가 많다. SSH, 웹 서버, 데이터베이스 서버처럼 시스템 시작과 함께 올라오고 계속 요청을 기다리는 프로그램을 데몬 서비스로 이해하면 된다.</p>
                    <p>과거에는 init 프로세스가 이런 서비스를 띄웠고, 지금 우분투에서는 systemd가 그 역할을 한다. systemd가 서비스, 소켓, 마운트, 부팅 타겟을 관리하고, 사용자는 <code>systemctl</code>로 제어한다.</p>
                    """,
                },
                {
                    "heading": "런레벨과 타겟",
                    "body": """
                    <p>고전적인 init 시스템에서는 runlevel 0, 1, 3, 5, 6 같은 숫자로 부팅 상태를 표현했다. 예를 들어 0은 종료, 1은 복구 모드, 3은 멀티유저 텍스트 모드, 5는 그래픽 모드처럼 이해할 수 있다. systemd에서는 이를 poweroff.target, rescue.target, multi-user.target, graphical.target처럼 글자로 표현한다.</p>
                    <p>기초 강의에서는 타겟을 깊게 다루지 않지만, systemd가 단순히 서비스 하나만 관리하는 것이 아니라 시스템 부팅 상태 전체를 관리한다는 점은 기억해야 한다.</p>
                    """,
                },
                {
                    "heading": "systemctl 기본 명령",
                    "body": """
                    <p><code>systemctl status sshd</code>처럼 서비스 상태를 볼 수 있다. 정식 이름은 <code>sshd.service</code>지만, <code>.service</code>는 생략해도 동작한다. 서비스 제어에는 관리자 권한이 필요하므로 start, stop, restart 같은 명령에는 보통 sudo가 필요하다.</p>
                    """ + code_block("""
                    systemctl status ssh
                    sudo systemctl start nginx
                    sudo systemctl stop nginx
                    sudo systemctl restart nginx
                    systemctl status nginx
                    """, "bash") + """
                    <p>리눅스 명령이 성공했을 때는 별도 메시지가 없는 경우가 많다. 오류가 나오지 않았으면 정상적으로 처리되었다고 보고, 상태 확인 명령으로 다시 확인한다.</p>
                    """,
                },
                {
                    "heading": "enable과 disable",
                    "body": """
                    <p><code>start</code>와 <code>stop</code>은 현재 실행 상태를 바꾼다. 반면 <code>enable</code>과 <code>disable</code>은 부팅 시 자동 시작 여부를 바꾼다. 따라서 현재 active이면서 disabled일 수도 있고, inactive이면서 enabled일 수도 있다.</p>
                    <table>
                      <thead><tr><th>상태 조합</th><th>의미</th></tr></thead>
                      <tbody>
                        <tr><td>active + enabled</td><td>지금 실행 중이고, 재부팅 후에도 자동 실행된다.</td></tr>
                        <tr><td>inactive + enabled</td><td>지금은 꺼져 있지만, 재부팅하면 자동 실행된다.</td></tr>
                        <tr><td>active + disabled</td><td>지금은 켜져 있지만, 재부팅 후 자동 실행되지는 않는다.</td></tr>
                        <tr><td>inactive + disabled</td><td>지금도 꺼져 있고, 재부팅해도 자동 실행되지 않는다.</td></tr>
                      </tbody>
                    </table>
                    """ + code_block("""
                    sudo systemctl enable nginx
                    sudo systemctl disable nginx
                    systemctl status nginx
                    """, "bash") + """
                    """,
                },
                {
                    "heading": "journalctl과 로그",
                    "body": """
                    <p>서비스가 실행되며 남긴 로그는 <code>journalctl</code>로 확인할 수 있다. 특정 서비스의 로그를 보거나, 특정 시간 이후의 로그를 볼 수 있다. 로그는 장애 분석에 중요하지만 계속 쌓이면 디스크를 차지하므로 관리가 필요하다.</p>
                    <p>로그에는 emergency, alert, critical, error, warning, notice, info, debug처럼 심각도 레벨이 있다. 단순 정보인지, 실제 장애인지 구분해서 읽을 수 있어야 한다.</p>
                    """ + code_block("""
                    journalctl -u nginx
                    journalctl -u nginx --since today
                    journalctl -xe
                    """, "bash") + """
                    """,
                },
                {
                    "heading": "Nginx 실습 흐름",
                    "body": """
                    <p>실습에서는 <code>sudo apt install nginx</code>로 웹 서버를 설치하고 <code>systemctl status nginx</code>로 상태를 확인한다. <code>curl localhost</code>나 브라우저에서 <code>localhost</code>를 열어 웹 서버가 응답하는지 본다. Nginx를 stop하면 curl과 브라우저 요청이 실패하고, 다시 start하면 응답이 돌아온다.</p>
                    """ + code_block("""
                    sudo apt install nginx
                    systemctl status nginx
                    curl localhost
                    sudo systemctl stop nginx
                    curl localhost
                    sudo systemctl start nginx
                    curl localhost
                    """, "bash") + """
                    """,
                },
            ],
            "checks": [
                "데몬 서비스와 일반 실행 프로그램의 차이를 설명할 수 있는가?",
                "systemd와 systemctl의 관계를 이해했는가?",
                "`start/stop`과 `enable/disable`의 차이를 말할 수 있는가?",
                "Nginx 서비스가 active인지 inactive인지 확인할 수 있는가?",
                "journalctl로 특정 서비스 로그를 볼 수 있는가?",
            ],
        },
        {
            "id": "1-9",
            "title": "서버프로그램 설치 및 관리",
            "transcript_title": "서버프로그램 설치 및 관리",
            "subtitle": "웹 서버, 파일 서버, 데이터베이스 서버를 설치하고 설정 파일과 서비스 관리를 연결해 본다.",
            "tags": ["웹 서버", "FTP", "MySQL"],
            "objectives": [
                "Nginx와 Apache 같은 웹 서버의 기본 구조와 설정 파일 위치를 이해한다.",
                "vsftpd를 이용한 FTP 서버 설정, 업로드 권한, chroot 제한을 이해한다.",
                "MySQL 서버 설치, 초기 접속, 데이터베이스와 사용자 권한 부여 흐름을 파악한다.",
            ],
            "sections": [
                {
                    "heading": "시즌2의 시작",
                    "body": """
                    <p>9강은 앞에서 배운 운영체제 개념, 우분투 설치, GUI/CLI, 계정과 권한, 패키지 설치, 데몬 서비스 관리 위에 서버 프로그램 운영을 얹는 강의다. 온라인 강의만 보고 따라 하기 어려운 설정도 있으므로, 포즈와 반복 재생을 하며 직접 명령어를 쳐 보라고 강조한다.</p>
                    <p>이 강의의 세 축은 웹 서버, 파일 서버, 데이터베이스 서버다. 모두 패키지 설치, 설정 파일 수정, systemctl로 서비스 재시작, 접속 확인이라는 공통 흐름을 가진다.</p>
                    """,
                },
                {
                    "heading": "웹 서버: Apache와 Nginx",
                    "body": """
                    <p>웹 서버로는 Apache와 Nginx가 대표적이다. Apache는 오래된 역사와 전통을 가진 웹 서버이고, Red Hat 계열에서는 httpd, Debian/Ubuntu 계열에서는 apache2라는 이름으로 설치된다. Nginx는 후발 주자지만 현재 많이 사용되는 웹 서버다. 이론에서는 Apache 설정 흐름을 설명하고, 실습은 Nginx로 진행한다.</p>
                    """ + code_block("""
                    sudo apt install apache2
                    sudo apt install nginx
                    systemctl status nginx
                    curl localhost
                    """, "bash") + """
                    """,
                },
                {
                    "heading": "Nginx 설정 파일 구조",
                    "body": """
                    <p>Nginx의 메인 설정은 <code>/etc/nginx/nginx.conf</code>에 있고, 사이트별 설정은 <code>/etc/nginx/sites-available/</code>과 <code>/etc/nginx/sites-enabled/</code> 구조로 관리된다. 실제 설정 파일은 available에 있고, enabled에는 심볼릭 링크로 활성화된 설정이 들어간다. <code>nginx.conf</code>는 enabled 안의 설정을 include한다.</p>
                    <table>
                      <thead><tr><th>경로</th><th>의미</th></tr></thead>
                      <tbody>
                        <tr><td><code>/etc/nginx/nginx.conf</code></td><td>Nginx 메인 설정 파일</td></tr>
                        <tr><td><code>/etc/nginx/sites-available/default</code></td><td>사이트별 실제 설정 파일</td></tr>
                        <tr><td><code>/etc/nginx/sites-enabled/default</code></td><td>활성화된 설정으로 연결되는 심볼릭 링크</td></tr>
                        <tr><td><code>/var/www/html</code></td><td>기본 웹 콘텐츠 루트</td></tr>
                      </tbody>
                    </table>
                    """ + code_block("""
                    cd /etc/nginx
                    cat nginx.conf
                    ls -l sites-enabled
                    cat sites-available/default
                    cat /var/www/html/index.nginx-debian.html
                    """, "bash") + """
                    """,
                },
                {
                    "heading": "가상 사이트와 포트 변경",
                    "body": """
                    <p>설정 파일의 <code>server</code> 블록에서 <code>listen 80</code>은 80번 포트로 요청을 받는다는 뜻이다. IPv4와 IPv6 설정이 각각 있을 수 있다. 기본 root를 <code>/var/www/html</code>에서 별도 디렉토리로 바꾸고, 8000번 포트로 새 사이트를 띄우는 실습을 진행한다.</p>
                    """ + code_block("""
                    sudo mkdir -p /var/www/whiteschool
                    sudo vi /var/www/whiteschool/index.html
                    sudo vi /etc/nginx/sites-available/default
                    sudo nginx -t
                    sudo systemctl restart nginx
                    curl localhost:8000
                    """, "bash") + """
                    <p>설정 파일을 바꿨으면 즉시 재시작하기 전에 <code>nginx -t</code>로 문법 오류가 없는지 확인한다. 오류가 없으면 서비스를 재시작하고 브라우저나 curl로 확인한다.</p>
                    """,
                },
                {
                    "heading": "파일 서버: vsftpd",
                    "body": """
                    <p>파일 서버는 FTP 서버를 예로 든다. 과거에는 문서, 유틸리티, 배포판 이미지, MP3, 영상 파일을 업로드·다운로드하는 데 FTP가 많이 쓰였다. 우분투에서는 <code>vsftpd</code>를 설치해 실습한다. 설정 파일은 별도 폴더가 아니라 <code>/etc/vsftpd.conf</code> 단일 파일로 존재한다.</p>
                    """ + code_block("""
                    sudo apt install vsftpd
                    sudo vi /etc/vsftpd.conf
                    sudo systemctl restart vsftpd
                    ftp 127.0.0.1
                    """, "bash") + """
                    <p>FTP 클라이언트는 우분투와 Windows에 기본 명령이 있고, GUI 클라이언트로 FileZilla도 사용할 수 있다. 한글이 깨질 경우 서버 설정에서 UTF-8 관련 값을 조정하고 서비스를 재시작한다.</p>
                    """,
                },
                {
                    "heading": "FTP 권한: 익명, 쓰기, chroot",
                    "body": """
                    <p>기본적으로 FTP는 OS 사용자 계정으로 로그인해 홈 디렉토리에 접근한다. 익명 사용자를 허용하려면 anonymous 관련 설정을 켜고, 공통 공유 폴더를 지정할 수 있다. 쓰기 권한은 기본적으로 꺼져 있는데, 업로드와 삭제가 가능해지므로 필요할 때만 <code>write_enable</code>을 켠다.</p>
                    <p>사용자가 로그인 후 <code>cd ..</code>으로 상위 디렉토리에 올라가 시스템 파일을 볼 수 있으면 위험하다. 이를 막기 위해 <code>chroot_local_user=YES</code> 같은 설정으로 사용자의 홈 디렉토리를 루트처럼 묶는다. 버전에 따라 추가 쓰기 관련 설정이 필요할 수 있고, 설정 후에는 반드시 서비스를 재시작한다.</p>
                    """ + code_block("""
                    # /etc/vsftpd.conf 예시
                    write_enable=YES
                    chroot_local_user=YES
                    allow_writeable_chroot=YES
                    """, "bash") + """
                    """,
                },
                {
                    "heading": "데이터베이스 서버: MySQL",
                    "body": """
                    <p>마지막은 MySQL 서버다. 데이터베이스에는 MySQL, MariaDB, MSSQL, PostgreSQL 등 여러 종류가 있지만, 실습에서는 대표적인 MySQL을 사용한다. 우분투 20.04 기준 최초 접속은 <code>sudo mysql</code>로 진행한다. 과거 버전이나 다른 배포판에서는 <code>mysql -u root</code> 흐름이 다를 수 있다.</p>
                    """ + code_block("""
                    sudo apt install mysql-server
                    systemctl status mysql
                    sudo mysql

                    SHOW DATABASES;
                    CREATE DATABASE whiteschool;
                    CREATE USER 'user1'@'localhost' IDENTIFIED BY 'QWE123';
                    GRANT ALL PRIVILEGES ON whiteschool.* TO 'user1'@'localhost';
                    FLUSH PRIVILEGES;
                    SELECT user, host FROM mysql.user;
                    exit

                    mysql -h localhost -u user1 -p
                    USE whiteschool;
                    """, "sql") + """
                    <p>FTP는 OS 사용자 계정을 사용할 수 있었지만, MySQL은 DB 내부 사용자와 권한을 따로 관리한다. 그래서 데이터베이스, 사용자, 접속 위치, 권한 부여가 별도로 필요하다.</p>
                    """,
                },
            ],
            "checks": [
                "Nginx의 available/enabled 설정 구조를 설명할 수 있는가?",
                "설정 변경 후 `nginx -t`와 서비스 재시작이 필요한 이유를 이해했는가?",
                "FTP에서 write_enable과 chroot 설정이 각각 무엇을 통제하는지 말할 수 있는가?",
                "MySQL에서 OS 사용자와 DB 사용자가 별도라는 점을 설명할 수 있는가?",
            ],
        },
        {
            "id": "1-10",
            "title": "개발환경 구축하기",
            "transcript_title": "개발환경 구축하기",
            "subtitle": "C, Python, Jupyter, Java, Docker 개발 환경을 우분투에서 설치하고 버전·권한·디스크 문제까지 함께 다룬다.",
            "tags": ["개발환경", "Python", "Docker"],
            "objectives": [
                "C 개발 도구와 바이너리 분석 도구의 설치 흐름을 이해한다.",
                "Anaconda, conda 가상 환경, Jupyter Notebook의 역할을 파악한다.",
                "Java 버전 관리와 Docker 설치·권한 설정의 기본 흐름을 이해한다.",
            ],
            "sections": [
                {
                    "heading": "개발 환경의 기본 관점",
                    "body": """
                    <p>개발 환경 구축은 단순히 프로그램 하나를 설치하는 일이 아니다. 언어별 컴파일러, 런타임, 라이브러리, 버전, 가상 환경, 서비스 관리, 권한, 디스크 공간까지 함께 고려해야 한다. 강의는 C, Python, Jupyter, Java, Docker를 예로 들어 우분투에서 개발 환경을 준비하는 흐름을 보여 준다.</p>
                    """,
                },
                {
                    "heading": "C 개발 환경",
                    "body": """
                    <p>C 언어 개발에는 <code>build-essential</code> 패키지를 설치한다. 여기에는 GCC, G++, make 같은 기본 빌드 도구가 포함된다. 바이너리 분석과 관련된 <code>binutils</code>에는 ld, ar, objdump 같은 도구가 들어 있다. 앞서 VirtualBox 확장팩 설치 과정에서 이미 설치되어 있을 수도 있다.</p>
                    """ + code_block("""
                    sudo apt install build-essential
                    sudo apt install binutils
                    gcc --version
                    g++ --version
                    make --version
                    """, "bash") + """
                    """ + code_block("""
                    #include <stdio.h>

                    int main(void) {
                        printf("hello world\\n");
                        return 0;
                    }
                    """) + code_block("""
                    gcc hello.c -o hello
                    ./hello
                    objdump -d hello
                    readelf -h hello
                    """, "bash") + """
                    <p>이 흐름은 이후 어셈블리어, ELF 파일, 악성코드 분석, 리버싱 수업과 연결된다.</p>
                    """,
                },
                {
                    "heading": "디스크 용량과 Anaconda 설치",
                    "body": """
                    <p>Anaconda는 용량을 많이 차지하므로 가상 머신 디스크가 부족할 수 있다. 강의에서는 VirtualBox에서 가상 디스크 크기를 늘리고, 리눅스 안에서 파티션과 파일 시스템을 확장하는 절차를 보여 준다. 이 부분은 파티셔닝과 파일 시스템이라는 큰 주제에 속하므로 기초 과정에서는 따라 하기 중심으로 다룬다.</p>
                    """ + code_block("""
                    df -h
                    lsblk
                    sudo apt install -y cloud-guest-utils
                    sudo growpart /dev/sda 2
                    sudo growpart /dev/sda 5
                    sudo resize2fs /dev/sda5
                    df -h
                    """, "bash") + """
                    <p>VirtualBox에서 물리적으로 디스크 파일을 늘린 뒤에도, 게스트 OS 안의 파티션과 파일 시스템을 확장해야 실제 사용 가능한 공간이 늘어난다.</p>
                    """,
                },
                {
                    "heading": "Python, Conda, Jupyter",
                    "body": """
                    <p>Python은 우분투에 기본으로 들어 있지만, AI나 데이터 분석, 보안 데이터 처리처럼 여러 프로젝트가 서로 다른 버전과 라이브러리를 요구하는 경우에는 가상 환경이 필요하다. Anaconda는 Python과 많은 데이터 분석 패키지, conda 환경 관리 기능을 제공한다.</p>
                    """ + code_block("""
                    conda create -n myenv python=3.10
                    conda activate myenv
                    python --version
                    conda deactivate
                    """, "bash") + """
                    <p>Jupyter Notebook은 웹 기반 개발 환경이다. 서버 안에서 실행하면 로컬 브라우저가 열릴 수 있고, SSH로 원격 접속한 환경에서는 <code>--ip=0.0.0.0</code>, <code>--no-browser</code> 옵션으로 외부 브라우저에서 접속할 수 있다. 토큰 링크를 사용하면 별도 입력 없이 접속할 수 있고, 토큰만 입력해도 된다.</p>
                    """ + code_block("""
                    jupyter notebook
                    jupyter notebook --ip=0.0.0.0 --no-browser
                    """, "bash") + """
                    <p>강의는 Jupyter Notebook을 systemd 서비스로 만들어 보는 것을 1강부터 배운 내용을 종합하는 숙제처럼 제안한다.</p>
                    """,
                },
                {
                    "heading": "Java와 update-alternatives",
                    "body": """
                    <p>자바는 런타임만 필요한 경우 JRE를, 개발까지 필요한 경우 JDK를 설치한다. 우분투 20.04에서는 OpenJDK 11이 기본 버전으로 제공된다. 여러 버전을 함께 관리하려면 <code>update-alternatives</code>를 사용한다.</p>
                    """ + code_block("""
                    sudo apt install default-jre
                    java -version
                    javac -version

                    sudo apt install default-jdk
                    javac -version

                    which java
                    whereis java
                    sudo update-alternatives --config java
                    """, "bash") + """
                    <p><code>which</code>는 지금 실행될 바이너리 경로를 보여 주고, <code>whereis</code>는 관련 파일 위치들을 넓게 보여 준다. update-alternatives는 여러 Java 또는 Python 버전 중 어떤 것을 기본으로 쓸지 선택하는 도구다.</p>
                    """,
                },
                {
                    "heading": "Docker 설치와 권한",
                    "body": """
                    <p>Docker는 우분투 공식 패키지로는 <code>docker.io</code> 이름으로 설치할 수 있다. 공식 Docker 최신 버전을 쓰려면 Docker 공식 저장소를 추가하는 다른 방법도 있지만, 기초 수업에서는 apt로 설치하는 흐름을 본다.</p>
                    """ + code_block("""
                    sudo apt install docker.io
                    docker --version
                    sudo docker run hello-world

                    sudo usermod -aG docker $USER
                    # 로그아웃 후 다시 로그인
                    docker version
                    docker run hello-world
                    """, "bash") + """
                    <p>Docker는 기본적으로 root 권한이 필요하므로 매번 <code>sudo docker</code>를 쓰게 된다. 개발 환경에서 sudo를 남용하지 않도록 현재 사용자를 docker 그룹에 추가하고, 다시 로그인해야 그룹 권한이 적용된다.</p>
                    <p>Docker 이미지는 기본적으로 <code>/var/lib/docker</code> 아래 쌓이므로 루트 파티션 공간을 빠르게 사용할 수 있다. 실무에서는 별도 디스크를 붙이고 데이터 파티션에 Docker 저장 경로를 배치하는 식으로 구성할 수 있다고 설명한다.</p>
                    """,
                },
                {
                    "heading": "개발 환경 구축의 결론",
                    "body": """
                    <p>필요한 개발 도구가 우분투 패키지로 제공되면 <code>sudo apt install</code>로 설치하고, 서비스가 필요하면 systemctl로 관리한다. 패키지가 없으면 공식 사이트에서 파일을 받거나 curl, dpkg 등으로 설치한다. 설치 후에는 <code>/etc</code> 아래 설정 파일을 확인하고 필요한 설정을 바꾸며, 서비스 재시작과 동작 확인까지 해야 개발 환경 구축이 끝난다.</p>
                    """,
                },
            ],
            "checks": [
                "build-essential과 binutils가 각각 어떤 개발·분석 도구를 제공하는지 말할 수 있는가?",
                "가상 디스크 크기와 리눅스 파일 시스템 크기가 별도라는 점을 이해했는가?",
                "conda 가상 환경이 여러 프로젝트의 라이브러리 충돌을 막는 이유를 설명할 수 있는가?",
                "JRE와 JDK의 차이를 구분할 수 있는가?",
                "Docker를 sudo 없이 쓰려면 왜 그룹 추가 후 재로그인이 필요한지 설명할 수 있는가?",
            ],
        },
        {
            "id": "1-11",
            "title": "배시 쉘 프로그래밍",
            "transcript_title": "배시 쉘 프로그래밍",
            "subtitle": "Bash 셸, 프롬프트, 리디렉션, 파이프, 히스토리, alias, 검색·필터 도구, 셸 스크립트 문법을 정리한다.",
            "tags": ["Bash", "Shell Script", "파이프"],
            "objectives": [
                "셸과 셸 스크립트의 의미를 이해하고 Bash를 기본 셸로 다룬다.",
                "프롬프트, 환경변수, 리디렉션, 파이프, 히스토리, alias를 설명한다.",
                "find, grep, awk, sed와 기본 셸 스크립트 문법을 활용한다.",
            ],
            "sections": [
                {
                    "heading": "셸과 Bash",
                    "body": """
                    <p>셸은 사용자의 명령어를 입력받아 실행하는 인터페이스다. 사용자는 셸에 명령을 입력하고, 셸은 시스템 콜 등을 통해 OS와 상호작용한 뒤 결과를 사용자에게 돌려준다. 반복 명령을 편하고 빠르게 처리하기 위해 짧은 프로그래밍을 작성하는 것이 셸 스크립트다.</p>
                    <p>셸에는 Bourne shell, Korn shell, C shell, Bash, Zsh 등이 있다. 이 수업은 가장 기본적으로 많이 쓰이는 Bash, 즉 Bourne Again Shell을 기준으로 한다. Oh My Zsh 같은 환경도 있지만, 실습은 Bash로 진행된다.</p>
                    """,
                },
                {
                    "heading": "프롬프트와 PS1",
                    "body": """
                    <p>프롬프트는 셸이 사용자의 입력을 받을 준비가 되었음을 보여 주는 표시다. 우분투에서는 보통 달러 기호가 보인다. 프롬프트에는 사용자명, 호스트명, 현재 디렉토리, 색상 코드가 포함될 수 있고, 이는 <code>PS1</code> 환경변수로 설정된다.</p>
                    """ + code_block("""
                    echo "$PS1"
                    default="$PS1"
                    PS1="\\u@\\h:\\w$ "
                    PS1="$default"
                    """, "bash") + """
                    <p><code>\\u</code>는 사용자명, <code>\\h</code>는 호스트명, <code>\\w</code>는 현재 디렉토리를 의미한다. 복잡한 숫자와 대괄호는 ANSI 색상 코드를 표현하기 위한 특수 문자다.</p>
                    """,
                },
                {
                    "heading": "리디렉션과 표준 입출력",
                    "body": """
                    <p>리디렉션은 명령의 출력이나 입력 방향을 바꾸는 기능이다. <code>&gt;</code>는 파일에 새로 쓰고, <code>&gt;&gt;</code>는 뒤에 덧붙인다. 표준 출력은 번호 1, 표준 에러는 번호 2로 다룰 수 있다. 성공 출력과 에러 출력을 같은 파일에 모으는 표현도 있다.</p>
                    """ + code_block("""
                    echo hello > hello.txt
                    echo world >> hello.txt
                    ls /tmp > result.txt 2>&1
                    ls /tmp &> result.txt
                    cat < hello.txt
                    """, "bash") + """
                    <p>애플리케이션마다 표준 입력을 받는 방식이 다르다. <code>cat</code>은 표준 입력을 받아 출력하지만, <code>echo</code>는 표준 입력을 읽는 도구가 아니기 때문에 같은 방식으로 동작하지 않는다.</p>
                    """,
                },
                {
                    "heading": "파이프, 히스토리, alias",
                    "body": """
                    <p>파이프는 한 명령의 출력을 다른 명령의 입력으로 넘기는 기능이다. <code>ls -l | grep hello</code>는 목록 출력 중 hello가 포함된 줄만 필터링한다. 파이프는 여러 번 이어 붙일 수도 있다.</p>
                    """ + code_block("""
                    ls -l | grep hello
                    ls -l | grep hello | wc -l
                    history
                    !120
                    !!
                    alias ll='ls -alF'
                    """, "bash") + """
                    <p><code>history</code>는 최근 실행 명령을 저장한다. <code>!</code>와 번호로 특정 명령을 다시 실행할 수 있고, <code>!!</code>는 바로 직전 명령을 다시 실행한다. alias는 긴 명령을 짧은 이름으로 줄이는 기능이다.</p>
                    """,
                },
                {
                    "heading": "검색과 필터 도구",
                    "body": """
                    <p><code>find</code>는 파일 이름, 크기, 날짜, 타입 같은 조건으로 파일을 찾는다. <code>grep</code>은 문자열이나 패턴을 찾고, <code>awk</code>는 컬럼을 골라 출력하며, <code>sed</code>는 스트림 편집기로 문자열 치환에 많이 쓰인다. 보안 로그 분석에서 특정 IP, 계정명, 공격 패턴을 뽑을 때 이런 도구들이 자주 쓰인다.</p>
                    """ + code_block("""
                    find / -size +100M -exec ls -lh {} \\; 2>/dev/null
                    grep -i "vim" file.txt
                    grep -R "password" /etc 2>/dev/null
                    ls -l | awk '{print $9, $5}'
                    cat copyright.txt | sed 's/book/books/g'
                    """, "bash") + """
                    <p>옵션을 모두 외울 수 없으므로 <code>man find</code>, <code>man grep</code>처럼 매뉴얼을 확인하며 필요한 옵션을 찾는 방식으로 익힌다.</p>
                    """,
                },
                {
                    "heading": "환경변수와 .bashrc",
                    "body": """
                    <p>Bash가 실행될 때 <code>.bashrc</code> 같은 설정 파일이 읽히고, alias, 프롬프트, Anaconda 초기화 스크립트 같은 내용이 적용된다. Anaconda를 삭제할 때 폴더만 지우면 끝나는 것이 아니라, <code>.bashrc</code>에 남아 있는 초기화 코드도 삭제해야 한다.</p>
                    """ + code_block("""
                    echo "$PATH"
                    which python3
                    vi ~/.bashrc
                    source ~/.bashrc
                    """, "bash") + """
                    """,
                },
                {
                    "heading": "셸 스크립트 작성",
                    "body": """
                    <p>셸 스크립트 파일은 보통 첫 줄에 shebang을 넣어 어떤 셸로 실행할지 표시한다. 실행 권한이 없으면 직접 실행할 수 없으므로 <code>chmod +x</code>로 권한을 준다. 또는 <code>bash script.sh</code>처럼 셸을 명시해 실행할 수도 있다.</p>
                    """ + code_block("""
                    #!/bin/bash
                    name="user"
                    echo "hello $name"
                    echo "first arg: $1"
                    echo "second arg: $2"
                    """, "bash") + code_block("""
                    chmod +x user.sh
                    ./user.sh white school
                    bash user.sh white school
                    """, "bash") + """
                    """,
                },
                {
                    "heading": "반복문과 조건문 예제",
                    "body": """
                    <p>강의 마지막 실습은 숫자를 출력하는 셸 스크립트다. 먼저 1부터 10까지 출력하고, 이후 if문을 넣어 짝수만 출력하도록 바꾼다. 이 예제는 앞서 배운 변수, 반복문, 조건문, 실행 권한을 하나로 묶는 연습이다.</p>
                    """ + code_block("""
                    #!/bin/bash
                    echo "짝수 출력 시작"

                    for ((i=1; i<=10; i++)); do
                        if [ $((i % 2)) -eq 0 ]; then
                            echo "$i"
                        fi
                    done

                    echo "짝수 출력 종료"
                    """, "bash") + """
                    """,
                },
            ],
            "checks": [
                "셸과 셸 스크립트의 차이를 설명할 수 있는가?",
                "리디렉션에서 표준 출력과 표준 에러를 구분할 수 있는가?",
                "파이프가 명령어 결과를 다음 프로세스로 넘긴다는 점을 이해했는가?",
                "find, grep, awk, sed가 각각 어떤 상황에 쓰이는지 설명할 수 있는가?",
                ".bashrc와 환경변수, alias의 관계를 이해했는가?",
                "셸 스크립트에 실행 권한이 필요한 이유를 말할 수 있는가?",
            ],
        },
        {
            "id": "1-12",
            "title": "시스템 운영 및 모니터링",
            "transcript_title": "시스템 운영 및 모니터링",
            "subtitle": "사용자, 프로세스, 파일 사용, 시스템 콜, 라이브러리, 네트워크 상태를 관찰하는 리눅스 운영 도구를 정리한다.",
            "tags": ["모니터링", "프로세스", "네트워크"],
            "objectives": [
                "사용자 접속 상태와 로그인 성공·실패 기록을 확인하는 도구를 이해한다.",
                "프로세스, job, signal, `/proc`, ps, kill, strace, ltrace의 용도를 파악한다.",
                "네트워크 인터페이스, 라우팅, 포트, DNS, 패킷 분석 도구의 기본 역할을 정리한다.",
            ],
            "sections": [
                {
                    "heading": "운영과 모니터링의 범위",
                    "body": """
                    <p>시스템을 운영하려면 사용자가 잘 접속하고 있는지, 원치 않는 접속 시도가 있는지, 어떤 프로세스가 동작하는지, 네트워크가 정상인지 계속 확인해야 한다. 이 강의는 사용자 모니터링, 프로세스 관리, 네트워크 모니터링 도구를 넓게 훑으며 OS 기초 과목을 마무리한다.</p>
                    """,
                },
                {
                    "heading": "사용자 모니터링",
                    "body": """
                    <p><code>users</code>는 접속 중인 사용자 이름을 보여 주지만 많이 쓰이지는 않는다. <code>who</code>는 사용자, 터미널, 접속 시간, 접속 위치를 보여 주고, <code>w</code>는 여기에 CPU 사용량과 최근 실행 명령까지 더 자세히 보여 준다.</p>
                    """ + code_block("""
                    users
                    who
                    w
                    """, "bash") + """
                    <p>TTY는 물리 터미널 성격의 접속을 의미하고, PTS는 네트워크를 통해 접속한 pseudo terminal을 의미한다. 현대 서버는 SSH 같은 네트워크 접속이 많으므로 PTS를 자주 보게 된다.</p>
                    """,
                },
                {
                    "heading": "로그인 기록과 침해 흔적",
                    "body": """
                    <p><code>last</code>는 로그인 성공 기록을 보여 주고, <code>lastb</code>는 로그인 실패 기록을 보여 준다. 클라우드 서버에는 공격자가 admin, root 같은 계정으로 무차별 로그인 시도를 하는 경우가 많고, 이런 실패 기록은 <code>lastb</code>로 확인할 수 있다.</p>
                    <p>관련 파일은 <code>/var/log/wtmp</code>와 <code>/var/log/btmp</code>다. wtmp는 일반 사용자가 읽을 수 있지만, btmp는 권한 때문에 sudo가 필요할 수 있다. 특정 사용자가 침해되었을 때는 <code>~/.bash_history</code>도 단서가 될 수 있지만, 공격자는 흔히 히스토리를 삭제하고 나가기 때문에 보조 자료로 봐야 한다.</p>
                    """ + code_block("""
                    last
                    sudo lastb
                    ls -l /var/log/wtmp /var/log/btmp
                    cat ~/.bash_history
                    """, "bash") + """
                    """,
                },
                {
                    "heading": "Job과 프로세스",
                    "body": """
                    <p>터미널에서 실행한 작업은 foreground와 background 사이를 오갈 수 있다. 실행 중인 작업을 잠시 멈추거나 백그라운드로 보내고, 다시 foreground로 가져오는 흐름을 job control이라고 볼 수 있다.</p>
                    """ + code_block("""
                    jobs
                    bg %1
                    fg %1
                    kill %1
                    """, "bash") + """
                    <p><code>ps</code>는 프로세스 상태를 보는 핵심 명령이다. 가장 자주 쓰는 형태 중 하나가 <code>ps aux</code>다. a는 전체 프로세스, u는 사용자 정보, x는 터미널에 붙지 않은 프로세스까지 포함하는 옵션으로 이해하면 된다.</p>
                    """ + code_block("""
                    ps
                    ps aux
                    ps aux | grep nginx
                    pstree
                    """, "bash") + """
                    """,
                },
                {
                    "heading": "/proc 파일 시스템",
                    "body": """
                    <p><code>/proc</code>는 물리 디스크에 저장된 일반 파일 시스템이 아니라, 커널이 프로세스와 시스템 정보를 파일처럼 보여 주는 특수 파일 시스템이다. 특정 PID 디렉토리에 들어가면 프로세스가 어떤 인자로 실행됐는지, 어떤 파일 디스크립터를 열고 있는지, 메모리 상태가 어떤지 확인할 수 있다.</p>
                    """ + code_block("""
                    pid=$(pgrep nginx | head -n 1)
                    cat /proc/$pid/cmdline
                    ls -l /proc/$pid/fd
                    cat /proc/$pid/status
                    """, "bash") + """
                    <p>침해 사고 분석이나 악성 프로세스 분석에서 어떤 파일과 소켓을 열고 있는지, 어떤 명령으로 실행됐는지 확인하는 데 도움이 된다.</p>
                    """,
                },
                {
                    "heading": "시그널과 추적 도구",
                    "body": """
                    <p><code>kill</code>은 이름과 달리 항상 “죽인다”는 뜻만은 아니다. 프로세스에 시그널을 보내는 명령이다. <code>SIGTERM</code>은 정상 종료를 요청하고, <code>SIGKILL</code>은 강제로 종료한다. <code>kill -9</code>는 강력하지만 프로세스가 정리 작업을 못 하고 종료될 수 있으므로 신중하게 사용한다.</p>
                    """ + code_block("""
                    kill -TERM <pid>
                    kill -9 <pid>
                    killall nginx
                    lsof -i
                    strace -p <pid>
                    ltrace ./hello
                    """, "bash") + """
                    <p><code>lsof</code>는 어떤 프로세스가 어떤 파일을 열고 있는지 보는 도구다. <code>strace</code>는 시스템 콜을 추적하고, <code>ltrace</code>는 라이브러리 호출을 추적한다. 기초 강의에서는 깊게 실습하지 않지만, 디버깅과 보안 분석에서 중요한 도구다.</p>
                    """,
                },
                {
                    "heading": "네트워크 인터페이스와 설정",
                    "body": """
                    <p>네트워크 모니터링에서는 먼저 인터페이스 상태와 IP 설정을 확인한다. 전통적으로 <code>ifconfig</code>가 많이 쓰였고, 현대 리눅스에서는 <code>ip</code> 명령도 많이 쓴다. 우분투 20.04에서는 NetworkManager가 GUI와 백그라운드에서 네트워크를 관리하므로 CLI 설정과 충돌할 수 있다.</p>
                    """ + code_block("""
                    ifconfig
                    ip addr
                    systemctl status NetworkManager
                    sudo systemctl stop NetworkManager
                    sudo systemctl start NetworkManager
                    """, "bash") + """
                    <p>우분투 18.04 이후 LTS 계열에서는 netplan 설정도 등장한다. <code>/etc/netplan/</code> 아래 설정 파일에서 NetworkManager나 networkd를 통해 네트워크를 관리하도록 지정할 수 있다.</p>
                    """,
                },
                {
                    "heading": "ARP, 라우팅, 포트",
                    "body": """
                    <p><code>arp</code>는 같은 LAN 구간의 인접 호스트 정보를 확인하는 데 사용된다. ARP 스푸핑 같은 공격은 별도 네트워크·보안 수업에서 더 자세히 다룬다. <code>route</code>와 <code>ip route</code>는 패킷이 어느 경로로 나가는지 확인하고, default route 같은 설정을 볼 때 사용한다.</p>
                    """ + code_block("""
                    arp -a
                    route -n
                    ip route
                    netstat -tulpen
                    ss -tulpen
                    """, "bash") + """
                    <p><code>netstat</code> 또는 <code>ss</code>는 열려 있는 포트와 연결 상태를 확인한다. 악성 코드가 어떤 포트를 열고 있는지, 어떤 프로세스가 외부와 통신하는지 볼 때도 유용하다.</p>
                    """,
                },
                {
                    "heading": "ping, traceroute, nslookup, tcpdump",
                    "body": """
                    <p><code>ping</code>은 ICMP 메시지를 보내 대상이 살아 있는지 확인하는 기본 도구다. <code>traceroute</code>는 목적지까지 가는 경로를 보여 주지만, 현대 네트워크에서는 중간 방화벽 때문에 결과가 잘 안 나오는 경우가 많다.</p>
                    <p><code>nslookup</code>은 도메인 이름을 IP 주소로 바꾸는 DNS 조회 도구다. DNS 서버 설정이 정상인지, DNS 스푸핑 같은 공격 때문에 의도와 다른 IP가 반환되는지 확인할 때 도움이 된다. 우분투 20.04에서는 과거의 <code>/etc/resolv.conf</code> 직접 관리보다 systemd-resolved를 통한 구조가 더 중요하다.</p>
                    """ + code_block("""
                    ping 8.8.8.8
                    traceroute google.com
                    nslookup google.com
                    systemctl status systemd-resolved
                    sudo tcpdump -i any
                    """, "bash") + """
                    <p><code>tcpdump</code>는 호스트로 들어오고 나가는 패킷을 덤프하는 핵심 네트워크 분석 도구다. 이 도구만으로도 여러 시간 강의가 가능할 정도로 방대하므로, 여기서는 “패킷을 직접 볼 수 있는 도구”라는 점만 잡고 이후 과정에서 더 깊게 다룬다.</p>
                    """,
                },
            ],
            "checks": [
                "`who`, `w`, `last`, `lastb`가 각각 어떤 정보를 보여 주는지 설명할 수 있는가?",
                "TTY와 PTS의 차이를 이해했는가?",
                "foreground/background job을 `fg`, `bg`, `jobs`로 관리할 수 있는가?",
                "`ps aux`와 `/proc/<pid>`가 프로세스 분석에 왜 유용한지 설명할 수 있는가?",
                "`kill -9`를 신중하게 써야 하는 이유를 이해했는가?",
                "네트워크 점검에서 ifconfig/ip, route, netstat/ss, ping, nslookup, tcpdump가 각각 어떤 역할을 하는지 말할 수 있는가?",
            ],
        },
    ]
