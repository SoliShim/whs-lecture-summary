from __future__ import annotations


def build_offline_weekend_lectures(code_block, image_figure):
    schedule_0613 = image_figure(
        "../../../../screenshots/offline-weekend/2026-06-13-schedule.jpg",
        "2026년 6월 13일 오프라인 시간표",
        "1교시는 정보보안윤리 / 사이버 안보, 2교시는 컴퓨터 구조 I, 3교시는 웹해킹 원리로 진행되었다.",
    )
    schedule_0614 = image_figure(
        "../../../../screenshots/offline-weekend/2026-06-14-schedule.jpg",
        "2026년 6월 14일 오프라인 시간표",
        "1교시는 프로그래밍 기초 및 응용 실습, 2교시는 해커의 프로그래밍, 3교시는 개인정보보호법으로 진행되었다.",
    )

    safe_query_example = code_block(
        """
        # 취약한 문자열 결합 대신 파라미터 바인딩을 사용한다.
        post_id = request.args.get("id", type=int)
        cursor.execute(
            "SELECT id, title, body FROM posts WHERE id = ?",
            (post_id,),
        )
        post = cursor.fetchone()
        """,
        "python",
    )
    integer_boundary_code = code_block(
        """
        #include <limits.h>
        #include <stdio.h>

        int main(void) {
            signed char max = SCHAR_MAX;
            signed char min = SCHAR_MIN;

            printf("SCHAR_MAX = %d\\n", max);
            printf("overflow  = %d\\n", (signed char)(max + 1));
            printf("SCHAR_MIN = %d\\n", min);
            printf("underflow = %d\\n", (signed char)(min - 1));
            return 0;
        }
        """,
        "c",
    )
    compile_pipeline_commands = code_block(
        """
        # 같은 C 소스가 단계별로 어떤 산출물을 만드는지 확인한다.
        gcc -E hello.c -o hello.i      # 전처리 결과
        gcc -S hello.i -o hello.s      # 어셈블리
        gcc -c hello.s -o hello.o      # relocatable object
        gcc hello.o -o hello           # 실행 파일

        file hello.o
        readelf -h hello.o
        objdump -d hello.o
        strip hello
        """,
        "bash",
    )
    file_lifecycle_code = code_block(
        """
        #include <stdio.h>

        int main(void) {
            FILE *fp = fopen("test.txt", "a");
            if (fp == NULL) {
                perror("fopen");
                return 1;
            }

            fputs("hello\\n", fp);
            fclose(fp);
            return 0;
        }
        """,
        "c",
    )
    resource_leak_code = code_block(
        """
        FILE *fp = fopen("access.log", "a");
        if (fp == NULL) {
            perror("fopen");
            return 1;
        }

        /* 작업 중간에 return하거나 예외 경로로 빠질 때도 fclose가 필요하다. */
        fprintf(fp, "request handled\\n");
        fclose(fp);
        """,
        "c",
    )
    json_shape_code = code_block(
        """
        {
          "name": "whitehat",
          "age": 4,
          "missions": [
            {"id": 1, "type": "file-io"},
            {"id": 2, "type": "static-analysis"}
          ]
        }
        """,
        "json",
    )
    ast_pattern_code = code_block(
        """
        # AST 기반 점검은 코드 문자열이 아니라 구조를 본다.
        if node.kind == "CallExpr" and node.name == "strcpy":
            report("경계 검사가 없는 문자열 복사 가능성 확인")
        """,
        "python",
    )
    commit_hunt_workflow = code_block(
        """
        git log --oneline --grep "vulnerability"
        git log --oneline --grep "XSS"
        git show <commit-id>

        # 빨간 줄은 삭제된 코드, 초록 줄은 추가된 코드다.
        # 취약점 수정 커밋을 보면 그 프로젝트의 실제 버그 패턴을 역추적할 수 있다.
        """,
        "bash",
    )
    requests_code = code_block(
        """
        import requests

        response = requests.get("http://board.nyan101.com/sample/list", timeout=5)
        print(response.status_code)
        print(response.text[:500])
        """,
        "python",
    )
    bs4_code = code_block(
        """
        from bs4 import BeautifulSoup

        soup = BeautifulSoup(response.text, "html.parser")
        for title in soup.select(".post-title"):
            print(title.get_text(strip=True))
        """,
        "python",
    )
    selenium_code = code_block(
        """
        from selenium import webdriver

        driver = webdriver.Chrome()
        driver.get("http://board.nyan101.com/post/1")
        for comment in driver.find_elements("css selector", ".comment"):
            print(comment.text)
        driver.quit()
        """,
        "python",
    )
    scraping_pipeline_code = code_block(
        """
        posts = collect_post_ids(page_start=1, page_end=10)
        comments = []

        for post_id in tqdm(posts, desc="collect comments"):
            comments.extend(fetch_comments(post_id))

        by_account = count_by(comments, key="account")
        by_hour = count_by(comments, key=("weekday", "hour"))
        """,
        "python",
    )
    heatmap_code = code_block(
        """
        import pandas as pd
        import seaborn as sns
        import matplotlib.pyplot as plt

        frame = pd.DataFrame(comments)
        pivot = frame.pivot_table(
            index="weekday",
            columns="hour",
            values="comment_id",
            aggfunc="count",
            fill_value=0,
        )

        sns.heatmap(pivot, cmap="YlGnBu")
        plt.title("account activity by weekday/hour")
        plt.show()
        """,
        "python",
    )
    privacy_lifecycle_code = code_block(
        """
        수집 -> 보관 -> 이용 -> 제공 또는 위탁 -> 파기

        사고 발생 시:
        1. 정보주체에게 통지한다.
        2. 정해진 기한 안에 관계 기관에 신고한다.
        3. 원인, 영향 범위, 재발 방지책을 정리한다.
        """,
        "text",
    )

    slide_hacker = image_figure(
        "../../../../screenshots/offline-weekend/hackers-programming/slide-07.jpg",
        "해커를 설명하는 네 가지 관점",
        "문제 해결을 넘어 문제를 찾고, 내부 원리를 파고들며, 배경지식으로 임기응변을 적용하는 사람으로 해커를 정의한다.",
    )
    slide_automation = image_figure(
        "../../../../screenshots/offline-weekend/hackers-programming/slide-09.jpg",
        "자동화를 좋아하는 태도",
        "반복 작업을 코드로 줄이는 효율뿐 아니라 코드가 대신 일하는 과정을 보는 만족감도 해커의 프로그래밍 동기가 된다.",
    )
    slide_programming = image_figure(
        "../../../../screenshots/offline-weekend/hackers-programming/slide-12.jpg",
        "해커가 좋은 프로그래머여야 하는 이유",
        "모든 라이브러리를 외우는 것이 아니라 머릿속 구상을 코드로 옮길 수 있어야 아이디어가 병목이 된다.",
    )
    slide_environment = image_figure(
        "../../../../screenshots/offline-weekend/hackers-programming/slide-19.jpg",
        "실습 환경 구축",
        "pip와 uv, requirements.txt와 pyproject.toml을 비교하며 이번 실습에서는 uv 기반 의존성 관리를 사용한다.",
    )
    slide_requests = image_figure(
        "../../../../screenshots/offline-weekend/hackers-programming/slide-22.jpg",
        "requests 실습",
        "브라우저 없이 HTTP 요청을 보내고 서버 응답 HTML을 직접 확인하는 첫 실습이다.",
    )
    slide_bs4 = image_figure(
        "../../../../screenshots/offline-weekend/hackers-programming/slide-25.jpg",
        "BeautifulSoup 실습",
        "목록 페이지에서 게시글 제목을 추출하고, 추가 실습으로 댓글 내용을 추출하는 흐름을 잡는다.",
    )
    slide_selenium = image_figure(
        "../../../../screenshots/offline-weekend/hackers-programming/slide-31.jpg",
        "동적 페이지 스크래핑",
        "직접 댓글 API에 접근하지 않고 브라우저가 실제로 페이지를 여는 흐름을 Selenium으로 따라간다.",
    )
    slide_datasaurus = image_figure(
        "../../../../screenshots/offline-weekend/hackers-programming/slide-35.jpg",
        "시각화가 필요한 이유",
        "평균, 분산, 상관계수가 같아도 데이터의 실제 모양은 완전히 다를 수 있음을 Datasaurus Dozen으로 보여준다.",
    )
    slide_visualize = image_figure(
        "../../../../screenshots/offline-weekend/hackers-programming/slide-36.jpg",
        "계정별 활동량 시각화 미션",
        "댓글 데이터를 계정별, 요일별, 시간대별로 정리해 이상 패턴을 찾는 실습으로 이어진다.",
    )
    slide_result = image_figure(
        "../../../../screenshots/offline-weekend/hackers-programming/slide-37.jpg",
        "시각화 결과 예시",
        "텍스트 카운트만으로는 보기 어려운 활동 패턴을 heatmap 형태로 확인하는 결과 화면이다.",
    )

    return [
        {
            "id": "1-1",
            "title": "정보보안윤리 / 사이버 안보",
            "subtitle": "기술을 배우기 전에 보안 전문가가 가져야 할 윤리, 책임, 국가 안보 관점을 먼저 세운다.",
            "tags": ["2026-06-13", "1교시", "정보보안윤리", "사이버 안보", "김수득"],
            "transcript_path": "오프라인 강의/0613-1.txt",
            "objectives": [
                "사이버 보안과 사이버 안보의 차이를 설명한다.",
                "보안 전문가가 개인정보, 기업 비밀, 국가 기술을 다룰 때 필요한 윤리 기준을 정리한다.",
                "국가배우 해킹 조직, 국제 범죄 조직, 랜섬웨어 생태계의 차이와 연결 관계를 이해한다.",
            ],
            "sections": [
                {
                    "heading": "오프라인 1일차 첫 시간의 위치",
                    "body": f"""
                    <p>첫 오프라인 강의는 기술 실습보다 먼저 <strong>정보보안윤리</strong>와 <strong>사이버 안보</strong>를 다뤘다. 강사는 화이트햇 과정에서 좋은 환경으로 교육을 받는 만큼, 배운 기술을 어떤 방향으로 써야 하는지 먼저 생각해야 한다고 강조했다.</p>
                    <p>강의의 출발점은 사이버 보안과 사이버 안보의 구분이다. 사이버 보안은 개인, 기업, 조직의 정보를 보호하는 기술적·관리적 관점에 가깝고, 사이버 안보는 국가 단위의 안전, 기반시설, 외교, 군사, 법제도까지 포함한다.</p>
                    <div class="diagram two-col">
                      <div><span class="node-title">사이버 보안</span><p>기업·기관·개인의 자산과 서비스를 보호하고 침해사고를 줄이는 활동이다.</p></div>
                      <div><span class="node-title">사이버 안보</span><p>국가 차원의 위협, 기반시설, 국가배우 공격, 국제 공조까지 포함하는 넓은 영역이다.</p></div>
                    </div>
                    {schedule_0613}
                    """,
                },
                {
                    "heading": "보안 전문가가 접근하게 되는 정보",
                    "body": """
                    <p>보안 전문가는 컨설팅, 진단, 사고 대응, 법률 검토, 내부 보안 업무를 하면서 일반 사용자가 보면 안 되는 정보에 접근할 수 있다. 강의에서는 개인정보, 기업 비밀, 국가 핵심 기술, 고객사의 내부 정보처럼 민감한 자료를 예로 들었다.</p>
                    <p>이때 핵심은 “볼 수 있다”와 “봐도 된다”를 구분하는 것이다. 업무상 접근 권한이 생겼더라도 호기심으로 열람하거나, 가족·친구에게 이야기하거나, 외부에 공유하면 안 된다. 보안 업무의 신뢰는 기술 실력만이 아니라 <strong>비밀 유지</strong>와 <strong>목적 제한</strong>에서 나온다.</p>
                    <table>
                      <thead><tr><th>정보 유형</th><th>강의에서 강조한 위험</th><th>올바른 태도</th></tr></thead>
                      <tbody>
                        <tr><td>개인정보</td><td>이름, 연락처, 계정, 사진, 서비스 이용 기록이 노출될 수 있다.</td><td>업무 목적 외 열람과 공유를 하지 않는다.</td></tr>
                        <tr><td>기업 비밀</td><td>고객사 시스템 구조, 취약점, 내부 정책이 경쟁상·법적 피해로 이어질 수 있다.</td><td>계약과 보안 절차 안에서만 다룬다.</td></tr>
                        <tr><td>국가 기술</td><td>방산, 기반시설, 핵심 산업 기술은 국가 안보 이슈가 된다.</td><td>기술적 판단과 국가적 책임을 함께 본다.</td></tr>
                      </tbody>
                    </table>
                    """,
                },
                {
                    "heading": "강사의 커리어가 보여준 사이버 안보의 범위",
                    "body": """
                    <p>강의 원문에서 강사는 LG전자 개발·보안 업무, 국가정보원, 회계법인, 법률사무소로 이어지는 본인의 경력을 설명했다. 이 흐름은 보안 커리어가 단순히 취약점 하나를 찾는 일로 끝나지 않는다는 점을 보여준다. 개발을 알아야 제품과 시스템을 이해할 수 있고, 국가기관 경험은 사이버 안보 관점을 만들며, 법률 업무는 사고 대응과 책임 판단으로 이어진다.</p>
                    <p>그래서 이 강의의 “윤리”는 추상적인 착한 마음 이야기가 아니다. 보안 전문가는 기술, 조직, 국가, 법, 사람의 피해를 함께 다룬다. 나중에 국정원, KISA, 경찰, 군, 보안 컨설팅, 기업 보안팀, 법률·컴플라이언스 쪽으로 가더라도 공통으로 필요한 것은 민감한 정보를 다루는 태도다.</p>
                    <div class="timeline compact">
                      <div><strong>개발 경험</strong><p>시스템이 실제로 어떻게 만들어지는지 알아야 취약점도 현실적으로 이해한다.</p></div>
                      <div><strong>국가기관 경험</strong><p>개별 시스템 사고를 국가 기반시설, 외교, 안보 관점까지 확장해 본다.</p></div>
                      <div><strong>법률·자문 경험</strong><p>기술 행위가 허용 범위, 책임, 신고, 증거 문제와 어떻게 연결되는지 판단한다.</p></div>
                    </div>
                    """,
                },
                {
                    "heading": "도구와 호기심의 양면성",
                    "body": """
                    <p>스캐너, 패킷 분석기, 클라우드 저장소, 생성형 AI는 원래 네트워크 상태 확인, 자산 관리, 학습, 방어 자동화를 위해 쓰일 수 있다. 그러나 같은 도구가 공격 대상 탐색, 열린 포트 확인, 서비스 버전 확인, 취약점 탐색에 쓰이면 완전히 다른 의미가 된다.</p>
                    <p>강사는 해커에게 호기심이 많다는 점을 인정하면서도, 그 호기심을 절제하지 못하면 목적을 잃고 선을 넘는다고 설명했다. 공개되어 보이는 관리자 페이지, 학교 홈페이지의 개인정보 노출, 웹셸 업로드, 점검을 핑계로 한 접근은 모두 “공개되어 있으니 괜찮다”로 처리할 수 없다.</p>
                    <div class="callout">실무 판단 기준: 내가 이걸 왜 보려고 했는지, 허가받은 범위인지, 담당 부서에 제보해야 할 상황인지 먼저 멈춰서 확인한다.</div>
                    """,
                },
                {
                    "heading": "선을 넘기 전 확인해야 할 질문",
                    "body": """
                    <p>원문에서 반복된 메시지는 “할 수 있다”와 “해도 된다”를 분리하라는 것이다. 취약한 페이지를 찾았고, 다크웹에서 정보를 봤고, 스캐너가 결과를 냈고, AI가 공격 절차를 알려줬다고 해서 그 행동이 정당화되지는 않는다. 보안 공부를 시작할수록 더 많은 것을 볼 수 있으므로, 판단 절차도 함께 가져야 한다.</p>
                    <table>
                      <thead><tr><th>상황</th><th>멈춰야 하는 질문</th><th>권장 행동</th></tr></thead>
                      <tbody>
                        <tr><td>학교·회사 사이트에서 취약해 보이는 기능 발견</td><td>명시적으로 진단 허가를 받았는가?</td><td>추가 탐색을 멈추고 담당 창구나 멘토에게 제보 방법을 확인한다.</td></tr>
                        <tr><td>검색 중 내부 문서나 개인정보가 노출됨</td><td>내가 이 내용을 열람할 업무상 필요가 있는가?</td><td>내용을 복사·공유하지 않고 노출 사실과 위치만 안전하게 보고한다.</td></tr>
                        <tr><td>AI가 공격 코드나 우회 방법을 제시함</td><td>허가된 실습 환경에서 검증하는가?</td><td>CTF, 워게임, 내부 승인 범위 안에서만 실행한다.</td></tr>
                        <tr><td>랜섬웨어·다크웹 자료를 더 찾아보고 싶음</td><td>호기심이 범죄 도구 접근으로 넘어가고 있지 않은가?</td><td>개념·보고서 수준에서 학습하고 실제 거래·접촉은 하지 않는다.</td></tr>
                      </tbody>
                    </table>
                    """,
                },
                {
                    "heading": "사이버 안보와 국가배우 위협",
                    "body": """
                    <p>강의 후반부는 사이버 안보로 넘어간다. 드라마나 영화에 나오는 교통, 전력, 통신, 금융 시스템 마비가 과장이 아니라 현실의 기반시설 위협과 연결될 수 있다고 설명했다. 알려지지 않은 취약점을 쓰는 공격은 방어자가 미리 알기 어렵기 때문에 더 위험하다.</p>
                    <p>국가정보원법에 사이버 안보 관련 정보가 포함된다는 점도 언급되었다. 국가정보원, 과기정통부, KISA, 경찰, 군, 외교 분야 등은 모두 사이버 안보 생태계의 일부가 될 수 있고, 화이트햇 교육생들이 장래에 들어갈 수 있는 분야이기도 하다.</p>
                    <table>
                      <thead><tr><th>행위자</th><th>주된 목적</th><th>강의에서 본 특징</th></tr></thead>
                      <tbody>
                        <tr><td>국가배우 해킹 조직</td><td>첩보, 영향력 행사, 기반시설 교란</td><td>국가 지원을 받아 은밀하게 움직이며 추적과 공개가 어렵다.</td></tr>
                        <tr><td>국제 해킹 범죄 조직</td><td>수익 창출, 협박, 정보 판매</td><td>랜섬웨어, 계정 정보, 취약점 접근권 판매 등 생태계가 형성되어 있다.</td></tr>
                        <tr><td>연계·위장 사례</td><td>귀속 추적 혼란</td><td>랜섬웨어가 실제 공격 주체를 가리는 포장지처럼 쓰일 수 있다.</td></tr>
                      </tbody>
                    </table>
                    """,
                },
                {
                    "heading": "랜섬웨어와 공격 주체 식별",
                    "body": """
                    <p>강사는 랜섬웨어 조직이 단순히 한두 명의 범죄자가 아니라, 결제, 협박, 데이터 판매, 접근권 거래가 얽힌 산업처럼 움직인다고 설명했다. 일부 조직은 학교나 병원은 공격하지 않는다는 식의 자체 규칙을 말하기도 하지만, 범죄 행위라는 본질은 바뀌지 않는다.</p>
                    <p>또 국가배우 조직과 범죄 조직을 엄격히 나누기 어려운 단계에 왔다고 했다. 예를 들어 특정 국가가 기존 랜섬웨어 도구를 사서 마지막 단계에 사용하면 겉으로는 유명 랜섬웨어 조직의 공격처럼 보일 수 있다. 그래서 프로파일링과 귀속 판단은 기술, 정보, 법, 국제 공조가 결합되어야 한다.</p>
                    """,
                },
                {
                    "heading": "질문 문화와 과정 완주",
                    "body": """
                    <p>강의 중간중간 질문을 적극적으로 하라는 메시지가 반복되었다. “멍청한 질문은 없다”는 태도는 화이트햇 과정 전체를 버티는 데 중요하다. 질문을 하면서 틀려도 되고, 대답도 하면서 서로 배워야 한다는 것이 강사의 주문이었다.</p>
                    <p>마지막 메시지는 주말을 반납해 공부하는 만큼 지금 해야 할 일을 먼저 하라는 것이었다. 과정은 6개월 동안 이어지고, 혼자 버티는 것이 아니라 멘토와 동료에게 도움을 요청하면서 끝까지 완주해야 한다. 이 강의에는 별도 과제가 없다고 안내되었다.</p>
                    """,
                },
            ],
            "checks": [
                "사이버 보안과 사이버 안보를 같은 말로 처리하면 어떤 관점이 빠지는가?",
                "업무상 볼 수 있는 정보와 실제로 봐도 되는 정보를 어떻게 구분할 수 있는가?",
                "랜섬웨어 이름만 보고 공격 주체를 단정하기 어려운 이유는 무엇인가?",
                "강사의 커리어 사례가 개발, 국가기관, 법률 판단을 하나로 연결해 보여주는 지점은 무엇인가?",
                "취약해 보이는 공개 페이지를 발견했을 때 추가 탐색 전에 확인해야 할 질문은 무엇인가?",
            ],
        },
        {
            "id": "1-2",
            "title": "컴퓨터 구조 I 실습",
            "subtitle": "GitHub Codespaces에서 데이터 표현과 C 컴파일 과정을 직접 확인하며 온라인 컴퓨터 구조 강의를 보강한다.",
            "tags": ["2026-06-13", "2교시", "컴퓨터 구조", "컴파일", "이현재"],
            "transcript_path": "오프라인 강의/0613-2.txt",
            "objectives": [
                "GitHub Codespaces를 이용해 빠르게 실습 환경을 만드는 흐름을 이해한다.",
                "자료형 크기, 값 범위, 오버플로우, 비트 연산을 컴퓨터의 데이터 표현과 연결한다.",
                "전처리, 컴파일, 어셈블, 링킹, 오브젝트 파일 확인 도구의 역할을 정리한다.",
            ],
            "sections": [
                {
                    "heading": "실습 환경과 수업 방식",
                    "body": """
                    <p>이 강의는 온라인 컴퓨터 구조 수업에서 배운 내용을 직접 확인하는 실습으로 진행되었다. 강사는 먼저 GitHub 계정을 준비하게 한 이유가 <strong>GitHub Codespaces</strong>를 쓰기 위해서였다고 설명했다. 로컬에 WSL, 가상머신, 리눅스 개발환경을 따로 만들지 않아도 브라우저 기반으로 실습을 시작할 수 있기 때문이다.</p>
                    <p>강의 중에는 무리하게 따라 치다가 내용을 놓치기보다, 지금은 설명을 듣고 나중에 과제와 복습으로 다시 입력해 보라고 안내했다. 수업 흐름은 환경 세팅, 데이터 표현 실습, 컴파일 과정 실습으로 이어졌다.</p>
                    """,
                },
                {
                    "heading": "자료형 크기와 값 범위",
                    "body": """
                    <p>첫 실습 주제는 C 언어 자료형의 크기와 표현 범위였다. <code>int</code>가 보통 4바이트라는 사실에서 멈추지 않고, <code>int8_t</code>, <code>int16_t</code>처럼 필요한 크기의 정수형을 선택할 수 있다는 점을 확인했다.</p>
                    <p>강사는 값의 범위를 외우는 것이 시험용 지식에만 머무르지 않는다고 했다. 크래시 로그나 디버깅 화면에서 익숙한 숫자, 예를 들어 32비트 정수의 최댓값 근처 값이 나오면 어떤 자료형 문제가 있는지 감을 잡는 데 도움이 된다.</p>
                    <table>
                      <thead><tr><th>확인 항목</th><th>실습 의미</th><th>보안·디버깅 연결</th></tr></thead>
                      <tbody>
                        <tr><td><code>sizeof</code></td><td>자료형이 메모리에서 차지하는 크기 확인</td><td>구조체, 파일 포맷, 네트워크 패킷 해석의 기초</td></tr>
                        <tr><td>값의 최댓값·최솟값</td><td>표현 가능한 수의 경계 확인</td><td>오버플로우와 언더플로우 원인 추적</td></tr>
                        <tr><td>고정 폭 정수형</td><td>필요한 크기의 자료형 선택</td><td>플랫폼 차이를 줄여 예측 가능한 동작 확보</td></tr>
                      </tbody>
                    </table>
                    """,
                },
                {
                    "heading": "경계값 실험을 디버깅 감각으로 바꾸기",
                    "body": f"""
                    <p>원문에서는 <code>limits.h</code>를 이용해 최댓값과 최솟값을 쉽게 가져오고, 그 값에 1을 더하거나 빼며 오버플로우와 언더플로우를 직접 확인하는 흐름이 나온다. 이 실습의 목적은 숫자를 외우는 것이 아니라, 이상한 값이 로그에 찍혔을 때 “자료형 범위를 넘었나?”라고 의심하는 감각을 만드는 것이다.</p>
                    <p>예를 들어 signed char의 최댓값은 127이고, 그 상태에서 1을 더하면 128이 아니라 음수 쪽으로 돌아갈 수 있다. 반대로 최솟값에서 1을 빼면 양수 쪽으로 감기는 현상이 보인다. 이런 감각은 취약점 분석, 파일 포맷 해석, 네트워크 패킷 파싱, 임베디드 장비 디버깅에서 모두 도움이 된다.</p>
                    {integer_boundary_code}
                    <div class="callout">실습 포인트: 결과 숫자만 보지 말고 “왜 이 자료형에서는 이 값이 더 이상 표현되지 않는가?”를 비트 수와 부호 비트 관점으로 설명해 본다.</div>
                    """,
                },
                {
                    "heading": "오버플로우와 비트 연산",
                    "body": """
                    <p>오버플로우는 자료형이 표현할 수 있는 범위를 넘어서면서 값이 의도와 다르게 바뀌는 현상으로 다뤄졌다. 강의에서는 유튜브 조회수 사례, 네이버 날씨처럼 큰 수를 다루는 서비스 사례를 언급하며, 파이썬이나 자바스크립트처럼 타입을 덜 의식하는 언어에 익숙하면 놓치기 쉽다고 했다.</p>
                    <p>이어 C 프로그램으로 <strong>AND</strong>, <strong>OR</strong> 같은 비트 연산을 직접 확인했다. 정수 값과 문자 값이 같은 바이트를 어떻게 다르게 해석하는지도 함께 다뤘다. 숫자 61이 문자로 보일 때의 느낌을 통해, 컴퓨터는 결국 비트열을 맥락에 따라 다르게 해석한다는 점을 잡는다.</p>
                    <div class="diagram three-col">
                      <div><span class="node-title">값</span><p>정수, 문자, 포인터처럼 소스 코드에서 보이는 의미</p></div>
                      <div><span class="node-title">비트열</span><p>메모리에 저장되는 실제 0과 1의 배열</p></div>
                      <div><span class="node-title">해석</span><p>자료형, 명령어, 디버거가 같은 비트를 다른 의미로 읽는다.</p></div>
                    </div>
                    """,
                },
                {
                    "heading": "C 컴파일 파이프라인",
                    "body": """
                    <p>마지막 기술 실습은 C 소스가 실행 파일이 되는 과정을 직접 나누어 보는 것이었다. 전처리 결과, 어셈블리, 오브젝트 파일, 실행 파일을 각각 만들고, 파일을 열었을 때 왜 텍스트처럼 보이지 않는지도 확인했다.</p>
                    <p>오브젝트 파일은 그냥 텍스트 편집기로 열 수 없고, <code>readelf</code>, 헥스 에디터, <code>objdump</code> 같은 도구로 구조를 봐야 한다. 강사는 오브젝트 파일이 <strong>relocatable</strong>하다는 점, strip 여부에 따라 심볼 테이블과 디버깅 정보가 남거나 사라질 수 있다는 점을 중요하게 짚었다.</p>
                    <div class="timeline">
                      <div><strong>전처리</strong><p>헤더 포함과 매크로 처리를 거쳐 컴파일러가 볼 소스 형태를 만든다.</p></div>
                      <div><strong>컴파일</strong><p>C 코드를 어셈블리 언어로 바꾼다.</p></div>
                      <div><strong>어셈블</strong><p>어셈블리 언어를 오브젝트 파일로 만든다.</p></div>
                      <div><strong>링킹</strong><p>오브젝트 파일과 라이브러리를 묶어 실행 파일을 만든다.</p></div>
                    </div>
                    """,
                },
                {
                    "heading": "오브젝트 파일을 보는 도구와 strip의 의미",
                    "body": f"""
                    <p>강의 원문에서 강사는 오브젝트 파일을 일반 텍스트 파일처럼 열어 보면 제대로 보이지 않는다고 설명했다. 오브젝트 파일은 실행 파일이 되기 전의 중간 산출물이고, 아직 재배치 가능한 형태다. 그래서 <code>readelf</code>는 ELF 헤더와 섹션을 보고, <code>objdump</code>는 디스어셈블이나 섹션 내용을 보는 데 쓴다.</p>
                    <p><code>strip</code> 여부도 중요하다. not stripped 상태에는 심볼 테이블과 디버깅 정보가 남아 있어 분석과 디버깅이 쉽지만, 배포 바이너리에서는 정보 노출을 줄이기 위해 제거할 수 있다. 리버싱, 시스템 해킹, 보안 제품 분석에서는 “무엇이 남아 있고 무엇이 제거되었는가”가 난이도를 크게 바꾼다.</p>
                    {compile_pipeline_commands}
                    <table>
                      <thead><tr><th>도구</th><th>주로 보는 것</th><th>보안 학습 연결</th></tr></thead>
                      <tbody>
                        <tr><td><code>file</code></td><td>파일 종류, 아키텍처, strip 여부</td><td>분석 대상을 빠르게 분류한다.</td></tr>
                        <tr><td><code>readelf</code></td><td>ELF 헤더, 섹션, 심볼</td><td>리눅스 바이너리 구조를 이해한다.</td></tr>
                        <tr><td><code>objdump</code></td><td>어셈블리와 섹션 내용</td><td>기계어 수준 동작을 추적한다.</td></tr>
                        <tr><td><code>strip</code></td><td>심볼·디버깅 정보 제거</td><td>배포와 분석 난이도의 차이를 이해한다.</td></tr>
                      </tbody>
                    </table>
                    """,
                },
                {
                    "heading": "과제와 복습 포인트",
                    "body": """
                    <p>과제는 수업에서 만든 환경과 예제를 다시 확인하도록 설계되었다. GitHub Codespaces로 개발 환경을 만들고, 오버플로우 예제를 언더플로우 예제로 바꾸며, 비트 연산 프로그램의 일부 함수를 구현하는 식으로 복습하게 된다.</p>
                    <p>강의 말미에는 보안 제품 개발자로서의 경험도 소개되었다. 리눅스 환경에서 동작하는 보안 제품을 만들고, 반도체 생산 장비 같은 제한된 환경에서는 무거운 시그니처 엔진보다 경량화된 보안 제품이 필요할 수 있다는 설명이 이어졌다.</p>
                    <ul class="check-list">
                      <li>실습 환경은 빠르게 만들되, 각 명령이 만든 파일의 의미를 다시 확인한다.</li>
                      <li>자료형 경계값은 단순 암기가 아니라 디버깅 힌트로 본다.</li>
                      <li>컴파일 과정의 중간 산출물을 도구로 확인해 실행 파일이 만들어지는 흐름을 몸으로 익힌다.</li>
                    </ul>
                    """,
                },
                {
                    "heading": "학습 조언",
                    "body": """
                    <p>강사는 AI를 학습 보조 도구로 쓰는 방법도 이야기했다. 모르는 단어 하나에서 시작해 파생 질문을 이어가며 본인이 원하는 깊이까지 들어가는 방식은 요즘 시대의 공부법이 될 수 있다. 다만 AI가 대신 공부해 주는 것이 아니라, 질문의 깊이를 스스로 조절해야 한다.</p>
                    <p>또 컴퓨터 공부에는 정해진 커리큘럼이 잘 보이지 않아 이쪽저쪽으로 흔들리기 쉽다고 했다. 그래서 질문을 많이 하고, 작은 난이도 조절을 하며, 체력과 지속성을 함께 챙기라는 조언이 이어졌다.</p>
                    """,
                },
            ],
            "checks": [
                "오브젝트 파일을 일반 텍스트처럼 열면 제대로 보이지 않는 이유를 설명할 수 있는가?",
                "전처리, 컴파일, 어셈블, 링킹이 각각 무엇을 만드는지 구분할 수 있는가?",
                "오버플로우와 언더플로우를 자료형의 표현 범위와 연결해 설명할 수 있는가?",
                "경계값 실험 결과를 디버깅 로그나 크래시 원인 추정에 어떻게 활용할 수 있는가?",
                "readelf, objdump, strip이 각각 바이너리 분석에서 어떤 단서를 주는가?",
            ],
        },
        {
            "id": "1-3",
            "title": "웹해킹 원리",
            "subtitle": "웹해킹 기술 자체보다 해커가 기술을 대하는 태도, AI 시대의 학습법, 허가된 실습의 경계를 정리한다.",
            "tags": ["2026-06-13", "3교시", "웹해킹", "SQL Injection", "정도원"],
            "transcript_path": "오프라인 강의/0613-3.txt",
            "objectives": [
                "웹해킹 학습에서 기술 이해와 윤리적 경계가 함께 필요한 이유를 정리한다.",
                "AI 도구를 사용할 때 개념 이해 없이 실행만 맡기면 생기는 위험을 설명한다.",
                "SQL Injection 실습을 통해 취약점 개념, 안전한 코드, 허가된 환경의 차이를 구분한다.",
            ],
            "sections": [
                {
                    "heading": "강의의 톤과 보안 유지",
                    "body": """
                    <p>웹해킹 원리 강의는 기초 기술을 세세하게 설명하기보다, 현업자가 해줄 수 있는 이야기와 교훈을 전달하는 방식으로 시작했다. 강사는 화이트햇 스쿨의 강의와 실습은 메모와 질문은 괜찮지만, 외부 공유는 조심해야 한다고 먼저 밝혔다.</p>
                    <p>보안 유지가 잘 되는 기수일수록 멘토들이 더 깊은 현장 이야기를 해줄 수 있다는 설명도 있었다. 즉 강의 내용을 어떻게 다루는지도 학습 공동체의 신뢰를 만든다.</p>
                    """,
                },
                {
                    "heading": "해커가 먹고사는 여러 방식",
                    "body": """
                    <p>강의는 해커가 꼭 한 가지 형태로 일하지 않는다는 점을 보여줬다. 민간 보안, 취약점 연구, 버그바운티, 침해사고 대응, 국가가 배후에 있는 공격자, 범죄 생태계 등 서로 다른 맥락이 존재한다.</p>
                    <p>우크라이나 전쟁 전후의 사이버 공격, 암호화폐 채굴 악성코드, 조직화된 사이버 범죄, 국가배우 공격자 이야기를 통해 웹해킹은 단순한 웹 폼 조작이 아니라 사회·정치·경제의 실제 사건과 연결된다고 설명했다.</p>
                    <table>
                      <thead><tr><th>맥락</th><th>예시</th><th>학습자가 얻어야 할 관점</th></tr></thead>
                      <tbody>
                        <tr><td>민간 보안</td><td>서비스 취약점 분석, 버그바운티, 보안 리뷰</td><td>허가된 범위와 보고 절차를 지킨다.</td></tr>
                        <tr><td>국가·전쟁</td><td>기반시설 공격, 선전, 정보 수집</td><td>기술이 물리 세계와 안보에 영향을 줄 수 있음을 본다.</td></tr>
                        <tr><td>범죄 생태계</td><td>악성코드, 암호화폐 채굴, 데이터 탈취</td><td>기술 호기심이 범죄로 연결되는 지점을 경계한다.</td></tr>
                      </tbody>
                    </table>
                    """,
                },
                {
                    "heading": "취약점 폭증과 AI 시대의 학습 압박",
                    "body": """
                    <p>녹취에서는 최근 CVE와 취약점 보고가 크게 늘어난 흐름도 언급된다. 강사는 2024년 이후 취약점 수가 눈에 띄게 증가했고, AI 때문에 코드 생산과 취약점 탐색 속도가 함께 빨라졌다고 설명했다. 그래서 이제는 모든 취약점을 똑같이 외우거나 따라가는 방식이 아니라, 어떤 취약점이 실제로 의미 있는지 선별하는 능력이 중요해진다.</p>
                    <p>이 대목은 웹해킹 학습 방향과도 연결된다. XSS, SQL Injection, 파일 업로드, 서비스 거부처럼 이름만 많이 아는 것보다, 각 취약점이 어떤 전제에서 성립하고 어떤 피해로 이어지며 어떤 방어 원칙으로 막히는지를 이해해야 한다. AI가 취약점 설명을 빠르게 제공하더라도, 위험도를 판단하고 맥락을 붙이는 일은 학습자가 해야 한다.</p>
                    <table>
                      <thead><tr><th>AI 시대 변화</th><th>학습자가 해야 할 일</th><th>잘못된 학습 방식</th></tr></thead>
                      <tbody>
                        <tr><td>취약점 정보와 예제가 빠르게 늘어남</td><td>공격 조건, 영향, 방어 원칙을 분류한다.</td><td>페이로드 문자열만 외운다.</td></tr>
                        <tr><td>AI가 풀이와 코드를 바로 제시함</td><td>풀이가 왜 맞는지 검증하고 실패 조건을 찾는다.</td><td>개념 없이 결과만 제출한다.</td></tr>
                        <tr><td>현업에서도 자동화 도구가 늘어남</td><td>도구 결과를 재현하고 우선순위를 정한다.</td><td>스캐너 결과를 그대로 믿는다.</td></tr>
                      </tbody>
                    </table>
                    """,
                },
                {
                    "heading": "기술이 물리 세계에 닿는 순간",
                    "body": """
                    <p>강사는 보안 취약점이 디지털 화면 안에서만 끝나지 않는다고 했다. 심장박동기, 자동차, 게임 경기 중단, 기반시설 공격처럼 취약점이 사람의 생명, 이동, 산업, 문화 활동까지 영향을 줄 수 있다.</p>
                    <p>그래서 웹해킹을 배울 때도 “재미로 해본다”는 태도만으로 접근하면 위험하다. 취약점 하나가 실제 서비스와 사람에게 어떤 피해로 이어지는지 상상할 수 있어야 한다.</p>
                    <div class="callout">핵심 태도: 실습은 재미있어도, 현실 서비스에서 같은 행동을 허가 없이 반복하면 사고가 된다.</div>
                    """,
                },
                {
                    "heading": "AI 시대의 해킹 학습",
                    "body": """
                    <p>강사는 AI를 무조건 쓰지 말라는 쪽보다는, 개념을 모른 채 풀이만 맡기지 말라고 설명했다. 버퍼가 무엇인지, SQL Injection이 어떤 논리 흐름인지 모르는 상태에서 AI가 문제를 풀어주면 학습 의미가 줄어든다.</p>
                    <p>반대로 기본 개념을 알고 있다면 AI의 진행 과정을 보며 “이 부분이 이상하다”는 감각을 잡을 수 있다. AI에게 일을 시키더라도 사람이 기술의 위험과 의도를 판단해야 한다는 점이 반복되었다.</p>
                    """,
                },
                {
                    "heading": "키워드를 얻고 스스로 파고드는 방법",
                    "body": """
                    <p>강의에서 중요한 학습법은 “정답을 바로 얻기”보다 “좋은 키워드를 얻기”였다. 예를 들어 subdomain takeover라는 말을 처음 들었다면, 그 단어로 HackerOne 글이나 공격 시나리오를 찾아보고, 어떤 조건에서 발생하며 어떤 서비스 설정 실수와 연결되는지 파고드는 식이다.</p>
                    <p>이 방식은 대학원, 버그바운티, 취업 준비에도 이어진다. 강사는 학벌이나 스펙보다 실제로 잘하는 것이 중요하다고 했고, 잘한다는 것은 대화를 하거나 실습을 시켜 보면 드러난다고 했다. 따라서 포트폴리오에는 “무엇을 했다”보다 “어떤 키워드를 어떻게 확장했고, 어떤 원리와 한계를 알게 됐는가”가 들어가야 한다.</p>
                    <div class="timeline compact">
                      <div><strong>키워드 수집</strong><p>강의, 블로그, 보고서에서 모르는 용어를 기록한다.</p></div>
                      <div><strong>공격 조건 정리</strong><p>이 취약점이 성립하려면 어떤 설정·입력·권한이 필요한지 쓴다.</p></div>
                      <div><strong>방어 원칙 연결</strong><p>검증, 권한 확인, 격리, 모니터링 중 무엇으로 막는지 연결한다.</p></div>
                      <div><strong>허가된 재현</strong><p>CTF, 워게임, 로컬 실습에서만 확인하고 실제 서비스에는 시도하지 않는다.</p></div>
                    </div>
                    """,
                },
                {
                    "heading": "SQL Injection 실습의 의미",
                    "body": f"""
                    <p>실습은 게시판 형태의 허가된 환경에서 진행되었다. 글 작성, 수정, 삭제, 읽기 기능이 있고 특정 파라미터에서 SQL Injection이 가능한 구조를 이용해 비밀글을 읽는 미션이었다.</p>
                    <p>정리에서 중요한 것은 공격 문자열을 외우는 것이 아니라, 사용자 입력이 SQL 문장의 구조를 바꾸지 못하게 해야 한다는 점이다. 그래서 방어 코드에서는 문자열 결합 대신 파라미터 바인딩을 쓴다.</p>
                    {safe_query_example}
                    <p>강의의 메시지는 허가된 실습 환경에서는 취약점 원리를 익히되, 실제 서비스에서는 같은 시도를 하지 않는다는 것이다. 허가 범위가 다르면 같은 기술도 학습이 아니라 침해가 된다.</p>
                    """,
                },
                {
                    "heading": "스펙보다 실력, 키워드보다 방향",
                    "body": """
                    <p>강의 후반부 질의응답에서는 대학원, 연구원, 산업계, 스펙, AI 시대의 채용 이야기가 이어졌다. 강사는 괜찮은 조직에는 이미 실력 있는 사람이 있고, 대화나 실습을 조금만 시켜 봐도 실제 역량은 드러난다고 말했다.</p>
                    <p>중요한 것은 특정 스펙을 쌓는 것보다 키워드를 얻고, 그 키워드에서 다음 질문으로 넘어가며, 기술의 원리와 부작용을 얼추라도 이해하는 것이다. AI가 발전해도 보안에서는 일을 안전하게 시키고 판단할 기술자가 필요하다는 결론으로 이어졌다.</p>
                    """,
                },
                {
                    "heading": "강의 기록과 비공개 메모의 경계",
                    "body": """
                    <p>질의응답에서는 강의 내용을 개인 블로그나 비공개 노션에 정리해도 되는지에 가까운 질문도 나온다. 강사는 개인 학습용 정리는 가능하더라도, 화이트햇 강의에서 들은 현장 이야기나 민감한 내부 맥락을 외부에 공개하는 것은 조심해야 한다고 했다. 이 말은 보안 커뮤니티에서 신뢰를 유지하는 기본 원칙과 연결된다.</p>
                    <p>정리할 때는 공개 가능한 일반 개념과 비공개 맥락을 분리해야 한다. 예를 들어 SQL Injection의 원리, 방어 방법, 허가된 실습에서 배운 점은 학습 기록으로 정리할 수 있지만, 특정 기관·회사·사람이 식별되는 사례, 실습 서버 주소, 공격 절차를 그대로 재현 가능한 정보는 공개 범위를 다시 확인해야 한다.</p>
                    """,
                },
            ],
            "checks": [
                "허가된 실습 환경과 실제 서비스의 경계는 무엇으로 구분되는가?",
                "AI가 취약점 풀이를 도와줄 때 사람이 최소한 알아야 할 것은 무엇인가?",
                "SQL Injection 방어에서 파라미터 바인딩이 왜 중요한가?",
                "취약점 정보가 폭증하는 시대에 페이로드 암기보다 조건과 영향 분류가 중요한 이유는 무엇인가?",
                "개인 학습 기록을 공개할 때 일반 개념과 비공개 맥락을 어떻게 분리해야 하는가?",
            ],
        },
        {
            "id": "1-4",
            "title": "프로그래밍 기초 및 응용 실습",
            "subtitle": "C 파일 입출력, JSON 처리, Git/GitHub, 정적 분석과 AST 과제를 하나의 흐름으로 연결한다.",
            "tags": ["2026-06-14", "1교시", "C 언어", "JSON", "정적 분석", "김진영"],
            "transcript_path": "오프라인 강의/0614-1.txt",
            "objectives": [
                "C에서 파일을 열고 읽고 쓰고 닫는 기본 생명주기를 설명한다.",
                "JSON Object와 JSON Array의 차이를 이해하고 C 구조체와 연결한다.",
                "정적 분석과 AST가 보안 약점 탐지 과제로 이어지는 이유를 정리한다.",
            ],
            "sections": [
                {
                    "heading": "수업 전체 흐름",
                    "body": f"""
                    <p>2일차 첫 강의는 프로그래밍 기초를 조금 더 심화한 실습으로 진행되었다. 사전에 C 언어 컴파일 환경을 준비하고, 실습 자료를 받은 뒤 파일 입출력, JSON, Git/GitHub, 정적 분석, AST 과제로 이어졌다.</p>
                    <p>강사는 파일을 읽고 쓰는 작업이 바이러스나 일반 프로그램 모두에서 많이 쓰이는 기본 동작이라고 설명했다. 파일을 열고, 읽거나 쓰고, 닫는 흐름은 단순하지만 이후 JSON과 정적 분석까지 이어지는 기반이 된다.</p>
                    {schedule_0614}
                    """,
                },
                {
                    "heading": "파일 입출력 생명주기",
                    "body": f"""
                    <p>C에서 파일 입출력은 <code>fopen</code>으로 열고, <code>fputs</code>, <code>fgetc</code>, 줄 단위 읽기 같은 함수로 처리한 뒤, <code>fclose</code>로 닫는 흐름이다. 강사는 이 짝이 맞지 않으면 당장 눈에 띄지 않아도 장시간 실행되는 프로그램에서 리소스 누수가 생길 수 있다고 설명했다.</p>
                    <p>모드는 크게 <code>r</code>, <code>w</code>, <code>a</code>를 먼저 이해하면 된다. <code>w</code>는 기존 내용을 덮어쓸 수 있으므로 조심해야 하고, 기존 내용 뒤에 붙이고 싶으면 <code>a</code>를 쓴다.</p>
                    {file_lifecycle_code}
                    <table>
                      <thead><tr><th>모드</th><th>의미</th><th>주의점</th></tr></thead>
                      <tbody>
                        <tr><td><code>r</code></td><td>읽기</td><td>파일이 없으면 열기에 실패할 수 있다.</td></tr>
                        <tr><td><code>w</code></td><td>쓰기</td><td>기존 파일 내용이 덮어써질 수 있다.</td></tr>
                        <tr><td><code>a</code></td><td>추가</td><td>기존 파일 뒤에 내용을 붙인다.</td></tr>
                      </tbody>
                    </table>
                    """,
                },
                {
                    "heading": "리소스 누수와 DoS 취약점 연결",
                    "body": f"""
                    <p>녹취에서 강사는 파일을 닫지 않으면 단순한 스타일 문제가 아니라 리소스 누수가 된다고 설명했다. 파일, 소켓, DB 연결, 동적 메모리는 모두 운영체제 관점에서 자원을 차지한다. 한두 번은 괜찮아 보여도 서버가 오래 실행되면서 누수가 반복되면 CPU와 메모리, 파일 디스크립터가 줄어들고 결국 프로그램이 멈출 수 있다.</p>
                    <p>보안 관점에서는 이 누수가 서비스 거부 취약점으로 이어질 수 있다. 공격자가 의도적으로 예외 경로나 실패 경로를 반복 호출해 닫히지 않는 리소스를 쌓게 만들면, 정상 사용자가 서비스를 쓰지 못하는 상태가 된다. 그래서 파일 입출력 예제에서도 성공 경로뿐 아니라 실패 경로와 중간 반환 경로를 함께 봐야 한다.</p>
                    {resource_leak_code}
                    <div class="callout">복습 기준: <code>fopen</code>을 찾으면 같은 함수 안에서 모든 경로가 <code>fclose</code>로 이어지는지 확인한다.</div>
                    """,
                },
                {
                    "heading": "JSON의 기본 구조",
                    "body": f"""
                    <p>두 번째 주제는 JSON이었다. JSON은 JavaScript Object Notation에서 출발했지만, 지금은 여러 언어와 프로그램 사이에서 데이터를 교환하는 대표 포맷이다. 강의에서는 key-value 구조, 중괄호로 표현하는 Object, 대괄호로 표현하는 Array를 먼저 잡았다.</p>
                    <p>Object는 이름이 붙은 값들의 묶음이고, Array는 여러 값을 순서대로 담는 구조다. Array 안에 Object가 여러 개 들어갈 수 있고, Object 안에 Array가 들어갈 수도 있다.</p>
                    {json_shape_code}
                    <div class="diagram two-col">
                      <div><span class="node-title">JSON Object</span><p><code>{{ }}</code>로 감싸며 key와 value를 가진다.</p></div>
                      <div><span class="node-title">JSON Array</span><p><code>[ ]</code>로 감싸며 여러 값이나 객체를 순서대로 담는다.</p></div>
                    </div>
                    """,
                },
                {
                    "heading": "JSON을 C 구조체로 옮기기",
                    "body": """
                    <p>강의는 단순히 JSON 문자열을 출력하는 데서 멈추지 않았다. 실제 작업에서는 JSON 안의 객체를 하나씩 꺼내 구조체 배열에 옮겨 담아야 한다. 그래서 구조체, 동적 메모리 할당, 배열 포인터까지 함께 등장했다.</p>
                    <p>핵심은 JSON Array의 길이를 구하고, 그 길이만큼 구조체 배열을 동적 할당한 뒤, 각 Object의 필드를 구조체 멤버로 옮기는 흐름이다. 이 과정은 이후 AST가 JSON 형태로 나올 때도 다시 쓰인다.</p>
                    <ul class="check-list">
                      <li>JSON 루트에서 필요한 배열을 찾는다.</li>
                      <li>배열 길이만큼 구조체 배열을 준비한다.</li>
                      <li>각 객체에서 <code>id</code>, <code>type</code> 같은 필드를 꺼내 구조체에 저장한다.</li>
                      <li>동적 할당한 메모리는 사용 후 해제한다.</li>
                    </ul>
                    """,
                },
                {
                    "heading": "Git과 GitHub를 보는 이유",
                    "body": """
                    <p>파일 입출력과 JSON을 마친 뒤에는 Git과 GitHub가 왜 등장하는지 설명했다. Git은 형상 관리 도구이고, GitHub는 저장소를 온라인에서 관리하고 공유하는 서비스다. 과제 버전 1, 2, 3처럼 파일명을 늘리는 대신, 커밋 단위로 변경 이력을 남긴다.</p>
                    <p>보안 관점에서 커밋 히스토리는 매우 유용하다. 어떤 커밋에서 빨간 줄로 삭제된 코드와 초록 줄로 추가된 코드가 보이면, 그 변경이 버그를 고쳤는지, 취약점을 만들었는지, 특정 패턴을 남겼는지 추적할 수 있다.</p>
                    <div class="timeline compact">
                      <div><strong>변경 전후 확인</strong><p>삭제된 줄과 추가된 줄을 비교해 의도를 추정한다.</p></div>
                      <div><strong>취약점 패턴 발견</strong><p>특정 함수, 조건, 예외 처리가 어떻게 바뀌었는지 본다.</p></div>
                      <div><strong>데이터셋 구축</strong><p>수정 전후 코드를 모아 자동 탐지·자동 수정 연구로 이어갈 수 있다.</p></div>
                    </div>
                    """,
                },
                {
                    "heading": "커밋 히스토리로 취약점 패턴 찾기",
                    "body": f"""
                    <p>강의 원문에서는 Jenkins 같은 유명 오픈소스 프로젝트의 커밋 히스토리를 예로 들며, 빨간 줄과 초록 줄을 보는 이유를 설명한다. 빨간 줄은 삭제된 코드, 초록 줄은 추가된 코드다. 취약점 수정 커밋을 보면 “어떤 코드가 위험했고, 어떤 검증이나 조건이 추가되었는지”를 역으로 배울 수 있다.</p>
                    <p>오픈소스 버그 헌팅을 할 때는 무작정 전체 코드를 읽기보다, vulnerability, XSS, injection 같은 키워드가 들어간 커밋을 먼저 보고 그 프로젝트에서 자주 터지는 패턴을 잡을 수 있다. 같은 XSS라도 템플릿 엔진, 입력 위치, escaping 함수, 라우팅 구조에 따라 트리거되는 방식이 달라지므로 프로젝트별 맥락이 중요하다.</p>
                    {commit_hunt_workflow}
                    <table>
                      <thead><tr><th>커밋에서 볼 것</th><th>왜 중요한가</th><th>정적 분석 과제와 연결</th></tr></thead>
                      <tbody>
                        <tr><td>삭제된 취약 코드</td><td>실제 버그가 어떤 형태였는지 알 수 있다.</td><td>탐지할 AST 패턴 후보가 된다.</td></tr>
                        <tr><td>추가된 검증 코드</td><td>프로젝트가 선택한 방어 방식을 알 수 있다.</td><td>자동 수정 또는 경고 메시지 설계에 도움된다.</td></tr>
                        <tr><td>테스트 추가 여부</td><td>재발 방지를 어떻게 확인하는지 알 수 있다.</td><td>탐지 결과 검증 기준을 만든다.</td></tr>
                      </tbody>
                    </table>
                    """,
                },
                {
                    "heading": "정적 분석과 AST 과제",
                    "body": f"""
                    <p>마지막 핵심은 정적 분석이었다. 정적 분석은 프로그램을 직접 실행하지 않고 코드 형태와 메타데이터를 보고 취약점 또는 보안 약점이 있을 가능성을 계산하는 방식이다. 테스트 케이스로 특정 메소드를 실행하는 동적 분석과 다르게, 컴파일 후 얻을 수 있는 구조를 분석한다.</p>
                    <p>강의에서 AST는 작성한 코드를 통일된 트리 구조로 바꾼 결과로 설명되었다. 사람마다 띄어쓰기, 변수명, 줄 배치는 다르지만 AST로 바뀌면 구조를 기준으로 패턴을 찾을 수 있다. 그래서 AST가 JSON으로 표현되고, 앞에서 배운 JSON 처리가 과제로 이어진다.</p>
                    {ast_pattern_code}
                    <p>과제는 AST 구조 분석기 제작과 버그 패턴 탐지 맛보기로 안내되었다. 기본 항목은 PDF 설명 중심이고, 가산점 성격으로 오픈소스에서 버그 패턴을 탐지해 보는 방향이 제시되었다.</p>
                    """,
                },
                {
                    "heading": "AST 과제를 수행하는 단계",
                    "body": """
                    <p>AST 과제는 “코드를 트리로 바꾼다”는 설명에서 끝나면 막막하다. 실제로는 소스 코드, AST JSON, 탐지 규칙, 결과 보고를 분리해 생각하면 된다. 사람이 보기에는 변수명과 줄바꿈이 달라도 AST에서는 함수 호출, 조건문, 대입문 같은 구조가 드러난다.</p>
                    <table>
                      <thead><tr><th>단계</th><th>해야 할 일</th><th>실수하기 쉬운 점</th></tr></thead>
                      <tbody>
                        <tr><td>입력 준비</td><td>분석할 C 소스와 AST로 변환된 JSON을 준비한다.</td><td>소스 문자열만 검색하면 공백·주석·변수명에 흔들린다.</td></tr>
                        <tr><td>구조 읽기</td><td>함수 호출, 인자, 대입, 조건문 노드를 구분한다.</td><td>JSON Object와 Array 계층을 혼동한다.</td></tr>
                        <tr><td>패턴 정의</td><td>위험 함수나 검증 누락 조건을 규칙으로 만든다.</td><td>함수 이름 하나만 보면 오탐이 많아진다.</td></tr>
                        <tr><td>결과 설명</td><td>어떤 노드 때문에 위험하다고 판단했는지 근거를 남긴다.</td><td>탐지 결과만 출력하고 이유를 쓰지 않는다.</td></tr>
                      </tbody>
                    </table>
                    """,
                },
            ],
            "checks": [
                "파일을 열고 닫지 않았을 때 어떤 종류의 문제가 누적될 수 있는가?",
                "JSON Object와 JSON Array를 C 구조체와 배열에 어떻게 대응할 수 있는가?",
                "정적 분석에서 AST가 소스 문자열보다 다루기 좋은 이유는 무엇인가?",
                "리소스 누수가 서비스 거부 취약점으로 이어질 수 있는 흐름을 설명할 수 있는가?",
                "취약점 수정 커밋의 빨간 줄과 초록 줄을 보고 어떤 버그 패턴을 뽑을 수 있는가?",
            ],
        },
        {
            "id": "1-5",
            "title": "해커의 프로그래밍",
            "subtitle": "해커의 태도, 자동화, Python 웹 스크래핑, 동적 페이지 처리, 데이터 시각화를 실습 자료와 함께 정리한다.",
            "tags": ["2026-06-14", "2교시", "해커의 프로그래밍", "Python", "김민철"],
            "transcript_path": "오프라인 강의/0614-2.txt",
            "objectives": [
                "해커를 문제 해결자이자 문제를 찾는 사람으로 설명한다.",
                "requests, BeautifulSoup, tqdm, Selenium을 쓰는 실습 흐름을 정리한다.",
                "댓글 데이터를 계정별·시간대별로 분석하고 시각화하는 이유를 이해한다.",
            ],
            "sections": [
                {
                    "heading": "해커의 정의와 태도",
                    "body": f"""
                    <p>강의자료는 해커를 단순히 침입하는 사람으로 설명하지 않는다. 해커는 주어진 문제 해결을 넘어 문제를 찾고, 내부까지 파고들어 원리를 이해하며, 본인의 배경지식으로 임기응변을 적용하는 사람으로 정리된다.</p>
                    <p>강사는 본인의 군 사이버, 공군본부 CERT, 대통령경호처, 국방과학연구소, Quora 경력과 대회 경험을 소개하면서, 보안 커리어도 기업 보안, 방산, 국방, 연구, 실전 공격·방어 등 여러 갈래가 있음을 설명했다.</p>
                    {slide_hacker}
                    """,
                },
                {
                    "heading": "자동화와 DIY 정신",
                    "body": f"""
                    <p>해커의 프로그래밍에서 중요한 태도는 “이것도 자동화 가능할까?”라는 질문이다. 자동화는 시간을 줄이는 효율도 있지만, 코드가 대신 일하는 모습을 보는 만족감도 있다. 강사는 20분짜리 일을 2초로 줄이는 프로그램을 2시간 들여 만들고 만족하는 프로그래머 농담을 예로 들었다.</p>
                    <p>다만 자동화는 기존 도구를 무시하고 모든 바퀴를 다시 만들라는 뜻은 아니다. 이미 좋은 라이브러리가 있으면 쓰되, 필요한 기능이 없거나 지원이 멈췄거나 기능을 조합해야 하면 직접 뜯어서 만들 수 있어야 한다.</p>
                    {slide_automation}
                    {slide_programming}
                    """,
                },
                {
                    "heading": "실습 환경 구축",
                    "body": f"""
                    <p>실습은 Python 기반으로 진행되며, 파일은 GitHub의 실습 저장소에서 내려받는 흐름이었다. 패키지 관리는 전통적인 <code>pip</code>와 최근 많이 쓰이는 <code>uv</code>를 비교했고, 수업에서는 uv 기반으로 의존성을 관리했다.</p>
                    <p>VS Code를 쓰는 경우 Code Runner 확장을 언급했지만 필수는 아니라고 했다. 중요한 것은 실습 코드를 실행하고, 결과를 보고, 필요한 패키지를 설치하는 기본 흐름을 잡는 것이다.</p>
                    {slide_environment}
                    """,
                },
                {
                    "heading": "requests와 BeautifulSoup",
                    "body": f"""
                    <p>첫 실습은 <strong>requests</strong>로 브라우저 없이 HTTP 요청을 보내고 HTML 응답을 그대로 출력하는 것이다. 브라우저 화면 대신 서버가 준 원문을 보면, 웹페이지가 데이터와 태그로 구성되어 있음을 직접 확인할 수 있다.</p>
                    {requests_code}
                    {slide_requests}
                    <p>다음 실습은 <strong>BeautifulSoup</strong>으로 HTML에서 원하는 요소를 추출하는 것이다. 개발자 도구에서 selector를 복사해 제목, 작성자, 댓글처럼 필요한 정보만 뽑는 흐름으로 이어졌다.</p>
                    {bs4_code}
                    {slide_bs4}
                    """,
                },
                {
                    "heading": "HTTP와 selector를 보는 사고방식",
                    "body": """
                    <p>강의에서는 HTTP를 “브라우저 주소창에 주소를 넣으면 서버로 요청이 가고 화면 정보가 돌아오는 흐름”으로 풀어 설명한다. 이 설명이 중요한 이유는 웹 스크래핑이 화면을 긁는 일이 아니라, 요청과 응답을 이해하는 일이라는 점 때문이다. 브라우저 없이도 같은 URL에 요청을 보내면 HTML 원문을 받을 수 있고, 그 안에서 필요한 태그를 선택할 수 있다.</p>
                    <p>개발자 도구에서 selector를 복사해 쓰는 실습은 편리하지만, selector가 너무 구조에 의존하면 페이지가 조금만 바뀌어도 깨진다. 따라서 처음에는 복사한 selector로 시작하더라도, 나중에는 클래스명, 링크 구조, 텍스트 패턴처럼 더 안정적인 기준을 찾아야 한다.</p>
                    <table>
                      <thead><tr><th>관찰 대상</th><th>확인할 질문</th><th>실무 감각</th></tr></thead>
                      <tbody>
                        <tr><td>URL</td><td>페이지 번호나 게시글 번호가 어디에 들어가는가?</td><td>반복 수집 범위를 설계한다.</td></tr>
                        <tr><td>HTML</td><td>제목, 작성자, 댓글이 어떤 태그와 클래스에 들어가는가?</td><td>selector를 만든다.</td></tr>
                        <tr><td>네트워크 요청</td><td>댓글이 HTML에 바로 있는가, 나중에 API로 불러오는가?</td><td>requests로 충분한지 Selenium이 필요한지 판단한다.</td></tr>
                      </tbody>
                    </table>
                    """,
                },
                {
                    "heading": "댓글 수집, 진행률, 동적 페이지",
                    "body": f"""
                    <p>목록 1페이지부터 10페이지까지 게시글 제목을 모으고, 각 게시글 댓글을 전부 수집하는 실습에서는 반복 작업의 진행 상황을 보여주는 <strong>tqdm</strong>이 등장했다. 오래 걸리는 코드가 어디까지 진행됐는지 보이는 것은 실무에서도 중요하다.</p>
                    <p>댓글이 정적 HTML에 없고 브라우저가 나중에 불러오는 구조라면, 단순 <code>requests.get()</code>만으로는 부족하다. 이때 Selenium으로 브라우저를 실제로 제어하면서 페이지가 동작한 뒤의 결과를 읽을 수 있다.</p>
                    {scraping_pipeline_code}
                    {selenium_code}
                    {slide_selenium}
                    """,
                },
                {
                    "heading": "진행률 표시는 디버깅 도구다",
                    "body": """
                    <p>원문에서 tqdm은 결과를 바꾸는 기능이 아니라 “잘 돌고 있는지 보는 장치”로 설명된다. 1~2분짜리 실습에서는 없어도 되지만, 20분 또는 몇 시간 걸리는 수집 작업에서는 진행률이 없으면 멈춘 것인지 정상 진행 중인지 알기 어렵다. 보안 자동화에서도 긴 스캔, 로그 분석, 대량 파일 처리에는 관찰 가능성이 필요하다.</p>
                    <p>그래서 자동화 코드를 만들 때는 결과 파일만 만들지 말고, 현재 몇 번째 대상을 처리 중인지, 실패한 요청은 몇 개인지, 재시도했는지, 중간 저장은 되는지까지 고려해야 한다. 이는 단순 편의 기능이 아니라 실무에서 장애와 누락을 줄이는 품질 요소다.</p>
                    <ul class="check-list">
                      <li>반복 대상 개수와 현재 진행 위치를 표시한다.</li>
                      <li>실패한 요청은 조용히 버리지 말고 별도 목록에 남긴다.</li>
                      <li>오래 걸리는 수집은 중간 결과를 저장해 재시작 가능하게 만든다.</li>
                      <li>서버에 부담을 주지 않도록 요청 간격과 범위를 제한한다.</li>
                    </ul>
                    """,
                },
                {
                    "heading": "데이터 처리와 시각화",
                    "body": f"""
                    <p>수집한 댓글 정보는 계정별로 정리하고, 계정마다 댓글을 몇 개 썼는지 계산한다. 여기서 끝나면 단순 카운트지만, 요일과 시간대를 함께 보면 특정 계정이 언제 활동하는지 더 잘 보인다.</p>
                    <p>강의자료는 Datasaurus Dozen을 통해 평균, 분산, 상관계수가 같아도 데이터 형태는 완전히 다를 수 있음을 보여준다. 그래서 보안 데이터 분석에서도 숫자 요약만 믿지 말고 시각화로 패턴을 확인해야 한다.</p>
                    {heatmap_code}
                    {slide_datasaurus}
                    {slide_visualize}
                    {slide_result}
                    """,
                },
                {
                    "heading": "봇 계정 활동 패턴을 찾는 관점",
                    "body": """
                    <p>강의 원문에서는 SNS 댓글과 여론 조작, 자동화된 계정 활동 이야기가 이어진다. 핵심은 댓글 내용만 읽는 것이 아니라 활동 시각과 반복성을 보는 것이다. 사람은 잠을 자고, 주중·주말 패턴이 다르고, 특정 시간대에 몰리는 경향이 있다. 반면 자동화 계정은 매시간 일정하게 움직이거나, 사람이 보기 어려운 시간대에도 규칙적으로 활동할 수 있다.</p>
                    <p>댓글 데이터를 계정별·요일별·시간대별로 시각화하면 “많이 쓴 사람”과 “사람답지 않게 쓴 사람”을 구분할 실마리를 얻는다. 이 관점은 CTF의 misc 문제, OSINT, 위협 인텔리전스, 로그 기반 이상 탐지와도 연결된다.</p>
                    <table>
                      <thead><tr><th>패턴</th><th>사람 활동 가능성</th><th>자동화 의심 포인트</th></tr></thead>
                      <tbody>
                        <tr><td>매일 비슷한 생활 시간대에 집중</td><td>높음</td><td>내용·빈도와 함께 추가 확인</td></tr>
                        <tr><td>24시간 매시간 일정량 활동</td><td>낮음</td><td>예약 작업 또는 봇 가능성</td></tr>
                        <tr><td>특정 이슈 직후 여러 계정이 동시에 활동</td><td>상황에 따라 다름</td><td>조직적 증폭 여부 확인</td></tr>
                      </tbody>
                    </table>
                    """,
                },
                {
                    "heading": "AI와 Git을 쓰는 방식",
                    "body": """
                    <p>질의응답에서는 AI와 개발 방식도 다뤘다. 강사는 AI에게 코드를 맡기더라도, 무엇을 원하는지 정확히 표현해야 한다고 했다. 예를 들어 “한 시간에 글 10개 제한”도 고정 시간 창인지, 최근 1시간 rolling window인지에 따라 구현이 달라진다.</p>
                    <p>AI가 코드를 바꿨을 때는 Git diff를 통해 빨간 줄과 초록 줄을 보며 무엇이 바뀌었는지 확인해야 한다. Git을 많이 알 필요는 없더라도 <code>git add</code>, <code>git commit</code>, <code>git push</code>와 변경 확인 습관은 중요하다고 설명했다.</p>
                    """,
                },
            ],
            "checks": [
                "해커의 프로그래밍에서 자동화가 단순 효율 이상의 의미를 갖는 이유는 무엇인가?",
                "requests와 Selenium은 각각 어떤 상황에서 적합한가?",
                "댓글 수만 세는 것보다 요일·시간대별 heatmap을 보는 것이 왜 유용한가?",
                "긴 수집 작업에서 tqdm이나 중간 저장 같은 관찰 가능성이 왜 디버깅 도구가 되는가?",
                "사람 계정과 봇 계정의 활동 패턴을 시간대 데이터로 구분할 때 어떤 신호를 볼 수 있는가?",
            ],
        },
        {
            "id": "1-6",
            "title": "개인정보보호법",
            "subtitle": "해킹과 보안 공부에서 반드시 알아야 할 개인정보, 접근 권한, 정보통신망법, 저작권 경계를 정리한다.",
            "tags": ["2026-06-14", "3교시", "개인정보보호법", "정보통신망법", "이유진"],
            "transcript_path": "오프라인 강의/0614-3.txt",
            "objectives": [
                "개인정보보호법의 목적과 개인정보의 범위를 이해한다.",
                "IDOR, 공개 연락처 크롤링, CCTV 얼굴정보처럼 애매한 사례를 법적 관점으로 검토한다.",
                "허가된 해킹 실습과 불법 접근의 차이를 정보통신망법 관점에서 정리한다.",
            ],
            "sections": [
                {
                    "heading": "해커에게 법 수업이 필요한 이유",
                    "body": """
                    <p>개인정보보호법 강의는 “해커에게 듣는 교양 수업”처럼 진행되었다. 강사는 보안 공부를 하면서 내가 하는 행동이 법적으로 어떤 의미를 갖는지 인지하고 가는 것이 목표라고 했다.</p>
                    <p>강사의 이력은 보안 연구원에서 로스쿨, 변호사, 게임 회사 사내변호사로 이어진다. 그래서 기술을 아는 사람이 법을 설명하는 방식으로, 개인정보보호법뿐 아니라 해킹과 관련된 법적 경계 전반을 다뤘다.</p>
                    """,
                },
                {
                    "heading": "수업을 여는 네 가지 그레이존 질문",
                    "body": """
                    <p>강의 원문에서 강사는 처음부터 애매한 질문들을 던진다. 아이디는 개인정보인가, URL 숫자를 바꿨더니 다른 사람 정보가 보이면 해킹인가, CCTV에 찍힌 얼굴은 개인정보인가, GitHub나 개인 웹사이트에 공개된 연락처는 마음대로 크롤링해도 되는가 같은 질문이다. 이 질문들은 모두 보안 공부를 하다 실제로 마주칠 수 있는 회색지대다.</p>
                    <p>강의의 목표는 법 조항을 외우는 것이 아니라 “하면 안 되는 것을 아는 것”이다. 기술적으로 보이는 것, 공개되어 있는 것, 클릭 한 번으로 접근되는 것과 법적으로 허용되는 것은 다르다. 그래서 개인정보보호법 강의는 실습을 줄이는 수업이 아니라, 실습을 오래 하기 위해 필요한 안전장치다.</p>
                    <table>
                      <thead><tr><th>질문</th><th>핵심 판단 기준</th><th>보안 공부에서의 의미</th></tr></thead>
                      <tbody>
                        <tr><td>아이디도 개인정보인가?</td><td>다른 정보와 결합해 특정 개인을 알아볼 수 있는지</td><td>로그·계정 데이터를 가볍게 다루면 안 된다.</td></tr>
                        <tr><td>URL 숫자만 바꿨는데 보이면 괜찮은가?</td><td>나에게 허용된 접근 권한 범위인지</td><td>IDOR는 “그냥 보였다”로 끝나지 않는다.</td></tr>
                        <tr><td>CCTV 얼굴은 개인정보인가?</td><td>살아 있는 개인을 식별할 수 있는 영상정보인지</td><td>영상·이미지도 개인정보 처리 대상이 될 수 있다.</td></tr>
                        <tr><td>공개 연락처 크롤링은 자유로운가?</td><td>공개 목적과 예측 가능한 이용 범위 안인지</td><td>공개 정보도 대량 수집·판매는 별도 문제가 된다.</td></tr>
                      </tbody>
                    </table>
                    """,
                },
                {
                    "heading": "개인정보보호법의 목적과 정보주체 권리",
                    "body": """
                    <p>개인정보보호법은 개인정보를 함부로 수집하거나 팔거나 목적 외로 쓰지 못하게 하는 법이다. 최근 흐름은 개인정보를 가진 사람, 즉 정보주체의 권리를 더 명확하게 보장하는 방향으로 발전하고 있다.</p>
                    <p>열람청구권, 삭제 요구, 처리정지 요구처럼 정보주체가 적극적으로 요구할 수 있는 권리가 언급되었다. 주민등록번호는 특히 강하게 보호되는 정보이고, 이름, 연락처, 주소처럼 직접 식별 가능한 정보뿐 아니라 다른 정보와 결합해 식별 가능한 정보도 개인정보가 될 수 있다.</p>
                    <table>
                      <thead><tr><th>개념</th><th>의미</th><th>강의에서 본 예</th></tr></thead>
                      <tbody>
                        <tr><td>개인정보</td><td>살아 있는 개인을 알아볼 수 있는 정보</td><td>이름, 전화번호, 주소, 주민등록번호</td></tr>
                        <tr><td>결합 가능 정보</td><td>다른 정보와 쉽게 결합해 개인을 알아볼 수 있는 정보</td><td>아이디, 위치, 활동 기록, 계정 패턴</td></tr>
                        <tr><td>정보주체 권리</td><td>본인 정보의 열람, 삭제, 처리정지를 요구할 권리</td><td>웹사이트가 보유한 내 정보를 확인하거나 삭제 요청</td></tr>
                      </tbody>
                    </table>
                    """,
                },
                {
                    "heading": "수집, 이용, 제공, 파기의 생애주기",
                    "body": f"""
                    <p>개인정보 처리는 생애주기로 이해할 수 있다. 쇼핑몰 가입 예시처럼 이름, 주소, 전화번호를 수집하고, 보관하고, 배송에 이용하고, 택배사에 제공 또는 위탁한 뒤, 목적이 끝나면 파기하는 흐름이다.</p>
                    <p>대부분의 처리는 동의를 기준으로 하지만, 계약 이행에 꼭 필요한 처리처럼 별도 동의를 매번 받기 어려운 경우도 있다. 코로나 시기 동선 공개처럼 공공의 안전을 위한 긴급한 근거도 설명되었다.</p>
                    {privacy_lifecycle_code}
                    """,
                },
                {
                    "heading": "동의와 목적 제한",
                    "body": """
                    <p>동의는 단순히 체크박스를 받은 것으로 끝나지 않는다. 누가, 어떤 목적으로, 어떤 정보를, 어디에 쓰는지 명확해야 한다. 홈플러스 경품 행사 사례처럼 경품 응모 정보를 보험사 마케팅 자료로 판매하는 식의 목적 외 이용은 문제가 된다.</p>
                    <p>공개된 정보도 아무렇게나 쓸 수 없다. GitHub나 개인 웹사이트에 연락처를 올린 사람은 연락을 받기 위해 공개한 것이지, 대규모 데이터베이스로 만들어 취업 사이트에 판매하라고 공개한 것은 아닐 수 있다. 공개 목적과 예측 가능성을 벗어나면 법적 문제가 생길 수 있다.</p>
                    <div class="callout">공개 정보 판단: 공개되어 있다는 사실보다, 공개한 사람이 예상할 수 있는 사용 목적 안에 있는지가 중요하다.</div>
                    """,
                },
                {
                    "heading": "동의가 유효하려면 보여야 하는 것",
                    "body": """
                    <p>홈플러스 경품 행사 사례에서 중요한 지점은 “동의를 받았다고 주장할 수 있는가”가 아니라 “정보주체가 무엇에 동의하는지 실제로 알 수 있었는가”다. 경품 응모라고 생각하고 정보를 냈는데, 아주 작은 글씨로 보험사 마케팅 제공이 숨어 있었다면 정보주체 입장에서는 목적을 제대로 알기 어렵다.</p>
                    <p>따라서 동의는 목적, 항목, 제공받는 자, 보유 기간, 거부 가능성과 불이익이 분명해야 한다. 보안 서비스나 버그바운티 플랫폼을 만들 때도 개인정보를 수집한다면 같은 원칙이 적용된다. “약관에 써두었다”는 말만으로는 충분하지 않을 수 있다.</p>
                    <table>
                      <thead><tr><th>동의 요소</th><th>질문</th><th>위험한 설계</th></tr></thead>
                      <tbody>
                        <tr><td>목적</td><td>왜 수집하는가?</td><td>가입 목적처럼 보이지만 마케팅·판매 목적을 숨긴다.</td></tr>
                        <tr><td>항목</td><td>어떤 정보를 받는가?</td><td>필요 이상으로 주민번호, 위치, 연락처를 요구한다.</td></tr>
                        <tr><td>제공·위탁</td><td>누구에게 넘어가는가?</td><td>택배사 위탁과 제3자 판매를 섞어 설명한다.</td></tr>
                        <tr><td>보유 기간</td><td>언제 지우는가?</td><td>목적 종료 후에도 무기한 보관한다.</td></tr>
                      </tbody>
                    </table>
                    """,
                },
                {
                    "heading": "가명정보와 익명정보",
                    "body": """
                    <p>강의에서는 가명정보와 익명정보도 다뤘다. 가명정보는 일부 식별자를 바꾸거나 제거해도 다른 정보와 결합하면 다시 개인을 알아볼 가능성이 남아 있는 정보다. 익명정보는 합리적으로 고려했을 때 더 이상 특정 개인을 알아보기 어려운 상태여야 한다.</p>
                    <p>복구 키를 제거한다고 자동으로 익명정보가 되는 것은 아니다. 시간, 비용, 기술을 합리적으로 고려해 결합 가능성이 남아 있으면 여전히 가명정보로 볼 수 있다. AI 학습에 가명정보를 쓰는 문제는 과학적 연구 목적과 사전 검토 이슈로 이어졌다.</p>
                    <table>
                      <thead><tr><th>구분</th><th>핵심</th><th>주의점</th></tr></thead>
                      <tbody>
                        <tr><td>개인정보</td><td>개인을 직접 또는 결합으로 식별 가능</td><td>수집·이용·제공 근거가 필요하다.</td></tr>
                        <tr><td>가명정보</td><td>추가 정보와 결합하면 식별 가능성이 남음</td><td>복구 키 제거만으로 익명정보가 되지 않는다.</td></tr>
                        <tr><td>익명정보</td><td>합리적으로 개인을 알아보기 어려움</td><td>충분한 익명 처리 판단이 필요하다.</td></tr>
                      </tbody>
                    </table>
                    """,
                },
                {
                    "heading": "IDOR와 정보통신망법",
                    "body": """
                    <p>해킹 공부와 직접 연결되는 쟁점은 URL 파라미터를 바꿨더니 다른 사람 정보가 보이는 경우다. 인증을 우회한 느낌이 없어도 객관적으로 접근 권한 제한이 있었다면 허용된 접근 권한을 넘은 것으로 볼 수 있다.</p>
                    <p>정보통신망법은 시스템이 정상적으로 운영되도록 보호하고, 허용되지 않은 접근이나 침해 행위를 처벌하는 규정을 둔다. 그래서 CTF, 워게임, 버그바운티처럼 허가된 환경에서는 실습이 되지만, 일반 서비스에서 같은 행동을 하면 침해가 될 수 있다.</p>
                    <div class="diagram two-col">
                      <div><span class="node-title">허가된 실습</span><p>범위, 목적, 대상, 규칙이 명확하다. 문제를 풀어도 되는 승낙이 있다.</p></div>
                      <div><span class="node-title">무단 접근</span><p>보이면 봐도 된다는 뜻이 아니다. 권한 제한을 넘으면 위법 위험이 있다.</p></div>
                    </div>
                    """,
                },
                {
                    "heading": "해킹하다 안 잡혀가기: 법률 지형도",
                    "body": """
                    <p>강사는 개인정보보호법만이 아니라 정보통신망법, 통신비밀보호법, 형법, 신용정보법, 부정경쟁방지법, 저작권법까지 언급했다. 보안 실습은 여러 법률의 경계에 걸릴 수 있기 때문이다. 예를 들어 개인정보를 수집하면 개인정보보호법, 시스템에 무단 접근하면 정보통신망법, 통신 내용을 엿보면 통신비밀보호법, 비밀 자료를 열람하면 형법상 비밀침해 문제가 될 수 있다.</p>
                    <p>따라서 좋은 판단 순서는 “어떤 법 조항이 몇 조인가”를 외우는 것보다, 내가 하려는 행동이 수집인지, 접근인지, 감청인지, 복제인지, 공개인지 먼저 나누는 것이다. 이 분류가 되면 멘토, 담당자, 법무팀, 버그바운티 운영자에게 무엇을 물어봐야 하는지도 명확해진다.</p>
                    <table>
                      <thead><tr><th>행동 유형</th><th>주로 연결되는 법 영역</th><th>안전한 접근</th></tr></thead>
                      <tbody>
                        <tr><td>개인정보 수집·이용·제공</td><td>개인정보보호법</td><td>목적, 동의, 보관, 파기 근거를 확인한다.</td></tr>
                        <tr><td>권한 없는 시스템 접근</td><td>정보통신망법</td><td>허가된 범위와 대상만 테스트한다.</td></tr>
                        <tr><td>통신 내용 엿보기</td><td>통신비밀보호법</td><td>패킷·로그 분석 권한과 범위를 문서화한다.</td></tr>
                        <tr><td>게임·캐릭터·세계관 활용</td><td>저작권법</td><td>원 저작물 기반 수익화 여부를 확인한다.</td></tr>
                      </tbody>
                    </table>
                    """,
                },
                {
                    "heading": "좋은 해커와 창작물 경계",
                    "body": """
                    <p>강사는 좋은 해커를 단순히 빠르고 똑똑한 사람으로만 보지 않았다. 내가 만든 기술을 다른 사람이 어떻게 안전하게 쓸 수 있는지, 위험을 어떻게 줄일지, 어떻게 설명해야 할지 고민하는 사람이 오래 함께 일할 수 있는 해커라고 했다.</p>
                    <p>마지막 질의응답에서는 AI와 저작권 이야기도 나왔다. LLM으로 글을 썼다는 사실 자체보다, 쿠키런 같은 기존 작품의 설정, 캐릭터, 세계관을 소재로 수익화하면 2차적 저작물 문제가 생길 수 있다. 해킹뿐 아니라 창작과 AI 사용에서도 원 권리자의 권리를 생각해야 한다.</p>
                    """,
                },
            ],
            "checks": [
                "아이디나 공개 연락처가 언제 개인정보 또는 개인정보 처리 이슈가 될 수 있는가?",
                "IDOR처럼 파라미터만 바꿨는데 정보가 보이는 상황도 왜 위험한가?",
                "가명정보와 익명정보를 복구 키 유무만으로 구분하면 안 되는 이유는 무엇인가?",
                "유효한 동의가 되려면 목적, 항목, 제공받는 자, 보유 기간이 어떻게 보여야 하는가?",
                "보안 실습 중 내가 하려는 행동이 수집, 접근, 감청, 복제 중 어디에 가까운지 분류해야 하는 이유는 무엇인가?",
            ],
        },
    ]
