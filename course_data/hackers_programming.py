def build_hackers_programming_lectures(code_block, screen_figure):
    square_test = code_block(
        """
        number = int(input("number: "))
        print(number ** 2)
        """,
        "python",
    )

    base64_decoder = code_block(
        """
        import base64
        from pprint import pprint

        with open("base64examples.txt", "r", encoding="utf-8") as file:
            lines = file.readlines()

        for line in lines:
            decoded = base64.b64decode(line.strip()).decode()
            if decoded.startswith("WHS"):
                print(decoded)
        """,
        "python",
    )

    request_note_search = code_block(
        """
        import requests
        from tqdm import tqdm

        for idx in tqdm(range(1, 101)):
            url = f"https://note.nyan101.com/{idx}"
            response = requests.get(url)
            body = response.content.decode()

            if "WHS" in body:
                print(idx)
                print(body)
        """,
        "python",
    )

    api_key_example = code_block(
        """
        import os
        import requests

        keyword = input("검색어: ")
        headers = {
            "X-Naver-Client-Id": os.environ["NAVER_CLIENT_ID"],
            "X-Naver-Client-Secret": os.environ["NAVER_CLIENT_SECRET"],
        }
        params = {"query": keyword, "display": 5}

        response = requests.get(
            "https://openapi.naver.com/v1/search/news.json",
            headers=headers,
            params=params,
        )
        response.raise_for_status()

        for item in response.json()["items"]:
            print(item["title"], item["link"])
        """,
        "python",
    )

    n8n_flow = code_block(
        """
        Schedule Trigger: 매일 아침 실행
        -> Set: keyword = "보안", "사이버", "해킹"
        -> HTTP Request: 네이버 검색 API 호출
        -> Code or Item Lists: 필요한 제목, 링크, 요약만 정리
        -> Google Sheets: 검색 결과 행 추가
        -> Slack or Gmail: 새 결과가 있으면 알림
        """,
        "text",
    )

    csv_join_example = code_block(
        """
        from pprint import pprint

        person_db = []

        lines = open("./person_info/email_address.csv", "r", encoding="utf-8").readlines()
        for line in lines:
            email, address = line.strip().split(",")
            person_db.append({
                "email": email,
                "address": address,
            })

        lines = open("./person_info/email_job.csv", "r", encoding="utf-8").readlines()
        for line in lines:
            email, job = line.strip().split(",")
            for person in person_db:
                if person["email"] == email:
                    person["job"] = job

        lines = open("./person_info/email_phone.csv", "r", encoding="utf-8").readlines()
        for line in lines:
            email, phone = line.strip().split(",")
            for person in person_db:
                if person["email"] == email:
                    person["phone"] = phone

        lines = open("./person_info/name_email.csv", "r", encoding="utf-8").readlines()
        for line in lines:
            name, email = line.strip().split(",")
            for person in person_db:
                if person["email"] == email:
                    person["name"] = name

        lines = open("./person_info/phone_sex.csv", "r", encoding="utf-8").readlines()
        for line in lines:
            phone, sex = line.strip().split(",")
            for person in person_db:
                if person["phone"] == phone:
                    person["sex"] = sex

        pprint(person_db)
        """,
        "python",
    )

    transaction_accumulate = code_block(
        """
        G = {}

        lines = open("./transactions.txt", "r", encoding="utf-8").readlines()

        for line in lines:
            src, dst, amount = line.strip().split(",")
            amount = int(amount)

            if src not in G:
                G[src] = {}

            if dst not in G[src]:
                G[src][dst] = 0

            G[src][dst] += amount

        for src in G:
            for dst in G[src]:
                print(f"{src} -> {dst} [{G[src][dst]}]")
        """,
        "python",
    )

    transaction_net_edges = code_block(
        """
        for src in G:
            for dst in G[src]:
                reverse_amount = G.get(dst, {}).get(src, 0)
                amount = G[src][dst] - reverse_amount
                if amount > 0:
                    print(f"{src} -> {dst} [{amount}]")
        """,
        "python",
    )

    transaction_graph = code_block(
        """
        G = {}

        lines = open("./transactions.txt", "r", encoding="utf-8").readlines()

        for line in lines:
            src, dst, amount = line.strip().split(",")
            amount = int(amount)

            if src not in G:
                G[src] = {}

            if dst not in G[src]:
                G[src][dst] = 0

            G[src][dst] += amount

        print("digraph BookingWorkflow {")
        for src in G:
            for dst in G[src]:
                amount = G[src][dst] - G.get(dst, {}).get(src, 0)
                if amount > 0:
                    print(f'  "{src}" -> "{dst}" [label="{amount}"]')
        print("}")
        """,
        "python",
    )

    bs4_selector = code_block(
        """
        import requests
        from bs4 import BeautifulSoup

        url = "http://dungeon.nyan101.com/HWJG.html"
        response = requests.get(url)

        soup = BeautifulSoup(response.content, "html.parser")

        elements = soup.select("body > div.navigation > a:nth-child(2)")
        print(f"링크 텍스트: {elements[0].text}")
        print(f"링크 URL: {elements[0]['href']}")
        """,
        "python",
    )

    bs4_all_links = code_block(
        """
        import requests
        from bs4 import BeautifulSoup

        url = "http://dungeon.nyan101.com/HWJG.html"
        response = requests.get(url)

        soup = BeautifulSoup(response.content, "html.parser")

        # selector에 해당하는 요소가 여럿인 경우
        elements = soup.select("body > div.navigation > a")
        for idx, element in enumerate(elements):
            print(f"{idx}번째 링크. 텍스트: {element.text} -> URL: {element['href']}")
        """,
        "python",
    )

    bs4_link_href_loop = code_block(
        """
        links = soup.select("body > div.navigation > a")
        for link in links:
            print(link["href"])

        visited_paths = set()

        def traversal(path):
            if path in visited_paths:
                return

            visited_paths.add(path)
        """,
        "python",
    )

    bs4_crawler = code_block(
        """
        import requests
        from bs4 import BeautifulSoup

        visited_paths = set()

        def traversal(path):
            if path in visited_paths:
                return
            visited_paths.add(path)

            url = f"http://dungeon.nyan101.com/{path}"
            response = requests.get(url)
            body = response.content.decode()

            if "WHS" in body:
                print(body)

            soup = BeautifulSoup(body, "html.parser")
            links = soup.select("body > div.navigation > a")
            for link in links:
                print(f"{path} -> {link['href']} [{link.text}]")
                traversal(link["href"])

        traversal("index.html")
        """,
        "python",
    )

    osint_graph = code_block(
        """
        김민철 멘토 --uses--> nyan101
        nyan101 --account--> GitHub
        nyan101 --may-also-use--> GitLab
        nyan101 --may-also-use--> Instagram
        김민철 멘토 --affiliation--> 화이트햇 스쿨
        GitHub repository --followed-by--> 홍길동
        Facebook 김철수 --friend--> 홍길동
        Instagram post --tagged--> 홍길동
        """,
        "text",
    )
    hp01 = "해커의 프로그래밍-01-강의-오리엔테이션"
    hp01_hacker_meaning = screen_figure(
        "hackers-programming",
        hp01,
        4,
        "해커라는 단어의 의미",
        "화면에는 위키백과의 해커 정의가 제시된다. 강사는 해커를 단순 침입자가 아니라 컴퓨터와 정보보안 전반을 깊이 이해하는 사람으로 설명한다.",
    )
    hp01_not_scope = screen_figure(
        "hackers-programming",
        hp01,
        10,
        "이 강의에서 다루지 않는 것",
        "웹셸 업로드, 비밀글 열람, 전산망 침해, 댓글 상대 해킹 같은 불법 침입 행위는 이 강의의 범위가 아니라고 못박는다.",
    )
    hp01_scope = screen_figure(
        "hackers-programming",
        hp01,
        13,
        "이 강의에서 다루는 것",
        "게시판 대량 글에서 필요한 정보 찾기, 사이트 구조 자동 파악, 거래내역 기반 자금 흐름 구성, 여러 출처 정보 종합이 핵심 학습 대상이다.",
    )
    hp01_three_tracks = screen_figure(
        "hackers-programming",
        hp01,
        19,
        "주요 추세: Web, Data, Tool",
        "전체 과목은 웹 스크래핑과 자동화, 데이터 분석, 오픈소스 도구 활용이라는 세 축으로 전개된다.",
    )
    hp01_ethics = screen_figure(
        "hackers-programming",
        hp01,
        37,
        "실습 범위 주의",
        "실습으로 제시된 사이트 외 일반 사이트를 대상으로 수행하지 말라는 법적·윤리적 제한을 마지막에 다시 강조한다.",
    )
    hp02 = "해커의 프로그래밍-02-파이썬-환경과-Base64-실습"
    hp02_code_runner = screen_figure(
        "hackers-programming",
        hp02,
        11,
        "VS Code Code Runner 확장 설치",
        "VS Code 확장 탭에서 Code Runner를 검색해 설치한다. 이후 Python 파일을 빠르게 실행하기 위한 실습 편의 도구로 사용된다.",
    )
    hp02_test_run = screen_figure(
        "hackers-programming",
        hp02,
        16,
        "test.py 실행과 터미널 입력 확인",
        "간단한 Python 파일을 만들고 실행해, 터미널에서 숫자 입력을 받을 수 있는지 확인한다.",
    )
    hp02_base64 = screen_figure(
        "hackers-programming",
        hp02,
        21,
        "Base64 인코딩 원리",
        "Base64가 64개 문자와 6비트 단위를 사용해 임의 바이트를 출력 가능한 문자로 바꾸는 방식을 설명하는 핵심 슬라이드다.",
    )
    hp02_cyberchef = screen_figure(
        "hackers-programming",
        hp02,
        36,
        "CyberChef 화면 구성",
        "왼쪽 작업 목록, 가운데 레시피, 오른쪽 입력과 출력 영역을 확인하며 인코딩·디코딩 작업을 조합하는 방식을 익힌다.",
    )
    hp02_decoder_code = screen_figure(
        "hackers-programming",
        hp02,
        65,
        "Base64 자동 디코딩 최종 코드",
        "파일의 각 줄을 Base64로 디코딩하고, 결과 문자열에 WHS가 들어 있는 경우만 출력하는 최종 코드 화면이다.",
    )
    hp03 = "해커의 프로그래밍-03-HTTP와-웹-스크래핑"
    hp03_http = screen_figure(
        "hackers-programming",
        hp03,
        6,
        "HTTP 요청과 응답의 기본 구조",
        "HTTP는 클라이언트 요청과 서버 응답으로 이루어지고, 헤더와 바디, 메소드와 상태 코드로 구분된다는 핵심 개념을 정리한다.",
    )
    hp03_real_request = screen_figure(
        "hackers-programming",
        hp03,
        11,
        "화이트햇 스쿨 홈페이지 실제 HTTP 요청",
        "실제 브라우저 요청에는 Host, Cookie, User-Agent, Accept, Sec-Fetch 계열 헤더처럼 예시보다 많은 정보가 포함된다.",
    )
    hp03_html_source = screen_figure(
        "hackers-programming",
        hp03,
        21,
        "브라우저에서 HTML 소스 보기",
        "화면에 보이는 웹페이지도 내부적으로는 태그가 중첩된 HTML 문서이며, 소스 보기로 구조를 직접 확인할 수 있다.",
    )
    hp03_requests = screen_figure(
        "hackers-programming",
        hp03,
        36,
        "requests로 GET과 POST 요청 보내기",
        "Python requests에서는 GET의 query string을 params로, POST의 본문 데이터를 data나 json으로 구성한다.",
    )
    hp03_final_code = screen_figure(
        "hackers-programming",
        hp03,
        61,
        "100개 노트 중 WHS 문자열 찾기",
        "1번부터 100번까지 반복 요청을 보내고, 응답 본문에 WHS가 들어 있는 페이지를 찾아 출력하는 최종 실습 코드다.",
    )
    hp04 = "해커의 프로그래밍-04-웹-API와-키-관리"
    hp04_api_definition = screen_figure(
        "hackers-programming",
        hp04,
        5,
        "API의 의미와 Web API 범위",
        "API는 서로 다른 소프트웨어가 약속된 방식으로 상호작용하는 인터페이스이며, 이 강의에서는 HTTP와 JSON 기반 Web API에 집중한다.",
    )
    hp04_api_response = screen_figure(
        "hackers-programming",
        hp04,
        13,
        "API 사용 시 명료한 요청과 정돈된 응답",
        "브라우저 검색 화면과 달리 API는 요청 인자와 응답 구조가 명확하고, JSON 같은 형태로 필요한 데이터만 받기 쉽다.",
    )
    hp04_naver_api = screen_figure(
        "hackers-programming",
        hp04,
        17,
        "네이버 개발자 센터의 API 목록",
        "검색, 로그인, 회원 프로필, CLOVA, 데이터랩, 캡차, 캘린더처럼 서비스별 API가 제공되고 호출 제한도 함께 관리된다.",
    )
    hp04_key_leak = screen_figure(
        "hackers-programming",
        hp04,
        29,
        "API 키 유출 사고 사례",
        "공개 저장소나 설정 파일에 남은 API 키와 env 파일은 대규모 침해나 무단 사용으로 이어질 수 있다.",
    )
    hp04_rules = screen_figure(
        "hackers-programming",
        hp04,
        37,
        "외부 API 사용 시 보안수칙",
        "API 키는 코드에 하드코딩하지 않고 별도 설정으로 관리하며, 업로드 전 포함 여부를 확인하고 유출 시 즉시 만료·재발급해야 한다.",
    )
    hp05 = "해커의 프로그래밍-05-n8n-워크플로우-자동화"
    hp05_features = screen_figure(
        "hackers-programming",
        hp05,
        5,
        "n8n의 드래그앤드롭 UI와 외부 연동",
        "n8n은 Schedule Trigger, HTTP Request, Google Sheets, Telegram, Discord, Postgres, Notion 같은 노드를 연결해 작업을 구성한다.",
    )
    hp05_examples = screen_figure(
        "hackers-programming",
        hp05,
        9,
        "n8n 활용 예시",
        "소규모 비즈니스 알림, Google Sheets와 DB·Slack 연동, 신규 IP 접속 시 VirusTotal 조회와 알림 같은 보안 자동화를 예로 든다.",
    )
    hp05_docker = screen_figure(
        "hackers-programming",
        hp05,
        13,
        "Docker 이미지로 로컬 n8n 구축",
        "공식 Docker 이미지를 이용하면 개인 시스템에 n8n 서버를 띄워 기능 제한 없이 실습할 수 있다.",
    )
    hp05_workflow = screen_figure(
        "hackers-programming",
        hp05,
        17,
        "노드 그래프로 표현한 작업 흐름",
        "Schedule Trigger에서 시작해 Edit Fields, HTTP Request, Split Out, Remove Duplicates, Google Sheets, Slack으로 이어지는 워크플로우 예시다.",
    )
    hp05_debug = screen_figure(
        "hackers-programming",
        hp05,
        29,
        "개별 노드의 입력과 출력 비교",
        "n8n은 각 노드의 INPUT과 OUTPUT 데이터를 비교하면서 HTTP 요청 결과와 다음 노드로 넘어가는 값을 확인할 수 있다.",
    )
    hp06 = "해커의 프로그래밍-06-개인정보-유출과-데이터-결합"
    hp06_leak_causes = screen_figure(
        "hackers-programming",
        hp06,
        7,
        "개인정보 유출 사고의 원인",
        "해킹, 내부자 유출, 업무상 과실뿐 아니라 중소규모 웹사이트, 해외 홈쇼핑, 브라우저 확장 취약점도 유출 경로가 될 수 있음을 보여 준다.",
    )
    hp06_breachforums = screen_figure(
        "hackers-programming",
        hp06,
        13,
        "BreachForums와 유출 데이터 유통",
        "BreachForums는 개인정보 유출 데이터를 거래·공유하는 온라인 포럼의 예시이며, 국내 유출 사고 관련 정보도 함께 올라올 수 있음을 보여 준다.",
    )
    hp06_mosaic = screen_figure(
        "hackers-programming",
        hp06,
        19,
        "모자이크 이론",
        "각각은 사소한 단서라도 아이디, 메일 주소, 가입 사이트, 거주지 단서, 직장 관계를 결합하면 새로운 사실을 추정할 수 있다.",
    )
    hp06_join = screen_figure(
        "hackers-programming",
        hp06,
        31,
        "데이터 결합과 JOIN 방식",
        "두 데이터 집합을 공통 속성으로 결합하고, 목적에 따라 INNER JOIN, LEFT/RIGHT JOIN, OUTER JOIN을 선택하는 기준을 정리한다.",
    )
    hp06_faker = screen_figure(
        "hackers-programming",
        hp06,
        37,
        "Faker를 이용한 가상 개인정보 생성",
        "Faker는 이름, 직업, 이메일, 주소, 전화번호, SSN 형식의 값을 만들 수 있고, ko_KR 로케일로 한국식 가상 정보도 생성할 수 있다.",
    )
    hp06_merge_code = screen_figure(
        "hackers-programming",
        hp06,
        84,
        "가상 개인정보 병합 코드",
        "실습에서는 person_info 폴더의 email_address.csv, email_job.csv, email_phone.csv, name_email.csv, phone_sex.csv를 읽고 이메일과 전화번호를 기준으로 흩어진 값을 하나의 딕셔너리에 병합한다.",
    )
    hp06_name_sex = screen_figure(
        "hackers-programming",
        hp06,
        80,
        "이름과 성별 정보 추가 병합",
        "주소, 직업, 전화번호를 붙인 뒤 name_email.csv로 이름을, phone_sex.csv로 성별을 추가해 최종 개인정보 레코드를 완성한다.",
    )
    hp07 = "해커의 프로그래밍-07-가상자산-믹싱과-거래-그래프"
    hp07_etherscan = screen_figure(
        "hackers-programming",
        hp07,
        5,
        "블록체인 거래 공개와 Etherscan",
        "Etherscan처럼 실시간 트랜잭션을 볼 수 있는 사이트가 있어도, 거래가 여러 노드로 쪼개지면 실제 의미 있는 흐름은 흐려질 수 있다.",
    )
    hp07_mixing_split = screen_figure(
        "hackers-programming",
        hp07,
        9,
        "단순 송금이 복잡한 거래망으로 나뉘는 방식",
        "A가 B에게 1000원을 보낸 단순 흐름과, 중간 노드 C·D·E·F를 거치지만 최종 효과는 같은 흐름을 비교해 믹싱의 직관을 보여 준다.",
    )
    hp07_grouping = screen_figure(
        "hackers-programming",
        hp07,
        17,
        "믹싱 노드 그룹화",
        "믹싱 서비스에 속한 여러 노드를 하나의 그룹 X로 묶으면 그룹 내부 거래보다 그룹 바깥에서 들어오고 나가는 자금 흐름에 집중할 수 있다.",
    )
    hp07_graph_structure = screen_figure(
        "hackers-programming",
        hp07,
        29,
        "그래프 구조: 정점과 간선",
        "거래 주체를 정점, 송금 방향과 금액을 간선으로 보면 자금 흐름을 방향 그래프로 표현할 수 있다.",
    )
    hp07_graphviz = screen_figure(
        "hackers-programming",
        hp07,
        37,
        "Graphviz를 이용한 그래프 시각화",
        "Graphviz는 텍스트로 작성한 노드와 간선 정의를 그래프로 렌더링하며, 온라인 편집기에서 바로 결과를 확인할 수 있다.",
    )
    hp07_mission = screen_figure(
        "hackers-programming",
        hp07,
        41,
        "실습 미션: 거래 내역으로 조직도 재구성",
        "transactions.txt에는 송금자, 수취인, 송금액이 한 줄씩 들어 있고, 상하 관계가 아닌 조직원끼리 주고받은 금액의 총합은 0이라는 조건이 주어진다.",
    )
    hp07_accumulate_code = screen_figure(
        "hackers-programming",
        hp07,
        64,
        "거래 누적 딕셔너리 구성",
        "각 거래 줄을 송금자, 수취인, 금액으로 나누고 G[src][dst]에 금액을 누적해 방향 그래프의 기본 자료구조를 만든다.",
    )
    hp07_raw_edges = screen_figure(
        "hackers-programming",
        hp07,
        69,
        "누적 그래프 원본 출력",
        "누적한 딕셔너리를 그대로 출력하면 양방향 거래와 잡음 거래가 모두 남아 있어 실제 상납 구조가 잘 보이지 않는다.",
    )
    hp07_reverse_lookup = screen_figure(
        "hackers-programming",
        hp07,
        77,
        "반대 방향 거래 조회와 KeyError",
        "반대 방향 거래를 빼려 할 때 도착 노드가 바깥 딕셔너리에 없을 수 있으므로 단순 인덱싱 대신 get()으로 기본값을 주어야 한다.",
    )
    hp07_net_edges = screen_figure(
        "hackers-programming",
        hp07,
        79,
        "순흐름만 남긴 거래 출력",
        "G[src][dst]에서 반대 방향 금액을 뺀 값이 0보다 클 때만 출력하면 중복·상쇄 거래가 사라지고 핵심 흐름만 남는다.",
    )
    hp07_final_graph = screen_figure(
        "hackers-programming",
        hp07,
        81,
        "정리된 순흐름 그래프",
        "양방향 거래를 상쇄한 뒤 Graphviz에 붙이면 복잡한 거래망에서 홍길동으로 돈이 모이는 조직 구조가 드러난다.",
    )
    hp08 = "해커의 프로그래밍-08-BeautifulSoup-웹-페이지-분석"
    hp08_bs4 = screen_figure(
        "hackers-programming",
        hp08,
        5,
        "BeautifulSoup의 기본 역할",
        "BeautifulSoup은 HTML/XML 문서를 파싱해 title, p, a, id 같은 요소를 Python 코드로 찾고 탐색할 수 있게 해 준다.",
    )
    hp08_selector = screen_figure(
        "hackers-programming",
        hp08,
        17,
        "Copy selector와 select() 실습",
        "개발자 도구에서 복사한 CSS selector를 BeautifulSoup의 select()에 넣어 특정 문 링크의 텍스트와 href 값을 출력한다.",
    )
    hp08_all_links = screen_figure(
        "hackers-programming",
        hp08,
        21,
        "조건을 만족하는 모든 요소 탐색",
        "nth-child 조건을 제거하고 body > div.navigation > a를 선택하면 빨간 문, 파란 문, 초록 문 링크를 모두 순회할 수 있다.",
    )
    hp08_crawling = screen_figure(
        "hackers-programming",
        hp08,
        25,
        "웹 크롤링의 의미",
        "크롤러는 시작 페이지에서 링크를 따라 2차, 3차 페이지로 이동하며 사이트 구조와 연결 관계를 탐색한다.",
    )
    hp08_mission = screen_figure(
        "hackers-programming",
        hp08,
        33,
        "미궁 사이트 탐색 미션",
        "각 방에 1~3개의 문이 있고, 여러 방 중 하나에 WHS 형식 보물 문자열이 있으므로 requests로 링크를 따라가며 찾아야 한다.",
    )
    hp08_traversal = screen_figure(
        "hackers-programming",
        hp08,
        57,
        "visited_paths와 재귀 탐색",
        "이미 방문한 방은 다시 탐색하지 않도록 visited_paths 집합을 두고, 각 링크의 href 값을 다시 traversal()에 넘기는 구조를 만든다.",
    )
    hp08_treasure = screen_figure(
        "hackers-programming",
        hp08,
        65,
        "보물 방 MMVK",
        "재귀 탐색 결과 MMVK.html에서 WHS 형식의 보물 문자열을 발견하고, 더 이상 이동할 방이 없는 막다른 길임을 확인한다.",
    )
    hp08_sitemap = screen_figure(
        "hackers-programming",
        hp08,
        77,
        "던전 지도 재구성 결과",
        "출발 방, 도착 방, 문 이름을 줄 단위로 입력하면 지도 페이지에서 전체 연결 그래프와 플래그 위치를 시각화할 수 있다.",
    )
    hp09 = "해커의 프로그래밍-09-OSINT와-정보-그래프"
    hp09_definition = screen_figure(
        "hackers-programming",
        hp09,
        3,
        "공개출처정보의 정의",
        "OSINT는 특별한 권한 없이 접근 가능한 공개 출처에서 수집된 모든 정보이며, 뉴스·블로그·SNS·정부 발표 등을 포함한다.",
    )
    hp09_use_cases = screen_figure(
        "hackers-programming",
        hp09,
        5,
        "OSINT 활용 사례",
        "사이버보안, 방산, 첩보 분야에서 공개 자료와 검색엔진을 이용해 전쟁, 악성코드, 인프라 위험 정보를 분석한다.",
    )
    hp09_criminalip = screen_figure(
        "hackers-programming",
        hp09,
        9,
        "Criminal IP 기반 CTI 검색",
        "Criminal IP는 IP 주소, 도메인, 포트, 배너, 취약점, 위험 점수 같은 사이버 위협 정보를 검색할 수 있는 OSINT 플랫폼이다.",
    )
    hp09_tool_classes = screen_figure(
        "hackers-programming",
        hp09,
        11,
        "OSINT 도구 분류",
        "CTI 검색엔진, 연결 그래프 도구, SNS 특화 도구처럼 목적에 따라 OSINT 도구를 나누어 사용할 수 있다.",
    )
    hp09_cia_quote = screen_figure(
        "hackers-programming",
        hp09,
        17,
        "SNS가 만든 공개 정보 환경",
        "사람들이 거주지, 견해, 친구 목록, 연락처, 사진, 활동 정보를 스스로 공개하는 시대가 되었음을 CIA 사례로 설명한다.",
    )
    hp09_metadata = screen_figure(
        "hackers-programming",
        hp09,
        25,
        "사진 메타데이터와 위치 노출",
        "스마트폰 사진에는 기기명, 촬영 시각, 카메라 설정, 위치 정보가 자동으로 포함될 수 있으므로 원본 업로드에 주의해야 한다.",
    )
    hp09_llm_risk = screen_figure(
        "hackers-programming",
        hp09,
        29,
        "LLM 시대의 공개 게시물 조합 위험",
        "핫스팟 이름, 블루투스 기기명, SNS 글처럼 사소한 단서도 LLM으로 대량 조합하면 위치나 신상 단서가 될 수 있다.",
    )
    hp09_predicta_start = screen_figure(
        "hackers-programming",
        hp09,
        35,
        "Predicta Graph 새 그래프 생성",
        "Predicta Graph에서 새 그래프를 만들고, 인물·조직·계정·서비스 같은 노드를 추가할 준비를 한다.",
    )
    hp09_predicta_graph = screen_figure(
        "hackers-programming",
        hp09,
        49,
        "Predicta Graph 정보 연결 예시",
        "화이트햇 스쿨, 김민철, nyan101, GitHub, Facebook, Instagram 게시물과 태그를 그래프 노드와 간선으로 연결한다.",
    )

    return [
        {
            "id": "1-1",
            "title": "강의 오리엔테이션",
            "subtitle": "해커의 프로그래밍이 무엇을 다루고 무엇을 다루지 않는지, 웹·데이터·도구 흐름으로 전체 과목을 잡는다.",
            "tags": ["오리엔테이션", "웹 자동화", "데이터 분석"],
            "objectives": [
                "해커라는 단어의 원래 의미와 이 과목에서 사용하는 의미를 이해한다.",
                "웹 취약점 공격 강의가 아니라 로직을 코드와 도구로 구현하는 수업임을 구분한다.",
                "웹, 데이터, 도구라는 세 축으로 이후 강의 흐름을 설명할 수 있다.",
                "실습 대상은 제공된 환경으로 제한해야 한다는 윤리·법적 기준을 기억한다.",
            ],
            "sections": [
                {
                    "heading": "멘토 소개와 과목 이름의 의미",
                    "body": f"""
                    <p>강의는 김민철 멘토의 소개로 시작한다. 멘토는 군에서 약 7년 동안 사이버 보안 업무를 수행했고, 국방과 공공 분야의 여러 기관을 거치며 정보보호 업무를 경험했다. 대회와 실무를 겪으며 느낀 점은 취약점을 많이 알고 익스플로잇을 작성하는 능력도 중요하지만, 머릿속에 떠오른 로직을 코드로 정확히 옮기고 이미 존재하는 도구를 이해해 활용하는 능력도 매우 중요하다는 것이다.</p>
                    <p>이런 이유로 과목 이름은 <strong>해커의 프로그래밍</strong>이다. 오늘날 프로그래머는 보통 개발자나 소프트웨어 엔지니어를 뜻하고, 해커는 해킹을 하는 사람이라는 뜻으로 많이 쓰인다. 하지만 멘토는 해커라는 단어의 원래 의미, 즉 어떤 원리를 파고들고 구조를 이해하며 문제를 풀어내는 사람이라는 의미에 가깝게 이 과목을 설명한다.</p>
                    {hp01_hacker_meaning}
                    <div class="callout">이 과목의 핵심은 “공격 기술 이름을 외우는 것”이 아니라 “필요한 정보를 얻기 위해 웹, 데이터, 도구를 어떻게 조합할지 생각하고 구현하는 것”이다.</div>
                    """,
                },
                {
                    "heading": "이 과목에서 다루지 않는 것",
                    "body": f"""
                    <p>강의는 먼저 범위를 명확히 자른다. 서버에 웹셸을 업로드해 임의 코드를 실행하는 것, 게시판의 숨겨진 비밀글을 보는 것, 파일 업로드 취약점, 히든 파라미터 취약점, 크로스 사이트 스크립팅, SQL 인젝션 같은 세부 웹해킹 기법은 이 과목의 중심이 아니다. 그런 내용은 별도의 웹해킹 전문 강의에서 다루는 영역이다.</p>
                    {hp01_not_scope}
                    <p>또한 전산망을 해킹해 거래 장부를 획득하거나 인터넷 댓글 창에서 상대방을 해킹하는 식의 공격도 다루지 않는다. 이 과목은 불법 침입을 배우는 시간이 아니라, 주어진 합법적 데이터와 허가된 실습 환경 안에서 필요한 정보를 자동화·분석·정리하는 방법을 배우는 시간이다.</p>
                    <table>
                      <thead><tr><th>다루지 않는 영역</th><th>이유</th></tr></thead>
                      <tbody>
                        <tr><td>웹셸 업로드, 임의 코드 실행</td><td>웹해킹 전문 강의의 영역이며 실제 서비스에서는 명백한 침해 행위가 될 수 있다.</td></tr>
                        <tr><td>SQL 인젝션, XSS, 파일 업로드 취약점</td><td>취약점 원리 자체보다 자동화와 데이터 처리 능력에 집중한다.</td></tr>
                        <tr><td>타인 시스템 침입과 댓글 상대 해킹</td><td>법적·윤리적으로 허용되지 않는 행위이며 화이트햇 스쿨의 목적과 맞지 않는다.</td></tr>
                      </tbody>
                    </table>
                    """,
                },
                {
                    "heading": "이 과목에서 다루는 것",
                    "body": f"""
                    <p>대신 이 과목은 현실의 보안 업무와 CTF 풀이에서 자주 필요한 자동화 사고를 다룬다. 예를 들어 게시판에 글이 천 개, 만 개, 수십만 개 있을 때 그중 필요한 글 하나를 수작업으로 찾기는 어렵다. 이때 프로그래밍으로 요청을 반복하고 조건을 검사하면 원하는 정보를 빠르게 찾을 수 있다.</p>
                    {hp01_scope}
                    <p>처음 보는 웹사이트의 구조를 자동으로 파악하는 법도 배운다. 웹 크롤링 또는 웹 스파이더링이라고 부르는 방식으로 링크를 따라가며 사이트 구조를 복원하고, 전체 페이지가 어떤 그래프 구조를 갖는지 확인한다.</p>
                    <p>거래 내역으로부터 자금 흐름을 구성하는 방법도 다룬다. 거래소를 해킹해 장부를 얻는 것이 아니라, 이미 주어진 거래 데이터가 있을 때 돈이 어디에서 어디로 흘렀는지 그래프로 단순화하는 사고를 배운다. 범죄 조직이나 가상자산 믹싱 사례처럼 A가 B에게 바로 보낸 흐름이 여러 단계를 거쳐 흐려질 때, 코드로 순흐름을 정리하는 방식이다.</p>
                    <p>마지막으로 여러 출처에 흩어진 정보를 종합하는 방법을 다룬다. 인터넷의 정보는 깔끔한 표 하나로 제공되지 않는 경우가 많다. 흩어진 글, 계정, 주소, 이메일, 게시물, 거래 내역을 연결해 사람이 이해할 수 있는 정보로 가공하는 능력이 중요하다.</p>
                    """,
                },
                {
                    "heading": "세 가지 큰 주제",
                    "body": f"""
                    <div class="timeline">
                      <div><strong>웹</strong><p>Python requests로 HTTP 요청을 보내고, HTML 구조를 이해하며, BeautifulSoup으로 필요한 요소를 뽑고, 크롤링으로 사이트 구조를 탐색한다.</p></div>
                      <div><strong>데이터</strong><p>거래 흐름 그래프, 개인정보 결합, OSINT처럼 흩어진 데이터를 분석해 유의미한 정보로 바꾼다.</p></div>
                      <div><strong>도구</strong><p>CyberChef, Graphviz, n8n 같은 도구를 필요한 시점에 활용해 반복 작업을 줄이고 결과를 보기 좋게 만든다.</p></div>
                    </div>
                    {hp01_three_tracks}
                    <p>웹 파트에서는 Python 환경 구축과 Base64 실습으로 시작한다. 이후 HTTP와 HTML을 살펴보고, requests로 요청을 자동화한다. 더 나아가 BeautifulSoup으로 HTML을 분석하고, 웹페이지끼리 연결된 그래프 구조를 따라가며 사이트맵을 복원한다.</p>
                    <p>데이터 파트에서는 가상자산 믹싱과 자금 흐름 그래프, 개인정보 유출 데이터의 결합, OSINT 분석을 다룬다. 툴 파트에서는 API 연동과 n8n 자동화를 다루며, 검색 API, CTI API, 메신저 봇 API, AI API, 클라우드 액세스 키 같은 주제를 소개한다.</p>
                    """,
                },
                {
                    "heading": "실습 범위와 윤리 기준",
                    "body": f"""
                    <p>멘토는 각 강의마다 작은 실습을 준비하지만, 실습은 멘토가 만든 예제 사이트와 제공된 파일을 대상으로 진행된다. 강의를 듣고 흥미가 생겼다고 해서 실제 운영 중인 외부 서비스를 대상으로 크롤링, 공격성 테스트, 개인정보 탐색을 시도해서는 안 된다.</p>
                    {hp01_ethics}
                    <p>정보통신망 관련 법, 개인정보 보호법 등 여러 법률이 있고, 화이트햇 스쿨의 목표는 합법적이고 윤리적인 보안 인재 양성이다. 따라서 호기심이 있어도 허가받지 않은 대상에는 실습 내용을 적용하지 않는 것이 이 과목의 기본 전제다.</p>
                    """,
                },
            ],
            "checks": [
                "이 과목에서 말하는 해커의 의미를 설명할 수 있는가?",
                "웹해킹 기법 강의와 해커의 프로그래밍 과목의 차이를 구분할 수 있는가?",
                "웹, 데이터, 도구 파트에서 각각 무엇을 배우는지 말할 수 있는가?",
                "제공된 실습 사이트 밖의 실제 서비스에 실습을 적용하면 안 되는 이유를 설명할 수 있는가?",
            ],
        },
        {
            "id": "1-2",
            "title": "파이썬 환경과 Base64 실습",
            "subtitle": "Python과 VS Code 실습 환경을 만들고, Base64와 CyberChef를 이해한 뒤 Python으로 디코딩을 자동화한다.",
            "tags": ["Python", "VS Code", "Base64"],
            "objectives": [
                "Python 3와 VS Code, Code Runner 확장 기능을 설치하고 실행 환경을 확인한다.",
                "Base64가 왜 필요한지 바이트, ASCII, 6비트 단위 표현과 연결해 이해한다.",
                "CyberChef에서 인코딩·디코딩·암호화 도구를 조합하는 방식을 익힌다.",
                "Python의 base64 패키지와 파일 읽기를 이용해 조건에 맞는 문자열을 자동으로 찾는다.",
            ],
            "sections": [
                {
                    "heading": "Python과 VS Code를 쓰는 이유",
                    "body": """
                    <p>강의는 Python 3와 Visual Studio Code를 실습 도구로 사용한다. Python은 수치해석, 공학, 과학, CTF, AI 분야에서 널리 쓰이는 범용 프로그래밍 언어다. CTF에서는 pwntools 같은 라이브러리가 자주 쓰이고, AI에서는 PyTorch와 TensorFlow 같은 라이브러리가 Python 생태계에서 널리 사용된다. 대학의 첫 프로그래밍 수업에서도 많이 쓰일 정도로 입문 난도가 낮은 편이다.</p>
                    <p>VS Code는 Python 전용 도구는 아니지만 다양한 확장 기능을 설치할 수 있고 무료로 사용할 수 있어 실습 환경 구성에 적합하다. 이 과목에서는 Python 자체와 VS Code를 연결하고, 코드를 빠르게 실행할 수 있도록 Code Runner 확장 기능을 사용한다.</p>
                    """,
                },
                {
                    "heading": "설치와 실행 설정",
                    "body": f"""
                    <table>
                      <thead><tr><th>단계</th><th>해야 할 일</th><th>이유</th></tr></thead>
                      <tbody>
                        <tr><td>Python 설치</td><td>python.org에서 Python 3 설치 파일을 내려받아 실행한다.</td><td>실습 코드를 실행할 기본 인터프리터가 필요하다.</td></tr>
                        <tr><td>PATH 설정</td><td>설치 화면의 <strong>Add Python EXE to PATH</strong> 항목을 체크한다.</td><td>VS Code 터미널과 명령줄에서 Python을 쉽게 찾게 한다.</td></tr>
                        <tr><td>VS Code 설치</td><td>code.visualstudio.com에서 운영체제에 맞는 설치 파일을 받는다.</td><td>코드 작성과 실행, 터미널 사용을 한 화면에서 처리한다.</td></tr>
                        <tr><td>설치 옵션 체크</td><td>설치 중 나오는 네 가지 편의 항목을 모두 체크한다.</td><td>나중에 파일 열기, 실행, 디버깅을 편하게 만든다.</td></tr>
                        <tr><td>Code Runner 설치</td><td>왼쪽 확장 기능 메뉴에서 Code Runner를 검색해 설치한다.</td><td>마우스 오른쪽 클릭 또는 단축키로 빠르게 코드를 실행한다.</td></tr>
                        <tr><td>Run In Terminal</td><td>Code Runner 설정에서 Run In Terminal을 켠다.</td><td>input()처럼 터미널 입력이 필요한 코드가 정상 동작한다.</td></tr>
                        <tr><td>Save Before Run</td><td>실행 전 저장 설정을 켠다.</td><td>수정한 코드가 저장되지 않아 이전 코드가 실행되는 실수를 줄인다.</td></tr>
                      </tbody>
                    </table>
                    {hp02_code_runner}
                    <p>설정이 끝나면 바탕화면에 <code>test.py</code>를 만들고 숫자를 입력받아 제곱을 출력하는 간단한 코드를 실행한다. Windows에서는 <code>Ctrl + Alt + N</code>, macOS에서는 <code>Command + Option + N</code>으로 실행할 수 있다. 실행 후 터미널을 클릭하고 숫자를 입력했을 때 코드가 그 값을 받아 제곱을 출력하면 환경 설정이 완료된 것이다.</p>
                    {hp02_test_run}
                    {square_test}
                    """,
                },
                {
                    "heading": "Base64가 필요한 이유",
                    "body": f"""
                    <p>Base64는 CTF나 프로그래밍에서 자주 마주치는 인코딩이다. 흔히 끝에 <code>=</code> 문자가 있으면 Base64일 가능성이 있다고 말하지만, 강의에서는 이것을 농담 섞인 첫 힌트로 소개하고 실제 원리를 설명한다.</p>
                    <p>컴퓨터의 한 바이트는 <code>0x00</code>부터 <code>0xFF</code>까지 256가지 값을 가질 수 있다. 하지만 사람이 화면에 그대로 출력해서 복사·붙여넣기할 수 있는 ASCII 문자는 훨씬 적다. 모든 바이트 값을 안전하게 문자 형태로 표현하려면 출력 가능한 문자 집합으로 바꾸는 방식이 필요하다.</p>
                    {hp02_base64}
                    <p>16진수로 표현하면 한 바이트를 <code>00</code>, <code>01</code>, <code>FF</code>처럼 두 글자로 나타낼 수 있지만, 한 바이트를 표현하는 데 두 바이트가 필요해 약 두 배의 공간을 쓴다. Base64는 대문자 26개, 소문자 26개, 숫자 10개, <code>+</code>, <code>/</code>를 합쳐 총 64개의 문자로 데이터를 표현한다. 64는 2의 6제곱이므로 6비트마다 한 글자로 바꿀 수 있고, 이 방식은 16진수보다 공간 낭비가 적다.</p>
                    <table>
                      <thead><tr><th>표현 방식</th><th>특징</th></tr></thead>
                      <tbody>
                        <tr><td>원본 바이트</td><td>모든 값이 화면에 안전하게 출력되지 않는다.</td></tr>
                        <tr><td>16진수</td><td>한 바이트를 두 글자로 표현하므로 이해는 쉽지만 길이가 커진다.</td></tr>
                        <tr><td>Base64</td><td>64개 문자로 6비트 단위 표현을 하며, 끝자리가 맞지 않을 때 <code>=</code> 패딩을 붙인다.</td></tr>
                      </tbody>
                    </table>
                    <p>한글, 일본어, 중국어 같은 문자는 Unicode, UTF, CP949 등 별도 문자 인코딩과 관련된 문제다. Base64는 그런 문자 자체를 정의하는 규칙이 아니라, 이미 존재하는 바이트열을 출력 가능한 문자로 바꾸는 범용 표현 방식으로 이해해야 한다.</p>
                    """,
                },
                {
                    "heading": "CyberChef로 먼저 확인하기",
                    "body": f"""
                    <p>CyberChef는 영국 정보기관 GCHQ가 공개한 오픈소스 분석 도구다. 강의에서는 “사이버 스위스 아미 나이프”처럼 다양한 변환과 분석을 한 화면에서 조합할 수 있는 도구로 소개한다. Base64 인코딩·디코딩, Hex 변환, AES·DES 같은 암호화, 해시, HTTP 요청, 문자열 처리 등 많은 기능을 레시피처럼 끌어다 쓸 수 있다.</p>
                    {hp02_cyberchef}
                    <p>CyberChef의 기본 사용 흐름은 왼쪽의 연산 목록에서 필요한 작업을 가운데 레시피 영역으로 끌어오고, 오른쪽 위 입력 창에 데이터를 넣은 뒤, 오른쪽 아래 출력 결과를 확인하는 방식이다. 강의에서는 문자열을 Base64로 바꾸고 다시 디코딩하는 작업, Hex 변환, AES 암호화 예시까지 가볍게 보여 준다. AES는 키와 IV 길이가 맞아야 오류가 사라진다는 점도 함께 확인한다.</p>
                    """,
                },
                {
                    "heading": "Base64 문자열 1만 개에서 필요한 값 찾기",
                    "body": f"""
                    <p>실습 파일에는 Base64로 인코딩된 문자열이 한 줄에 하나씩 약 1만 개 들어 있고, 그중 하나만 <code>WHS</code>로 시작하는 값을 디코딩 결과로 갖는다. CyberChef에 한 줄씩 붙여 넣어 확인할 수도 있지만, 1만 줄을 수작업으로 검사하는 것은 비효율적이다. 그래서 Python으로 파일을 읽고, 각 줄을 Base64 디코딩한 뒤 조건을 검사한다.</p>
                    <p>먼저 <code>open()</code>과 <code>readlines()</code>로 파일의 각 줄을 읽는다. 단순히 출력하면 보기 불편하므로 <code>pprint</code>로 정돈된 출력도 확인한다. Python에는 <code>base64</code> 패키지가 기본 제공되며, <code>base64.b64decode()</code>로 디코딩할 수 있다.</p>
                    <p>디코딩 결과 앞에 <code>b</code>가 붙어 보이면 그것은 문자열이 아니라 <code>bytes</code> 타입이라는 뜻이다. 바이트는 일반 문자뿐 아니라 널 바이트, 공백 문자, 출력되지 않는 데이터까지 포함하는 자료형이다. 사람이 읽는 문자열로 다루려면 <code>.decode()</code>를 호출해 <code>str</code> 타입으로 바꾼다. 마지막으로 <code>startswith("WHS")</code> 조건을 걸어 원하는 값만 출력한다.</p>
                    {hp02_decoder_code}
                    {base64_decoder}
                    """,
                },
            ],
            "checks": [
                "Python 설치 시 PATH 설정을 켜야 하는 이유를 설명할 수 있는가?",
                "Code Runner의 Run In Terminal 설정이 input() 실습에 왜 필요한지 이해했는가?",
                "Base64가 64개 문자와 6비트 단위 표현을 사용하는 이유를 말할 수 있는가?",
                "bytes와 str의 차이, 그리고 decode()가 필요한 이유를 설명할 수 있는가?",
                "1만 줄 파일에서 WHS로 시작하는 디코딩 결과만 찾는 코드를 작성할 수 있는가?",
            ],
        },
        {
            "id": "1-3",
            "title": "HTTP와 웹 스크래핑",
            "subtitle": "HTTP 요청·응답, HTML 구조, 개발자 도구, requests 패키지를 이해하고 게시판 탐색을 자동화한다.",
            "tags": ["HTTP", "HTML", "requests"],
            "objectives": [
                "HTTP가 클라이언트와 서버 사이의 요청·응답 규칙임을 이해한다.",
                "요청 메소드, 응답 상태 코드, 헤더와 바디의 역할을 구분한다.",
                "HTML, CSS, JavaScript가 웹페이지에서 맡는 역할을 설명한다.",
                "Python requests로 1번부터 100번까지의 노트를 자동 요청하고 조건에 맞는 페이지를 찾는다.",
            ],
            "sections": [
                {
                    "heading": "HTTP 요청과 응답",
                    "body": f"""
                    <p>HTTP는 Hypertext Transfer Protocol의 약자이며, 웹브라우저와 웹서버가 데이터를 주고받기 위한 규칙이다. 웹브라우저는 클라이언트로서 요청을 보내고, 서버는 그 요청에 대한 응답을 돌려준다. 이 구조를 request와 response 방식이라고 이해하면 된다.</p>
                    {hp03_http}
                    <p>요청과 응답은 모두 헤더와 바디로 구성된다. 요청에는 <code>GET</code>, <code>POST</code>, <code>PUT</code>, <code>DELETE</code> 같은 메소드가 있고, 응답에는 <code>200</code>, <code>300</code>, <code>400</code>, <code>500</code> 계열 상태 코드가 있다. 강의에서는 특히 요청 쪽에서는 GET과 POST, 응답 쪽에서는 정상 응답인 200과 클라이언트 오류 계열인 400번대를 우선 보면 된다고 설명한다.</p>
                    <table>
                      <thead><tr><th>구분</th><th>강의에서 보는 핵심</th></tr></thead>
                      <tbody>
                        <tr><td>GET</td><td>URL과 쿼리 문자열에 필요한 인자를 붙여 서버에 데이터를 요청한다.</td></tr>
                        <tr><td>POST</td><td>요청 바디에 데이터를 담아 서버에 보낸다. 폼 데이터나 JSON을 보낼 수 있다.</td></tr>
                        <tr><td>200</td><td>요청이 정상 처리되었음을 의미한다.</td></tr>
                        <tr><td>400 계열</td><td>잘못된 요청, 권한 문제, 존재하지 않는 페이지처럼 클라이언트 쪽 문제가 있음을 나타낸다.</td></tr>
                      </tbody>
                    </table>
                    """,
                },
                {
                    "heading": "예시 요청과 실제 웹사이트 헤더",
                    "body": f"""
                    <p>예를 들어 브라우저가 <code>www.example.com</code>의 <code>index.html</code>을 요청한다면, 요청에는 HTTP 버전, User-Agent, Accept-Encoding 같은 정보가 들어간다. 서버는 HTTP 1.1 200 OK 같은 상태 줄과 함께 Content-Type, 문자 인코딩, Content-Length 같은 정보를 돌려주고, 바디에는 실제 HTML이 들어간다.</p>
                    {hp03_real_request}
                    <p>강의에서는 화이트햇 스쿨 홈페이지에 직접 요청을 보내 본 결과도 보여 준다. 실제 요청은 예시보다 훨씬 많은 헤더를 포함한다. 쿠키, 세션, Accept-Encoding, <code>Sec-</code>로 시작하는 브라우저 보안 관련 헤더들이 붙는다. 응답 역시 HTML을 제외해도 많은 헤더를 포함하며, <code>X-Frame-Options</code>, <code>X-XSS-Protection</code> 같은 보안 관련 헤더가 보인다. 핵심 구조는 예시와 같지만 실제 웹은 상태 유지와 보안을 위해 더 많은 정보를 주고받는다.</p>
                    """,
                },
                {
                    "heading": "HTML, CSS, JavaScript",
                    "body": f"""
                    <p>HTTP로 받아오는 바디에는 대개 HTML 코드가 들어 있다. HTML은 Hypertext Markup Language의 약자이며, 웹페이지를 구조화하고 콘텐츠를 표시하는 표준 마크업 언어다. 여는 태그와 닫는 태그가 있고, <code>head</code>, <code>body</code>, <code>p</code>, <code>a</code>, <code>div</code> 같은 태그가 계층적으로 중첩된다.</p>
                    {hp03_html_source}
                    <p>웹페이지는 HTML만으로 완성되지 않는다. HTML은 구조를 담당하고, CSS는 글자 모양·색상·레이아웃 같은 꾸밈을 담당하며, JavaScript는 버튼 클릭, 광고 배너, 동적 표시처럼 기능적 동작을 담당한다. 그래서 웹 스크래핑을 하려면 화면에 보이는 결과뿐 아니라 그 화면을 만든 HTML 구조를 볼 수 있어야 한다.</p>
                    """,
                },
                {
                    "heading": "소스 보기와 개발자 도구",
                    "body": """
                    <p>브라우저에서 마우스 오른쪽 클릭 후 페이지 소스 보기를 누르면 HTML 코드를 볼 수 있다. 처음 보면 복잡해 보이지만, 태그들이 계층을 이루고 있고 화면에 보이는 요소들이 어떤 HTML 구조에 대응하는지 추적할 수 있다.</p>
                    <p>특정 글자나 버튼이 HTML 코드 어디에 있는지 찾기 어려울 때는 Chrome 개발자 도구를 사용한다. <code>F12</code>, <code>Ctrl + Shift + I</code>, 또는 마우스 오른쪽 클릭 후 검사를 누르면 왼쪽 화면과 오른쪽 HTML 요소가 1대1로 대응된다. 코드 일부를 바꾸면 왼쪽 화면이 어떻게 바뀌는지도 바로 확인할 수 있다. 이 과정은 나중에 BeautifulSoup으로 특정 태그를 선택할 때 기준을 잡는 데도 중요하다.</p>
                    """,
                },
                {
                    "heading": "requests 패키지와 GET/POST",
                    "body": f"""
                    <p>Python의 requests 패키지는 HTTP 요청을 쉽게 보내고 응답을 객체로 받아오게 해 준다. 설치는 터미널에서 <code>pip install requests</code>로 할 수 있다. 이후 프로젝트가 커지면 virtualenv나 Poetry 같은 가상 환경 도구로 라이브러리 버전을 관리하는 것이 좋다.</p>
                    {hp03_requests}
                    <p>GET 요청에서는 URL 뒤의 쿼리 문자열에 들어갈 인자를 <code>params</code> 딕셔너리로 넘긴다. POST 요청에서는 본문에 들어갈 데이터를 <code>data</code> 또는 <code>json</code> 인자로 넘긴다. 폼 전송처럼 <code>a=b&c=d</code> 형태로 보내는 경우는 <code>data</code>, JSON 객체를 보내는 경우는 <code>json</code>을 사용한다.</p>
                    """,
                },
                {
                    "heading": "1번부터 100번까지 자동으로 찾기",
                    "body": f"""
                    <p>실습 사이트에는 1번부터 100번까지의 노트가 있고, 그중 한 페이지에만 <code>WHS</code> 문자열이 포함되어 있다. 수동으로 100번 클릭하는 대신 URL의 숫자 부분이 규칙적이라는 점을 이용해 반복 요청을 보낸다.</p>
                    <p>처음 <code>requests.get()</code> 결과를 그대로 출력하면 <code>&lt;Response [200]&gt;</code>처럼 상태만 보인다. 실제 HTML을 보려면 <code>response.text</code>나 <code>response.content.decode()</code>를 사용한다. 한글이 깨지는 경우에는 바이트로 받은 뒤 적절히 디코딩하면 된다.</p>
                    <p>반복문으로 1부터 100까지 URL을 만들고, 응답 본문 안에 <code>WHS</code>가 있을 때만 출력한다. 강의에서는 73번 노트에서 <code>congratulations the flag is WHS simple web scraping</code>이라는 결과를 찾는 흐름을 보여 준다. 반복 진행 상황을 보기 위해 <code>tqdm</code>으로 루프를 감싸는 방법도 소개한다.</p>
                    {hp03_final_code}
                    {request_note_search}
                    """,
                },
            ],
            "checks": [
                "HTTP 요청과 응답이 각각 헤더와 바디를 가진다는 점을 설명할 수 있는가?",
                "GET과 POST의 차이를 params, data, json 인자와 연결해 말할 수 있는가?",
                "HTML, CSS, JavaScript의 역할을 구분할 수 있는가?",
                "requests 응답에서 상태 코드와 페이지 내용을 구분해 확인할 수 있는가?",
                "반복 요청과 조건문으로 100개 노트 중 원하는 페이지를 찾을 수 있는가?",
            ],
        },
        {
            "id": "1-4",
            "title": "웹 API와 키 관리",
            "subtitle": "웹 API가 브라우저 화면보다 자동화에 적합한 이유를 이해하고, API 키 유출 위험과 관리 방법을 정리한다.",
            "tags": ["API", "JSON", "키 관리"],
            "objectives": [
                "API를 서로 다른 소프트웨어가 약속된 방식으로 통신하는 인터페이스로 설명한다.",
                "웹 API가 HTTP와 JSON을 통해 깔끔한 데이터를 제공하는 장점을 이해한다.",
                "검색, CTI, 메신저, AI, 클라우드 API의 활용 범위를 구분한다.",
                "API 키를 하드코딩하거나 공개 저장소·AI 대화에 노출했을 때의 위험을 설명한다.",
            ],
            "sections": [
                {
                    "heading": "API의 의미",
                    "body": f"""
                    <p>API는 Application Programming Interface의 약자다. 서로 다른 소프트웨어 애플리케이션이 상호작용하기 위해 정해 둔 인터페이스다. “이 요청을 이런 형식으로 보내면 이런 데이터를 돌려주겠다”는 약속이라고 이해하면 된다.</p>
                    {hp04_api_definition}
                    <p>API에는 운영체제의 POSIX API, 데이터베이스 API, 모바일 SDK API, 웹서비스 업체가 제공하는 자체 API 등 여러 종류가 있다. 이 강의에서는 HTTP 또는 HTTPS로 요청과 응답을 주고받는 웹 API에 집중한다. 클라이언트가 HTTP 프로토콜로 요청을 보내면 서버는 사전에 정한 형식에 따라 데이터를 처리하고 반환한다.</p>
                    """,
                },
                {
                    "heading": "브라우저 검색과 API 검색의 차이",
                    "body": f"""
                    <p>강의는 네이버 뉴스를 웹브라우저로 검색했을 때와 검색 API로 호출했을 때를 비교한다. 브라우저 검색 요청에는 사용자가 직접 신경 쓰기 어려운 많은 인자와 헤더가 붙고, 응답에는 검색 결과뿐 아니라 CSS, JavaScript, 버튼, 레이아웃, 광고 등 화면을 꾸미기 위한 요소가 많이 섞인다. 자동화하려면 이 복잡한 HTML에서 필요한 데이터만 다시 파싱해야 한다.</p>
                    {hp04_api_response}
                    <p>반면 검색 API는 내가 어떤 인자로 검색하는지 명확하고, 응답도 대개 JSON처럼 프로그램이 바로 읽기 좋은 형태로 온다. 검색 결과의 제목, 링크, 요약, 작성 시각 같은 값이 구조화되어 있기 때문에 코드가 간결하고 로직이 분명해진다.</p>
                    <table>
                      <thead><tr><th>방식</th><th>특징</th><th>자동화 관점</th></tr></thead>
                      <tbody>
                        <tr><td>브라우저 화면</td><td>사람이 보기 좋게 디자인된 HTML, CSS, JavaScript가 함께 온다.</td><td>필요한 값을 따로 찾아 파싱해야 한다.</td></tr>
                        <tr><td>웹 API</td><td>정해진 요청 인자와 JSON 같은 구조화된 응답을 제공한다.</td><td>프로그램이 바로 처리하기 쉽다.</td></tr>
                      </tbody>
                    </table>
                    """,
                },
                {
                    "heading": "API 제공 분야",
                    "body": f"""
                    <p>API는 여러 서비스에서 제공된다. 일반 포털은 검색, 캘린더, 문서, AI 기능을 API로 제공할 수 있고, 보안 분야에서는 CTI 관련 API가 중요하다. Criminal IP, Shodan, VirusTotal 같은 서비스는 IP 위협 점수, 취약점 정보, 악성코드 관련 정보, 다른 회원사에서 관찰된 활동 같은 보안 데이터를 제공한다. 무료 버전과 유료 버전이 나뉘며, 유료 버전이 더 많은 기능과 한도를 제공하는 경우가 많다.</p>
                    {hp04_naver_api}
                    <p>메신저 API도 있다. Telegram, Slack, Discord 같은 서비스는 봇을 만들어 메시지를 보내거나 특정 명령에 반응하게 하는 기능을 제공한다. AI API는 ChatGPT나 Claude 같은 모델에 프롬프트를 보내고 결과만 받아와 자체 서비스에 붙이는 데 쓰인다. 클라우드 API는 AWS, Azure, GCP 같은 클라우드 자원을 콘솔 클릭 없이 코드로 관리하기 위해 사용되며, 이때는 API 키보다 액세스 키라는 표현을 많이 쓴다.</p>
                    <table>
                      <thead><tr><th>분야</th><th>예시</th><th>할 수 있는 일</th></tr></thead>
                      <tbody>
                        <tr><td>포털·일반 서비스</td><td>검색, 캘린더, 시트, 클로바</td><td>검색 결과 수집, 일정·문서 자동화</td></tr>
                        <tr><td>사이버보안 CTI</td><td>Criminal IP, Shodan, VirusTotal</td><td>IP 평판, 취약점, 악성 여부 확인</td></tr>
                        <tr><td>메신저</td><td>Telegram, Slack, Discord</td><td>봇 응답, 채널 알림, 명령 자동화</td></tr>
                        <tr><td>AI</td><td>ChatGPT, Claude</td><td>프롬프트 처리 결과를 자체 코드에서 활용</td></tr>
                        <tr><td>클라우드</td><td>AWS, Azure, GCP</td><td>리소스 생성, 권한 관리, 운영 자동화</td></tr>
                      </tbody>
                    </table>
                    """,
                },
                {
                    "heading": "API 키 유출 사고",
                    "body": f"""
                    <p>API를 사용하는 쪽에서 가장 조심해야 할 것은 키 관리다. 공개되는 소스 코드나 설정 파일에 API 키를 그대로 넣어 GitHub에 올리면, 다른 사람이 그 키를 가져가 비용이 발생하는 API를 마음대로 사용할 수 있다. 데이터베이스 접속 정보나 AWS 액세스 키가 노출되면 더 큰 침해로 이어질 수 있다.</p>
                    {hp04_key_leak}
                    <p>한 번 공개된 키는 여러 곳으로 퍼질 수 있다. 공개 저장소, 블로그 글, 설정 파일, 이후 수집된 LLM 학습 데이터셋까지 흘러갈 수 있다. 또 최근에는 오류가 난 코드를 그대로 AI 대화창에 붙여 넣는 경우가 많다. 그 코드 안에 비밀키, 로그, 설정값이 포함되어 있으면 AI 서비스 자체가 침해되거나 대화 내용이 노출될 때 함께 새어 나갈 수 있다.</p>
                    """,
                },
                {
                    "heading": "키 관리 원칙과 실습 방향",
                    "body": f"""
                    <p>가장 기본 원칙은 API 키를 소스 코드에 하드코딩하지 않는 것이다. 별도 설정 파일이나 환경 변수로 분리하고, 그 파일은 공개 저장소나 클라우드 공유 폴더에 올리지 않는다. 사용량 기반으로 비용이 청구되는 API라면 정기적으로 사용량을 확인해 내가 쓰지 않은 호출이 있는지 살펴야 한다.</p>
                    {hp04_rules}
                    <p>유출이 의심되거나 사용 이력이 이상하면 키를 즉시 만료하고 새로 발급한다. 비밀번호가 유출되면 바꾸는 것과 같은 대응이다. 강의에서는 별도 문제를 제공하지 않지만, 네이버 검색 API는 네이버 계정으로 무료 발급이 가능하고 한도도 비교적 넉넉하므로, 키워드를 입력받아 블로그나 뉴스 글을 검색하는 Python 스크립트를 작성해 보라고 안내한다.</p>
                    {api_key_example}
                    """,
                },
            ],
            "checks": [
                "웹 API가 브라우저 화면보다 자동화에 적합한 이유를 JSON 응답과 연결해 설명할 수 있는가?",
                "CTI API와 메신저 봇 API, AI API, 클라우드 API의 차이를 말할 수 있는가?",
                "API 키를 GitHub나 AI 대화창에 넣으면 어떤 위험이 생기는지 이해했는가?",
                "환경 변수나 별도 설정 파일로 키를 분리하고, 이상 사용 시 키를 폐기해야 하는 이유를 설명할 수 있는가?",
            ],
        },
        {
            "id": "1-5",
            "title": "n8n 워크플로우 자동화",
            "subtitle": "노드 기반 자동화 도구 n8n으로 서비스 연동, 트리거, 데이터 흐름, 액션, 디버깅을 이해한다.",
            "tags": ["n8n", "워크플로우", "자동화"],
            "objectives": [
                "n8n이 오픈소스 워크플로우 자동화 도구이며 노드 그래프로 작업 흐름을 구성한다는 점을 이해한다.",
                "클라우드 체험판과 Docker 기반 로컬 구축의 차이를 구분한다.",
                "트리거 노드, 데이터·흐름 관리 노드, 액션 노드, 노트 기능의 역할을 설명한다.",
                "네이버 검색 API와 스케줄링을 결합한 보안 뉴스 자동 정리 워크플로우를 설계할 수 있다.",
            ],
            "sections": [
                {
                    "heading": "n8n의 역할",
                    "body": f"""
                    <p>n8n은 오픈소스 워크플로우 자동화 도구다. 코드를 직접 많이 작성하지 않아도 그래프 형태로 주요 작업 흐름을 시각적으로 구성할 수 있다. IT 인프라 작업, DevSecOps 업무 자동화, 개인 일정·다이어리 자동화, 소규모 비즈니스 운영까지 폭넓게 활용할 수 있다.</p>
                    {hp05_features}
                    <p>가장 큰 특징은 드래그 앤 드롭 기반으로 노드를 연결하는 직관적인 UI다. Telegram, Discord, Slack 같은 메신저, MySQL과 PostgreSQL 같은 데이터베이스, Gmail, Google Docs, AWS, Azure 같은 클라우드 서비스까지 매우 많은 애플리케이션과 연동할 수 있다.</p>
                    """,
                },
                {
                    "heading": "활용 예시",
                    "body": f"""
                    <table>
                      <thead><tr><th>상황</th><th>자동화 흐름</th></tr></thead>
                      <tbody>
                        <tr><td>소규모 쇼핑몰 메일 확인</td><td>들어온 메일을 검사하고 피싱으로 의심되면 Slack으로 알림을 보낸다.</td></tr>
                        <tr><td>업무 데이터 동기화</td><td>PostgreSQL에 저장된 정보를 Google Sheets에도 업데이트하고, 특별한 정보가 있으면 Slack 알림을 보낸다.</td></tr>
                        <tr><td>보안 로그 감시</td><td>서버 로그인 로그를 실시간으로 받고, 처음 보는 IP를 VirusTotal에 조회한 뒤 악성·의심 결과가 나오면 Slack과 Gmail로 알린다.</td></tr>
                      </tbody>
                    </table>
                    {hp05_examples}
                    <p>강의는 n8n을 지금까지 배운 HTTP 요청, API, 데이터 처리 흐름을 24시간 동작하는 자동화로 이어 주는 도구로 소개한다.</p>
                    """,
                },
                {
                    "heading": "설치와 사용 방식",
                    "body": f"""
                    <p>n8n을 사용하는 방법은 크게 두 가지다. 첫 번째는 공식 사이트에서 계정을 만들고 서비스가 제공하는 환경을 사용하는 것이다. 별도 설치가 필요하지 않고, 이메일 가입 시 약 14일 무료 체험을 제공하므로 먼저 기능을 알아보기 좋다.</p>
                    {hp05_docker}
                    <p>두 번째는 Docker 이미지로 로컬에 구축하는 방식이다. n8n은 오픈소스 도구이고 공식 Docker 이미지를 제공한다. Docker Desktop 같은 도구로 이미지를 내려받아 내 PC 안에 n8n 서버를 띄우면, 서버가 돌아가는 동안 별도 유료 회원 제한 없이 기능을 사용할 수 있다. 개인이 가볍게 써 볼 때는 공식 서비스가 편하고, 본격적으로 운영해 보고 싶다면 Docker 기반 로컬 구축이 적합하다.</p>
                    """,
                },
                {
                    "heading": "노드 종류와 흐름",
                    "body": f"""
                    <p>n8n의 핵심은 노드들을 그래프로 연결하는 것이다. 트리거 노드에서 흐름이 시작되고, 데이터는 웹 요청, 중복 제거, 코드 실행, Google Sheets, Slack 같은 노드를 지나며 변환되고 전달된다.</p>
                    {hp05_workflow}
                    <table>
                      <thead><tr><th>노드 또는 기능</th><th>역할</th><th>예시</th></tr></thead>
                      <tbody>
                        <tr><td>트리거 노드</td><td>작업 흐름이 언제 시작될지 정한다.</td><td>수동 실행, 5분마다 실행, 매일 아침 실행, Webhook, GitHub push, GitLab merge</td></tr>
                        <tr><td>데이터·흐름 관리 노드</td><td>데이터 필드 변환, 새 값 설정, 조건 분기, 루프, 필터링, 중복 제거를 처리한다.</td><td>IF, Set, Item Lists, Code</td></tr>
                        <tr><td>액션 노드</td><td>외부 애플리케이션과 연동해 실제 작업을 수행한다.</td><td>GitHub 코멘트 작성, DB 쿼리, Discord 메시지 전송</td></tr>
                        <tr><td>인증 정보</td><td>API 키, credential, access key를 안전하게 연결한다.</td><td>GitHub, Google, Slack, 클라우드 계정 연동</td></tr>
                        <tr><td>노트</td><td>그래프 위에 설명을 붙여 작업 흐름의 가시성을 높인다.</td><td>마크다운으로 특정 영역의 목적과 사용법 기록</td></tr>
                      </tbody>
                    </table>
                    """,
                },
                {
                    "heading": "디버깅과 네이버 검색 API 예시",
                    "body": f"""
                    <p>n8n에서 각 노드를 클릭하면 그 노드를 거치기 전과 후의 데이터가 표시된다. 어떤 입력이 들어왔고, 노드가 어떤 출력을 만들었는지 볼 수 있으므로 디버깅이 쉬워진다.</p>
                    {hp05_debug}
                    <p>강의에서는 네이버 검색 API를 쓰는 노드를 예로 든다. 왼쪽 입력에는 <code>해킹</code> 같은 키워드가 들어오고, HTTP Request 노드는 네이버 검색 API를 호출한다. 결과는 오른쪽 출력에서 JSON 형태로 깔끔하게 정리되어 다음 노드로 넘어간다. 이전 강의에서 Python으로 한 번 검색을 실행했다면, n8n에서는 그 실행을 스케줄링하고 다른 서비스와 연결할 수 있다.</p>
                    {n8n_flow}
                    <p>강의에서는 모든 수강생이 n8n 환경을 개별 구축하기 어려울 수 있어 별도 필수 실습으로 두지는 않는다. 대신 관심이 있다면 네이버 검색 API 키를 이용해 매일 아침 보안, 사이버, 해킹 키워드로 뉴스를 검색하고 그 결과를 Google Sheets에 자동 정리하는 워크플로우를 만들어 보라고 권한다.</p>
                    """,
                },
            ],
            "checks": [
                "n8n이 코드 중심 도구가 아니라 노드 기반 워크플로우 도구라는 점을 설명할 수 있는가?",
                "공식 서비스 사용과 Docker 로컬 구축의 장단점을 구분할 수 있는가?",
                "트리거 노드, 데이터·흐름 관리 노드, 액션 노드의 차이를 말할 수 있는가?",
                "네이버 검색 API 결과를 Google Sheets와 Slack으로 이어 주는 흐름을 설계할 수 있는가?",
            ],
        },
        {
            "id": "1-6",
            "title": "개인정보 유출과 데이터 결합",
            "subtitle": "개인정보가 유출되는 형태, 다크웹 유통, 모자이크 이론, 조인과 Faker 기반 가상 데이터 결합을 정리한다.",
            "tags": ["개인정보", "데이터 결합", "Faker"],
            "objectives": [
                "개인정보를 개인을 특정할 수 있거나 개인과 관련된 민감한 정보로 이해한다.",
                "유출 정보가 다크웹·포럼에서 어떤 형태로 유통되는지 설명한다.",
                "모자이크 이론과 데이터 결합이 왜 개인정보 위험을 키우는지 이해한다.",
                "inner, left, right, outer join과 고유 식별자 판단의 중요성을 구분한다.",
                "가상 개인정보 파일을 Python으로 결합할 때 어떤 값이 키가 될 수 있는지 판단한다.",
            ],
            "sections": [
                {
                    "heading": "개인정보의 범위",
                    "body": """
                    <p>강의는 개인정보를 법적 정의에서 출발해 설명한다. 개인정보는 개인을 특정할 수 있는 정보를 뜻한다. 주민등록번호는 개인을 강하게 특정할 수 있고, 이메일도 특정 가능성이 높다. 이름은 동명이인이 있을 수 있어 단독으로는 애매할 수 있으며, IP 주소로 사람을 특정할 수 있는지도 상황에 따라 어려운 문제다.</p>
                    <p>강의의 목적은 법률 해석이 아니므로, 이름, 생년월일, 집주소, 비밀번호, 카드번호처럼 나와 관련되어 있고 민감할 수 있는 정보를 넓게 개인정보로 보고 다룬다. 아이디와 비밀번호도 법적으로 항상 같은 방식으로 분류되는 것은 아니지만, 사용자 입장에서는 비밀번호 유출을 개인정보 침해로 받아들이는 경우가 많으므로 포함해서 생각한다.</p>
                    """,
                },
                {
                    "heading": "개인정보 유출 원인과 사례",
                    "body": f"""
                    <p>개인정보 유출 원인은 다양하다. 해킹으로 데이터베이스가 털릴 수도 있고, 내부자가 유출할 수도 있으며, 누군가 의도하지 않았지만 파일을 잘못 업로드하는 업무상 과실로 새어 나갈 수도 있다. 중소규모 웹사이트, 신뢰하기 어려운 해외 쇼핑몰, 브라우저 확장 기능 취약점 등도 유출 경로가 될 수 있다.</p>
                    {hp06_leak_causes}
                    <p>강의에서는 홈쇼핑이나 작은 사이트에서도 한 번 사고가 나면 수십만 명, 백만 명 단위의 개인정보가 유출될 수 있다고 설명한다. 또 2024년 KISA 보도자료 사례로 자동 로그인 기능을 활용한 로그인 정보 탈취를 언급한다. 브라우저의 비밀번호 자동완성 기능에 문제가 있으면 사용자가 저장해 둔 여러 사이트의 아이디와 비밀번호가 함께 노출될 수 있다.</p>
                    """,
                },
                {
                    "heading": "유출 데이터의 유통 형태",
                    "body": f"""
                    <p>유출된 개인정보는 다크웹이나 해킹 포럼에서 공유·판매될 수 있다. 강의에서는 BreachForums 같은 온라인 포럼을 예로 들며, 해커들이 개인정보 유출 데이터나 침해 접근 권한을 거래하는 공간이라고 설명한다. 이 사이트는 미국 FBI와 사법부의 조치로 폐쇄된 적이 있지만 다시 살아나는 등 차단과 재등장이 반복되는 특징이 있다.</p>
                    {hp06_breachforums}
                    <p>실제 유통되는 데이터 형태도 다양하다. 아이디와 패스워드가 콜론으로 구분된 텍스트 파일, 이름·주소·전화번호·SSN이 들어간 CSV 파일, 데이터베이스 전체를 가져온 SQL 덤프 파일 등이 있다. 중요한 점은 하나의 파일만으로도 위험하지만, 여러 파일이 결합되면 훨씬 더 심각한 정보가 될 수 있다는 것이다.</p>
                    <table>
                      <thead><tr><th>형태</th><th>포함될 수 있는 정보</th></tr></thead>
                      <tbody>
                        <tr><td>텍스트 파일</td><td><code>id:password</code>처럼 로그인 정보가 한 줄씩 나열될 수 있다.</td></tr>
                        <tr><td>CSV 파일</td><td>이름, 주소, 전화번호, 주민등록번호 또는 SSN 같은 항목이 표 형태로 정리될 수 있다.</td></tr>
                        <tr><td>SQL 덤프</td><td>서비스 데이터베이스의 테이블 구조와 데이터가 통째로 포함될 수 있다.</td></tr>
                      </tbody>
                    </table>
                    """,
                },
                {
                    "heading": "모자이크 이론",
                    "body": f"""
                    <p>모자이크 이론은 단편적인 개별 정보는 별로 중요해 보이지 않아도, 여러 조각을 결합하면 이전에는 몰랐던 핵심 사실을 알 수 있다는 주장이다. 원래 정보기관 쪽에서 많이 언급되던 이론이지만, 개인정보와 OSINT에서도 매우 중요하다.</p>
                    {hp06_mosaic}
                    <p>예를 들어 김민철이라는 사람이 <code>nyan101</code>이라는 아이디를 쓴다는 정보는 그 자체로 큰 비밀이 아닐 수 있다. 그 아이디가 Gmail 주소와 연결되어 있고, 그 메일로 어떤 사이트에 가입했으며, 그 사이트의 게시글에서 어느 도시에 산다는 단서가 나오고, 또 직장 동료라고 소개한 사람이 어떤 회사에 다니는지 공개되어 있다면 상황이 달라진다. 조각들을 합치면 특정 사람이 어디에 살고, 어떤 회사와 관련 있고, 어떤 이메일을 쓰는지까지 추정할 수 있다.</p>
                    <p>이처럼 데이터 결합은 모자이크를 채워 큰 그림을 완성하는 과정과 같다. 그래서 개별 정보 하나하나는 사소해 보여도, 공개 범위와 결합 가능성을 함께 고려해야 한다.</p>
                    """,
                },
                {
                    "heading": "조인 방식",
                    "body": f"""
                    <p>서로 다른 데이터 집합에 공통된 값이 있으면 그 값을 기준으로 하나의 큰 데이터로 합칠 수 있다. SQL에서는 이를 join이라고 한다. 목적에 따라 inner join, left join, right join, outer join을 선택한다.</p>
                    {hp06_join}
                    <table>
                      <thead><tr><th>방식</th><th>의미</th><th>강의 예시</th></tr></thead>
                      <tbody>
                        <tr><td>inner join</td><td>양쪽 모두에 존재하는 데이터만 남긴다.</td><td>이름·이메일 표와 이메일·전화번호 표에서 공통 이메일이 있는 사람만 이름, 이메일, 연락처를 가진다.</td></tr>
                        <tr><td>left join</td><td>왼쪽 표를 기준으로 남기고, 오른쪽 정보가 없으면 빈 값으로 둔다.</td><td>이름과 이메일 정보가 더 중요하면 연락처가 없어도 사람을 남긴다.</td></tr>
                        <tr><td>right join</td><td>오른쪽 표를 기준으로 남긴다.</td><td>이메일과 연락처 정보가 더 중요하면 이름이 없어도 남긴다.</td></tr>
                        <tr><td>outer join</td><td>양쪽 중 어느 한쪽에만 있어도 모두 남긴다.</td><td>조금 난잡하더라도 어느 정보도 버리지 않고 전체 후보를 유지한다.</td></tr>
                      </tbody>
                    </table>
                    <p>분석 목적에 따라 어떤 정보를 버릴 수 있는지, 어떤 정보를 반드시 보존해야 하는지를 먼저 정해야 한다. 무조건 많이 합치는 것이 좋은 것이 아니라, 데이터의 의미와 고유성을 이해해야 한다.</p>
                    """,
                },
                {
                    "heading": "Faker와 가상 개인정보",
                    "body": f"""
                    <p>개인정보 실습에서 실제 사람의 정보를 사용하면 윤리적·법적 문제가 생긴다. 그래서 강의에서는 Python 패키지 Faker를 소개한다. Faker는 실제 존재하지 않는 이름, 직업, 이메일, 주소, 연락처, 주민등록번호 형식의 값 등을 만들어 낼 수 있다.</p>
                    {hp06_faker}
                    <p>Faker는 한국어 로케일도 지원한다. 같은 코드에 <code>ko_KR</code>을 지정하면 외국 이름과 주소 대신 한국식 이름, 직업, 주소, 주민등록번호 형식의 값이 생성된다. 강의 실습 데이터는 이런 방식으로 100명 정도의 가상 개인정보를 만든 뒤, 이름-이메일, 이메일-주소, 이메일-연락처처럼 여러 파일로 흩어 둔 형태다.</p>
                    """,
                },
                {
                    "heading": "실습: 파일 여러 개를 하나로 묶기",
                    "body": f"""
                    <p>실습 목표는 흩어진 가상 개인정보 파일을 하나의 테이블로 결합하는 것이다. 압축 파일을 풀면 이메일-주소, 주소-직업, 이메일-직업, 이메일-전화번호 같은 여러 CSV 파일이 나온다. 각 줄은 쉼표로 구분되며, 강의에서는 주소나 직장 이름 안에 쉼표가 들어가지 않도록 처리되어 있다고 가정한다.</p>
                    {hp06_merge_code}
                    <p>Python에서는 파일을 읽은 뒤 <code>line.strip()</code>으로 양끝 공백과 줄바꿈을 제거하고, <code>split(",")</code>로 두 항목을 나눈다. 여기서 중요한 것은 어떤 값이 사람을 구분하는 키가 될 수 있는지 판단하는 것이다. 이름은 동명이인이 있을 수 있고, 직업은 당연히 여러 사람이 같을 수 있다. 주소도 가족끼리 공유할 수 있다. 강의에서는 이메일 주소를 비교적 고유한 기준으로 보고 사람을 묶는다.</p>
                    {hp06_name_sex}
                    <p>코드는 먼저 <code>email_address.csv</code>를 기준으로 <code>person_db</code> 리스트를 만든다. 각 원소는 한 사람을 나타내는 딕셔너리이며, 처음에는 이메일과 주소만 들어 있다. 그다음 <code>email_job.csv</code>, <code>email_phone.csv</code>를 차례로 읽고, 이미 만들어 둔 사람 목록을 순회하면서 이메일이 같은 사람에게 직업과 전화번호를 붙인다.</p>
                    <p>이후 <code>name_email.csv</code>에서는 이름과 이메일을 읽는다. 이메일이 이미 기준 키로 쓰이고 있으므로 이름을 붙이는 것은 비교적 안전하다. 마지막으로 <code>phone_sex.csv</code>에서는 전화번호와 성별을 읽고, 전화번호가 같은 사람에게 성별 값을 붙인다. 캡처 화면의 출력처럼 최종 딕셔너리에는 <code>address</code>, <code>email</code>, <code>job</code>, <code>phone</code>, <code>name</code>, <code>sex</code>가 함께 들어간다.</p>
                    {csv_join_example}
                    <p>이메일을 기준으로 주소, 직업, 전화번호는 비교적 자연스럽게 붙일 수 있다. 하지만 직업으로 성별이나 주민등록번호를 붙이는 것은 위험하다. 같은 직업을 가진 사람이 여러 명일 수 있기 때문이다. “재봉사라는 직업을 가진 사람이 남자”라는 데이터가 있어도, 다른 재봉사는 여성일 수 있다. 따라서 직업은 고유 키가 아니며, 그 값을 기준으로 특정인의 민감 정보를 확정하면 안 된다.</p>
                    <p>강의의 결론은 데이터 결합에서 유일하지 않은 값을 유일한 값처럼 취급하면 오류와 침해 위험이 커진다는 것이다. 단순한 Python 코드로도 실습은 가능하지만, 실제 분석에서는 키의 고유성, 중복, 후보 수, 매칭 한계를 먼저 따져야 한다.</p>
                    """,
                },
            ],
            "checks": [
                "이름, 이메일, IP 주소, 비밀번호가 각각 개인정보 판단에서 왜 다르게 보일 수 있는지 설명할 수 있는가?",
                "유출 데이터가 텍스트, CSV, SQL 덤프 형태로 유통될 수 있다는 점을 이해했는가?",
                "모자이크 이론이 개인정보 위험과 어떻게 연결되는지 예시로 말할 수 있는가?",
                "inner, left, right, outer join의 차이를 설명할 수 있는가?",
                "이메일, 이름, 직업, 주소 중 어떤 값이 결합 키로 적합한지 판단할 수 있는가?",
            ],
        },
        {
            "id": "1-7",
            "title": "가상자산 믹싱과 거래 그래프",
            "subtitle": "블록체인 거래가 공개되어도 믹싱으로 흐름이 흐려지는 이유를 이해하고, 거래 내역을 그래프로 단순화한다.",
            "tags": ["믹싱", "그래프", "Graphviz"],
            "objectives": [
                "가상자산 믹싱이 자금 추적을 어렵게 하기 위해 거래 흐름을 섞는 과정임을 이해한다.",
                "중복 거래 제거, 믹싱 노드 그룹화, 시간·금액 패턴, 현실 금융 접점 추적 같은 분석 아이디어를 설명한다.",
                "거래 내역을 노드와 간선으로 표현하는 그래프 구조를 이해한다.",
                "Python 딕셔너리로 송금 그래프를 만들고, 양방향 거래를 순흐름으로 정리한다.",
                "Graphviz 문법으로 결과를 시각화할 수 있다.",
            ],
            "sections": [
                {
                    "heading": "믹싱이란 무엇인가",
                    "body": f"""
                    <p>가상자산 거래소 해킹 기사에서는 비트코인이나 다른 가상화폐가 탈취되었다는 말과 함께 믹싱이라는 단어가 자주 나온다. 믹싱은 흔히 돈세탁이라고도 하며, 자금 추적을 어렵게 하기 위해 여러 거래 내역을 섞고 흐름을 복잡하게 엮는 작업이다.</p>
                    <p>블록체인은 거래 내역이 공개된다는 특징이 있다. Etherscan 같은 사이트에서는 어떤 지갑에서 어떤 지갑으로 얼마만큼의 코인이나 토큰이 이동하는지 실시간으로 확인할 수 있다. 그래서 “거래가 모두 보이는데 어떻게 숨길 수 있나?”라는 의문이 생긴다. 믹싱의 핵심은 거래를 숨기는 것이 아니라, 실제 의미 있는 흐름이 무엇인지 알기 어렵게 만드는 것이다.</p>
                    {hp07_etherscan}
                    <p>예를 들어 A가 B에게 1000원을 보내면 누구나 흐름을 이해할 수 있다. 하지만 A가 여러 노드로 나누어 보내고, 중간 노드들이 서로 주고받고, 최종적으로 B에게 비슷한 금액이 모이면 겉보기 흐름은 매우 복잡해진다. 결과적으로 A는 1000원이 줄고 B는 1000원이 늘며, 중간 노드들은 들어온 만큼 다시 내보내 실질 변화가 없을 수 있다.</p>
                    {hp07_mixing_split}
                    """,
                },
                {
                    "heading": "믹싱 추적 아이디어",
                    "body": f"""
                    <table>
                      <thead><tr><th>방법</th><th>설명</th></tr></thead>
                      <tbody>
                        <tr><td>중복 거래 제거</td><td>두 노드 사이에 오간 여러 거래의 플러스·마이너스를 합산해 최종 순거래 한 건으로 간소화한다.</td></tr>
                        <tr><td>믹싱 노드 그룹화</td><td>알려진 믹싱 서비스 지갑을 하나의 그룹으로 묶고, 그룹 안팎의 자금 유입·유출에 집중한다.</td></tr>
                        <tr><td>서비스 패턴 역분석</td><td>특정 믹싱 업체의 난독화 패턴을 알고 있으면 그 패턴을 거꾸로 분석한다.</td></tr>
                        <tr><td>시간·금액 매칭</td><td>비슷한 시간대에 비슷한 규모의 금액이 빠져나가고 들어오는 흐름을 연결해 추정한다.</td></tr>
                        <tr><td>현실 금융 접점</td><td>가상자산을 원화, 달러, 금 같은 현실 자산과 교환하는 지점에서 은행·거래소 협조를 통해 추적한다.</td></tr>
                      </tbody>
                    </table>
                    {hp07_grouping}
                    <p>이 강의의 실습은 데이터 분석이 목적이므로 첫 번째 방법, 즉 A와 B 사이에 오간 여러 건의 거래를 하나로 합치는 방식에 집중한다.</p>
                    """,
                },
                {
                    "heading": "그래프 구조 복습",
                    "body": f"""
                    <p>거래 흐름은 그래프로 표현하기 좋다. 그래프는 노드와 링크, 즉 정점과 간선으로 연결된 데이터 구조다. SNS 친구 관계, 도시 간 도로망, 네트워크 인프라처럼 대상과 관계가 있는 문제를 표현할 때 사용한다. 이 강의에서는 지갑 또는 사람을 노드로 보고, 송금 관계를 방향 있는 간선으로 본다.</p>
                    {hp07_graph_structure}
                    <p>Python으로 그래프를 표현하는 방식에는 인접행렬과 인접리스트가 있다. 강의에서는 Python 딕셔너리를 이용해 두 방식의 장점을 절충한다. 바깥 딕셔너리의 키는 출발 노드이고, 그 값은 다시 딕셔너리다. 안쪽 딕셔너리의 키는 도착 노드, 값은 송금액이다. 즉 <code>graph["A"]["B"] = 10</code>은 A가 B에게 10을 보냈다는 뜻이다.</p>
                    """,
                },
                {
                    "heading": "Graphviz로 시각화하기",
                    "body": f"""
                    <p>코드 출력만으로는 복잡한 그래프를 이해하기 어렵다. 그래서 강의에서는 Graphviz를 소개한다. Graphviz는 노드와 간선을 텍스트 문법으로 적으면 그래프로 그려 주는 범용 시각화 도구다. 설치해서 사용할 수도 있고, 온라인 편집기에서 바로 확인할 수도 있다.</p>
                    {hp07_graphviz}
                    <p>가장 기본 문법은 <code>"A" -&gt; "B" [label="1000"];</code>처럼 출발 노드, 도착 노드, 간선 라벨을 한 줄로 적는 방식이다. 이번 실습에서는 송금자, 수취인, 송금액을 Graphviz 문법으로 출력해 거래 흐름을 눈으로 확인한다.</p>
                    """,
                },
                {
                    "heading": "실습: 조직도 재구성",
                    "body": f"""
                    <p>실습 설정은 범죄 조직 구성원들의 송금 내역을 확보했고, 이를 통해 조직도를 재구성한다는 것이다. 파일에는 송금자, 수취인, 송금액이 한 줄에 하나씩 들어 있다. 조직 특성상 아래 사람이 위 사람에게 수익금을 상납하는 구조를 알고 있다고 가정한다.</p>
                    {hp07_mission}
                    <p>하지만 거래 내역을 숨기기 위해 관련 없는 조직원끼리 돈을 주고받는 거래도 섞여 있다. 예를 들어 A가 F에게 100원을 보내고, F가 A에게 50원씩 두 번 보내면 전체 순효과는 0이다. 이런 거래를 그대로 그리면 그래프가 매우 복잡해진다. 목표는 플러스와 마이너스를 정리해 실제 순흐름만 남기는 것이다.</p>
                    <p>먼저 파일을 읽고 쉼표로 나눈 뒤 송금액은 정수로 바꾼다. 그다음 <code>G[src][dst]</code>에 송금액을 누적한다. <code>src</code>가 바깥 딕셔너리에 없으면 <code>G[src] = {{}}</code>로 새 딕셔너리를 만들고, <code>dst</code>가 안쪽 딕셔너리에 없으면 <code>G[src][dst] = 0</code>으로 시작한다. 같은 방향 거래가 여러 번 나오면 <code>G[src][dst] += amount</code>로 누적된다.</p>
                    {hp07_accumulate_code}
                    {transaction_accumulate}
                    {hp07_raw_edges}
                    <p>이 단계의 출력은 아직 정리되지 않은 원본 그래프다. 예를 들어 A가 B에게 보낸 금액과 B가 A에게 다시 보낸 금액이 따로 남아 있다. 조직도를 보려면 같은 두 사람 사이의 반대 방향 거래를 서로 상쇄해야 한다. 단순히 <code>G[dst][src]</code>를 바로 읽으면 도착 노드가 바깥 딕셔너리에 없을 때 <code>KeyError</code>가 발생한다.</p>
                    {hp07_reverse_lookup}
                    <p>그래서 강의에서는 <code>get()</code>을 사용한다. <code>G.get(dst, {{}}).get(src, 0)</code>은 반대 방향 거래가 있으면 그 금액을 가져오고, 없으면 0으로 처리한다. 그런 다음 <code>G[src][dst] - reverse_amount</code>가 0보다 큰 경우만 출력하면 순흐름만 남는다.</p>
                    {transaction_net_edges}
                    {hp07_net_edges}
                    <p>마지막 단계에서는 같은 순흐름 계산을 Graphviz 문법으로 출력한다. <code>label</code>에는 순금액을 적고, 노드 이름과 간선을 붙여 넣으면 온라인 Graphviz 편집기에서 바로 조직도처럼 볼 수 있다.</p>
                    {transaction_graph}
                    {hp07_final_graph}
                    <p>정리 전 그래프는 여러 사람이 얽히고설킨 모습이지만, 순흐름만 남기면 돈이 모이는 최상위 위치가 드러난다. 강의 예시에서는 홍길동이 가장 위에 있고, 그 아래 김철수와 다른 인물들이 이어지는 구조로 재구성된다. 핵심은 복잡한 거래 내역을 그대로 보는 것이 아니라, 분석 목적에 맞게 순효과를 계산해 구조를 단순화하는 것이다.</p>
                    """,
                },
            ],
            "checks": [
                "블록체인 거래가 공개되어도 믹싱이 추적을 어렵게 만드는 이유를 설명할 수 있는가?",
                "중복 거래 제거와 믹싱 노드 그룹화의 차이를 말할 수 있는가?",
                "Python 딕셔너리로 방향 그래프를 표현하는 방식을 이해했는가?",
                "graph.get(dst, {}).get(src, 0)이 왜 필요한지 설명할 수 있는가?",
                "Graphviz 문법으로 송금 흐름을 시각화할 수 있는가?",
            ],
        },
        {
            "id": "1-8",
            "title": "BeautifulSoup 웹 페이지 분석",
            "subtitle": "BeautifulSoup과 개발자 도구로 HTML 요소를 선택하고, 링크를 따라가며 사이트 구조와 보물 페이지를 찾는다.",
            "tags": ["BeautifulSoup", "크롤링", "사이트맵"],
            "objectives": [
                "requests와 BeautifulSoup의 역할 차이를 설명한다.",
                "Chrome 개발자 도구의 Copy selector를 이용해 필요한 HTML 요소를 찾는다.",
                "웹 스크래핑과 웹 크롤링의 차이를 이해한다.",
                "visited 집합과 재귀 함수를 이용해 이미 방문한 페이지를 중복 탐색하지 않는다.",
                "찾은 링크 관계를 Graphviz 형식으로 출력해 사이트맵을 그린다.",
            ],
            "sections": [
                {
                    "heading": "BS4의 역할",
                    "body": f"""
                    <p>BS4, 즉 BeautifulSoup은 Python에서 HTML이나 XML 문서를 쉽게 처리하도록 도와주는 패키지다. 이전에 배운 requests가 HTTP 요청을 보내고 응답을 받는 역할이라면, BeautifulSoup은 받은 HTML을 해석하고 필요한 정보만 뽑아내는 역할이다.</p>
                    {hp08_bs4}
                    <p>HTML 코드를 BeautifulSoup으로 해석하면 제목, <code>p</code> 태그, <code>a</code> 태그, 특정 클래스나 아이디를 가진 요소를 코드로 쉽게 찾을 수 있다. 웹페이지의 모든 하이퍼링크를 나열하거나, 본문의 글자 정보를 추출하거나, 특정 버튼과 광고 배너 같은 요소를 찾고, 태그 트리를 재귀적으로 탐색할 수 있다.</p>
                    <p>강의에서 보인 예처럼 <code>soup.title</code>은 제목 태그를, <code>soup.p</code>는 첫 번째 문단 태그를, <code>soup.a</code>는 첫 번째 링크 태그를 가져온다. 여러 링크를 모두 보고 싶으면 <code>soup.find_all("a")</code>처럼 태그 이름으로 전체를 찾고, 특정 아이디가 있는 요소만 찾고 싶으면 <code>soup.find(id="link3")</code>처럼 조건을 준다.</p>
                    """,
                },
                {
                    "heading": "개발자 도구와 selector",
                    "body": f"""
                    <p>BeautifulSoup으로 요소를 찾으려면 무엇을 기준으로 찾을지 알아야 한다. 이때 Chrome 개발자 도구가 유용하다. 화면에서 원하는 버튼이나 링크를 마우스 오른쪽 클릭하고 검사 버튼을 누르면, 해당 화면 요소가 어떤 HTML 태그에 해당하는지 강조된다.</p>
                    <p>개발자 도구에서 다시 마우스 오른쪽 클릭 후 Copy selector를 선택하면, 그 요소를 가리키는 CSS selector가 복사된다. 예를 들어 <code>body &gt; div.navigation &gt; a:nth-child(2)</code> 같은 selector가 만들어질 수 있다. 이 값을 BeautifulSoup의 <code>select()</code>에 넘기면 해당 요소를 리스트로 얻는다.</p>
                    {hp08_selector}
                    {bs4_selector}
                    <p><code>select()</code>는 조건을 만족하는 요소 전체를 리스트로 반환한다. 특정 번째 자식 조건을 넣으면 화면 예시처럼 두 번째 문 하나만 나오고, 그 조건을 빼면 빨간문, 파란문, 초록문처럼 여러 링크가 모두 나온다. 요소의 화면 텍스트는 <code>elements[0].text</code>로 읽고, 이동 주소는 <code>elements[0]["href"]</code>로 읽는다.</p>
                    {hp08_all_links}
                    {bs4_all_links}
                    <p>이 코드는 화면의 “조건을 만족하는 모든 요소 탐색” 예제와 같은 흐름이다. <code>soup.select("body &gt; div.navigation &gt; a")</code>가 문 링크 전체를 리스트로 가져오고, <code>enumerate()</code>로 순번을 붙여 각 링크의 표시 텍스트와 실제 이동 URL을 함께 출력한다.</p>
                    <p>이 단계에서 중요한 점은 “사람이 눈으로 본 버튼”과 “코드가 선택할 HTML 요소”를 연결하는 것이다. 개발자 도구는 그 연결을 확인하는 도구이고, BeautifulSoup은 확인한 selector를 반복 실행 가능한 Python 코드로 바꾸는 도구다.</p>
                    """,
                },
                {
                    "heading": "스크래핑과 크롤링",
                    "body": f"""
                    <p>웹 스크래핑과 웹 크롤링은 비슷하게 쓰이지만 강의에서는 구분해서 설명한다. 웹 스크래핑은 이미 알고 있는 페이지나 구조에서 필요한 정보를 뽑아내는 것이다. 예를 들어 뉴스 목록 페이지에서 제목과 링크만 추출하는 경우가 여기에 가깝다.</p>
                    {hp08_crawling}
                    <p>웹 크롤링은 링크를 따라가며 웹사이트 전체 구조를 탐색하는 것이다. 첫 페이지에 들어가고, 그 페이지가 가리키는 다른 페이지로 이동하고, 다시 그 페이지의 링크를 따라가며 전체 지도를 그린다. 그래서 크롤링에서는 그래프 구조가 중요하다. 페이지는 노드가 되고, 링크는 간선이 된다.</p>
                    <table>
                      <thead><tr><th>구분</th><th>관심 대상</th><th>예시</th></tr></thead>
                      <tbody>
                        <tr><td>웹 스크래핑</td><td>특정 페이지에서 필요한 값 추출</td><td>게시판 글 목록에서 제목, 작성자, 링크만 가져오기</td></tr>
                        <tr><td>웹 크롤링</td><td>링크를 따라가며 전체 구조 탐색</td><td>첫 페이지에서 시작해 모든 방을 방문하고 사이트맵 만들기</td></tr>
                      </tbody>
                    </table>
                    """,
                },
                {
                    "heading": "미궁 사이트 탐색 실습",
                    "body": f"""
                    <p>실습 사이트는 <code>dungeon.nyan101.com</code>이다. 각 방에는 하나에서 세 개의 문이 있고, 문을 누르면 다른 방으로 이동한다. 여러 페이지 중 하나에만 <code>WHS</code>로 시작하는 보물 문자열이 있다. 이전 HTTP 실습처럼 URL이 1, 2, 3으로 예측 가능한 구조가 아니므로, 먼저 현재 페이지의 링크를 읽고 그 링크를 따라가야 한다.</p>
                    {hp08_mission}
                    <p>처음에는 <code>index.html</code>에서 시작해 <code>body &gt; div.navigation &gt; a</code> selector로 모든 문 링크를 가져온다. 링크의 <code>text</code>를 출력하면 빨간 문, 파란 문, 초록 문처럼 화면에 보이는 이름이 나오고, <code>href</code>를 출력하면 <code>HWJG.html</code>, <code>ZDTW.html</code>, <code>JRBM.html</code>처럼 실제 이동할 파일 이름이 나온다. 이 단계를 확인한 뒤에야 자동 탐색 함수를 만들 수 있다.</p>
                    {hp08_traversal}
                    {bs4_link_href_loop}
                    <p>탐색 함수는 <code>path</code>를 입력받는다. 이미 방문한 경로라면 멈추고, 처음 보는 경로라면 <code>visited_paths</code> 집합에 추가한다. 그다음 <code>http://dungeon.nyan101.com/</code> 뒤에 현재 경로를 붙여 URL을 만들고 requests로 HTML을 받아온다. 본문에 <code>WHS</code>가 있으면 해당 페이지의 HTML을 출력한다. 이후 BeautifulSoup으로 문 링크를 모두 찾고, 각 링크의 <code>href</code>를 다시 탐색 함수에 넘긴다.</p>
                    {bs4_crawler}
                    {hp08_treasure}
                    <p>강의 예시에서는 보물 페이지의 아이디가 <code>MMVK</code>로 확인된다. 실제 사이트에서 <code>MMVK.html</code>로 이동하면 “보물을 찾았습니다!”라는 문구와 함께 <code>WHS{{Y0u_f0und_7h3_Tr345ur3}}</code> 형식의 문자열을 볼 수 있다. 이 방은 막다른 길이므로 더 이상 따라갈 문이 없고, 크롤러도 이 지점에서 해당 경로의 탐색을 끝낸다.</p>
                    """,
                },
                {
                    "heading": "사이트맵 그리기",
                    "body": f"""
                    <p>보물 페이지를 찾는 것만으로도 문제는 풀 수 있지만, 전체 사이트가 어떤 구조인지 보려면 링크 관계를 기록해야 한다. 강의에서는 시작 페이지에서 빨간문을 통해 어떤 페이지로 가고, 그 페이지에서 파란문을 통해 어디로 가는지 같은 정보를 지도 형태로 그리는 추가 과제를 제시한다.</p>
                    <p>코드에서는 링크로 들어가기 직전에 출발점, 도착점, 라벨 이름을 출력한다. 출발점은 현재 <code>path</code>, 도착점은 링크의 <code>href</code>, 라벨은 빨간문·파란문·초록문 같은 텍스트다. 강의 화면에서는 <code>HWJG.html -&gt; ZXFD.html [빨간 문]</code>처럼 한 줄에 하나의 연결을 남긴다.</p>
                    {hp08_sitemap}
                    <p>출력된 Graphviz 문법을 지도 페이지나 Graphviz 도구에 붙여 넣으면 어떤 페이지에서 어떤 문을 통해 어디로 이동하는지 전체 구조를 시각화할 수 있다. 복잡한 지도라도 페이지들이 그래프 형태로 연결된다는 점을 이해하면, 목표 페이지까지의 경로를 찾는 사고가 쉬워진다.</p>
                    <div class="callout">핵심은 보물 문자열만 찾는 데서 끝내지 않는 것이다. 링크 관계를 함께 남기면 “어떤 방에서 어떤 문을 통해 목표 방에 도달했는지”를 설명할 수 있고, 사이트 전체가 방향 그래프라는 사실도 눈으로 확인할 수 있다.</div>
                    """,
                },
            ],
            "checks": [
                "requests와 BeautifulSoup의 역할 차이를 설명할 수 있는가?",
                "Chrome 개발자 도구에서 Copy selector가 왜 유용한지 이해했는가?",
                "스크래핑과 크롤링의 차이를 예시로 말할 수 있는가?",
                "visited 집합이 없으면 크롤러에서 어떤 문제가 생길 수 있는지 설명할 수 있는가?",
                "링크 관계를 Graphviz 출력으로 바꾸어 사이트맵을 그릴 수 있는가?",
            ],
        },
        {
            "id": "1-9",
            "title": "OSINT와 정보 그래프",
            "subtitle": "공개 출처 정보의 의미, OSINT 도구, 무심코 노출되는 개인정보, Predicta Graph 기반 정보 연결을 정리한다.",
            "tags": ["OSINT", "개인정보", "그래프"],
            "objectives": [
                "OSINT가 특별한 권한 없이 접근 가능한 공개 출처에서 수집한 정보라는 점을 이해한다.",
                "Google, Criminal IP, Maltego, VirusTotal, Shodan 등 OSINT 도구의 역할을 구분한다.",
                "SNS, 게시글, 사진 EXIF, 핫스팟 이름 같은 일상 정보가 개인정보 단서가 될 수 있음을 설명한다.",
                "LLM으로 공개 게시물을 모아 분석할 때 위험이 커지는 이유를 이해한다.",
                "Predicta Graph 같은 도구로 사람, 계정, 조직, 게시물, 관계를 그래프로 연결하는 방식을 설명한다.",
            ],
            "sections": [
                {
                    "heading": "OSINT의 의미와 활용 분야",
                    "body": f"""
                    <p>OSINT는 Open Source Intelligence의 약자이며, 공개 출처 정보를 뜻한다. 여기서 공개 출처란 특별한 권한 없이 접근 가능한 공개된 출처를 말한다. 뉴스, 개인 블로그, SNS, 정부기관 공식 발표, 공개된 위성 사진 등이 모두 포함될 수 있다.</p>
                    {hp09_definition}
                    <p>디지털 시대에는 종이 신문보다 온라인 뉴스와 SNS가 훨씬 많은 정보를 만든다. 그래서 OSINT의 중요성이 커졌다. 강의에서는 러시아·우크라이나 전쟁, Criminal IP와 Shodan 같은 CTI 플랫폼, 위성 지도와 Google Earth를 활용한 시설 탐색 사례 등을 OSINT 활용 예로 설명한다.</p>
                    {hp09_use_cases}
                    <p>핵심은 “비밀 시스템에 침입해서 얻은 정보”가 아니라 “이미 공개되어 있지만 흩어져 있는 정보”를 체계적으로 수집·검증·연결한다는 점이다. 공개 정보라고 해서 항상 사용이 자유로운 것은 아니며, 개인정보와 민감 정보가 섞여 있을 수 있기 때문에 목적과 범위를 분명히 해야 한다.</p>
                    """,
                },
                {
                    "heading": "대표 도구와 분야별 도구",
                    "body": f"""
                    <p>가장 대표적인 OSINT 도구는 Google이다. Google dorking 또는 Google hacking이라는 표현이 있을 정도로, 검색 옵션을 잘 활용하면 일반 검색으로는 잘 드러나지 않는 정보도 찾을 수 있다.</p>
                    <p>Criminal IP는 사이버보안 OSINT와 CTI에 특화된 검색 엔진·위협 정보 플랫폼이다. 인터넷을 주기적으로 스캔하고, 특정 IP가 얼마나 위험한지, 알려진 취약점이 있는지, 악성코드 C2로 쓰이는지 같은 정보를 제공한다. Maltego는 사이버보안에만 한정되지 않고 여러 데이터 소스를 통합해 그래프 시각화하는 데 강점이 있는 분석 도구다.</p>
                    {hp09_criminalip}
                    {hp09_tool_classes}
                    <table>
                      <thead><tr><th>분야</th><th>도구 예시</th><th>역할</th></tr></thead>
                      <tbody>
                        <tr><td>일반 검색</td><td>Google</td><td>검색 연산자와 공개 웹 정보를 활용한다.</td></tr>
                        <tr><td>CTI</td><td>Criminal IP, Shodan, VirusTotal</td><td>IP, 도메인, 취약점, 악성 여부, 위협 평판을 확인한다.</td></tr>
                        <tr><td>연결 그래프</td><td>Maltego, Predicta Graph</td><td>사람, 계정, 조직, 사건, 주소 같은 관계를 그래프로 그린다.</td></tr>
                        <tr><td>SNS</td><td>Social Searcher, Recon-ng 등</td><td>게시물, 계정, 태그, 공개 프로필을 탐색한다.</td></tr>
                        <tr><td>위치·지도</td><td>Google Maps, Google Earth</td><td>공개 지도와 위성 사진에서 위치 단서를 찾는다.</td></tr>
                        <tr><td>다크웹 탐색</td><td>전문 OSINT 도구들</td><td>일반 웹 밖의 공개·반공개 정보를 추적한다.</td></tr>
                      </tbody>
                    </table>
                    """,
                },
                {
                    "heading": "나도 모르게 드러나는 정보",
                    "body": f"""
                    <p>강의는 EBS 다큐멘터리 속 은퇴한 CIA 부국장의 인터뷰를 소개한다. 많은 사람이 자신이 어디에 사는지, 종교적·정치적 견해, 친구 관계, 이메일 주소, 전화번호, 사진을 스스로 인터넷에 공개한다는 점이 과거 정보기관 관점에서는 꿈같은 상황이라는 취지다. SNS와 IoT가 일상화되면서 개인은 자신도 모르게 많은 정보를 남긴다.</p>
                    {hp09_cia_quote}
                    <p>게시판에서 실명을 쓰지 않고 아이디나 익명으로 글을 써도 단서는 남을 수 있다. 언제 글을 쓰고 댓글을 다는지, 어떤 IP를 쓰는지, 글 내용에 동네 행사나 학교 건물, 수업 시간표 단서가 있는지 등이 모두 정보가 된다. “오늘 집 앞에 드라마 촬영이 왔다”, “어느 콘서트장이 집에서 10분 거리다” 같은 글만으로도 위치, 취미, 생활권이 드러날 수 있다.</p>
                    <p>강의 화면의 예시처럼 온라인 활동 시간, IP 주소, 동네 행사 같은 사소한 단서도 여러 개가 모이면 의미가 생긴다. 학교 와이파이 연결 문제를 올린 시간, 댓글을 단 시간, 주변 행사를 언급한 글을 이어 보면 사용자의 생활 패턴이나 소속 공간을 추정할 수 있다.</p>
                    <p>사진도 마찬가지다. 스마트폰 사진에는 EXIF 메타데이터가 들어갈 수 있고, 촬영 기기, 촬영 옵션, GPS 위치가 포함될 수 있다. 강의에서는 책상 위 장식품 사진만 보면 취미 정도만 알 수 있지만, EXIF를 보면 휴대폰 기종과 집 위치에 가까운 주소까지 나올 수 있다고 설명한다.</p>
                    {hp09_metadata}
                    <p>따라서 온라인에 사진 원본을 올릴 때는 위치 정보 저장 설정, 메타데이터 제거 여부, 업로드 대상의 공개 범위를 확인해야 한다. 화면에 보이는 사물보다 파일 내부 메타데이터가 더 직접적인 개인정보가 될 수 있다.</p>
                    """,
                },
                {
                    "heading": "핫스팟, 블루투스, LLM 시대의 위험",
                    "body": f"""
                    <p>스마트폰 핫스팟 이름이나 블루투스 기기 이름도 단서가 된다. iPhone은 기본 핫스팟 이름이 “누구누구의 iPhone”처럼 설정되는 경우가 많고, Android는 기기명이나 전화번호 일부가 노출될 수 있다. 작은 방이나 한정된 공간에서는 그 정보만으로 주변 사람의 이름이나 전화번호 일부를 추정할 수 있다.</p>
                    {hp09_llm_risk}
                    <p>과거에는 누군가가 밤새 게시글을 읽고 조합해야 가능한 일이었지만, LLM이 등장한 지금은 공개 글을 모아 “이 사람의 집 주소, 직장, 개인정보 단서가 있는지 모두 뽑아 달라”고 시킬 수 있다. 그래서 별로 중요하지 않아 보이는 공개 게시물도 대량 분석과 결합되면 위험이 커진다.</p>
                    <p>이 지점에서 강의가 강조하는 것은 방어적 습관이다. 핫스팟 이름을 실명이나 전화번호가 드러나지 않게 바꾸고, 블루투스 기기명도 기본값 그대로 두지 않는 것이 좋다. 게시글을 올릴 때도 시간, 장소, 주변 사람, 반복되는 생활 패턴이 한꺼번에 드러나지 않는지 확인해야 한다.</p>
                    """,
                },
                {
                    "heading": "Predicta Graph로 정보 연결하기",
                    "body": f"""
                    <p>강의 후반부는 문제 풀이보다 OSINT 도구 소개에 가깝다. Predicta Graph는 무료 버전에서도 어느 정도 기능을 쓸 수 있는 그래프 기반 도구로 소개된다. 목적은 알고 있는 정보를 하나의 큰 지도로 연결해 보는 것이다.</p>
                    {hp09_predicta_start}
                    <p>예를 들어 한 사람에 대해 알고 있는 것이 <code>nyan101</code>이라는 아이디뿐이라고 하자. 그 아이디가 GitHub 계정일 수 있고, 같은 아이디를 GitLab이나 Instagram에서도 쓸 수 있다. 어떤 GitHub 저장소를 다른 사람이 팔로우하고 있고, Facebook에서 실명 계정끼리 친구 관계가 있으며, Instagram 게시물에 누군가 태그되어 있다면, 서로 다른 출처의 단서를 그래프로 연결할 수 있다.</p>
                    {osint_graph}
                    {hp09_predicta_graph}
                    <p>무료 버전은 사용자가 알고 있는 정보를 직접 정제하고 연결하는 데 초점이 있고, 유료 기능은 같은 아이디가 여러 플랫폼에서 쓰이는지 자동으로 찾아 주는 식의 추가 기능을 제공할 수 있다. 강의의 핵심은 도구 이름 자체보다, 흩어진 공개 정보를 정리하고 관계를 시각화하면 새로운 연결이 보인다는 점이다.</p>
                    <div class="callout">그래프 도구의 가치는 자동으로 정답을 내는 데 있지 않다. 이미 확인한 단서의 출처와 관계를 시각적으로 정리해, 어떤 연결은 확인되었고 어떤 연결은 추정인지 구분하게 해 주는 데 있다.</div>
                    """,
                },
            ],
            "checks": [
                "OSINT가 공개 출처 정보라는 뜻을 설명할 수 있는가?",
                "Google, Criminal IP, Maltego가 각각 어떤 OSINT 역할을 하는지 구분할 수 있는가?",
                "게시글 시간, 사진 EXIF, 핫스팟 이름이 왜 개인정보 단서가 될 수 있는지 말할 수 있는가?",
                "LLM이 공개 게시물 분석 위험을 키우는 이유를 이해했는가?",
                "사람, 계정, 조직, 게시물, 태그를 그래프로 연결해 정보를 정리하는 방식을 설명할 수 있는가?",
            ],
        },
    ]
