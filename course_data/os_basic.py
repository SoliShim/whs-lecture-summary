def build_os_basic_lectures(code_block, screen_figure):
    os01 = "운영체제 기초-01-강의-개요"
    os01_intro = screen_figure(
        "os-basic",
        os01,
        1,
        "운영체제 기초 과목 시작",
        "박수현 멘토가 WhiteHat School 운영체제 기초 과정을 소개하며, 첫 시간은 본격 실습 전 전체 과정의 방향을 잡는 오리엔테이션으로 진행된다.",
    )
    os01_outline = screen_figure(
        "os-basic",
        os01,
        13,
        "운영체제 기초 과정소개",
        "슬라이드는 운영체제와 리눅스·우분투, 리눅스 설치와 가상머신·클라우드, GUI와 CLI, 파일/디렉토리, 계정·권한, 패키지, 데몬 서비스, 서버 프로그램, 배시 쉘 프로그래밍으로 이어지는 큰 흐름을 보여 준다.",
    )
    os02 = "운영체제 기초-02-운영체제란-무엇인가-리눅스란-우분투란"
    os02_definition = screen_figure(
        "os-basic",
        os02,
        15,
        "운영체제의 정의와 계층 구조",
        "운영체제는 사용자와 응용 프로그램이 하드웨어를 직접 다루지 않아도 되도록 중간에서 하드웨어 추상화와 공통 시스템 서비스를 제공하는 시스템 소프트웨어다.",
    )
    os02_functions = screen_figure(
        "os-basic",
        os02,
        22,
        "운영체제의 주요 기능",
        "프로세스, 파일, 네트워크, 메인 메모리, 디스크 저장소, 입출력 장치, 보안, 명령어 해석 시스템처럼 응용 프로그램이 공통으로 필요로 하는 기능을 운영체제가 맡는다.",
    )
    os02_unix = screen_figure(
        "os-basic",
        os02,
        31,
        "UNIX 운영체제 계보",
        "Linux는 어느 날 갑자기 등장한 것이 아니라, AT&T UNIX와 BSD·System V·Solaris·AIX·HP-UX 등으로 이어지는 UNIX 계열 역사와 교육용 Minix의 흐름 속에서 탄생했다.",
    )
    os02_torvalds = screen_figure(
        "os-basic",
        os02,
        36,
        "리눅스 운영체제의 탄생",
        "리누스 토발즈는 Minix를 참고해 학습과 취미 목적으로 1991년 Linux 커널을 처음 공개했고, 이후 다양한 CPU와 워크스테이션·임베디드 장치로 이식되었다.",
    )
    os02_gnu = screen_figure(
        "os-basic",
        os02,
        46,
        "GNU 프로젝트와 자유 소프트웨어",
        "GNU 프로젝트는 누구나 실행, 복사, 수정, 배포할 수 있는 자유 소프트웨어를 지향했고, gcc·glibc·gnu-utils·gdb·emacs 같은 핵심 도구를 제공했다.",
    )
    os02_distribution_family = screen_figure(
        "os-basic",
        os02,
        75,
        "대표 리눅스 배포판 계열",
        "강의는 Slackware, Debian, Red Hat 계열을 대표 흐름으로 정리하고, 각 계열의 파생 배포판과 패키지 관리자 rpm·zypper, dpkg·apt, rpm·yum을 함께 소개한다.",
    )
    os02_distribution_components = screen_figure(
        "os-basic",
        os02,
        91,
        "리눅스 배포판의 구성 요소",
        "배포판은 리눅스 커널만이 아니라 데스크톱 UI, 유틸리티, 배포판 특화 설정 도구, 응용 소프트웨어, 매뉴얼, 고객지원까지 묶은 사용 가능한 운영체제 묶음이다.",
    )
    os02_desktop = screen_figure(
        "os-basic",
        os02,
        102,
        "리눅스 데스크톱 환경",
        "GNOME, KDE, XFce, LXDE처럼 리눅스에는 여러 데스크톱 환경이 있고, 강의에서는 대표적으로 GNOME과 KDE의 철학과 기반 기술을 비교한다.",
    )
    os02_kernel_types = screen_figure(
        "os-basic",
        os02,
        113,
        "단일형 커널과 마이크로 커널",
        "단일형 커널은 여러 핵심 기능을 한 덩어리로 묶고, 마이크로 커널은 통신·파일 시스템·장치 관리자 등을 더 작게 나누어 구성한다. 실제 운영체제는 이론적 구분만큼 단순하지 않고 하이브리드 성격을 가진다.",
    )
    os02_kernel_org = screen_figure(
        "os-basic",
        os02,
        125,
        "kernel.org와 바닐라 커널",
        "kernel.org와 git.kernel.org에서는 Linux 커널의 mainline, stable, longterm 버전과 토발즈가 관리하는 바닐라 커널 소스 트리를 확인할 수 있다.",
    )
    os02_ubuntu_version = screen_figure(
        "os-basic",
        os02,
        143,
        "우분투 버전, LTS, GA, HWE",
        "Ubuntu 버전은 출시 연월을 바탕으로 이해할 수 있고, LTS는 장기 지원, GA는 정식 일반 배포, HWE는 새 하드웨어 지원을 위한 커널·드라이버 보강 흐름을 뜻한다.",
    )
    os02_popularity = screen_figure(
        "os-basic",
        os02,
        156,
        "리눅스 주요 배포판 인기도 변화",
        "강의 마지막에는 DistroWatch 기반 인기도 변화 영상을 보며 Ubuntu가 2004년 등장 후 빠르게 성장했고, Mint·Debian·Manjaro 같은 배포판도 시대에 따라 주목받았음을 설명한다.",
    )
    os03 = "운영체제 기초-03-리눅스-설치하기-가상머신-및-클라우드"
    os03_hypervisor = screen_figure(
        "os-basic",
        os03,
        11,
        "대표 하이퍼바이저 소프트웨어",
        "VirtualBox, VMware, Microsoft Hyper-V는 하나의 물리 PC 위에서 여러 운영체제를 실행할 수 있게 해 주는 대표적인 하이퍼바이저다.",
    )
    os03_download = screen_figure(
        "os-basic",
        os03,
        21,
        "VirtualBox 다운로드와 Extension Pack",
        "강의 자료는 VirtualBox 6.1 기준 캡처지만 최신 7.0 계열로 설치해도 무방하며, 본체와 Oracle VM VirtualBox Extension Pack을 함께 내려받는다.",
    )
    os03_create_vm = screen_figure(
        "os-basic",
        os03,
        35,
        "새 가상 머신 생성",
        "새로 만들기 메뉴에서 Ubuntu 가상 머신을 만들고, 화면 캡처의 16.04 대신 실습 기준인 20.04를 사용하라는 강사의 주석을 확인한다.",
    )
    os03_disk = screen_figure(
        "os-basic",
        os03,
        47,
        "디스크 종류와 동적 할당",
        "가상 디스크는 VirtualBox 기본 형식인 VDI를 사용하고, 교육용 환경에서는 10GB 정도의 동적 할당 디스크로 시작해도 충분하다.",
    )
    os03_iso_network = screen_figure(
        "os-basic",
        os03,
        61,
        "ISO 삽입과 네트워크 어댑터",
        "Ubuntu ISO를 가상 CD-ROM에 넣고, 어댑터 1은 NAT로 유지하며, 이후 호스트 전용 어댑터를 추가해 Windows 호스트에서 게스트 Ubuntu로 접속할 수 있음을 설명한다.",
    )
    os03_install_button = screen_figure(
        "os-basic",
        os03,
        70,
        "Ubuntu 체험하기가 아니라 설치하기",
        "한국어를 선택한 뒤에는 Ubuntu 체험하기가 아니라 Ubuntu 설치를 눌러야 실제 디스크에 설치가 진행된다.",
    )
    os03_user_account = screen_figure(
        "os-basic",
        os03,
        75,
        "기본 사용자 계정 설정",
        "수업을 그대로 따라가려면 사용자 이름은 user1, 교육용 비밀번호는 qwe123으로 맞추되, 이 비밀번호는 실무나 클라우드에서는 절대 사용하면 안 된다.",
    )
    os03_updates = screen_figure(
        "os-basic",
        os03,
        102,
        "업그레이드와 자동 업데이트 설정",
        "20.04 실습 환경을 유지하기 위해 새 배포판 업그레이드는 거부하고, 교육용 VM에서는 자동 업데이트를 최소화해 실습 중 방해를 줄인다.",
    )
    os03_shutdown = screen_figure(
        "os-basic",
        os03,
        111,
        "VirtualBox 종료 옵션",
        "현재 상태 저장, 전원 버튼 신호 보내기, 시스템 전원 끄기 옵션 중 안정적인 종료는 전원 버튼 신호 보내기처럼 OS의 정상 종료 절차를 거치는 방식이다.",
    )
    os03_guest_additions = screen_figure(
        "os-basic",
        os03,
        123,
        "Guest Additions 설치와 build-essential",
        "Ubuntu 20.04에서는 Guest Additions 모듈 빌드에 필요한 도구가 빠져 있을 수 있으므로 sudo apt install build-essential -y를 먼저 실행해야 한다.",
    )
    os03_network_modes = screen_figure(
        "os-basic",
        os03,
        126,
        "VirtualBox 네트워크 모드",
        "NAT, 브리지 어댑터, 내부 네트워크, 호스트 전용 어댑터, NAT 네트워크를 조합하면 공격자·방어자 VM 같은 실습망을 구성할 수 있다.",
    )
    os03_mac_alt = screen_figure(
        "os-basic",
        os03,
        136,
        "Mac 사용자를 위한 대안",
        "Intel Mac은 VirtualBox를 사용할 수 있지만 M1·M2 Mac은 UTM, VMware Fusion, Parallels 같은 대안을 검토해야 한다.",
    )
    os03_cloud = screen_figure(
        "os-basic",
        os03,
        141,
        "클라우드 대안과 EC2 프리티어",
        "정말 로컬 가상화 환경을 만들 수 없다면 AWS EC2 프리티어에서 Ubuntu Server 20.04 LTS, t2.micro, SSH 접속으로 최소 실습 환경을 만들 수 있다.",
    )
    os04 = "운영체제 기초-04-리눅스-GUI-환경-다루기-및-CLI-환경-이해하기"
    os04_gui_cli = screen_figure(
        "os-basic",
        os04,
        8,
        "GUI 환경과 CLI 환경 비교",
        "왼쪽은 Ubuntu Desktop의 그래픽 환경이고, 오른쪽은 Ubuntu Desktop의 텍스트 모드 또는 Ubuntu Server에서 주로 쓰는 CLI 환경이다.",
    )
    os04_gnome_menu = screen_figure(
        "os-basic",
        os04,
        13,
        "GNOME 메뉴바와 런처 구성",
        "Ubuntu Desktop 기본 GUI인 GNOME은 좌측 런처, 상단 메뉴바, 우측 상단 시스템 트레이를 중심으로 구성된다.",
    )
    os04_window_menu = screen_figure(
        "os-basic",
        os04,
        21,
        "GNOME의 상단 메뉴바 표시 방식",
        "GNOME에서는 파일 관리자, Firefox, LibreOffice처럼 현재 활성화된 창에 따라 창 메뉴가 화면 상단 메뉴바에 표시되는 특징이 있다.",
    )
    os04_program_search = screen_figure(
        "os-basic",
        os04,
        27,
        "프로그램 검색과 Ubuntu 20.04 UI 차이",
        "16.04 기준 캡처와 달리 Ubuntu 20.04에서는 프로그램 검색 화면의 위치와 표현이 달라졌고, 하단 앱 메뉴에서 설치된 앱과 파일을 찾는다.",
    )
    os04_firefox_hangul = screen_figure(
        "os-basic",
        os04,
        40,
        "Firefox에서 인터넷 접속과 한글 입력 확인",
        "Ubuntu 기본 브라우저인 Firefox로 네이버에 접속하고, 한글 키보드와 한영 전환이 제대로 동작하는지 확인한다.",
    )
    os04_chrome_deb = screen_figure(
        "os-basic",
        os04,
        47,
        "Chrome Linux 패키지 선택",
        "Ubuntu는 Debian 계열이므로 Chrome 다운로드 화면에서 64비트 .deb(Debian/Ubuntu용) 패키지를 선택한다.",
    )
    os04_chrome_cli = screen_figure(
        "os-basic",
        os04,
        59,
        "터미널에서 dpkg와 sudo로 Chrome 설치",
        "dpkg -i만 실행하면 슈퍼유저 권한이 필요하다는 오류가 나고, sudo dpkg -i로 관리자 권한을 사용해야 설치가 진행된다.",
    )
    os04_launcher_pin = screen_figure(
        "os-basic",
        os04,
        68,
        "Chrome 실행 후 런처에 고정",
        "Chrome을 한 번 실행한 뒤 아이콘을 우클릭하면 런처에 고정할 수 있고, 드래그 앤 드롭으로 Firefox 근처에 배치할 수 있다.",
    )
    os04_libreoffice = screen_figure(
        "os-basic",
        os04,
        74,
        "LibreOffice 오피스 프로그램",
        "Ubuntu에는 LibreOffice Writer, Calc, Impress가 기본 제공되어 Word, Excel, PowerPoint와 유사한 문서 작업을 할 수 있다.",
    )
    os04_ubuntu_software = screen_figure(
        "os-basic",
        os04,
        84,
        "Ubuntu Software에서 애플리케이션 설치",
        "Ubuntu Software는 스마트폰 앱스토어처럼 애플리케이션을 검색하고 설치·업데이트·삭제할 수 있는 GUI 도구다.",
    )
    os04_settings = screen_figure(
        "os-basic",
        os04,
        101,
        "Ubuntu 20.04 시스템 설정",
        "Ubuntu 20.04의 시스템 설정은 스마트폰 설정처럼 왼쪽에서 항목을 고르고 오른쪽에서 세부 옵션을 조정하는 방식이다.",
    )
    os04_updates = screen_figure(
        "os-basic",
        os04,
        108,
        "Software & Updates의 업데이트 정책",
        "보안 업데이트와 추천 업데이트, 백포트, 자동 확인 주기, 새 Ubuntu 버전 알림 같은 업데이트 정책을 여기에서 조정한다.",
    )
    os04_terminal = screen_figure(
        "os-basic",
        os04,
        111,
        "터미널 실행과 Ctrl+Alt+T",
        "터미널은 바탕화면 우클릭 메뉴의 터미널 열기나 Ctrl+Alt+T 단축키로 실행할 수 있고, 이후 강의의 중심 도구가 된다.",
    )
    os04_tweaks = screen_figure(
        "os-basic",
        os04,
        123,
        "GNOME Tweaks와 창 활성화 방식",
        "GNOME Tweaks를 설치하면 폰트, 테마, 바탕화면 아이콘, 창 활성화 방식처럼 기본 설정 화면에 없는 세부 GUI 옵션을 조정할 수 있다.",
    )
    os04_compiz = screen_figure(
        "os-basic",
        os04,
        129,
        "Compiz Fusion 3D Desktop 효과",
        "리눅스 GUI는 3D 데스크톱과 화려한 창 효과도 구성할 수 있지만, VirtualBox 실습 환경에서는 그래픽 성능 때문에 권장하지 않는다.",
    )
    os05 = "운영체제 기초-05-리눅스-기초-명령어"
    os05_fhs = screen_figure(
        "os-basic",
        os05,
        3,
        "Filesystem Hierarchy Standard 구조",
        "리눅스 파일시스템은 최상위 루트 디렉토리 / 아래에 bin, boot, dev, etc, home, lib, media, mnt, proc, root, sbin, tmp, usr, var 같은 표준 디렉토리를 둔다.",
    )
    os05_boot = screen_figure(
        "os-basic",
        os05,
        15,
        "/boot 디렉토리와 커널 파일",
        "ls -al /boot 결과에서 grub, initrd 이미지, memtest 도구, vmlinuz 커널 파일을 확인하며, 커널이 운영체제 핵심 기능을 담는 작은 파일임을 설명한다.",
    )
    os05_etc = screen_figure(
        "os-basic",
        os05,
        32,
        "/etc 설정 파일 디렉토리",
        "/etc에는 네트워크, 보안 기능, 패키지 관리자, 웹 서버, 사용자 계정 등 시스템 프로세스의 각종 설정 파일이 모여 있다.",
    )
    os05_var_log = screen_figure(
        "os-basic",
        os05,
        36,
        "/var와 /var/log",
        "/var는 시스템 운용 중 생성되는 임시 데이터와 변동 데이터를 담고, /var/log에는 오류 분석과 운영 점검에 필요한 로그 파일이 저장된다.",
    )
    os05_ls = screen_figure(
        "os-basic",
        os05,
        50,
        "ls로 파일 목록 보기",
        "ls는 list의 약자이며, -l, -a, -al, -la, -a -l, *.txt 같은 옵션과 패턴으로 목록 표시 범위를 조정한다.",
    )
    os05_touch = screen_figure(
        "os-basic",
        os05,
        59,
        "touch와 숨김 파일",
        "touch는 원래 타임스탬프를 갱신하는 명령이지만, 없는 파일을 지정하면 0바이트 파일을 만들며, 점으로 시작하는 파일명은 숨김 파일이 된다.",
    )
    os05_cat = screen_figure(
        "os-basic",
        os05,
        73,
        "cat으로 파일 내용 보기",
        "cat은 concatenate에서 온 이름으로, 파일 입력을 표준 출력으로 연결해 내용을 보여 주며 -e, -n 옵션으로 숨은 문자나 줄 번호를 확인할 수 있다.",
    )
    os05_mkdir = screen_figure(
        "os-basic",
        os05,
        92,
        "mkdir, rmdir, rm -r",
        "mkdir은 디렉토리를 만들고 rmdir은 빈 디렉토리를 삭제하며, rm -r은 재귀 삭제라 위험하므로 사용할 때 주의해야 한다.",
    )
    os05_cd = screen_figure(
        "os-basic",
        os05,
        103,
        "cd와 특수 경로",
        "cd는 change directory의 약자이고, ., .., ~, -는 각각 현재 디렉토리, 부모 디렉토리, 홈 디렉토리, 이전 디렉토리를 의미한다.",
    )
    os05_cp_mv = screen_figure(
        "os-basic",
        os05,
        112,
        "cp와 mv",
        "cp는 파일과 디렉토리를 복사하고, mv는 파일을 이동하거나 이름을 바꾸며, 목적지가 디렉토리인지 파일명인지에 따라 결과가 달라진다.",
    )
    os05_link = screen_figure(
        "os-basic",
        os05,
        124,
        "하드링크와 심볼릭 링크",
        "ln은 링크를 만들며, 하드링크는 같은 파일 데이터를 가리키고, ln -s로 만드는 심볼릭 링크는 Windows 바로가기처럼 다른 파일 경로를 가리킨다.",
    )
    os05_inode = screen_figure(
        "os-basic",
        os05,
        134,
        "inode와 파일 메타데이터",
        "파일명은 실제 데이터 자체가 아니라 inode로 이어지는 이름이고, inode는 소유자, 크기, 시간, 권한, 데이터 블록 위치 같은 메타데이터를 가진다.",
    )
    os05_file = screen_figure(
        "os-basic",
        os05,
        135,
        "file 명령으로 파일 속성 확인",
        "file 명령은 대상이 텍스트, 디렉토리, 실행 파일, 심볼릭 링크인지 같은 파일 유형을 판별해 보여 준다.",
    )
    os05_man = screen_figure(
        "os-basic",
        os05,
        139,
        "man 매뉴얼",
        "man은 명령어 설명과 옵션을 확인하는 내장 매뉴얼이며, man ls, man file, man man처럼 명령어별 도움말을 확인할 수 있다.",
    )
    os05_vim_nano = screen_figure(
        "os-basic",
        os05,
        148,
        "Vim, vimtutor, Nano",
        "GUI가 없는 서버에서도 파일을 편집할 수 있도록 vi/vim과 nano를 익혀야 하며, vimtutor는 Vim 기본 조작을 단계적으로 연습하게 해 준다.",
    )
    os05_remote_demo = screen_figure(
        "os-basic",
        os05,
        158,
        "강의자용 원격 접속 실습 환경",
        "강사는 학생들이 화면을 보기 쉽도록 OpenSSH Server를 설치하고 원격 터미널로 접속해 글자를 크게 키운 환경에서 실습을 진행한다.",
    )
    os05_practice = screen_figure(
        "os-basic",
        os05,
        170,
        "실습: /etc/passwd 확인과 보호된 파일 삭제 실패",
        "실습에서는 cat /etc/passwd로 계정 파일을 보고, rm /etc/passwd가 권한 문제로 실패하는 것을 통해 시스템 파일 보호와 권한 개념을 미리 확인한다.",
    )
    os05_vimtutor = screen_figure(
        "os-basic",
        os05,
        174,
        "vimtutor 실행",
        "vimtutor는 이동, 종료, 저장 같은 Vim 기본 조작을 직접 따라 하도록 구성되어 있어 최소 한 번 끝까지 실행해 보는 것이 좋다.",
    )
    os05_nano = screen_figure(
        "os-basic",
        os05,
        177,
        "Nano 편집기와 Control 단축키",
        "Nano 화면 아래의 ^O, ^X 같은 표기는 Control 조합을 뜻하며, ^O는 저장, ^X는 종료처럼 기본 단축키를 화면에서 바로 확인할 수 있다.",
    )
    os06 = "운영체제 기초-06-사용자-계정-권한-관리"
    os06_user_philosophy = screen_figure(
        "os-basic",
        os06,
        2,
        "Windows와 Linux의 사용자 권한 철학",
        "개인용 PC에서 출발한 Windows와 달리, Unix 계열 철학을 이어받은 Linux는 여러 사용자가 한 시스템을 함께 쓰는 상황을 전제로 사용자와 관리자를 분리한다.",
    )
    os06_superuser = screen_figure(
        "os-basic",
        os06,
        16,
        "superuser와 sudo",
        "root는 최상위 관리자이며, Ubuntu는 root 직접 사용을 기본으로 권장하지 않고 필요한 순간에 sudo로 관리자 권한을 빌려 쓰게 한다.",
    )
    os06_whoami_id = screen_figure(
        "os-basic",
        os06,
        25,
        "whoami와 id로 현재 사용자 확인",
        "whoami는 현재 사용자 이름을, id는 UID·GID·보조 그룹을 보여 주며 설치 시 만든 user1이 sudo, adm, cdrom, netdev 등 여러 그룹에 속한 것을 확인한다.",
    )
    os06_sudo_id = screen_figure(
        "os-basic",
        os06,
        29,
        "sudo로 root 권한을 잠깐 빌리기",
        "sudo whoami와 sudo id를 실행하면 명령을 수행하는 그 순간만 root 권한이 적용되고, 명령이 끝나면 다시 일반 사용자로 돌아온다.",
    )
    os06_sudoers = screen_figure(
        "os-basic",
        os06,
        38,
        "/etc/sudoers와 sudo 권한",
        "/etc/sudoers는 누가 어떤 방식으로 sudo를 사용할 수 있는지 관리하는 민감한 설정 파일이므로 일반 사용자에게 바로 공개되지 않는다.",
    )
    os06_account_files = screen_figure(
        "os-basic",
        os06,
        44,
        "계정 관리 파일 세 가지",
        "/etc/passwd는 사용자 계정, /etc/shadow는 암호 해시와 암호 정책, /etc/group은 그룹 정보를 관리한다.",
    )
    os06_passwd_structure = screen_figure(
        "os-basic",
        os06,
        45,
        "/etc/passwd 필드 구조",
        "/etc/passwd 한 줄에는 사용자명, 암호 자리표시자 x, UID, GID, 이름/설명, 홈 디렉토리, 로그인 셸이 콜론으로 구분되어 들어간다.",
    )
    os06_uid_ranges = screen_figure(
        "os-basic",
        os06,
        51,
        "UID 범위와 시스템 계정",
        "root는 UID 0, 기본 시스템 계정은 낮은 번호, 실제 로그인 사용자는 보통 UID 1000부터 시작하며 nologin 셸을 가진 계정은 서비스용 계정으로 이해한다.",
    )
    os06_shadow_structure = screen_figure(
        "os-basic",
        os06,
        54,
        "/etc/shadow와 epoch 날짜",
        "shadow 파일은 암호 해시와 마지막 변경일, 최소·최대 사용일, 경고일, 만료일을 담고, 날짜 숫자는 1970년 1월 1일 UTC를 기준으로 계산한다.",
    )
    os06_hash_locked = screen_figure(
        "os-basic",
        os06,
        62,
        "잠긴 root와 해시 알고리즘",
        "shadow의 느낌표는 잠긴 계정을 뜻하고, 사용자 암호는 MD5, Blowfish, SHA-256, SHA-512 같은 단방향 해시 형식으로 저장된다.",
    )
    os06_adduser = screen_figure(
        "os-basic",
        os06,
        64,
        "adduser로 user2 생성",
        "사용자 계정 생성은 관리 작업이므로 sudo adduser user2처럼 관리자 권한으로 수행하며, 생성 뒤 /etc/passwd와 /etc/shadow에 새 항목이 반영된다.",
    )
    os06_chage_passwd = screen_figure(
        "os-basic",
        os06,
        72,
        "passwd와 chage",
        "passwd는 실제 암호를 바꾸고, chage는 암호 만료일·최소/최대 사용일·경고일 같은 암호 정책을 관리한다.",
    )
    os06_deluser = screen_figure(
        "os-basic",
        os06,
        79,
        "deluser와 홈 디렉토리",
        "deluser는 사용자를 삭제하지만 기본 옵션만으로는 홈 디렉토리까지 모두 지우지 않으며, 업무 파일 보존이나 백업 필요성을 고려해야 한다.",
    )
    os06_group_add = screen_figure(
        "os-basic",
        os06,
        88,
        "addgroup과 delgroup",
        "그룹도 계정처럼 별도 관리 대상이며, addgroup과 delgroup으로 그룹을 만들고 삭제할 수 있다.",
    )
    os06_usermod_group = screen_figure(
        "os-basic",
        os06,
        92,
        "usermod와 deluser로 그룹 구성 변경",
        "usermod -a -G sudo user2로 user2를 sudo 그룹에 추가하고, deluser user2 sudo로 해당 그룹에서 제거할 수 있다. 강의는 한국어 번역 문구가 헷갈릴 수 있음을 함께 지적한다.",
    )
    os06_permission_intro = screen_figure(
        "os-basic",
        os06,
        98,
        "ls -l 권한 표시",
        "ls -l 첫 열의 문자들은 파일 유형과 owner, group, other에 대한 rwx 권한을 보여 준다.",
    )
    os06_permission_numbers = screen_figure(
        "os-basic",
        os06,
        108,
        "rwx와 4·2·1 권한 계산",
        "read는 4, write는 2, execute는 1이며, 세 값을 더해 0부터 7까지의 권한 숫자를 만든다.",
    )
    os06_umask = screen_figure(
        "os-basic",
        os06,
        115,
        "umask와 기본 생성 권한",
        "파일은 기본 666, 디렉토리는 기본 777에서 umask로 막힌 비트를 제외해 실제 생성 권한이 결정된다.",
    )
    os06_chmod_numeric = screen_figure(
        "os-basic",
        os06,
        120,
        "chmod 숫자 모드",
        "chmod 777, chmod 700처럼 숫자 세 자리로 owner, group, other 권한을 한 번에 지정할 수 있다.",
    )
    os06_chmod_symbolic = screen_figure(
        "os-basic",
        os06,
        123,
        "chmod 문자 모드",
        "u+x, g-rw, o+rw처럼 대상 사용자 범주와 더하기·빼기 연산을 이용해 필요한 권한만 바꿀 수도 있다.",
    )
    os06_chown_chgrp = screen_figure(
        "os-basic",
        os06,
        127,
        "chown과 chgrp",
        "chown은 소유자를, chgrp는 그룹을 바꾸며, 실무에서는 chown user:group file 형태로 소유자와 그룹을 함께 바꾸는 일이 많다.",
    )
    os06_special_bits = screen_figure(
        "os-basic",
        os06,
        133,
        "특수 권한 SUID, SGID, Sticky bit",
        "강의는 SUID, SGID, Sticky bit를 맛보기로 소개하며, 기초 단계에서는 일반 rwx와 umask를 먼저 정확히 이해하는 것이 목표다.",
    )
    os06_practice_ls = screen_figure(
        "os-basic",
        os06,
        137,
        "실습: ls -l로 권한 확인",
        "실습은 큰 글씨 터미널에서 ls -l을 실행해 기존 파일과 디렉토리의 권한, 소유자, 그룹, 크기, 시간을 확인하는 것으로 시작한다.",
    )
    os06_practice_umask = screen_figure(
        "os-basic",
        os06,
        145,
        "실습: umask 변경 결과",
        "umask를 바꾸고 touch와 mkdir을 실행하면 새 파일과 새 디렉토리의 권한이 달라지는 것을 바로 확인할 수 있다.",
    )
    os06_practice_user2 = screen_figure(
        "os-basic",
        os06,
        149,
        "실습: user2 생성과 동시 로그인",
        "리눅스는 여러 사용자가 동시에 로그인할 수 있으므로, 강의는 user1 터미널과 user2 터미널을 나란히 열어 권한 차이를 보여 준다.",
    )
    os06_practice_user2_id = screen_figure(
        "os-basic",
        os06,
        156,
        "user2의 id와 홈 디렉토리",
        "새로 만든 user2는 sudo 같은 관리 그룹에 들어 있지 않고, 터미널에서 만든 계정이라 GUI 기본 폴더 구성이 user1과 다르게 보일 수 있다.",
    )
    os06_practice_file_write = screen_figure(
        "os-basic",
        os06,
        159,
        "echo 리다이렉션과 파일 권한",
        "echo hello > hello.txt로 파일에 내용을 쓰고, ls -l로 owner·group·other 권한이 실제 읽기·쓰기 가능 여부에 어떻게 영향을 주는지 확인한다.",
    )
    os06_practice_user2_write = screen_figure(
        "os-basic",
        os06,
        163,
        "user2의 읽기와 쓰기 실패",
        "other에게 읽기 권한만 있으면 user2는 cat으로 읽을 수 있지만, 쓰기 권한이 없으면 리다이렉션으로 파일을 덮어쓸 수 없다.",
    )
    os06_practice_dir_exec = screen_figure(
        "os-basic",
        os06,
        171,
        "디렉토리 execute 권한",
        "디렉토리에서 x는 실행 파일 실행이 아니라 그 디렉토리에 진입하고 경로를 통과할 수 있는 권한이다.",
    )
    os06_practice_dir_chmod = screen_figure(
        "os-basic",
        os06,
        175,
        "chmod로 디렉토리 접근 제어",
        "chmod 771, 775, 770처럼 디렉토리 권한을 바꾸며 other가 들어갈 수 있는지, 목록을 볼 수 있는지, 다시 막히는지를 실습으로 확인한다.",
    )
    os07 = "운영체제 기초-07-패키지-설치"
    os07_package_concept = screen_figure(
        "os-basic",
        os07,
        5,
        "패키지의 필요성",
        "소프트웨어를 소스 코드로 받아 각자 컴파일하는 부담을 줄이기 위해 배포판 환경에 맞게 미리 빌드된 묶음이 패키지다.",
    )
    os07_apt_structure = screen_figure(
        "os-basic",
        os07,
        18,
        "APT와 저장소 구조",
        "apt는 사용자의 명령을 받아 apt-get 같은 하위 도구와 로컬 캐시, 공개·사설 저장소를 연결해 패키지를 찾고 설치한다.",
    )
    os07_apt_commands = screen_figure(
        "os-basic",
        os07,
        25,
        "apt 기본 명령어",
        "apt update, list, install, search, show는 모두 실제 원격 저장소와 로컬 캐시의 관계를 이해해야 올바르게 사용할 수 있다.",
    )
    os07_remove_purge = screen_figure(
        "os-basic",
        os07,
        33,
        "remove와 purge의 차이",
        "apt remove는 실행 파일 중심으로 제거하고 설정·데이터를 남길 수 있으며, apt purge는 설정 파일까지 포함해 더 깨끗하게 제거한다.",
    )
    os07_dependency = screen_figure(
        "os-basic",
        os07,
        44,
        "의존성 패키지와 autoremove",
        "A 패키지를 설치하며 함께 깔린 B, C, D가 다른 패키지에서도 쓰일 수 있으므로, 더 이상 참조되지 않는 패키지만 autoremove로 정리한다.",
    )
    os07_install_upgrade = screen_figure(
        "os-basic",
        os07,
        46,
        "install, update, upgrade 구분",
        "install은 설치, update는 저장소 목록 갱신, upgrade는 실제 설치된 패키지 버전 올리기라는 점을 구분해야 한다.",
    )
    os07_gui_repo = screen_figure(
        "os-basic",
        os07,
        52,
        "Software & Updates 저장소 설정",
        "GUI의 Software & Updates 화면에서도 Ubuntu Software 탭을 통해 main, universe, restricted, multiverse 저장소 사용 여부를 조정할 수 있다.",
    )
    os07_security_updates = screen_figure(
        "os-basic",
        os07,
        60,
        "보안 업데이트와 업데이트 정책",
        "Updates 탭에서는 security, updates, backports 같은 업데이트 채널과 자동 업데이트 정책을 확인할 수 있다.",
    )
    os07_apt_files = screen_figure(
        "os-basic",
        os07,
        62,
        "/etc/apt와 패키지 캐시 위치",
        "/etc/apt/sources.list와 sources.list.d는 저장소 설정을 담고, /var/cache/apt/archives와 /var/lib/apt/lists는 다운로드·목록 캐시와 연결된다.",
    )
    os07_apt_update_demo = screen_figure(
        "os-basic",
        os07,
        66,
        "apt update 실습",
        "apt update는 원격 저장소에서 현재 패키지 목록을 받아 로컬 캐시를 갱신하지만, 설치된 프로그램 자체를 업그레이드하지는 않는다.",
    )
    os07_apt_upgrade_demo = screen_figure(
        "os-basic",
        os07,
        69,
        "apt upgrade 실습",
        "apt upgrade는 설치된 패키지 중 새 버전이 있는 항목을 실제로 업그레이드하며, apt list --upgradable로 대상 목록을 확인할 수 있다.",
    )
    os07_autoremove_demo = screen_figure(
        "os-basic",
        os07,
        74,
        "apt autoremove 실습",
        "apt autoremove는 더 이상 어떤 패키지도 필요로 하지 않는 의존성 패키지를 찾아 정리한다.",
    )
    os07_add_repository = screen_figure(
        "os-basic",
        os07,
        75,
        "add-apt-repository와 PPA",
        "개인 저장소나 PPA를 추가할 때 add-apt-repository를 사용할 수 있으며, 필요 없어진 저장소는 --remove로 제거한다.",
    )
    os07_lock_issue = screen_figure(
        "os-basic",
        os07,
        83,
        "apt 잠금 파일 문제",
        "백그라운드 업데이트 프로세스가 apt를 사용 중이면 lock 오류가 나며, 강의는 ps와 kill로 원인을 찾는 방식을 설명하되 신중한 사용을 강조한다.",
    )
    os07_dpkg = screen_figure(
        "os-basic",
        os07,
        85,
        "dpkg와 deb 패키지 직접 설치",
        "저장소가 아닌 .deb 파일을 직접 설치할 때는 dpkg -i를 사용할 수 있으며, Chrome 설치가 대표 예시다.",
    )
    os07_release_upgrade = screen_figure(
        "os-basic",
        os07,
        89,
        "배포판 업그레이드",
        "do-release-upgrade는 Ubuntu 배포판 자체를 올리는 명령이며, 수업 VM은 버전을 유지해야 하므로 실습 중 함부로 실행하지 않는다.",
    )
    os07_practice_openssh = screen_figure(
        "os-basic",
        os07,
        96,
        "실습: openssh-server 설치",
        "실습에서는 sudo apt install openssh-server -y로 패키지 설치와 의존 패키지 자동 설치 과정을 확인한다.",
    )
    os07_practice_tree = screen_figure(
        "os-basic",
        os07,
        98,
        "실습: tree 설치와 실행",
        "tree 패키지를 설치하면 디렉토리 구조를 계층형으로 출력할 수 있고, 설치 전후 명령 실행 결과가 달라진다.",
    )
    os07_practice_htop = screen_figure(
        "os-basic",
        os07,
        99,
        "실습: htop",
        "htop은 프로세스와 CPU·메모리 사용량을 터미널에서 보기 좋게 보여 주는 도구로, 패키지 설치 후 바로 실행해 볼 수 있다.",
    )
    os07_practice_sl = screen_figure(
        "os-basic",
        os07,
        105,
        "실습: sl 패키지",
        "sl은 실수로 ls를 잘못 친 사용자를 위한 장난성 패키지이며, 패키지 설치가 실제 명령 실행 가능 상태로 이어짐을 가볍게 확인하는 예시다.",
    )
    os08 = "운영체제 기초-08-데몬서비스-관리"
    os08_daemon_service = screen_figure(
        "os-basic",
        os08,
        4,
        "데몬과 서비스",
        "데몬은 사용자가 직접 제어하지 않아도 백그라운드에서 계속 동작하는 프로그램이고, 서비스는 사용자의 요청에 응답하는 서버 성격의 프로그램을 뜻한다.",
    )
    os08_service_legacy = screen_figure(
        "os-basic",
        os08,
        12,
        "구방식 service 명령",
        "System V init 시절에는 service 명령으로 데몬을 관리했지만, 현재 Ubuntu에서는 systemctl을 표준으로 사용한다.",
    )
    os08_systemctl_status = screen_figure(
        "os-basic",
        os08,
        16,
        "systemctl 기본 명령",
        "systemctl status, start, stop, restart로 서비스 상태 확인과 시작·중지·재시작을 수행하며, .service 접미사는 생략할 수 있다.",
    )
    os08_systemd_init = screen_figure(
        "os-basic",
        os08,
        20,
        "init에서 systemd로",
        "과거 init이 수행하던 서비스 실행과 부팅 관리 역할을 현재는 systemd가 맡고, 사용자는 systemctl로 제어한다.",
    )
    os08_targets = screen_figure(
        "os-basic",
        os08,
        24,
        "systemd target 구조",
        "고전적 runlevel 숫자는 systemd에서 poweroff, rescue, multi-user, graphical 같은 target 이름으로 표현된다.",
    )
    os08_units = screen_figure(
        "os-basic",
        os08,
        29,
        "systemd 유닛 종류",
        "systemd는 service뿐 아니라 socket, device, mount, automount, swap, target, path, timer, slice, scope 같은 다양한 unit을 관리한다.",
    )
    os08_journal = screen_figure(
        "os-basic",
        os08,
        33,
        "journalctl과 로그 레벨",
        "journalctl은 systemd journal 로그를 조회하며, 로그에는 emergency부터 debug까지 심각도 레벨이 있다.",
    )
    os08_ssh_status = screen_figure(
        "os-basic",
        os08,
        37,
        "SSH 서비스 상태 확인",
        "systemctl status ssh.service로 SSH 데몬이 loaded, active, running 상태인지 확인하고 최근 로그도 함께 볼 수 있다.",
    )
    os08_nginx_install = screen_figure(
        "os-basic",
        os08,
        41,
        "Nginx 설치와 의존 패키지",
        "sudo apt install nginx를 실행하면 Nginx와 함께 필요한 의존 패키지가 설치되며, Y/n 질문에서 대문자가 기본값이다.",
    )
    os08_nginx_status_active = screen_figure(
        "os-basic",
        os08,
        47,
        "Nginx active 상태",
        "Nginx 설치 뒤 systemctl status nginx를 보면 웹 서버가 active running 상태로 올라온 것을 확인할 수 있다.",
    )
    os08_curl_browser = screen_figure(
        "os-basic",
        os08,
        51,
        "curl localhost와 브라우저 확인",
        "curl localhost로 CLI에서 웹 서버 응답 HTML을 확인하고, 브라우저에서 localhost를 열어 같은 Nginx 기본 페이지를 볼 수 있다.",
    )
    os08_stop_permission = screen_figure(
        "os-basic",
        os08,
        57,
        "서비스 중지에는 관리자 권한 필요",
        "일반 사용자로 systemctl stop nginx를 실행하면 권한 문제가 나며, sudo systemctl stop nginx로 관리자 권한을 빌려야 한다.",
    )
    os08_nginx_inactive = screen_figure(
        "os-basic",
        os08,
        59,
        "Nginx inactive 상태",
        "서비스를 중지하면 status가 inactive로 바뀌고, curl localhost와 브라우저 요청도 응답을 받지 못한다.",
    )
    os08_start_again = screen_figure(
        "os-basic",
        os08,
        64,
        "Nginx 다시 시작",
        "sudo systemctl start nginx로 서비스를 다시 시작하면 active running으로 돌아오고 웹 응답도 다시 살아난다.",
    )
    os08_enable_disable = screen_figure(
        "os-basic",
        os08,
        69,
        "enable과 disable",
        "start/stop은 현재 실행 상태를 바꾸고, enable/disable은 부팅 시 자동 시작 여부를 바꾼다.",
    )
    os08_reboot_check = screen_figure(
        "os-basic",
        os08,
        72,
        "재부팅 후 서비스 상태 확인",
        "disable된 서비스는 현재 실행 중이어도 재부팅 후 자동으로 올라오지 않을 수 있으며, enable 여부와 active 여부를 구분해야 한다.",
    )
    os09 = "운영체제 기초-09-서버프로그램-설치-및-관리"
    os09_season2_outline = screen_figure(
        "os-basic",
        os09,
        11,
        "서버 프로그램 설치 및 관리 목차",
        "시즌2 첫 강의는 웹 서버, 파일 서버, 데이터베이스 서버를 설치하고 설정하며 서비스 관리와 연결해 보는 흐름으로 진행된다.",
    )
    os09_web_compare = screen_figure(
        "os-basic",
        os09,
        17,
        "Apache와 Nginx",
        "Apache는 오래된 역사와 전통을 가진 웹 서버이고, Nginx는 후발 주자지만 최근 널리 쓰이는 웹 서버로 소개된다.",
    )
    os09_apache_structure = screen_figure(
        "os-basic",
        os09,
        23,
        "Apache 설치와 설정 파일 구조",
        "Ubuntu에서는 apache2 패키지를 설치하고, /etc/apache2/apache2.conf와 sites-available, sites-enabled 구조로 사이트 설정을 관리한다.",
    )
    os09_sites_available = screen_figure(
        "os-basic",
        os09,
        27,
        "sites-available과 sites-enabled",
        "여러 가상 호스트 설정은 sites-available에 두고, 실제 활성화할 사이트는 sites-enabled의 심볼릭 링크로 연결하는 구조를 사용한다.",
    )
    os09_apache_default = screen_figure(
        "os-basic",
        os09,
        36,
        "Apache 기본 페이지",
        "apache2 설치 뒤 서비스가 실행되면 브라우저에서 Apache2 Ubuntu Default Page를 확인할 수 있다.",
    )
    os09_nginx_structure = screen_figure(
        "os-basic",
        os09,
        38,
        "Nginx 설정 파일 구조",
        "Nginx도 /etc/nginx/nginx.conf와 sites-available, sites-enabled를 이용하며, 기본 문서 루트는 /var/www/html이다.",
    )
    os09_vm_network = screen_figure(
        "os-basic",
        os09,
        45,
        "VirtualBox 네트워크 확인",
        "강사는 Windows 호스트에서 Ubuntu VM에 접속하기 위해 NAT와 호스트 전용 어댑터 구성을 확인하고, 접속 IP가 환경마다 다를 수 있음을 설명한다.",
    )
    os09_nginx_status = screen_figure(
        "os-basic",
        os09,
        49,
        "Nginx 설치와 상태 확인",
        "sudo apt install nginx 후 systemctl status nginx로 서비스 상태를 확인하고, 브라우저에서 기본 페이지가 뜨는지 점검한다.",
    )
    os09_nginx_conf = screen_figure(
        "os-basic",
        os09,
        56,
        "nginx.conf의 include 구조",
        "nginx.conf는 sites-enabled 안의 설정 파일을 include하여 활성화된 가상 호스트 설정을 불러온다.",
    )
    os09_nginx_default = screen_figure(
        "os-basic",
        os09,
        70,
        "Nginx default 사이트 설정",
        "default 설정 파일의 server 블록에는 listen 포트, root 디렉토리, index 파일, location 설정이 들어간다.",
    )
    os09_symlink_activate = screen_figure(
        "os-basic",
        os09,
        78,
        "심볼릭 링크로 사이트 활성화",
        "sites-available의 white school 설정을 sites-enabled에 ln -s로 연결해 새 가상 호스트를 활성화한다.",
    )
    os09_port_conflict = screen_figure(
        "os-basic",
        os09,
        83,
        "80 포트 중복 오류",
        "default와 새 설정이 모두 80 포트를 listen하면 Nginx 재시작이 실패하고, status와 로그에서 bind 오류를 확인할 수 있다.",
    )
    os09_nginx_test = screen_figure(
        "os-basic",
        os09,
        90,
        "nginx -t로 설정 검사",
        "sudo nginx -t는 재시작 전 설정 문법과 포트 충돌 같은 문제를 미리 확인하는 데 사용된다.",
    )
    os09_custom_page = screen_figure(
        "os-basic",
        os09,
        98,
        "새 웹 루트와 Hello 페이지",
        "/var/www/html 아래 새 디렉토리와 index.html을 만들고 root를 바꾸면 8000번 포트에서 별도 페이지를 서비스할 수 있다.",
    )
    os09_ftp_intro = screen_figure(
        "os-basic",
        os09,
        100,
        "vsftpd 파일 서버",
        "FTP 서버는 vsftpd 패키지로 설치하며, 설정은 /etc/vsftpd.conf 단일 파일에서 관리한다.",
    )
    os09_filezilla = screen_figure(
        "os-basic",
        os09,
        109,
        "FileZilla FTP 클라이언트",
        "Ubuntu와 Windows에는 ftp CLI 클라이언트가 있고, GUI 클라이언트로 FileZilla 같은 서드파티 도구도 사용할 수 있다.",
    )
    os09_ftp_config_theory = screen_figure(
        "os-basic",
        os09,
        117,
        "FTP 익명 접속, write_enable, chroot",
        "vsftpd.conf에서 anonymous_enable, local_enable, write_enable, chroot_local_user, allow_writeable_chroot 같은 설정으로 접속과 권한을 제어한다.",
    )
    os09_vsftpd_status = screen_figure(
        "os-basic",
        os09,
        123,
        "vsftpd 설치와 상태",
        "sudo apt install vsftpd 후 systemctl status vsftpd로 파일 서버가 active running 상태인지 확인한다.",
    )
    os09_ftp_local_login = screen_figure(
        "os-basic",
        os09,
        128,
        "Ubuntu 내부 FTP 접속",
        "Ubuntu 안에서 ftp 127.0.0.1로 접속하면 현재 사용자 계정이 기본값으로 들어가고 홈 디렉토리 파일을 볼 수 있다.",
    )
    os09_ftp_windows_get = screen_figure(
        "os-basic",
        os09,
        134,
        "Windows에서 FTP 다운로드",
        "Windows 클라이언트에서는 VM의 원격 IP로 접속하고 get hello.txt로 서버의 파일을 내려받는다.",
    )
    os09_ftp_put_denied = screen_figure(
        "os-basic",
        os09,
        140,
        "FTP 업로드 권한 거부",
        "기본 설정에서는 쓰기 권한이 꺼져 있어 put myFile.txt 같은 업로드 시도가 permission denied로 실패한다.",
    )
    os09_write_enable = screen_figure(
        "os-basic",
        os09,
        146,
        "write_enable 활성화",
        "vsftpd.conf에서 write_enable을 켜고 서비스를 재시작하면 FTP 업로드가 가능해진다.",
    )
    os09_chroot_config = screen_figure(
        "os-basic",
        os09,
        153,
        "chroot로 홈 디렉토리에 가두기",
        "chroot_local_user=YES와 allow_writeable_chroot=YES를 설정하면 사용자가 FTP 접속 후 상위 디렉토리로 벗어나지 못하게 할 수 있다.",
    )
    os09_ftp_final = screen_figure(
        "os-basic",
        os09,
        158,
        "FTP 다운로드·업로드·chroot 확인",
        "설정 적용 후 다운로드와 업로드가 가능하고, cd ..로 상위 디렉토리 이동을 시도해도 홈 밖으로 벗어나지 않는 것을 확인한다.",
    )
    os09_db_types = screen_figure(
        "os-basic",
        os09,
        160,
        "대표 데이터베이스 서버",
        "DB 서버에는 MySQL, MariaDB, MSSQL, PostgreSQL 등이 있으며 실습에서는 MySQL을 사용한다.",
    )
    os09_mysql_theory = screen_figure(
        "os-basic",
        os09,
        161,
        "MySQL 설치와 secure installation",
        "mysql-server 패키지를 설치하고, 필요하면 mysql_secure_installation으로 암호 정책과 기본 보안 설정을 조정할 수 있다.",
    )
    os09_mysql_status = screen_figure(
        "os-basic",
        os09,
        167,
        "MySQL 상태와 최초 접속",
        "Ubuntu 18.04 이후 흐름에서는 systemctl status mysql로 상태를 보고, 최초 관리는 sudo mysql로 접속한다.",
    )
    os09_mysql_install_demo = screen_figure(
        "os-basic",
        os09,
        176,
        "MySQL 설치 실습",
        "mysql-server 설치 과정에서는 서버뿐 아니라 클라이언트와 여러 의존 패키지가 함께 설치된다.",
    )
    os09_mysql_console = screen_figure(
        "os-basic",
        os09,
        184,
        "MySQL 콘솔과 DB 생성",
        "sudo mysql로 접속한 뒤 show databases, create database, create user, grant privileges 같은 SQL 명령을 실행한다.",
    )
    os09_mysql_user_grant = screen_figure(
        "os-basic",
        os09,
        188,
        "DB 사용자와 권한 부여",
        "MySQL은 OS 계정과 별도의 DB 사용자를 관리하며, 특정 데이터베이스에 대한 권한을 grant로 부여하고 flush privileges로 적용한다.",
    )
    os09_mysql_table = screen_figure(
        "os-basic",
        os09,
        191,
        "테이블 생성과 조회",
        "권한을 받은 user1으로 접속해 데이터베이스를 선택하고 테이블을 만들며, show tables와 select로 결과를 확인한다.",
    )
    os10 = "운영체제 기초-10-개발환경-구축하기"
    os10_outline = screen_figure(
        "os-basic",
        os10,
        2,
        "개발 환경 구축의 범위",
        "강의는 언어별 도구, 런타임, 버전 관리, 가상 환경, IDE까지 개발 환경 구축에서 확인해야 할 범위를 먼저 정리한다.",
    )
    os10_c_tools = screen_figure(
        "os-basic",
        os10,
        5,
        "C 개발 환경과 binutils",
        "build-essential은 gcc, g++, make 같은 기본 빌드 도구를 제공하고, binutils는 ld, ar, objdump 같은 바이너리 분석 도구를 제공한다.",
    )
    os10_build_install = screen_figure(
        "os-basic",
        os10,
        11,
        "build-essential 설치와 버전 확인",
        "터미널에서 build-essential과 binutils를 설치하고 gcc, g++, make 버전을 확인해 C 개발 도구가 준비되었는지 검증한다.",
    )
    os10_hello_code = screen_figure(
        "os-basic",
        os10,
        15,
        "hello.c 작성",
        "vim으로 hello.c를 열어 stdio.h를 포함하고 hello world를 출력하는 가장 기본적인 C 프로그램을 작성한다.",
    )
    os10_compile_run = screen_figure(
        "os-basic",
        os10,
        16,
        "gcc 컴파일과 실행",
        "gcc hello.c -o hello로 실행 파일을 만들고 ./hello로 현재 디렉토리의 바이너리를 실행한다.",
    )
    os10_objdump = screen_figure(
        "os-basic",
        os10,
        19,
        "objdump와 ELF 정보 확인",
        "objdump와 readelf 같은 도구로 실행 파일의 어셈블리 코드와 ELF 헤더 정보를 살펴보며 이후 리버싱·악성코드 분석 수업과 연결한다.",
    )
    os10_python_versions = screen_figure(
        "os-basic",
        os10,
        21,
        "Ubuntu 버전별 Python 기본 제공",
        "Ubuntu 16.04와 18.04는 Python 2와 3이 함께 있었지만, Ubuntu 20.04부터는 Python 2가 기본 제공되지 않고 Python 3 중심으로 바뀐다.",
    )
    os10_anaconda_plan = screen_figure(
        "os-basic",
        os10,
        24,
        "Anaconda 설치 방법",
        "Anaconda는 Ubuntu 공식 apt 패키지로 설치하는 도구가 아니라 공식 사이트에서 다운로드하거나 curl로 스크립트를 받아 bash로 실행한다.",
    )
    os10_virtualbox_resize = screen_figure(
        "os-basic",
        os10,
        34,
        "VirtualBox 가상 디스크 크기 증설",
        "VirtualBox의 가상 미디어 관리자에서 VM 디스크 크기를 늘리면 물리적인 가상 디스크 파일 크기는 커지지만, 게스트 OS의 파티션은 아직 그대로다.",
    )
    os10_partition_theory = screen_figure(
        "os-basic",
        os10,
        46,
        "파티션과 파일 시스템 확장의 구분",
        "가상 디스크를 늘린 뒤에는 extended partition, logical partition, 파일 시스템을 순서대로 확장해야 실제 df 결과가 늘어난다.",
    )
    os10_growpart_slide = screen_figure(
        "os-basic",
        os10,
        37,
        "growpart와 resize2fs 명령",
        "cloud-guest-utils의 growpart로 파티션을 확장하고 resize2fs로 ext 파일 시스템 크기를 늘리는 명령 순서를 정리한다.",
    )
    os10_disk_terminal = screen_figure(
        "os-basic",
        os10,
        64,
        "디스크 확장 결과 확인",
        "lsblk와 df -h로 20GB까지 늘어난 파티션과 사용 가능한 공간을 확인한 뒤 Anaconda 설치를 진행할 수 있음을 확인한다.",
    )
    os10_anaconda_download = screen_figure(
        "os-basic",
        os10,
        68,
        "Anaconda 다운로드 완료",
        "브라우저에서 Anaconda 설치 스크립트를 내려받고, 같은 파일을 curl로도 받을 수 있음을 설명한다.",
    )
    os10_anaconda_install = screen_figure(
        "os-basic",
        os10,
        76,
        "Anaconda 설치 스크립트 실행",
        "bash로 설치 스크립트를 실행하면 라이선스 확인, yes 입력, 설치 경로 선택, conda 초기화 여부 질문이 순서대로 나온다.",
    )
    os10_conda_init = screen_figure(
        "os-basic",
        os10,
        84,
        "conda init과 셸 재로그인",
        "conda init 또는 source로 셸 환경을 초기화하고 다시 로그인하면 conda 명령과 base 환경을 사용할 수 있다.",
    )
    os10_conda_env = screen_figure(
        "os-basic",
        os10,
        88,
        "conda 가상 환경 생성과 활성화",
        "conda create로 원하는 Python 버전의 환경을 만들고 conda activate로 프로젝트별 환경을 전환한다.",
    )
    os10_jupyter_options = screen_figure(
        "os-basic",
        os10,
        91,
        "Jupyter Notebook 실행 옵션",
        "Jupyter Notebook은 로컬 브라우저 실행뿐 아니라 --ip=0.0.0.0, --no-browser 옵션으로 원격 접속용 서버처럼 실행할 수 있다.",
    )
    os10_jupyter_token = screen_figure(
        "os-basic",
        os10,
        102,
        "Jupyter 토큰 로그인",
        "외부 브라우저에서 접속하면 토큰을 입력하거나 토큰이 포함된 URL로 접속해 Notebook 화면에 들어갈 수 있다.",
    )
    os10_jupyter_service = screen_figure(
        "os-basic",
        os10,
        106,
        "Jupyter Notebook systemd 서비스 예시",
        "앞서 배운 systemd 지식을 응용해 Jupyter Notebook도 서비스 파일로 등록하고 start, stop, enable로 관리할 수 있다.",
    )
    os10_java_jre_jdk = screen_figure(
        "os-basic",
        os10,
        108,
        "Java JRE와 JDK 설치",
        "default-jre는 Java 프로그램 실행 환경이고 default-jdk는 javac 컴파일러까지 포함한 개발 키트다.",
    )
    os10_java_where = screen_figure(
        "os-basic",
        os10,
        114,
        "which와 whereis로 실행 파일 위치 확인",
        "which는 실제 실행될 바이너리 위치를 보여 주고, whereis는 관련 파일의 여러 위치를 넓게 찾아 준다.",
    )
    os10_update_alternatives = screen_figure(
        "os-basic",
        os10,
        118,
        "update-alternatives로 버전 관리",
        "여러 Python 또는 Java 버전을 등록하고 우선순위와 선택 메뉴를 통해 기본 실행 버전을 전환할 수 있다.",
    )
    os10_docker_install_plan = screen_figure(
        "os-basic",
        os10,
        125,
        "Docker 설치 방법",
        "Ubuntu 패키지의 docker.io를 설치할 수도 있고, Docker 공식 저장소를 추가해 더 최신 버전을 설치할 수도 있다.",
    )
    os10_docker_permissions = screen_figure(
        "os-basic",
        os10,
        130,
        "Docker 그룹 권한과 데이터 경로",
        "sudo 없이 docker를 쓰려면 사용자를 docker 그룹에 추가해야 하며, 이미지와 컨테이너는 기본적으로 /var/lib/docker 아래 쌓인다.",
    )
    os10_docker_run = screen_figure(
        "os-basic",
        os10,
        146,
        "docker hello-world 실행",
        "docker run hello-world는 이미지 다운로드와 컨테이너 실행이 정상 동작하는지 확인하는 가장 기본적인 테스트다.",
    )
    os10_docker_storage = screen_figure(
        "os-basic",
        os10,
        151,
        "Docker 저장 경로 변경 개념",
        "실무에서는 별도 디스크를 /data 같은 위치에 마운트하고 daemon.json의 data-root로 Docker 저장 위치를 옮길 수 있다.",
    )
    os10_summary = screen_figure(
        "os-basic",
        os10,
        152,
        "개발 환경 구축 요약",
        "필요한 도구 검색, apt 또는 공식 사이트 설치, 설정 파일 수정, 서비스 재시작까지가 개발 환경 구축의 공통 흐름이다.",
    )
    os11 = "운영체제 기초-11-배시-쉘-프로그래밍"
    os11_shell_diagram = screen_figure(
        "os-basic",
        os11,
        2,
        "셸의 위치와 역할",
        "셸은 사용자의 명령을 입력받아 시스템 콜을 통해 운영체제와 상호작용하고, 실행 결과를 다시 사용자에게 보여 주는 인터페이스다.",
    )
    os11_shell_types = screen_figure(
        "os-basic",
        os11,
        5,
        "대표 셸 종류와 기본 로그인 셸",
        "Bourne shell, Korn shell, C shell, Bash, Zsh 같은 여러 셸이 있고, Ubuntu 실습 사용자는 기본적으로 /bin/bash를 사용한다.",
    )
    os11_ohmyzsh = screen_figure(
        "os-basic",
        os11,
        10,
        "Oh My Zsh 예시",
        "Zsh와 Oh My Zsh는 Git 상태와 색상 정보를 풍부하게 보여 주는 개발자 친화적 셸 환경이지만, 강의 실습은 기본 Bash로 진행한다.",
    )
    os11_prompt_ps1 = screen_figure(
        "os-basic",
        os11,
        18,
        "프롬프트와 PS1 구조",
        "PS1은 사용자명, 호스트명, 현재 디렉토리, 색상 코드를 조합해 Bash 프롬프트 표시 방식을 결정한다.",
    )
    os11_ansi_codes = screen_figure(
        "os-basic",
        os11,
        24,
        "ANSI escape code와 색상",
        "프롬프트의 복잡한 숫자와 대괄호는 ANSI escape code로, 터미널 글자 색상과 스타일을 바꾸는 데 쓰인다.",
    )
    os11_echo_variables = screen_figure(
        "os-basic",
        os11,
        29,
        "echo와 변수 출력",
        "echo는 문자열과 변수 값을 출력하는 가장 기본적인 명령이며, 변수 앞에 $를 붙이면 저장된 값을 참조한다.",
    )
    os11_redirection_slide = screen_figure(
        "os-basic",
        os11,
        49,
        "리디렉션과 표준 출력·표준 에러",
        ">와 >>는 표준 출력을 파일로 보내고, 2>와 2>&1은 표준 에러를 별도로 또는 표준 출력과 함께 다루는 방법이다.",
    )
    os11_stdin_slide = screen_figure(
        "os-basic",
        os11,
        58,
        "표준 입력과 cat",
        "< 리디렉션은 파일 내용을 표준 입력으로 넘기며, cat처럼 표준 입력을 읽는 프로그램과 echo처럼 읽지 않는 프로그램의 차이를 확인한다.",
    )
    os11_pipe_slide = screen_figure(
        "os-basic",
        os11,
        64,
        "파이프와 프로세스 연결",
        "파이프는 한 명령의 표준 출력을 다음 명령의 표준 입력으로 넘기며, grep, wc, sort, awk, sed 같은 도구와 자주 결합된다.",
    )
    os11_history_slide = screen_figure(
        "os-basic",
        os11,
        70,
        "history와 명령 재실행",
        "history는 최근 명령을 저장하고, !번호와 !! 문법으로 과거 명령 또는 직전 명령을 다시 실행할 수 있게 한다.",
    )
    os11_path_slide = screen_figure(
        "os-basic",
        os11,
        76,
        "PATH 환경변수",
        "PATH는 명령어 이름만 입력했을 때 Bash가 실행 파일을 찾기 위해 순서대로 검색하는 디렉토리 목록이다.",
    )
    os11_which_slide = screen_figure(
        "os-basic",
        os11,
        80,
        "which로 실행 파일 위치 확인",
        "which는 PATH 검색 결과 실제로 실행될 바이너리 경로를 보여 주며, Anaconda 설치 여부에 따라 python 경로가 달라질 수 있다.",
    )
    os11_env_table = screen_figure(
        "os-basic",
        os11,
        81,
        "주요 환경변수 표",
        "PATH, PWD, USER, HOME, LANG, LANGUAGE, PS1, LS_COLORS처럼 Bash와 사용자 환경을 구성하는 대표 환경변수를 정리한다.",
    )
    os11_alias_slide = screen_figure(
        "os-basic",
        os11,
        85,
        "alias로 긴 명령 줄이기",
        "alias는 cd .. 같은 자주 쓰는 명령을 .. 또는 ... 같은 짧은 이름으로 줄여 반복 입력을 편하게 만든다.",
    )
    os11_bash_startup = screen_figure(
        "os-basic",
        os11,
        89,
        "Bash 시작 파일과 .bashrc",
        "Bash는 /etc/profile, /etc/bash.bashrc, ~/.profile, ~/.bashrc, ~/.bash_logout 같은 시작·종료 파일을 읽어 환경을 구성한다.",
    )
    os11_find_slide = screen_figure(
        "os-basic",
        os11,
        94,
        "find 기본 검색",
        "find는 파일 이름, 경로, 크기, 시간, 타입 같은 조건으로 파일을 찾고, -exec와 함께 후속 명령을 실행할 수 있다.",
    )
    os11_find_advanced = screen_figure(
        "os-basic",
        os11,
        100,
        "find 고급 조건과 -exec",
        "find는 루트부터 특정 크기 이상 파일을 찾거나, 이름 조건과 grep을 결합해 파일 내부 내용까지 검색할 수 있다.",
    )
    os11_grep_slide = screen_figure(
        "os-basic",
        os11,
        104,
        "grep 문자열 검색",
        "grep은 파일이나 표준 입력에서 특정 문자열 또는 패턴을 찾아내며, 보안 로그에서 IP나 계정명을 필터링할 때 자주 쓰인다.",
    )
    os11_awk_slide = screen_figure(
        "os-basic",
        os11,
        108,
        "awk 컬럼 처리",
        "awk는 공백이나 구분자로 나뉜 컬럼 중 원하는 필드를 골라 출력하고 재배치할 수 있다.",
    )
    os11_sed_slide = screen_figure(
        "os-basic",
        os11,
        116,
        "sed 스트림 편집",
        "sed는 입력 스트림에서 특정 패턴을 찾아 다른 문자열로 바꾸는 search and replace 작업에 사용된다.",
    )
    os11_redirect_terminal = screen_figure(
        "os-basic",
        os11,
        127,
        "리디렉션 실습 결과",
        "터미널 실습에서 정상 출력과 에러 출력이 각각 파일로 들어가는 방식과 2>/dev/null로 에러를 버리는 방식을 확인한다.",
    )
    os11_bashrc_anaconda = screen_figure(
        "os-basic",
        os11,
        149,
        ".bashrc와 Anaconda 초기화 코드",
        "Anaconda 폴더를 삭제해도 ~/.bashrc의 conda 초기화 코드가 남아 있으면 셸 시작 때 계속 실행되므로 함께 정리해야 한다.",
    )
    os11_script_shebang = screen_figure(
        "os-basic",
        os11,
        154,
        "셸 스크립트 첫 줄과 실행 권한",
        "셸 스크립트는 보통 #!/bin/bash shebang으로 시작하며, 직접 실행하려면 chmod +x로 실행 권한을 부여해야 한다.",
    )
    os11_script_args = screen_figure(
        "os-basic",
        os11,
        164,
        "스크립트 인자 변수",
        "$0은 스크립트 파일명, $1과 $2는 첫 번째와 두 번째 인자, $#은 인자 개수처럼 실행 시 전달된 값을 스크립트에서 사용할 수 있다.",
    )
    os11_number_script = screen_figure(
        "os-basic",
        os11,
        166,
        "for와 if를 이용한 숫자 출력",
        "for 반복문으로 숫자를 순회하고 if 조건문과 나머지 연산으로 짝수만 출력하는 셸 스크립트 예시를 보여 준다.",
    )
    os11_complex_script = screen_figure(
        "os-basic",
        os11,
        173,
        "find, sort, while을 결합한 실무형 스크립트",
        "디렉토리와 확장자를 인자로 받아 파일을 찾고, 크기순으로 정렬한 뒤, while read 루프로 결과를 포맷팅하는 종합 예시다.",
    )
    os11_script_practice = screen_figure(
        "os-basic",
        os11,
        190,
        "셸 스크립트 실습 결과",
        "user.sh, number.sh, find_large.sh 같은 스크립트를 직접 작성하고 실행하며 권한, 인자, 반복문, 조건문의 동작을 확인한다.",
    )
    os12 = "운영체제 기초-12-시스템-운영-및-모니터링"
    os12_scope = screen_figure(
        "os-basic",
        os12,
        3,
        "시스템 운영과 모니터링 범위",
        "사용자 접속 상태, 로그인 성공·실패 기록, 셸 히스토리, 인증 로그를 통해 누가 시스템을 사용하고 있는지 확인하는 흐름을 먼저 잡는다.",
    )
    os12_process_scope = screen_figure(
        "os-basic",
        os12,
        8,
        "프로세스 모니터링 범위",
        "job control, ps와 /proc, 프로세스 트리, signal, lsof, fuser, gcore, strace, ltrace처럼 실행 중인 프로그램을 관찰하고 제어하는 도구들을 묶어 소개한다.",
    )
    os12_network_scope = screen_figure(
        "os-basic",
        os12,
        10,
        "네트워크 모니터링 범위",
        "ifconfig, ping, arp, route, ip, netstat, nmap, nc, tcpdump와 ntopd, iftop, iptraf, nethogs, bmon 같은 네트워크 관찰 도구의 큰 목록을 보여 준다.",
    )
    os12_users_who_w = screen_figure(
        "os-basic",
        os12,
        18,
        "users, who, w 명령 실습",
        "users는 접속 사용자 이름만, who는 사용자·터미널·접속 시간·접속 위치를, w는 부하·idle·JCPU·PCPU·현재 명령까지 더 자세히 보여 준다.",
    )
    os12_tty_pts = screen_figure(
        "os-basic",
        os12,
        20,
        "TTY와 PTS의 차이",
        "TTY는 물리적 또는 가상 콘솔 터미널을, PTS는 SSH나 GUI 터미널처럼 pseudo terminal을 통해 연결된 세션을 의미한다.",
    )
    os12_wall_write = screen_figure(
        "os-basic",
        os12,
        39,
        "wall과 write 메시지 전송",
        "유지보수나 종료 공지를 위해 wall은 로그인한 모든 사용자에게, write는 특정 사용자와 터미널에 메시지를 보낼 수 있다.",
    )
    os12_last = screen_figure(
        "os-basic",
        os12,
        48,
        "last와 로그인 성공 기록",
        "last는 /var/log/wtmp에 저장된 로그인 성공, 재부팅, 세션 유지·종료 기록을 읽어 최근 접속 이력을 보여 준다.",
    )
    os12_lastb = screen_figure(
        "os-basic",
        os12,
        52,
        "lastb와 로그인 실패 기록",
        "lastb는 /var/log/btmp에 저장된 로그인 실패 기록을 보여 주며, 클라우드 서버에서 admin, root 같은 계정으로 반복되는 무차별 대입 시도를 확인할 때 유용하다.",
    )
    os12_history_auth = screen_figure(
        "os-basic",
        os12,
        73,
        "history와 인증 로그",
        "사용자 홈의 .bash_history와 /var/log/auth.log는 사용자가 실행한 명령, sudo, SSH, 인증 이벤트를 추적하는 보조 단서가 된다.",
    )
    os12_jobs = screen_figure(
        "os-basic",
        os12,
        80,
        "foreground와 background job",
        "Ctrl+Z로 foreground 작업을 잠시 멈추고, bg와 fg로 background와 foreground 사이를 오가며, jobs로 현재 셸의 작업 목록을 확인한다.",
    )
    os12_jobs_practice = screen_figure(
        "os-basic",
        os12,
        96,
        "tail 명령으로 job control 실습",
        "tail -f로 로그를 계속 출력하다가 Ctrl+Z, bg, jobs, fg를 차례로 사용해 같은 프로세스가 셸의 제어 상태만 바꾸는 과정을 확인한다.",
    )
    os12_ps_states = screen_figure(
        "os-basic",
        os12,
        99,
        "ps 출력과 프로세스 상태",
        "ps는 PID, TTY, TIME, CMD와 함께 D, R, S, T, Z 같은 프로세스 상태 문자를 보여 주며, 상태 문자는 실행·대기·정지·좀비 상태를 읽는 단서다.",
    )
    os12_ps_aux = screen_figure(
        "os-basic",
        os12,
        100,
        "ps aux 옵션",
        "a는 전체 사용자 프로세스, u는 사용자 중심 상세 정보, x는 터미널에 붙지 않은 데몬 프로세스까지 포함하므로 서버 운영에서 자주 쓰인다.",
    )
    os12_proc = screen_figure(
        "os-basic",
        os12,
        110,
        "/proc/<pid> 파일 시스템",
        "/proc는 메모리에 존재하는 특수 파일 시스템이며, 각 PID 디렉토리의 cmdline, cwd, environ, exe, fd, stat, status로 실행 중 프로세스를 파일처럼 관찰한다.",
    )
    os12_proc_practice = screen_figure(
        "os-basic",
        os12,
        115,
        "nginx 프로세스의 /proc 확인",
        "nginx PID를 기준으로 /proc/<pid>/cmdline과 fd를 확인해 어떤 명령으로 실행됐고 어떤 파일·소켓을 열고 있는지 살펴본다.",
    )
    os12_pstree = screen_figure(
        "os-basic",
        os12,
        117,
        "pstree와 프로세스 트리",
        "pstree는 프로세스의 부모·자식 관계를 트리로 보여 주며, ps f 옵션도 비슷하게 프로세스 관계를 계층적으로 표시할 수 있다.",
    )
    os12_kill = screen_figure(
        "os-basic",
        os12,
        120,
        "kill과 signal",
        "kill은 프로세스를 무조건 죽이는 명령이 아니라 SIGHUP, SIGINT, SIGQUIT, SIGTERM, SIGKILL 같은 signal을 보내는 명령이다.",
    )
    os12_lsof = screen_figure(
        "os-basic",
        os12,
        123,
        "lsof로 열린 파일 확인",
        "lsof는 프로세스가 열고 있는 파일, 네트워크 소켓, 사용자별 열린 자원 정보를 보여 주며 특정 파일을 누가 잡고 있는지 찾을 때 유용하다.",
    )
    os12_htop = screen_figure(
        "os-basic",
        os12,
        136,
        "htop과 프로세스 종료 실습",
        "htop 같은 대화형 도구를 실행한 뒤 ps aux와 grep으로 PID를 찾고 kill -9 또는 killall로 종료하는 흐름을 실습한다.",
    )
    os12_strace = screen_figure(
        "os-basic",
        os12,
        141,
        "strace 시스템 콜 트레이싱",
        "strace는 whoami나 ls 같은 명령이 실행되는 동안 커널에 요청하는 open, read, write 등 시스템 콜과 반환값을 추적한다.",
    )
    os12_ltrace = screen_figure(
        "os-basic",
        os12,
        142,
        "ltrace 라이브러리 콜 트레이싱",
        "ltrace는 프로그램이 malloc, printf 같은 라이브러리 함수를 호출하는 과정을 추적해 시스템 콜보다 위 단계의 동작을 볼 수 있게 한다.",
    )
    os12_ifconfig = screen_figure(
        "os-basic",
        os12,
        146,
        "ifconfig 네트워크 인터페이스 설정",
        "ifconfig는 인터페이스 확인, up/down 전환, IP 주소 부여에 쓰였고, 고전적인 eth0 대신 enp0s3처럼 슬롯 기반 이름을 볼 수 있다.",
    )
    os12_network_manager = screen_figure(
        "os-basic",
        os12,
        151,
        "NetworkManager 상태와 GUI 설정",
        "Ubuntu Desktop에서는 NetworkManager가 GUI와 백그라운드에서 인터페이스를 관리하므로 CLI 설정과 충돌할 수 있고 systemctl로 상태를 확인한다.",
    )
    os12_netplan = screen_figure(
        "os-basic",
        os12,
        157,
        "netplan 설정 파일",
        "/etc/netplan/ 아래 YAML 파일은 renderer를 NetworkManager 또는 networkd로 지정하고, 주소·게이트웨이·DNS 같은 부팅 시 네트워크 설정을 선언한다.",
    )
    os12_arp = screen_figure(
        "os-basic",
        os12,
        162,
        "arp로 인접 호스트 확인",
        "arp는 같은 LAN 구간의 IP 주소와 MAC 주소 매핑을 확인하는 도구이며, ARP spoofing 같은 네트워크 공격을 이해하는 기초가 된다.",
    )
    os12_route = screen_figure(
        "os-basic",
        os12,
        164,
        "route와 라우팅 테이블",
        "route는 default gateway와 정적 라우팅 항목을 확인·추가·삭제해 패킷이 어느 네트워크로 나갈지 결정하는 표를 다룬다.",
    )
    os12_ip = screen_figure(
        "os-basic",
        os12,
        166,
        "ip 명령과 PBR",
        "ip는 link, addr, route, rule 같은 하위 명령으로 인터페이스, 주소, 라우팅, 정책 기반 라우팅까지 다루는 현대적인 네트워크 관리 도구다.",
    )
    os12_netstat = screen_figure(
        "os-basic",
        os12,
        171,
        "netstat와 열린 포트",
        "netstat는 listening 포트와 TCP/UDP 연결, 프로세스 정보를 보여 주며, 강의에서는 포트와 프로세스를 함께 확인하는 방식으로 소개한다.",
    )
    os12_ping = screen_figure(
        "os-basic",
        os12,
        173,
        "ping으로 연결성 확인",
        "ping은 ICMP echo request/reply로 대상까지 네트워크 연결이 가능한지, 지연 시간이 어느 정도인지 확인하는 가장 기본적인 진단 도구다.",
    )
    os12_traceroute = screen_figure(
        "os-basic",
        os12,
        176,
        "traceroute 경로 추적",
        "traceroute는 목적지까지 거치는 라우터 경로를 추적하지만, 현대 네트워크에서는 방화벽이나 ICMP 차단 때문에 중간 결과가 비어 보일 수 있다.",
    )
    os12_nslookup = screen_figure(
        "os-basic",
        os12,
        179,
        "nslookup과 DNS 조회",
        "nslookup은 도메인 이름이 어떤 IP로 해석되는지 DNS 서버에 질의하며, DNS 서버 설정과 DNS spoofing 가능성을 점검할 때 쓰인다.",
    )
    os12_tcpdump = screen_figure(
        "os-basic",
        os12,
        184,
        "tcpdump 패킷 캡처",
        "tcpdump는 인터페이스에서 오가는 패킷을 캡처하고, -i, -c, -w, -r, host, port, icmp 같은 옵션과 필터로 필요한 트래픽만 볼 수 있다.",
    )
    os12_tcpdump_filters = screen_figure(
        "os-basic",
        os12,
        187,
        "tcpdump 필터 예시",
        "icmp, host, src/dst host, port, portrange, and/or/not 조건을 조합해 분석 대상 패킷을 좁히는 기본 필터 문법을 보여 준다.",
    )

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
                    "body": f"""
                    <p>강의는 WhiteHat School에서 운영체제 기초 과정을 맡은 박수현 멘토의 소개로 시작한다. 첫 시간은 명령어를 바로 치는 실습이 아니라, 앞으로 운영체제 기초 과정이 어떤 흐름으로 진행되는지 확인하는 오리엔테이션이다.</p>
                    {os01_intro}
                    <p>강사는 먼저 <strong>운영체제란 무엇인가</strong>를 알아야 한다고 말한다. 운영체제에는 어떤 유형이 있는지, 운영체제가 무엇을 해 주는지 살펴본 뒤, 대표적인 운영체제 중 하나인 <strong>리눅스</strong>로 넘어간다. 리눅스에는 다양한 배포판이 있고, 이 수업에서는 그중 <strong>우분투</strong>를 기준 환경으로 사용한다.</p>
                    <p>따라서 이 과목의 출발점은 “운영체제 일반론”과 “리눅스 실습 환경”을 연결하는 것이다. 단순히 우분투 화면을 클릭해 보는 수업이 아니라, 운영체제가 어떤 역할을 하고, 리눅스 서버 환경을 어떻게 설치·사용·관리하는지를 순서대로 익히는 과정이다.</p>
                    """,
                },
                {
                    "heading": "설치와 실습 환경",
                    "body": """
                    <p>운영체제는 원래 물리 PC에 직접 설치해 사용할 수 있다. 하지만 학생들이 사용하는 개인 PC에는 보통 Windows가 설치되어 있고, 수업을 위해 Windows를 모두 지운 뒤 우분투를 설치할 수는 없다. 그래서 강의는 <strong>VirtualBox</strong> 같은 가상 환경에 우분투를 설치하는 방식으로 진행된다.</p>
                    <p>강사는 VirtualBox를 기준으로 설명하지만, MacBook을 사용하는 학생, 특히 M1·M2 계열 Mac 사용자는 VirtualBox 설치가 어렵거나 불가능할 수 있다고 안내한다. 이런 경우를 대비해 클라우드에 우분투를 설치하는 방법도 최소한으로 소개할 예정이다. 다만 클라우드 자체는 별도의 수업이 있으므로, 이 강의에서는 운영체제 기초 실습에 필요한 만큼만 다룬다.</p>
                    <div class="callout">강의의 기본 실습 방향은 “내 PC의 기존 운영체제는 유지하고, 가상 머신 안에 우분투를 설치해서 안전하게 연습한다”이다.</div>
                    """,
                },
                {
                    "heading": "GUI와 CLI",
                    "body": """
                    <p>우분투를 설치한 뒤에는 먼저 GUI 환경을 살펴본다. GUI는 <strong>Graphical User Interface</strong>의 약자로, Windows처럼 마우스로 클릭하면서 창을 열고 기능을 사용하는 그래픽 환경이다. 처음 리눅스를 접하는 학생은 GUI를 통해 리눅스도 일반 PC처럼 사용할 수 있음을 확인한다.</p>
                    <p>하지만 강사는 실무적인 환경에서는 GUI를 잘 사용하지 않는다고 강조한다. 서버 환경에서는 보통 <strong>CLI, Command Line Interface</strong>를 사용한다. 흔히 “검은 바탕에 하얀 글씨”로 떠올리는 터미널에서 명령어를 입력하고, 파일 시스템과 디렉토리, 계정, 권한, 패키지, 서비스 같은 운영체제 기능을 다룬다.</p>
                    <p>따라서 이 과목의 핵심은 CLI와 셸 사용 능력이다. 셸에도 여러 종류가 있지만, 수업에서는 가장 기본적으로 널리 쓰이는 <strong>Bash</strong>를 기준으로 배운다. 리눅스를 제대로 사용하려면 GUI보다 터미널과 명령어에 익숙해져야 한다.</p>
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
                    "body": f"""
                    <p>슬라이드는 운영체제 기초 과정을 9개 큰 주제로 소개한다. 현재 HTML 자료집은 이후 실습 내용을 더 잘 따라갈 수 있도록 일부 항목을 세분해 여러 강의로 나누어 두었지만, 1강에서 제시하는 큰 흐름은 아래 화면과 같다.</p>
                    {os01_outline}
                    <div class="timeline">
                      <div><strong>OS와 리눅스</strong><p>운영체제, 리눅스, 우분투의 의미를 잡는다.</p></div>
                      <div><strong>설치</strong><p>VirtualBox와 클라우드 환경에서 우분투를 준비한다.</p></div>
                      <div><strong>사용법</strong><p>GUI를 가볍게 보고, CLI에서 파일과 디렉토리를 다룬다.</p></div>
                      <div><strong>관리</strong><p>계정, 권한, 패키지, 데몬 서비스를 관리한다.</p></div>
                      <div><strong>운영</strong><p>서버 프로그램, 개발 환경, 배시 스크립트, 모니터링으로 확장한다.</p></div>
                    </div>
                    <p>강사의 설명을 따라가면 흐름은 자연스럽다. 먼저 운영체제와 리눅스·우분투가 무엇인지 이해하고, 그 다음 가상 머신이나 클라우드에 우분투를 설치한다. 이후 GUI를 가볍게 확인하되 본격적으로는 CLI 명령어를 통해 파일과 디렉토리, 사용자 계정과 권한, 패키지 설치, 데몬 서비스 관리, 서버 프로그램 설치와 관리, 배시 셸 프로그래밍으로 확장한다.</p>
                    <p>이 첫 강의에서 기억해야 할 결론은 명확하다. 운영체제 기초는 단순히 리눅스를 “설치해 보는” 과정이 아니라, 실무와 보안 학습에서 필요한 리눅스 운영 능력을 CLI 중심으로 쌓는 과정이다.</p>
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
                    "body": f"""
                    <p>강사는 먼저 “우리가 컴퓨터를 쓰는 목적은 운영체제 자체가 아니라 그 위에서 돌아가는 소프트웨어를 쓰는 것”이라고 설명한다. 사용자는 웹브라우저로 인터넷을 보고, 워드 프로세서·파워포인트·엑셀로 문서를 만들고, 포토샵이나 영상 편집 프로그램처럼 원하는 응용 프로그램을 실행하고 싶어 한다. 이때 운영체제는 그 소프트웨어들이 하드웨어 위에서 원활하게 동작하도록 받쳐 주는 기반이다.</p>
                    {os02_definition}
                    <p>슬라이드의 정의처럼 운영체제(OS, Operating System)는 <strong>시스템 하드웨어를 관리</strong>하고, 응용 소프트웨어가 하드웨어를 직접 제어하지 않아도 되도록 <strong>하드웨어를 추상화</strong>하며, 여러 프로그램이 공통으로 필요로 하는 <strong>시스템 서비스</strong>를 제공하는 시스템 소프트웨어다. 계층으로 보면 사용자 아래에 응용 프로그램이 있고, 그 아래에서 운영체제가 하드웨어를 감싼다.</p>
                    <p>Windows는 개인용 PC에서 가장 익숙한 운영체제지만 전부는 아니다. 강의에서는 Windows, Linux, Solaris, macOS, Ubuntu 같은 여러 OS를 언급한다. 스마트폰, 스마트 TV, 셋톱박스, 자율주행차, ATM 같은 장치도 모두 각자 목적에 맞는 운영체제를 갖는다. 예전 TV가 방송을 보여 주는 단순 장치였다면, 스마트 TV는 넷플릭스·유튜브·VOD·웹서핑 앱을 동시에 실행하므로 TV용 운영체제가 필요하다.</p>
                    """,
                },
                {
                    "heading": "하드웨어 추상화와 시스템 서비스",
                    "body": f"""
                    <p>운영체제가 중요한 이유는 하드웨어의 복잡성을 응용 프로그램 대신 처리하기 때문이다. 예를 들어 파워포인트와 엑셀을 동시에 쓰고, 엑셀에서 만든 자료를 워드에 붙여 넣는 동안 파일 저장과 읽기, 화면 출력, 메모리 사용, 입력 장치 처리가 계속 일어난다. 이런 일을 응용 프로그램 개발자가 SSD인지 HDD인지, C 드라이브인지 D 드라이브인지, 그래픽 카드가 어떤 모델인지까지 모두 직접 제어하도록 만들면 개발은 지나치게 복잡해진다.</p>
                    {os02_functions}
                    <p>운영체제는 저장소, 그래픽 카드, 모니터, 프린터, 키보드, 마우스, 터치펜, 지문 인식 장치, 듀얼 모니터 같은 다양한 하드웨어를 응용 프로그램이 쓰기 쉬운 형태로 감싼다. 이 추상화 덕분에 Chrome 같은 브라우저는 유선랜인지 Wi-Fi인지, Bluetooth인지 LTE·5G인지 일일이 몰라도 “인터넷이 연결되어 있다”는 환경을 사용할 수 있다.</p>
                    <table>
                      <thead><tr><th>운영체제 기능</th><th>강의에서의 설명</th></tr></thead>
                      <tbody>
                        <tr><td>프로세스 관리</td><td>여러 프로그램이 동시에 실행되는 것처럼 보이도록 CPU 사용과 실행 흐름을 조정한다.</td></tr>
                        <tr><td>파일 관리</td><td>파일 저장, 읽기, 디렉토리 구조, 파일 시스템 접근을 응용 프로그램에 제공한다.</td></tr>
                        <tr><td>네트워크 관리</td><td>유선랜, Wi-Fi, Bluetooth, LTE, 5G 같은 통신 수단의 차이를 숨기고 네트워크 서비스를 제공한다.</td></tr>
                        <tr><td>메인 메모리 관리</td><td>프로그램이 실행될 때 필요한 메모리 공간을 배분하고 회수한다.</td></tr>
                        <tr><td>디스크 저장소 관리</td><td>SSD, HDD, 파티션, 드라이브 차이를 파일과 디렉토리라는 공통 구조로 보여 준다.</td></tr>
                        <tr><td>입출력 장치 관리</td><td>키보드, 마우스, 프린터, 모니터, 센서 같은 장치를 응용 프로그램과 연결한다.</td></tr>
                        <tr><td>보안 관리</td><td>사용자와 권한, 접근 통제, 기본 보호 기능을 제공한다.</td></tr>
                        <tr><td>명령어 해석 시스템</td><td>사용자가 입력한 명령어를 해석해 운영체제 기능을 호출하게 한다.</td></tr>
                      </tbody>
                    </table>
                    """,
                },
                {
                    "heading": "UNIX에서 Linux로 이어지는 역사",
                    "body": f"""
                    <p>운영체제 종류를 설명하면서 강사는 Linux가 갑자기 독립적으로 생긴 것이 아니라 UNIX의 역사와 이어져 있다고 강조한다. UNIX는 AT&amp;T에서 1960년대에 개발되어 메인프레임, 중형 컴퓨터, 소형 컴퓨터에서 오래 사용된 운영체제다. 당시에는 방 하나를 차지할 정도의 큰 서버와 메인프레임이 있었고, 그 서버용 운영체제 흐름에서 UNIX가 중요한 위치를 차지했다.</p>
                    {os02_unix}
                    <p>UNIX는 시간이 지나며 BSD 계열, System V 계열, POSIX 계열, SunOS, AIX, HP-UX, Solaris 등 여러 갈래로 파생되었다. 교육 목적으로는 Minix라는 운영체제도 등장했다. 강사는 Minix 이름만 알고 있어도 충분하다고 했지만, Linux의 출발점을 이해하려면 “UNIX와 비슷한 교육용 OS인 Minix를 배우던 학생이 직접 만든 커널”이라는 맥락이 중요하다.</p>
                    {os02_torvalds}
                    <p>리누스 토발즈는 핀란드 헬싱키 출신 개발자로, 대학생 시절 Minix를 참고해 취미와 학습 목적으로 Linux 커널을 만들었다. 1991년에 0.1 버전이 처음 공개되었고, 처음에는 Intel 80386 CPU가 장착된 PC에서 동작하는 운영체제로 출발했다. 이후 다양한 CPU와 워크스테이션, 라우터, 자동 제어 시스템, TV, 셋톱박스, 게임 콘솔, 스마트워치 같은 임베디드 장치까지 포팅되었다.</p>
                    """,
                },
                {
                    "heading": "GNU, 자유 소프트웨어, 오픈소스",
                    "body": f"""
                    <p>Linux 역사에서 리누스 토발즈만큼 중요한 인물로 강사는 리처드 스톨먼을 설명한다. 과거에는 하드웨어가 비싼 장비였고, 소프트웨어는 연구자들이 짧은 코드로 작성해 연구 목적으로 공유하는 경우가 많았다. 시간이 지나 소프트웨어가 커지고 상업적으로 판매되기 시작하자, 스톨먼은 소프트웨어가 자유롭게 공유·수정·배포되어야 한다는 철학을 내세워 자유 소프트웨어 재단과 GNU 프로젝트를 이끌었다.</p>
                    {os02_gnu}
                    <p>GNU는 “GNU is Not Unix”의 재귀 약자다. GNU 프로젝트는 누구나 실행, 복사, 수정, 배포할 수 있고 그런 권리를 제한하면 안 된다는 자유 소프트웨어 라이선스 철학을 중심에 둔다. 이 프로젝트를 통해 C 컴파일러인 <strong>gcc</strong>, C 표준 라이브러리인 <strong>glibc</strong>, <strong>make</strong> 같은 GNU 유틸리티, 디버거 <strong>gdb</strong>, 편집기 <strong>emacs</strong> 등 수많은 도구가 만들어졌다.</p>
                    <p>강사는 자유 소프트웨어 운동이 정치적·철학적 성격도 띠었고, 이후에는 그 성격에 부담을 느낀 사람들이 오픈소스라는 흐름을 별도로 만들었다고 설명한다. 그래서 오늘날에는 GNU 프로젝트뿐 아니라 Apache 재단과 Apache License 같은 다양한 오픈소스 재단·라이선스가 존재한다. 수업에서 오픈소스 라이선스를 별도로 깊게 다루지는 않지만, 취업 후 많은 오픈소스를 다루게 되므로 라이선스 원칙은 반드시 알아야 한다는 점도 강조한다.</p>
                    """,
                },
                {
                    "heading": "리눅스 배포판이란 무엇인가",
                    "body": f"""
                    <p>GNU 프로젝트에는 많은 도구가 있었지만, 사용자가 PC에 설치해 쓸 수 있는 완성된 운영체제 커널은 부족했다. 반대로 토발즈가 만든 Linux 커널은 하드웨어를 관리하는 핵심은 제공했지만, 사용자가 편하게 쓰려면 컴파일러, 셸, 편집기, X Window, 유틸리티, 패키지 관리자, 매뉴얼 같은 주변 도구가 필요했다. 이 둘이 결합하면서 실제 사용 가능한 <strong>리눅스 배포판</strong>이라는 형태가 탄생했다.</p>
                    {os02_distribution_family}
                    <p>오픈소스이기 때문에 누구든 기존 배포판을 기반으로 포크를 만들고, 자신의 목적에 맞는 “향”을 더할 수 있다. 강사는 이를 아이스크림의 바닐라, 딸기, 초코, 민트초코 같은 flavor에 비유한다. 기본 바탕인 Linux 커널, 즉 토발즈가 관리하는 바닐라 커널에 각 회사와 커뮤니티가 설정과 도구를 더해 Debian, Slackware, Red Hat, Ubuntu, Fedora, Mint, Kali Linux 같은 다양한 배포판을 만든다.</p>
                    <table>
                      <thead><tr><th>계열</th><th>대표 파생</th><th>패키지 관리자</th><th>강의에서 강조한 특징</th></tr></thead>
                      <tbody>
                        <tr><td>Slackware 계열</td><td>SuSE Linux, SLES, SLED, OpenSUSE</td><td>rpm, zypper</td><td>안정성을 자랑하며 Novell에 인수된 이력이 있다.</td></tr>
                        <tr><td>Debian 계열</td><td>Ubuntu, Knoppix, Lindows, Mint, Kali Linux</td><td>dpkg, apt</td><td>Debian 선언문과 FSF GNU 프로젝트 지원을 바탕으로 비상업적 배포판을 지향했다. Ubuntu는 이 계열에서 나왔다.</td></tr>
                        <tr><td>Red Hat 계열</td><td>RHEL, Fedora, CentOS, Mandrake</td><td>rpm, yum</td><td>국내 기업에서 많이 쓰는 서버 운영체제 계열이며, 유료 RHEL과 무료 CentOS/Fedora 흐름이 있다.</td></tr>
                      </tbody>
                    </table>
                    {os02_distribution_components}
                    <p>배포판 구성 요소는 단순히 Linux 커널만을 뜻하지 않는다. 리눅스 커널 위에 GUI나 Office 같은 운영환경, 배포판 특화 소프트웨어, 시스템 설정 도구, 패키지 관리자, 응용 소프트웨어, 매뉴얼, 고객지원이 함께 묶인다. 그래서 “Linux OS”는 좁게 커널과 핵심 기능을 가리킬 수 있지만, 실제 사용자가 설치하는 “Linux Distribution”은 사용 환경 전체를 뜻한다.</p>
                    """,
                },
                {
                    "heading": "배포판 선택 기준과 데스크톱 환경",
                    "body": f"""
                    <p>강사는 배포판이 너무 많기 때문에 무엇을 선택해야 하는지는 목적에 따라 달라진다고 설명한다. 개인 학습용인지 회사 업무용인지, 서버인지 데스크톱인지 임베디드인지, 특수 목적의 라우터·공유기인지, 교육·과학·음악·생물학·군사 목적처럼 특정 산업군에 맞는지에 따라 선택 기준이 달라진다. 보안적 안정성, 사용성, 이식성, 특정 국가에서 기술지원이 되는지도 고려해야 한다.</p>
                    {os02_desktop}
                    <p>배포판 선택과 함께 데스크톱 환경도 중요하다. 리눅스 커널 위에서 사용자가 창과 아이콘을 볼 수 있도록 해 주는 X Window/데스크톱 환경에는 GNOME, KDE, XFce, LXDE 등이 있다. GNOME은 GNU 프로젝트의 영향을 받아 Free and Open Source Software 철학을 담고, 단순한 사용을 지향하며 GTK+와 Unity 계열 기술을 언급한다. KDE는 기능과 확장성, 다중 플랫폼 호환성을 강조하고 Qt와 Plasma를 기반으로 한다. XFce와 LXDE는 오래된 하드웨어나 저사양 환경에서도 쓸 수 있는 가벼운 데스크톱 환경으로 소개된다.</p>
                    <div class="callout">이 강의에서 꼭 기억할 대표 데스크톱 환경은 GNOME과 KDE다. 뒤 강의에서 우분투 GUI를 볼 때 기본적으로 GNOME 계열 환경을 만나게 된다.</div>
                    """,
                },
                {
                    "heading": "커널의 의미와 커널 유형",
                    "body": f"""
                    <p>커널은 운영체제의 핵심이 되는 컴퓨터 프로그램이다. CPU, 메모리, 디스크, 네트워크 장치 같은 하드웨어를 관리하고, 응용 프로그램이 필요한 서비스를 사용할 수 있도록 중간에서 요청을 처리한다. 사용자가 입력하는 명령어와 응용 프로그램은 유저 모드에서 실행되고, 하드웨어를 직접 다루는 핵심 기능은 커널 모드에서 동작한다. 이 둘 사이의 경계에서 시스템 콜이 사용된다.</p>
                    {os02_kernel_types}
                    <p>강의에서는 커널을 크게 <strong>단일형 커널(monolithic kernel)</strong>과 <strong>마이크로 커널(micro kernel)</strong>로 나눈다. 단일형 커널은 프로세스 관리, 메모리 관리, 통신, 파일 시스템, 디바이스 드라이버 같은 기능이 하나의 큰 덩어리 안에 들어가는 형태다. Linux는 대표적으로 단일형 커널 계열로 설명된다. 속도가 빠르고 용량이 작을 수 있지만, 모든 기능이 한 덩어리에 가깝다는 점이 특징이다.</p>
                    <p>마이크로 커널은 통신 모듈, 파일 시스템, 디바이스 드라이버, 장치 관리자 같은 기능을 작은 서브시스템으로 나누고 서로 통신하게 한다. 구조만 보면 더 좋아 보일 수 있지만, 모듈 간 통신과 인터페이스가 늘어나 성능이 느려지거나 용량이 커질 수 있다. Windows, QNX, Mach 계열이 예시로 언급된다. 다만 강사는 현실의 운영체제가 이론처럼 딱 잘라지지 않으며, Linux도 모노리식 커널이지만 디바이스 드라이버는 모듈화되어 있어 하이브리드 성격이 있다고 설명한다.</p>
                    {os02_kernel_org}
                    <p>강사는 자신이 과거 Linux 커널 개발자였다고 밝히며, 커널 소스 코드를 직접 내려받아 모듈 구조를 파악하고 C 언어로 원하는 기능을 구현했던 경험도 언급한다. Linux 커널 소스는 kernel.org와 git.kernel.org에서 볼 수 있고, 토발즈가 관리하는 메인라인 커널은 흔히 바닐라 커널이라고 부른다. 강의 화면은 2020년 무렵의 5.x 커널, stable, longterm 버전 목록을 보여 주지만, 핵심은 “커널도 계속 개발되고 버전이 올라간다”는 점이다.</p>
                    """,
                },
                {
                    "heading": "Ubuntu의 위치와 버전 체계",
                    "body": f"""
                    <p>Ubuntu는 Debian 계열에서 나온 대표적인 배포판이다. 강사는 Ubuntu가 “전 세계 사람 누구나 어렵지 않게 Linux를 사용하게 하겠다”는 목적과 철학으로 등장했다고 설명한다. 처음에는 데스크톱 일반 PC를 대상으로 출발했지만, Ubuntu를 쉽게 배운 사용자들이 회사에 들어가고 시간이 지나면서 서버, 클라우드, 컨테이너, IoT, 임베디드 환경에서도 널리 쓰이게 되었다.</p>
                    {os02_ubuntu_version}
                    <p>Ubuntu 버전 번호는 출시 연월을 의미한다. 예를 들어 14.04는 2014년 4월, 16.04는 2016년 4월, 20.04는 2020년 4월에 나온 버전이다. 화면에는 Trusty, Xenial, Bionic, Eoan 같은 프로젝트명도 함께 표시된다. 강사는 버전을 <code>Major Version.Minor Version.Patch Version</code>처럼 이해할 수 있다고 설명하고, 홀수 계열은 최신 기능이 들어가는 플래그십 성격이 강하며 짝수 LTS 버전은 안정성을 중시한다고 정리한다.</p>
                    <table>
                      <thead><tr><th>용어</th><th>의미</th></tr></thead>
                      <tbody>
                        <tr><td>LTS</td><td>Long-Term Support. 최초 릴리즈부터 최소 5년 보안 지원을 제공하는 장기 지원 버전이다.</td></tr>
                        <tr><td>GA</td><td>General Availability. 일반 사용자에게 정식으로 제공되는 기본 커널·배포 상태이며, 강의 화면에서는 5년 보안 지원과 연결해 설명한다.</td></tr>
                        <tr><td>HWE</td><td>Hardware Enablement. 새 하드웨어 지원을 위해 커널과 드라이버를 보강하는 흐름이며, 화면에서는 6개월 보안 지원 후 다음 HWE 버전으로 이어지는 방식으로 설명한다.</td></tr>
                      </tbody>
                    </table>
                    <p>강의 시점에는 22.04도 나와 있었지만, 수업에서는 명령어와 화면을 맞추기 위해 Ubuntu 20.04를 기준으로 진행한다고 말한다. 18.04, 20.04, 22.04 어느 버전을 써도 기본 흐름은 크게 다르지 않지만, 학생들이 같은 실습 결과를 보려면 같은 버전을 맞추는 편이 좋다.</p>
                    {os02_popularity}
                    <p>마지막으로 강사는 Linux 배포판 인기도 영상을 보여 준다. 2004년 Ubuntu가 등장하면서 빠르게 상위권을 차지했고, 이후 Mint Linux가 한동안 많은 인기를 얻었으며 Manjaro 같은 후발 주자도 인터넷 입소문을 타고 빠르게 올라왔다. 그래도 Ubuntu는 오랜 기간 높은 인지도를 유지한 대표적인 배포판이므로, 수업용 기준 배포판으로 삼기에 적절하다는 결론으로 강의가 마무리된다.</p>
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
                    "body": f"""
                    <p>강사는 앞 시간의 운영체제 정의를 짧게 복습한 뒤 설치로 넘어간다. 운영체제는 하드웨어를 제어하는 시스템 소프트웨어이므로 원칙적으로는 물리 PC에 직접 설치해야 한다. 그러나 학생들의 PC에는 Windows나 macOS와 개인 데이터가 들어 있으므로, 학습 목적으로 기존 OS를 지우고 Ubuntu를 설치할 수는 없다.</p>
                    {os03_hypervisor}
                    <p>그래서 수업은 <strong>하이퍼바이저</strong>를 사용한다. 하이퍼바이저는 하드웨어를 가상화해 하나의 물리 PC 안에 여러 OS를 설치할 수 있게 해 주는 또 다른 시스템 소프트웨어이며, Virtual Machine Manager라고도 부른다. 이를 통해 Windows 위에 Ubuntu를 설치하거나, 여러 Linux·Windows VM을 동시에 만들 수 있다.</p>
                    <p>강의에서 기준 도구는 <strong>VirtualBox</strong>다. VirtualBox는 오픈소스라 교육용으로 쓰기 좋다. VMware는 하이퍼바이저 분야에서 오래된 강자이고, 과거에는 비싼 상용 제품이었지만 현재는 개인용으로 무료 배포되는 버전도 있다. Microsoft Hyper-V는 Windows Pro 이상에서 쓸 수 있고, WSL도 엄밀히 보면 Windows 안의 Hyper-V 기반 가상화 위에서 Ubuntu 환경을 제공하는 방식으로 이해할 수 있다.</p>
                    """,
                },
                {
                    "heading": "VirtualBox 설치와 새 VM 생성",
                    "body": f"""
                    <p>VirtualBox는 공식 다운로드 페이지에서 설치 파일을 내려받는다. 강의 캡처는 6.1.4 기준이지만 강사는 최신 7.0 계열을 설치해도 무방하다고 안내한다. 다만 오픈소스 소프트웨어는 메이저 버전이 올라간 직후 버그가 있을 수 있어, 강사는 6.1 계열을 오래 선호했고 7.0은 다소 느리거나 불편한 점이 있었다고 언급한다.</p>
                    {os03_download}
                    <p>다운로드할 것은 두 가지다. 하나는 VirtualBox 본체이고, 다른 하나는 <strong>Oracle VM VirtualBox Extension Pack</strong>이다. Extension Pack은 GUI 사용, USB 장치, 그래픽·해상도 조정 같은 기능을 더 편하게 해 주는 확장 플러그인이다. 설치 과정은 대부분 기본값으로 Next, Yes, Install을 눌러 진행하면 된다. 중간에 네트워크·USB 등 가상 장치를 위한 드라이버가 호스트 OS에 설치될 수 있다.</p>
                    {os03_create_vm}
                    <p>VirtualBox를 실행한 뒤에는 상단의 <strong>새로 만들기</strong> 버튼이나 메뉴의 <strong>머신 &gt; 새로 만들기</strong>를 사용한다. 캡처에는 Ubuntu 16.04가 보이지만, 강사는 반복해서 이번 수업의 기준은 <strong>Ubuntu 20.04</strong>라고 표시한다. 이름에 Ubuntu를 넣으면 종류가 Linux, 버전이 Ubuntu 64-bit로 자동 탐지될 수 있고, 자동 탐지가 틀리면 직접 수정한다. 이 선택에 따라 VirtualBox 내부의 가상 하드웨어 기본 옵션이 맞춰진다.</p>
                    <table>
                      <thead><tr><th>항목</th><th>강의 기준</th><th>설명</th></tr></thead>
                      <tbody>
                        <tr><td>OS 이름</td><td>Ubuntu 20.04</td><td>화면 캡처가 16.04여도 실제 실습은 20.04로 진행한다.</td></tr>
                        <tr><td>메모리</td><td>최소 2GB 이상</td><td>PC가 8GB라면 2GB 정도, 16GB 이상이면 4GB·6GB·8GB처럼 여유 있게 줄 수 있다.</td></tr>
                        <tr><td>디스크</td><td>약 10GB</td><td>기초 수업 실습에는 충분하며, 나중에 늘릴 수 있지만 처음부터 너무 크게 만들 필요는 없다.</td></tr>
                      </tbody>
                    </table>
                    """,
                },
                {
                    "heading": "가상 디스크와 ISO 연결",
                    "body": f"""
                    <p>가상 머신을 만들 때 디스크 파일 형식은 기본값인 <strong>VDI(VirtualBox Disk Image)</strong>를 사용한다. VHD나 VMDK는 다른 하이퍼바이저와의 호환성을 고려할 때 의미가 있지만, 초급 과정에서는 VirtualBox 기본값이 충분하다.</p>
                    {os03_disk}
                    <table>
                      <thead><tr><th>옵션</th><th>설명</th><th>강의의 기준</th></tr></thead>
                      <tbody>
                        <tr><td>동적 할당</td><td>처음부터 전체 용량을 차지하지 않고 필요할 때 커진다.</td><td>교육용 환경에서는 일반적으로 무리가 없다.</td></tr>
                        <tr><td>고정 크기</td><td>처음부터 정한 용량을 실제 파일로 확보한다.</td><td>과거 HDD 환경에서는 성능상 유리할 수 있었지만 요즘 SSD/NVMe 환경에서는 체감 차이가 크지 않다.</td></tr>
                        <tr><td>VDI</td><td>VirtualBox 기본 디스크 이미지 형식이다.</td><td>다른 하이퍼바이저 호환성이 필요 없으면 기본값으로 충분하다.</td></tr>
                      </tbody>
                    </table>
                    <p>디스크까지 만들면 CPU, 메모리, 저장소 같은 가상 하드웨어 틀은 준비된 것이다. 하지만 아직 Ubuntu가 설치된 것은 아니다. 앞 강의에서 받은 Ubuntu ISO 이미지를 <strong>저장소 &gt; 비어 있음 &gt; CD 아이콘</strong>을 통해 가상 CD-ROM에 넣어야 한다. 강사는 이것을 실제 PC에 설치 CD나 USB를 꽂고 부팅하는 것과 같다고 설명한다.</p>
                    {os03_iso_network}
                    <p>네트워크는 일단 기본값인 <strong>어댑터 1: NAT</strong>를 그대로 둔다. NAT는 게스트 Ubuntu가 인터넷을 쓰기 위한 기본 연결이다. 이후 오프라인 실습에서는 <strong>어댑터 2: 호스트 전용 어댑터</strong>를 추가해 Windows 호스트에서 Ubuntu 게스트로 접속하는 환경을 만들 수 있다.</p>
                    """,
                },
                {
                    "heading": "ISO와 설치 과정",
                    "body": f"""
                    <p>ISO를 넣고 시작 버튼을 누르면 Ubuntu 설치 화면으로 부팅된다. 언어 목록에서 한국어를 선택할 수 있다. 여기서 가장 중요한 주의점은 <strong>Ubuntu 체험하기</strong>가 아니라 <strong>Ubuntu 설치</strong>를 눌러야 한다는 것이다. 체험하기를 누르면 설치된 것처럼 보일 수 있지만 실제 디스크에 설치된 것이 아니므로, 이 수업의 목적과 다르다.</p>
                    {os03_install_button}
                    <p>Ubuntu 20.04를 VirtualBox에서 설치할 때는 화면 해상도 때문에 오른쪽 아래의 <strong>계속</strong> 또는 <strong>다음</strong> 버튼이 보이지 않을 수 있다. 강사는 이때 당황하지 말고 <code>Alt + F7</code>을 누른 뒤 마우스로 창을 움직이면 아래쪽 버튼을 볼 수 있다고 설명한다. 캡처의 16.04에서는 버튼이 잘 보이지만, 20.04에서는 이 문제가 더 잘 나타날 수 있다.</p>
                    {os03_user_account}
                    <p>사용자 계정 화면에서는 수업을 그대로 따라가고 싶다면 이름과 사용자 이름을 <code>user1</code>로 맞춘다. 뒤 강의에서 <code>user2</code>를 만들어 비교할 예정이기 때문이다. 비밀번호는 교육용으로 <code>qwe123</code>을 안내하지만, 강사는 이것이 보안적으로 매우 취약한 비밀번호라고 분명히 경고한다. VirtualBox 안의 폐쇄된 교육용 VM에서는 기억하기 쉽게 쓰는 것이고, 클라우드나 실무 서버에서는 절대 이렇게 만들면 안 된다.</p>
                    <p>설치 도중에는 Ubuntu에서 제공하는 기능 소개 화면이 지나간다. 강사는 시간이 남을 때 이 화면들을 훑어보며 Windows에서 하던 웹, 문서, 그래픽, 인터넷 작업을 Linux에서도 무료 소프트웨어로 할 수 있음을 확인하라고 말한다. 설치가 끝나면 <strong>지금 다시 시작</strong>을 눌러 재부팅한다. 이후 <code>Please remove the installation medium</code> 메시지가 나오면 가상 CD를 뺐다고 알려 주는 의미로 Enter를 누르면 된다.</p>
                    """,
                },
                {
                    "heading": "업데이트와 종료 방식",
                    "body": f"""
                    <p>설치 후 로그인 화면이 나오고 <code>user1</code> 비밀번호를 입력하면 Ubuntu 데스크톱에 들어갈 수 있다. 20.04 이후에는 22.04 같은 새 버전이 나왔다는 업그레이드 알림이 뜰 수 있다. 강사는 수업 환경을 맞추기 위해 20.04를 설치한 것이므로, 새 배포판 업그레이드는 하지 말라고 설명한다.</p>
                    {os03_updates}
                    <p>패키지 업데이트 알림도 뜰 수 있다. 물리 서버라면 보안 업데이트를 자주 확인하는 것이 좋지만, 교육용 VirtualBox VM에서는 켤 때마다 업데이트가 실행되어 실습을 방해할 수 있다. 그래서 자동 다운로드·자동 설치를 최소화하고, 필요할 때 나중에 터미널이나 GUI에서 수동으로 업데이트하는 흐름을 권장한다.</p>
                    {os03_shutdown}
                    <p>VM을 종료할 때도 방식이 중요하다. <strong>시스템 전원 끄기</strong>는 물리 PC의 전원 플러그를 뽑는 것과 비슷한 강제 종료라 데이터 손실이 생길 수 있다. 안정적인 방법은 <strong>전원 버튼 신호 보내기</strong>처럼 OS가 정상 종료 절차를 밟게 하는 것이다. 이런 정상 종료를 graceful shutdown이라고 부른다. 현재 상태 저장은 나중에 다시 켰을 때 하던 일을 복구하는 기능이지만, 기초 실습에서는 일반적으로 권장하지 않는다.</p>
                    """,
                },
                {
                    "heading": "Guest Additions와 네트워크 모드",
                    "body": f"""
                    <p>VirtualBox를 더 편하게 쓰려면 Guest Additions를 설치할 수 있다. Guest Additions는 화면 해상도 자동 조정, 그래픽 드라이버 개선, Drag&amp;Drop, Clipboard, USB 3.0 같은 기능을 더 부드럽게 만들어 준다. 장치 메뉴에서 Guest Additions CD 이미지를 삽입하면 가상 CD가 마운트되고, 실행 여부를 묻는 창과 관리자 인증 창이 나온다.</p>
                    {os03_guest_additions}
                    <p>검은 터미널 창에 많은 로그가 지나갈 때는 닫지 말고 읽는 습관을 가져야 한다. 로그는 “잘 됐다”, “무엇이 빠졌다”, “명령어 입력을 기다린다” 같은 정보를 담고 있다. 설치가 끝나면 <code>Press Return to close this window</code>처럼 Enter를 누르라는 메시지가 나온다. 단, Ubuntu 20.04에서는 Guest Additions 모듈 빌드에 필요한 도구가 기본 설치되어 있지 않을 수 있으므로 아래 명령을 먼저 실행해야 한다.</p>
                    {code_block("sudo apt install build-essential -y", "bash")}
                    {os03_network_modes}
                    <p>VirtualBox 네트워크는 뒤 실습의 기반이다. NAT는 게스트 OS가 인터넷으로 나갈 때 쓰고, 브리지 어댑터는 게스트가 실제 네트워크 장비처럼 동작하게 한다. 내부 네트워크는 VM끼리만 통신하는 망을 만들 때 쓰며, 호스트 전용 어댑터는 Windows 같은 호스트 OS에서 Ubuntu 게스트로 접속하는 데 사용한다. NAT 네트워크는 NAT와 내부 네트워크 성격을 섞은 모드로 이해하면 된다.</p>
                    <table>
                      <thead><tr><th>모드</th><th>의미</th></tr></thead>
                      <tbody>
                        <tr><td>NAT</td><td>게스트 OS가 외부 인터넷을 사용할 수 있게 하는 기본 모드다.</td></tr>
                        <tr><td>브리지</td><td>게스트가 실제 네트워크에 직접 붙은 장비처럼 동작한다.</td></tr>
                        <tr><td>내부 네트워크</td><td>가상 머신끼리만 통신하는 실습망을 만들 때 쓴다.</td></tr>
                        <tr><td>호스트 전용</td><td>호스트 OS에서 게스트 OS로 접속하기 위한 망을 만들 때 쓴다.</td></tr>
                        <tr><td>NAT 네트워크</td><td>NAT와 내부 네트워크의 성격을 합친 모드로, 여러 VM이 함께 NAT 환경을 쓸 때 활용할 수 있다.</td></tr>
                      </tbody>
                    </table>
                    """,
                },
                {
                    "heading": "Mac 사용자와 클라우드 대안",
                    "body": f"""
                    <p>강사는 Mac 사용자에 대한 주의도 별도로 설명한다. Intel CPU를 쓰는 Mac은 VirtualBox를 설치할 수 있지만, 많은 학생이 사용하는 M1·M2 Mac은 VirtualBox 지원이 안정적이지 않거나 제공되지 않을 수 있다. 하이퍼바이저는 하드웨어를 가상화하는 도구이므로 Apple Silicon을 제대로 지원하는지가 중요하다.</p>
                    {os03_mac_alt}
                    <p>M1·M2 Mac에서는 무료 도구인 <strong>UTM</strong>, 개인용 무료로 사용할 수 있는 <strong>VMware Fusion</strong>, 상용 제품인 <strong>Parallels</strong> 같은 대안을 검토할 수 있다. 강사는 구체 설치 방법은 따로 안내하지 않으므로 직접 찾아서 진행하라고 말하지만, 앞으로 개발·보안 실습을 하려면 자신의 PC에 하이퍼바이저 하나 정도는 갖추는 것이 거의 필수라고 설명한다.</p>
                    {os03_cloud}
                    <p>정말 로컬 환경을 만들 수 없다면 클라우드도 임시 대안이 될 수 있다. 예를 들어 AWS EC2 프리티어에서 Ubuntu Server 20.04 LTS, t2.micro 같은 최소 사양으로 VM을 만들고 SSH로 접속할 수 있다. 다만 강사는 초급자에게는 권장하지 않는다. 이후 수업에는 GUI 환경도 있고, 클라우드 자체가 별도 학습 범위이기 때문이다. 이 수업을 모두 마친 뒤에는 학생들이 EC2를 직접 만들고 터미널로 접속할 수 있는 역량을 갖추는 것이 목표다.</p>
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
            "subtitle": "우분투 GNOME GUI를 기능별로 둘러보고, 실제 서버 실무에서는 CLI와 터미널이 중심이 되는 이유를 이해한다.",
            "tags": ["GUI", "CLI", "GNOME"],
            "objectives": [
                "GUI와 CLI의 차이, 서버 실무에서 CLI가 중요한 이유를 설명한다.",
                "우분투 GNOME 환경의 메뉴바, 런처, 시스템 트레이, 앱 검색, 기본 앱을 화면 기준으로 파악한다.",
                "Firefox, Chrome, LibreOffice, Ubuntu Software, 시스템 설정을 통해 데스크톱 환경에서 가능한 작업을 이해한다.",
                "터미널을 여는 방법과 GUI/CLI 설치 방식의 차이를 이해하고, 이후 CLI 중심 수업으로 넘어갈 준비를 한다.",
            ],
            "sections": [
                {
                    "heading": "GUI와 CLI가 갈라지는 지점",
                    "body": f"""
                    <p>이 시간의 주제는 <strong>리눅스 GUI 환경 다루기</strong>와 <strong>CLI 환경 이해</strong>다. GUI는 Graphical User Interface의 약자로, Windows에서 하듯이 마우스로 아이콘을 클릭하고 창을 움직이며 프로그램을 실행하는 그래픽 사용자 환경을 뜻한다. 앞 시간에 VirtualBox 안에 설치한 Ubuntu Desktop도 가상의 모니터를 가진 컴퓨터이므로, 마우스와 창 중심의 GUI를 사용할 수 있다.</p>
                    {os04_gui_cli}
                    <p>하지만 강사는 실제 업무 환경이 GUI 중심으로 굴러가지 않는다고 강조한다. 서버가 모여 있는 IDC나 데이터센터에는 수많은 서버가 랙에 꽂혀 있고, 그 안에 작업자가 들어가 모니터를 연결해 클릭하면서 관리하지 않는다. 보통은 멀리 떨어진 곳에서 네트워크를 통해 접속하고, 원격 터미널에서 명령어를 입력해 작업한다. 이 명령어 기반 환경이 <strong>CLI, Command Line Interface</strong>다.</p>
                    <p>화면의 왼쪽은 Ubuntu Desktop의 GUI 환경이고, 오른쪽은 Ubuntu Desktop의 텍스트 모드 또는 Ubuntu Server에서 주로 만나는 CLI 환경이다. Ubuntu Server는 기본적으로 GUI를 제공하지 않는 경우가 많다. 서버에는 어차피 모니터가 없고, X Window 같은 그래픽 환경을 설치하면 디스크 용량과 메모리, CPU 같은 자원을 불필요하게 더 쓰기 때문이다.</p>
                    <div class="callout">이번 강의에서는 GUI를 먼저 익혀 리눅스 데스크톱이 낯설지 않게 만들지만, 이후 실무형 운영체제 수업의 중심은 터미널과 CLI 명령어다.</div>
                    """,
                },
                {
                    "heading": "GNOME 데스크톱의 기본 구조",
                    "body": f"""
                    <p>Ubuntu Desktop의 기본 그래픽 환경은 <strong>GNOME</strong>이다. 앞 강의에서 GNOME과 KDE 같은 리눅스 데스크톱 환경을 배웠는데, Ubuntu 기본값은 GNOME이므로 이 수업도 GNOME 기준으로 진행한다. 원한다면 KDE를 추가 설치하거나 로그인할 때 GNOME과 KDE를 바꿔 쓸 수도 있지만, 이 강의에서는 데스크톱 환경 교체 자체를 다루지는 않는다.</p>
                    {os04_gnome_menu}
                    <p>GNOME 화면은 Windows와 배치가 다르다. 왼쪽에는 <strong>런처</strong>가 있고, 이는 Windows의 작업 표시줄이나 태스크바와 비슷하다. 자주 쓰는 앱 아이콘이 세로로 놓이며, 실행 중인 앱도 여기에 표시된다. 우측 상단에는 Windows의 우측 하단 시스템 트레이와 비슷한 영역이 있다. 여기서 전원, 사용자 변경, 로그아웃, 네트워크, 키보드와 한글 전환 같은 상태와 설정을 다룬다.</p>
                    <ul>
                      <li><strong>GNOME 메뉴바</strong>: 화면 상단에 고정되어 있으며, 활성화된 프로그램에 맞는 메뉴가 나타난다.</li>
                      <li><strong>좌측 런처</strong>: Firefox, 파일, LibreOffice, Ubuntu Software, 설정 같은 앱을 빠르게 실행한다.</li>
                      <li><strong>우측 시스템 트레이</strong>: 전원, 사용자, 네트워크, 키보드, 한글 전환, 볼륨 같은 상태를 제어한다.</li>
                    </ul>
                    {os04_window_menu}
                    <p>GNOME의 중요한 특징은 <strong>프로그램 메뉴가 창 안이 아니라 상단 메뉴바에 붙어 보일 수 있다는 점</strong>이다. 파일 관리자를 띄우면 파일 관리자 메뉴가 상단에 나타나고, Firefox를 띄우면 Firefox 메뉴가 상단에 나타나며, LibreOffice Writer를 띄우면 Writer 메뉴가 상단에 나타난다. 창을 화면 아래쪽으로 멀리 떨어뜨려 놓으면 메뉴가 창 안에 있을 것 같은데 실제로는 위쪽에 있어 처음에는 불편하게 느껴질 수 있다.</p>
                    <p>강사는 이 동작을 “GNOME의 특징”으로 이해하라고 설명한다. 어떤 창을 선택했는지에 따라 상단 메뉴가 계속 바뀌므로, 메뉴가 보이지 않는다고 당황하지 말고 화면 맨 위 메뉴바를 확인하면 된다. Ubuntu 16.04에서는 이 메뉴 위치를 창 제목 표시줄 쪽으로 바꾸는 설정도 있었지만, Ubuntu 20.04 기본 설정에서는 해당 옵션이 사라졌고 추가 플러그인을 설치해야 비슷한 설정을 다시 만날 수 있다.</p>
                    """,
                },
                {
                    "heading": "앱 검색, 파일 탐색, 미디어 앱",
                    "body": f"""
                    <p>GNOME 런처의 앱 검색 기능은 스마트폰에서 설치된 앱을 검색하는 화면과 비슷하게 생각하면 된다. Ubuntu 16.04 기준 화면에서는 좌측 런처 상단 아이콘으로 검색 화면을 열었지만, Ubuntu 20.04에서는 앱 메뉴 위치와 표현이 달라져 화면 아래쪽 앱 버튼에서 검색하는 흐름이 더 익숙하다. 강사는 20.04 화면을 따로 보여 주며 캡처와 다르게 보일 수 있다고 설명한다.</p>
                    {os04_program_search}
                    <p>검색 화면에서는 설치된 프로그램, 파일과 폴더, 최근에 사용한 항목, 플러그인과 검색 원본 등을 찾을 수 있다. 기본 앱에는 파일 관리자, 텍스트 편집기, 리듬박스 음악 플레이어, 동영상 플레이어, Firefox, LibreOffice 등이 있다. 파일 관리자는 Windows의 파일 탐색기나 Explorer처럼 폴더를 이동하고 파일을 여는 도구다.</p>
                    <p>Ubuntu 16.04에는 기본 샘플 음악과 동영상 파일이 있어서 리듬박스나 동영상 플레이어를 바로 시험해 볼 수 있었지만, Ubuntu 20.04는 경량화를 위해 이런 샘플 파일이 포함되지 않는다. 음악이나 동영상 재생을 시험하고 싶다면 직접 파일을 내려받아 실행해 보면 된다. 중요한 점은 Ubuntu GUI에서도 Windows처럼 파일 탐색, 음악, 영상, 문서 작업을 할 수 있다는 것이다.</p>
                    """,
                },
                {
                    "heading": "Firefox와 한글 입력 확인",
                    "body": f"""
                    <p>Ubuntu에는 Chrome이 아니라 <strong>Firefox</strong>가 기본 브라우저로 설치되어 있다. 먼저 Firefox를 실행해 <code>www.naver.com</code> 같은 사이트에 접속해 보고, 인터넷 연결과 브라우저 사용이 정상인지 확인한다. 강사는 네이버 검색창에 한글을 입력해 보며 한영 전환이 제대로 되는지도 확인하라고 말한다.</p>
                    {os04_firefox_hangul}
                    <p>한글 키보드를 선택했다고 해서 한글만 입력할 수 있는 것은 아니다. 한글 키보드 하나로 한글과 영문을 모두 입력할 수 있으므로, 영어(미국) 입력기가 불필요하다면 삭제해도 된다. 이렇게 정리해 두면 키보드의 한영 키로 더 편하게 전환할 수 있다.</p>
                    <p>만약 한영 키가 동작하지 않는다면 우측 상단 시스템 트레이의 입력기 상태를 확인해야 한다. 일부 특수 키보드, 예를 들어 표준 104키·107키가 아닌 116키, 121키, 인체공학 키보드 등은 한영 키 호환 문제가 생길 수 있다. 노트북 기본 키보드에서는 대부분 문제가 없지만, 안 되는 경우에는 키보드 옵션에서 수동으로 조정해야 할 수 있다.</p>
                    """,
                },
                {
                    "heading": "Chrome 설치: GUI 다운로드와 .deb 패키지",
                    "body": f"""
                    <p>Chrome을 쓰고 싶다면 별도로 설치해야 한다. Firefox나 검색 엔진에서 “Chrome 다운로드 Ubuntu”처럼 검색하면 Google의 Linux용 Chrome 다운로드 페이지로 이동할 수 있다. 여기서 중요한 선택은 배포판 계열에 맞는 패키지 형식이다.</p>
                    {os04_chrome_deb}
                    <p>Ubuntu는 Debian 계열이므로 <strong>64비트 .deb(Debian/Ubuntu용)</strong> 패키지를 선택한다. 강사는 앞 강의에서 배운 Debian 계열, <code>dpkg</code>, <code>.deb</code>의 관계를 다시 떠올리게 한다. Fedora나 openSUSE 계열이라면 <code>.rpm</code>을 선택하겠지만, 이 수업의 Ubuntu 환경에서는 <code>.deb</code>가 맞다.</p>
                    <p>패키지를 내려받은 뒤 파일을 더블클릭하면 GUI로 설치할 수도 있다. 다만 Ubuntu Software나 설치 프로그램이 백그라운드에서 조용히 작업하면서 진행 바를 명확히 보여 주지 않는 경우가 있다. 설치 버튼을 눌렀는데 아무 반응이 없는 것처럼 보이더라도 곧바로 실패했다고 판단하지 말고 잠시 기다려야 한다. 설치가 끝나면 앱 검색에서 Chrome이 나타난다.</p>
                    """,
                },
                {
                    "heading": "Chrome 설치: CLI에서 dpkg와 sudo 사용",
                    "body": f"""
                    <p>GUI 설치가 잘 되지 않거나 CLI로 설치 과정을 확인해 보고 싶다면 터미널을 열어 다운로드 폴더로 이동한 뒤 <code>dpkg</code>를 사용할 수 있다. 터미널은 바탕화면 우클릭 메뉴의 <strong>터미널 열기</strong>, 단축키 <code>Ctrl + Alt + T</code>, 또는 앱 검색에서 실행할 수 있다.</p>
                    {os04_chrome_cli}
                    <p>화면의 흐름은 짧지만 중요한 리눅스 개념을 미리 보여 준다. 먼저 다운로드 폴더로 이동한다. 강의 화면은 한글 환경이므로 <code>cd 다운로드</code>가 나오지만, 영어 환경에서는 <code>cd ~/Downloads</code>일 수 있다. 이후 <code>dpkg -i</code>의 <code>-i</code>는 install을 뜻한다. 파일명이 길기 때문에 <code>google</code> 정도까지 입력한 뒤 키보드의 Tab 키를 눌러 <strong>탭 완성(tab completion)</strong>으로 긴 파일명을 자동 완성할 수 있다.</p>
                    {code_block("""
                    cd ~/다운로드
                    dpkg -i google-chrome-stable_current_amd64.deb
                    sudo dpkg -i google-chrome-stable_current_amd64.deb
                    google-chrome
                    """, "bash")}
                    <p><code>dpkg -i</code>만 실행하면 “요청한 작업을 하려면 슈퍼유저 권한이 필요합니다”라는 오류가 나온다. 이 메시지는 프로그램 설치가 아무 사용자에게나 허용되지 않고 관리자 권한이 필요하다는 뜻이다. 그래서 <code>sudo dpkg -i ...</code>처럼 <strong>sudo</strong>를 붙여 관리자 권한으로 실행해야 한다. 강사는 이 지점에서 앞으로 사용자, 권한, 관리자 권한을 차근차근 배울 것이라고 예고한다.</p>
                    <p>GUI로 이미 설치했다면 CLI로 다시 중복 설치할 필요는 없다. 이 부분은 “GUI 설치와 CLI 설치가 둘 다 가능하며, CLI에서는 권한과 명령어 흐름을 직접 볼 수 있다”는 감각을 익히기 위한 예시다.</p>
                    """,
                },
                {
                    "heading": "런처 정리와 LibreOffice",
                    "body": f"""
                    <p>Chrome을 설치해 실행하면 실행 중인 동안에는 런처에 Chrome 아이콘이 보인다. 하지만 창을 닫으면 아이콘이 사라질 수 있어, 다음에 실행하려면 다시 앱 검색을 해야 한다. 이를 피하려면 Chrome이 떠 있을 때 아이콘을 우클릭하고 <strong>런처에 고정</strong>을 선택한다.</p>
                    {os04_launcher_pin}
                    <p>고정한 뒤에도 위치가 마음에 들지 않으면 마우스로 드래그해서 위아래로 옮기면 된다. Firefox와 Chrome을 둘 다 브라우저 영역에 모아 두거나, Firefox를 쓰지 않을 계획이라면 런처에서 고정 해제해도 된다. Amazon 아이콘처럼 국내 수업 환경에서 거의 쓰지 않는 스폰서성 런처 항목도 우클릭 후 고정 해제로 제거할 수 있다.</p>
                    {os04_libreoffice}
                    <p>업무 환경에서 중요한 기본 앱은 오피스 프로그램이다. Ubuntu에는 기본적으로 <strong>LibreOffice</strong>가 설치되어 있고, Writer, Calc, Impress를 통해 각각 Word, Excel, PowerPoint와 비슷한 작업을 할 수 있다. 오픈소스 오피스에는 Apache 재단의 OpenOffice와 The Document Foundation의 LibreOffice 흐름이 있으며, 현재 Ubuntu에서는 LibreOffice가 기본으로 제공된다.</p>
                    <p>DOCX, XLSX, PPTX 같은 Microsoft Office 문서 형식은 XML 기반으로 표준화된 부분이 있어 LibreOffice에서도 열고 편집하고 저장할 수 있다. 다만 아주 세밀한 폰트, 레이아웃, 애니메이션 효과, 고급 기능은 완벽히 호환되지 않을 수 있으므로, 중요한 문서를 Windows Office와 Linux LibreOffice 사이에서 계속 왕복 편집하는 것은 조심해야 한다. 그래도 기본 문서 확인과 일반 업무에는 충분히 활용할 수 있다.</p>
                    """,
                },
                {
                    "heading": "Ubuntu Software와 시스템 설정",
                    "body": f"""
                    <p><strong>Ubuntu Software</strong>는 Windows의 Microsoft Store나 스마트폰 앱스토어처럼 애플리케이션을 검색하고 설치하는 도구다. 강사는 예시로 <code>code</code>를 검색하면 Visual Studio Code가 나타나고, 설치 버튼으로 원하는 앱을 추가할 수 있다고 설명한다.</p>
                    {os04_ubuntu_software}
                    <p>Ubuntu Software에는 설치뿐 아니라 업데이트와 제거 기능도 있다. 상단의 업데이트 메뉴에서는 업데이트가 필요한 소프트웨어 목록을 볼 수 있고, 설치된 항목 메뉴에서는 더 이상 쓰지 않는 앱을 제거해 공간을 확보할 수 있다. Ubuntu 20.04의 화면은 16.04보다 더 깔끔하고 표현 방식은 다르지만, 검색·설치·업데이트·삭제라는 기본 기능은 같다.</p>
                    {os04_settings}
                    <p>런처의 시스템 설정은 Windows의 제어판에 더 가깝다. 여기서는 디스플레이 해상도, 화면 잠금, 언어 지원, 키보드, 마우스, 프린터, 네트워크, Bluetooth, 소리, 전원, 시간대 같은 운영체제 설정을 조정한다. 강사는 모든 메뉴를 하나하나 설명하기보다, 학생들이 시간을 들여 직접 눌러 보고 어디에 어떤 설정이 있는지 익혀 두라고 권한다.</p>
                    <p>Ubuntu 20.04 설정 화면은 스마트폰 설정처럼 왼쪽 목록에서 네트워크, 배경, 검색, 개인정보, 공유, 소리, 전원, 디스플레이 같은 항목을 고르고 오른쪽에서 세부 옵션을 바꾸는 방식이다. 필요한 설정을 빠르게 찾으려면 이 구조에 익숙해지는 것이 좋다.</p>
                    """,
                },
                {
                    "heading": "Software & Updates와 업데이트 정책",
                    "body": f"""
                    <p>시스템 설정의 정보 화면이나 별도 메뉴에서 <strong>Software &amp; Updates</strong>로 들어가면 Ubuntu 소프트웨어 저장소와 업데이트 정책을 조정할 수 있다. CD-ROM 설치 매체에서 소프트웨어를 가져올지, 외부 소프트웨어 저장소를 사용할지, 어떤 보안 업데이트를 받을지 같은 설정이 여기에 모인다.</p>
                    {os04_updates}
                    <p>Chrome을 설치했다면 Google Chrome 저장소가 업데이트 목록에 추가될 수 있다. 이는 Chrome이 앞으로 새 버전이 나올 때 해당 경로에서 업데이트를 받기 위해 설치 과정에서 스스로 저장소를 추가했기 때문이다. 즉, Ubuntu의 소프트웨어 업데이트는 운영체제 본체뿐 아니라 외부에서 추가한 패키지 저장소도 함께 관리할 수 있다.</p>
                    <p>보안적으로는 업데이트가 많은 것이 일반적으로 좋다. 하지만 이 수업의 VM은 교육용 실습 환경이므로, 매번 켤 때마다 자동 업데이트가 길게 실행되면 수업 진행을 방해할 수 있다. 그래서 앞 강의에서 설명한 것처럼 새 Ubuntu 버전 업그레이드는 하지 않고, 자동 다운로드와 자동 설치도 최소화해 실습 환경을 일정하게 유지하는 방향을 권장한다.</p>
                    """,
                },
                {
                    "heading": "터미널: 이후 수업의 중심 도구",
                    "body": f"""
                    <p>GUI를 둘러본 뒤 강사는 다시 핵심을 강조한다. 리눅스를 잘 쓰려면 결국 <strong>터미널</strong>을 잘 써야 한다. 터미널은 바탕화면에서 우클릭해 <strong>터미널 열기</strong>를 누르거나, 단축키 <code>Ctrl + Alt + T</code>를 눌러 실행할 수 있다. 앱 검색에서 “터미널” 또는 “terminal”을 검색해도 된다.</p>
                    {os04_terminal}
                    <p>터미널을 많이 쓸 예정이므로, 실행한 뒤 런처 아이콘을 우클릭해 런처에 고정해 두면 편하다. 다음 강의부터는 이 터미널을 기준으로 CLI 명령어를 본격적으로 배운다. 파일과 디렉토리를 이동하고, 사용자와 권한을 확인하고, 패키지를 설치하고, 서비스를 관리하는 대부분의 실습이 터미널에서 이루어진다.</p>
                    <div class="callout">4강의 결론은 “GUI도 쓸 수 있지만, 리눅스를 제대로 다루려면 CLI 명령어가 핵심”이라는 것이다.</div>
                    """,
                },
                {
                    "heading": "GNOME Tweaks와 화려한 GUI 효과",
                    "body": f"""
                    <p>강의 마지막의 꿀팁은 GUI를 더 세밀하게 꾸미는 방법이다. 기본 설정만으로 부족하다면 <strong>Unity Tweak Tool</strong>이나 <strong>GNOME Tweaks</strong> 같은 추가 도구를 설치해 폰트, 테마, 창 배치, 바탕화면 아이콘, 애니메이션 효과, 마우스 포커스 방식을 바꿀 수 있다.</p>
                    {os04_tweaks}
                    <p>예를 들어 Windows에서는 일반적으로 창을 클릭해야 활성화되지만, 전통적인 UNIX나 일부 Linux 데스크톱 환경에서는 마우스 포인터가 창 위에 올라가기만 해도 그 창이 활성화되는 방식을 쓸 수 있다. GNOME Tweaks의 창 설정에서 “마우스 단추를 눌러서 활성화”와 “포인터를 올려두면 활성화” 같은 옵션을 비교해 볼 수 있다.</p>
                    {code_block("""
                    sudo apt install unity-tweak-tool
                    sudo apt install gnome-tweak-tool
                    """, "bash")}
                    <p>Ubuntu 20.04에서는 CLI 명령어를 쓰지 않고도 Ubuntu Software에서 “gnome tweak”을 검색해 GNOME Tweaks를 설치할 수 있다. 강사는 말로만 듣는 것보다 직접 옵션을 바꿔 보는 것이 훨씬 잘 와닿는다고 설명한다.</p>
                    {os04_compiz}
                    <p>마지막에는 Compiz Fusion 3D Desktop 같은 화려한 GUI 효과 영상을 보여 준다. 오래전부터 Linux GUI에서는 창을 3D로 돌리거나 데스크톱 큐브를 쓰는 등 Windows보다 더 화려한 효과를 구성할 수 있었다. 다만 VirtualBox에서는 그래픽 카드와 메모리 성능이 제한되므로 이런 효과를 켜는 것을 권장하지 않는다. 실제 데스크톱 PC에 네이티브로 설치한 Linux에서는 취향에 따라 이런 효과를 구성할 수 있지만, 수업의 본론은 어디까지나 CLI를 잘 다루는 능력이다.</p>
                    """,
                },
            ],
            "checks": [
                "GUI와 CLI의 차이를 서버 실무 관점에서 설명할 수 있는가?",
                "GNOME의 런처, 상단 메뉴바, 시스템 트레이, 활성 창 메뉴 표시 방식을 이해했는가?",
                "Firefox에서 한글 입력을 확인하고, 한영 전환 문제가 생겼을 때 어디를 확인해야 하는지 아는가?",
                "우분투에서 Chrome을 설치할 때 `.deb`, `dpkg -i`, `sudo`, 탭 완성이 각각 어떤 의미인지 설명할 수 있는가?",
                "Ubuntu Software와 시스템 설정, Software & Updates가 각각 어떤 역할을 하는지 구분할 수 있는가?",
                "터미널을 여는 방법과 다음 강의부터 CLI가 중심이 되는 이유를 이해했는가?",
            ],
        },
        {
            "id": "1-5",
            "title": "리눅스 기초 명령어",
            "subtitle": "리눅스 파일시스템 구조를 이해하고, 터미널에서 파일과 디렉토리를 다루는 기본 명령어를 실습한다.",
            "tags": ["CLI 명령어", "파일 시스템", "Vim", "Nano"],
            "objectives": [
                "리눅스 표준 파일시스템 구조와 /boot, /etc, /var/log 같은 주요 디렉토리의 역할을 설명한다.",
                "clear, ls, touch, cat, more, less, rm, mkdir, rmdir, cd, cp, mv, ln, file, man의 기본 의미와 옵션을 이해한다.",
                "숨김 파일, 프롬프트, 홈 디렉토리, 현재/부모/이전 디렉토리, 권한 오류 같은 CLI 사용 감각을 익힌다.",
                "vimtutor와 nano를 통해 GUI가 없는 서버에서도 파일을 편집할 준비를 한다.",
            ],
            "sections": [
                {
                    "heading": "리눅스 파일시스템을 먼저 봐야 하는 이유",
                    "body": f"""
                    <p>5강은 박소연 멘토가 진행하는 리눅스 기초 명령어 수업이다. 오늘의 핵심은 파일과 디렉토리를 다루는 법이다. 명령어 자체를 외우기 전에, 리눅스 안에서 파일과 디렉토리가 어떤 구조로 놓이는지 알아야 한다.</p>
                    {os05_fhs}
                    <p>리눅스 파일시스템은 <strong>FHS, Filesystem Hierarchy Standard</strong>라는 표준 구조를 따른다. 최상단에는 루트 디렉토리 <code>/</code>가 있고, 그 아래에 <code>/bin</code>, <code>/boot</code>, <code>/dev</code>, <code>/etc</code>, <code>/home</code>, <code>/lib</code>, <code>/media</code>, <code>/mnt</code>, <code>/proc</code>, <code>/root</code>, <code>/sbin</code>, <code>/tmp</code>, <code>/usr</code>, <code>/var</code> 같은 디렉토리가 놓인다. 처음에는 복잡해 보이지만 모든 리눅스의 기본 표준이므로 자주 보는 위치는 암기하는 것이 좋다.</p>
                    <table>
                      <thead><tr><th>디렉토리</th><th>강의에서 강조한 의미</th></tr></thead>
                      <tbody>
                        <tr><td><code>/</code></td><td>모든 디렉토리의 최상단인 루트 디렉토리다.</td></tr>
                        <tr><td><code>/bin</code></td><td>일반 사용자가 실행하는 기본 명령어 바이너리가 놓인다.</td></tr>
                        <tr><td><code>/boot</code></td><td>부트로더, 커널, initrd처럼 부팅에 필요한 파일이 있다.</td></tr>
                        <tr><td><code>/dev</code></td><td>디스크, 터미널 같은 시스템 장치를 파일처럼 표현하는 장치 파일이 있다.</td></tr>
                        <tr><td><code>/etc</code></td><td>각종 시스템 설정 파일이 모이는 매우 중요한 위치다.</td></tr>
                        <tr><td><code>/home</code></td><td><code>user1</code>, <code>user2</code> 같은 일반 사용자 홈 디렉토리가 놓인다.</td></tr>
                        <tr><td><code>/root</code></td><td>최상위 관리자 root 사용자의 홈 디렉토리다.</td></tr>
                        <tr><td><code>/sbin</code></td><td>super user, 즉 관리자용 시스템 명령어가 놓이는 위치다.</td></tr>
                        <tr><td><code>/tmp</code></td><td>임시 파일 저장소다.</td></tr>
                        <tr><td><code>/usr</code></td><td>일반 사용자를 위한 공통 프로그램과 라이브러리가 많이 놓인다.</td></tr>
                        <tr><td><code>/var</code></td><td>시스템 운용 중 계속 변하는 임시 데이터, 로그, 캐시 등이 저장된다.</td></tr>
                      </tbody>
                    </table>
                    <p>강사는 특히 <code>/etc</code>와 <code>/var</code>를 반드시 알고 있어야 한다고 강조한다. 서버를 운영하고 문제를 분석할 때 가장 많이 들어가게 되는 곳이 설정 파일이 모인 <code>/etc</code>와 로그가 쌓이는 <code>/var/log</code>이기 때문이다.</p>
                    """,
                },
                {
                    "heading": "/boot, /home, /root, /etc, /var/log",
                    "body": f"""
                    <p>강의는 표준 구조를 설명한 뒤 실제 디렉토리를 몇 군데 들어가 본다. 먼저 <code>/boot</code>는 리눅스가 부팅될 때 필요한 파일이 있는 곳이다. <code>ls -al /boot</code>로 보면 grub, initrd, memtest, vmlinuz 같은 파일이 보인다.</p>
                    {os05_boot}
                    <p><code>vmlinuz</code>로 보이는 파일들이 Linux 커널이다. 강사는 Ubuntu 16.04 기준 커널 파일 하나가 약 8MB 정도에 불과하다고 설명한다. 운영체제의 핵심 기능, 즉 프로세스 관리, 네트워크 관리, 파일시스템 관리, 하드웨어 관리 같은 핵심이 이 작은 커널에 담겨 있다. 다만 사용자 프로그램과 부팅에 필요한 나머지 도구는 initrd 같은 별도 파일에 포함된다.</p>
                    <p><code>/home</code>에는 일반 사용자 홈 디렉토리가 있다. 수업에서는 <code>user1</code>만 있으면 감이 덜 오므로 <code>user2</code>도 만들어 여러 사용자가 한 시스템 안에 공존할 수 있음을 보여 준다. 반대로 <code>/root</code>는 root 사용자의 홈 디렉토리라 일반 사용자가 그냥 보려고 하면 권한이 없어 접근이 제한된다. <code>sudo ls -l /root</code>처럼 관리자 권한을 빌리면 볼 수 있는데, 이 <code>sudo</code>와 권한 개념은 뒤 강의에서 자세히 배운다.</p>
                    {os05_etc}
                    <p><code>/etc</code>는 설정 파일 디렉토리다. 화면에는 “설명 파일”이라고 적힌 부분이 있지만 강사가 바로 “설정 파일”이 맞다고 고쳐 설명한다. 이곳에는 네트워크 설정, AppArmor 같은 보안 기능 설정, APT 패키지 관리자 설정, 웹 서버 설정, 사용자 계정 정보가 들어 있는 <code>passwd</code> 파일 등 시스템을 움직이는 핵심 설정이 모인다. 잘못 바꾸면 시스템에 치명적인 문제가 생길 수 있으므로 의미를 알고 조심해서 다뤄야 한다.</p>
                    {os05_var_log}
                    <p><code>/var</code>는 시스템 운용 중 변하는 파일이 쌓이는 위치다. 웹 서버를 설치하면 웹 콘텐츠가 들어갈 수 있고, 캐시, crash 파일, lock 파일, 임시 데이터도 생긴다. 그중 가장 중요한 곳은 <code>/var/log</code>다. 프로그램을 설치했는데 잘 되었는지 모르거나, 오류가 났거나, 어떤 일이 있었는지 분석해야 할 때 로그 파일을 본다. 서버 운영자는 <code>/var/log</code>를 자주 확인하게 된다.</p>
                    """,
                },
                {
                    "heading": "터미널 프롬프트와 clear",
                    "body": f"""
                    <p>파일시스템을 훑은 뒤 기본 명령어로 들어간다. 앞으로 실습은 별도 설명이 없어도 터미널을 띄운 뒤 그 안에서 명령어를 입력한다고 보면 된다. 가장 먼저 보는 명령은 <code>clear</code>다. 터미널에 명령어 출력이 많이 쌓여 지저분할 때 <code>clear</code>를 입력하면 화면이 깨끗해진다. 데이터가 삭제되는 것이 아니라 화면 출력만 지워지는 것이다.</p>
                    {code_block("""
                    clear
                    """, "bash")}
                    <p>터미널 맨 끝의 <code>$</code> 표시는 <strong>프롬프트(prompt)</strong>다. 운영체제가 “명령어를 기다리고 있다”는 뜻으로 보여 주는 표시다. 프롬프트 앞에 보이는 <code>~</code>는 틸드라고 부르며, 현재 사용자의 홈 디렉토리를 의미한다. 이 수업의 <code>user1</code> 기준으로는 <code>/home/user1</code>을 짧게 <code>~</code>로 보여 주는 것이다.</p>
                    <p>Windows에도 파일 탐색기뿐 아니라 명령 프롬프트가 있고, 숨김 파일 표시 옵션이 있다. Linux도 마찬가지로 GUI 없이 터미널 명령어만으로 파일과 디렉토리를 만들고, 보고, 옮기고, 지울 수 있다. 이 강의는 그 기본 명령어들을 하나씩 익히는 시간이다.</p>
                    """,
                },
                {
                    "heading": "ls: 파일 목록 보기와 숨김 파일",
                    "body": f"""
                    <p><code>ls</code>는 list의 약자다. 오래된 UNIX 계열 명령어는 역사적으로 짧은 약어가 많다. 예전에는 글자 하나하나도 메모리와 입력 비용이었고, 명령어를 길게 치는 것이 비효율적이었다. 그래서 오늘날에도 <code>list</code>가 아니라 <code>ls</code>처럼 짧은 형태가 남아 있다. 강사는 약자를 풀어 외우면 나중에 기억하기 쉽다고 설명한다.</p>
                    {os05_ls}
                    {code_block("""
                    ls
                    ls -l
                    ls -a
                    ls -al
                    ls -la
                    ls -a -l
                    ls *.txt
                    """, "bash")}
                    <table>
                      <thead><tr><th>명령</th><th>의미</th></tr></thead>
                      <tbody>
                        <tr><td><code>ls</code></td><td>현재 디렉토리의 파일과 디렉토리 목록을 보여 준다.</td></tr>
                        <tr><td><code>ls -l</code></td><td>long list. 권한, 소유자, 크기, 시간 같은 상세 정보를 함께 보여 준다.</td></tr>
                        <tr><td><code>ls -a</code></td><td>all. 점으로 시작하는 숨김 파일까지 보여 준다.</td></tr>
                        <tr><td><code>ls -al</code>, <code>ls -la</code>, <code>ls -a -l</code></td><td>숨김 파일까지 긴 형식으로 보여 준다. 옵션 순서는 바뀌어도 된다.</td></tr>
                        <tr><td><code>ls *.txt</code></td><td>확장자가 <code>.txt</code>인 파일만 패턴으로 골라 보여 준다.</td></tr>
                      </tbody>
                    </table>
                    <p><code>ls -al</code> 결과의 첫 줄에는 <code>.</code>과 <code>..</code>이 보인다. <code>.</code>은 현재 디렉토리, <code>..</code>은 부모 디렉토리다. 그 외에 <code>.bashrc</code>처럼 점으로 시작하는 파일은 숨김 파일이다.</p>
                    """,
                },
                {
                    "heading": "touch와 cat: 파일 만들기와 내용 보기",
                    "body": f"""
                    <p><code>touch</code>는 원래 “파일을 툭 건드린다”는 의미에 가깝다. 정확한 기본 기능은 파일의 수정 시간을 현재 시간으로 바꾸는 것이다. 하지만 존재하지 않는 파일을 touch하면 해당 이름의 0바이트 파일이 만들어진다. 그래서 실무에서도 빈 파일을 빠르게 만들 때 자주 사용한다.</p>
                    {os05_touch}
                    {code_block("""
                    touch hello.txt
                    touch test1 test2 test3
                    touch .hello.txt
                    ls -l
                    ls -al
                    rm .hello.txt
                    """, "bash")}
                    <p><code>touch .hello.txt</code>는 기존 <code>hello.txt</code>를 숨기는 명령이 아니다. <code>hello.txt</code>와 <code>.hello.txt</code>는 서로 다른 파일이고, <code>.hello.txt</code>는 파일명이 점으로 시작하기 때문에 기본 <code>ls -l</code>에서는 보이지 않을 뿐이다. <code>ls -al</code>로 보면 숨김 파일까지 확인할 수 있다.</p>
                    {os05_cat}
                    <p><code>cat</code>은 concatenate에서 온 이름이다. 연결한다는 뜻인데, 여기서는 파일이라는 입력(input)을 화면의 표준 출력(standard output)으로 연결해 내용을 보여 준다고 이해하면 된다. <code>cat /etc/passwd</code>는 사용자 계정 정보가 들어 있는 파일을 보여 주고, <code>cat /var/log/syslog</code>는 시스템 로그를 바로 출력한다.</p>
                    {code_block("""
                    cat hello.txt
                    cat /etc/passwd
                    cat /var/log/syslog
                    cat -e /etc/passwd
                    cat -n /etc/passwd
                    """, "bash")}
                    <p><code>cat -e</code>는 줄 끝에 <code>$</code>를 붙여 공백이나 숨은 문자를 확인하는 데 쓸 수 있고, <code>cat -n</code>은 줄 번호를 붙여 보여 준다. 다만 아주 긴 로그 파일을 무작정 <code>cat</code>으로 보면 화면이 한 번에 지나가 버리므로, 뒤에서 소개하는 <code>more</code>나 <code>less</code>가 더 적합할 때가 많다.</p>
                    """,
                },
                {
                    "heading": "more, less, rm: 긴 파일 보기와 삭제",
                    "body": f"""
                    <p><code>more</code>와 <code>less</code>는 긴 파일을 한 화면씩 넘겨 보게 해 주는 명령이다. <code>cat</code>은 파일 전체를 한 번에 출력하지만, 로그처럼 긴 파일은 한 번에 지나가 버려 읽기 어렵다. <code>more</code>는 아래로 내려가며 보고, <code>less</code>는 위아래 이동이 더 자유롭고 파일 전체를 메모리에 올리지 않아 큰 파일을 볼 때 속도도 유리하다.</p>
                    {code_block("""
                    more hello.txt
                    more /etc/passwd
                    more /var/log/syslog
                    less hello.txt
                    less /etc/passwd
                    less /var/log/syslog
                    """, "bash")}
                    <p><code>rm</code>은 remove의 약자로 파일을 삭제한다. 강사는 <code>rm hello.txt</code>, <code>rm test1 test2 test3</code>처럼 여러 파일을 삭제하는 예를 설명한다. 하지만 시스템 파일은 일반 사용자가 삭제할 수 없다. <code>rm /etc/passwd</code>처럼 중요한 파일을 지우려 하면 권한 문제로 실패한다. 이는 리눅스에 사용자와 권한 체계가 있고, 시스템 파일이 보호된다는 사실을 미리 보여 주는 예다.</p>
                    {code_block("""
                    rm hello.txt
                    rm test1 test2 test3
                    rm /etc/passwd
                    """, "bash")}
                    """,
                },
                {
                    "heading": "mkdir, rmdir, cd: 디렉토리 만들기와 이동",
                    "body": f"""
                    <p><code>mkdir</code>은 make directory의 약자이고, <code>rmdir</code>은 remove directory의 약자다. <code>mkdir dir1</code>은 <code>dir1</code>을 만들고, <code>mkdir dir2 dir3</code>은 여러 디렉토리를 한 번에 만든다. <code>mkdir dir1/sub1</code>처럼 하위 디렉토리를 만들 수 있고, 부모 디렉토리까지 함께 만들려면 <code>-p</code> 옵션을 사용한다.</p>
                    {os05_mkdir}
                    {code_block("""
                    mkdir dir1
                    mkdir dir2 dir3
                    mkdir dir1/sub1
                    mkdir -p dir2/sub1
                    rmdir dir1
                    rmdir dir2 dir3
                    rmdir -p dir2
                    rm -r dir1
                    """, "bash")}
                    <p><code>rmdir</code>은 빈 디렉토리만 삭제할 수 있다. 안에 파일이나 하위 디렉토리가 있으면 실패한다. 반대로 <code>rm -r</code>은 recursive, 즉 재귀적으로 안쪽 파일과 디렉토리까지 지우므로 매우 위험하다. 실수로 중요한 위치에서 실행하면 큰 사고가 날 수 있어 반드시 주의해야 한다.</p>
                    {os05_cd}
                    <p><code>cd</code>는 change directory의 약자다. <code>cd dir1</code>로 하위 디렉토리에 들어가고, <code>cd ..</code>으로 부모 디렉토리로 올라간다. <code>cd ../..</code>은 부모의 부모로 이동하고, <code>cd ~</code> 또는 인자 없이 <code>cd</code>만 입력하면 홈 디렉토리로 돌아간다. <code>cd -</code>는 직전에 있던 디렉토리로 돌아간다. <code>cd -</code>를 반복하면 두 위치를 왔다 갔다 할 수 있다.</p>
                    {code_block("""
                    cd dir1
                    cd ..
                    cd dir1/sub1
                    cd .
                    cd ../..
                    cd ~
                    cd
                    cd -
                    cd /etc
                    cd /var/log
                    """, "bash")}
                    <p>강사는 <code>cd /etc</code>, <code>cd /var/log</code>, <code>cd</code>로 홈에 돌아오기처럼 여러 경로를 직접 이동해 보라고 한다. 터미널에서 원하는 폴더로 자유롭게 이동할 수 있어야 이후 모든 CLI 실습이 가능하다.</p>
                    """,
                },
                {
                    "heading": "cp와 mv: 복사, 이동, 이름 변경",
                    "body": f"""
                    <p><code>cp</code>는 copy, <code>mv</code>는 move의 약자다. <code>cp hello.txt hello2.txt</code>는 파일을 복제하고, <code>cp test1 dir1</code>처럼 목적지가 존재하는 디렉토리라면 그 안으로 파일을 복사한다. 목적지가 디렉토리가 아니라 없는 이름이면, 그 이름의 새 파일로 복사될 수 있다. 이 차이를 알고 써야 한다.</p>
                    {os05_cp_mv}
                    {code_block("""
                    touch hello.txt test1 test2
                    mkdir dir1
                    cp hello.txt hello2.txt
                    cp test1 dir1
                    cp test2 dir1
                    cp -r dir1 dir2
                    mv hello.txt hello2.txt
                    mv test1 dir1
                    mv test2 dir1
                    rm -r dir1 dir2
                    rm hello2.txt
                    """, "bash")}
                    <p>디렉토리를 복사하려면 <code>cp -r</code>처럼 recursive 옵션이 필요하다. 강의 화면의 cleanup 명령은 실습 중 만든 <code>dir1</code>, <code>dir2</code>, <code>hello2.txt</code>를 정리하기 위한 예다. 복사와 이동 명령은 파일명을 바꾸는 데도 쓰이므로, “목적지가 파일인지 디렉토리인지”를 항상 확인해야 한다.</p>
                    """,
                },
                {
                    "heading": "ln, 하드링크, 심볼릭 링크, inode",
                    "body": f"""
                    <p><code>ln</code>은 link를 만드는 명령이다. Windows의 바로가기처럼 특정 파일을 다른 위치에서 빠르게 가리키는 기능을 떠올리면 이해하기 쉽다. 강의에서는 초급 단계에서 하드링크는 개념만 알고, 실무에서 자주 쓰는 심볼릭 링크를 꼭 알아야 한다고 설명한다.</p>
                    {os05_link}
                    {code_block("""
                    touch hello.txt
                    ln hello.txt hellolink
                    ln -s hello.txt hellosymlink
                    ls -ali
                    """, "bash")}
                    <p>하드링크는 두 파일명이 같은 실제 파일 데이터를 가리키는 구조다. 복사와 달리 데이터를 두 배로 차지하지 않고, 한쪽 이름으로 내용을 바꾸면 같은 데이터를 바라보는 다른 이름에서도 바뀐 내용이 보인다. 심볼릭 링크는 <code>ln -s</code>로 만들며, 실제 파일 데이터가 아니라 다른 파일 경로를 가리킨다. 그래서 Windows 바로가기와 더 비슷하다.</p>
                    {os05_inode}
                    <p>이 설명은 inode 개념과 이어진다. 우리가 파일명 자체가 파일이라고 생각하기 쉽지만, 실제 데이터는 inode를 거쳐 접근된다. inode에는 소유자, 권한(mode), 파일 크기, 생성·변경 시간(timestamp), 직접/간접 블록 위치 같은 메타데이터가 들어 있다. <code>ls -ali</code>를 보면 하드링크가 같은 inode 번호를 공유하고, 심볼릭 링크는 별도 inode를 갖고 대상 경로를 가리키는 모습을 확인할 수 있다.</p>
                    """,
                },
                {
                    "heading": "file과 man: 속성 확인과 도움말",
                    "body": f"""
                    <p><code>file</code> 명령은 대상 파일이 무엇인지 판별한다. 빈 텍스트 파일인지, <code>/etc/passwd</code> 같은 ASCII text인지, 디렉토리인지, 실행 파일인지, 심볼릭 링크인지 확인할 수 있다. 파일 확장자만 믿지 않고 실제 내용을 보고 유형을 추정한다는 점이 중요하다.</p>
                    {os05_file}
                    {code_block("""
                    file hello.txt
                    file /etc/passwd
                    file dir1
                    file /usr/bin/file
                    file hellosymlink
                    """, "bash")}
                    <p>명령어와 옵션을 전부 외울 수는 없다. 예전에는 구글이나 인터넷이 없었으므로, 시스템 안에서 바로 도움말을 볼 수 있는 매뉴얼이 필요했다. 그 도구가 <code>man</code>이다.</p>
                    {os05_man}
                    {code_block("""
                    man ls
                    man file
                    man man
                    """, "bash")}
                    <p><code>man ls</code>는 <code>ls</code> 명령의 설명과 옵션을 보여 주고, <code>man file</code>은 <code>file</code> 명령의 설명을 보여 준다. 심지어 <code>man man</code>처럼 매뉴얼 자체의 매뉴얼도 볼 수 있다. 강사는 모르는 옵션을 그때그때 검색만 하기보다, 리눅스 안의 매뉴얼을 읽는 습관을 들이라고 설명한다.</p>
                    """,
                },
                {
                    "heading": "Vim과 Nano: GUI 없는 서버에서 편집하기",
                    "body": f"""
                    <p>강의 마지막 이론 파트는 편집기 숙제다. 서버에는 GUI가 없을 수 있으므로, 터미널 안에서 파일을 편집할 수 있어야 한다. 대표 도구는 <strong>vi/vim</strong>과 <strong>nano</strong>다. Vim은 기능이 강력하지만 처음에는 어렵기 때문에, 강사는 <code>vimtutor</code>를 꼭 따라 해 보라고 한다.</p>
                    {os05_vim_nano}
                    {code_block("""
                    sudo apt install vim
                    vimtutor
                    nano hello.txt
                    nano /etc/passwd
                    """, "bash")}
                    <p>Ubuntu 20.04에서는 Vim이 이미 설치되어 있어 <code>sudo apt install vim</code>을 하지 않아도 <code>vimtutor</code>가 바로 실행될 수 있다. 설치 방법 자체는 뒤 패키지 강의에서 다시 배우므로, 여기서는 “편집기를 익혀야 한다”는 목적에 집중하면 된다.</p>
                    {os05_vimtutor}
                    <p><code>vimtutor</code>는 약 30분 정도면 끝까지 따라 할 수 있다. 한 번 했다고 바로 익숙해지지는 않으므로, 앞부분 5분 분량만이라도 며칠 반복해서 이동, 입력, 저장, 종료를 몸에 익히는 것이 좋다.</p>
                    {os05_nano}
                    <p>Nano는 Vim보다 단순하다. 화면 아래에 <code>^O</code>, <code>^X</code> 같은 단축키가 보이는데, 여기서 <code>^</code>는 Control 키를 의미한다. 즉 <code>^O</code>는 <code>Ctrl+O</code>로 저장, <code>^X</code>는 <code>Ctrl+X</code>로 종료한다는 뜻이다. 강의 실습에서는 저장하지 않고 나가기 위해 <code>Ctrl+X</code> 후 <code>N</code>을 선택하는 흐름도 보여 준다.</p>
                    """,
                },
                {
                    "heading": "강의 실습 환경과 실제 따라 하기",
                    "body": f"""
                    <p>강사는 VirtualBox GUI 안의 터미널 글자가 학생들에게 작게 보일 수 있어, 자신은 원격 접속 환경을 따로 만들어 글자를 크게 보여 주겠다고 설명한다. 이를 위해 <code>openssh-server</code>를 설치하고 Windows 터미널에서 원격 접속한다. 하지만 학생들은 지금 이 과정을 따라 할 필요가 없다. 각자 Ubuntu GUI 안에서 터미널을 열고 같은 명령을 입력해 보면 된다.</p>
                    {os05_remote_demo}
                    {code_block("""
                    sudo apt install openssh-server
                    """, "bash")}
                    <p>강사가 설치 중 보이는 오류 메시지는 패키지를 받으려는 경로가 오래되었거나 로컬 패키지 목록이 맞지 않는다는 의미에 가깝다. 이 부분은 뒤 패키지 강의에서 배울 내용이므로, 지금은 “강의자 화면을 크게 보여 주기 위한 준비”로만 이해하면 된다.</p>
                    {os05_practice}
                    <p>실습에서는 <code>clear</code>, <code>ls</code>, <code>ls -l</code>, <code>ls -al</code>을 실제로 입력해 보고, <code>touch hello.txt</code>와 <code>touch .hello.txt</code>의 차이를 확인한다. <code>.hello.txt</code>는 <code>hello.txt</code>를 숨긴 것이 아니라 별개의 숨김 파일이다. <code>mkdir dir1</code>, <code>cd dir1</code>, <code>cd ..</code>, <code>cd ~</code>, <code>cd -</code>로 경로 이동도 직접 해 본다.</p>
                    <p><code>cat /etc/passwd</code>로 계정 정보 파일을 읽고, <code>rm /etc/passwd</code>가 실패하는 것도 확인한다. 이 실패는 실습 오류가 아니라 정상적인 보호 동작이다. 중요한 시스템 파일은 일반 사용자가 삭제할 수 없으며, 이것이 뒤에서 배울 사용자·권한 개념의 출발점이다.</p>
                    <p>마지막으로 강사는 시간이 부족해 모든 실습을 길게 진행하지 못하므로, 학생들이 각자 교안의 명령어를 복습하고 <code>vimtutor</code>와 <code>nano</code>를 직접 실행해 보라고 숙제로 남긴다.</p>
                    """,
                },
            ],
            "checks": [
                "FHS 구조에서 `/`, `/boot`, `/etc`, `/home`, `/root`, `/var/log`의 역할을 설명할 수 있는가?",
                "`clear`, 프롬프트 `$`, 틸드 `~`가 각각 무엇을 의미하는지 이해했는가?",
                "`ls -l`, `ls -a`, `ls -al`, `ls *.txt`의 차이를 설명할 수 있는가?",
                "`touch hello.txt`와 `touch .hello.txt`가 서로 다른 파일을 만든다는 점을 이해했는가?",
                "`cat`, `more`, `less`를 긴 파일 보기 상황에 맞게 구분할 수 있는가?",
                "`mkdir -p`, `rmdir`, `rm -r`의 차이와 삭제 위험성을 설명할 수 있는가?",
                "`cd .`, `cd ..`, `cd ~`, `cd -`, `cd /etc`, `cd /var/log`로 경로를 이동할 수 있는가?",
                "`cp`, `mv`, `ln`, `ln -s`, inode, `file`, `man`의 역할을 말할 수 있는가?",
                "`vimtutor`와 `nano`를 왜 익혀야 하는지, Nano의 `^O`와 `^X`가 무엇인지 설명할 수 있는가?",
            ],
        },
        {
            "id": "1-6",
            "title": "사용자 계정 권한 관리",
            "transcript_title": "사용자 계정 권한 관리",
            "subtitle": "사용자와 관리자를 분리하는 리눅스 철학에서 출발해 root, sudo, 계정 파일, 그룹, rwx 권한, umask, chmod, chown, 실제 user1/user2 실습까지 정리한다.",
            "tags": ["root", "sudo", "chmod", "umask"],
            "objectives": [
                "Windows와 Linux의 사용자 권한 철학 차이를 이해하고, 리눅스에서 일반 사용자와 관리자를 구분해야 하는 이유를 설명한다.",
                "root, superuser, sudo의 의미와 sudo를 습관적으로 남용하면 안 되는 이유를 이해한다.",
                "`whoami`, `id`, `/etc/passwd`, `/etc/shadow`, `/etc/sudoers`, `/etc/group`을 통해 사용자·그룹·권한 정보를 읽는 법을 익힌다.",
                "`adduser`, `passwd`, `chage`, `deluser`, `addgroup`, `usermod`, `deluser user group`으로 사용자와 그룹을 관리하는 흐름을 정리한다.",
                "rwx 권한, 숫자 권한 4·2·1, umask, chmod, chown, chgrp가 실제 파일·디렉토리 접근에 어떻게 반영되는지 실습 기준으로 이해한다.",
            ],
            "sections": [
                {
                    "heading": "Windows식 개인용 PC 관점과 Linux식 멀티유저 관점",
                    "body": f"""
                    <p>강의는 Windows와 Linux의 출발점 차이에서 시작한다. Windows는 MS-DOS와 초기 Windows 시절부터 개인용 PC, 즉 한 사람이 자기 컴퓨터를 쓰는 환경을 중심으로 발전했다. 그래서 과거에는 별도의 사용자 계정이나 권한 구분이 약했고, “내가 사용자이면서 곧 관리자”라는 관점이 자연스러웠다. 지금의 Windows는 계정과 권한 기능을 갖추었지만, 역사적으로는 개인용 운영체제의 성격이 강했다.</p>
                    {os06_user_philosophy}
                    <p>반면 Linux는 Unix 계열 철학을 이어받았다. Unix는 한 사람이 혼자 쓰는 PC가 아니라, 여러 사용자가 메인프레임이나 서버에 동시에 붙어 작업하는 환경에서 출발했다. 여러 사람이 같은 시스템을 쓰는데 아무나 프로그램을 설치하고, 아무나 삭제하고, 아무 때나 재부팅하면 장애와 인적 오류가 바로 발생한다. 그래서 리눅스는 처음부터 <strong>사용자</strong>와 <strong>관리자</strong>를 분리하고, 파일과 디렉토리마다 소유자(owner), 그룹(group), 기타 사용자(other)에 대한 권한을 둔다.</p>
                    <p>강사가 반복해서 강조한 핵심 문장은 “사용자로서의 나와 관리자로서의 나는 다르다”이다. 내가 설치한 Ubuntu라도 일반 사용자로 로그인한 나는 시스템 전체를 마음대로 바꿀 수 있는 관리자가 아니다. 필요한 순간에만 관리자 권한을 빌려야 하고, 그 권한으로 무엇을 하는지 이해해야 한다.</p>
                    """,
                },
                {
                    "heading": "root, superuser, sudo: 강력한 권한을 빌려 쓰는 방식",
                    "body": f"""
                    <p>리눅스의 최상위 관리자는 <strong>root</strong>다. root는 superuser라고도 부르며, 그 위에 더 높은 관리자는 없다. root는 권한 검사를 사실상 뛰어넘어 모든 파일을 읽고, 쓰고, 실행하고, 패키지를 설치하고, 시스템 설정을 바꿀 수 있다. 이 힘은 편리하지만 위험하다. 정상 파일인 줄 알고 실행한 것이 악성코드라면, root 권한으로 실행되는 순간 시스템 전체와 다른 사용자 계정까지 피해를 줄 수 있다.</p>
                    {os06_superuser}
                    <p>Ubuntu는 초보자와 일반 사용자가 root 계정을 남용하는 문제를 줄이기 위해 root 직접 로그인을 기본적으로 막고, <code>sudo</code>를 사용해 필요한 명령 하나에 대해서만 관리자 권한을 빌리게 한다. <code>sudo</code>는 superuser 권한으로 do, 즉 “관리자 권한으로 수행한다”는 의미로 이해하면 된다.</p>
                    {os06_whoami_id}
                    {code_block("""
                    whoami
                    id
                    groups
                    sudo whoami
                    sudo id
                    """, "bash")}
                    <p><code>whoami</code>는 현재 명령을 실행하는 사용자를 보여 주고, <code>id</code>는 UID, GID, 소속 그룹을 보여 준다. 설치할 때 만든 첫 계정 <code>user1</code>은 보통 UID 1000, GID 1000을 가지며, <code>sudo</code>, <code>adm</code>, <code>cdrom</code>, <code>netdev</code>, <code>sambashare</code> 같은 여러 그룹에 들어 있다. 강사는 이 계정이 “유일한 사용자이면서 설치를 수행한 계정”이기 때문에 여러 장치와 관리 기능에 접근할 수 있는 그룹을 기본으로 가진다고 설명한다.</p>
                    {os06_sudo_id}
                    <p><code>sudo whoami</code>를 실행하면 그 명령을 수행하는 동안에는 결과가 <code>root</code>로 나온다. 이어서 다시 <code>whoami</code>를 치면 <code>user1</code>로 돌아온다. 즉 sudo는 내가 영구히 root가 되는 명령이 아니라, 그 순간만 root 권한을 빌려 오는 장치다. 그래서 권한이 없다고 나올 때마다 습관적으로 sudo를 붙이는 것은 좋지 않은 습관이다. 먼저 “왜 권한이 없는지”, “정말 관리자 권한이 필요한 작업인지”, “내가 지금 어떤 파일을 건드리는지”를 생각해야 한다.</p>
                    {os06_sudoers}
                    <p>sudo를 아무나 사용할 수 있는 것도 아니다. <code>/etc/sudoers</code> 파일은 어떤 사용자나 그룹이 sudo를 쓸 수 있는지, 어떤 방식으로 쓸 수 있는지 관리한다. 일반 사용자로 <code>cat /etc/sudoers</code>를 실행하면 권한이 없어 볼 수 없고, 관리자 권한으로 <code>sudo cat /etc/sudoers</code>를 해야 확인할 수 있다. 파일 안에서 <code>%</code>로 시작하는 항목은 그룹을 의미한다. 이 파일의 세부 문법은 복잡하므로 기초반에서는 “sudo 권한도 별도 정책 파일로 관리된다”는 점만 확실히 잡으면 된다.</p>
                    {code_block("""
                    cat /etc/sudoers
                    sudo cat /etc/sudoers
                    """, "bash")}
                    """,
                },
                {
                    "heading": "/etc/passwd, /etc/shadow, /etc/group 읽기",
                    "body": f"""
                    <p>리눅스의 로컬 계정 정보는 대표적으로 세 파일에 나뉘어 저장된다. <code>/etc/passwd</code>는 사용자 계정 목록과 기본 정보를 담고, <code>/etc/shadow</code>는 암호 해시와 암호 정책을 담으며, <code>/etc/group</code>은 그룹 정보를 관리한다.</p>
                    {os06_account_files}
                    {code_block("""
                    cat /etc/passwd
                    cat /etc/shadow
                    sudo cat /etc/shadow
                    cat /etc/group
                    """, "bash")}
                    <p><code>/etc/passwd</code>라는 이름 때문에 비밀번호가 그대로 들어 있다고 오해하기 쉽다. 과거에는 이 파일 안에 암호 해시가 있었지만, <code>/etc/passwd</code>는 여러 프로그램이 사용자 정보를 확인해야 하므로 누구나 읽을 수 있었다. 해시가 평문은 아니더라도, 공격자가 해시를 얻으면 사전 공격이나 크래킹 도구로 약한 패스워드를 맞힐 수 있다. 그래서 민감한 암호 해시는 <code>/etc/shadow</code>로 분리되었고, 일반 사용자는 shadow를 읽지 못한다.</p>
                    {os06_passwd_structure}
                    <p><code>/etc/passwd</code> 한 줄은 콜론(<code>:</code>)으로 구분된다. 필드는 순서대로 사용자명, 패스워드 자리표시자, UID, GID, 사용자 이름 또는 설명, 홈 디렉토리, 로그인 셸이다. 현재는 실제 암호가 shadow로 빠져 있으므로 패스워드 칸에는 보통 <code>x</code>가 들어간다. 예를 들어 <code>user1:x:1000:1000:user1,,,:/home/user1:/bin/bash</code> 같은 줄은 user1의 UID와 GID가 1000이고, 홈 디렉토리는 <code>/home/user1</code>, 로그인 셸은 <code>/bin/bash</code>라는 뜻이다.</p>
                    {os06_uid_ranges}
                    <p>UID 0은 root다. 1~99 사이의 낮은 번호는 전통적으로 미리 정의된 시스템 계정에 쓰이고, 100~999는 관리용 또는 시스템 서비스 계정에 활용될 수 있도록 남겨 둔 범위로 설명한다. 실제 사용자가 로그인해 작업하는 계정은 보통 1000번부터 시작한다. 화면의 여러 계정 중 <code>/usr/sbin/nologin</code>을 로그인 셸로 가진 계정은 사람이 터미널로 로그인해 쓰는 계정이 아니라, 프린터, 메일, 데몬 같은 시스템 서비스 실행을 위한 계정으로 보면 된다.</p>
                    {os06_shadow_structure}
                    <p><code>/etc/shadow</code>에는 사용자명, 암호 해시, 마지막 암호 변경일, 최소 사용일, 최대 사용일, 만료 경고일, 비활성 기간, 계정 만료일 같은 정보가 들어간다. 강의에서는 마지막 변경일처럼 보이는 <code>18357</code> 같은 숫자를 설명한다. 리눅스의 시간 계산은 epoch, 즉 1970년 1월 1일 00:00:00 UTC를 기준으로 한다. 1970년 1월 1일에 18,357일을 더하면 2020년 4월 5일이 되므로, shadow의 날짜 숫자도 계산 가능한 값이라는 점을 보여 준다.</p>
                    {os06_hash_locked}
                    <p>root 계정의 암호 칸에 느낌표(<code>!</code>)가 있으면 암호 로그인이 잠겨 있다는 뜻이다. Ubuntu가 root 직접 로그인을 기본적으로 막는 흐름과 연결된다. 일반 사용자 암호는 평문이 아니라 단방향 해시로 저장되며, 강의 화면은 <code>$1$</code> MD5, <code>$2a$</code> Blowfish, <code>$5$</code> SHA-256, <code>$6$</code> SHA-512 같은 식별자를 예로 보여 준다. 여기서 중요한 것은 “암호를 저장하더라도 평문이 아니라 해시로 저장하고, 그 해시 파일 자체도 보호한다”는 구조다.</p>
                    """,
                },
                {
                    "heading": "사용자와 그룹 만들기, 바꾸기, 삭제하기",
                    "body": f"""
                    <p>새 사용자 계정은 아무나 만들 수 없다. 회사에서 신입사원이 마음대로 계정을 만들 수 있다면, 퇴사 전에 백도어 계정을 만들거나 권한 추적을 어렵게 만들 수 있다. 그래서 계정 생성은 관리자 권한으로 수행한다.</p>
                    {os06_adduser}
                    {code_block("""
                    adduser user2
                    sudo adduser user2
                    cat /etc/passwd
                    sudo cat /etc/shadow
                    """, "bash")}
                    <p>일반 사용자로 <code>adduser user2</code>를 실행하면 실패하고, <code>sudo adduser user2</code>로 실행해야 한다. 생성 과정에서는 user2의 홈 디렉토리를 만들고, 기본 그룹을 만들고, 암호와 사용자 정보를 입력한다. 이후 <code>/etc/passwd</code>를 보면 user2 항목이 추가되고, <code>/etc/shadow</code>를 관리자 권한으로 보면 user2의 암호 해시와 날짜 정보도 생긴다.</p>
                    {os06_chage_passwd}
                    {code_block("""
                    sudo passwd user2
                    sudo chage -l user2
                    sudo chage user2
                    sudo chage -E 2026-12-31 -m 1 -M 90 -W 7 user2
                    """, "bash")}
                    <p><code>passwd</code>는 실제 암호를 바꾸는 명령이다. 반면 <code>chage</code>는 암호의 정책을 바꾼다. 예를 들어 외주 직원 계정이 연말까지만 유효해야 한다면 계정 만료일을 지정할 수 있고, 암호를 최소 며칠 사용해야 하는지, 최대 며칠마다 바꿔야 하는지, 만료 며칠 전부터 경고할지도 지정할 수 있다. <code>chage -l user2</code>는 현재 정책을 목록으로 보여 준다.</p>
                    {os06_deluser}
                    {code_block("""
                    sudo deluser user2
                    sudo deluser --remove-home user2
                    """, "bash")}
                    <p><code>deluser user2</code>는 사용자 계정을 삭제한다. 하지만 기본 삭제는 홈 디렉토리까지 항상 지우지는 않는다. 강사는 새 직원을 받거나 퇴사자를 처리할 때 그 사람의 문서와 작업물을 바로 삭제하면 안 되는 경우가 많기 때문에, 홈 디렉토리 보존 여부가 중요하다고 설명한다. 홈 디렉토리까지 지우려면 <code>--remove-home</code> 같은 옵션을 명시해야 한다.</p>
                    {os06_group_add}
                    {code_block("""
                    sudo addgroup group1
                    sudo delgroup group1
                    """, "bash")}
                    <p>그룹도 별도로 만들고 삭제할 수 있다. 그룹은 파일 권한에서 owner와 other 사이에 있는 중간 범주다. 같은 팀, 같은 역할, 같은 서비스 계정을 묶어 권한을 부여할 때 사용한다.</p>
                    {os06_usermod_group}
                    {code_block("""
                    sudo usermod -a -G sudo user2
                    id user2
                    sudo deluser user2 sudo
                    id user2
                    """, "bash")}
                    <p><code>usermod -a -G sudo user2</code>는 user2를 sudo 그룹에 추가한다. 여기서 <code>-a</code>는 append, 즉 기존 그룹을 유지한 채 새 그룹을 추가한다는 뜻이다. <code>-G</code>만 잘못 쓰면 기존 보조 그룹 구성이 바뀔 수 있으므로 주의해야 한다. 그룹에서 제거할 때는 Ubuntu에서 <code>sudo deluser user2 sudo</code>처럼 쓸 수 있다. 강의 화면의 한국어 메시지는 “user2 그룹에서 sudo 사용자 제거”처럼 순서가 어색하게 번역되어 보이는데, 실제 영어 의미는 “sudo 그룹에서 user2 사용자를 제거한다”에 가깝다. 기능은 맞고 번역만 헷갈리는 사례로 이해하면 된다.</p>
                    <p>강사는 실무에서는 로컬 계정만으로 모든 사용자를 관리하지 않고 LDAP이나 Active Directory 같은 중앙 인증 체계를 쓰는 경우도 많다고 덧붙인다. 그래도 로컬 파일과 기본 명령을 이해해야 중앙 인증도 제대로 이해할 수 있다.</p>
                    """,
                },
                {
                    "heading": "파일 권한: owner, group, other와 rwx",
                    "body": f"""
                    <p>파일 권한은 <code>ls -l</code>의 첫 열에서 확인한다. 첫 글자는 파일 유형이다. <code>-</code>는 일반 파일, <code>d</code>는 디렉토리, <code>l</code>은 심볼릭 링크다. 그 뒤 9글자는 세 글자씩 나뉘어 owner, group, other의 권한을 나타낸다.</p>
                    {os06_permission_intro}
                    <p>예를 들어 <code>-rw-r--r--</code>라면 일반 파일이고, 소유자는 읽기·쓰기 가능, 그룹은 읽기만 가능, 기타 사용자도 읽기만 가능하다. <code>drwxr-xr-x</code>라면 디렉토리이고, 소유자는 읽기·쓰기·진입 가능, 그룹과 기타 사용자는 읽기와 진입이 가능하지만 쓰기는 못 한다.</p>
                    {os06_permission_numbers}
                    <table>
                      <thead><tr><th>값</th><th>권한</th><th>파일에서의 의미</th><th>디렉토리에서의 의미</th></tr></thead>
                      <tbody>
                        <tr><td>4</td><td>r</td><td>내용 읽기</td><td>목록 조회</td></tr>
                        <tr><td>2</td><td>w</td><td>내용 수정</td><td>항목 생성·삭제·이름 변경</td></tr>
                        <tr><td>1</td><td>x</td><td>실행 파일 실행</td><td>디렉토리 진입·경로 통과</td></tr>
                      </tbody>
                    </table>
                    <p>숫자 권한은 read 4, write 2, execute 1을 더해 만든다. <code>7</code>은 4+2+1이므로 <code>rwx</code>, <code>6</code>은 4+2이므로 <code>rw-</code>, <code>5</code>는 4+1이므로 <code>r-x</code>, <code>0</code>은 아무 권한 없음이다. 세 자리 숫자 <code>755</code>는 owner 7, group 5, other 5라는 뜻이다. 강사는 이 부분이 정보보안기사 같은 시험에도 자주 나오므로 반드시 익혀야 한다고 강조한다.</p>
                    {os06_umask}
                    <p>새 파일과 디렉토리는 기본 권한에서 <code>umask</code>가 막는 권한을 제외해 만들어진다. 파일은 기본적으로 실행 권한이 빠진 <code>666</code>에서 시작하고, 디렉토리는 진입 권한이 필요하므로 <code>777</code>에서 시작한다. Ubuntu의 일반적인 <code>umask 0002</code>에서는 새 파일이 <code>664</code>, 새 디렉토리가 <code>775</code>처럼 만들어진다.</p>
                    {code_block("""
                    umask
                    touch hello2.txt
                    mkdir testdir
                    ls -l
                    umask 007
                    touch private.txt
                    mkdir private-dir
                    ls -l
                    umask 002
                    """, "bash")}
                    <p>특수 권한 때문에 <code>umask</code>가 네 자리로 보일 수 있는데, 기초 단계에서는 뒤 세 자리 owner/group/other 마스크를 먼저 이해하면 된다. 앞쪽 한 자리는 SUID, SGID, sticky bit 같은 특수 권한과 연결된다.</p>
                    """,
                },
                {
                    "heading": "chmod, chown, chgrp로 권한과 소유권 바꾸기",
                    "body": f"""
                    <p><code>chmod</code>는 change mode의 약자이며, 파일이나 디렉토리의 권한 모드를 바꾼다. 두 가지 방식이 있다. 첫째는 숫자 모드다. <code>chmod 777 hello.txt</code>는 owner, group, other 모두에게 읽기·쓰기·실행 권한을 준다. <code>chmod 700 hello.txt</code>는 owner에게만 모든 권한을 주고 나머지는 모두 막는다.</p>
                    {os06_chmod_numeric}
                    {code_block("""
                    chmod 777 hello.txt
                    chmod 700 hello.txt
                    chmod 755 script.sh
                    chmod 644 note.txt
                    """, "bash")}
                    <p>둘째는 문자 모드다. 대상은 <code>u</code>(user/owner), <code>g</code>(group), <code>o</code>(other), <code>a</code>(all)로 지정하고, <code>+</code>는 추가, <code>-</code>는 제거, <code>=</code>는 정확히 설정을 의미한다.</p>
                    {os06_chmod_symbolic}
                    {code_block("""
                    chmod u+x hello.txt
                    chmod u-x hello.txt
                    chmod g+rw hello.txt
                    chmod g-rw hello.txt
                    chmod o+w hello.txt
                    chmod o-rx hello.txt
                    """, "bash")}
                    <p><code>chmod u+x</code>는 소유자에게 실행 권한을 더하고, <code>chmod g-rw</code>는 그룹에서 읽기와 쓰기 권한을 제거한다. <code>chmod o+w</code>처럼 other에게 쓰기 권한을 주면 다른 사용자도 파일을 바꿀 수 있으므로 실제 운영 환경에서는 매우 조심해야 한다.</p>
                    {os06_chown_chgrp}
                    {code_block("""
                    sudo chown user2:user2 hello.txt
                    sudo chown user2 hello.txt
                    sudo chgrp user2 hello.txt
                    sudo chown user1:user1 hello.txt
                    """, "bash")}
                    <p><code>chown</code>은 change owner, <code>chgrp</code>는 change group이다. 실무에서는 <code>chown user:group file</code>처럼 한 번에 소유자와 그룹을 바꾸는 형태가 자주 쓰인다. 이 작업은 보통 관리자 권한이 필요하다. 아무 사용자가 파일 소유자를 마음대로 바꿀 수 있으면, 악성 파일을 남의 소유처럼 보이게 하거나 책임 추적을 흐릴 수 있기 때문이다.</p>
                    {os06_special_bits}
                    <p>강의는 특수 권한인 SUID, SGID, sticky bit도 짧게 소개한다. 이들은 일반 <code>rwx</code> 권한 앞에 붙는 추가 권한으로, 실행 시 소유자 권한을 빌리거나, 디렉토리 안의 그룹 상속을 조정하거나, 공유 디렉토리에서 삭제 권한을 제한하는 식으로 쓰인다. 기초반에서는 세부 활용까지 외우기보다, 나중에 앞자리 숫자와 연결해 다시 배울 내용이라고 이해하면 된다.</p>
                    """,
                },
                {
                    "heading": "실습: user1과 user2로 권한 차이 확인하기",
                    "body": f"""
                    <p>강사는 VirtualBox 안의 글자가 작게 보일 수 있어 원격 터미널 환경으로 큰 글씨를 보여 주지만, 학생들은 Ubuntu GUI 터미널에서 같은 명령을 따라 하면 된다. 실습은 <code>ls -l</code>로 현재 파일들의 권한과 소유자, 그룹을 확인하는 것부터 시작한다.</p>
                    {os06_practice_ls}
                    {code_block("""
                    ls
                    ls -l
                    touch hello2.txt
                    mkdir dir1
                    mkdir dir2
                    ls -l
                    """, "bash")}
                    <p>기존 <code>umask</code>가 <code>002</code>라면 새 파일은 대체로 <code>rw-rw-r--</code>, 새 디렉토리는 <code>rwxrwxr-x</code>처럼 만들어진다. 이후 <code>umask 007</code>처럼 값을 바꾸고 새 파일과 디렉토리를 만들면 other 권한이 빠지는 것을 볼 수 있다. 이 실습은 umask가 “권한을 더하는 값”이 아니라 “기본 권한에서 빼는 마스크”라는 점을 확인하게 해 준다.</p>
                    {os06_practice_umask}
                    <p>다음으로 <code>sudo adduser user2</code>를 실행해 두 번째 사용자를 만든다. 리눅스는 멀티유저 운영체제이므로 user1과 user2가 동시에 로그인할 수 있다. 강의에서는 한쪽 터미널은 user1, 다른 한쪽 터미널은 user2로 열어 같은 파일에 대한 접근 결과를 비교한다.</p>
                    {os06_practice_user2}
                    {os06_practice_user2_id}
                    {code_block("""
                    sudo adduser user2
                    su - user2
                    whoami
                    id
                    pwd
                    ls
                    """, "bash")}
                    <p>user2의 <code>id</code>를 보면 user1처럼 sudo, adm, cdrom, netdev 같은 관리·장치 그룹에 들어 있지 않다. 또한 터미널에서 만든 계정은 GUI에서 처음 만든 계정과 달리 Downloads, Documents 같은 폴더가 아직 없을 수 있다. 이는 계정 생성 방식과 초기 설정 차이일 뿐, 이상 현상은 아니다.</p>
                    {os06_practice_file_write}
                    {code_block("""
                    echo hello > hello.txt
                    cat hello.txt
                    ls -l hello.txt
                    """, "bash")}
                    <p><code>echo hello &gt; hello.txt</code>는 <code>hello</code>라는 문자열을 표준 출력으로 내보내고, <code>&gt;</code> 리다이렉션으로 그 출력을 파일에 저장한다. 리다이렉션 자체는 뒤 배시 쉘 강의에서 더 자세히 다루지만, 여기서는 파일에 내용을 써서 권한 차이를 확인하는 데 사용한다.</p>
                    {os06_practice_user2_write}
                    <p>user1이 만든 <code>hello.txt</code>에 other 읽기 권한이 있으면 user2는 <code>cat hello.txt</code>로 내용을 읽을 수 있다. 하지만 other 쓰기 권한이 없으면 <code>echo hacker &gt; hello.txt</code>처럼 덮어쓰려 할 때 권한 거부가 난다. user1이 <code>chmod o+w hello.txt</code>로 other 쓰기 권한을 주면, 그때부터 user2도 파일 내용을 바꿀 수 있다. 이 장면이 파일 권한이 단순 표기가 아니라 실제 데이터 보호에 직접 연결된다는 핵심 실습이다.</p>
                    {code_block("""
                    chmod o+w hello.txt
                    # user2 터미널
                    echo hacker > hello.txt
                    cat hello.txt
                    # user1 터미널
                    chmod o-w hello.txt
                    """, "bash")}
                    {os06_practice_dir_exec}
                    <p>디렉토리 권한은 파일 권한보다 더 헷갈리기 쉽다. 파일에서 <code>x</code>는 실행을 뜻하지만, 디렉토리에서 <code>x</code>는 그 디렉토리에 들어가거나 경로 중간을 통과할 수 있는 권한이다. <code>r</code>은 목록을 볼 수 있는 권한이고, <code>w</code>는 그 안에 항목을 만들거나 삭제하거나 이름을 바꿀 수 있는 권한이다.</p>
                    {os06_practice_dir_chmod}
                    {code_block("""
                    chmod 771 dir2
                    # other는 dir2에 cd로 들어갈 수는 있지만 ls 목록 확인은 제한될 수 있다.
                    chmod 775 dir2
                    # other도 읽기와 진입이 가능해 목록을 볼 수 있다.
                    chmod 770 dir2
                    # other의 접근을 다시 막는다.
                    """, "bash")}
                    <p><code>chmod 771 dir2</code>는 other에게 execute만 주는 예다. 이 경우 경로를 알고 있으면 들어가거나 통과할 수 있지만, 목록을 읽는 것은 제한된다. <code>chmod 775 dir2</code>는 other에게 read와 execute를 주므로 목록 조회와 진입이 가능하다. 마지막으로 <code>chmod 770 dir2</code> 또는 <code>chmod o-rx dir2</code>를 적용하면 other의 접근을 다시 막을 수 있다.</p>
                    """,
                },
            ],
            "checks": [
                "Windows의 개인용 PC 관점과 Linux/Unix의 멀티유저 관점 차이를 설명할 수 있는가?",
                "root, superuser, sudo의 관계와 sudo를 습관적으로 남용하면 안 되는 이유를 말할 수 있는가?",
                "`whoami`, `id`, `sudo whoami`, `sudo id` 결과에서 UID 0과 UID 1000의 차이를 이해했는가?",
                "`/etc/passwd`, `/etc/shadow`, `/etc/group`, `/etc/sudoers`가 각각 어떤 정보를 관리하는지 설명할 수 있는가?",
                "`/etc/passwd`의 사용자명, x, UID, GID, 홈 디렉토리, 로그인 셸 필드를 읽을 수 있는가?",
                "shadow 파일의 잠긴 계정 표시, 해시 식별자, 1970년 1월 1일 UTC 기준 epoch 날짜를 설명할 수 있는가?",
                "`adduser`, `passwd`, `chage`, `deluser`, `addgroup`, `usermod -a -G`, `deluser user group`의 역할을 구분할 수 있는가?",
                "`ls -l` 첫 열에서 파일 유형, owner/group/other, r/w/x 권한을 해석할 수 있는가?",
                "read=4, write=2, execute=1을 이용해 777, 755, 700, 664, 775, 770을 계산할 수 있는가?",
                "파일 기본 666, 디렉토리 기본 777과 umask 002 또는 007의 관계를 이해했는가?",
                "`chmod 777`, `chmod 700`, `chmod u+x`, `chmod g-rw`, `chmod o+w`, `chmod o-rx`가 어떤 권한 변화를 만드는지 설명할 수 있는가?",
                "`chown`, `chgrp`, `chown user:group file`의 차이와 관리자 권한이 필요한 이유를 이해했는가?",
                "파일에서 other 읽기 권한과 쓰기 권한이 user2의 `cat`, `echo > file` 결과를 어떻게 바꾸는지 설명할 수 있는가?",
                "디렉토리에서 r, w, x가 각각 목록 조회, 항목 변경, 진입/경로 통과와 어떻게 연결되는지 설명할 수 있는가?",
            ],
        },
        {
            "id": "1-7",
            "title": "패키지 설치",
            "subtitle": "소스 코드 직접 컴파일의 어려움에서 출발해 패키지, 저장소, APT, dpkg, update와 upgrade, remove와 purge, 의존성 정리, 실제 설치 실습을 정리한다.",
            "tags": ["apt", "dpkg", "repository", "패키지 관리"],
            "objectives": [
                "패키지가 배포판 환경에 맞게 미리 컴파일되어 제공되는 이유를 이해한다.",
                "APT가 저장소, 로컬 캐시, dpkg, 의존성 계산을 연결해 설치를 편하게 해 주는 상위 도구임을 설명한다.",
                "`apt update`, `apt install`, `apt remove`, `apt purge`, `apt autoremove`, `apt upgrade`, `apt full-upgrade`의 차이를 구분한다.",
                "Ubuntu 저장소의 main, universe, restricted, multiverse와 security, updates, backports의 의미를 정리한다.",
                "`/etc/apt`, `/var/cache/apt/archives`, `/var/lib/apt/lists`, `dpkg -i`, `do-release-upgrade`가 어떤 상황에서 등장하는지 이해한다.",
            ],
            "sections": [
                {
                    "heading": "패키지란 무엇인가",
                    "body": f"""
                    <p>패키지는 설치를 쉽게 하기 위해 배포판 환경에 맞춰 미리 컴파일하고 묶어 둔 소프트웨어다. 소프트웨어는 원래 누군가 작성한 소스 코드에서 출발한다. 그 소스 코드가 실제로 실행되려면 컴파일러를 통해 바이너리 실행 파일로 만들어져야 한다. Windows에서는 과거 <code>.exe</code>, 최근에는 <code>.msi</code> 같은 설치 파일을 흔히 보지만, 리눅스는 배포판과 버전이 매우 다양하다.</p>
                    {os07_package_concept}
                    <p>리눅스에는 Ubuntu, Debian, Red Hat, Fedora, CentOS, Arch처럼 많은 배포판이 있고, 각 배포판마다 커널 버전, 기본 라이브러리, 설치된 구성 요소가 다를 수 있다. 어떤 라이브러리는 또 다른 라이브러리를 필요로 한다. 개발자가 지구상의 모든 배포판과 버전에 맞춰 미리 빌드 파일을 제공하는 것은 현실적으로 어렵다.</p>
                    <p>그래서 과거 리눅스 세계에서는 “소스 코드를 줄 테니 각자 자기 환경에 맞게 컴파일해서 쓰라”는 방식이 흔했다. 그러나 일반 사용자가 컴파일러를 설치하고, 버전 충돌을 해결하고, 의존 라이브러리를 직접 찾아 맞추는 일은 어렵다. 이 부담을 줄이기 위해 배포판을 만드는 회사나 커뮤니티가 유용한 프로그램을 자기 배포판 환경에 맞게 미리 컴파일하고, 압축하고, 설치 스크립트와 메타데이터를 붙여 서버에 올려 둔다. 이것이 패키지다.</p>
                    <p>Debian과 Ubuntu 계열은 <code>.deb</code> 패키지를 쓰고, Red Hat 계열은 <code>.rpm</code> 패키지를 쓴다. 이 강의의 Ubuntu에서는 <code>apt</code>와 <code>dpkg</code>를 중심으로 패키지를 설치하고 관리한다.</p>
                    """,
                },
                {
                    "heading": "APT, 저장소, 로컬 캐시, dpkg의 관계",
                    "body": f"""
                    <p><code>apt</code>는 Advanced Package Tool의 약자다. 사용자는 <code>apt install vim</code>처럼 명령을 내리고, apt는 사전에 등록된 저장소(repository)와 로컬 캐시를 참고해 어떤 패키지를 어디에서 받아야 하는지 찾는다. 필요하면 의존 패키지도 함께 계산한다. 실제 <code>.deb</code> 파일을 설치하는 더 낮은 단계에서는 <code>dpkg</code>가 관여한다.</p>
                    {os07_apt_structure}
                    <p>저장소는 공개 저장소일 수도 있고, 사설 저장소일 수도 있다. Canonical이 운영하는 Ubuntu 공식 저장소가 있고, Google Chrome처럼 회사가 자체 저장소를 제공하는 경우도 있으며, 개인이 운영하는 PPA 저장소도 있다. 사용자는 저장소 목록을 등록해 두고, apt는 그 목록을 바탕으로 패키지를 찾는다.</p>
                    {os07_apt_commands}
                    {code_block("""
                    sudo apt update
                    apt list
                    apt list --upgradable
                    apt search tcpdump
                    apt show vim
                    sudo apt install vim
                    sudo apt install tree
                    sudo dpkg -i package-name.deb
                    """, "bash")}
                    <p><code>apt update</code>는 저장소의 최신 패키지 목록을 로컬로 가져온다. <code>apt list</code>와 <code>apt search</code>는 이 로컬 목록을 바탕으로 보여 주거나 검색한다. <code>apt show</code>는 패키지 설명, 버전, 의존성 같은 정보를 확인할 때 사용한다. 오래된 자료에서는 <code>apt-get</code>을 많이 볼 수 있는데, 강의에서는 apt가 사용자 친화적인 상위 도구이고 apt-get은 그보다 낮은 단계의 오래된 명령으로 이해하면 된다고 설명한다.</p>
                    """,
                },
                {
                    "heading": "install, remove, purge, autoremove, upgrade",
                    "body": f"""
                    <p>설치는 <code>apt install</code>이다. apt는 로컬에 캐시된 저장소 목록에서 패키지 위치를 찾고, 실제 URL에서 패키지를 내려받은 뒤, 내부적으로 dpkg를 이용해 설치한다. 패키지를 지울 때는 목적에 따라 명령을 구분해야 한다.</p>
                    {os07_remove_purge}
                    {code_block("""
                    sudo apt install nginx
                    sudo apt remove nginx
                    sudo apt purge nginx
                    sudo apt autoremove
                    """, "bash")}
                    <p><code>apt remove</code>는 실행 파일과 주된 패키지 파일을 제거하지만 설정 파일이나 데이터 파일을 남길 수 있다. 예를 들어 웹 서버를 새 버전으로 바꾸거나 잠시 지웠다가 다시 설치할 때 기존 설정이 남아 있으면 유용하다. 반대로 더 이상 쓰지 않을 소프트웨어를 완전히 정리하려면 <code>apt purge</code>를 사용한다. 강사는 이 차이를 “업그레이드를 위해 잠깐 지우는 것인지, 진짜로 폐기하는 것인지”로 구분해 설명한다.</p>
                    {os07_dependency}
                    <p>패키지는 혼자 설치되지 않는 경우가 많다. A를 설치하려면 B와 C가 필요하고, B는 D와 E를 필요로 할 수 있다. 그런데 나중에 A를 지울 때 B, C, D, E를 무조건 같이 지우면 문제가 생길 수 있다. 다른 패키지 G가 B, D, E를 함께 쓰고 있을 수 있기 때문이다. 그래서 remove나 purge로는 요청한 패키지 중심으로 지우고, 더 이상 아무도 참조하지 않는 의존 패키지는 <code>apt autoremove</code>로 정리한다.</p>
                    {os07_install_upgrade}
                    {code_block("""
                    sudo apt update
                    apt list --upgradable
                    sudo apt upgrade
                    sudo apt full-upgrade
                    """, "bash")}
                    <p>강의에서 가장 강조한 혼동 지점은 <code>apt update</code>다. 이름만 보면 설치된 프로그램을 업데이트하는 것처럼 보이지만, 실제로는 패키지 목록과 주소 정보를 갱신할 뿐이다. 실제 설치된 패키지를 새 버전으로 올리는 명령은 <code>apt upgrade</code>다. <code>apt full-upgrade</code>는 업그레이드 과정에서 패키지 삭제나 더 큰 의존성 변경이 필요할 때까지 처리할 수 있는 더 강한 명령이며, 기초 실습에서는 자주 쓰지 않는다.</p>
                    """,
                },
                {
                    "heading": "GUI 저장소 설정: main, universe, restricted, multiverse",
                    "body": f"""
                    <p>저장소 설정은 CLI 파일로도 볼 수 있지만, Ubuntu Desktop에서는 Software & Updates GUI에서도 확인할 수 있다. GUI 시간에 봤던 화면과 연결해, 어떤 저장소를 사용할지 체크박스로 고를 수 있다.</p>
                    {os07_gui_repo}
                    <table>
                      <thead><tr><th>저장소</th><th>의미</th></tr></thead>
                      <tbody>
                        <tr><td>main</td><td>Canonical이 공식적으로 지원하고 유지보수하는 오픈소스 소프트웨어 저장소</td></tr>
                        <tr><td>universe</td><td>커뮤니티가 유지보수하는 오픈소스 소프트웨어 저장소</td></tr>
                        <tr><td>restricted</td><td>장치 드라이버처럼 벤더가 제공하고 Canonical이 완전히 책임지지 않는 성격의 저장소</td></tr>
                        <tr><td>multiverse</td><td>공식 지원 밖의 소프트웨어, 라이선스 제약이나 상용 성격이 섞일 수 있는 저장소</td></tr>
                      </tbody>
                    </table>
                    <p>Other Software 탭에는 추가 저장소가 들어간다. 예를 들어 Chrome을 설치하면 Google이 제공하는 저장소 항목이 추가될 수 있다. 필요에 따라 회사 내부 저장소나 개인 저장소를 추가할 수도 있다.</p>
                    {os07_security_updates}
                    <p>Updates 탭에는 보안 업데이트와 일반 업데이트 정책이 있다. <code>security</code>는 중요한 보안 업데이트를 다루며, 취약점(CVE)이 패치되어 올라오는 채널로 이해할 수 있다. <code>updates</code>는 보안만은 아니지만 안정적인 수정 업데이트를 포함하고, <code>backports</code>는 최신 기능을 구버전 배포판에 가져오는 성격이 있어 안정성 관점에서 더 신중히 봐야 한다. 강사는 보안 업데이트는 체크되어 있어야 한다고 설명한다.</p>
                    """,
                },
                {
                    "heading": "CLI에서 저장소 파일과 업데이트 흐름 확인하기",
                    "body": f"""
                    <p>GUI로 보이는 저장소 설정은 CLI에서는 파일과 디렉토리로 관리된다. 대표 경로는 <code>/etc/apt/</code> 아래다. <code>/etc/apt/sources.list</code>는 기본 저장소 목록을 담고, <code>/etc/apt/sources.list.d/</code>는 추가 저장소 파일을 담는다.</p>
                    {os07_apt_files}
                    {code_block("""
                    ls /etc/apt
                    cat /etc/apt/sources.list
                    ls /etc/apt/sources.list.d
                    ls /var/cache/apt/archives
                    ls /var/lib/apt/lists
                    """, "bash")}
                    <p><code>/var/cache/apt/archives</code>는 내려받은 패키지 파일 캐시와 관련되고, <code>/var/lib/apt/lists</code>는 저장소에서 가져온 패키지 목록과 관련된다. 이 구조를 알고 있으면 <code>apt update</code>가 왜 “목록 갱신”인지 더 명확해진다.</p>
                    {os07_apt_update_demo}
                    {code_block("""
                    sudo apt update
                    apt list --upgradable
                    sudo apt upgrade
                    """, "bash")}
                    <p><code>sudo apt update</code>를 실행하면 여러 저장소에서 목록을 가져오는 출력이 지나간다. 이때 설치된 Vim이나 nginx가 실제로 바뀌는 것이 아니다. 업데이트 가능한 항목은 <code>apt list --upgradable</code>로 확인하고, 실제 업그레이드는 <code>sudo apt upgrade</code>로 실행한다.</p>
                    {os07_apt_upgrade_demo}
                    <p>업그레이드 과정에서는 새 패키지를 내려받고, 압축을 풀고, 기존 버전을 대체하고, 필요한 후처리 스크립트를 실행한다. 강의에서는 “update는 목록 갱신, upgrade는 실제 버전 업그레이드”라는 이름 혼동을 받아들이고 정확히 구분해 쓰라고 정리한다.</p>
                    {os07_autoremove_demo}
                    <p>업그레이드나 삭제 후에는 <code>sudo apt autoremove</code>로 남은 의존성 패키지를 정리할 수 있다. 이 명령은 실무에서 자주 쓰이며, 아무 패키지도 더 이상 필요로 하지 않는 라이브러리나 보조 패키지를 제거한다.</p>
                    {os07_add_repository}
                    {code_block("""
                    sudo add-apt-repository ppa:PPA_REPO_NAME/PPA
                    sudo apt update
                    sudo add-apt-repository --remove ppa:PPA_REPO_NAME/PPA
                    sudo ppa-purge ppa:PPA_REPO_NAME/PPA
                    """, "bash")}
                    <p>개인 저장소는 PPA(Personal Package Archives) 형태로 추가할 수 있다. 저장소를 추가한 뒤에는 보통 <code>apt update</code>로 새 목록을 받아야 검색과 설치가 가능하다. 저장소를 제거할 때는 <code>--remove</code>를 사용하고, PPA에서 설치한 패키지까지 배포판 기본 버전으로 되돌리는 작업에는 <code>ppa-purge</code> 같은 도구를 쓸 수 있다.</p>
                    """,
                },
                {
                    "heading": "잠금 오류, dpkg, 배포판 업그레이드",
                    "body": f"""
                    <p>가끔 <code>apt install</code>을 실행했는데 lock 관련 오류가 날 수 있다. 이는 다른 apt, dpkg, update-manager 프로세스가 패키지 데이터베이스를 사용 중이라는 뜻이다. 패키지 데이터베이스를 두 프로세스가 동시에 고치면 깨질 수 있으므로 잠금 파일로 한 번에 하나만 작업하게 막는다.</p>
                    {os07_lock_issue}
                    {code_block("""
                    ps aux | grep apt
                    ps aux | grep dpkg
                    sudo kill PID
                    sudo dpkg --configure -a
                    """, "bash")}
                    <p>초급 단계에서는 lock 오류가 나면 먼저 기다리는 것이 안전하다. 정말 멈춘 프로세스가 확실할 때만 어떤 프로세스가 잠금을 잡고 있는지 확인하고 종료해야 한다. 종료 후 패키지 설정이 중간에 멈췄다면 <code>sudo dpkg --configure -a</code>로 미완료 설정을 이어갈 수 있다. 함부로 잠금 파일만 삭제하는 방식은 패키지 데이터베이스를 망가뜨릴 수 있으므로 피해야 한다.</p>
                    {os07_dpkg}
                    {code_block("""
                    sudo dpkg -i google-chrome-stable_current_amd64.deb
                    sudo apt install -f
                    dpkg -l
                    dpkg -L google-chrome-stable
                    dpkg -s google-chrome-stable
                    """, "bash")}
                    <p><code>dpkg</code>는 Debian package manager의 낮은 단계 도구다. 저장소에서 검색하고 의존성을 자동 해결하는 일은 apt가 더 잘하지만, 이미 내려받은 <code>.deb</code> 파일을 직접 설치할 때는 <code>dpkg -i</code>가 등장한다. 예전 GUI 강의에서 Chrome <code>.deb</code> 파일을 설치한 흐름과 연결된다. 다만 <code>dpkg -i</code>는 의존성을 자동으로 다 해결하지 못할 수 있으므로, 문제가 나면 <code>sudo apt install -f</code>로 빠진 의존성을 고치는 일이 있다.</p>
                    {os07_release_upgrade}
                    {code_block("""
                    sudo apt update
                    sudo apt upgrade
                    sudo do-release-upgrade
                    """, "bash")}
                    <p><code>do-release-upgrade</code>는 패키지 하나를 올리는 명령이 아니라 Ubuntu 배포판 자체를 다음 릴리스로 올리는 명령이다. 예를 들어 16.04에서 18.04, 18.04에서 20.04처럼 단계적으로 올리는 식이다. 강사는 수업 환경에서는 20.04를 기준으로 맞춰야 하므로 실습 중 배포판 업그레이드를 함부로 진행하지 말라고 설명한다.</p>
                    """,
                },
                {
                    "heading": "실습: openssh-server, vim, tree, htop, sl 설치",
                    "body": f"""
                    <p>강의 마지막은 실제 설치 실습이다. 강사는 화면을 크게 보여 주기 위해 <code>openssh-server</code>를 설치해 원격 접속 환경을 구성한다. 학생들은 동일한 명령을 Ubuntu 터미널에서 따라 하면서, apt가 패키지와 의존 패키지를 내려받고 설치하는 과정을 확인하면 된다.</p>
                    {os07_practice_openssh}
                    {code_block("""
                    sudo apt install -y openssh-server
                    sudo apt install vim
                    sudo apt install tree
                    tree
                    """, "bash")}
                    <p><code>-y</code> 옵션은 설치 중 “계속하시겠습니까?” 같은 질문에 자동으로 yes를 선택한다. 스크립트나 자동화에서는 편리하지만, 무엇이 설치되는지 모르는 상태에서 습관적으로 붙이는 것은 좋지 않다. 처음 배우는 단계에서는 출력에 어떤 의존 패키지가 함께 설치되는지 읽어 보는 것이 좋다.</p>
                    {os07_practice_tree}
                    <p><code>vim</code>은 앞선 편집기 강의에서 언급한 터미널 편집기이고, <code>tree</code>는 디렉토리 구조를 계층형으로 보여 주는 도구다. 설치 전에는 명령을 찾을 수 없지만, 설치 후에는 바로 실행된다. 이것이 패키지 설치가 시스템에 새 명령을 추가하는 가장 직관적인 결과다.</p>
                    {os07_practice_htop}
                    <p><code>htop</code>은 CPU, 메모리, 프로세스 목록을 터미널에서 보기 좋게 보여 주는 도구다. 뒤의 시스템 모니터링 강의와도 연결된다. 패키지를 설치하면 단순히 파일 하나가 생기는 것이 아니라, 실행 파일, 문서, 설정, 의존 라이브러리 등이 함께 관리될 수 있음을 떠올리면 된다.</p>
                    {os07_practice_sl}
                    {code_block("""
                    sudo apt install htop
                    htop
                    sudo apt install sl
                    sl
                    """, "bash")}
                    <p><code>sl</code>은 <code>ls</code>를 잘못 친 사용자를 놀리기 위해 기차 애니메이션을 보여 주는 장난성 패키지다. 중요한 도구는 아니지만, 패키지 설치 후 새 명령이 시스템에 추가되고 바로 실행된다는 점을 가볍게 확인하는 예시다. 강의는 이런 실습을 통해 패키지 설치, 실행, 삭제, 의존성 정리까지 직접 반복해 보라고 마무리한다.</p>
                    """,
                },
            ],
            "checks": [
                "패키지가 배포판 환경에 맞게 미리 컴파일된 소프트웨어 묶음인 이유를 설명할 수 있는가?",
                "Debian/Ubuntu 계열의 `.deb`와 Red Hat 계열의 `.rpm` 차이를 알고 있는가?",
                "apt, apt-get, dpkg, 저장소, 로컬 캐시의 관계를 설명할 수 있는가?",
                "`apt update`가 실제 프로그램 업그레이드가 아니라 저장소 목록 갱신임을 설명할 수 있는가?",
                "`apt install`, `apt remove`, `apt purge`, `apt autoremove`, `apt upgrade`, `apt full-upgrade`를 구분할 수 있는가?",
                "main, universe, restricted, multiverse 저장소의 의미를 이해했는가?",
                "security, updates, backports 업데이트 채널의 차이를 이해했는가?",
                "`/etc/apt/sources.list`, `sources.list.d`, `/var/cache/apt/archives`, `/var/lib/apt/lists`의 역할을 말할 수 있는가?",
                "PPA를 추가한 뒤 `apt update`가 필요한 이유를 설명할 수 있는가?",
                "apt lock 오류가 왜 발생하고, 왜 함부로 잠금 파일만 삭제하면 안 되는지 설명할 수 있는가?",
                "`dpkg -i`로 `.deb` 파일을 설치할 때 apt와 어떤 차이가 있는지 이해했는가?",
                "`do-release-upgrade`가 일반 패키지 업그레이드가 아니라 배포판 업그레이드임을 구분할 수 있는가?",
                "`openssh-server`, `vim`, `tree`, `htop`, `sl` 설치 실습에서 패키지 설치 전후 명령 실행 결과가 왜 달라지는지 설명할 수 있는가?",
            ],
        },
        {
            "id": "1-8",
            "title": "데몬서비스 관리",
            "transcript_title": "데몬서비스 관리",
            "subtitle": "백그라운드 데몬과 서비스 개념에서 출발해 systemd, systemctl, journalctl, target, start/stop, enable/disable, Nginx 실습까지 연결한다.",
            "tags": ["systemd", "systemctl", "Nginx"],
            "objectives": [
                "데몬과 서비스의 의미, 그리고 두 개념이 실제 서버 프로그램에서 어떻게 겹치는지 이해한다.",
                "과거 System V init/service 명령과 현재 systemd/systemctl 방식의 차이를 설명한다.",
                "runlevel과 systemd target의 대응 관계, systemd unit의 기본 종류를 파악한다.",
                "systemctl의 status, start, stop, restart, reload, enable, disable, mask, unmask를 구분한다.",
                "journalctl로 서비스 로그를 확인하고 로그 레벨과 로그 용량 관리 필요성을 이해한다.",
                "Nginx를 설치해 active/inactive 상태, curl/브라우저 응답, sudo 권한, 자동 시작 여부를 실습한다.",
            ],
            "sections": [
                {
                    "heading": "데몬과 서비스: 백그라운드에서 요청을 기다리는 프로그램",
                    "body": f"""
                    <p>강의는 온라인 운영체제 기초 강의의 마지막 범위로, 앞에서 설치한 여러 서버 프로그램과 데몬 서비스를 관리하는 방법을 다룬다. 데몬(daemon)은 사용자가 직접 화면에서 조작하지 않아도 백그라운드에서 계속 돌면서 특정 작업을 수행하는 프로그램이다. 서비스(service)는 주로 서버-클라이언트 모델에서 사용자의 요청을 기다렸다가 응답하는 프로그램을 뜻한다.</p>
                    {os08_daemon_service}
                    <p>둘은 완전히 분리된 개념이라기보다 많이 겹친다. 웹 서버는 사용자가 언제 접속할지 모르기 때문에 백그라운드에서 계속 대기하고, 요청이 들어오면 응답한다. FTP 파일 서버도 마찬가지다. 네트워크 서비스가 아니어도 프린터 서비스처럼 사용자가 문서에서 인쇄를 누를 때까지 백그라운드에서 기다렸다가 프린터 하드웨어로 작업을 전달하는 프로그램도 있다.</p>
                    <p>이런 서비스는 리눅스에만 있는 것이 아니다. Windows 작업 관리자에서도 서비스 탭을 보면 수많은 서비스가 백그라운드에서 실행 중인 것을 볼 수 있다. 리눅스 운영을 하려면 이런 백그라운드 서비스가 현재 켜져 있는지, 꺼져 있는지, 부팅 때 자동으로 올라오는지, 로그는 어디에 남는지 다룰 수 있어야 한다.</p>
                    """,
                },
                {
                    "heading": "service 명령에서 systemctl로",
                    "body": f"""
                    <p>고전적인 리눅스 배포판에서는 System V init 방식과 <code>service</code> 명령으로 서비스를 관리했다. 인터넷에서 오래된 블로그를 검색하면 <code>service ssh status</code>, <code>service nginx restart</code> 같은 명령을 많이 볼 수 있다. 지금도 호환성을 위해 동작하는 경우가 있지만, Ubuntu 16.04 이후의 현대적인 관리 방식은 <code>systemctl</code>이다.</p>
                    {os08_service_legacy}
                    <p>강사는 <code>service</code> 명령만 소개하는 자료는 오래된 자료일 가능성이 높으므로, 현재 Ubuntu 기준으로는 <code>systemctl</code>을 중심으로 공부하라고 말한다. 서비스 이름의 정식 단위는 <code>sshd.service</code>, <code>nginx.service</code>처럼 <code>.service</code>가 붙지만, 실무 명령에서는 보통 <code>systemctl status nginx</code>처럼 접미사를 생략해도 동작한다.</p>
                    {os08_systemctl_status}
                    {code_block("""
                    systemctl status ssh.service
                    systemctl status ssh
                    sudo systemctl start nginx
                    sudo systemctl stop nginx
                    sudo systemctl restart nginx
                    sudo systemctl reload nginx
                    """, "bash")}
                    <p><code>status</code>는 상태 확인, <code>start</code>는 시작, <code>stop</code>은 중지, <code>restart</code>는 재시작이다. 설정 파일만 다시 읽어도 되는 서비스는 <code>reload</code>를 쓸 수 있다. 실행 상태를 바꾸는 명령은 시스템 전체에 영향을 줄 수 있으므로 보통 관리자 권한이 필요하다.</p>
                    """,
                },
                {
                    "heading": "init, systemd, target, unit",
                    "body": f"""
                    <p>그렇다면 많은 데몬 서비스는 누가 처음 실행해 줄까? 과거에는 <code>init</code> 프로세스가 시스템 부팅 과정에서 여러 서비스를 순서대로 띄웠다. 현재 Ubuntu에서는 그 역할을 <code>systemd</code>가 맡는다. systemd가 서비스를 실행하고, 사용자는 <code>systemctl</code> 명령으로 systemd에게 시작·중지·상태 확인을 요청한다.</p>
                    {os08_systemd_init}
                    <p>고전적인 init 시스템에는 runlevel이라는 숫자 개념이 있었다. <code>init 0</code>은 전원 끄기, <code>init 1</code>은 복구 모드, <code>init 3</code>은 멀티유저 텍스트 모드, <code>init 5</code>는 GUI 모드처럼 이해한다. 숫자만 보면 직관적이지 않기 때문에 systemd에서는 이를 글자 기반 target으로 표현한다.</p>
                    {os08_targets}
                    <table>
                      <thead><tr><th>고전 runlevel</th><th>systemd target</th><th>의미</th></tr></thead>
                      <tbody>
                        <tr><td>0</td><td>poweroff.target</td><td>전원 끄기</td></tr>
                        <tr><td>1</td><td>rescue.target</td><td>복구 모드</td></tr>
                        <tr><td>3</td><td>multi-user.target</td><td>여러 사용자 텍스트 기반 서버 모드</td></tr>
                        <tr><td>5</td><td>graphical.target</td><td>GUI 포함 일반 사용자 모드</td></tr>
                        <tr><td>6</td><td>reboot.target</td><td>재부팅</td></tr>
                      </tbody>
                    </table>
                    {os08_units}
                    <p>systemd는 서비스만 관리하지 않는다. <code>service</code> 외에도 <code>socket</code>, <code>device</code>, <code>mount</code>, <code>automount</code>, <code>swap</code>, <code>target</code>, <code>path</code>, <code>timer</code>, <code>slice</code>, <code>scope</code> 같은 unit을 다룬다. 기초반에서는 이 모든 unit을 깊게 다루지는 않지만, systemd가 “서비스 하나 켜고 끄는 도구”보다 더 넓은 시스템 관리 프레임워크라는 점을 기억하면 된다.</p>
                    {code_block("""
                    systemctl list-units
                    systemctl list-units --type=service
                    systemctl get-default
                    sudo systemctl set-default multi-user.target
                    sudo systemctl set-default graphical.target
                    """, "bash")}
                    """,
                },
                {
                    "heading": "journalctl과 로그 레벨",
                    "body": f"""
                    <p>서비스는 실행 중에 상태 변화와 오류를 로그로 남긴다. systemd 환경에서는 <code>journalctl</code>로 journal 로그를 볼 수 있다. 서비스가 왜 시작되지 않았는지, 언제 중지되었는지, 어떤 포트에서 대기 중인지 같은 정보가 로그에 남는다.</p>
                    {os08_journal}
                    {code_block("""
                    journalctl
                    journalctl -u nginx
                    journalctl -u nginx --since today
                    journalctl -xe
                    journalctl --disk-usage
                    """, "bash")}
                    <p><code>-u nginx</code>는 특정 unit의 로그만 보는 옵션이고, <code>--since today</code>는 오늘 이후 로그만 보는 식으로 시간을 제한한다. <code>-xe</code>는 최근 오류와 설명을 보는 데 자주 등장한다. 로그는 장애 분석에 매우 중요하지만 계속 쌓이면 디스크를 차지한다. 장애가 많이 나서 로그가 폭증하고, 그 로그 때문에 디스크가 꽉 차 2차 장애가 날 수도 있으므로 로그 용량도 관리 대상이다.</p>
                    <p>로그 레벨은 심각도에 따라 나뉜다. 강의 화면은 <code>emerg</code>, <code>alert</code>, <code>crit</code>, <code>err</code>, <code>warning</code>, <code>notice</code>, <code>info</code>, <code>debug</code> 같은 레벨을 보여 준다. 운영자는 단순 정보 로그인지, 즉시 대응해야 하는 장애 로그인지 구분해서 읽어야 한다.</p>
                    """,
                },
                {
                    "heading": "실습 준비: SSH 상태와 Nginx 설치",
                    "body": f"""
                    <p>실습은 앞 시간에 설치한 SSH 데몬의 상태를 확인하는 것에서 시작한다. <code>systemctl status ssh.service</code> 또는 <code>systemctl status ssh</code>를 실행하면 서비스가 loaded 되었는지, active running 상태인지, 어떤 PID로 떠 있는지, 최근 로그가 무엇인지 한 화면에서 확인할 수 있다.</p>
                    {os08_ssh_status}
                    {code_block("""
                    systemctl status ssh.service
                    systemctl status ssh
                    """, "bash")}
                    <p>다음으로 웹 서버 Nginx를 설치한다. 설치 과정에서 추가 의존 패키지가 함께 설치된다. 리눅스에서 <code>Y/n</code> 또는 <code>y/N</code> 질문이 나오면 대문자로 표시된 값이 기본값이다. 즉 <code>Y/n</code>에서 그냥 Enter를 누르면 yes가 선택된다. 이 질문을 생략하려고 앞 강의에서 배운 <code>-y</code> 옵션을 붙일 수 있다.</p>
                    {os08_nginx_install}
                    {code_block("""
                    sudo apt install nginx
                    sudo apt install -y nginx
                    systemctl status nginx
                    """, "bash")}
                    {os08_nginx_status_active}
                    <p>설치가 끝난 뒤 <code>systemctl status nginx</code>를 실행하면 <code>active (running)</code> 상태를 확인할 수 있다. 상태 화면에는 서비스 파일 위치, enabled/disabled 여부, Main PID, 프로세스 트리, 최근 로그가 함께 표시된다. 강의 중 오타가 한 번 나오지만, 올바른 명령은 <code>systemctl status nginx</code>다.</p>
                    """,
                },
                {
                    "heading": "Nginx 응답 확인: curl과 브라우저",
                    "body": f"""
                    <p>Nginx가 실행 중이면 로컬 웹 서버가 80번 포트에서 HTTP 요청을 기다린다. GUI 브라우저에서 <code>localhost</code>를 열어도 되고, 서버 환경처럼 GUI가 없는 곳에서는 <code>curl localhost</code>로 HTML 응답을 확인할 수 있다.</p>
                    {os08_curl_browser}
                    {code_block("""
                    sudo apt install curl
                    curl localhost
                    # 브라우저 주소창에서도 localhost 입력
                    """, "bash")}
                    <p><code>curl localhost</code> 결과는 보기 좋은 웹페이지가 아니라 HTML 코드로 나온다. 브라우저도 실제로는 이 HTML을 받아 태그를 해석하고, 색상과 크기와 배치를 적용해 사람이 보기 좋은 페이지로 렌더링한다. 브라우저에서 페이지 소스 보기를 하면 curl로 받은 내용과 같은 HTML을 확인할 수 있다.</p>
                    """,
                },
                {
                    "heading": "stop, start, active, inactive",
                    "body": f"""
                    <p>이제 잘 동작하는 웹 서버를 중지해 본다. 일반 사용자가 아무 서비스나 마음대로 끄면 안 되므로, <code>systemctl stop nginx</code>를 일반 권한으로 실행하면 권한 문제가 발생한다. 관리자 권한을 빌려 <code>sudo systemctl stop nginx</code>를 실행해야 한다.</p>
                    {os08_stop_permission}
                    {code_block("""
                    systemctl status nginx
                    sudo systemctl stop nginx
                    systemctl status nginx
                    curl localhost
                    """, "bash")}
                    {os08_nginx_inactive}
                    <p>리눅스 명령은 성공했을 때 별도 메시지를 주지 않는 경우가 많다. <code>sudo systemctl stop nginx</code> 뒤 아무 메시지가 없으면 보통 성공한 것으로 보고, <code>systemctl status nginx</code>로 확인한다. 중지된 서비스는 <code>inactive</code> 상태가 되고, <code>curl localhost</code>는 연결할 서버가 없어 실패한다. 브라우저에서 새로고침해도 Nginx 기본 페이지가 뜨지 않는다.</p>
                    {os08_start_again}
                    {code_block("""
                    sudo systemctl start nginx
                    systemctl status nginx
                    curl localhost
                    """, "bash")}
                    <p><code>sudo systemctl start nginx</code>로 다시 켜면 상태가 <code>active (running)</code>으로 돌아오고, curl과 브라우저 응답도 다시 살아난다. 이 실습의 핵심은 “서비스 상태”와 “실제 네트워크 응답”을 함께 확인하는 것이다. 상태만 보지 말고 실제 요청이 성공하는지도 확인해야 한다.</p>
                    """,
                },
                {
                    "heading": "enable과 disable: 지금 켜짐과 부팅 시 자동 시작은 다르다",
                    "body": f"""
                    <p><code>start</code>와 <code>stop</code>은 현재 실행 상태를 바꾼다. 반면 <code>enable</code>과 <code>disable</code>은 부팅할 때 자동으로 시작할지 여부를 바꾼다. 그래서 현재 실행 중이지만 disabled일 수 있고, 현재 꺼져 있지만 enabled일 수도 있다.</p>
                    {os08_enable_disable}
                    <table>
                      <thead><tr><th>상태 조합</th><th>의미</th></tr></thead>
                      <tbody>
                        <tr><td>active + enabled</td><td>지금 실행 중이고, 재부팅 후에도 자동 실행된다.</td></tr>
                        <tr><td>inactive + enabled</td><td>지금은 꺼져 있지만, 재부팅하면 자동 실행된다.</td></tr>
                        <tr><td>active + disabled</td><td>지금은 켜져 있지만, 재부팅 후 자동 실행되지는 않는다.</td></tr>
                        <tr><td>inactive + disabled</td><td>지금도 꺼져 있고, 재부팅해도 자동 실행되지 않는다.</td></tr>
                      </tbody>
                    </table>
                    {code_block("""
                    sudo systemctl enable nginx
                    sudo systemctl disable nginx
                    systemctl status nginx
                    sudo systemctl restart nginx
                    sudo systemctl mask nginx
                    sudo systemctl unmask nginx
                    """, "bash")}
                    <p><code>enable</code>은 부팅 시 자동 시작을 등록하고, <code>disable</code>은 자동 시작 등록을 해제한다. <code>restart</code>는 stop 후 start를 한 번에 하는 명령이다. <code>mask</code>는 서비스를 숨기거나 실행되지 못하게 강하게 막는 기능이고, <code>unmask</code>는 다시 풀어 준다. 기초 실습에서는 start/stop/status/enable/disable을 확실히 구분하는 것이 우선이다.</p>
                    {os08_reboot_check}
                    <p>강의 마지막 실습은 재부팅 후 상태 확인으로 이어진다. disable된 서비스는 지금 active로 실행 중이어도 재부팅하면 자동으로 올라오지 않을 수 있다. 반대로 enabled인 서비스는 지금 stop되어 있어도 다음 부팅 때 자동으로 시작될 수 있다. 서비스 운영에서는 “현재 상태”와 “부팅 정책”을 반드시 따로 확인해야 한다.</p>
                    """,
                },
            ],
            "checks": [
                "데몬과 서비스의 차이와 겹치는 지점을 웹 서버, 파일 서버, 프린터 서비스 예로 설명할 수 있는가?",
                "오래된 `service` 명령과 현재 Ubuntu의 `systemctl` 명령을 구분할 수 있는가?",
                "init, systemd, systemctl의 관계를 말할 수 있는가?",
                "runlevel 0/1/3/5/6과 poweroff/rescue/multi-user/graphical/reboot target의 관계를 이해했는가?",
                "systemd가 service 외에도 socket, mount, timer 같은 unit을 관리한다는 점을 이해했는가?",
                "`systemctl status`, `start`, `stop`, `restart`, `reload`의 역할을 구분할 수 있는가?",
                "`journalctl -u nginx`, `--since today`, `-xe`, `--disk-usage`가 어떤 상황에서 쓰이는지 설명할 수 있는가?",
                "Nginx 설치 후 `systemctl status nginx`에서 loaded, active, Main PID, 최근 로그를 읽을 수 있는가?",
                "`curl localhost` 결과와 브라우저의 `localhost` 화면이 같은 웹 응답을 다른 방식으로 보여 준다는 점을 이해했는가?",
                "일반 사용자로 서비스 stop/start가 실패하고 `sudo systemctl`이 필요한 이유를 설명할 수 있는가?",
                "Nginx를 stop하면 inactive가 되고 curl/브라우저 응답이 실패하며, start하면 active와 응답이 돌아오는 흐름을 설명할 수 있는가?",
                "`start/stop`과 `enable/disable`의 차이, active+disabled 같은 조합의 의미를 말할 수 있는가?",
            ],
        },
        {
            "id": "1-9",
            "title": "서버프로그램 설치 및 관리",
            "transcript_title": "서버프로그램 설치 및 관리",
            "subtitle": "웹 서버, FTP 파일 서버, MySQL 데이터베이스 서버를 설치하고 설정 파일, 심볼릭 링크, 서비스 재시작, 접속 확인까지 한 흐름으로 실습한다.",
            "tags": ["Nginx", "Apache", "vsftpd", "MySQL"],
            "objectives": [
                "서버 프로그램 운영의 공통 흐름인 패키지 설치, 설정 파일 수정, 서비스 재시작, 접속 확인을 이해한다.",
                "Apache와 Nginx의 이름 차이, 설정 파일 위치, 가상 호스트, sites-available/sites-enabled 구조를 설명한다.",
                "Nginx에서 새 사이트 설정을 복사·수정하고, 포트 충돌을 nginx -t와 systemctl status로 확인하는 법을 익힌다.",
                "vsftpd를 설치하고 FTP 접속, 다운로드, 업로드 권한, chroot 제한, UTF-8/클라이언트 문제를 이해한다.",
                "MySQL 서버를 설치하고 sudo mysql로 접속한 뒤 데이터베이스, DB 사용자, 권한 부여, 테이블 생성 흐름을 파악한다.",
            ],
            "sections": [
                {
                    "heading": "시즌2의 시작: 서버 프로그램을 직접 운영하기",
                    "body": f"""
                    <p>이번 강의는 시즌2의 첫 강의다. 시즌1에서는 운영체제가 무엇인지, Linux와 Ubuntu가 무엇인지, 가상 머신에 Ubuntu를 설치하는 법, GUI와 CLI를 다루는 법, 파일과 디렉토리, 사용자 계정과 권한, 패키지 설치, 데몬 서비스 관리를 배웠다. 이제 그 위에 실제 서버 프로그램을 설치하고 운영하는 내용을 얹는다.</p>
                    {os09_season2_outline}
                    <p>강사는 일부 설정이 온라인 강의만으로 따라 하기 어려울 수 있으므로, 영상을 멈추고 다시 재생하면서 직접 커맨드라인을 쳐 보라고 당부한다. 이 강의의 큰 축은 세 가지다. 첫째 웹 서버 구축, 둘째 파일 서버 구축, 셋째 데이터베이스 서버 구축이다. 세 영역은 모두 “패키지 설치 -> 설정 파일 확인과 수정 -> 서비스 재시작 -> 실제 접속 확인”이라는 공통 흐름을 가진다.</p>
                    """,
                },
                {
                    "heading": "웹 서버: Apache와 Nginx의 이름과 구조",
                    "body": f"""
                    <p>웹 서버의 대표 프로그램은 Apache와 Nginx다. Apache는 더 오래된 역사와 전통을 가진 웹 서버다. Red Hat/Fedora 계열에서는 <code>httpd</code>라는 이름으로 부르고, Debian/Ubuntu 계열에서는 <code>apache2</code>라는 패키지와 서비스 이름으로 다룬다. Nginx는 Apache보다 늦게 나온 후발 주자지만, 최근 실무에서 매우 많이 쓰인다.</p>
                    {os09_web_compare}
                    <p>이론 설명은 Apache의 구조에서 출발한다. 많은 웹 서버 설정 구조가 Apache에서 먼저 정리되었고, Nginx도 유사한 방식으로 sites-available과 sites-enabled 구조를 사용한다. 다만 실습 시간은 제한되어 있으므로 실제 조작은 Nginx 중심으로 진행한다.</p>
                    {os09_apache_structure}
                    {code_block("""
                    sudo apt install apache2
                    systemctl status apache2
                    sudo systemctl start apache2
                    sudo systemctl stop apache2
                    sudo systemctl restart apache2
                    """, "bash")}
                    <p>Apache의 메인 설정은 <code>/etc/apache2/apache2.conf</code>에 있고, 사이트 설정은 <code>/etc/apache2/sites-available/</code>과 <code>/etc/apache2/sites-enabled/</code> 구조로 관리한다. 웹 콘텐츠의 기본 위치는 <code>/var/www/html</code>이고, 로그는 <code>/var/log/apache2/</code>에 쌓인다. 설정 파일은 <code>/etc</code>, 변동 데이터와 로그는 <code>/var</code> 아래에 둔다는 앞 강의의 파일시스템 구조와 연결된다.</p>
                    {os09_sites_available}
                    <p>하나의 웹 서버 프로그램이 여러 사이트를 운영할 수 있다. 이것을 가상 호스트, virtual host라고 부른다. 예를 들어 site1, site2, site3 설정 파일을 <code>sites-available</code>에 만들어 두고, 실제 켤 사이트만 <code>sites-enabled</code>에 심볼릭 링크로 연결한다. 여기서 5강의 <code>ln -s</code>가 실제 서버 운영에 쓰인다. “설정 후보는 available에 보관하고, 활성화는 enabled의 링크로 결정한다”는 구조를 기억하면 된다.</p>
                    {os09_apache_default}
                    <p>Apache를 설치하고 서비스가 실행되면 브라우저에서 Apache2 Ubuntu Default Page를 볼 수 있다. 이것은 웹 서버가 포트를 열고, 요청을 받고, 기본 문서 루트의 HTML을 반환한다는 뜻이다.</p>
                    """,
                },
                {
                    "heading": "Nginx 설치와 설정 파일 읽기",
                    "body": f"""
                    <p>Nginx도 Apache와 유사한 설정 구조를 가진다. 패키지는 <code>sudo apt install nginx</code>로 설치하고, 상태는 <code>systemctl status nginx</code>로 확인한다. 강사는 VirtualBox 안에서 직접 볼 수도 있고, Windows 호스트에서 VM의 호스트 전용 어댑터 IP로 접속할 수도 있다고 설명한다. 예시 화면의 IP는 강사의 환경 기준이며, 학생의 VM IP는 다를 수 있다.</p>
                    {os09_nginx_structure}
                    {os09_vm_network}
                    {os09_nginx_status}
                    {code_block("""
                    sudo apt install nginx
                    systemctl status nginx
                    curl localhost
                    # VM 안 브라우저: http://127.0.0.1
                    # 호스트 PC 브라우저: http://<Ubuntu_VM_IP>
                    """, "bash")}
                    <p>Nginx의 메인 설정 파일은 <code>/etc/nginx/nginx.conf</code>다. 이 파일에는 worker 설정, 로그 위치, gzip, SSL 관련 기본 설정, 그리고 다른 설정 파일을 불러오는 <code>include</code> 구문이 있다. 특히 <code>include /etc/nginx/sites-enabled/*;</code>가 중요하다. Nginx는 <code>sites-available</code>을 직접 읽는 것이 아니라, <code>sites-enabled</code> 안에 활성화된 링크를 읽는다.</p>
                    {os09_nginx_conf}
                    <table>
                      <thead><tr><th>경로</th><th>의미</th></tr></thead>
                      <tbody>
                        <tr><td><code>/etc/nginx/nginx.conf</code></td><td>Nginx 메인 설정 파일</td></tr>
                        <tr><td><code>/etc/nginx/sites-available/default</code></td><td>사이트별 실제 설정 파일</td></tr>
                        <tr><td><code>/etc/nginx/sites-enabled/default</code></td><td>활성화된 설정을 가리키는 심볼릭 링크</td></tr>
                        <tr><td><code>/var/www/html</code></td><td>기본 웹 콘텐츠 루트</td></tr>
                        <tr><td><code>/var/log/nginx/</code></td><td>접속 로그와 오류 로그 위치</td></tr>
                      </tbody>
                    </table>
                    {os09_nginx_default}
                    {code_block("""
                    cd /etc/nginx
                    cat nginx.conf
                    ls -l sites-enabled
                    cat sites-available/default
                    cat /var/www/html/index.nginx-debian.html
                    """, "bash")}
                    <p><code>sites-available/default</code>의 <code>server</code> 블록에는 <code>listen</code>, <code>root</code>, <code>index</code>, <code>server_name</code>, <code>location</code> 설정이 들어 있다. <code>listen 80</code>은 80번 포트를 열겠다는 의미이고, <code>root /var/www/html;</code>은 요청한 파일을 찾을 기본 웹 루트다. <code>index index.html index.htm ...</code>은 디렉토리에 접근했을 때 기본으로 찾을 파일 이름이다.</p>
                    """,
                },
                {
                    "heading": "새 Nginx 가상 사이트 만들기와 포트 충돌 해결",
                    "body": f"""
                    <p>새 사이트를 만들 때는 기존 <code>default</code> 설정을 복사해서 출발할 수 있다. 강사는 <code>sites-available/default</code>를 <code>whiteschool</code>이라는 이름으로 복사한 뒤, 주석을 지우고 필요한 설정만 남긴다. Vim에서 <code>dd</code>는 한 줄 삭제, <code>10dd</code>는 10줄 삭제처럼 쓸 수 있다.</p>
                    {os09_symlink_activate}
                    {code_block("""
                    cd /etc/nginx/sites-available
                    sudo cp default whiteschool
                    sudo vi whiteschool
                    cd /etc/nginx/sites-enabled
                    sudo ln -s /etc/nginx/sites-available/whiteschool
                    ls -l
                    sudo systemctl restart nginx
                    """, "bash")}
                    <p>여기서 바로 재시작하면 오류가 날 수 있다. 복사한 설정 파일도 <code>listen 80</code>이고, 기존 default 설정도 <code>listen 80</code>이면 하나의 서버에서 같은 IP와 같은 포트를 두 설정이 동시에 잡으려 하기 때문이다. <code>systemctl status nginx</code>나 <code>journalctl -u nginx</code>를 보면 “80 포트를 이미 사용 중”이라는 bind 오류를 확인할 수 있다.</p>
                    {os09_port_conflict}
                    {os09_nginx_test}
                    {code_block("""
                    sudo nginx -t
                    sudo vi /etc/nginx/sites-available/whiteschool
                    # listen 80; 을 listen 8000; 등으로 변경
                    sudo nginx -t
                    sudo systemctl restart nginx
                    curl localhost:8000
                    """, "bash")}
                    <p><code>sudo nginx -t</code>는 Nginx 설정 문법과 기본적인 충돌을 재시작 전에 검사한다. 설정에 문제가 없으면 <code>syntax is ok</code>, <code>test is successful</code>처럼 나온다. 오류가 있으면 어느 파일의 몇 번째 줄인지 알려 주므로, 재시작 전에 반드시 확인하는 습관을 들여야 한다.</p>
                    {os09_custom_page}
                    {code_block("""
                    sudo mkdir -p /var/www/html/whiteschool
                    echo '<h1>Hello, WHS</h1>' | sudo tee /var/www/html/whiteschool/index.html
                    sudo vi /etc/nginx/sites-available/whiteschool
                    # root /var/www/html/whiteschool; 로 변경
                    sudo nginx -t
                    sudo systemctl restart nginx
                    curl localhost
                    curl localhost:8000
                    """, "bash")}
                    <p>80번 포트의 기본 사이트는 기존 Nginx 기본 페이지를 보여 주고, 8000번 포트의 새 사이트는 <code>Hello, WHS</code> 같은 별도 콘텐츠를 보여 줄 수 있다. 이 실습은 하나의 서버 안에서 여러 사이트를 설정 파일과 포트로 나누어 운영할 수 있음을 보여 준다.</p>
                    """,
                },
                {
                    "heading": "FTP 파일 서버와 vsftpd",
                    "body": f"""
                    <p>웹 서버 다음은 파일 서버다. 강의에서는 대표적인 FTP 서버로 <code>vsftpd</code>를 사용한다. FTP는 과거 문서, 유틸리티, 배포판 이미지, MP3, 영상 파일을 업로드·다운로드하는 데 많이 쓰였던 파일 전송 프로토콜이다. 지금은 SFTP, 클라우드 스토리지, 웹 기반 파일 공유가 더 많이 쓰이지만, 서버와 클라이언트, 계정, 권한, 디렉토리 제한을 배우는 데 좋은 예제다.</p>
                    {os09_ftp_intro}
                    <p>웹 서버처럼 설정 파일이 항상 폴더 구조를 갖는 것은 아니다. Apache와 Nginx는 설정이 많아 <code>/etc/apache2/</code>, <code>/etc/nginx/</code> 아래 여러 파일과 폴더를 쓰지만, vsftpd는 기본 설정이 비교적 단순해 <code>/etc/vsftpd.conf</code> 단일 파일을 중심으로 관리한다. 설정 파일 구조는 Ubuntu가 임의로 정한다기보다 각 서버 프로그램을 만든 쪽의 설계에 따라 달라진다.</p>
                    {os09_filezilla}
                    <p>FTP 클라이언트는 Ubuntu와 Windows에 기본 CLI 명령으로 들어 있을 수 있고, GUI 클라이언트로 FileZilla 같은 서드파티 도구도 있다. Ubuntu 내부 FTP CLI에서는 한글 파일명이 깨질 수 있고, GUI 클라이언트에서도 설정에 따라 깨질 수 있다. 이런 경우 서버의 UTF-8 관련 설정을 조정하고 서비스를 재시작해 확인한다.</p>
                    {os09_ftp_config_theory}
                    <p>vsftpd의 주요 설정은 다음처럼 이해한다. <code>anonymous_enable</code>은 익명 접속 허용 여부, <code>local_enable</code>은 로컬 OS 계정 접속 허용 여부, <code>write_enable</code>은 업로드·삭제 같은 쓰기 작업 허용 여부, <code>chroot_local_user</code>는 사용자를 홈 디렉토리 밖으로 나가지 못하게 가두는 설정이다. 쓰기 권한은 업로드뿐 아니라 삭제와 변경까지 가능하게 하므로 기본값이 꺼져 있는 이유를 이해해야 한다.</p>
                    """,
                },
                {
                    "heading": "FTP 실습: 접속, 다운로드, 업로드, chroot",
                    "body": f"""
                    <p>실습에서는 먼저 vsftpd가 설치되어 있지 않음을 <code>systemctl status vsftpd</code>로 확인한 뒤 설치한다. 설치 중 systemd에 서비스가 등록되고, 설치 후에는 active running 상태가 된다.</p>
                    {os09_vsftpd_status}
                    {code_block("""
                    systemctl status vsftpd
                    sudo apt install vsftpd
                    systemctl status vsftpd
                    ftp 127.0.0.1
                    """, "bash")}
                    {os09_ftp_local_login}
                    <p>Ubuntu 안에서 <code>ftp 127.0.0.1</code>로 접속하면 현재 로그인한 사용자 <code>user1</code>이 기본 사용자명처럼 들어갈 수 있다. 비밀번호를 입력하면 user1의 홈 디렉토리를 볼 수 있고, <code>ls</code>, <code>pwd</code>, <code>get</code>, <code>put</code>, <code>cd</code> 같은 FTP 명령을 사용할 수 있다. 로컬에서 만든 <code>hello.txt</code>가 FTP 접속에서도 보이는 것을 통해, FTP가 OS 사용자 홈 디렉토리를 보여 주고 있음을 확인한다.</p>
                    {os09_ftp_windows_get}
                    {code_block("""
                    # Windows 또는 다른 클라이언트에서
                    ftp <Ubuntu_VM_IP>
                    user1
                    get hello.txt
                    quit
                    type hello.txt
                    """, "bash")}
                    <p>Windows에서 접속할 때 <code>127.0.0.1</code>은 Windows 자신을 의미하므로 Ubuntu VM에 접속되지 않는다. VM의 호스트 전용 어댑터 IP로 접속해야 한다. Ubuntu 안에서 Ubuntu 자신으로 접속할 때와 달리, Windows 클라이언트에서는 사용자명을 직접 입력해야 한다.</p>
                    {os09_ftp_put_denied}
                    <p>기본 설정에서는 업로드가 막혀 있다. Windows에서 메모장으로 <code>myFile.txt</code>를 만들고 FTP에서 <code>put myFile.txt</code>를 실행하면 <code>permission denied</code>가 날 수 있다. 이때 서버의 <code>/etc/vsftpd.conf</code>에서 쓰기 권한을 켜야 한다.</p>
                    {os09_write_enable}
                    {code_block("""
                    sudo vi /etc/vsftpd.conf
                    # /etc/vsftpd.conf 예시
                    write_enable=YES
                    sudo systemctl restart vsftpd
                    systemctl status vsftpd
                    ftp <Ubuntu_VM_IP>
                    put myFile.txt
                    """, "bash")}
                    <p>설정 파일을 바꿨으면 항상 서비스를 재시작해야 한다. 재시작 후 다시 접속하면 <code>put</code> 업로드가 성공하고, 서버 홈 디렉토리에 파일이 생긴 것을 확인할 수 있다.</p>
                    {os09_chroot_config}
                    {code_block("""
                    sudo vi /etc/vsftpd.conf
                    chroot_local_user=YES
                    allow_writeable_chroot=YES
                    sudo systemctl restart vsftpd
                    ftp <Ubuntu_VM_IP>
                    cd ..
                    pwd
                    """, "bash")}
                    <p>처음 상태에서는 FTP 로그인 후 <code>cd ..</code>로 상위 디렉토리로 올라가 시스템의 여러 파일을 볼 수 있다. 이것은 운영 환경에서는 위험하다. <code>chroot_local_user=YES</code>를 켜면 사용자의 홈 디렉토리를 FTP 세션의 루트처럼 만들어 상위로 벗어나지 못하게 할 수 있다. 일부 vsftpd 버전에서는 홈 디렉토리가 쓰기 가능할 때 로그인이 거부될 수 있어 <code>allow_writeable_chroot=YES</code>가 함께 필요하다.</p>
                    {os09_ftp_final}
                    <p>최종적으로 다운로드, 업로드, chroot 제한이 모두 동작하는지 확인한다. 이 강의에서는 모든 FTP 설정을 다 실습하지는 않지만, 익명 접속 허용, 특정 사용자 허용/거부, 화이트리스트/블랙리스트 같은 접근 제어도 설정 파일을 통해 더 확장할 수 있다고 설명한다.</p>
                    """,
                },
                {
                    "heading": "데이터베이스 서버: MySQL 설치와 최초 접속",
                    "body": f"""
                    <p>마지막은 데이터베이스 서버다. DB 서버에는 MySQL, MariaDB, MSSQL, PostgreSQL 등 여러 종류가 있다. 이 강의에서는 가장 대표적인 MySQL을 사용한다. 데이터베이스 수업이 아니므로 SQL 문법을 깊게 다루지는 않고, 리눅스 서버에 DB 서버를 설치하고 서비스 상태를 확인한 뒤 기본 사용자와 권한을 만드는 흐름만 익힌다.</p>
                    {os09_db_types}
                    {os09_mysql_theory}
                    {code_block("""
                    sudo apt install mysql-server
                    sudo mysql_secure_installation
                    systemctl status mysql
                    sudo mysql
                    """, "bash")}
                    <p><code>mysql-server</code> 패키지를 설치하면 서버뿐 아니라 MySQL 클라이언트와 여러 의존 패키지가 함께 설치된다. 설치 중 패키지 목록이 오래되어 다운로드가 실패하면 앞 강의처럼 <code>sudo apt update</code> 후 다시 설치한다. 설치가 끝날 때 systemd에 MySQL 서비스가 등록되는 심볼릭 링크 메시지도 볼 수 있다.</p>
                    {os09_mysql_status}
                    <p><code>mysql_secure_installation</code>은 암호 복잡도, root 암호, 익명 사용자, 원격 root 로그인, 테스트 DB 같은 보안 관련 기본 설정을 조정하는 도구다. 강의에서는 복잡한 정책 없이 기본 실습을 진행하지만, 운영 환경에서는 반드시 보안 설정을 신중히 적용해야 한다. Ubuntu 18.04 이후 흐름에서는 초기 관리 접속을 <code>sudo mysql</code>로 수행한다. 과거 자료에서 보이는 <code>mysql -u root</code> 방식은 버전과 배포판에 따라 다를 수 있다.</p>
                    {os09_mysql_install_demo}
                    """,
                },
                {
                    "heading": "MySQL 내부 사용자, 권한, 테이블 실습",
                    "body": f"""
                    <p>FTP는 Ubuntu의 OS 사용자 계정으로 로그인할 수 있었다. 하지만 MySQL은 DB 내부 사용자와 권한을 따로 관리한다. 따라서 데이터베이스를 만들고, DB 사용자를 만들고, 그 사용자가 어느 위치에서 접속할 수 있는지와 어떤 데이터베이스에 권한을 가질지를 별도로 지정해야 한다.</p>
                    {os09_mysql_console}
                    {code_block("""
                    sudo mysql

                    SHOW DATABASES;
                    CREATE DATABASE whiteschool;
                    CREATE USER 'user1'@'localhost' IDENTIFIED BY 'qwe123';
                    GRANT ALL PRIVILEGES ON whiteschool.* TO 'user1'@'localhost';
                    FLUSH PRIVILEGES;
                    SELECT user, host FROM mysql.user;
                    EXIT;

                    mysql -h localhost -u user1 -p
                    USE whiteschool;
                    """, "sql")}
                    {os09_mysql_user_grant}
                    <p><code>SHOW DATABASES;</code>는 현재 보이는 데이터베이스 목록을 출력한다. <code>CREATE DATABASE whiteschool;</code>은 새 데이터베이스를 만든다. <code>CREATE USER 'user1'@'localhost'</code>는 localhost에서 접속할 수 있는 DB 사용자 user1을 만든다는 뜻이다. 여기서 user1은 Ubuntu OS 사용자 user1과 이름이 같을 수는 있지만 별개의 DB 사용자다.</p>
                    <p><code>GRANT ALL PRIVILEGES ON whiteschool.* TO 'user1'@'localhost';</code>는 user1에게 whiteschool 데이터베이스의 모든 테이블에 대한 권한을 준다. <code>FLUSH PRIVILEGES;</code>는 권한 변경을 반영한다. 그 후 <code>mysql -h localhost -u user1 -p</code>로 새 DB 사용자로 접속해 <code>USE whiteschool;</code>을 실행하면, 해당 데이터베이스 안에서 작업할 수 있다.</p>
                    {os09_mysql_table}
                    {code_block("""
                    CREATE TABLE students (
                      id INT PRIMARY KEY AUTO_INCREMENT,
                      name VARCHAR(50)
                    );
                    INSERT INTO students (name) VALUES ('user1');
                    SHOW TABLES;
                    SELECT * FROM students;
                    """, "sql")}
                    <p>강의는 데이터베이스 문법 자체를 깊게 다루지는 않는다. 중요한 점은 리눅스 서버 운영 관점에서 MySQL도 하나의 서버 프로그램이며, 패키지 설치, 서비스 상태 확인, 초기 접속, 내부 사용자 생성, 권한 부여, 접속 테스트라는 운영 흐름을 가진다는 것이다.</p>
                    """,
                },
            ],
            "checks": [
                "서버 프로그램 운영의 공통 흐름인 설치, 설정 파일 수정, 서비스 재시작, 접속 확인을 설명할 수 있는가?",
                "Apache가 Red Hat 계열에서 httpd, Ubuntu 계열에서 apache2로 불린다는 점과 Nginx의 위치를 이해했는가?",
                "Nginx의 `/etc/nginx/nginx.conf`, `sites-available`, `sites-enabled`, `/var/www/html`, `/var/log/nginx`의 역할을 말할 수 있는가?",
                "sites-enabled가 심볼릭 링크로 활성 사이트를 관리한다는 점을 설명할 수 있는가?",
                "80 포트 중복으로 Nginx 재시작이 실패할 수 있고, `systemctl status`, `journalctl`, `nginx -t`로 원인을 확인할 수 있는가?",
                "새 웹 루트와 `index.html`을 만들고 `listen 8000`, `root /var/www/html/whiteschool` 같은 설정으로 별도 사이트를 띄우는 흐름을 이해했는가?",
                "vsftpd가 `/etc/vsftpd.conf` 단일 설정 파일을 사용하며, FTP 클라이언트 접속에서 로컬호스트와 VM IP의 차이를 구분할 수 있는가?",
                "FTP의 `get`, `put`, `write_enable=YES`, `chroot_local_user=YES`, `allow_writeable_chroot=YES`가 각각 무엇을 하는지 설명할 수 있는가?",
                "FileZilla 같은 GUI FTP 클라이언트와 UTF-8 파일명 문제를 이해했는가?",
                "MySQL 설치 후 `systemctl status mysql`, `sudo mysql`, `mysql_secure_installation`의 역할을 구분할 수 있는가?",
                "MySQL에서 OS 사용자와 DB 사용자가 별도이며, `CREATE USER`, `GRANT`, `FLUSH PRIVILEGES`로 DB 권한을 부여한다는 점을 설명할 수 있는가?",
                "권한을 받은 DB 사용자로 접속해 `USE`, `CREATE TABLE`, `INSERT`, `SHOW TABLES`, `SELECT`를 실행하는 기본 흐름을 이해했는가?",
            ],
        },
        {
            "id": "1-10",
            "title": "개발환경 구축하기",
            "transcript_title": "개발환경 구축하기",
            "subtitle": "C, Python, Jupyter, Java, Docker 개발 환경을 우분투에서 설치하고 버전·권한·디스크 문제까지 함께 다룬다.",
            "tags": ["개발환경", "Python", "Docker"],
            "objectives": [
                "언어별 개발 환경이 컴파일러, 런타임, 버전 관리, 가상 환경, IDE까지 포함한다는 점을 이해한다.",
                "C 개발 도구와 바이너리 분석 도구를 설치하고 hello.c를 컴파일·실행·분석하는 흐름을 익힌다.",
                "Anaconda 설치 전에 디스크 공간을 확인하고 VirtualBox 디스크, 파티션, 파일 시스템을 확장하는 절차를 이해한다.",
                "conda 가상 환경, Jupyter Notebook 실행 옵션, systemd 서비스 등록 개념을 설명할 수 있다.",
                "Java JRE/JDK, update-alternatives, Docker 설치·권한·저장소 관리의 기본 흐름을 이해한다.",
            ],
            "sections": [
                {
                    "heading": "개발 환경은 프로그램 하나가 아니라 전체 작업 조건이다",
                    "body": f"""
                    <p>이번 강의의 주제는 개발 환경 구축이다. 개발 환경은 “언어 하나를 설치했다”에서 끝나지 않는다. C나 Java처럼 오래된 전통적 언어는 컴파일러와 런타임을 명확히 구분해 준비해야 하고, Python이나 JavaScript/npm 같은 현대적 언어는 프로젝트별 가상 환경과 패키지 의존성 관리가 중요하다. 여기에 git, bash, shell, 환경변수, Anaconda, Python venv, Docker, VS Code, Jupyter Notebook 같은 도구가 함께 붙는다.</p>
                    {os10_outline}
                    <p>강사는 이 강의를 C, Python/Anaconda/Jupyter, Java, Docker 순서로 진행한다. 공통 관점은 같다. 먼저 필요한 도구가 Ubuntu 패키지로 있는지 확인하고, 있으면 apt로 설치한다. 패키지가 없거나 더 최신 버전이 필요하면 공식 사이트, curl, dpkg, 설치 스크립트를 사용한다. 설치 후에는 버전 확인, 설정 파일 수정, 권한 설정, 서비스 실행 여부까지 확인해야 개발 환경 구축이 끝난다.</p>
                    """,
                },
                {
                    "heading": "C 개발 환경: build-essential, binutils, hello.c",
                    "body": """
                    <p>C 언어는 역사와 전통이 오래된 언어라 Linux 개발 환경에서 거의 기본처럼 다뤄진다. Ubuntu에서 C 개발에 필요한 기본 도구 묶음은 <code>build-essential</code>이다. 여기에는 C 컴파일러인 <code>gcc</code>, C++ 컴파일러인 <code>g++</code>, 빌드 자동화 도구인 <code>make</code> 등이 포함된다. 바이너리 분석과 관련된 <code>binutils</code>에는 링커 <code>ld</code>, 아카이브 도구 <code>ar</code>, 오브젝트 덤프 도구 <code>objdump</code> 등이 들어 있다.</p>
                    """ + os10_c_tools + """
                    <p>앞서 VirtualBox Guest Additions를 설치할 때 커널 모듈 빌드 때문에 build-essential을 이미 설치한 학생도 있을 수 있다. 그래서 실습 화면에서는 “이미 최신 버전”처럼 보일 수 있다. 없으면 새로 설치하면 되고, 이미 있으면 버전 확인으로 넘어가면 된다.</p>
                    """ + os10_build_install + code_block("""
                    sudo apt install build-essential
                    sudo apt install binutils
                    gcc --version
                    g++ --version
                    make --version
                    """, "bash") + """
                    <p>도구가 준비되면 <code>vim hello.c</code>로 C 파일을 만들고 가장 기본적인 hello world 코드를 작성한다. 이때 <code>#include &lt;stdio.h&gt;</code>는 표준 입출력 함수인 <code>printf</code>를 쓰기 위해 포함하는 헤더다. <code>main</code> 함수에서 <code>printf("hello world\\n");</code>를 호출하고 <code>return 0;</code>으로 정상 종료를 표시한다.</p>
                    """ + os10_hello_code + code_block("""
                    #include <stdio.h>

                    int main(void) {
                        printf("hello world\\n");
                        return 0;
                    }
                    """, "c") + os10_compile_run + code_block("""
                    gcc hello.c -o hello
                    ./hello
                    """, "bash") + """
                    <p><code>gcc hello.c -o hello</code>는 hello.c 소스 파일을 컴파일해 <code>hello</code>라는 실행 파일을 만든다. 실행할 때는 <code>hello</code>만 치는 것이 아니라 <code>./hello</code>처럼 현재 디렉토리의 실행 파일임을 명시한다. 이후 보안·리버싱·악성코드 분석 수업에서는 이렇게 만들어진 바이너리의 내부 구조를 더 깊게 보게 된다.</p>
                    """ + os10_objdump + code_block("""
                    objdump -d hello
                    readelf -h hello
                    """, "bash") + """
                    <p><code>objdump -d</code>는 실행 파일을 역어셈블해 어셈블리 코드 형태로 보여 준다. <code>readelf -h</code>는 ELF 파일 헤더를 보여 준다. 강사는 여기서 ELF, 어셈블리, 바이너리 분석을 자세히 다루지는 않지만, 앞으로 다른 멘토 수업에서 리버싱과 악성코드 분석을 배울 때 이 도구들이 이어진다고 설명한다.</p>
                    """,
                },
                {
                    "heading": "Python 기본 버전과 Anaconda가 필요한 경우",
                    "body": """
                    <p>Python은 이제 거의 필수 유틸리티처럼 쓰이기 때문에 Ubuntu에도 기본 탑재되어 있다. Ubuntu 16.04에는 Python 2.7과 Python 3.5가 함께 있었고, Ubuntu 18.04에는 Python 2.7과 Python 3.6이 있었다. 이 강의의 기준인 Ubuntu 20.04부터는 Python 2가 기본 설치되지 않고 Python 3 중심으로 바뀌었으며, 실습 환경에서는 Python 3.8.10을 확인한다.</p>
                    """ + os10_python_versions + """
                    <p>기본 Python만으로도 많은 작업은 가능하다. 하지만 AI, 데이터 분석, 보안 데이터 기반 이상 탐지처럼 대량의 패키지와 복잡한 라이브러리 조합이 필요한 경우에는 Anaconda 같은 대형 Python 배포판을 쓰는 편이 편하다. Anaconda는 Python, conda, 데이터 분석 패키지, Jupyter Notebook 등을 함께 제공한다.</p>
                    """ + os10_anaconda_plan + """
                    <p>다만 Anaconda는 용량이 매우 크다. 설치 파일만 약 1GB 수준이고, 설치 후 실제로 제대로 쓰려면 여러 GB에서 10GB 안팎의 공간이 필요할 수 있다. 강사는 처음 VM을 10GB 또는 12GB로 만들었다면 Anaconda 설치가 어렵고, 원활한 실습을 위해서는 20GB 이상이 필요하다고 설명한다. CSB 과정에서 데이터 분석이나 AI 실습을 할 학생은 따라 하고, 필요 없는 학생은 흐름만 이해해도 된다.</p>
                    <p>Anaconda는 Ubuntu 공식 저장소에서 <code>sudo apt install anaconda</code>처럼 설치하는 도구가 아니다. 공식 사이트에서 브라우저로 내려받거나, 강의자료의 URL을 이용해 <code>curl</code>로 설치 스크립트를 받은 뒤 <code>bash</code>로 실행한다. 기본 설치 위치는 사용자의 홈 디렉토리 아래이며, 별도 디스크나 다른 파티션에 설치하고 싶다면 설치 경로를 직접 지정할 수 있다.</p>
                    """,
                },
                {
                    "heading": "VirtualBox 디스크 증설: 물리 디스크, 파티션, 파일 시스템",
                    "body": """
                    <p>Anaconda 설치 공간을 확보하기 위해 먼저 VirtualBox 디스크를 늘린다. VM을 종료한 뒤 VirtualBox의 <strong>도구 -> 가상 미디어 관리자</strong>에서 해당 가상 디스크를 선택하고 크기를 20GB 정도로 늘린다. 이 단계는 VirtualBox가 관리하는 가상 디스크 파일의 물리적 크기를 키우는 작업이다.</p>
                    """ + os10_virtualbox_resize + """
                    <p>중요한 점은, VirtualBox에서 디스크 크기를 키웠다고 해서 Ubuntu 안의 사용 가능한 공간이 바로 늘어나는 것은 아니라는 점이다. 게스트 OS 입장에서는 “디스크 장치 전체 크기”만 커졌고, 그 안의 파티션과 파일 시스템은 아직 기존 크기를 유지한다. 따라서 Ubuntu 안에서 파티션과 파일 시스템을 다시 확장해야 한다.</p>
                    """ + os10_partition_theory + """
                    <p>강의의 예시는 extended partition인 <code>/dev/sda2</code>를 먼저 늘리고, 그 안의 실제 데이터 파티션인 <code>/dev/sda5</code>를 늘린 뒤, 마지막으로 ext 파일 시스템을 <code>resize2fs</code>로 확장하는 흐름이다. 이 내용은 파티셔닝과 파일 시스템이라는 더 큰 주제에 속하므로, 기초 과정에서는 원리만 간단히 이해하고 명령 순서를 정확히 따라 하는 것이 목표다.</p>
                    """ + os10_growpart_slide + code_block("""
                    df -h
                    lsblk
                    sudo apt install -y cloud-guest-utils
                    sudo growpart /dev/sda 2
                    sudo growpart /dev/sda 5
                    sudo resize2fs /dev/sda5
                    lsblk
                    df -h
                    """, "bash") + """
                    <p><code>cloud-guest-utils</code> 패키지 안에 <code>growpart</code>가 들어 있다. <code>sudo growpart /dev/sda 2</code>와 <code>sudo growpart /dev/sda 5</code>는 장치명과 파티션 번호 사이에 공백이 있다. 반대로 <code>sudo resize2fs /dev/sda5</code>는 장치 경로가 하나의 이름이므로 <code>sda</code>와 <code>5</code> 사이를 띄우지 않는다. 강사는 실습 중 이 공백 차이를 특히 주의하라고 강조한다.</p>
                    """ + os10_disk_terminal + """
                    <p>마지막에 <code>lsblk</code>와 <code>df -h</code>를 다시 확인한다. <code>lsblk</code>는 블록 장치와 파티션 크기를 보여 주고, <code>df -h</code>는 실제 파일 시스템의 사용 가능 공간을 사람이 읽기 쉬운 단위로 보여 준다. 두 결과가 모두 늘어났다면 Anaconda를 설치할 수 있는 충분한 공간이 확보된 것이다.</p>
                    """,
                },
                {
                    "heading": "Anaconda 설치 스크립트 실행과 conda 초기화",
                    "body": """
                    <p>공간을 확보했다면 Anaconda 공식 사이트에서 설치 파일을 내려받는다. 강의 화면에서는 브라우저로 다운로드하지만, 같은 파일을 <code>curl</code>로 받을 수도 있다. 다운로드가 끝나면 보통 <code>~/Downloads</code> 아래에 <code>Anaconda3-...-Linux-x86_64.sh</code> 같은 셸 스크립트가 생긴다.</p>
                    """ + os10_anaconda_download + code_block("""
                    cd ~/Downloads
                    bash Anaconda3-2023.09-0-Linux-x86_64.sh
                    # 파일명은 다운로드한 버전에 맞게 탭 자동완성으로 입력
                    """, "bash") + """
                    <p>긴 파일명을 모두 직접 칠 필요는 없다. 강사는 앞 강의에서 배운 탭 자동완성(tab completion)을 사용하라고 설명한다. <code>bash Anaconda</code> 정도까지 입력하고 Tab을 누르면 파일명이 자동 완성된다.</p>
                    """ + os10_anaconda_install + """
                    <p>설치 중에는 라이선스 약관을 보여 주고, 약관 화면은 <code>q</code>로 빠져나올 수 있다. 그 다음 “동의하느냐”는 질문에 그냥 Enter를 치면 기본값이 No일 수 있으므로, 설치하려면 반드시 <code>yes</code>를 입력해야 한다. 설치 경로는 기본값인 <code>/home/user1/anaconda3</code>를 그대로 쓰거나 원하는 경로로 바꿀 수 있다. 설치가 끝날 때 conda 초기화 여부를 묻는데, 자주 쓸 환경이면 yes를 선택하고, 강의처럼 방법만 보는 경우에는 no로 넘길 수도 있다.</p>
                    """ + os10_conda_init + code_block("""
                    /home/user1/anaconda3/bin/conda init
                    source ~/.bashrc
                    conda --version
                    python --version
                    """, "bash") + """
                    <p>초기화를 바로 하지 않았거나 현재 셸에서 <code>conda</code> 명령이 잡히지 않으면, 설치된 <code>anaconda3/bin</code> 안의 conda를 직접 실행해 초기화할 수 있다. 이후 셸을 다시 열거나 <code>source ~/.bashrc</code>를 실행하면 프롬프트에 base 환경이 보이고 conda 명령을 쓸 수 있다.</p>
                    """,
                },
                {
                    "heading": "conda 가상 환경: 프로젝트별 Python 버전과 의존성 분리",
                    "body": """
                    <p>Anaconda를 설치하면 기본 Python 버전이 Ubuntu 기본 Python과 다를 수 있다. 강의에서는 기본 환경에서 Python 3.11이 보이고, 별도 환경에서는 Python 3.10을 쓰는 예시를 든다. 핵심은 Python 버전만 바꾸는 것이 아니라 프로젝트별 라이브러리와 의존성을 분리한다는 점이다.</p>
                    """ + os10_conda_env + code_block("""
                    conda create -n myenv python=3.10
                    conda activate myenv
                    python --version
                    conda deactivate
                    """, "bash") + """
                    <p>예를 들어 프로젝트 1은 Python 3.10과 특정 버전의 pandas가 필요하고, 프로젝트 2는 다른 Python 버전과 다른 라이브러리 조합이 필요할 수 있다. 하나의 시스템 Python에 모두 설치하면 충돌이 날 수 있으므로, Python 개발에서는 가상 환경을 만들어 프로젝트마다 독립된 실행 환경을 유지하는 것이 기본 습관이다.</p>
                    <p>강사는 이 부분이 AI, 머신러닝, 보안 데이터 분석, 이상 탐지처럼 데이터 기반 작업을 Linux 환경에서 하려는 학생에게 특히 중요하다고 설명한다.</p>
                    """,
                },
                {
                    "heading": "Jupyter Notebook: 로컬 실행, 원격 접속, 서비스화",
                    "body": """
                    <p>Anaconda를 설치하는 이유 중 하나는 Jupyter Notebook 같은 웹 기반 개발 환경을 쉽게 쓸 수 있기 때문이다. 단순히 <code>jupyter notebook</code>을 실행하면 서버 안에서 브라우저가 열리고, 파일 목록과 노트북 화면을 웹 UI로 볼 수 있다. VM 내부 GUI에서 실행한다면 이 방식이 가장 단순하다.</p>
                    """ + os10_jupyter_options + code_block("""
                    jupyter notebook
                    jupyter notebook --ip=0.0.0.0 --no-browser
                    """, "bash") + """
                    <p>하지만 SSH로 원격 접속한 터미널에서 실행한다면 서버 쪽 브라우저를 띄울 수 없다. 이때 <code>--no-browser</code> 옵션으로 브라우저 자동 실행을 끄고, <code>--ip=0.0.0.0</code>으로 외부 접속을 허용할 수 있다. 그러면 Windows 호스트나 다른 PC의 브라우저에서 Ubuntu VM의 IP와 포트로 접속할 수 있다. 기본값은 로컬 사용자만 접속하는 상태이므로, 외부 접속을 열 때는 인증과 네트워크 노출을 함께 생각해야 한다.</p>
                    """ + os10_jupyter_token + """
                    <p>Jupyter는 웹 서비스이므로 접속 시 토큰을 요구한다. 터미널에 출력된 토큰을 입력해 로그인할 수도 있고, 토큰이 포함된 URL을 그대로 복사해 접속하면 별도 입력 없이 들어갈 수도 있다. 비밀번호를 따로 설정하고 싶다면 설정 파일을 생성한 뒤 password 관련 항목을 조정할 수 있다.</p>
                    """ + code_block("""
                    jupyter notebook --generate-config
                    # ~/.jupyter/jupyter_notebook_config.py 수정
                    # c.NotebookApp.ip = '0.0.0.0'
                    # c.NotebookApp.open_browser = False
                    # c.NotebookApp.password = '<hashed password>'
                    """, "bash") + os10_jupyter_service + """
                    <p>강사는 여기서 한 걸음 더 나아가, 앞에서 배운 systemd 서비스 관리를 응용해 Jupyter Notebook을 나만의 서비스로 등록해 보라고 제안한다. 강의에서 숙제 검사까지 하지는 않지만, 1강부터 배운 패키지 설치, 설정 파일, 서비스 관리, 권한 개념을 종합해 보는 좋은 연습이다.</p>
                    """ + code_block("""
                    sudo vi /etc/systemd/system/jupyter.service
                    sudo systemctl daemon-reload
                    sudo systemctl start jupyter
                    sudo systemctl status jupyter
                    sudo systemctl enable jupyter
                    """, "bash") + """
                    """,
                },
                {
                    "heading": "Java 개발 환경: JRE, JDK, 실행 파일 위치",
                    "body": """
                    <p>Java도 버전 관리가 중요한 언어다. 최신 Java는 21, 22, 23처럼 계속 올라가지만, Ubuntu 20.04의 기본 흐름에서는 OpenJDK 11이 대표 기본 버전으로 제공된다. 모든 프로젝트가 최신 버전을 요구하는 것은 아니므로, 실습에서는 기본 패키지를 먼저 이해한다.</p>
                    """ + os10_java_jre_jdk + """
                    <p><code>default-jre</code>는 Java Runtime Environment다. Java 프로그램을 실행할 수는 있지만, Java 소스 파일을 컴파일하는 <code>javac</code>는 포함하지 않는다. Java로 개발까지 하려면 <code>default-jdk</code>, 즉 Java Development Kit를 설치해야 한다.</p>
                    """ + code_block("""
                    sudo apt install default-jre
                    java -version
                    javac -version

                    sudo apt install default-jdk
                    javac -version
                    java -version

                    which gcc
                    which python3
                    which java
                    whereis java
                    """, "bash") + """
                    """ + os10_java_where + """
                    <p><code>which</code>는 지금 명령을 입력했을 때 실제 실행될 바이너리 경로를 보여 준다. 내가 실행하는 gcc가 어디 있는지, python3가 어느 경로의 파일인지, java가 어떤 링크를 따라 실행되는지 확인할 때 사용한다. <code>whereis</code>는 바이너리, 소스, 매뉴얼 등 관련 파일이 있는 여러 위치를 넓게 보여 준다.</p>
                    """,
                },
                {
                    "heading": "update-alternatives: 여러 버전 중 기본 실행 버전 선택",
                    "body": """
                    <p>여러 Java 버전이나 여러 Python 버전을 함께 설치하면, <code>python</code> 또는 <code>java</code>라고 입력했을 때 어느 버전이 실행될지 정해야 한다. Ubuntu는 이런 선택을 관리하기 위해 <code>update-alternatives</code>라는 유틸리티를 제공한다.</p>
                    """ + os10_update_alternatives + code_block("""
                    sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 10
                    sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.4 20
                    sudo update-alternatives --config python

                    sudo update-alternatives --install /usr/bin/java java /usr/java/jdk-12.0.2/bin/java 1
                    sudo update-alternatives --install /usr/bin/javac javac /usr/java/jdk-12.0.2/bin/javac 1
                    sudo update-alternatives --config java
                    """, "bash") + """
                    <p><code>--install</code> 뒤에는 “대표 명령 경로”, “대체 그룹 이름”, “실제 바이너리 경로”, “우선순위”를 지정한다. 예시에서 Python 2.7과 Python 3.4를 같은 <code>python</code> 그룹에 등록하면, <code>--config python</code>으로 어떤 버전을 기본으로 쓸지 선택할 수 있다. 숫자 우선순위는 자동 모드에서 어떤 항목이 기본이 될지에 영향을 준다.</p>
                    <p>강의에서는 update-alternatives를 깊게 실습하지 않고, 여러 버전을 통합 관리하는 도구가 있다는 정도를 이해하면 된다고 설명한다. Java도 공식 아카이브에서 여러 버전을 내려받아 같은 방식으로 등록할 수 있다.</p>
                    """,
                },
                {
                    "heading": "Docker 설치: docker.io와 공식 저장소 방식",
                    "body": """
                    <p>마지막 개발 환경은 Docker다. Docker는 컨테이너 기반 개발·실행 환경을 만들 때 쓰는 도구다. 이 강의는 Docker 명령어 자체를 깊게 배우는 수업이 아니라, 운영체제 기초 관점에서 Docker를 Ubuntu에 설치하고 권한과 저장 경로를 이해하는 데 초점을 둔다.</p>
                    """ + os10_docker_install_plan + """
                    <p>Ubuntu에서 가장 간단한 설치 방법은 <code>docker.io</code> 패키지를 apt로 설치하는 것이다. 이것은 Ubuntu를 만드는 Canonical 쪽에서 Docker 오픈소스 프로젝트를 Ubuntu 패키지 형태로 묶어 제공하는 버전이다. 더 최신 Docker 공식 버전을 쓰고 싶다면 Docker 공식 저장소를 apt source에 추가하거나 curl로 설치 스크립트를 받아 설치하는 다른 방법을 사용해야 한다. 방법이 다르면 설치되는 버전도 달라질 수 있다.</p>
                    """ + code_block("""
                    sudo apt install docker.io
                    docker --version
                    sudo docker run hello-world
                    docker ps
                    """, "bash") + """
                    <p>설치가 오래 걸릴 때는 네트워크와 패키지 미러 위치도 영향을 준다. 강사는 기본 Ubuntu 저장소가 멀리 있으면 속도가 느릴 수 있고, 국내 미러 예를 들어 Kakao 미러처럼 가까운 저장소로 바꾸면 더 빠르게 설치할 수 있다고 덧붙인다.</p>
                    """,
                },
                {
                    "heading": "Docker 권한: sudo 없이 쓰려면 그룹을 이해해야 한다",
                    "body": """
                    <p>Docker를 설치한 직후 일반 사용자로 <code>docker run hello-world</code>를 실행하면 권한 오류가 날 수 있다. 그래서 처음에는 <code>sudo docker run ...</code>처럼 실행하게 된다. 하지만 개발 환경에서 매번 sudo를 남용하는 것은 좋지 않다. Docker를 쓸 수 있는 권한을 현재 사용자에게 부여해야 한다.</p>
                    """ + os10_docker_permissions + code_block("""

                    sudo usermod -aG docker $USER
                    groups
                    # 로그아웃 후 다시 로그인
                    docker version
                    docker run hello-world
                    docker ps
                    """, "bash") + """
                    <p><code>$USER</code>는 현재 로그인한 사용자 이름으로 치환된다. <code>usermod -aG docker $USER</code>는 현재 사용자를 docker 그룹에 추가한다. 여기서 <code>-a</code>는 기존 보조 그룹을 유지한 채 append하겠다는 뜻이고, <code>-G docker</code>는 docker 그룹에 넣겠다는 뜻이다.</p>
                    <p>그룹 권한은 이미 열려 있는 셸에 즉시 완전히 적용되지 않을 수 있다. 앞 강의에서 배운 것처럼 로그인 시점에 그룹 권한이 부여되므로, 로그아웃 후 다시 로그인해야 <code>docker</code> 그룹이 적용된다. 재로그인 후에는 sudo 없이 <code>docker version</code>, <code>docker run hello-world</code>가 실행된다.</p>
                    """ + os10_docker_run + """
                    <p><code>hello-world</code> 이미지는 Docker 설치와 실행이 정상인지 확인하는 테스트 이미지다. 로컬에 이미지가 없으면 원격 저장소에서 이미지를 내려받고, 컨테이너를 실행한 뒤 성공 메시지를 출력한다. 이 강의에서는 컨테이너 내부 동작을 깊게 다루지는 않고, OS 관점에서 설치와 권한 확인까지를 목표로 한다.</p>
                    """,
                },
                {
                    "heading": "Docker 저장소와 디스크 관리",
                    "body": """
                    <p>Docker는 기본적으로 이미지, 컨테이너, 레이어 데이터를 <code>/var/lib/docker</code> 아래에 저장한다. 이 위치가 루트 파티션에 있으면 이미지를 많이 받거나 컨테이너를 많이 만들수록 루트 공간이 빠르게 줄어든다. 앞에서 Anaconda 설치를 위해 디스크를 늘린 것처럼, Docker도 저장 공간 관리가 중요하다.</p>
                    """ + os10_docker_storage + code_block("""
                    sudo systemctl stop docker
                    sudo mkdir -p /data/docker_dir
                    sudo rsync -aHXS /var/lib/docker/ /data/docker_dir/
                    sudo vi /etc/docker/daemon.json
                    """, "bash") + code_block("""
                    {
                      "data-root": "/data/docker_dir"
                    }
                    """, "json") + code_block("""
                    sudo systemctl daemon-reload
                    sudo systemctl start docker
                    docker info
                    """, "bash") + """
                    <p>강의에서는 이 저장 경로 변경을 상세 실습까지 하지는 않는다. 다만 실무에서는 별도의 하드디스크를 추가하고, 새 디스크를 <code>/data</code> 같은 위치에 마운트한 뒤, Docker의 <code>data-root</code>를 그쪽으로 옮기는 구성이 흔하다고 설명한다. 이 과정은 파일 시스템, 마운트, systemd 서비스 관리, 설정 파일 편집이 모두 연결된 주제다.</p>
                    """,
                },
                {
                    "heading": "개발 환경 구축의 공통 결론",
                    "body": """
                    """ + os10_summary + """
                    <p>강의의 결론은 개발 도구를 설치하는 공통 흐름이다. 먼저 필요한 컴파일러, 런타임, 서버, IDE, 분석 도구를 검색한다. Ubuntu 패키지로 제공되면 <code>sudo apt install</code>로 설치하고, 서비스로 동작하는 도구라면 <code>systemctl</code>로 상태를 확인하고 관리한다. Ubuntu 패키지가 없거나 공식 최신 버전이 필요하면 공식 사이트에서 브라우저로 다운로드하거나, <code>curl</code>로 파일을 받고, <code>dpkg -i</code> 또는 설치 스크립트로 설치한다.</p>
                    <p>설치만으로 끝나지 않는다. 대부분의 서버형 개발 도구는 <code>/etc</code> 아래의 설정 파일, 패키지별 config 파일, systemd unit, 권한, 그룹, 저장 경로를 확인해야 한다. 설정을 바꾼 뒤에는 서비스를 재시작하고, 버전 확인이나 샘플 실행으로 실제 동작을 검증해야 한다. 이번 강의의 C, Anaconda, Jupyter, Java, Docker 예시는 모두 이 공통 흐름을 다른 도구에 적용한 사례다.</p>
                    """,
                },
            ],
            "checks": [
                "개발 환경 구축이 컴파일러, 런타임, 가상 환경, IDE, 권한, 서비스, 디스크까지 포함한다는 점을 설명할 수 있는가?",
                "build-essential과 binutils가 각각 gcc/g++/make와 ld/ar/objdump/readelf 같은 도구를 제공한다는 점을 말할 수 있는가?",
                "hello.c 작성, gcc 컴파일, ./hello 실행, objdump/readelf 분석 흐름을 직접 설명할 수 있는가?",
                "Ubuntu 20.04부터 Python 2가 기본 제공되지 않고 Python 3 중심으로 바뀐 배경을 이해했는가?",
                "Anaconda가 apt 패키지가 아니라 공식 사이트나 curl로 받은 셸 스크립트로 설치된다는 점을 이해했는가?",
                "VirtualBox 디스크 크기 증가, growpart 파티션 확장, resize2fs 파일 시스템 확장의 차이를 설명할 수 있는가?",
                "`growpart /dev/sda 2`, `growpart /dev/sda 5`, `resize2fs /dev/sda5`에서 공백 위치가 왜 다른지 구분할 수 있는가?",
                "conda create, conda activate, conda deactivate로 프로젝트별 Python 버전과 의존성을 분리하는 이유를 설명할 수 있는가?",
                "Jupyter Notebook의 `--ip=0.0.0.0`, `--no-browser`, 토큰 로그인, systemd 서비스화 개념을 이해했는가?",
                "JRE와 JDK의 차이, java와 javac 확인 방법, which와 whereis의 차이를 말할 수 있는가?",
                "update-alternatives가 여러 Python 또는 Java 버전 중 기본 실행 버전을 관리하는 도구라는 점을 이해했는가?",
                "docker.io 패키지 설치와 Docker 공식 저장소 설치 방식의 차이를 설명할 수 있는가?",
                "Docker를 sudo 없이 쓰려면 docker 그룹 추가와 재로그인이 필요한 이유를 설명할 수 있는가?",
                "Docker 이미지와 컨테이너가 기본적으로 `/var/lib/docker`에 쌓이며, 실무에서는 data-root를 별도 디스크로 옮길 수 있음을 이해했는가?",
            ],
        },
        {
            "id": "1-11",
            "title": "배시 쉘 프로그래밍",
            "transcript_title": "배시 쉘 프로그래밍",
            "subtitle": "Bash 셸, 프롬프트, 리디렉션, 파이프, 히스토리, alias, 검색·필터 도구, 셸 스크립트 문법을 정리한다.",
            "tags": ["Bash", "Shell Script", "파이프"],
            "objectives": [
                "셸이 사용자 명령을 받아 운영체제와 연결하는 인터페이스라는 점과 Bash의 위치를 이해한다.",
                "PS1, ANSI 색상, 환경변수, PATH, alias, Bash 시작 파일이 셸 환경을 구성하는 방식을 설명한다.",
                "표준 입력, 표준 출력, 표준 에러, 리디렉션, 파이프가 프로세스 입출력을 연결하는 방식을 익힌다.",
                "history, find, grep, awk, sed를 사용해 명령 재실행, 파일 검색, 문자열 필터링, 컬럼 처리, 문자열 치환을 수행한다.",
                "shebang, 실행 권한, 인자 변수, for, if, while을 이용해 기본 셸 스크립트를 작성한다.",
            ],
            "sections": [
                {
                    "heading": "셸과 Bash",
                    "body": """
                    <p>셸은 사용자의 명령어를 입력받아 실행할 수 있는 공간이자 사용자와 운영체제 사이의 인터페이스다. 사용자가 셸에 명령을 입력하면 셸은 명령을 해석하고, 필요한 경우 시스템 콜을 통해 커널과 상호작용하며, 결과를 다시 사용자에게 보여 준다. 셸 스크립트는 반복적인 명령을 편하고 빠르게 실행하기 위해 짧고 간결한 프로그래밍을 하는 방식이다.</p>
                    """ + os11_shell_diagram + """
                    <p>셸에는 Bourne shell, Korn shell, C shell, Bash, Zsh 등이 있다. 이 수업은 가장 기본적으로 많이 쓰이는 Bash, 즉 Bourne Again Shell을 기준으로 한다. 로그인할 때 어느 셸이 뜨는지는 사용자 계정 정보의 마지막 필드에 정의되고, Ubuntu 실습 계정은 보통 <code>/bin/bash</code>를 사용한다.</p>
                    """ + os11_shell_types + os11_ohmyzsh + """
                    <p>Zsh와 Oh My Zsh는 Git 상태와 색상 정보를 풍부하게 보여 주는 개발자 친화적 환경이다. macOS 사용자나 개발자들이 많이 쓰지만, 이 강의의 목적은 Bash 기본기를 익히는 것이므로 실습은 Bash 기준으로 진행한다.</p>
                    """,
                },
                {
                    "heading": "프롬프트와 PS1",
                    "body": """
                    <p>프롬프트는 셸이 사용자의 입력을 받을 준비가 되었음을 보여 주는 표시다. 우분투에서는 보통 달러 기호가 보인다. 프롬프트에는 사용자명, 호스트명, 현재 디렉토리, 색상 코드가 포함될 수 있고, 이는 <code>PS1</code> 환경변수로 설정된다.</p>
                    """ + os11_prompt_ps1 + """
                    """ + code_block("""
                    echo "$PS1"
                    default="$PS1"
                    PS1="\\u@\\h:\\w$ "
                    PS1="$default"
                    """, "bash") + """
                    <p><code>\\u</code>는 사용자명, <code>\\h</code>는 호스트명, <code>\\w</code>는 현재 디렉토리를 의미한다. 복잡한 숫자와 대괄호는 ANSI 색상 코드를 표현하기 위한 특수 문자다. 강사는 기본값을 <code>default</code> 변수에 저장한 뒤 PS1을 단순한 흰색 프롬프트로 바꾸고, 다시 기본값으로 복구하는 실습을 보여 준다.</p>
                    """ + os11_ansi_codes + """
                    <p>ANSI escape code는 터미널 글자 색상과 스타일을 바꾸는 방식이다. 프롬프트는 시간, 사용자, 경로, Git 상태 등 원하는 정보를 넣어 꾸밀 수 있지만, 서버 운영에서는 필요한 정보를 안정적으로 보여 주는 구성이 우선이다.</p>
                    """,
                },
                {
                    "heading": "변수와 echo",
                    "body": """
                    <p>셸에서는 값을 임시로 저장해 두기 위해 변수를 사용할 수 있다. 변수에 값을 넣을 때는 등호 주변에 공백을 두지 않고, 변수 값을 꺼낼 때는 변수명 앞에 <code>$</code>를 붙인다. <code>echo</code>는 문자열과 변수 값을 화면에 출력하는 가장 기본적인 명령이다.</p>
                    """ + os11_echo_variables + code_block("""
                    greeting="hello"
                    name="user1"
                    echo "$greeting"
                    echo "hello $name"
                    echo 'hello $name'
                    """, "bash") + """
                    <p>큰따옴표 안에서는 <code>$name</code> 같은 변수가 값으로 치환되지만, 작은따옴표 안에서는 문자 그대로 출력된다. 이 차이는 셸 스크립트에서 파일명, 공백, 특수문자를 다룰 때 중요하다.</p>
                    """,
                },
                {
                    "heading": "리디렉션과 표준 입출력",
                    "body": """
                    <p>리디렉션은 명령의 출력이나 입력 방향을 바꾸는 기능이다. <code>&gt;</code>는 파일에 새로 쓰고, <code>&gt;&gt;</code>는 뒤에 덧붙인다. 표준 출력은 번호 1, 표준 에러는 번호 2로 다룰 수 있다. 성공 출력과 에러 출력을 같은 파일에 모으는 표현도 있다.</p>
                    """ + os11_redirection_slide + """
                    """ + code_block("""
                    echo hello > hello.txt
                    echo world >> hello.txt
                    ls > file.txt
                    ls no-such-file > file.txt
                    ls no-such-file 2> error.txt
                    ls /tmp > result.txt 2>&1
                    ls /tmp &> result.txt
                    find / -name "hello.txt" > ok.txt 2> err.txt
                    find / -name "hello.txt" 2>/dev/null
                    cat < hello.txt
                    """, "bash") + """
                    <p>표준 입력은 0, 표준 출력은 1, 표준 에러는 2로 다룬다. <code>2&gt;</code>는 에러만 저장하고, <code>2&gt;&amp;1</code>은 에러를 표준 출력과 같은 대상으로 보낸다. <code>/dev/null</code>은 버리는 장치라서 권한 오류처럼 필요 없는 에러를 숨길 때 자주 쓴다.</p>
                    """ + os11_stdin_slide + """
                    <p>입력 방향을 바꿀 때는 <code>&lt;</code>를 쓴다. 다만 모든 명령이 표준 입력을 읽는 것은 아니다. <code>cat</code>은 표준 입력을 받아 출력하지만, <code>echo</code>는 표준 입력을 읽는 도구가 아니기 때문에 같은 방식으로 동작하지 않는다.</p>
                    """ + os11_redirect_terminal + """
                    """,
                },
                {
                    "heading": "파이프, 히스토리, alias",
                    "body": """
                    <p>파이프는 한 명령의 출력을 다른 명령의 입력으로 넘기는 기능이다. <code>ls -l | grep hello</code>는 목록 출력 중 hello가 포함된 줄만 필터링한다. 파이프는 여러 번 이어 붙일 수도 있다.</p>
                    """ + os11_pipe_slide + """
                    """ + code_block("""
                    ls -l | grep hello
                    ls -l | grep hello | wc -l
                    cat hello.txt | more
                    cat hello.txt | sort | uniq
                    find / -name "hello.txt" 2>/dev/null | grep home
                    history
                    !120
                    !!
                    alias ll='ls -alF'
                    """, "bash") + """
                    <p>파이프는 <code>grep</code>, <code>wc</code>, <code>sort</code>, <code>awk</code>, <code>sed</code> 같은 도구와 자주 결합된다. 한 명령의 결과가 다음 명령의 입력이 된다는 점만 정확히 이해하면 복잡한 명령도 단계별로 읽을 수 있다.</p>
                    """ + os11_history_slide + """
                    <p><code>history</code>는 최근 실행 명령을 저장한다. <code>!</code>와 번호로 특정 명령을 다시 실행할 수 있고, <code>!!</code>는 바로 직전 명령을 다시 실행한다. 저장 개수는 <code>HISTSIZE</code>, <code>HISTFILESIZE</code> 같은 환경변수의 영향을 받는다. alias는 긴 명령을 짧은 이름으로 줄이는 기능이다.</p>
                    """,
                },
                {
                    "heading": "PATH, 환경변수, alias, Bash 시작 파일",
                    "body": """
                    <p><code>PATH</code>는 명령어 이름만 입력했을 때 Bash가 실행 파일을 찾기 위해 순서대로 검색하는 디렉토리 목록이다. 예를 들어 <code>ls</code>라고만 입력해도 실행되는 이유는 <code>/bin</code>이나 <code>/usr/bin</code> 같은 디렉토리가 PATH에 들어 있기 때문이다.</p>
                    """ + os11_path_slide + code_block("""
                    echo "$PATH"
                    export PATH="$PATH:/home/user1/bin"
                    which ls
                    which python3
                    """, "bash") + os11_which_slide + os11_env_table + code_block("""
                    printenv
                    env
                    echo "$HOME"
                    echo "$USER"
                    echo "$PWD"
                    echo "$LANG"
                    """, "bash") + """
                    <p>환경변수는 셸과 프로그램이 공유하는 설정값이다. 홈 디렉토리, 현재 사용자, 언어 설정, 프롬프트, 색상, 명령 검색 경로가 모두 환경변수로 표현될 수 있다.</p>
                    """ + os11_alias_slide + code_block("""
                    alias
                    alias ..='cd ..'
                    alias ...='cd ../..'
                    alias ll='ls -alF'
                    unalias ll
                    """, "bash") + """
                    <p>alias는 긴 명령을 짧은 이름으로 줄이는 기능이다. 한 번 입력한 alias는 현재 셸에서만 유지되므로 계속 쓰려면 시작 파일에 적어야 한다.</p>
                    """ + os11_bash_startup + """
                    <p>Bash는 <code>/etc/profile</code>, <code>/etc/bash.bashrc</code>, <code>~/.profile</code>, <code>~/.bashrc</code> 같은 시작 파일을 읽어 사용자 환경을 구성한다. 종료 시에는 <code>~/.bash_logout</code>을 사용할 수 있다. conda 초기화, alias, PS1 설정 같은 내용이 이 파일들에 들어간다.</p>
                    """,
                },
                {
                    "heading": "검색과 필터 도구",
                    "body": """
                    <p><code>find</code>는 파일 이름, 크기, 날짜, 타입 같은 조건으로 파일을 찾는다. <code>grep</code>은 문자열이나 패턴을 찾고, <code>awk</code>는 컬럼을 골라 출력하며, <code>sed</code>는 스트림 편집기로 문자열 치환에 많이 쓰인다. 보안 로그 분석에서 특정 IP, 계정명, 공격 패턴을 뽑을 때 이런 도구들이 자주 쓰인다.</p>
                    """ + os11_find_slide + os11_find_advanced + code_block("""
                    find / -name "hello.txt" 2>/dev/null
                    find / -name "*.txt" 2>/dev/null
                    find / -size +100M -exec ls -lh {} \\; 2>/dev/null
                    find / -name "*.txt" -exec grep "HELP" {} \\; -print 2>/dev/null
                    find / -mtime -2 -type f
                    """, "bash") + os11_grep_slide + code_block("""
                    grep -i "vim" file.txt
                    grep -n "vim" file.txt
                    grep -R "password" /etc 2>/dev/null
                    history | grep apt
                    """, "bash") + os11_awk_slide + code_block("""
                    ls -l | awk '{print $9, $5}'
                    ls -al | awk '{print "FILENAME:" $9, "SIZE:" $5}'
                    cat /etc/passwd | awk -F ':' '{print $1}'
                    """, "bash") + os11_sed_slide + code_block("""
                    cat copyright.txt | sed 's/book/books/g'
                    cat /etc/passwd | sed 's/bin/BIN/g'
                    """, "bash") + """
                    <p>옵션을 모두 외울 수 없으므로 <code>man find</code>, <code>man grep</code>처럼 매뉴얼을 확인하며 필요한 옵션을 찾는 방식으로 익힌다. 셸 스크립트에서는 find로 대상을 찾고, grep으로 거르고, awk로 필요한 필드를 뽑고, sed로 문자열을 치환하는 조합이 자주 나온다.</p>
                    """,
                },
                {
                    "heading": "환경변수와 .bashrc",
                    "body": """
                    <p>Bash가 실행될 때 <code>.bashrc</code> 같은 설정 파일이 읽히고, alias, 프롬프트, Anaconda 초기화 스크립트 같은 내용이 적용된다. Anaconda를 삭제할 때 폴더만 지우면 끝나는 것이 아니라, <code>.bashrc</code>에 남아 있는 초기화 코드도 삭제해야 한다.</p>
                    """ + os11_bashrc_anaconda + code_block("""
                    echo "$PATH"
                    which python3
                    rm -rf ~/anaconda3
                    vi ~/.bashrc
                    # conda initialize 블록 삭제
                    source ~/.bashrc
                    conda --version
                    """, "bash") + """
                    <p>Anaconda 폴더를 지워도 <code>.bashrc</code>에 conda 초기화 코드가 남아 있으면 셸이 시작될 때 존재하지 않는 경로의 스크립트를 실행하려고 할 수 있다. 따라서 삭제 후에는 <code>.bashrc</code>에 남아 있는 conda 블록까지 정리해야 한다. 이후 새 터미널을 열면 프롬프트의 <code>(base)</code>가 사라지고, <code>which python3</code>는 시스템 Python 경로를 가리키게 된다.</p>
                    """,
                },
                {
                    "heading": "셸 스크립트 작성",
                    "body": """
                    <p>셸 스크립트 파일은 보통 첫 줄에 shebang을 넣어 어떤 셸로 실행할지 표시한다. 실행 권한이 없으면 직접 실행할 수 없으므로 <code>chmod +x</code>로 권한을 준다. 또는 <code>bash script.sh</code>처럼 셸을 명시해 실행할 수도 있다.</p>
                    """ + os11_script_shebang + code_block("""
                    #!/bin/bash
                    NAME="user1"
                    AGE=30
                    echo "hello $NAME"
                    echo "first arg: $1"
                    echo "second arg: $2"
                    """, "bash") + code_block("""
                    bash user.sh white school
                    chmod +x user.sh
                    ./user.sh white school
                    """, "bash") + """
                    """ + os11_script_args + """
                    <table>
                      <thead><tr><th>표현</th><th>의미</th></tr></thead>
                      <tbody>
                        <tr><td><code>$0</code></td><td>실행된 스크립트 파일명</td></tr>
                        <tr><td><code>$1</code>, <code>$2</code></td><td>첫 번째, 두 번째 인자</td></tr>
                        <tr><td><code>$#</code></td><td>전달된 인자 개수</td></tr>
                        <tr><td><code>$@</code></td><td>전체 인자 목록</td></tr>
                        <tr><td><code>$?</code></td><td>직전 명령의 종료 상태</td></tr>
                      </tbody>
                    </table>
                    <p>스크립트를 직접 <code>./user.sh</code>로 실행하려면 파일에 실행 권한이 있어야 한다. 실행 권한이 없더라도 <code>bash user.sh</code>처럼 Bash를 명시하면 Bash가 파일을 읽어 실행할 수 있다. 인자값을 사용하면 스크립트 안에 값을 하드코딩하지 않고 실행할 때마다 다른 값을 넣어 처리할 수 있다.</p>
                    """,
                },
                {
                    "heading": "반복문과 조건문 예제",
                    "body": """
                    <p>강의 마지막 실습은 숫자를 출력하는 셸 스크립트다. 먼저 1부터 10까지 출력하고, 이후 if문을 넣어 짝수만 출력하도록 바꾼다. 이 예제는 앞서 배운 변수, 반복문, 조건문, 실행 권한을 하나로 묶는 연습이다.</p>
                    """ + os11_number_script + code_block("""
                    #!/bin/bash
                    echo "숫자 출력 시작"

                    for ((i=1; i<=10; i++)); do
                        echo "$i"
                    done

                    echo "숫자 출력 종료"
                    """, "bash") + code_block("""
                    #!/bin/bash
                    echo "짝수 출력 시작"

                    for ((i=1; i<=10; i++)); do
                        if [ $((i % 2)) -eq 0 ]; then
                            echo "$i"
                        fi
                    done

                    echo "짝수 출력 종료"
                    """, "bash") + """
                    <p><code>for ((...))</code>는 C 언어식 반복문처럼 초기값, 조건, 증가식을 한 줄에 적는다. <code>$((i % 2))</code>는 산술 확장이고, <code>-eq</code>는 숫자가 같은지 비교하는 조건 연산자다. <code>if</code>를 열었으면 <code>fi</code>로 닫고, <code>for</code>를 열었으면 <code>done</code>으로 닫는다.</p>
                    """ + os11_complex_script + code_block("""
                    #!/bin/bash

                    directory="$1"
                    extension="$2"
                    minsize="${3:-100M}"

                    if [ $# -lt 2 ]; then
                        echo "Usage: $0 <directory> <extension> [minsize]"
                        exit 1
                    fi

                    cd "$directory" || exit 1

                    find . -type f -name "*.${extension}" -size +"$minsize" -print0 |
                      xargs -0 ls -lh |
                      sort -k5 -hr |
                      while read -r line; do
                          echo "$line"
                      done
                    """, "bash") + """
                    <p>마지막 예시는 지금까지 배운 내용을 종합한다. 디렉토리와 확장자를 인자로 받고, 해당 디렉토리로 이동하며, 이동 실패 시 종료한다. 그 다음 <code>find</code>로 조건에 맞는 파일을 찾고, <code>ls -lh</code>로 크기를 표시하고, <code>sort</code>로 큰 파일 순서로 정렬한 뒤, <code>while read</code>로 한 줄씩 처리한다.</p>
                    """ + os11_script_practice + """
                    <p>셸 스크립트는 문법 자체보다 “평소 터미널에서 반복하던 명령을 파일로 저장해 재사용한다”는 관점으로 접근하면 이해하기 쉽다. 보안 운영에서는 로그 검색, 큰 파일 탐색, 특정 문자열 추출, 반복 점검 작업을 자동화할 때 이런 기본 문법이 바로 사용된다.</p>
                    """,
                },
            ],
            "checks": [
                "셸이 사용자 명령을 받아 시스템 콜을 통해 운영체제와 연결되는 인터페이스라는 점을 설명할 수 있는가?",
                "Bourne shell, Bash, Zsh, Oh My Zsh의 위치와 이 강의가 Bash를 기준으로 하는 이유를 이해했는가?",
                "PS1의 `\\u`, `\\h`, `\\w`와 ANSI escape code가 프롬프트를 어떻게 구성하는지 말할 수 있는가?",
                "셸 변수와 환경변수의 차이, 큰따옴표와 작은따옴표에서 변수 치환이 달라지는 점을 설명할 수 있는가?",
                "표준 입력 0, 표준 출력 1, 표준 에러 2와 `>`, `>>`, `2>`, `2>&1`, `&>`, `<`의 의미를 구분할 수 있는가?",
                "파이프가 한 명령의 출력을 다음 명령의 입력으로 전달한다는 점과 `grep`, `wc`, `sort`와 결합하는 방식을 이해했는가?",
                "history, `!번호`, `!!`, `HISTSIZE`가 어떤 역할을 하는지 설명할 수 있는가?",
                "PATH가 명령 검색 경로이며 `which`가 실제 실행될 파일 위치를 보여 준다는 점을 이해했는가?",
                "alias와 `/etc/profile`, `/etc/bash.bashrc`, `~/.profile`, `~/.bashrc`, `~/.bash_logout`의 역할을 구분할 수 있는가?",
                "find, grep, awk, sed가 각각 파일 검색, 문자열 필터링, 컬럼 처리, 문자열 치환에 쓰인다는 점을 설명할 수 있는가?",
                "Anaconda 삭제 시 폴더 삭제와 `.bashrc` 초기화 코드 삭제가 모두 필요하다는 점을 이해했는가?",
                "shebang, 실행 권한, `bash script.sh`, `$0`, `$1`, `$#`, `$@`, `$?`의 의미를 설명할 수 있는가?",
                "for, if, while, 산술 확장, 종료 상태를 조합해 간단한 셸 스크립트를 작성할 수 있는가?",
            ],
        },
        {
            "id": "1-12",
            "title": "시스템 운영 및 모니터링",
            "transcript_title": "시스템 운영 및 모니터링",
            "subtitle": "사용자 접속, 로그인 흔적, 프로세스, 시스템 콜, 네트워크 인터페이스와 패킷을 관찰하는 리눅스 운영 도구를 정리한다.",
            "tags": ["모니터링", "프로세스", "네트워크"],
            "objectives": [
                "현재 접속 사용자, 로그인 성공·실패 기록, 명령 히스토리, 인증 로그를 점검하는 방법을 익힌다.",
                "foreground/background job, ps, /proc, pstree, signal, lsof, strace, ltrace로 프로세스를 관찰하고 제어하는 흐름을 이해한다.",
                "ifconfig, NetworkManager, netplan, arp, route, ip, netstat, ping, traceroute, nslookup, tcpdump의 역할을 구분한다.",
            ],
            "sections": [
                {
                    "heading": "운영과 모니터링의 범위",
                    "body": """
                    <p>시스템 운영은 설치가 끝난 뒤부터 시작된다. 서버가 켜져 있다고 끝나는 것이 아니라, 누가 접속해 있는지, 원치 않는 접속 시도가 있었는지, 어떤 데몬과 프로세스가 실행 중인지, 네트워크가 정상적으로 통신하는지 계속 관찰해야 한다. 강의에서는 이 넓은 관찰 활동을 사용자 모니터링, 프로세스 모니터링, 네트워크 모니터링으로 나누어 살펴본다.</p>
                    """ + os12_scope + """
                    <p>사용자 쪽에서는 <code>users</code>, <code>who</code>, <code>w</code>, <code>last</code>, <code>lastb</code>, <code>history</code>, <code>/var/log/auth.log</code>를 본다. 프로세스 쪽에서는 job control, <code>ps</code>, <code>/proc/&lt;pid&gt;</code>, <code>pstree</code>, <code>kill</code>, <code>killall</code>, <code>lsof</code>, <code>strace</code>, <code>ltrace</code>를 본다. 네트워크 쪽에서는 인터페이스, 라우팅, 포트, DNS, 패킷 캡처를 확인한다.</p>
                    """ + os12_process_scope + os12_network_scope + """
                    <p>강사는 이 강의의 많은 도구가 각각 따로 몇 시간씩 다룰 수 있을 정도로 깊다고 설명한다. 따라서 이 시간의 목표는 모든 옵션을 외우는 것이 아니라 “어떤 상황에서 어떤 도구를 떠올려야 하는지”를 잡는 것이다. 나중에 침해 사고 분석, 서버 장애 대응, 네트워크 보안 실습을 할 때 이 도구들이 다시 등장한다.</p>
                    """,
                },
                {
                    "heading": "현재 접속 사용자 확인: users, who, w",
                    "body": """
                    <p>가장 먼저 볼 것은 현재 누가 시스템에 접속해 있는지다. <code>users</code>는 로그인한 사용자 이름만 간단히 보여 준다. 같은 사용자가 여러 터미널을 열면 같은 이름이 여러 번 나올 수 있다. 실무에서는 정보가 너무 적어서 단독으로 많이 쓰이지는 않지만, “지금 접속자가 있는가”를 빠르게 볼 수 있다.</p>
                    <p><code>who</code>는 사용자 이름, 터미널, 로그인 시간, 접속 위치를 보여 준다. <code>w</code>는 여기에 현재 시간, uptime, load average, 사용자별 idle 시간, JCPU, PCPU, 현재 실행 중인 명령까지 붙여서 보여 준다. 강의 실습에서는 VirtualBox GUI 세션과 여러 터미널을 열어 둔 상태에서 <code>w</code>를 실행해, 각 터미널에서 무엇을 하고 있는지까지 표시되는 것을 확인한다.</p>
                    """ + os12_users_who_w + code_block("""
                    users
                    who
                    w
                    who am i
                    """, "bash") + """
                    <p><code>w</code> 출력의 <code>WHAT</code> 열은 해당 세션에서 현재 실행 중인 명령을 보여 준다. 강사가 두 번째 터미널에서 <code>w</code>를 실행하면, 그 세션의 <code>WHAT</code>에도 <code>w</code>가 표시된다. 운영자가 원격 서버에서 낯선 계정이나 낯선 접속 위치를 발견하면, 먼저 이런 명령으로 어느 터미널에서 무엇을 하고 있는지 확인한다.</p>
                    """ + os12_tty_pts + """
                    <p>터미널 표기에서 <code>tty</code>는 teletypewriter에서 온 말로, 리눅스에서는 로컬 콘솔 같은 물리·가상 터미널을 의미한다. <code>pts</code>는 pseudo terminal slave의 약자이며, SSH 접속이나 GUI 터미널처럼 네트워크·그래픽 환경을 통해 열린 터미널 세션에서 주로 보인다. 현대 서버 운영에서는 SSH 접속이 많기 때문에 <code>/dev/pts/0</code>, <code>/dev/pts/1</code> 같은 표기를 자주 보게 된다.</p>
                    """ + code_block("""
                    # 로컬 콘솔 계열
                    /dev/tty1

                    # SSH, GUI terminal 계열
                    /dev/pts/0
                    /dev/pts/1
                    """, "bash") + """
                    """,
                },
                {
                    "heading": "접속자에게 메시지 보내기: wall, write",
                    "body": """
                    <p>과거에는 터미널을 통해 사용자끼리 메시지를 주고받는 기능도 많이 쓰였다. 지금은 메신저나 협업 도구를 주로 쓰지만, 서버 운영에서는 여전히 의미가 있다. 예를 들어 유지보수 때문에 곧 시스템을 종료해야 하는데 접속자가 남아 있다면, 모든 터미널에 공지를 띄워야 한다.</p>
                    """ + os12_wall_write + code_block("""
                    wall "System will shut down in 5 minutes."

                    # 특정 사용자와 터미널에 메시지 전송
                    write user1 pts/1
                    """, "bash") + """
                    <p><code>wall</code>은 write all의 의미로 로그인한 모든 사용자에게 메시지를 보낸다. <code>write</code>는 특정 사용자와 터미널을 지정해 1:1 메시지를 보낸다. 강의에서는 여러 터미널을 열어 둔 상태에서 <code>wall</code> 메시지가 각 터미널 위에 표시되는 것을 확인한다.</p>
                    """,
                },
                {
                    "heading": "로그인 성공·실패 기록: last, lastb",
                    "body": """
                    <p>현재 접속자만 보는 것으로는 부족하다. 이미 접속했다가 나간 사람, 재부팅 기록, 로그인 실패 흔적도 봐야 한다. <code>last</code>는 로그인 성공 기록을 보여 준다. 사용자 이름을 붙이면 특정 사용자 기록만 볼 수 있고, <code>last reboot</code>처럼 재부팅 이력도 확인할 수 있다.</p>
                    """ + os12_last + code_block("""
                    last
                    last user1
                    last -n 20
                    last reboot
                    """, "bash") + """
                    <p><code>last</code>가 읽는 원본은 <code>/var/log/wtmp</code>다. 이 파일은 텍스트가 아니라 바이너리 로그다. 강사는 접속 기록이 평문 텍스트라면 너무 쉽게 위변조될 수 있기 때문에, 일반적인 <code>cat</code>이 아니라 <code>last</code> 같은 전용 명령으로 읽는 구조라고 설명한다.</p>
                    """ + os12_lastb + """
                    <p><code>lastb</code>는 로그인 실패 기록을 보여 준다. 원본 파일은 <code>/var/log/btmp</code>이며, 실패 기록은 민감한 정보라서 일반 사용자 권한으로 읽지 못하고 <code>sudo</code>가 필요할 수 있다. 강의의 로컬 VM에는 실패 로그가 거의 없지만, 클라우드 서버에서는 admin, root, test 같은 계정명으로 무차별 대입 공격이 계속 남을 수 있다.</p>
                    """ + code_block("""
                    sudo lastb
                    sudo lastb -n 20

                    ls -l /var/log/wtmp /var/log/btmp
                    sudo lastb
                    """, "bash") + """
                    <p>강사는 실제 클라우드 서버 예시에서 공격자가 계정명을 모르는 상태로 여러 이름을 시도하며 로그인 실패 로그를 남기는 모습을 설명한다. 이런 실패가 일정 횟수 이상 반복되면 자동 차단하는 보안 도구도 있지만, 그 부분은 이 강의의 범위를 넘어 오프라인 실습에서 별도로 다룬다고 정리한다.</p>
                    """,
                },
                {
                    "heading": "명령 히스토리와 인증 로그",
                    "body": """
                    <p>사용자가 접속한 뒤 무엇을 했는지 보려면 셸 히스토리와 인증 로그를 함께 본다. <code>history</code>는 현재 셸이 기억하는 명령 목록이고, Bash에서는 보통 사용자 홈의 <code>~/.bash_history</code>에 저장된다. 침해 사고에서 공격자가 어떤 명령을 실행했는지 단서가 될 수 있다.</p>
                    """ + os12_history_auth + code_block("""
                    history
                    cat ~/.bash_history

                    sudo tail -n 100 /var/log/auth.log
                    sudo grep sudo /var/log/auth.log
                    sudo grep sshd /var/log/auth.log
                    """, "bash") + """
                    <p>다만 히스토리는 완전한 증거가 아니다. 공격자는 흔히 <code>.bash_history</code>를 지우거나 히스토리 기록을 남기지 않도록 설정하고 나간다. 그래서 <code>/var/log/auth.log</code> 같은 인증 로그도 함께 봐야 한다. 이 로그에는 SSH 로그인, sudo 사용, 인증 성공·실패 같은 이벤트가 남는다.</p>
                    """,
                },
                {
                    "heading": "foreground, background, job control",
                    "body": """
                    <p>프로세스 모니터링의 첫 단계는 내가 실행한 작업을 셸에서 어떻게 제어하는지 이해하는 것이다. 터미널 앞에서 입력을 차지하고 있는 작업을 foreground job이라고 하고, 뒤에서 실행되면서 터미널 입력을 직접 차지하지 않는 작업을 background job이라고 한다.</p>
                    """ + os12_jobs + """
                    <p>강의에서는 <code>tail -f</code>로 로그 파일을 계속 따라가며 출력하는 명령을 예로 든다. 이 명령은 계속 실행되기 때문에 터미널이 돌아오지 않는다. 이때 <code>Ctrl+Z</code>를 누르면 프로세스가 종료되는 것이 아니라 일시 정지된다. <code>jobs</code>로 현재 셸의 작업 번호를 보고, <code>bg %1</code>로 백그라운드에서 다시 실행하며, <code>fg %1</code>로 다시 앞으로 가져올 수 있다.</p>
                    """ + os12_jobs_practice + code_block("""
                    tail -f /var/log/syslog

                    # 실행 중 Ctrl+Z 입력
                    jobs
                    bg %1
                    jobs
                    fg %1

                    # foreground로 가져온 뒤 Ctrl+C 입력
                    """, "bash") + """
                    <p><code>Ctrl+C</code>는 보통 foreground 프로세스에 SIGINT를 보내 종료를 요청한다. <code>Ctrl+Z</code>는 종료가 아니라 정지라는 점을 구분해야 한다. 작업 번호 앞의 <code>%</code>는 PID가 아니라 현재 셸이 관리하는 job 번호를 가리킨다.</p>
                    """,
                },
                {
                    "heading": "ps로 프로세스 상태 읽기",
                    "body": """
                    <p><code>ps</code>는 실행 중인 프로세스를 보는 가장 기본적인 명령이다. 옵션 없이 실행하면 현재 터미널 세션과 관련된 프로세스만 짧게 나온다. 화면에는 PID, TTY, TIME, CMD가 표시된다. PID는 프로세스 식별자, TTY는 연결된 터미널, TIME은 CPU 사용 시간, CMD는 실행 명령이다.</p>
                    """ + os12_ps_states + """
                    <p>상태 문자도 중요하다. <code>R</code>은 실행 중이거나 실행 가능한 상태, <code>S</code>는 interruptible sleep, <code>D</code>는 보통 I/O를 기다리는 uninterruptible sleep, <code>T</code>는 stopped 또는 traced, <code>Z</code>는 좀비 프로세스를 뜻한다. 강의 슬라이드에는 추가 표시로 우선순위가 높은 프로세스, 메모리에 없는 프로세스, 페이지된 프로세스, swap된 프로세스, 멀티스레드, foreground process group 표시도 함께 소개된다.</p>
                    """ + os12_ps_aux + code_block("""
                    ps
                    ps aux
                    ps -ef
                    ps -e --sort pid
                    ps -A
                    ps -f

                    ps aux | grep htop
                    """, "bash") + """
                    <p><code>ps aux</code>에서 <code>a</code>는 모든 사용자의 프로세스, <code>u</code>는 사용자 중심 상세 출력, <code>x</code>는 터미널에 붙지 않은 프로세스까지 포함한다. 그래서 데몬과 백그라운드 프로세스를 보는 서버 운영에서 자주 쓴다. <code>grep</code>으로 특정 프로세스를 찾으면 실제 대상 프로세스뿐 아니라 <code>grep</code> 명령 자체도 함께 잡힐 수 있다는 점도 강의에서 확인한다.</p>
                    """,
                },
                {
                    "heading": "/proc와 프로세스 내부 관찰",
                    "body": """
                    <p><code>/proc</code>는 디스크에 저장된 일반 파일 시스템이 아니라 커널이 메모리 위에 만들어 주는 특수 파일 시스템이다. 리눅스는 실행 중인 프로세스와 시스템 정보를 파일처럼 보여 주며, <code>/proc/&lt;pid&gt;</code> 디렉토리 안에 특정 프로세스의 실행 정보를 모아 둔다.</p>
                    """ + os12_proc + """
                    <p>대표 파일은 다음과 같다. <code>cmdline</code>은 실행 명령과 인자, <code>cwd</code>는 현재 작업 디렉토리, <code>environ</code>은 환경변수, <code>exe</code>는 실행 파일 링크, <code>fd</code>는 열린 파일 디스크립터, <code>root</code>는 프로세스가 보는 루트 디렉토리, <code>stat</code>, <code>statm</code>, <code>status</code>는 상태와 메모리 정보를 보여 준다.</p>
                    """ + os12_proc_practice + code_block("""
                    pid=$(pgrep nginx | head -n 1)

                    cat /proc/$pid/cmdline
                    readlink /proc/$pid/cwd
                    sudo ls -l /proc/$pid/fd
                    cat /proc/$pid/status
                    """, "bash") + """
                    <p>침해 사고나 장애 분석에서는 “이 프로세스가 어떤 명령으로 실행됐는가”, “어떤 파일과 소켓을 잡고 있는가”, “어떤 사용자 권한으로 떠 있는가”가 중요하다. <code>/proc</code>는 이런 질문에 바로 접근할 수 있는 출발점이다.</p>
                    """ + os12_pstree + code_block("""
                    pstree
                    ps f
                    """, "bash") + """
                    <p><code>pstree</code>는 프로세스의 부모·자식 관계를 트리로 보여 준다. 복잡한 서버에서는 어떤 데몬이 어떤 자식 프로세스를 만들었는지, 셸에서 실행한 명령이 어떤 계층에 있는지 확인하는 데 도움이 된다. <code>ps f</code>도 비슷하게 트리 형태로 보여 줄 수 있다.</p>
                    """,
                },
                {
                    "heading": "signal, kill, killall",
                    "body": """
                    <p><code>kill</code>은 이름 때문에 “프로세스를 죽이는 명령”으로만 오해하기 쉽지만, 정확히는 프로세스에 signal을 보내는 명령이다. 기본 signal은 보통 <code>SIGTERM</code>이며, 프로세스에게 정상 종료를 요청한다. <code>SIGINT</code>는 <code>Ctrl+C</code>와 비슷한 인터럽트, <code>SIGHUP</code>은 터미널 연결 끊김이나 설정 재읽기 용도로 쓰일 수 있고, <code>SIGKILL</code>은 프로세스가 무시할 수 없는 강제 종료다.</p>
                    """ + os12_kill + code_block("""
                    kill <pid>          # 기본적으로 SIGTERM
                    kill -1 <pid>       # SIGHUP
                    kill -2 <pid>       # SIGINT
                    kill -9 <pid>       # SIGKILL

                    killall -s TERM nginx
                    sudo killall nginx
                    """, "bash") + """
                    <p>강의 실습에서는 <code>htop</code>을 실행한 뒤 다른 터미널에서 <code>ps aux | grep htop</code>으로 PID를 찾고, <code>kill -9 &lt;pid&gt;</code>로 종료한다. 다시 실행하면 PID가 달라지고, 이번에는 <code>killall htop</code>처럼 프로세스 이름으로 종료할 수 있음을 확인한다.</p>
                    """ + os12_htop + """
                    <p><code>kill -9</code>는 정리 작업을 할 기회를 주지 않고 바로 종료시키므로 마지막 수단에 가깝다. 설정 파일 저장, 임시 파일 정리, 연결 종료 같은 정상 종료 절차가 필요한 프로그램이라면 먼저 <code>SIGTERM</code>을 보내고, 그래도 종료되지 않을 때 강제 종료를 고려한다.</p>
                    """,
                },
                {
                    "heading": "lsof, strace, ltrace",
                    "body": """
                    <p><code>lsof</code>는 list open files의 약자로, 프로세스가 열고 있는 파일과 소켓을 보여 준다. 리눅스에서는 일반 파일뿐 아니라 장치, 파이프, 네트워크 소켓도 파일처럼 다루므로, <code>lsof</code>는 “어떤 프로세스가 이 자원을 잡고 있는가”를 찾는 데 유용하다.</p>
                    """ + os12_lsof + code_block("""
                    lsof /path/to/file
                    lsof -i
                    lsof -u user1
                    sudo lsof -i :80
                    """, "bash") + """
                    <p><code>strace</code>는 시스템 콜을 추적한다. 예를 들어 <code>strace whoami</code>를 실행하면 셸에서 <code>whoami</code>가 실행되고, 그 결과를 출력하기까지 커널에 어떤 요청을 하는지 볼 수 있다. <code>ls</code>도 파일 목록을 얻기 위해 디렉토리와 파일 정보를 커널에 요청하고, 그 과정의 open, read, write 같은 호출이 표시된다.</p>
                    """ + os12_strace + code_block("""
                    strace whoami
                    strace ls
                    strace -c ls
                    strace -t ls
                    strace -e trace=file ls
                    """, "bash") + """
                    <p><code>ltrace</code>는 시스템 콜보다 위 단계인 라이브러리 호출을 추적한다. C 프로그램이라면 <code>malloc</code>, <code>printf</code>, 문자열 처리 함수처럼 라이브러리 함수 호출을 볼 수 있다. 강사는 이 두 도구를 깊게 실습하지는 않고, 나중에 리눅스 디버깅과 보안 분석을 더 깊게 배울 때 필요해지는 도구라고 소개한다.</p>
                    """ + os12_ltrace + code_block("""
                    ltrace ./program
                    ltrace -c ./program
                    """, "bash") + """
                    """,
                },
                {
                    "heading": "네트워크 인터페이스: ifconfig, NetworkManager, netplan",
                    "body": """
                    <p>네트워크 모니터링은 인터페이스 확인에서 시작한다. <code>ifconfig</code>는 오래전부터 사용된 네트워크 인터페이스 확인·설정 도구다. 과거에는 <code>eth0</code>, <code>eth1</code> 같은 이름을 많이 썼지만, 최신 리눅스에서는 하드웨어 위치를 반영한 <code>enp0s3</code> 같은 이름을 자주 본다.</p>
                    """ + os12_ifconfig + code_block("""
                    ifconfig
                    ifconfig enp0s3

                    sudo ifconfig enp0s3 down
                    sudo ifconfig enp0s3 up
                    sudo ifconfig enp0s3 192.168.0.2/24
                    """, "bash") + """
                    <p>Ubuntu Desktop 20.04 같은 환경에서는 GUI 네트워크 설정이 뒤에서 인터페이스를 관리한다. 이 역할을 하는 것이 <code>NetworkManager</code>다. 강사는 CLI에서 직접 설정하려고 할 때 NetworkManager가 다시 설정을 덮어쓰거나 GUI 설정과 충돌할 수 있으므로, 상태를 보고 필요하면 잠시 중지할 줄 알아야 한다고 설명한다.</p>
                    """ + os12_network_manager + code_block("""
                    systemctl status NetworkManager
                    sudo systemctl stop NetworkManager
                    sudo systemctl start NetworkManager
                    """, "bash") + """
                    <p>NetworkManager를 중지하면 우측 상단 네트워크 아이콘과 GUI 설정 기능이 사라지고, 다시 시작하면 GUI에서 IP 자동·수동 설정 화면을 사용할 수 있다. 서버 환경에서는 GUI보다 설정 파일 기반 관리가 더 중요하다.</p>
                    """ + os12_netplan + """
                    <p>Ubuntu 18.04 이후 LTS 계열에서는 <code>netplan</code>이 네트워크 설정의 중심에 있다. <code>/etc/netplan/</code> 아래 YAML 파일에서 renderer를 <code>NetworkManager</code> 또는 <code>networkd</code>로 지정하고, 주소, 게이트웨이, DNS를 선언한다. Desktop 기본값은 NetworkManager인 경우가 많고, Server에서는 networkd를 쓰는 구성이 흔하다.</p>
                    """ + code_block("""
                    ls -l /etc/netplan/
                    sudo vi /etc/netplan/01-network-manager-all.yaml
                    sudo netplan apply
                    """, "bash") + """
                    <p>강의 화면의 예시는 <code>addresses</code>, <code>gateway4</code>, <code>nameservers</code>에 DNS 주소를 넣는 형태를 보여 준다. YAML은 들여쓰기가 중요하므로, 공백과 계층을 잘못 쓰면 설정 적용에 실패할 수 있다.</p>
                    """,
                },
                {
                    "heading": "ARP, route, ip",
                    "body": """
                    <p><code>arp</code>는 같은 LAN 구간에서 IP 주소와 MAC 주소의 매핑을 확인한다. 같은 네트워크 안의 인접 호스트를 확인할 때 쓰며, 보안 수업에서는 ARP spoofing 같은 공격을 이해하는 데 기초가 된다. 이 강의에서는 공격 실습까지 들어가지는 않고, “LAN 안의 이웃 정보와 MAC 주소를 보는 도구”라는 점을 잡는다.</p>
                    """ + os12_arp + code_block("""
                    arp
                    arp -a
                    arp -n
                    arp -s <ip> <mac>
                    arp -d <ip>
                    """, "bash") + """
                    <p><code>route</code>는 라우팅 테이블을 확인하고 수정한다. 라우팅 테이블은 목적지 네트워크별로 어느 gateway와 인터페이스로 패킷을 보낼지 결정하는 표다. 인터넷이 되려면 일반적으로 default route가 올바른 gateway를 가리켜야 한다.</p>
                    """ + os12_route + code_block("""
                    route
                    route -n

                    sudo route add default gw 10.0.2.2
                    sudo route del default gw 10.0.2.2

                    sudo route add -net 192.168.0.0 netmask 255.255.255.0 gw 10.0.2.2
                    sudo route del -net 192.168.0.0 netmask 255.255.255.0
                    """, "bash") + """
                    <p><code>ip</code> 명령은 현대 리눅스에서 인터페이스와 주소, 라우팅, 정책 기반 라우팅을 포괄하는 도구다. <code>ip link</code>, <code>ip addr</code>, <code>ip route</code>, <code>ip rule</code>처럼 하위 명령을 붙여 사용한다.</p>
                    """ + os12_ip + code_block("""
                    ip link
                    ip addr
                    ip addr show enp0s3
                    ip route
                    ip route show table main
                    ip rule

                    sudo ip addr add 10.0.2.15/24 dev enp0s3
                    sudo ip addr del 10.0.2.15/24 dev enp0s3
                    sudo ip link set enp0s3 up
                    sudo ip link set enp0s3 down
                    """, "bash") + """
                    <p>강사는 정책 기반 라우팅(PBR, Policy Based Routing)도 언급한다. 출발지나 정책에 따라 다른 라우팅 테이블을 쓰는 고급 기능이며, 이 수업 수준에서는 깊게 다루지 않고 <code>ip rule</code>, <code>ip route add ... table 1</code> 같은 형태가 있다는 정도만 기억하면 된다.</p>
                    """,
                },
                {
                    "heading": "열린 포트와 연결 상태: netstat, ss",
                    "body": """
                    <p>네트워크 서비스가 제대로 열려 있는지, 어떤 포트가 listening 중인지 확인하려면 <code>netstat</code> 또는 <code>ss</code>를 사용한다. 강의 화면에서는 <code>netstat</code> 옵션으로 프로토콜, 로컬 주소, 외부 주소, 상태, PID/프로그램 정보를 함께 보는 예시를 보여 준다.</p>
                    """ + os12_netstat + code_block("""
                    netstat
                    netstat -tulpen
                    netstat -ant

                    ss
                    ss -tulpen
                    ss -ant
                    """, "bash") + """
                    <p><code>-t</code>는 TCP, <code>-u</code>는 UDP, <code>-l</code>은 listening 소켓, <code>-p</code>는 프로세스 정보, <code>-e</code>는 확장 정보, <code>-n</code>은 이름 해석 없이 숫자로 표시하는 옵션으로 이해하면 된다. 악성 프로세스가 외부 연결을 열었는지, 웹 서버가 80번 포트에서 정상 대기 중인지 확인할 때 이런 명령을 쓴다.</p>
                    """,
                },
                {
                    "heading": "연결성, 경로, DNS: ping, traceroute, nslookup",
                    "body": """
                    <p><code>ping</code>은 ICMP echo request를 보내고 echo reply가 돌아오는지 확인한다. 대상이 살아 있는지, 왕복 지연 시간이 어느 정도인지, 패킷 손실이 있는지 보는 가장 기본적인 도구다. 강의 예시는 <code>8.8.8.8</code> 같은 외부 IP로 연결을 확인한다.</p>
                    """ + os12_ping + code_block("""
                    ping 8.8.8.8
                    ping -c 3 8.8.8.8
                    """, "bash") + """
                    <p><code>traceroute</code>는 목적지까지 거치는 라우터 경로를 보여 준다. 설치되어 있지 않으면 <code>sudo apt install traceroute</code>로 설치한다. 다만 현대 네트워크에서는 방화벽이나 중간 장비가 ICMP 응답을 막아 일부 홉이 별표로 보일 수 있다. 경로가 비어 보인다고 곧바로 네트워크가 끊겼다고 단정하면 안 된다.</p>
                    """ + os12_traceroute + code_block("""
                    sudo apt install traceroute

                    traceroute 8.8.8.8
                    traceroute www.google.com
                    traceroute www.naver.com
                    traceroute www.daum.com
                    """, "bash") + """
                    <p><code>nslookup</code>은 도메인 이름을 IP 주소로 변환하는 DNS 조회 도구다. DNS 서버가 정상인지, 도메인이 어떤 주소로 해석되는지, 특정 DNS 서버를 지정했을 때 결과가 달라지는지 확인할 수 있다.</p>
                    """ + os12_nslookup + code_block("""
                    nslookup google.com
                    nslookup google.com 8.8.8.8
                    nslookup www.naver.com
                    nslookup www.naver.com 8.8.8.8
                    """, "bash") + """
                    <p>강사는 과거에는 <code>/etc/resolv.conf</code>에 DNS 서버를 직접 쓰는 방식이 단순했지만, Ubuntu 20.04에서는 <code>systemd-resolved</code>와 netplan을 통해 DNS가 관리되는 구조를 이해해야 한다고 설명한다. DNS spoofing처럼 의도와 다른 IP가 반환되는 공격도 있으므로, DNS 조회 결과는 보안 점검에서도 중요한 단서가 된다.</p>
                    """,
                },
                {
                    "heading": "패킷 관찰: tcpdump",
                    "body": """
                    <p><code>tcpdump</code>는 네트워크 트래픽을 직접 캡처하고 분석하는 도구다. 특정 인터페이스에서 오가는 패킷을 터미널에 출력하거나, 파일로 저장해 나중에 Wireshark 같은 도구로 열어 볼 수 있다. 강사는 이 도구만으로도 몇 시간 강의가 가능할 만큼 내용이 방대하므로, 여기서는 기본 형태와 필터 감각을 잡는 수준으로 소개한다.</p>
                    """ + os12_tcpdump + code_block("""
                    tcpdump -i enp0s3
                    tcpdump -i enp0s3 -w test.pcap
                    tcpdump -i enp0s3 -w test.pcap -c 10
                    tcpdump -i enp0s3 -nn
                    """, "bash") + """
                    <p>주요 옵션은 다음처럼 읽으면 된다. <code>-i</code>는 인터페이스, <code>-c</code>는 캡처할 패킷 수, <code>-w</code>는 파일 저장, <code>-r</code>은 저장 파일 읽기, <code>-n</code>은 주소 이름 해석 생략, <code>-nn</code>은 주소와 포트 이름 해석을 모두 생략한다.</p>
                    """ + os12_tcpdump_filters + code_block("""
                    tcpdump -i enp0s3 icmp
                    tcpdump -i enp0s3 host 1.2.3.4
                    tcpdump -i enp0s3 src 1.2.3.4
                    tcpdump -i enp0s3 dst 1.2.3.4
                    tcpdump -i enp0s3 src 1.2.3.4 and port 80
                    tcpdump 'dst 192.168.0.2 and src not 192.168.0.1'
                    tcpdump dst 8.8.8.8 and '(src port 3392 or 22)'
                    tcpdump 'src 8.8.8.8 and dst port 3399 or 22'
                    """, "bash") + """
                    <p>필터에는 <code>icmp</code>, <code>host</code>, <code>src</code>, <code>dst</code>, <code>port</code>, <code>portrange</code>, <code>and</code>, <code>or</code>, <code>not</code>을 조합한다. 운영자는 서비스 장애를 볼 때 “패킷이 서버까지 오는가”, “서버가 응답을 내보내는가”, “중간에서 DNS나 라우팅이 틀어졌는가”를 이런 도구로 단계적으로 확인한다.</p>
                    <p>이 강의는 OS 기초의 마지막 운영 도구 정리다. 완전한 숙달은 이후 네트워크, 보안 관제, 침해 대응 실습에서 반복해야 하지만, 여기서 배운 명령들은 실제 서버에 문제가 생겼을 때 가장 먼저 떠올릴 기본 점검 도구들이다.</p>
                    """,
                },
            ],
            "checks": [
                "`users`, `who`, `w`가 현재 접속자를 어느 수준까지 보여 주는지 구분할 수 있는가?",
                "TTY와 PTS의 차이, `wall`과 `write`의 용도를 설명할 수 있는가?",
                "`last`, `lastb`, `/var/log/wtmp`, `/var/log/btmp`, `.bash_history`, `/var/log/auth.log`가 각각 어떤 흔적을 남기는지 이해했는가?",
                "`Ctrl+Z`, `bg`, `fg`, `jobs`, `Ctrl+C`로 foreground/background 작업을 제어할 수 있는가?",
                "`ps aux`, 프로세스 상태 문자, `/proc/<pid>`, `pstree`를 이용해 실행 중 프로세스를 분석할 수 있는가?",
                "`kill`, `killall`, `SIGTERM`, `SIGKILL`의 차이와 `kill -9`를 신중하게 써야 하는 이유를 설명할 수 있는가?",
                "`lsof`, `strace`, `ltrace`가 각각 열린 파일, 시스템 콜, 라이브러리 콜을 관찰한다는 점을 이해했는가?",
                "ifconfig, NetworkManager, netplan이 Ubuntu 네트워크 설정에서 어떤 관계를 가지는지 설명할 수 있는가?",
                "ARP, route, ip, netstat/ss가 각각 인접 호스트, 라우팅, 인터페이스·정책, 포트·연결 상태를 확인한다는 점을 구분할 수 있는가?",
                "ping, traceroute, nslookup, tcpdump를 연결성·경로·DNS·패킷 관찰 단계에 맞춰 사용할 수 있는가?",
            ],
        },
    ]
