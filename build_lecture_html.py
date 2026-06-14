from __future__ import annotations

import html
import re
from html.parser import HTMLParser
from pathlib import Path
from textwrap import dedent

from course_data.computer_architecture_1 import build_computer_architecture_1_lectures
from course_data.cryptography_basic import build_cryptography_basic_lectures
from course_data.ethics_cyber_security import build_ethics_cyber_security_lectures
from course_data.hackers_programming import build_hackers_programming_lectures
from course_data.latest_security_trend import build_latest_security_trend_lectures
from course_data.modern_web_dev_security import build_modern_web_dev_security_lectures
from course_data.network_basic import build_network_basic_lectures
from course_data.os_basic import build_os_basic_lectures
from course_data.secure_coding import build_secure_coding_lectures


ROOT = Path(__file__).resolve().parent
COURSE_ROOT = ROOT / "courses"
ASSET_DIR = ROOT / "assets"
STT_ROOT = ROOT / "stt"
PUBLIC_OPERATIONAL_PATTERNS = [
    "STT",
    "자동 전사",
    "전사 내용",
    "전사되어",
    "전사에서는",
    "전사 흐름",
    "전사 잡음",
    "반복 전사",
    "정돈본",
    "자료 기준",
    "작성 기준",
    "파일 기준",
    "외부 인터넷 자료",
    "HTML 본문",
    "스크린샷 기준",
    "문장과 문단",
    "접이식",
    "텍스트만",
    "사용자가 요청한",
    "하단에는",
    "문맥상",
]
REPEATED_TRANSCRIPT_PHRASES = [
    "다음 영상에서 만나요",
    "바로 이어서 진행하겠습니다",
    "수고하셨습니다",
    "감사합니다",
]
EMPHASIS_TERMS = (
    "Software Development Life Cycle",
    "도메인별 표준",
    "소프트웨어 품질",
    "품질 기준",
    "품질 매트릭",
    "국제 표준",
    "스마트 팩토리",
    "스마트 헬스케어",
    "헬스 인포메틱스",
    "SDLC",
    "Planning",
    "Analysis",
    "Design",
    "Implementation",
    "Testing",
    "Deployment",
    "Maintenance",
    "Agile",
    "Waterfall",
    "스프린트",
    "유지보수성",
    "복구성",
    "효율성",
    "신뢰성",
    "재사용성",
    "보안성",
    "Maintainability",
    "Recoverability",
    "Efficiency",
    "Reliability",
    "Reusability",
    "Security",
    "오픈소스 소프트웨어",
    "MIT 라이선스",
    "Apache 2.0",
    "소스 공개 의무",
    "동일 라이선스",
    "상업적 이용",
    "요구사항 명세서",
    "Information Architecture",
    "서비스 정책",
    "개발 정책",
    "와이어프레임",
    "WBS",
    "프로젝트 이해관계자",
    "프로젝트 일정",
    "프로젝트 결과물",
    "C 언어",
    "컴파일러",
    "Visual Studio Code",
    "GCC",
    "MinGW",
    "변수",
    "상수",
    "자료형",
    "const",
    "short",
    "int",
    "long",
    "char",
    "unsigned char",
    "printf",
    "형식 지정자",
    "입력",
    "출력",
    "I/O",
    "scanf",
    "fgets",
    "sprintf",
    "fputs",
    "조건문",
    "if",
    "else if",
    "else",
    "switch case",
    "반복문",
    "for",
    "while",
    "do while",
    "초기식",
    "조건식",
    "증감식",
    "함수",
    "반환형",
    "매개변수",
    "return",
    "배열",
    "중첩 반복문",
    "포인터",
    "call by value",
    "call by reference",
    "주소",
    "문자열",
    "null 문자",
    "string.h",
    "strcpy",
    "strlen",
    "strcmp",
    "strcat",
    "버퍼 오버플로우",
    "동적 메모리",
    "stack",
    "heap",
    "malloc",
    "calloc",
    "realloc",
    "memset",
    "free",
    "구조체",
    "typedef",
    "멤버 변수",
    "컴퓨터 구조",
    "컴퓨터 시스템",
    "CPU",
    "중앙처리장치",
    "제어장치",
    "연산장치",
    "레지스터",
    "메모리",
    "입출력",
    "주기억장치",
    "보조기억장치",
    "입출력장치",
    "버스",
    "데이터 버스",
    "주소 버스",
    "제어 버스",
    "명령어 사이클",
    "인출",
    "해독",
    "실행",
    "인터럽트",
    "8비트",
    "비트",
    "바이트",
    "2진수",
    "10진수",
    "16진수",
    "보수",
    "부동소수점",
    "ASCII",
    "유니코드",
    "캐시 메모리",
    "가상 메모리",
    "RAM",
    "ROM",
    "운영체제",
    "커널",
    "시스템 호출",
    "프로세스",
    "스레드",
    "파일 시스템",
    "리눅스",
    "우분투",
    "가상머신",
    "클라우드",
    "CLI",
    "GUI",
    "쉘",
    "배시",
    "패키지",
    "데몬",
    "서비스",
    "권한",
    "사용자 계정",
    "그룹",
    "root",
    "sudo",
    "프로세스 관리",
    "모니터링",
    "로그",
    "환경 변수",
    "환경변수",
    "PATH",
    "systemd",
    "apt",
    "cron",
    "쉘 스크립트",
    "네트워크",
    "인터넷",
    "프로토콜",
    "계층 구조",
    "OSI 7계층",
    "TCP/IP",
    "물리 계층",
    "데이터 링크 계층",
    "네트워크 계층",
    "트랜스포트 계층",
    "애플리케이션 계층",
    "이더넷",
    "MAC 주소",
    "ARP",
    "IP 주소",
    "서브넷",
    "라우팅",
    "ICMP",
    "TCP",
    "UDP",
    "포트",
    "소켓",
    "HTTP",
    "DNS",
    "TLS",
    "Wireshark",
    "패킷",
    "캡처",
    "3-way handshake",
    "혼잡 제어",
    "흐름 제어",
    "암호학",
    "평문",
    "암호문",
    "암호화",
    "복호화",
    "대칭키 암호",
    "공개키 암호",
    "기밀성",
    "무결성",
    "인증",
    "부인방지",
    "해시 함수",
    "메시지 인증 코드",
    "전자서명",
    "인증서",
    "PKI",
    "RSA",
    "AES",
    "DES",
    "블록 암호",
    "스트림 암호",
    "난수",
    "키 교환",
    "Diffie-Hellman",
    "시큐어 코딩",
    "보안 약점",
    "취약점",
    "공격 유형",
    "OWASP Top 10",
    "입력 검증",
    "접근 통제",
    "권한 관리",
    "SQL Injection",
    "XSS",
    "SSRF",
    "경로 조작",
    "파일 업로드",
    "에러 처리",
    "예외 처리",
    "API 오용",
    "경쟁 상태",
    "Race Condition",
    "세션 관리",
    "보안 기능",
    "안전한 코딩",
    "위협 모델링",
    "리스크",
    "퍼징",
    "정보보안윤리",
    "사이버 안보",
    "사이버 위협",
    "사이버 전쟁",
    "국가 사이버 안보체계",
    "국가 사이버 안보 전략",
    "정보보호",
    "개인정보",
    "해킹",
    "악성코드",
    "랜섬웨어",
    "피싱",
    "APT",
    "사회공학",
    "제로데이",
    "보안 거버넌스",
    "침해사고",
    "대응 체계",
    "법제도",
    "국가 기반시설",
    "주요 정보통신 기반시설",
    "제로트러스트",
    "Zero Trust",
    "AI 보안",
    "생성형 AI",
    "클라우드 보안",
    "블록체인",
    "스마트 컨트랙트",
    "가상자산",
    "사이버 테러",
    "인간중심보안",
    "보안 인식",
    "최소 권한",
    "마이크로 세그멘테이션",
    "멀티팩터 인증",
    "MFA",
    "CASB",
    "CSPM",
    "DevSecOps",
    "공급망 보안",
    "해커의 프로그래밍",
    "Python",
    "파이썬",
    "Base64",
    "웹 스크래핑",
    "BeautifulSoup",
    "requests",
    "API",
    "API 키",
    "n8n",
    "워크플로우 자동화",
    "개인정보 유출",
    "데이터 결합",
    "가상자산 믹싱",
    "거래 그래프",
    "OSINT",
    "정보 그래프",
    "정규표현식",
    "JSON",
    "CSV",
    "크롤링",
)
EMPHASIS_BLOCK_TAGS = {"p", "li", "td"}
EMPHASIS_SKIP_TAGS = {"a", "b", "button", "code", "h1", "h2", "h3", "option", "pre", "script", "select", "strong", "style", "summary", "textarea"}
EMPHASIS_MAX_PER_BLOCK = 2
EMPHASIS_STOPWORDS = {
    "강의",
    "개요",
    "기초",
    "방법",
    "문법",
    "복습",
    "실습",
    "정리",
    "총정리",
    "활용",
}


def code_block(source: str, lang: str = "c") -> str:
    return f'<pre><code class="language-{lang}">{html.escape(dedent(source).strip())}</code></pre>'


def image_figure(src: str, title: str, note: str) -> str:
    return f"""
    <figure class="screen-figure">
      <a href="{html.escape(src, quote=True)}" target="_blank" rel="noopener">
        <img src="{html.escape(src, quote=True)}" alt="{html.escape(title, quote=True)}" loading="lazy">
      </a>
      <figcaption>
        <strong>{html.escape(title)}</strong>
        <span>{html.escape(note)}</span>
      </figcaption>
    </figure>
    """


def screen_figure(course_id: str, lecture_stem: str, image_no: int, title: str, note: str) -> str:
    image_name = f"{lecture_stem} - {image_no:04d}.jpg"
    src = f"../../../../videos/common-development/{course_id}/{lecture_stem}/{image_name}"
    return image_figure(src, title, note)


def clean_transcript_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text.strip())
    for phrase in REPEATED_TRANSCRIPT_PHRASES:
        pattern = rf"(?:{re.escape(phrase)}[.!?！。]*\s*){{2,}}"
        text = re.sub(pattern, f"{phrase}. ", text)
    return text.strip()


def validate_public_html(path: Path, content: str) -> None:
    visible_page_copy = re.sub(r'<section id="transcript"[\s\S]*?</section>', "", content)
    found = [pattern for pattern in PUBLIC_OPERATIONAL_PATTERNS if pattern in visible_page_copy]
    if found:
        joined = ", ".join(found)
        raise ValueError(f"{path} contains user-facing operational copy: {joined}")


def write_public_html(path: Path, content: str) -> None:
    validate_public_html(path, content)
    path.write_text(content, encoding="utf-8")


def reading_transcript(text: str) -> str:
    text = clean_transcript_text(text)
    text = re.sub(r"([.!?。])\s+", r"\1\n", text)
    text = re.sub(r"(요|죠|니다|세요|겁니다|입니다|됩니다)(?![.!?。])\s+", r"\1.\n", text)
    return html.escape(text)


def readable_transcript_block(text: str) -> str:
    text = reading_transcript(text)
    chunks = [chunk.strip() for chunk in text.splitlines() if chunk.strip()]
    paragraphs = []
    current = []
    current_len = 0
    for chunk in chunks:
        current.append(chunk)
        current_len += len(chunk)
        if current_len >= 520:
            paragraphs.append(" ".join(current))
            current = []
            current_len = 0
    if current:
        paragraphs.append(" ".join(current))
    return "".join(f"<p>{paragraph}</p>" for paragraph in paragraphs)


def normalize_emphasis_term(term: object) -> str:
    term = html.unescape(re.sub(r"<[^>]+>", " ", str(term)))
    term = re.sub(r"\s+", " ", term).strip(" :-–—,./·()[]")
    if len(term) < 2 or term in EMPHASIS_STOPWORDS:
        return ""
    return term


def split_candidate_terms(text: object) -> list[str]:
    plain = html.unescape(re.sub(r"<[^>]+>", " ", str(text)))
    plain = re.sub(r"\([^)]*\)", " ", plain)
    parts = re.split(r"[,·:：]|(?:\s+(?:및|그리고|와|과)\s+)", plain)
    return [part for part in (normalize_emphasis_term(part) for part in parts) if part and len(part) <= 18]


def emphasis_terms_for(lecture: dict | None = None, section: dict | None = None) -> list[str]:
    candidates: list[object] = list(EMPHASIS_TERMS)
    if lecture:
        candidates.extend(lecture.get("tags", []))
    if section:
        candidates.extend(split_candidate_terms(section.get("heading", "")))

    terms = []
    seen = set()
    for candidate in candidates:
        term = normalize_emphasis_term(candidate)
        key = term.casefold()
        if not term or key in seen:
            continue
        seen.add(key)
        terms.append(term)

    return sorted(terms, key=len, reverse=True)


def emphasis_pattern(term: str) -> re.Pattern[str]:
    escaped = re.escape(term)
    if re.fullmatch(r"[A-Za-z0-9_+.#/\- ]+", term):
        return re.compile(rf"(?<![A-Za-z0-9_+.#/\-]){escaped}(?![A-Za-z0-9_+.#/\-])", re.IGNORECASE)
    return re.compile(rf"(?<![가-힣A-Za-z0-9]){escaped}", re.IGNORECASE)


class AutoEmphasisParser(HTMLParser):
    def __init__(self, terms: list[str]):
        super().__init__(convert_charrefs=False)
        self.output: list[str] = []
        self.tag_stack: list[str] = []
        self.block_counts: list[int] = []
        self.used_terms: set[str] = set()
        self.term_patterns = [(term.casefold(), emphasis_pattern(term)) for term in terms]

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag_name = tag.lower()
        self.output.append(self.get_starttag_text() or self.rebuild_starttag(tag, attrs))
        self.tag_stack.append(tag_name)
        if tag_name in EMPHASIS_BLOCK_TAGS:
            self.block_counts.append(0)

    def handle_startendtag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        self.output.append(self.get_starttag_text() or self.rebuild_starttag(tag, attrs, closed=True))

    def handle_endtag(self, tag: str) -> None:
        tag_name = tag.lower()
        if tag_name in EMPHASIS_BLOCK_TAGS and self.block_counts:
            self.block_counts.pop()
        self.pop_tag(tag_name)
        self.output.append(f"</{tag}>")

    def handle_data(self, data: str) -> None:
        if not data.strip() or not self.emphasis_allowed():
            self.output.append(data)
            return
        self.output.append(self.emphasize_data(data))

    def handle_entityref(self, name: str) -> None:
        self.output.append(f"&{name};")

    def handle_charref(self, name: str) -> None:
        self.output.append(f"&#{name};")

    def rebuild_starttag(self, tag: str, attrs: list[tuple[str, str | None]], *, closed: bool = False) -> str:
        attr_text = "".join(
            f' {name}="{html.escape(value, quote=True)}"' if value is not None else f" {name}"
            for name, value in attrs
        )
        suffix = " /" if closed else ""
        return f"<{tag}{attr_text}{suffix}>"

    def pop_tag(self, tag: str) -> None:
        for index in range(len(self.tag_stack) - 1, -1, -1):
            if self.tag_stack[index] == tag:
                del self.tag_stack[index:]
                break

    def emphasis_allowed(self) -> bool:
        return bool(self.block_counts) and not any(tag in EMPHASIS_SKIP_TAGS for tag in self.tag_stack)

    def emphasize_data(self, data: str) -> str:
        remaining = EMPHASIS_MAX_PER_BLOCK - self.block_counts[-1]
        if remaining <= 0:
            return data

        matches = []
        for key, pattern in self.term_patterns:
            if key in self.used_terms:
                continue
            match = pattern.search(data)
            if match:
                length = match.end() - match.start()
                matches.append((match.start(), -length, match.end(), key))

        if not matches:
            return data

        selected = []
        occupied_until = -1
        for start, _negative_length, end, key in sorted(matches):
            if start < occupied_until:
                continue
            selected.append((start, end, key))
            occupied_until = end
            if len(selected) >= remaining:
                break

        if not selected:
            return data

        parts = []
        cursor = 0
        for start, end, key in selected:
            parts.append(data[cursor:start])
            parts.append(f"<strong>{data[start:end]}</strong>")
            cursor = end
            self.used_terms.add(key)
        parts.append(data[cursor:])
        self.block_counts[-1] += len(selected)
        return "".join(parts)

    def get_html(self) -> str:
        return "".join(self.output)


def emphasize_html(fragment: str, terms: list[str]) -> str:
    if not terms:
        return fragment
    parser = AutoEmphasisParser(terms)
    parser.feed(fragment)
    parser.close()
    return parser.get_html()


def emphasize_plain_text(text: object, terms: list[str]) -> str:
    wrapped = emphasize_html(f"<p>{html.escape(str(text))}</p>", terms)
    return wrapped.removeprefix("<p>").removesuffix("</p>")


def lecture_number(lecture: dict) -> int:
    return int(str(lecture["id"]).split("-")[-1])


def lesson_file_stem(lecture: dict) -> str:
    return f"lesson-{lecture_number(lecture):02d}"


def lecture_html_file(lecture: dict) -> str:
    return f"{lesson_file_stem(lecture)}.html"


def filename_part(text: str, *, keep_spaces: bool = False) -> str:
    text = re.sub(r"[\\/:*?\"<>|]+", "-", text.strip())
    text = re.sub(r"\s+", " " if keep_spaces else "-", text)
    text = re.sub(r"-+", "-", text)
    return text.strip("-")


def transcript_file_stem(course: dict, lecture: dict) -> str:
    course_name = filename_part(str(course.get("transcript_title", course["title"])), keep_spaces=True)
    lecture_title = filename_part(str(lecture.get("transcript_title", lecture["title"])))
    return f"{course_name}-{lecture_number(lecture):02d}-{lecture_title}"


def get_transcripts(course: dict) -> dict[str, str]:
    transcripts: dict[str, str] = {}
    stt_dir = STT_ROOT / str(course["track_id"]) / str(course["id"])
    for lecture in course.get("lectures", []):
        file = stt_dir / f"{transcript_file_stem(course, lecture)}.txt"
        legacy_file = stt_dir / f"{lesson_file_stem(lecture)}.txt"
        if file.exists():
            transcripts[str(lecture["id"])] = file.read_text(encoding="utf-8")
        elif legacy_file.exists():
            transcripts[str(lecture["id"])] = legacy_file.read_text(encoding="utf-8")
        else:
            transcripts[str(lecture["id"])] = ""
    return transcripts


LECTURES = [
    {
        "id": "1-1",
        "file": "lecture-1-1.html",
        "title": "산업별 소프트웨어 품질 기준",
        "subtitle": "스마트 팩토리와 스마트 헬스케어는 같은 소프트웨어라도 서로 다른 품질 기준을 요구한다.",
        "tags": ["소프트웨어 산업", "품질 기준", "국제 표준"],
        "objectives": [
            "소프트웨어 품질을 모든 산업에 같은 잣대로 평가하면 안 되는 이유를 이해한다.",
            "스마트 팩토리와 스마트 헬스케어의 품질 표준 예시를 비교한다.",
            "앞으로 어떤 분야로 가더라도 해당 분야의 표준을 확인해야 함을 정리한다.",
        ],
        "sections": [
            {
                "heading": "강의의 핵심 질문",
                "body": """
                <p>이 강의는 “도메인이 달라도 공통적인 품질 매트릭만 올리면 충분한가?”라는 질문에서 출발한다. 강의의 결론은 명확하다. 소프트웨어는 다양한 산업군에 들어가지만, 산업마다 요구하는 최소 품질 기준과 검토 관점이 다르므로 한 산업의 기준을 다른 산업에 그대로 적용하면 무리가 있다.</p>
                <div class="diagram two-col">
                  <div><span class="node-title">공통 착각</span><p>소프트웨어니까 모든 산업에 같은 품질 기준을 적용하면 될 것 같다.</p></div>
                  <div><span class="node-title">강의 결론</span><p>도메인별 표준과 품질 기준을 확인하고, 그 기준을 만족하도록 설계해야 한다.</p></div>
                </div>
                """,
            },
            {
                "heading": "스마트 팩토리의 품질 기준",
                "body": """
                <p>스마트 팩토리에도 소프트웨어가 들어간다. 다만 공장 자동화와 제조 환경에 들어가는 소프트웨어는 해당 도메인이 요구하는 품질 수준을 만족해야 한다. 강의에서는 스마트 팩토리 쪽 예시로 <strong>ISOICTR 6306-1</strong>이라는 국제 표준을 언급한다. 이 표준은 스마트 팩토리에 들어가는 소프트웨어가 최소한 어느 정도 품질을 만족한다고 판단하기 위한 가이드라인으로 설명된다.</p>
                <p>핵심은 “스마트 팩토리 소프트웨어라면 스마트 팩토리 맥락의 표준을 봐야 한다”는 점이다. 단순히 기능이 돌아가는지, 코드가 깔끔한지 같은 일반 기준만으로는 충분하지 않다.</p>
                """,
            },
            {
                "heading": "스마트 헬스케어의 품질 기준",
                "body": """
                <p>스마트 헬스케어 역시 소프트웨어가 들어가지만, 스마트 팩토리 표준을 그대로 가져다 쓰기는 어렵다. 강의에서는 헬스케어 디바이스 소프트웨어와 관련해 <strong>ISOTR 22696</strong>을 예로 들고, 이 표준이 <strong>헬스 인포메틱스</strong>라는 제목으로 만들어졌다고 설명한다.</p>
                <p>즉 헬스케어 디바이스 안에 들어가는 소프트웨어는 의료·건강 정보 처리라는 도메인 특성에 맞는 품질 정보를 만족해야 한다. 제조 현장 기준과 의료기기 기준은 위험 모델, 사용자, 실패 비용이 다르기 때문에 같은 기준으로 처리할 수 없다.</p>
                """,
            },
            {
                "heading": "정리",
                "body": """
                <ul class="check-list">
                  <li>소프트웨어 산업은 여러 산업군으로 확장되어 있고, 산업군마다 소프트웨어가 요구받는 역할이 다르다.</li>
                  <li>품질을 높인다는 말은 단순히 공통 지표만 올린다는 뜻이 아니라, 해당 도메인의 최소 품질 기준을 만족한다는 뜻까지 포함한다.</li>
                  <li>스마트 팩토리와 스마트 헬스케어는 각각 별도의 국제 표준 예시가 있을 정도로 품질 기준이 다르다.</li>
                  <li>앞으로 어떤 분야로 진출하더라도 그 분야의 표준을 확인하고, 안전한 소프트웨어를 만들 수 있어야 한다.</li>
                </ul>
                """,
            },
        ],
        "checks": [
            "스마트 팩토리 표준을 스마트 헬스케어에 그대로 쓰기 어려운 이유를 설명할 수 있는가?",
            "도메인별 최소 품질 기준을 확인해야 하는 이유를 말할 수 있는가?",
            "소프트웨어 품질이 코드 자체의 품질만 의미하지 않는다는 점을 이해했는가?",
        ],
    },
    {
        "id": "1-2",
        "file": "lecture-1-2.html",
        "title": "산업별 표준을 다시 확인하기",
        "subtitle": "1-1과 같은 주제를 반복 복습할 수 있도록 도메인별 품질 기준을 다시 정리한다.",
        "tags": ["복습", "도메인 표준", "품질 기준"],
        "objectives": [
            "도메인별 품질 기준을 다시 정리한다.",
            "스마트 팩토리와 스마트 헬스케어 예시의 차이를 반복 확인한다.",
            "표준 준수와 안전한 소프트웨어 개발의 연결고리를 복습한다.",
        ],
        "sections": [
            {
                "heading": "반복 복습 구성",
                "body": """
                <p>이 강의는 1-1에서 다룬 도메인별 품질 기준을 복습 관점으로 다시 묶는다. 새로운 개념을 무리하게 덧붙이기보다 스마트 팩토리와 스마트 헬스케어 예시를 다시 비교하면서 핵심 결론을 확실히 잡는 데 초점을 둔다.</p>
                <div class="callout">복습 포인트: 산업군이 달라지면 소프트웨어에 요구되는 품질 기준과 검토 관점도 달라진다.</div>
                """,
            },
            {
                "heading": "도메인별 품질 기준이 필요한 이유",
                "body": """
                <p>강의는 스마트 팩토리와 스마트 헬스케어를 비교하면서, 소프트웨어가 들어간다는 공통점만으로 같은 품질 기준을 적용할 수 없다고 설명한다. 각 산업군은 사용자, 운용 환경, 실패했을 때의 피해, 법적·산업적 요구가 다르다. 그래서 산업군별 표준을 확인해야 한다.</p>
                <table>
                  <thead><tr><th>도메인</th><th>강의에서 언급한 표준</th><th>의미</th></tr></thead>
                  <tbody>
                    <tr><td>스마트 팩토리</td><td>ISOICTR 6306-1</td><td>스마트 팩토리에 들어가는 소프트웨어의 최소 품질 가이드라인</td></tr>
                    <tr><td>스마트 헬스케어</td><td>ISOTR 22696</td><td>헬스 인포메틱스 관점의 헬스케어 디바이스 소프트웨어 품질 기준</td></tr>
                  </tbody>
                </table>
                """,
            },
            {
                "heading": "학생이 기억할 결론",
                "body": """
                <ul class="check-list">
                  <li>공통 품질 매트릭만 올린다고 모든 산업의 소프트웨어 품질이 보장되는 것은 아니다.</li>
                  <li>소프트웨어가 들어가는 산업군을 먼저 이해하고, 그 산업군이 요구하는 표준을 확인해야 한다.</li>
                  <li>표준 준수는 단순 문서 작업이 아니라 안전한 소프트웨어를 만들기 위한 최소 조건이다.</li>
                  <li>개발자나 보안 인력은 자신이 속한 분야의 기준을 찾아보고 따라갈 수 있어야 한다.</li>
                </ul>
                """,
            },
        ],
        "checks": [
            "1-1과 1-2가 같은 주제를 반복해서 다룬다는 점을 확인했는가?",
            "스마트 팩토리와 스마트 헬스케어의 표준 예시를 구분할 수 있는가?",
            "산업군별 표준을 확인하는 태도가 왜 중요한지 설명할 수 있는가?",
        ],
    },
    {
        "id": "1-3",
        "file": "lecture-1-3.html",
        "title": "SDLC와 프로젝트 관리 방법론",
        "subtitle": "소프트웨어를 최소한의 버그와 높은 품질로 만들기 위한 개발 생명주기와 관리 방식.",
        "tags": ["SDLC", "Agile", "Waterfall"],
        "objectives": [
            "SDLC의 여섯 단계를 순서대로 설명한다.",
            "유지보수 단계에서 새로운 요구가 생기면 다시 기획으로 돌아간다는 순환 구조를 이해한다.",
            "Agile과 Waterfall의 차이를 프로젝트 상황에 맞춰 선택할 수 있다.",
        ],
        "sections": [
            {
                "heading": "왜 개발 생명주기를 배워야 하는가",
                "body": """
                <p>취약점 분석을 하든 일반 소프트웨어를 만들든 결과물은 결국 소프트웨어다. 그래서 “어떻게 개발해야 최소한의 버그로 고품질 소프트웨어를 만들 수 있는가”를 설명하기 위해 <strong>SDLC</strong>, 즉 Software Development Life Cycle을 다룬다.</p>
                """,
            },
            {
                "heading": "SDLC 여섯 단계",
                "body": """
                <div class="timeline">
                  <div><strong>1. Planning</strong><p>무엇을 만들지, 유사 소프트웨어가 무엇인지, 큰 방향을 계획한다.</p></div>
                  <div><strong>2. Analysis</strong><p>요구사항, 페이지, 기능, 예외 등을 기술적으로 풀어 쓴다.</p></div>
                  <div><strong>3. Design</strong><p>아키텍처, 플로우차트, 예외 흐름을 시각화한다.</p></div>
                  <div><strong>4. Implementation</strong><p>실제 코드로 구현한다.</p></div>
                  <div><strong>5. Testing</strong><p>기획 요구를 얼마나 만족하는지, 버그와 취약점이 있는지 확인한다.</p></div>
                  <div><strong>6. Deployment & Maintenance</strong><p>배포 후 유지보수한다. 새 요구가 생기면 다시 Planning으로 돌아간다.</p></div>
                </div>
                <p>강의에서는 유지보수 단계에서 새로운 니즈가 발생하면 다시 1번 기획부터 사이클이 시작된다고 설명한다. 그래서 SDLC는 직선이 아니라 원형 흐름으로 이해해야 한다.</p>
                """,
            },
            {
                "heading": "Agile",
                "body": """
                <p>Agile은 하나의 방향성을 가지고 소프트웨어를 만들되, 중간중간 짧은 <strong>스프린트</strong>로 끊어서 개발하는 방식이다. 강의 예시처럼 첫 스프린트에서는 20%, 다음에는 40%, 다음에는 80%, 다음에는 100% 기능을 만족시키는 식으로 빠르게 보강한다.</p>
                <ul>
                  <li>스프린트가 짧다.</li>
                  <li>요구사항을 지속적으로 반영한다.</li>
                  <li>다양한 직군의 팀원이 짧은 주기 안에 함께 움직이므로 소통이 중요하다.</li>
                  <li>시장의 변화에 빠르게 대응해야 하거나 요구사항 변경이 자주 발생하는 서비스에 적합하다.</li>
                </ul>
                """,
            },
            {
                "heading": "Waterfall",
                "body": """
                <p>Waterfall은 처음부터 깊게 기획하고, 기획을 바탕으로 개발하고, 개발이 끝나면 테스트하는 식으로 한 단계씩 완성도 있게 넘어가는 방식이다. 강의에서는 폭포수가 한 단계씩 떨어지는 그림처럼 설명한다.</p>
                <ul>
                  <li>프로젝트 초기에 무엇을 만들고 어떤 결과물을 배포할지 명확히 파악한다.</li>
                  <li>각 단계 산출물 작성에 시간이 많이 든다.</li>
                  <li>새 요구사항이 들어와도 Agile처럼 바로 반영하지 않고, V1.1, V1.3, V2.0 같은 다음 버전에 반영하는 경우가 많다.</li>
                  <li>요구사항이 명확하고 디테일해야 하는 서비스, 큰 규모 제품, 핵심 기능 개발에 적합하다.</li>
                </ul>
                """,
            },
            {
                "heading": "선택 기준",
                "body": """
                <table>
                  <thead><tr><th>구분</th><th>Agile</th><th>Waterfall</th></tr></thead>
                  <tbody>
                    <tr><td>흐름</td><td>짧은 스프린트 반복</td><td>단계별 순차 진행</td></tr>
                    <tr><td>요구사항 변경</td><td>빠르게 반영</td><td>보통 다음 버전에서 반영</td></tr>
                    <tr><td>강점</td><td>시장 변화 대응, 빠른 보강</td><td>명확한 산출물, 디테일한 계획</td></tr>
                    <tr><td>어울리는 상황</td><td>변경이 잦은 서비스</td><td>대규모 제품, 핵심 기능, 요구가 명확한 프로젝트</td></tr>
                  </tbody>
                </table>
                <p>강의의 결론은 Agile이 좋고 Waterfall이 나쁘다는 식의 구분이 아니라, 프로젝트 상황에 맞춰 두 방법론의 특징을 떠올려 선택해야 한다는 것이다.</p>
                """,
            },
        ],
        "checks": [
            "SDLC 6단계를 순서대로 말할 수 있는가?",
            "유지보수 이후 다시 Planning으로 돌아가는 이유를 설명할 수 있는가?",
            "Agile과 Waterfall 중 요구사항이 자주 바뀌는 서비스에 더 적합한 방법론을 고를 수 있는가?",
        ],
    },
    {
        "id": "1-4",
        "file": "lecture-1-4.html",
        "title": "소프트웨어 품질 평가 방법",
        "subtitle": "여러 품질 매트릭 중 반복적으로 등장하는 핵심 항목을 골라 품질을 판단한다.",
        "tags": ["품질 매트릭", "유지보수성", "보안성"],
        "objectives": [
            "소프트웨어 품질 평가 항목이 매우 많지만 자주 겹치는 핵심 매트릭이 있음을 이해한다.",
            "유지보수성, 복구성, 재사용성, 보안성의 의미를 설명한다.",
            "보안성은 기능 동작 여부와 별개로 악의적 행위 가능성을 줄이는 품질 항목임을 이해한다.",
        ],
        "sections": [
            {
                "heading": "품질 매트릭을 보는 이유",
                "body": """
                <p>강의에서는 소프트웨어 품질을 1부터 100, 1부터 1000까지도 나열할 수 있다고 말한다. 하지만 실제로는 학계와 산업계에서 반복적으로 중요하게 보는 가중치 높은 품질 매트릭이 있다. 여러 분류 체계에는 Portability, Modifiability, Correctness, Functionality, Supportability, Functional, Portability 등 다양한 항목이 나오지만, 자세히 보면 서로 겹치는 항목이 많다.</p>
                <p>겹치는 항목을 추려 보면 최소한 유지해야 할 핵심 매트릭을 얻을 수 있고, 강의에서는 오른쪽 표에 8가지 매트릭이 정리된다고 설명한다. 특히 자세히 다룬 항목은 아래와 같다.</p>
                """,
            },
            {
                "heading": "유지보수성",
                "body": """
                <p><strong>Maintainability</strong>는 배포 이후에도 코드를 쉽게 다시 이해하고 수정할 수 있는 성질이다. 새로운 니즈가 일주일 뒤에 오면 아직 코드가 익숙해서 금방 수정할 수 있지만, 3개월, 6개월, 1년 뒤에 오면 아무리 문서화를 해도 다시 코드를 읽고 해석하는 비용이 증가한다.</p>
                <p>따라서 유지보수성이 높은 소프트웨어는 시간이 지나도 요구사항을 반영하기 쉽고, 코드를 다시 살펴보는 비용이 낮다.</p>
                """,
            },
            {
                "heading": "복구성, 효율성, 신뢰성",
                "body": """
                <p><strong>Recoverability</strong>는 서비스가 중단되었을 때 몇 초 또는 몇 분 안에 복구할 수 있는지를 보는 항목이다. 장애가 전혀 없을 수는 없으므로, 장애 이후 회복 능력도 품질의 일부가 된다.</p>
                <p>강의에서는 <strong>Efficiency</strong>와 <strong>Reliability</strong>도 품질 매트릭으로 함께 언급한다. 효율성은 제한된 자원을 얼마나 잘 쓰는가와 연결되고, 신뢰성은 기능이 기대한 대로 안정적으로 동작하는가와 연결된다.</p>
                """,
            },
            {
                "heading": "재사용성과 보안성",
                "body": """
                <p><strong>Reusability</strong>는 내가 만든 소스 코드를 다른 프로그램에서 얼마나 다시 사용할 수 있는지를 의미한다. 강의에서는 코드 서치와 결합될 수 있는 개념으로 설명한다.</p>
                <p><strong>Security</strong>는 이 강의 흐름에서 가장 집중하는 항목이다. 보안 문제는 기능 자체를 동작시키는 데는 지장이 없어 보일 수 있다. 하지만 특정 기능이 정상 동작하는 동시에 악의적인 행위를 가능하게 한다면 보안 취약점이 발생한 것이다. 따라서 기능이 “된다”는 사실과 안전하게 “된다”는 사실은 구분해야 한다.</p>
                """,
            },
            {
                "heading": "핵심 표",
                "body": """
                <table>
                  <thead><tr><th>매트릭</th><th>강의에서 정리한 의미</th><th>학생이 기억할 포인트</th></tr></thead>
                  <tbody>
                    <tr><td>Maintainability</td><td>나중에도 코드를 읽고 수정하기 쉬움</td><td>시간이 지난 뒤 요구사항을 반영하는 비용을 줄인다.</td></tr>
                    <tr><td>Recoverability</td><td>중단 후 빠르게 복구 가능</td><td>장애 후 몇 초/몇 분 안에 회복되는지가 중요하다.</td></tr>
                    <tr><td>Efficiency</td><td>자원을 효율적으로 사용</td><td>성능과 자원 사용량도 품질이다.</td></tr>
                    <tr><td>Reliability</td><td>기능이 안정적으로 동작</td><td>반복 실행해도 기대대로 동작해야 한다.</td></tr>
                    <tr><td>Reusability</td><td>다른 프로그램에서 재사용 가능</td><td>잘 나눈 코드는 다른 맥락에서도 쓸 수 있다.</td></tr>
                    <tr><td>Security</td><td>악의적 행위 가능성을 줄임</td><td>기능이 동작해도 취약하면 좋은 품질이 아니다.</td></tr>
                  </tbody>
                </table>
                """,
            },
        ],
        "checks": [
            "유지보수성이 낮으면 왜 시간이 지날수록 비용이 늘어나는가?",
            "복구성은 장애가 없다는 뜻이 아니라 무엇을 의미하는가?",
            "기능이 정상 동작해도 보안 품질이 낮을 수 있는 이유를 설명할 수 있는가?",
        ],
    },
    {
        "id": "1-5",
        "file": "lecture-1-5.html",
        "title": "오픈소스 소프트웨어와 라이선스",
        "subtitle": "공개된 코드를 가져다 쓸 때는 소스 공개, 동일 라이선스, 상업적 이용 가능성을 확인해야 한다.",
        "tags": ["OSS", "라이선스", "상업적 이용"],
        "objectives": [
            "오픈소스 소프트웨어를 사용하는 이유를 설명한다.",
            "라이선스를 확인할 때 볼 세 가지 기준을 정리한다.",
            "MIT 라이선스 예시와 Apache 2.0처럼 제약이 있을 수 있는 경우를 구분한다.",
        ],
        "sections": [
            {
                "heading": "오픈소스 소프트웨어란",
                "body": """
                <p>소프트웨어를 만들 때 처음부터 끝까지 모든 기능을 직접 만들 수도 있지만, 시간과 역량의 한계가 있다. 그래서 기존 개발자들이 많이 사용하고 인터넷에 공개적으로 사용할 수 있게 해 둔 소스 코드를 가져와 내 소프트웨어에 합칠 수 있다. 이런 소프트웨어를 <strong>오픈소스 소프트웨어</strong>, 줄여서 <strong>OSS</strong>라고 부른다.</p>
                """,
            },
            {
                "heading": "공개되어 있다고 마음대로 쓸 수 있는가",
                "body": """
                <p>강의의 질문은 “인터넷에 공개되어 있으니 원하는 대로 가져와 붙이고 돈을 벌고 공유해도 되는가?”이다. 답은 “반은 맞고 반은 틀리다”이다. 공개되어 있다는 사실과 사용 조건이 자유롭다는 사실은 다르다. 오픈소스에도 <strong>라이선스</strong>가 있고, 라이선스마다 허용 범위와 의무가 다르다.</p>
                """,
            },
            {
                "heading": "라이선스를 볼 때의 세 가지 기준",
                "body": """
                <div class="diagram three-col">
                  <div><span class="node-title">1. 소스 공개 의무</span><p>오픈소스를 가져와 만든 내 코드까지 공개해야 하는가?</p></div>
                  <div><span class="node-title">2. 동일 라이선스 적용</span><p>내 소프트웨어에도 같은 라이선스를 적용해야 하는가?</p></div>
                  <div><span class="node-title">3. 상업적 이용</span><p>이 라이선스를 사용해 만든 소프트웨어로 돈을 벌 수 있는가?</p></div>
                </div>
                <p>강의에서는 라이선스가 수십 가지 더 있지만, 최소한 이 세 기준으로 먼저 필터링하면 내 프로젝트에 적합한 오픈소스인지 판단하는 데 도움이 된다고 설명한다.</p>
                """,
            },
            {
                "heading": "MIT와 Apache 2.0 예시",
                "body": """
                <p><strong>MIT 라이선스</strong>는 강의에서 가장 자유로운 예시로 다룬다. 소스 코드 공개 의무가 없고, 동일한 라이선스를 강제로 적용하지 않아도 되며, 상업적 이용도 가능하다고 설명한다.</p>
                <p><strong>Apache 2.0</strong>은 “세 가지를 모두 완전히 풀어주는 것이 아니라 몇 가지 제약이 있다”는 예시로 언급된다. 강의의 목적은 특정 라이선스 조항을 모두 외우는 것이 아니라, 라이선스마다 조건이 다르므로 세 기준으로 먼저 판별하는 습관을 갖는 것이다.</p>
                """,
            },
            {
                "heading": "정리",
                "body": """
                <ul class="check-list">
                  <li>OSS는 개발 시간을 줄이고 기존 코드를 활용할 수 있게 해 준다.</li>
                  <li>하지만 공개되어 있다는 이유만으로 무제한 사용이 가능한 것은 아니다.</li>
                  <li>소스 공개 의무, 동일 라이선스 적용 의무, 상업적 이용 가능 여부를 먼저 확인해야 한다.</li>
                  <li>라이선스 조건이 프로젝트 목적과 맞지 않으면 품질을 높이려던 선택이 법적·운영 리스크가 될 수 있다.</li>
                </ul>
                """,
            },
        ],
        "checks": [
            "OSS를 사용하는 이유와 주의할 점을 함께 설명할 수 있는가?",
            "라이선스 판단 기준 세 가지를 말할 수 있는가?",
            "MIT 라이선스가 강의에서 어떤 예시로 사용되었는가?",
        ],
    },
    {
        "id": "1-6",
        "file": "lecture-1-6.html",
        "title": "소프트웨어 기획 프로세스와 WBS",
        "subtitle": "고품질 소프트웨어는 코드를 쓰기 전 요구, 구조, 정책, 기능, 화면을 반복 정리하는 데서 시작한다.",
        "tags": ["기획", "요구사항", "WBS"],
        "objectives": [
            "취약점 예방과 기획의 관계를 이해한다.",
            "요구사항 명세, IA, 서비스 정책, 개발 정책, 와이어프레임의 역할을 구분한다.",
            "WBS가 이해관계자, 일정, 결과물을 공유하기 위한 도구임을 이해한다.",
        ],
        "sections": [
            {
                "heading": "왜 기획이 중요한가",
                "body": """
                <p>강의는 앞선 소프트웨어 산업, 품질 평가, 오픈소스 라이선스 내용을 정리한 뒤 “소프트웨어 자체의 품질을 올리기 위해 가장 중요한 것은 기획”이라고 강조한다. 취약점은 잘못 작성된 소스 코드에서 발생하지만, 애초에 그런 코드를 작성할 필요가 없도록 요구사항과 기능 범위를 잡았다면 취약점 자체가 생기지 않았을 수 있다.</p>
                <p>따라서 프로그래밍은 머릿속 아이디어를 바로 코드로 옮기는 일이 아니라, 프로그램의 방향과 요구, 필요한 코드가 명확히 정리된 상태에서 구현으로 넘어가는 과정이다.</p>
                """,
            },
            {
                "heading": "기획 프로세스 5단계",
                "body": """
                <div class="timeline compact">
                  <div><strong>Requirement Specification</strong><p>무엇을 해야 하는지 요구를 러프하게 나열한다. 산출물은 요구사항 정의서/명세서다.</p></div>
                  <div><strong>Information Architecture</strong><p>요구별 페이지, 단계, 데이터 배치와 흐름을 정의한다. 줄여서 IA라고 한다.</p></div>
                  <div><strong>Service Policy</strong><p>회원 가입 방식, 소셜 로그인 여부처럼 사용자 경험과 서비스 운영 정책을 정한다.</p></div>
                  <div><strong>Development Policy</strong><p>요구를 만족하기 위한 실제 기능들을 하나하나 쪼개고 나열한다.</p></div>
                  <div><strong>Sketch / Wireframe</strong><p>글로 정리한 내용을 네모, 세모, 동그라미 수준으로 시각화한다. 디자인이 아니라 검토용 화면 구조다.</p></div>
                </div>
                <p>이 과정은 한 번에 끝나지 않는다. 와이어프레임을 보다가 “이 요구는 빼야겠다”, “이 데이터는 이 페이지에 있으면 안 되겠다”, “이 기능은 추가해야겠다”가 보이면 요구사항, IA, 정책서로 다시 돌아가 수정한다.</p>
                """,
            },
            {
                "heading": "요구사항 정의서",
                "body": """
                <p>요구사항 정의서는 “나 뭐 해야 돼?”를 문서화하는 단계다. 강의 예시에서는 요구사항 번호, 적용 버전, 요구사항 종류를 적는다. 종류에는 기능 요구사항, 성능 요구사항, 데이터 요구사항, 보안 요구사항 등이 들어갈 수 있다.</p>
                <table>
                  <thead><tr><th>항목</th><th>예시</th><th>의미</th></tr></thead>
                  <tbody>
                    <tr><td>요구사항 번호</td><td>고유 번호</td><td>요구를 추적하기 위한 식별자</td></tr>
                    <tr><td>적용 버전</td><td>1.0</td><td>어느 버전에 들어갈 요구인지 표시</td></tr>
                    <tr><td>요구 종류</td><td>기능, 성능, 데이터, 보안</td><td>요구의 성격 구분</td></tr>
                    <tr><td>로그인 기능</td><td>자체 로그인 화면, 추가 정보 입력, 가입 완료 및 서비스 소개 화면</td><td>기능 요구를 구체 문장으로 정리</td></tr>
                    <tr><td>수집 데이터</td><td>필요 개인정보 수준에 따라 협의</td><td>아직 결정이 필요한 부분도 문서에 남긴다.</td></tr>
                  </tbody>
                </table>
                """,
            },
            {
                "heading": "IA, 서비스 정책, 개발 정책",
                "body": """
                <p><strong>IA</strong>는 요구사항을 바탕으로 페이지와 데이터 흐름을 구체화한다. 예를 들어 앱 구동 시 나타나는 스플래시 화면, 회원 가입 화면, 소셜 회원 가입 후 추가 데이터를 입력받는 화면처럼 1뎁스부터 필요한 화면과 데이터를 나눈다.</p>
                <p><strong>서비스 정책</strong>은 회원을 어떻게 정의할지, 회원 분류를 일반 회원 하나로 둘지, V1.1이나 2.0부터 기업 회원을 둘지, 가입 방식을 소셜 로그인과 자체 로그인 중 어떻게 할지 같은 서비스 측면의 결정을 적는다. 와이어프레임을 보다가 소셜 로그인이 필요 없다고 판단되면 정책서에서 제거하고 수정 버전을 만든다.</p>
                <p><strong>개발 정책</strong>은 요구사항을 만족하기 위한 기능 목록이다. 회원 가입, 약관 동의, 인증을 위한 패스 인증, IP 인증처럼 구현 관점의 기능을 나열한다. 기능을 하나하나 쓰다 보면 해당 요구가 왜 필요한지, 또는 필요 없는 요구가 있는지도 발견할 수 있다.</p>
                """,
            },
            {
                "heading": "와이어프레임과 반복 수정",
                "body": """
                <p>와이어프레임은 예쁘게 디자인하는 단계가 아니다. 네모, 세모, 동그라미, 별표를 그리며 머릿속 내용을 화면으로 확인하는 과정이다. 버튼을 눌렀을 때 어떤 기능이 실행되고 어떤 요구가 만족되는지 확인하면서, 이상한 부분이 보이면 다시 개발 정책, 서비스 정책, IA, 요구사항으로 돌아가 수정한다.</p>
                <div class="diagram">
                  <div><span class="node-title">글로 정리</span><p>요구사항, IA, 정책서</p></div>
                  <span class="arrow">→</span>
                  <div><span class="node-title">그림으로 검토</span><p>와이어프레임/스토리보드</p></div>
                  <span class="arrow">→</span>
                  <div><span class="node-title">개발 착수</span><p>디자인, API 명세, DB 설계</p></div>
                </div>
                """,
            },
            {
                "heading": "WBS",
                "body": """
                <p>개발에 착수할 때는 <strong>WBS</strong>, 즉 프로젝트 업무분류 체계를 만들면 좋다. 강의에서는 WBS 안에 최소 세 가지 정보가 나타나야 한다고 설명한다.</p>
                <ul>
                  <li><strong>프로젝트 이해관계자:</strong> 각 단계에 A 개발자, B 기획자, C 디자이너, PM 등이 누가 들어가는지 표시한다.</li>
                  <li><strong>프로젝트 일정:</strong> 어느 단계부터 어느 단계까지 무엇이 끝나야 하는지 표시한다.</li>
                  <li><strong>프로젝트 결과물:</strong> 일정이 끝났을 때 어떤 산출물을 기대할 수 있는지 표시한다.</li>
                </ul>
                <p>혼자 개발할 때는 WBS가 덜 중요해 보일 수 있지만, 산업계에서는 여러 팀이 함께 움직인다. 개발 일정과 결과물이 명시되어야 마케팅팀, 기획팀, CEO, 프로덕트팀 등 다른 이해관계자도 자신의 일을 준비할 수 있다. 강의에서는 수동으로 파워포인트나 엑셀로 만들 수도 있고, Jira 같은 도구로 보라색 막대 형태의 일정과 산출물을 관리할 수도 있다고 설명한다.</p>
                """,
            },
            {
                "heading": "모의 기획 예시: 안드로이드 대상 DoS 도구",
                "body": """
                <p>강의 마지막에는 “안드로이드 기기를 대상으로 DoS 공격을 수행하는 소프트웨어를 제작한다”는 아이디어를 예로 들어 기획 순서를 다시 정리한다. 먼저 기존에 안드로이드를 대상으로 DoS를 수행한 도구를 조사해 레퍼런스를 분석한다. 같은 플로우를 가진 도구가 있는지, 차별점이 있는지 확인하면 내 소프트웨어의 장점을 더할 수 있다.</p>
                <ol>
                  <li>기존 도구와 레퍼런스를 조사한다.</li>
                  <li>최종적으로 만족해야 할 내용을 요구사항 명세서로 쓴다.</li>
                  <li>앱 화면, 데이터, 모델, 팝업, 데이터 흐름은 IA로 정리한다.</li>
                  <li>필요한 기능을 나열해 정책서로 누락을 확인한다.</li>
                  <li>글로 정리한 세 가지를 와이어프레임으로 스케치한다.</li>
                  <li>와이어프레임에서 문제가 보이면 앞 단계로 돌아가 수정한다.</li>
                </ol>
                <p>Waterfall에서는 각 단계에 많은 정성을 들이므로 크리티컬한 문제가 아니라면 다음 버전에 반영하는 경우가 많고, Agile에서는 와이어프레임에서 결함을 발견하면 바로 올라가 수정하고 그 수정 버전을 이번 스프린트에 포함할 수 있다.</p>
                """,
            },
        ],
        "checks": [
            "요구사항 명세서와 IA의 차이를 설명할 수 있는가?",
            "서비스 정책과 개발 정책이 각각 어떤 관점의 문서인지 구분할 수 있는가?",
            "WBS에 이해관계자, 일정, 결과물이 들어가야 하는 이유를 설명할 수 있는가?",
            "와이어프레임에서 문제가 발견되면 어떤 문서로 돌아가야 하는가?",
        ],
    },
    {
        "id": "1-7",
        "file": "lecture-1-7.html",
        "title": "C 언어 기초 문법 총정리",
        "subtitle": "개발 환경, 변수와 상수, 입출력, 조건문, 반복문, 함수, 배열, 포인터, 문자열, 동적 메모리, 구조체까지.",
        "tags": ["C 언어", "문법", "메모리"],
        "objectives": [
            "C 언어가 소스 코드에서 컴파일러를 거쳐 기계어로 변환되는 흐름을 이해한다.",
            "기초 문법을 외우기보다 어떤 상황에서 활용하는지 중심으로 정리한다.",
            "변수, 배열, 포인터, 문자열, 동적 메모리, 구조체의 연결 관계를 이해한다.",
        ],
        "sections": [
            {
                "heading": "강의 방향: 왜 C 언어인가",
                "body": """
                <p>앞선 강의에서 소프트웨어 산업과 품질, 기획의 중요성을 배웠고, 기획이 끝났다면 이제 개발을 할 수 있어야 한다. 강의에서는 개발을 “선택한 프로그래밍 언어의 문법을 작성하고, 그 문법을 응용해 응용 프로그램을 만드는 행위”로 설명한다.</p>
                <p>C, C++, Python, Java, Go, Kotlin 등 언어는 많지만, 화이트햇과 정보보안 맥락에서는 원초적인 언어인 C를 먼저 다룬다. 다만 짧은 시간 안에 압축적으로 다루므로 핵심 내용 위주이며, 문법을 무조건 외우기보다 “이 문법을 어디에 활용하는가”에 초점을 맞추라고 안내한다.</p>
                """,
            },
            {
                "heading": "소스 코드, 컴파일러, 프로그램",
                "body": """
                <p>C 소스 코드는 사람이 읽을 수 있는 영어 알파벳 형태로 작성된다. 그러나 컴퓨터는 이 문장을 바로 이해하지 못하므로, 컴퓨터가 알아들을 수 있는 0과 1 형태로 바꿔 주는 <strong>컴파일러</strong>가 필요하다.</p>
                <div class="diagram">
                  <div><span class="node-title">C 소스 코드</span><p>사람이 작성한 문법</p></div>
                  <span class="arrow">→</span>
                  <div><span class="node-title">컴파일러</span><p>GCC, MinGW 등</p></div>
                  <span class="arrow">→</span>
                  <div><span class="node-title">기계어/프로그램</span><p>컴퓨터가 실행 가능한 형태</p></div>
                </div>
                """,
            },
            {
                "heading": "개발 환경 구성",
                "body": """
                <p>강의에서 언급한 C 개발 환경은 GCC, Turbo C, Visual Studio, Eclipse, Visual Studio Code 등이다. 실습은 <strong>Visual Studio Code</strong>를 에디터로 사용하고, C/C++ 컴파일러를 별도로 붙이는 가벼운 방식으로 진행한다.</p>
                <ol>
                  <li>Visual Studio Code를 설치한다.</li>
                  <li>좌측 확장 마켓에서 C/C++ Extension Pack을 설치한다.</li>
                  <li>MinGW를 설치한다.</li>
                  <li>필요 패키지를 Mark for Installation 한 뒤 Installation 메뉴에서 Apply Changes를 누른다.</li>
                  <li>Windows 환경 변수에 MinGW의 bin 경로를 추가한다.</li>
                  <li>CMD에서 <code>gcc -v</code>, <code>g++ -v</code>로 버전이 나오는지 확인한다.</li>
                  <li>VS Code에 <code>.vscode</code> 폴더와 작업 설정 파일을 두고, 단축키를 설정한다.</li>
                  <li><code>Ctrl+F7</code>은 빌드, <code>Ctrl+F5</code>는 빌드된 파일 실행에 사용한다.</li>
                  <li><code>hello.c</code> 파일을 만들고 <code>printf</code>로 문자열이 출력되는지 확인한다.</li>
                </ol>
                """ + code_block("""
                #include <stdio.h>

                int main(void) {
                    printf("hello world\\n");
                    return 0;
                }
                """),
            },
            {
                "heading": "변수와 상수",
                "body": """
                <p>변수와 상수는 공통적으로 값을 저장할 수 있는 공간이다. 차이는 값이 바뀔 수 있는가이다. <strong>3</strong>은 언제 불러도 3이므로 상수이고, <strong>a = 3</strong>에서 a는 나중에 4로 바뀔 수 있으므로 변수다.</p>
                <p>C에서는 자료형, 변수 이름, 대입값으로 변수를 만들고, <code>const</code> 키워드를 붙여 값을 바꿀 수 없는 상수로 만든다. 같은 공간 안에서 같은 이름의 변수를 다시 만들 수 없고, 이미 만든 변수에는 자료형 없이 새 값을 대입한다.</p>
                """ + code_block("""
                int a = 3;
                printf("a value %d\\n", a);

                a = 4;
                printf("a value %d\\n", a);

                const int b = 5;
                /* b = 6;  // const가 붙었으므로 변경 불가 */
                """) + """
                <p>자료형은 상자의 크기와 범위를 정한다. 예를 들어 <code>short</code>는 2바이트로 약 -32,768부터 32,767까지 넣을 수 있고, <code>int</code>는 약 -21억부터 21억대까지 담을 수 있다. 범위를 넘는 값을 넣으면 이상한 값이 나오거나 넘어가 버릴 수 있다.</p>
                <table>
                  <thead><tr><th>자료형/개념</th><th>강의에서 설명한 포인트</th></tr></thead>
                  <tbody>
                    <tr><td>short</td><td>2바이트, -32,768부터 32,767 정도의 범위</td></tr>
                    <tr><td>int</td><td>4바이트, 약 -21억부터 21억대까지</td></tr>
                    <tr><td>long / long long</td><td>int보다 더 큰 숫자가 필요할 때 고려</td></tr>
                    <tr><td>char / unsigned char</td><td>문자나 1바이트 단위 데이터를 다룰 때 등장</td></tr>
                    <tr><td>const</td><td>한 번 정한 값을 바꿀 수 없게 만드는 키워드</td></tr>
                  </tbody>
                </table>
                """,
            },
            {
                "heading": "printf와 형식 지정",
                "body": """
                <p><code>printf("a")</code>처럼 큰따옴표 안에 변수 이름을 쓰면 변수 a가 아니라 문자 a가 출력된다. 변수 값을 출력하려면 형식 지정자와 쉼표 뒤 변수명을 사용한다. 강의에서는 숫자형 출력에 <code>%d</code>를 사용하고, 줄바꿈에는 <code>\\n</code>을 사용한다고 설명한다.</p>
                """ + code_block("""
                int a = 3;

                printf("a");              // 문자 a 출력
                printf("%d", a);          // 변수 a의 값 3 출력
                printf("a value %d\\n", a);
                """),
            },
            {
                "heading": "입력과 출력",
                "body": """
                <p>입력은 사람 입장에서 키보드를 치는 것이 아니라, 컴퓨터 관점에서 <strong>외부 장치로부터 데이터를 가져오는 것</strong>이다. 출력은 컴퓨터가 <strong>외부 장치에 데이터를 전달하는 것</strong>이다. 둘을 합쳐 I/O라고 한다.</p>
                <table>
                  <thead><tr><th>구분</th><th>예시 장치</th><th>방향</th></tr></thead>
                  <tbody>
                    <tr><td>입력</td><td>키보드, 마이크, 마우스</td><td>외부 장치 → 프로그램</td></tr>
                    <tr><td>출력</td><td>모니터, 스피커</td><td>프로그램 → 외부 장치</td></tr>
                  </tbody>
                </table>
                <p>실습에서는 키보드 입력과 콘솔 출력만 다룬다. 입력 함수 예시로 <code>scanf</code>, <code>fgets</code>를 언급하고, 출력 함수 예시로 <code>printf</code>, <code>sprintf</code>, <code>fputs</code>를 언급한다.</p>
                """ + code_block("""
                int age = 0;

                printf("your age: ");
                scanf("%d", &age);
                printf("my age is %d\\n", age);
                """) + """
                <p>나이 입력 예제에서는 아직 제한 조건이 없으므로 21억 살 같은 비현실적인 값도 들어갈 수 있다. 실제 프로그램에서는 최소 0세, 최대 150세 또는 200세처럼 조건 검사가 필요하다.</p>
                """,
            },
            {
                "heading": "조건문",
                "body": """
                <p>조건문은 조건에 따라 다른 코드를 실행하게 만든다. 게임 시작 버튼을 눌렀을 때 일반 게임, 랭크 게임, 다른 모드로 나뉘거나, 랭크 게임 안에서도 개인 랭크와 단체 랭크로 나뉘는 상황을 떠올리면 된다.</p>
                <p><code>if</code>, <code>else if</code>, <code>else</code>는 위에서부터 조건을 차례대로 검사해 세 갈래 중 하나를 선택한다. <code>switch case</code>는 대상 값이 무엇인지 보고 해당 케이스로 바로 이동하는 방식으로 설명된다.</p>
                """ + code_block("""
                int age = 0;

                printf("your age: ");
                scanf("%d", &age);

                if (age < 0) {
                    printf("age is not under 0\\n");
                } else if (age < 19) {
                    printf("no\\n");
                } else {
                    printf("welcome\\n");
                }
                """) + """
                <p>나이 예제에서는 처음에 19세 미만이면 <code>no</code>, 19세 이상이면 <code>welcome</code>만 처리했다. 그러나 -1을 입력하면 <code>no</code>가 나오므로 잘못된 나이를 별도로 처리하도록 조건을 앞에 추가했다.</p>
                """,
            },
            {
                "heading": "복잡한 조건문: 점수와 등급",
                "body": """
                <p>두 번째 조건문 실습은 국어, 영어, 수학 점수를 입력받아 평균을 구하고 A/B/C/D/F 등급을 나누는 예시다. 평균은 소수점이 필요하므로 <code>int</code> 대신 <code>double</code>을 사용한다. 평균을 출력할 때는 <code>%lf</code>를 사용한다.</p>
                """ + code_block("""
                int korean = 0;
                int english = 0;
                int math = 0;

                scanf("%d", &korean);
                scanf("%d", &english);
                scanf("%d", &math);

                double average = (korean + english + math) / 3.0;
                printf("average: %lf\\n", average);

                if (average >= 90) {
                    printf("A\\n");
                } else if (average >= 80) {
                    printf("B\\n");
                } else if (average >= 70) {
                    printf("C\\n");
                } else if (average >= 60) {
                    printf("D\\n");
                } else {
                    printf("F\\n");
                }
                """) + """
                <p>강의에서는 98, 99, 91을 넣으면 평균 96점대로 A가 나오고, 60, 76, 58을 넣으면 평균 64점대로 D가 나오는 흐름을 확인한다.</p>
                """,
            },
            {
                "heading": "반복문",
                "body": """
                <p>반복문은 공통된 코드나 로직을 반복 실행하기 위한 문법이다. 강의에서는 마켓 프로그램의 정산 예시를 든다. 1번 품목 100원, 2번 품목 200원, 3번 품목 500원을 사용자가 계속 입력하고, 그 번호에 해당하는 가격을 누적하다가 사용자가 그만둘 때까지 반복할 수 있다.</p>
                <p>C에는 <code>for</code>, <code>while</code>, <code>do while</code>이 있지만 실습에서는 <code>for</code>와 <code>while</code>을 다룬다.</p>
                """ + code_block("""
                for (int i = 0; i < 10; i++) {
                    printf("hello\\n");
                }

                int j = 0;
                while (j < 10) {
                    printf("hello\\n");
                    j++;
                }
                """) + """
                <p><code>for</code>의 <strong>초기식</strong>은 반복문을 만나 처음 한 번 보는 부분, <strong>조건식</strong>은 계속 검사하는 조건, <strong>증감식</strong>은 기준값을 변화시키는 부분이다. 강의는 0부터 시작해 0,1,2,3,4,5,6,7,8,9까지 10번 출력하는 흐름을 설명하며, 프로그래밍에서는 0부터 인덱스를 세는 연습이 중요하다고 말한다.</p>
                """,
            },
            {
                "heading": "함수",
                "body": """
                <p>함수는 C뿐 아니라 대부분의 프로그래밍 언어에 있는 개념이다. 수학에서 <code>f(x) = x + 1</code>처럼 입력에 따라 출력이 결정되는 구조로 이해할 수 있고, 코드에서는 <strong>재사용할 수 있는 코드 뭉치</strong>로 이해하면 된다.</p>
                <p>함수의 기본 형태는 반환형, 함수 이름, 매개변수, 중괄호 안 코드로 구성된다. 반환형과 매개변수가 있느냐 없느냐에 따라 네 가지 대표 형태가 나온다.</p>
                <table>
                  <thead><tr><th>형태</th><th>의미</th><th>예시</th></tr></thead>
                  <tbody>
                    <tr><td>반환형 없음, 매개변수 없음</td><td>부르면 정해진 코드만 수행</td><td><code>void function1(void)</code></td></tr>
                    <tr><td>반환형 있음, 매개변수 없음</td><td>부르면 값을 반환</td><td><code>int function2(void)</code></td></tr>
                    <tr><td>반환형 없음, 매개변수 있음</td><td>값을 받아 코드만 수행</td><td><code>void function3(int a, int b)</code></td></tr>
                    <tr><td>반환형 있음, 매개변수 있음</td><td>값을 받아 계산하고 반환</td><td><code>int function4(int a, int b)</code></td></tr>
                  </tbody>
                </table>
                """ + code_block("""
                void function1(void) {
                    printf("function1 call\\n");
                }

                int function2(void) {
                    printf("function2 call\\n");
                    return 5;
                }

                void function3(int num1, int num2) {
                    int result = num1 + num2;
                    printf("%d + %d = %d\\n", num1, num2, result);
                }

                int function4(int num1, int num2) {
                    return num1 * num2;
                }
                """) + """
                <p><code>main</code>도 함수다. 메인 밖에 함수를 만들어 놓기만 하면 실행되지 않고, 메인 안에서 함수 이름과 소괄호로 호출해야 한다. 반환형이 있는 함수는 <code>return</code>한 값을 변수에 받아 사용할 수 있고, 매개변수는 함수를 부를 때 넘겨준 값이 순서대로 들어간다.</p>
                """,
            },
            {
                "heading": "배열",
                "body": """
                <p>배열은 변수를 메모리에서 연속적으로 할당해 방 번호로 접근하게 해 주는 문법이다. <code>int a</code>, <code>int b</code>, <code>int c</code>를 나란히 코드에 썼다고 해서 메모리에서도 연속인 것은 아니다. 배열을 사용하면 같은 집 이름 아래 0번 방, 1번 방, 2번 방처럼 연속된 공간을 만들 수 있다.</p>
                """ + code_block("""
                int array[3] = {1, 2, 3};

                array[0] = 10;
                array[1] = 20;
                array[2] = 30;

                printf("%d\\n", array[0] + array[1]);  // 30
                """) + """
                <p>배열은 반복문과 결합했을 때 강력하다. <code>array[i]</code>처럼 방 번호를 변수로 바꾸면 0번, 1번, 2번 방을 차례대로 순회할 수 있다.</p>
                """ + code_block("""
                int ar[3] = {10, 20, 30};
                int result = 0;

                for (int i = 0; i < 3; i++) {
                    result = result + ar[i];
                }
                printf("%d\\n", result);  // 60
                """) + """
                <p>2차원 배열은 행렬처럼 이해한다. 예를 들어 <code>int ar[2][2]</code>는 <code>ar[0][0]</code>, <code>ar[0][1]</code>, <code>ar[1][0]</code>, <code>ar[1][1]</code> 네 칸을 가진다. 2차원 배열을 순회할 때는 반복문 안에 반복문이 들어가는 중첩 반복문을 사용한다. 3차원 배열은 <code>x, y, z</code> 축처럼 생각할 수 있고, 그래픽이나 게임에서 RGB 값을 저장하는 예시가 언급된다.</p>
                """ + code_block("""
                int ar2[2][2] = {0};

                for (int i = 0; i < 2; i++) {
                    for (int j = 0; j < 2; j++) {
                        scanf("%d", &ar2[i][j]);
                    }
                }
                """),
            },
            {
                "heading": "포인터",
                "body": """
                <p>포인터는 값이 아니라 <strong>위치 정보</strong>를 활용하는 개념이다. 강의에서는 <strong>call by value</strong>와 <strong>call by reference</strong>를 먼저 설명한다. call by value는 값을 직접 복사해 호출하는 것이고, call by reference는 주소를 넘겨 그 주소를 따라가 값을 다루는 간접 호출이다.</p>
                <p><code>&</code>는 변수의 주소를 얻는 연산자이고, <code>*</code>는 포인터 변수 선언 또는 주소를 따라가 실제 값을 참조하는 데 사용된다.</p>
                """ + code_block("""
                int a = 10;
                int *aptr = &a;

                printf("%p\\n", aptr);   // a의 주소
                printf("%d\\n", *aptr);  // 주소를 따라가 얻은 값 10
                """) + """
                <p>2차원 포인터는 포인터의 포인터다. 한 번 따라가면 다른 포인터의 주소가 나오고, 다시 한 번 따라가야 실제 값에 도달한다. 별표 개수는 몇 번 간접적으로 따라갈지를 나타내는 감각으로 이해하면 된다.</p>
                """,
            },
            {
                "heading": "포인터 실습: swap",
                "body": """
                <p>포인터를 반드시 사용해야 하는 상황으로 <code>swap</code> 함수를 다룬다. <code>num1</code>과 <code>num2</code>를 함수에 값으로 넘기면 10과 20이 복사되어 함수 내부의 a, b만 바뀐다. 메인에 있는 원래 변수는 바뀌지 않는다.</p>
                """ + code_block("""
                void swap_value(int a, int b) {
                    int temp = a;
                    a = b;
                    b = temp;
                }
                """) + """
                <p>원래 값을 바꾸려면 값이 아니라 주소를 넘겨야 한다. 함수는 주소를 받아 그 주소를 따라가 실제 값을 바꾼다.</p>
                """ + code_block("""
                void swap(int *a, int *b) {
                    int temp = *a;
                    *a = *b;
                    *b = temp;
                }

                int num1 = 10;
                int num2 = 20;

                swap(&num1, &num2);
                printf("%d %d\\n", num1, num2);  // 20 10
                """) + """
                <p>강의에서는 주소를 현실 세계의 “서울특별시 강남구 몇 동 몇 호”처럼 비유한다. 값을 복사한 것이 아니라 실제 위치를 알려 주었기 때문에, 함수가 그 위치를 찾아가 값을 바꿀 수 있다.</p>
                """,
            },
            {
                "heading": "문자열",
                "body": """
                <p>C에는 Java나 Kotlin의 <code>String</code> 같은 문자열 자료형이 기본 제공되지 않는다. 대신 문자 하나를 저장하는 <code>char</code>와 배열 또는 포인터를 사용한다. 핵심은 여러 문자가 이어지다가 마지막에 <strong>null 문자</strong>가 오면 그 앞까지를 문자열로 판단한다는 것이다.</p>
                """ + code_block("""
                char str1[6] = "hello";  // h e l l o \\0
                printf("%s\\n", str1);

                str1[0] = 'b';
                printf("%s\\n", str1);   // bello

                char *str2 = "bye";
                printf("%s\\n", str2);
                /* str2[0] = 'c';  // 문자열 상수이므로 수정 불가 */
                """) + """
                <p>배열로 만든 문자열은 방 번호로 접근해 문자를 바꿀 수 있지만, 포인터로 문자열 상수의 시작 주소를 들고 있는 경우에는 그 내용을 바꿀 수 없다. 문자열 출력은 <code>%s</code>를 사용한다.</p>
                """,
            },
            {
                "heading": "문자열 함수",
                "body": """
                <p>문자열 관련 함수는 <code>string.h</code>를 포함해 사용한다. 강의에서는 네 가지를 대표로 다룬다.</p>
                <table>
                  <thead><tr><th>함수</th><th>역할</th><th>활용 예시</th></tr></thead>
                  <tbody>
                    <tr><td><code>strcpy</code></td><td>문자열 복사</td><td>클립보드처럼 한 문자열을 다른 배열에 복사</td></tr>
                    <tr><td><code>strlen</code></td><td>문자열 길이 확인</td><td>이름이 최대 5글자를 넘는지 검사</td></tr>
                    <tr><td><code>strcmp</code></td><td>문자열 비교</td><td>아이디, 이메일 중복 여부 비교</td></tr>
                    <tr><td><code>strcat</code></td><td>문자열 연결</td><td>여러 문자열을 이어 하나의 긴 문자열로 만들기</td></tr>
                  </tbody>
                </table>
                """ + code_block("""
                #include <string.h>

                char str1[] = "bello";
                char str3[6] = {0};
                strcpy(str3, str1);

                int size = (int)strlen(str3);
                int same = strcmp(str1, str3);  // 같으면 0

                char str5[] = "cello";
                char str6[30] = {0};
                strcat(str6, str5);
                strcat(str6, str3);             // cellobello
                """) + """
                <p>강의는 나중에 버퍼 오버플로우나 시스템 해킹을 배우면 <code>strcpy</code> 같은 문자열 함수에서 취약점이 발생할 수 있음을 이해하게 된다고 예고한다. 이후에는 <code>strncpy</code>처럼 개선된 함수들도 공부하게 된다.</p>
                """,
            },
            {
                "heading": "동적 메모리 관리",
                "body": """
                <p>C 프로그램은 stack과 heap 등 여러 메모리 영역을 사용한다. 지금까지 다룬 많은 변수는 미리 정해지는 stack 쪽 흐름으로 이해할 수 있고, <strong>동적 메모리</strong>는 프로그램 실행 도중 heap 영역을 개발자가 직접 확보하고 반환하는 방식이다.</p>
                <p>heap은 실행 중 필요한 만큼 잡을 수도 있고, 더 필요하면 늘리거나 줄일 수도 있다. 하지만 개발자가 반환을 잊으면 리소스 누수나 취약점 원인이 될 수 있다.</p>
                <table>
                  <thead><tr><th>함수</th><th>역할</th></tr></thead>
                  <tbody>
                    <tr><td><code>malloc</code></td><td>원하는 바이트만큼 heap 메모리를 할당하고 포인터를 반환</td></tr>
                    <tr><td><code>calloc</code></td><td>크기와 개수를 곱한 만큼 할당</td></tr>
                    <tr><td><code>realloc</code></td><td>기존 포인터를 기준으로 크기를 변경</td></tr>
                    <tr><td><code>memset</code></td><td>메모리 영역을 원하는 값, 주로 0으로 일괄 초기화</td></tr>
                    <tr><td><code>free</code></td><td>다 쓴 동적 메모리를 반환</td></tr>
                  </tbody>
                </table>
                """ + code_block("""
                #include <stdio.h>
                #include <stdlib.h>
                #include <memory.h>

                int byte_size = 3;
                int *ptr1 = (int *)malloc(sizeof(int) * byte_size);

                ptr1[0] = 10;
                *(ptr1 + 1) = 40;

                int *ptr2 = (int *)realloc(ptr1, sizeof(int) * 10);
                ptr2[9] = 900;

                memset(ptr2, 0, sizeof(int) * 10);
                free(ptr2);
                """) + """
                <p><code>sizeof(int)</code>는 int 자료형의 크기를 반환한다. <code>ptr[0]</code>과 <code>*(ptr + 0)</code>은 같은 방식으로 접근할 수 있고, <code>ptr + 1</code>은 주소에서 한 칸 이동한다는 뜻이다. 동적으로 할당한 메모리는 반드시 <code>free</code>해야 한다.</p>
                """,
            },
            {
                "heading": "구조체",
                "body": """
                <p>구조체는 사용자가 여러 자료형을 묶어서 자신만의 자료형을 만들 수 있게 해 준다. <code>int</code>, <code>double</code>, <code>float</code>, <code>char</code> 같은 원시 자료형만 쓰는 것이 아니라, 학생 타입, 학교 타입처럼 설계 관점에서 더 큰 자료형을 만들 수 있다.</p>
                <p>구조체 안의 변수들은 멤버, 멤버 변수, 프로퍼티라고 부를 수 있다. 강의에서는 이것이 객체지향의 시작처럼 볼 수도 있다고 설명한다.</p>
                """ + code_block("""
                #include <stdio.h>

                typedef struct {
                    int age;
                    char address[100];
                    char name[20];
                } Student;

                int main(void) {
                    Student s1;

                    scanf("%s", s1.name);
                    scanf("%d", &s1.age);
                    scanf("%s", s1.address);

                    printf("name: %s\\n", s1.name);
                    printf("age: %d\\n", s1.age);
                    printf("address: %s\\n", s1.address);
                    return 0;
                }
                """) + """
                <p>구조체도 자료형이므로 배열과 포인터로 사용할 수 있다. 예를 들어 학생 수를 입력받아 <code>malloc(count * sizeof(Student))</code>으로 여러 학생을 동적으로 관리할 수 있고, 다 쓴 뒤에는 <code>free</code>로 반환한다. 구조체 안에 포인터가 들어가거나 구조체의 포인터를 다루는 고급 문법은 기본을 익힌 뒤 필요할 때 추가로 공부하면 된다.</p>
                """,
            },
        ],
        "checks": [
            "C 소스 코드가 컴파일러를 거쳐 실행 가능한 프로그램이 되는 흐름을 설명할 수 있는가?",
            "변수와 상수를 const 기준으로 구분할 수 있는가?",
            "scanf에서 왜 변수 주소를 넘기는지 설명할 수 있는가?",
            "for문의 초기식, 조건식, 증감식 흐름을 실제 실행 순서로 설명할 수 있는가?",
            "함수의 반환형과 매개변수가 각각 무엇을 의미하는가?",
            "배열이 반복문과 결합될 때 유용한 이유를 설명할 수 있는가?",
            "call by value와 call by reference의 차이를 swap 예제로 설명할 수 있는가?",
            "문자열 배열과 문자열 포인터의 수정 가능성 차이를 설명할 수 있는가?",
            "malloc으로 잡은 메모리를 free하지 않으면 어떤 문제가 생기는가?",
            "구조체가 사용자 정의 자료형이라는 점을 이해했는가?",
        ],
    },
    {
        "id": "1-8",
        "file": "lecture-1-8.html",
        "title": "소프트웨어 개선과 장애 대응",
        "subtitle": "유지보수 단계에서 사용자 신고를 단서로 원인을 좁혀 가는 실무형 사고법.",
        "tags": ["유지보수", "장애 대응", "메모리 누수"],
        "objectives": [
            "사용자 신고가 들어왔을 때 개발자가 바로 원인을 단정하지 않고 단서를 좁혀 가는 방식을 이해한다.",
            "결제 장애 시나리오에서 외부 모듈과 이용 기간을 점검하는 흐름을 정리한다.",
            "전체 인터랙션 지연 시나리오에서 리소스 사용과 메모리 누수를 의심하는 과정을 이해한다.",
        ],
        "sections": [
            {
                "heading": "강의 위치",
                "body": """
                <p>앞 강의들에서 소프트웨어 산업, 품질 향상, 기획 프로세스, 프로젝트 관리 방법론, C 언어 핵심 문법을 다뤘다. 이 강의는 그 지식을 바탕으로 프로그램을 만들고 유지보수하는 과정에서 새로운 니즈나 장애가 발생했을 때 어떻게 대처할지 시나리오로 설명한다.</p>
                """,
            },
            {
                "heading": "시나리오 1: 결제가 갑자기 안 된다",
                "body": """
                <p>사용자들이 “어제부터 결제가 갑자기 안 된다”고 말한다. 개발자 입장에서는 언제, 무엇을, 어떻게 눌렀는지 알고 싶지만 사용자는 소스 코드나 내부 구조를 모른다. 사용자는 결제가 되는지 안 되는지가 중요하다. 그래서 개발자는 질문을 통해 단서를 좁혀야 한다.</p>
                <ol>
                  <li>어제 서비스에 영향을 줄 수 있는 이벤트가 있었는지 확인한다.</li>
                  <li>로그를 확인하고, “어제부터”가 정확히 몇 시인지 추가로 묻는다.</li>
                  <li>내부 이벤트가 없고 오후 9시부터 동작하지 않았다는 단서를 얻는다.</li>
                  <li>원래 잘 동작하던 기능이므로 외부 요인일 가능성을 의심한다.</li>
                  <li>결제 모듈과 정상적으로 통신되는지 확인한다.</li>
                  <li>결제 모듈과 통신되지 않는다는 사실을 확인한다.</li>
                  <li>원인을 파악해 보니 외부 결제 모듈 이용 기간이 종료되었음을 발견한다.</li>
                  <li>결제 모듈 이용 기간을 갱신하고, 새 키를 발급받고, 재배포 일정을 수립한다.</li>
                </ol>
                <p>이 시나리오는 장애 대응에서 “갑자기 안 된다”는 신고를 내부 이벤트, 시간, 외부 연동, 계약/키 상태 순서로 좁혀 가는 예시다.</p>
                """,
            },
            {
                "heading": "시나리오 2: 모든 인터랙션이 느려졌다",
                "body": """
                <p>두 번째 시나리오는 소프트웨어의 모든 인터랙션이 갑자기 느려진 경우다. 먼저 모든 사용자가 느려진 것인지, 일부 사용자만 느려진 것인지 확인해야 한다. 100명이 사용한다면 100명 모두인지, 일부 인원인지에 따라 원인이 달라질 수 있다. 디바이스 환경 문제일 수도 있기 때문이다.</p>
                <ol>
                  <li>모든 유저에게 해당하는지 확인한다.</li>
                  <li>조사 결과 일부 인원이 오랫동안 켜 두었을 때 증상이 발생한다는 단서를 얻는다.</li>
                  <li>오랫동안 켜 두었을 때라는 조건 때문에 실행 중 불필요하게 하드웨어 리소스를 사용하는 사례를 의심한다.</li>
                  <li>각 기능별로 리소스를 낭비하고 있는지 다시 테스트한다.</li>
                  <li>A 함수에서 heap 메모리를 사용한 뒤 적절한 시점에 해제하지 않아 메모리 누수가 발생했음을 찾는다.</li>
                  <li>오래 켜 둘수록 누수가 누적되어 전체 인터랙션이 느려진다.</li>
                  <li>모든 함수를 다시 검증하고 재배포 일정을 수립한다.</li>
                </ol>
                """,
            },
            {
                "heading": "장애 대응 사고법",
                "body": """
                <div class="diagram">
                  <div><span class="node-title">사용자 신고</span><p>결제가 안 됨, 느려짐</p></div>
                  <span class="arrow">→</span>
                  <div><span class="node-title">단서 수집</span><p>시간, 범위, 이벤트, 환경</p></div>
                  <span class="arrow">→</span>
                  <div><span class="node-title">가설 세우기</span><p>외부 모듈, 리소스 낭비</p></div>
                  <span class="arrow">→</span>
                  <div><span class="node-title">검증과 조치</span><p>키 갱신, 메모리 해제, 재배포</p></div>
                </div>
                <p>강의가 보여주는 공통 패턴은 소거법이다. 처음부터 원인을 단정하지 않고, 사용자가 제공한 말에서 시간과 범위를 뽑고, 내부 이벤트와 외부 요인을 나누고, 실제 통신이나 리소스 사용을 확인해 원인을 좁힌다.</p>
                """,
            },
            {
                "heading": "과목 마무리",
                "body": """
                <p>강의 마지막에서는 프로그래밍 기초 과목이 단순히 언어와 문법을 많이 외우는 수업이 아니라, 개발자 또는 화이트 해커로서 프로그래밍을 할 준비가 되도록 만들기 위한 수업이었다고 정리한다. 이론과 실무 내용을 함께 다루려 했고, 긴 강의를 따라온 수강생에게 감사 인사를 전하며 마무리한다.</p>
                """,
            },
        ],
        "checks": [
            "사용자 신고가 모호할 때 어떤 추가 정보를 먼저 물어봐야 하는가?",
            "결제 장애에서 외부 모듈을 의심하게 되는 단서는 무엇인가?",
            "오래 켜 둘수록 느려지는 증상에서 메모리 누수를 의심하는 이유는 무엇인가?",
            "장애 대응에서 소거법이 왜 중요한가?",
        ],
    },
]


COMPUTER_ARCHITECTURE_1_LECTURES = build_computer_architecture_1_lectures(code_block, screen_figure, image_figure)
OS_BASIC_LECTURES = build_os_basic_lectures(code_block, screen_figure)
NETWORK_BASIC_LECTURES = build_network_basic_lectures(code_block, screen_figure)
CRYPTOGRAPHY_BASIC_LECTURES = build_cryptography_basic_lectures(code_block, screen_figure)
ETHICS_CYBER_SECURITY_LECTURES = build_ethics_cyber_security_lectures(code_block, screen_figure)
HACKERS_PROGRAMMING_LECTURES = build_hackers_programming_lectures(code_block, screen_figure)
LATEST_SECURITY_TREND_LECTURES = build_latest_security_trend_lectures(code_block, screen_figure)
SECURE_CODING_LECTURES = build_secure_coding_lectures(code_block, screen_figure)
MODERN_WEB_DEV_SECURITY_LECTURES = build_modern_web_dev_security_lectures(code_block, screen_figure)


TRACKS = [
    {
        "id": "common-development",
        "title": "공통/개발",
        "description": "프로그래밍, 컴퓨터 구조, 운영체제, 네트워크, 암호학처럼 모든 보안 분야의 바탕이 되는 과목 묶음.",
    },
    {
        "id": "vulnerability",
        "title": "취약점",
        "description": "웹, 시스템, 소프트웨어 취약점 분석과 공격 원리를 다루는 과목 묶음.",
    },
    {
        "id": "forensics",
        "title": "포렌식",
        "description": "증거 수집, 분석 절차, 디지털 흔적 해석을 다루는 과목 묶음.",
    },
    {
        "id": "security-ops-infra-consulting",
        "title": "보안운영관리/인프라/컨설팅",
        "description": "보안 운영, 인프라, 관리 체계, 컨설팅 실무를 다루는 과목 묶음.",
    },
]


COURSES = [
    {
        "id": "programming-basics-c",
        "track_id": "common-development",
        "title": "프로그래밍 기초(C)",
        "short_title": "프밍",
        "status": "ready",
        "summary": "소프트웨어 품질, 개발 생명주기, 기획, C 언어 문법, 유지보수 사고 흐름을 정리한 과목.",
        "featured_lecture": "1-7",
        "flow": ["산업", "품질", "기획", "C 문법", "개선"],
        "map": [
            ("1-1 · 1-2", "도메인별 품질 기준", "스마트 팩토리와 헬스케어 표준"),
            ("1-3 · 1-4", "SDLC와 품질 매트릭", "Agile, Waterfall, 유지보수성, 보안성"),
            ("1-5 · 1-6", "OSS와 기획", "라이선스 기준, 요구사항, IA, WBS"),
            ("1-7", "C 언어 기초", "변수부터 구조체까지 문법 총정리"),
            ("1-8", "개선과 장애 대응", "결제 장애, 메모리 누수, 재배포"),
        ],
        "lectures": LECTURES,
    },
    {
        "id": "computer-architecture-1",
        "track_id": "common-development",
        "title": "컴퓨터 구조 I",
        "transcript_title": "컴퓨터 구조 1",
        "short_title": "컴구 I",
        "status": "ready",
        "summary": "컴퓨터의 정의, 데이터 표현, CPU 실행 과정, 메모리 시스템, 입출력 구조를 보안 학습과 연결해 정리한 과목.",
        "featured_lecture": "1-4",
        "flow": ["컴퓨터", "데이터", "CPU", "메모리", "입출력"],
        "map_intro": "강의는 컴퓨터가 무엇인지에서 시작해 0과 1의 데이터 표현, CPU 명령 실행, 메모리 관찰과 계층 구조, 입출력 장치와 인터럽트로 이어진다.",
        "map": [
            ("1-1", "과목 방향", "컴퓨터 구조 I의 다섯 가지 큰 주제"),
            ("1-2", "시스템 개요", "컴퓨터 정의, 구성 요소, 역사, x86과 ARM"),
            ("1-3", "데이터 표현", "비트, 바이트, 정수, 실수, 오버플로우"),
            ("1-4", "CPU", "소스 코드, 어셈블리, 명령어 사이클, CISC/RISC"),
            ("1-5 · 1-6", "메모리와 입출력", "디버거, 엔디안, 계층 구조, USB, 인터럽트, DMA"),
        ],
        "lectures": COMPUTER_ARCHITECTURE_1_LECTURES,
    },
    {
        "id": "os-basic",
        "track_id": "common-development",
        "title": "운영체제 기초",
        "short_title": "운영체제",
        "status": "ready",
        "summary": "우분투 리눅스를 기준으로 운영체제 개념, 설치, CLI 명령어, 계정·권한, 패키지, 데몬, 서버, 개발환경, 배시, 모니터링을 정리한 과목.",
        "featured_lecture": "1-5",
        "flow": ["OS", "설치", "CLI", "관리", "서버"],
        "map_intro": "강의는 운영체제와 리눅스의 의미에서 출발해 우분투 설치, GUI와 CLI, 파일·디렉토리 명령, 계정과 권한, 패키지와 서비스, 서버 운영, 개발환경, 배시 스크립트, 시스템 모니터링까지 이어진다.",
        "map": [
            ("1-1 · 1-2", "OS와 리눅스", "운영체제, 리눅스, 우분투, 배포판"),
            ("1-3 · 1-4", "설치와 사용 환경", "VirtualBox, 클라우드, GUI, CLI"),
            ("1-5 · 1-6", "기본 명령과 권한", "파일·디렉토리, Vim, 계정, sudo, chmod"),
            ("1-7 · 1-8", "패키지와 서비스", "apt, dpkg, systemd, systemctl, journalctl"),
            ("1-9 · 1-12", "운영 실습", "웹·FTP·DB 서버, 개발환경, 배시, 모니터링"),
        ],
        "lectures": OS_BASIC_LECTURES,
    },
    {
        "id": "network-basic",
        "track_id": "common-development",
        "title": "네트워크 기초",
        "short_title": "네트워크",
        "status": "ready",
        "summary": "네트워크와 인터넷, TCP/IP 계층, 데이터 링크·네트워크·전송·응용 계층, 와이어샤크 패킷 분석, 소켓 프로그래밍을 정리한 과목.",
        "featured_lecture": "1-7",
        "flow": ["인터넷", "계층", "주소", "프로토콜", "실습"],
        "map_intro": "강의는 네트워크와 인터넷이 보안에서 중요한 이유로 시작해 TCP/IP 계층 구조, 데이터 링크·네트워크·전송·응용 계층, Wireshark 패킷 분석, UDP/TCP 소켓 프로그래밍으로 이어진다.",
        "map": [
            ("1-1 · 1-2", "네트워크 큰 그림", "네트워크, 인터넷, 프로토콜, TCP/IP 계층과 캡슐화"),
            ("1-3 · 1-4", "하위 계층", "프레임, MAC, ARP, Ethernet, IP, 라우팅, IPv4/IPv6"),
            ("1-5 · 1-6", "전송과 응용", "TCP/UDP, 포트, HTTP, HTTPS, DNS"),
            ("1-7", "패킷 분석", "Wireshark, HTTP request/response, 캡슐화, TCP 3-way handshake"),
            ("1-8", "소켓 프로그래밍", "UDP/TCP client-server 구현 흐름과 Python socket 예시"),
        ],
        "lectures": NETWORK_BASIC_LECTURES,
    },
    {
        "id": "cryptography-basic",
        "track_id": "common-development",
        "title": "암호학 기초",
        "short_title": "암호학",
        "status": "ready",
        "summary": "보안 목표, 암호 기술 분류, 해시와 HMAC, 기밀성, 공개키 암호, 디지털 서명, PKI, TLS와 하이브리드 암호 기술을 정리한 과목.",
        "featured_lecture": "1-6",
        "flow": ["보안 목표", "해시", "기밀성", "공개키", "TLS"],
        "map_intro": "강의는 암호학 기초 강의 계획에서 출발해 보안 목표와 Kerckhoffs 원리, 무결성과 인증을 위한 해시·HMAC, 기밀성을 위한 대칭키·비대칭키, 공개키 신뢰 체계, TLS와 하이브리드 암호 기술 활용으로 이어진다.",
        "map": [
            ("1-1", "강의 계획", "암호학 기초 비대면 강의의 전체 흐름과 오프라인 보완 계획"),
            ("1-2", "암호학 개요", "보안 목표, 보안 서비스, Kerckhoffs 원리, 보안 강도, 암호 기술 분류"),
            ("1-3", "무결성과 인증", "암호 해시, 메시지 다이제스트, 비둘기집 원리, 생일 문제, HMAC과 한계"),
            ("1-4", "기밀성", "대칭키와 비대칭키 암호 기술, stream/block 암호, 인증과 부인방지"),
            ("1-5", "공개키 체계", "키 배송 문제, Diffie-Hellman, 디지털 서명, 인증서, PKI, X.509"),
            ("1-6", "암호 기술 활용", "SSL/TLS, cipher suite, 암호화 트래픽 모니터링, 하이브리드 암호 기술"),
        ],
        "lectures": CRYPTOGRAPHY_BASIC_LECTURES,
    },
    {
        "id": "ethics-cyber-security",
        "track_id": "common-development",
        "title": "정보보안윤리 / 사이버 안보",
        "transcript_title": "정보보안윤리-사이버-안보",
        "short_title": "보안윤리",
        "status": "ready",
        "summary": "사이버 안보의 정의, 국내 사이버 위협 사건사, 사이버 전쟁, 국가별 전략, 한국의 안보 체계와 국가 사이버 안보 전략을 정리한 과목.",
        "featured_lecture": "1-8",
        "flow": ["사이버 안보", "위협 사건", "사이버전", "국가 체계", "전략"],
        "map_intro": "강의는 사이버 안보의 의미에서 출발해 국내 정보보호 환경과 위협 사건, 사이버 냉전·전쟁, 주요 국가의 노력, 한국의 국가 사이버 안보 체계, 2024년 국가 사이버 안보 전략으로 이어진다.",
        "map": [
            ("1-1", "사이버 안보 개요", "개인·기업·국가 보호, 주요 보안 기술, 레질리언스"),
            ("1-2 · 1-3", "사이버 위협 사건사", "정보통신망법, 인터넷 대란, DDoS, 개인정보, 한수원, 가상자산"),
            ("1-4", "사이버 전쟁과 안보", "사이버 냉전, Great Firewall, 러시아·우크라이나 하이브리드전"),
            ("1-5", "국가별 노력", "미국 Defend Forward, 중국·러시아·EU·한국의 전략"),
            ("1-6 · 1-7", "한국 안보 체계", "국가안보실, 국가정보원, NCSC, 과기정통부, KISA, 금융보안원, 개보위"),
            ("1-8", "국가 사이버 안보 전략", "2024 전략의 비전, 목표, 공세적 방어, 글로벌 공조, 복원력"),
        ],
        "lectures": ETHICS_CYBER_SECURITY_LECTURES,
    },
    {
        "id": "latest-security-trend",
        "track_id": "common-development",
        "title": "최신 보안 동향",
        "short_title": "보안 동향",
        "status": "ready",
        "summary": "제로트러스트, AI 보안, 클라우드 보안, 블록체인·Web 3.0, 사이버 테러, 인간중심보안을 최신 보안 키워드 관점에서 정리한 과목.",
        "featured_lecture": "1-6",
        "flow": ["동향 학습", "제로트러스트", "AI", "클라우드", "블록체인", "사이버 테러", "사람 중심"],
        "map_intro": "강의는 최신 보안 동향을 따라가는 학습 방법에서 출발해 제로트러스트, AI와 보안, 클라우드 보안, 블록체인과 Web 3.0 보안 이슈, 사이버 테러와 랜섬웨어·피싱, 인간중심보안으로 이어진다.",
        "map": [
            ("1-1", "학습 방향", "구글링, 뉴스레터, 기록 습관과 6개 최신 보안 키워드"),
            ("1-2", "제로트러스트", "원격근무와 탈경계화, 경계 보안의 한계, MFA, 최소 권한, ZTA"),
            ("1-3", "AI와 보안", "NLP, 컴퓨터 비전, 보안 관제, AI 악용, 적대적 공격"),
            ("1-4", "클라우드 보안", "IaaS/PaaS/SaaS, CSP/MSP, 책임 공유, SECaaS, 클라우드 위협"),
            ("1-5", "블록체인 보안", "Web 3.0, DeFi, DAO, NFT, 암호화폐 해킹, CBDC"),
            ("1-6", "사이버 테러", "사이버전, 러시아·우크라이나, 랜섬웨어, 피싱, BEC"),
            ("1-7", "인간중심보안", "사람 중심 설계, 보안 문화, 유저블 시큐리티"),
        ],
        "notes": [
            "최신 보안 동향 STT 텍스트 7개 파일을 기준으로 작성했다.",
            "각 강의 하단에는 STT 전체 흐름을 문단으로 정돈한 ‘STT 정돈본’을 접이식 패널로 제공한다.",
            "자동 전사 오류로 보이는 표현은 문맥상 의미가 분명한 경우에만 학습 가능한 보안 용어와 설명으로 정돈했다.",
            "외부 인터넷 자료나 이미지는 사용하지 않았고, 필요한 표·도식·흐름 예시는 HTML 본문 안에 직접 구성했다.",
        ],
        "lectures": LATEST_SECURITY_TREND_LECTURES,
    },
    {
        "id": "hackers-programming",
        "track_id": "common-development",
        "title": "해커의 프로그래밍",
        "short_title": "해커 프로그래밍",
        "status": "ready",
        "summary": "Python, HTTP, API, 자동화, 개인정보 결합, 가상자산 거래 그래프, BeautifulSoup 크롤링, OSINT를 해커의 문제 해결 관점에서 정리한 과목.",
        "featured_lecture": "1-8",
        "flow": ["환경 구축", "웹 요청", "API", "자동화", "데이터 결합", "그래프", "OSINT"],
        "map_intro": "강의는 해커의 프로그래밍이 무엇인지에서 출발해 Python 실습 환경과 Base64, HTTP와 requests, API와 키 관리, n8n 자동화, 개인정보 결합, 가상자산 믹싱 그래프, BeautifulSoup 크롤링, OSINT 정보 그래프로 이어진다.",
        "map": [
            ("1-1", "과목 방향", "해커의 원래 의미, 웹·데이터·도구 흐름, 실습 윤리"),
            ("1-2", "Python과 Base64", "Python/VS Code 환경, Code Runner, CyberChef, Base64 자동 디코딩"),
            ("1-3", "HTTP와 스크래핑", "요청·응답, HTML 구조, requests, 100개 노트 자동 탐색"),
            ("1-4 · 1-5", "API와 자동화", "웹 API, JSON, 키 관리, n8n 노드 기반 워크플로우"),
            ("1-6 · 1-7", "데이터 분석", "개인정보 결합, 모자이크 이론, Faker, 믹싱, 거래 그래프, Graphviz"),
            ("1-8 · 1-9", "크롤링과 OSINT", "BeautifulSoup, 사이트맵 복원, 공개 출처 정보, 정보 그래프"),
        ],
        "lectures": HACKERS_PROGRAMMING_LECTURES,
    },
    {
        "id": "secure-coding",
        "track_id": "common-development",
        "title": "시큐어코딩",
        "short_title": "시큐어코딩",
        "status": "ready",
        "summary": "시큐어 코딩의 정의, OWASP Top 10, 입력 검증, 보안 기능, 시간·상태, 에러 처리, 코드 오류, API 오용, Secure SDLC를 정리한 과목.",
        "featured_lecture": "1-4",
        "flow": ["개요", "OWASP", "입력 검증", "보안 기능", "시간·상태", "에러 처리", "Secure SDLC"],
        "map_intro": "강의는 시큐어 코딩의 위치와 필요성에서 출발해 OWASP Top 10, 입력 데이터 검증, 보안 기능과 시간·상태 문제, 에러 처리와 API 오용, 마지막으로 Secure SDLC와 위협 모델링으로 이어진다.",
        "map": [
            ("1-1", "시큐어 코딩 개요", "개발 생명주기에서 구현 단계의 보안 약점 제거"),
            ("1-2 · 1-3", "OWASP Top 10", "접근 제어, 암호화 실패, 인젝션, 설계·설정 오류, 취약 구성요소, 인증, 무결성, 로깅, SSRF"),
            ("1-4 · 1-5", "입력 데이터 검증", "SQL/Code/Command Injection, Path Traversal, XSS, 업로드, CSRF, SSRF, Response Splitting, Integer Overflow, Format String"),
            ("1-6", "보안 기능과 시간·상태", "암호 알고리즘, 하드코딩, 난수, 쿠키, 무결성, 인증 제한, Race Condition, 무한 루프"),
            ("1-7", "에러 처리와 API 오용", "오류 메시지 노출, 예외 처리, 널 참조, 역직렬화, DNS lookup, 취약 API"),
            ("1-8", "Secure SDLC", "보안 요구사항, 설계 원칙, BLP 모델, 위협 모델링, 리스크 처리"),
        ],
        "lectures": SECURE_CODING_LECTURES,
    },
    {
        "id": "modern-web-dev",
        "track_id": "common-development",
        "title": "모던 웹 개발 및 보안",
        "short_title": "웹 보안",
        "status": "ready",
        "summary": "Node.js와 Express 기초에서 출발해 라우팅, 미들웨어, EJS, Prototype Pollution, EJS RCE까지 웹 개발과 보안을 함께 정리한 과목.",
        "featured_lecture": "1-9",
        "flow": ["Node.js", "개발환경", "Express", "HTTP 요청", "라우팅", "미들웨어", "EJS", "Prototype Pollution", "EJS RCE"],
        "map_intro": "강의는 Node.js의 실행 모델과 개발환경 구축에서 시작해 Express 웹앱 구현, HTTP 요청 처리, 라우팅과 미들웨어, Node 내장 객체, EJS 템플릿을 거친 뒤 Prototype Pollution과 EJS 템플릿 원격 코드 실행 분석으로 이어진다.",
        "map": [
            ("1-1", "Node.js 개요", "런타임, 비동기, 논블로킹 I/O, 싱글 스레드, 이벤트 기반 구조"),
            ("1-2", "개발환경 구축", "Node.js LTS, npm, VS Code, package.json, Express 설치"),
            ("1-3", "Express 웹앱", "http 모듈 비교, app.get, app.listen, localhost 실습"),
            ("1-4", "HTTP 요청 처리", "req.query, req.params, req.body, 본문 파싱 미들웨어"),
            ("1-5", "라우팅", "기본 라우팅, 정적 파일, CRUD, express.Router"),
            ("1-6", "미들웨어", "req, res, next, 에러 처리, 인증 미들웨어"),
            ("1-7", "Node 내장 객체", "global, process, require, __dirname, fs, path, child_process"),
            ("1-8", "EJS 템플릿", "view engine, res.render, include, 조건문, 반복문, 출력 보안"),
            ("1-9", "Prototype Pollution", "Prototype chain, __proto__, 안전하지 않은 merge, 방어 방법"),
            ("1-10", "EJS RCE", "템플릿/옵션/데이터 경계, Prototype Pollution 연계, 안전한 렌더링"),
        ],
        "lectures": MODERN_WEB_DEV_SECURITY_LECTURES,
    },
]


def track_courses(track_id: str) -> list[dict]:
    return [course for course in COURSES if course["track_id"] == track_id]


def ready_courses() -> list[dict]:
    return [course for course in COURSES if course["status"] == "ready"]


def course_output_dir(course: dict) -> Path:
    return COURSE_ROOT / str(course["track_id"]) / str(course["id"])


def lecture_output_dir(course: dict) -> Path:
    return course_output_dir(course) / "lectures"


def course_href(course: dict) -> str:
    return f"courses/{course['track_id']}/{course['id']}/index.html"


def course_status_label(course: dict) -> str:
    if course["status"] == "ready":
        return "정리 완료"
    if course["status"] == "pending-stt":
        return "자료 준비 중"
    return "준비 예정"


# Course cards get stable visual hooks so regenerated/new courses keep the same theme.
COURSE_ICON_BY_ID = {
    "programming-basics-c": "code",
    "computer-architecture-1": "systems",
    "os-basic": "operations",
    "network-basic": "network",
    "cryptography-basic": "crypto",
    "ethics-cyber-security": "shield",
    "security-ethics-cyber-security": "shield",
    "security-trends": "trend",
    "latest-security-trend": "trend",
    "latest-security-trends": "trend",
    "hacker-programming": "code",
    "hackers-programming": "code",
    "secure-coding": "secure-code",
    "modern-web-dev": "web",
    "modern-web-dev-security": "web",
    "modern-web-security": "web",
}

COURSE_ICON_CYCLE = [
    "code",
    "systems",
    "operations",
    "network",
    "crypto",
    "shield",
    "trend",
    "code",
    "secure-code",
    "web",
]


def course_icon_key(course: dict, position: int) -> str:
    explicit_icon = str(course.get("icon", "")).strip()
    if explicit_icon:
        return filename_part(explicit_icon).lower() or "code"

    course_id = str(course.get("id", ""))
    if course_id in COURSE_ICON_BY_ID:
        return COURSE_ICON_BY_ID[course_id]

    if "network" in course_id:
        return "network"
    if "crypto" in course_id or "cipher" in course_id:
        return "crypto"
    if "web" in course_id:
        return "web"
    if "coding" in course_id or "program" in course_id:
        return "code"
    if "os" in course_id or "operating" in course_id:
        return "operations"

    return COURSE_ICON_CYCLE[(position - 1) % len(COURSE_ICON_CYCLE)]


def shared_head(title: str, css_prefix: str = "") -> str:
    return f"""<!doctype html>
<html lang="ko">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{html.escape(title)}</title>
  <link rel="stylesheet" href="{css_prefix}assets/styles.css?v=20260613-hero-kicker">
  <script src="{css_prefix}assets/code-highlight.js" defer></script>
  <script src="{css_prefix}assets/study-state.js" defer></script>
  <script src="{css_prefix}assets/study-tools.js" defer></script>
</head>
"""


def tag_list(tags: list[str]) -> str:
    return "".join(f"<span>{html.escape(tag)}</span>" for tag in tags)


def text_from_html(fragment: str) -> str:
    without_code = re.sub(r"<pre[\s\S]*?</pre>", " ", dedent(fragment), flags=re.IGNORECASE)
    without_tags = re.sub(r"<[^>]+>", " ", without_code)
    return re.sub(r"\s+", " ", html.unescape(without_tags)).strip()


def render_section_body(section: dict, lecture: dict | None = None) -> str:
    body = dedent(str(section.get("body", ""))).strip()
    if not body:
        return ""

    return emphasize_html(body, emphasis_terms_for(lecture, section))


def render_lecture_control_panel(lecture: dict, transcript_nav: str) -> str:
    options = "".join(
        f'<option value="#section-{index}">{index:02d}. {html.escape(str(section["heading"]))}</option>'
        for index, section in enumerate(lecture["sections"], start=1)
    )
    transcript_link = '<a class="button secondary" href="#transcript">강의 원문</a>' if transcript_nav else ""
    return f"""
    <section class="content-wrap lecture-control-panel" aria-label="강의 탐색 도구">
      <div class="section-jump-field">
        <label for="section-jump-{html.escape(str(lecture['id']))}">섹션 바로가기</label>
        <select id="section-jump-{html.escape(str(lecture['id']))}" data-section-jump>
          <option value="">읽을 섹션 선택</option>
          {options}
        </select>
      </div>
      <div class="lecture-control-actions" aria-label="섹션 보기 방식">
        <button class="button secondary" type="button" data-section-toggle="collapse">섹션 접기</button>
        <button class="button secondary" type="button" data-section-toggle="expand">전체 펼치기</button>
        <a class="button secondary" href="#review">복습 체크</a>
        {transcript_link}
      </div>
    </section>
    """


def lecture_content_stats(lecture: dict) -> dict[str, int]:
    sections = list(lecture.get("sections", []))
    body_html = "\n".join(str(section.get("body", "")) for section in sections).lower()
    body_text = " ".join(text_from_html(str(section.get("body", ""))) for section in sections)
    return {
        "sections": len(sections),
        "code": body_html.count("<pre"),
        "tables": body_html.count("<table"),
        "diagrams": body_html.count('class="diagram'),
        "timelines": body_html.count('class="timeline'),
        "lists": body_html.count("<ul") + body_html.count("<ol"),
        "chars": len(body_text),
    }


def render_site_index() -> str:
    ready_course_buttons = "".join(
        f'<a class="button secondary" href="{course_href(course)}">{html.escape(str(course["title"]))} 열기</a>'
        for course in ready_courses()
    )

    track_sections = []
    for index, track in enumerate(TRACKS, start=1):
        courses = track_courses(str(track["id"]))
        course_items = []
        for course_position, course in enumerate(courses, start=1):
            status_class = "status-ready" if course["status"] == "ready" else "status-pending"
            icon_key = course_icon_key(course, course_position)
            lecture_count = len(course.get("lectures", []))
            course_search = " ".join(
                [
                    str(course.get("title", "")),
                    str(course.get("short_title", "")),
                    str(course.get("summary", "")),
                    str(track.get("title", "")),
                    str(course.get("status", "")),
                ]
            )
            progress_attr = (
                f' data-course-total="{lecture_count}" data-course-progress-target="true"'
                if course["status"] == "ready"
                else ""
            )
            action = (
                f'<a class="button" href="{course_href(course)}">과목 열기</a>'
                if course["status"] == "ready"
                else '<span class="status-note">준비 중</span>'
            )
            course_items.append(
                f"""
                <article class="course-item course-icon-{html.escape(icon_key)}" data-course-id="{html.escape(str(course['id']))}" data-course-status="{html.escape(str(course['status']))}" data-search-text="{html.escape(course_search.lower())}"{progress_attr}>
                  <div>
                    <div class="course-item-head">
                      <h3>{html.escape(str(course['title']))}</h3>
                      <span class="status-pill {status_class}">{course_status_label(course)}</span>
                      {('<span class="course-progress-chip" data-course-progress-label>0/' + str(lecture_count) + ' 완료</span>') if course["status"] == "ready" else ""}
                    </div>
                    <p>{html.escape(str(course['summary']))}</p>
                  </div>
                  {action}
                </article>
                """
            )
        if not course_items:
            course_items.append('<div class="empty-state">과목 목록이 확정되면 같은 구조로 추가한다.</div>')

        track_sections.append(
            f"""
            <section id="track-{html.escape(str(track['id']))}" class="track-section">
              <div class="content-wrap">
                <div class="section-heading-row">
                  <div>
                    <span class="small-label">TRACK {index:02d}</span>
                    <h2>{html.escape(str(track['title']))}</h2>
                  </div>
                  <p>{html.escape(str(track['description']))}</p>
                </div>
                <div class="course-list">
                  {''.join(course_items)}
                </div>
              </div>
            </section>
            """
        )

    return shared_head("화이트햇 강의 정리") + f"""
<body>
  <header class="site-header">
    <nav class="top-nav">
      <a class="brand" href="index.html">화이트햇 강의 정리</a>
      <a href="#courses">과목</a>
    </nav>
    <section class="index-hero">
      <div>
        <p class="small-label hero-kicker">이거 언제 다 듣지? 혹시 시간 젠슨 황이세요? 아니라면 이 노트를 보십쇼.</p>
        <h1>화이트햇 강의 요약 노트</h1>
        <p class="lead">강의마다 핵심만 뽑아 정리했습니다. 제가 한건 아니고 AI가요. 화이트햇 4기 화이팅!</p>
        <div class="hero-actions">
          <a class="button primary" href="#courses">과목 보기</a>
          {ready_course_buttons}
        </div>
      </div>
    </section>
  </header>

  <main>
    <span id="tracks" class="skip-anchor" aria-hidden="true"></span>
    <div id="courses">
      {''.join(track_sections)}
    </div>

  </main>
</body>
</html>
"""


def lecture_card_profile_items(lecture: dict) -> list[tuple[str, str]]:
    stats = lecture_content_stats(lecture)
    items: list[tuple[str, str]] = [
        ("섹션", f"{stats['sections']}개"),
        ("복습", f"{len(lecture.get('checks', []))}문항"),
    ]

    focus_items: list[tuple[str, str]] = []
    if stats["code"]:
        focus_items.append(("코드", f"{stats['code']}개"))
    if stats["tables"]:
        focus_items.append(("표", f"{stats['tables']}개"))
    if stats["diagrams"] or stats["timelines"]:
        focus_items.append(("그림", f"{stats['diagrams'] + stats['timelines']}개"))
    if stats["lists"]:
        focus_items.append(("목록", f"{stats['lists']}개"))
    if not focus_items:
        focus_items.append(("개념", "중심"))

    return items + focus_items[:3]


def render_lecture_card_profile(lecture: dict) -> str:
    chips = "".join(
        f"<span><strong>{html.escape(label)}</strong>{html.escape(value)}</span>"
        for label, value in lecture_card_profile_items(lecture)
    )
    return f"""
              <div class="lecture-profile" aria-label="강의 학습 정보">
                {chips}
              </div>
    """


def course_overview_stats(course: dict) -> dict[str, int]:
    lectures = list(course.get("lectures", []))
    totals = {
        "lectures": len(lectures),
        "sections": 0,
        "checks": 0,
        "code": 0,
        "tables": 0,
        "diagrams": 0,
        "timelines": 0,
        "lists": 0,
        "minutes": 0,
    }
    for lecture in lectures:
        stats = lecture_content_stats(lecture)
        totals["sections"] += stats["sections"]
        totals["checks"] += len(lecture.get("checks", []))
        totals["code"] += stats["code"]
        totals["tables"] += stats["tables"]
        totals["diagrams"] += stats["diagrams"]
        totals["timelines"] += stats["timelines"]
        totals["lists"] += stats["lists"]
        totals["minutes"] += max(8, min(65, round(stats["chars"] / 420) + stats["sections"] * 2 + stats["code"] * 3))
    return totals


def course_focus_summary(stats: dict[str, int]) -> list[tuple[str, str]]:
    items = [
        ("코드", stats["code"]),
        ("표", stats["tables"]),
        ("그림/흐름", stats["diagrams"] + stats["timelines"]),
        ("목록", stats["lists"]),
    ]
    present = [(label, count) for label, count in items if count]
    if not present:
        return [("개념 중심", "핵심 문장 위주")]
    return [(label, f"{count}개") for label, count in present[:4]]


def render_course_overview(course: dict) -> str:
    stats = course_overview_stats(course)
    focus_items = "".join(
        f"<span><strong>{html.escape(label)}</strong>{html.escape(str(value))}</span>"
        for label, value in course_focus_summary(stats)
    )
    metric_cards = [
        ("강의", f"{stats['lectures']}개", "순서대로 듣기"),
        ("섹션", f"{stats['sections']}개", "나누어 읽기"),
        ("예상", f"약 {stats['minutes']}분", "2~3회 분할"),
        ("복습", f"{stats['checks']}문항", "질문으로 확인"),
    ]
    metrics = "".join(
        f"""
        <article>
          <span>{html.escape(label)}</span>
          <strong>{html.escape(value)}</strong>
          <p>{html.escape(helper)}</p>
        </article>
        """
        for label, value, helper in metric_cards
    )
    return f"""
    <section class="content-wrap course-overview-panel" aria-label="과목 학습 개요">
      <div class="course-overview-copy">
        <span class="study-card-kicker">과목 학습 개요</span>
        <h2>전체 분량을 보고 오늘 들을 양 정하기</h2>
        <p>강의 목록으로 내려가기 전에 과목 전체의 분량과 학습 유형을 먼저 확인한다.</p>
        <div class="course-focus-strip" aria-label="주요 학습 유형">
          {focus_items}
        </div>
      </div>
      <div class="course-overview-metrics">
        {metrics}
      </div>
    </section>
    """


def render_course_index(course: dict) -> str:
    cards = []
    lectures = course.get("lectures", [])
    unique_tags = sorted({str(tag) for lecture in lectures for tag in lecture.get("tags", [])})
    review_count = sum(len(lecture.get("checks", [])) for lecture in lectures)
    featured_id = course.get("featured_lecture")
    featured = next((lecture for lecture in lectures if lecture["id"] == featured_id), lectures[-1])
    for lecture in lectures:
        lesson_key = f"{course['id']}:{lecture['id']}"
        profile_text = " ".join(
            f"{label} {value}" for label, value in lecture_card_profile_items(lecture)
        )
        lecture_search = " ".join(
            [
                str(lecture.get("id", "")),
                str(lecture.get("title", "")),
                str(lecture.get("subtitle", "")),
                " ".join(str(tag) for tag in lecture.get("tags", [])),
                profile_text,
            ]
        )
        lecture_tags = "|||".join(str(tag).lower() for tag in lecture.get("tags", []))
        cards.append(
            f"""
            <article class="lecture-card" data-course-id="{html.escape(str(course['id']))}" data-lesson-id="{html.escape(str(lecture['id']))}" data-lesson-key="{html.escape(lesson_key)}" data-search-text="{html.escape(lecture_search.lower())}" data-tags="{html.escape(lecture_tags)}">
              <div class="card-top">
                <span class="lecture-id">{html.escape(str(course['short_title']))} {lecture['id']}</span>
                <div class="tag-row">{tag_list(lecture['tags'])}</div>
              </div>
              <h3>{html.escape(lecture['title'])}</h3>
              <p>{html.escape(lecture['subtitle'])}</p>
              {render_lecture_card_profile(lecture)}
              <div class="card-actions">
                <a class="button" href="lectures/{lecture_html_file(lecture)}">강의 정리 보기</a>
                <button class="completion-toggle" type="button" data-lesson-key="{html.escape(lesson_key)}" aria-pressed="false">
                  <span class="completion-dot" aria-hidden="true"></span>
                  <span class="completion-label">완료 표시</span>
                </button>
              </div>
            </article>
            """
        )

    course_map = "".join(
        f"<div><span>{html.escape(item[0])}</span><strong>{html.escape(item[1])}</strong><p>{html.escape(item[2])}</p></div>"
        for item in course.get("map", [])
    )
    flow = "".join(f"<span>{html.escape(item)}</span>" for item in course.get("flow", []))
    tag_filters = "".join(
        f'<button class="filter-chip" type="button" data-lecture-tag-filter="{html.escape(tag.lower())}">{html.escape(tag)}</button>'
        for tag in unique_tags[:18]
    )

    return shared_head(f"{course['title']} 강의 정리", "../../../") + f"""
<body>
  <header class="site-header">
    <nav class="top-nav">
      <a class="brand" href="../../../index.html">화이트햇 강의 정리</a>
      <a href="../../../index.html#tracks">전체 트랙</a>
      <a href="#lectures">강의 목록</a>
      <a href="#map">전체 흐름</a>
    </nav>
    <section class="index-hero">
      <div>
        <p class="small-label">과목 강의 노트</p>
        <h1>{html.escape(str(course['title']))}</h1>
        <p class="lead">{html.escape(str(course['summary']))}</p>
        <div class="hero-actions">
          <a class="button primary" href="#lectures">강의 목록으로 이동</a>
          <a class="button secondary" href="lectures/{lecture_html_file(featured)}">대표 강의 바로가기</a>
        </div>
      </div>
      <aside class="hero-panel">
        <div class="panel-stat"><strong>{len(lectures)}</strong><span>강의</span></div>
        <div class="panel-stat"><strong>{review_count}</strong><span>복습 질문</span></div>
        <div class="mini-flow">
          {flow}
        </div>
      </aside>
    </section>
  </header>

  <main>
    <section class="content-wrap course-routine" aria-label="과목 학습 루틴">
      <article>
        <span>1</span>
        <strong>전체 흐름 보기</strong>
        <p>과목에서 어떤 순서로 개념이 이어지는지 먼저 잡는다.</p>
      </article>
      <article>
        <span>2</span>
        <strong>강의 하나 선택</strong>
        <p>태그와 설명을 보고 지금 필요한 강의부터 들어간다.</p>
      </article>
      <article>
        <span>3</span>
        <strong>복습 질문으로 확인</strong>
        <p>읽고 끝내지 말고 질문에 답하면서 기억을 고정한다.</p>
      </article>
    </section>

    {render_course_overview(course)}

    <section class="content-wrap course-progress-panel" data-course-id="{html.escape(str(course['id']))}" data-course-total="{len(lectures)}" aria-label="과목 학습 진행률">
      <div>
        <span class="study-card-kicker">나의 과목 진행률</span>
        <strong><span data-course-completed>0</span> / <span data-course-total-label>{len(lectures)}</span>강 완료</strong>
        <p>완료 표시는 이 브라우저에 저장된다. 강의를 들은 뒤 카드나 강의 페이지에서 체크하면 된다.</p>
      </div>
      <div class="progress-track"><i data-course-bar></i></div>
    </section>

    <section class="content-wrap finder-panel lecture-finder" data-lecture-finder aria-label="강의 검색과 필터">
      <div class="finder-copy">
        <span class="study-card-kicker">강의 찾기</span>
        <h2>제목, 태그, 완료 상태로 좁히기</h2>
        <p>복습할 강의만 찾거나 아직 안 본 강의만 남겨서 이어 들을 수 있다.</p>
      </div>
      <div class="finder-controls">
        <label class="search-box">
          <span>강의 검색</span>
          <input type="search" data-lecture-search placeholder="예: 포인터, OWASP, TCP">
        </label>
        <div class="filter-row" role="group" aria-label="완료 상태 필터">
          <button class="filter-chip is-active" type="button" data-lecture-status-filter="all">전체</button>
          <button class="filter-chip" type="button" data-lecture-status-filter="remaining">남은 강의</button>
          <button class="filter-chip" type="button" data-lecture-status-filter="done">완료한 강의</button>
        </div>
        <div class="filter-row tag-filter-row" role="group" aria-label="강의 태그 필터">
          <button class="filter-chip is-active" type="button" data-lecture-tag-filter="all">모든 태그</button>
          {tag_filters}
        </div>
        <p class="finder-result"><strong data-lecture-result-count>{len(lectures)}</strong>개 강의 표시 중</p>
        <p class="finder-empty" data-lecture-empty hidden>조건에 맞는 강의가 없다. 검색어를 줄이거나 모든 태그로 바꿔 본다.</p>
      </div>
    </section>

    <section id="map" class="section-band">
      <div class="content-wrap">
        <h2>전체 흐름</h2>
        <p class="section-intro">{html.escape(str(course.get("map_intro", "강의의 핵심 개념, 예시, 실무 맥락을 순서대로 정리한다.")))}</p>
        <div class="course-map">
          {course_map}
        </div>
      </div>
    </section>

    <section id="lectures" class="content-wrap lecture-grid-section">
      <h2>강의별 정리</h2>
      <p class="section-intro">각 강의 페이지에서 학습 목표, 상세 정리, 예시, 복습 질문과 강의 원문을 바로 확인할 수 있다.</p>
      <div class="lecture-grid">
        {''.join(cards)}
      </div>
    </section>

  </main>
</body>
</html>
"""


def render_lecture(lecture: dict, course: dict, transcripts: dict[str, str] | None = None) -> str:
    lectures = course.get("lectures", [])
    transcripts = transcripts or {}
    lecture_terms = emphasis_terms_for(lecture)
    raw_transcript = transcripts.get(str(lecture["id"]), "").strip()
    transcript_nav = '<a href="#transcript">강의 원문</a>' if raw_transcript else ""
    transcript_section = ""
    if raw_transcript:
        transcript_section = f"""
    <section id="transcript" class="content-wrap transcript-wrap">
      <details class="reveal-section">
        <summary>
          <span>
            <strong>강의 원문 보기</strong>
            <small>읽기용 문단 보기와 원문 그대로 보기를 함께 제공한다.</small>
          </span>
        </summary>
        <div class="transcript-reading-panel">
          <div class="transcript-reading-head">
            <span class="study-card-kicker">읽기용 문단 보기</span>
            <p>긴 STT 원문을 문장 흐름에 맞춰 문단으로 나누어 정리본과 비교하기 쉽게 만든 보기다.</p>
          </div>
          <div class="readable-transcript">
            {readable_transcript_block(raw_transcript)}
          </div>
          <details class="raw-transcript-panel">
            <summary>
              <span>
                <strong>원문 그대로 보기</strong>
                <small>STT 원문을 수정하지 않은 형태로 확인한다.</small>
              </span>
            </summary>
            <div class="transcript-text raw-transcript-text">{html.escape(raw_transcript)}</div>
          </details>
        </div>
      </details>
    </section>
        """

    prev_next = []
    idx = lectures.index(lecture)
    if idx > 0:
        prev = lectures[idx - 1]
        prev_next.append(f'<a class="button secondary" href="{lecture_html_file(prev)}">이전: {prev["id"]}</a>')
    prev_next.append('<a class="button secondary" href="../index.html">과목 목록으로</a>')
    if idx < len(lectures) - 1:
        nxt = lectures[idx + 1]
        prev_next.append(f'<a class="button secondary" href="{lecture_html_file(nxt)}">다음: {nxt["id"]}</a>')

    section_nav = "".join(
        f'<a href="#section-{i + 1}">{html.escape(section["heading"])}</a>'
        for i, section in enumerate(lecture["sections"])
    ) + '<a href="#review">복습 체크</a>' + transcript_nav
    side_nav = "".join(
        f"""
        <a{(' class="is-active"' if i == 0 else '')} href="#section-{i + 1}" data-side-section-link="section-{i + 1}">
          <span>{i + 1:02d}</span>
          <strong>{html.escape(section["heading"])}</strong>
        </a>
        """
        for i, section in enumerate(lecture["sections"])
    )
    sections = "".join(
        f"""
        <details id="section-{i + 1}" class="note-section section-disclosure" data-note-section open>
          <summary>
            <span>SECTION {i + 1:02d}</span>
            <h2>{html.escape(section['heading'])}</h2>
          </summary>
          <div class="note-section-body">
            {render_section_body(section, lecture)}
          </div>
        </details>
        """
        for i, section in enumerate(lecture["sections"])
    )
    checks = "".join(f"<li>{emphasize_plain_text(item, lecture_terms)}</li>" for item in lecture["checks"])
    objectives = "".join(f"<li>{emphasize_plain_text(item, lecture_terms)}</li>" for item in lecture["objectives"])
    lecture_label = f"{course['short_title']} {lecture['id']}"
    lesson_key = f"{course['id']}:{lecture['id']}"
    subtitle = emphasize_plain_text(lecture["subtitle"], lecture_terms)

    return shared_head(f"{course['title']} {lecture['id']} - {lecture['title']}", "../../../../") + f"""
<body data-course-id="{html.escape(str(course['id']))}" data-lesson-id="{html.escape(str(lecture['id']))}" data-lesson-key="{html.escape(lesson_key)}" data-lesson-title="{html.escape(str(lecture['title']))}" data-lesson-label="{html.escape(lecture_label)}">
  <header class="site-header lecture-header">
    <nav class="top-nav">
	      <a class="brand" href="../../../../index.html">화이트햇 강의 정리</a>
	      <a href="../index.html#lectures">과목 강의 목록</a>
	      <a href="#review">복습 체크</a>
	      {transcript_nav}
	    </nav>
    <section class="lecture-hero">
      <div>
        <p class="small-label">{html.escape(lecture_label)}</p>
        <h1>{html.escape(lecture['title'])}</h1>
        <p class="lead">{subtitle}</p>
        <div class="tag-row large">{tag_list(lecture['tags'])}</div>
      </div>
      <aside class="toc-box">
        <strong>페이지 목차</strong>
        {section_nav}
      </aside>
    </section>
  </header>

  <main class="lecture-main">
    <section class="content-wrap lesson-status-panel" aria-label="현재 강의 완료 상태">
      <div>
        <span class="study-card-kicker">현재 강의</span>
        <strong>{html.escape(lecture_label)} 완료 상태</strong>
        <p>정리와 복습 질문까지 확인했다면 완료로 표시해 둔다.</p>
      </div>
      <button class="completion-toggle large" type="button" data-lesson-key="{html.escape(lesson_key)}" aria-pressed="false">
        <span class="completion-dot" aria-hidden="true"></span>
        <span class="completion-label">완료 표시</span>
      </button>
    </section>

    {render_lecture_control_panel(lecture, transcript_nav)}

    <section id="goals" class="content-wrap intro-grid">
      <article class="note-block">
        <h2>학습 목표</h2>
        <ul class="check-list">{objectives}</ul>
      </article>
    </section>

    <div class="content-wrap lecture-study-layout">
      <aside class="lecture-side-guide" data-lecture-side-guide aria-label="상세 정리 섹션 길잡이">
        <div class="side-guide-head">
          <span data-side-current>SECTION 01</span>
          <strong>상세 정리 길잡이</strong>
          <p>{len(lecture["sections"])}개 섹션을 따라가며 현재 읽는 위치를 확인한다.</p>
        </div>
        <nav class="side-guide-links" aria-label="상세 정리 바로가기">
          {side_nav}
        </nav>
      </aside>
      <div class="notes-layout">
        {sections}
      </div>
    </div>

	    <section id="review" class="content-wrap note-block">
	      <h2>복습 체크</h2>
	      <ul class="check-list">{checks}</ul>
	    </section>

	    {transcript_section}

	    <nav class="content-wrap page-nav">
	      {''.join(prev_next)}
    </nav>
  </main>
</body>
</html>
"""


def write_styles() -> None:
    ASSET_DIR.mkdir(exist_ok=True)
    styles_path = ASSET_DIR / "styles.css"
    if styles_path.exists():
        return

    styles_path.write_text(
        dedent(
            """
            :root {
              --bg: #f6f7f9;
              --paper: #ffffff;
              --ink: #172033;
              --muted: #5e6a7d;
              --line: #dce3ea;
              --soft-line: #edf1f4;
              --green: #147d64;
              --green-dark: #0f5f4d;
              --amber: #b86b0e;
              --rose: #a33d4b;
              --blue: #28587b;
              --code-bg: #111827;
              --code-text: #f4f7fb;
              --code-label-bg: #1f2937;
              --code-line: #5f6f89;
              --tok-keyword: #ff7ab6;
              --tok-type: #7dd3fc;
              --tok-string: #f9c74f;
              --tok-comment: #94a3b8;
              --tok-number: #c4b5fd;
              --tok-function: #93c5fd;
              --tok-variable: #a7f3d0;
              --tok-operator: #fca5a5;
              --tok-preprocessor: #fdba74;
              --tok-option: #86efac;
              --tok-register: #fda4af;
              --shadow: 0 18px 45px rgba(23, 32, 51, 0.08);
              --radius: 8px;
            }

            * { box-sizing: border-box; }

            html { scroll-behavior: smooth; }

            body {
              margin: 0;
              font-family: -apple-system, BlinkMacSystemFont, "Apple SD Gothic Neo", "Noto Sans KR", "Segoe UI", sans-serif;
              background: var(--bg);
              color: var(--ink);
              line-height: 1.72;
              letter-spacing: 0;
            }

            a { color: inherit; }

            .site-header {
              background: var(--paper);
              border-bottom: 1px solid var(--line);
            }

            .top-nav {
              width: min(1120px, calc(100% - 32px));
              margin: 0 auto;
              min-height: 64px;
              display: flex;
              align-items: center;
              gap: 22px;
              font-size: 14px;
              color: var(--muted);
            }

            .top-nav a {
              text-decoration: none;
            }

            .top-nav .brand {
              margin-right: auto;
              font-weight: 800;
              color: var(--ink);
              font-size: 16px;
            }

            .index-hero,
            .lecture-hero {
              width: min(1120px, calc(100% - 32px));
              margin: 0 auto;
              padding: 54px 0 58px;
              display: grid;
              grid-template-columns: minmax(0, 1fr) 340px;
              gap: 42px;
              align-items: center;
            }

            .lecture-hero {
              grid-template-columns: minmax(0, 1fr) 300px;
              padding-bottom: 44px;
            }

            .small-label {
              margin: 0 0 14px;
              color: var(--green-dark);
              font-size: 13px;
              font-weight: 800;
              text-transform: uppercase;
            }

            .index-hero .hero-kicker {
              max-width: 980px;
              font-size: calc(15px + 7pt);
              line-height: 1.45;
            }

            h1, h2, h3 {
              margin: 0;
              line-height: 1.22;
              letter-spacing: 0;
            }

            h1 {
              max-width: 840px;
              font-size: clamp(34px, 5vw, 60px);
              font-weight: 850;
            }

            h2 {
              font-size: clamp(24px, 3vw, 34px);
              margin-bottom: 14px;
            }

            h3 {
              font-size: 21px;
              margin-bottom: 10px;
            }

            .lead {
              margin: 20px 0 0;
              max-width: 760px;
              color: var(--muted);
              font-size: 18px;
            }

            .hero-actions {
              display: flex;
              flex-wrap: wrap;
              gap: 12px;
              margin-top: 28px;
            }

            .button {
              display: inline-flex;
              align-items: center;
              justify-content: center;
              min-height: 42px;
              padding: 0 16px;
              border-radius: var(--radius);
              border: 1px solid var(--line);
              background: var(--paper);
              color: var(--ink);
              text-decoration: none;
              font-size: 14px;
              font-weight: 750;
              transition: transform 150ms ease, border-color 150ms ease, background 150ms ease;
            }

            .button:hover {
              transform: translateY(-1px);
              border-color: var(--green);
            }

            .button.primary {
              background: var(--green);
              border-color: var(--green);
              color: #fff;
            }

            .button.secondary {
              background: #f9fbfb;
            }

            .hero-panel,
            .toc-box,
            .note-block,
            .lecture-card,
            .note-section,
            .transcript-wrap details {
              background: var(--paper);
              border: 1px solid var(--line);
              border-radius: var(--radius);
              box-shadow: var(--shadow);
            }

            .hero-panel {
              padding: 24px;
            }

            .panel-stat {
              display: flex;
              align-items: baseline;
              justify-content: space-between;
              padding: 14px 0;
              border-bottom: 1px solid var(--soft-line);
            }

            .panel-stat strong {
              font-size: 34px;
              line-height: 1;
              color: var(--green-dark);
            }

            .panel-stat span {
              color: var(--muted);
              font-weight: 700;
            }

            .mini-flow {
              display: grid;
              grid-template-columns: repeat(5, 1fr);
              gap: 6px;
              margin-top: 22px;
            }

            .mini-flow span {
              padding: 10px 6px;
              border-radius: 6px;
              text-align: center;
              background: #eef6f2;
              color: var(--green-dark);
              font-size: 12px;
              font-weight: 800;
            }

            .content-wrap {
              width: min(1120px, calc(100% - 32px));
              margin: 0 auto;
            }

            .section-band {
              background: #eef3f1;
              border-top: 1px solid var(--line);
              border-bottom: 1px solid var(--line);
              padding: 58px 0;
            }

            .section-intro {
              margin: 0 0 24px;
              max-width: 760px;
              color: var(--muted);
              font-size: 17px;
            }

            .track-grid-section {
              padding: 58px 0 28px;
            }

            .track-grid {
              display: grid;
              grid-template-columns: repeat(4, 1fr);
              gap: 16px;
            }

            .track-card {
              min-height: 230px;
              padding: 22px;
              background: var(--paper);
              border: 1px solid var(--line);
              border-radius: var(--radius);
              box-shadow: var(--shadow);
              display: flex;
              flex-direction: column;
            }

            .track-card strong {
              display: block;
              margin: 12px 0 2px;
              font-size: 38px;
              line-height: 1;
              color: var(--ink);
            }

            .track-card p {
              margin: 0;
              color: var(--muted);
              font-size: 14px;
            }

            .track-card .button {
              margin-top: auto;
              width: fit-content;
            }

            .track-section {
              padding: 44px 0;
              border-top: 1px solid var(--line);
            }

            .track-section:nth-child(even) {
              background: #eef3f1;
            }

            .section-heading-row {
              display: grid;
              grid-template-columns: minmax(0, 0.85fr) minmax(0, 1.15fr);
              gap: 28px;
              align-items: end;
              margin-bottom: 20px;
            }

            .section-heading-row p {
              margin: 0;
              color: var(--muted);
            }

            .course-list {
              display: grid;
              gap: 12px;
            }

            .course-item {
              display: grid;
              grid-template-columns: minmax(0, 1fr) auto;
              gap: 18px;
              align-items: center;
              padding: 18px 20px;
              background: var(--paper);
              border: 1px solid var(--line);
              border-radius: var(--radius);
              box-shadow: var(--shadow);
            }

            .course-item-head {
              display: flex;
              flex-wrap: wrap;
              gap: 10px;
              align-items: center;
              margin-bottom: 8px;
            }

            .course-item h3 {
              margin: 0;
              font-size: 20px;
            }

            .course-item p {
              margin: 0;
              color: var(--muted);
              font-size: 14px;
            }

            .status-pill {
              display: inline-flex;
              align-items: center;
              min-height: 26px;
              padding: 0 9px;
              border-radius: 999px;
              font-size: 12px;
              font-weight: 850;
            }

            .status-ready {
              background: #eef6f2;
              color: var(--green-dark);
            }

            .status-pending {
              background: #f5f1e8;
              color: var(--amber);
            }

            .status-note,
            .empty-state {
              color: var(--muted);
              font-size: 14px;
              font-weight: 750;
            }

            .empty-state {
              padding: 18px 20px;
              background: var(--paper);
              border: 1px dashed var(--line);
              border-radius: var(--radius);
            }

            .course-map {
              display: grid;
              grid-template-columns: repeat(5, 1fr);
              gap: 12px;
            }

            .course-map div {
              background: var(--paper);
              border: 1px solid var(--line);
              border-radius: var(--radius);
              padding: 18px;
              min-height: 158px;
            }

            .course-map span,
            .lecture-id {
              display: block;
              color: var(--amber);
              font-size: 13px;
              font-weight: 850;
              margin-bottom: 10px;
            }

            .course-map strong {
              display: block;
              font-size: 18px;
              line-height: 1.3;
              margin-bottom: 10px;
            }

            .course-map p,
            .lecture-card p {
              margin: 0;
              color: var(--muted);
              font-size: 14px;
            }

            .lecture-grid-section {
              padding: 58px 0;
            }

            .lecture-grid {
              display: grid;
              grid-template-columns: repeat(4, 1fr);
              gap: 16px;
            }

            .lecture-card {
              padding: 20px;
              min-height: 276px;
              display: flex;
              flex-direction: column;
            }

            .lecture-card .button {
              margin-top: auto;
              width: fit-content;
            }

            .card-top {
              margin-bottom: 14px;
            }

            .tag-row {
              display: flex;
              flex-wrap: wrap;
              gap: 6px;
            }

            .tag-row span {
              display: inline-flex;
              align-items: center;
              min-height: 26px;
              padding: 0 9px;
              border-radius: 999px;
              background: #eef6f2;
              color: var(--green-dark);
              font-size: 12px;
              font-weight: 800;
            }

            .tag-row.large {
              margin-top: 22px;
            }

            .note-block {
              padding: 24px;
              margin-bottom: 42px;
            }

            .note-block h2 {
              font-size: 24px;
            }

            .lecture-main {
              padding: 42px 0 70px;
            }

            .intro-grid {
              display: grid;
              grid-template-columns: 1fr;
              gap: 18px;
            }

            .compact-source p {
              margin-bottom: 0;
            }

            .toc-box {
              padding: 20px;
              align-self: start;
            }

            .toc-box strong {
              display: block;
              margin-bottom: 12px;
              font-size: 14px;
            }

            .toc-box a {
              display: block;
              padding: 8px 0;
              color: var(--muted);
              font-size: 14px;
              text-decoration: none;
              border-top: 1px solid var(--soft-line);
            }

            .toc-box a:hover {
              color: var(--green-dark);
            }

            .notes-layout {
              display: grid;
              gap: 22px;
            }

            .note-section {
              padding: 30px;
            }

            .note-section h2 {
              padding-bottom: 12px;
              border-bottom: 1px solid var(--soft-line);
            }

            .note-section p,
            .note-block p {
              margin: 16px 0 0;
            }

            ul, ol {
              margin: 16px 0 0;
              padding-left: 22px;
            }

            li + li {
              margin-top: 8px;
            }

            .check-list {
              padding-left: 0;
              list-style: none;
            }

            .check-list li {
              position: relative;
              padding-left: 24px;
            }

            .check-list li::before {
              content: "";
              position: absolute;
              left: 0;
              top: 0.72em;
              width: 9px;
              height: 9px;
              border-radius: 50%;
              background: var(--green);
            }

            table {
              width: 100%;
              margin-top: 18px;
              border-collapse: collapse;
              overflow: hidden;
              border: 1px solid var(--line);
              border-radius: var(--radius);
              font-size: 15px;
            }

            th, td {
              padding: 13px 14px;
              border-bottom: 1px solid var(--soft-line);
              vertical-align: top;
              text-align: left;
            }

            th {
              background: #f1f5f8;
              color: var(--ink);
              font-weight: 850;
            }

            tr:last-child td {
              border-bottom: 0;
            }

            code {
              font-family: "SFMono-Regular", Consolas, "Liberation Mono", monospace;
              font-size: 0.92em;
              padding: 0.1em 0.32em;
              border-radius: 5px;
              background: #edf1f5;
            }

            pre {
              position: relative;
              margin: 18px 0 0;
              padding: 18px;
              overflow-x: auto;
              border-radius: var(--radius);
              border: 1px solid rgba(148, 163, 184, 0.22);
              background: var(--code-bg);
              color: var(--code-text);
              line-height: 1.55;
              font-size: 14px;
            }

            pre[data-language] {
              padding-top: 48px;
            }

            pre[data-language]::before {
              content: attr(data-language);
              position: absolute;
              top: 0;
              left: 0;
              right: 0;
              height: 34px;
              display: flex;
              align-items: center;
              padding: 0 18px;
              background: var(--code-label-bg);
              color: #dbeafe;
              font-size: 12px;
              font-weight: 850;
              letter-spacing: 0;
              text-transform: uppercase;
              border-bottom: 1px solid rgba(148, 163, 184, 0.22);
            }

            pre code {
              display: block;
              min-width: max-content;
              counter-reset: code-line;
              padding: 0;
              background: transparent;
              color: inherit;
              font-size: inherit;
            }

            .code-line {
              display: block;
              position: relative;
              min-height: 1.55em;
              padding-left: 3.2rem;
              white-space: pre;
              counter-increment: code-line;
            }

            .code-line::before {
              content: counter(code-line);
              position: absolute;
              left: 0;
              width: 2.2rem;
              color: var(--code-line);
              text-align: right;
              user-select: none;
            }

            .tok-keyword { color: var(--tok-keyword); font-weight: 700; }
            .tok-type { color: var(--tok-type); font-weight: 700; }
            .tok-string { color: var(--tok-string); }
            .tok-comment { color: var(--tok-comment); font-style: italic; }
            .tok-number { color: var(--tok-number); }
            .tok-function { color: var(--tok-function); }
            .tok-variable { color: var(--tok-variable); }
            .tok-operator { color: var(--tok-operator); }
            .tok-preprocessor { color: var(--tok-preprocessor); font-weight: 700; }
            .tok-option { color: var(--tok-option); }
            .tok-register { color: var(--tok-register); font-weight: 700; }

            .diagram {
              display: flex;
              align-items: stretch;
              gap: 12px;
              margin-top: 18px;
            }

            .diagram > div {
              flex: 1;
              border: 1px solid var(--line);
              border-radius: var(--radius);
              padding: 16px;
              background: #fbfcfd;
            }

            .diagram.two-col,
            .diagram.three-col {
              display: grid;
            }

            .diagram.two-col {
              grid-template-columns: repeat(2, 1fr);
            }

            .diagram.three-col {
              grid-template-columns: repeat(3, 1fr);
            }

            .node-title {
              display: block;
              margin-bottom: 8px;
              color: var(--blue);
              font-weight: 850;
            }

            .arrow {
              display: flex;
              align-items: center;
              color: var(--amber);
              font-weight: 900;
            }

            .timeline {
              display: grid;
              gap: 12px;
              margin-top: 18px;
            }

            .timeline div {
              padding: 16px;
              border: 1px solid var(--line);
              border-left: 5px solid var(--green);
              border-radius: var(--radius);
              background: #fbfcfd;
            }

            .timeline.compact div {
              border-left-color: var(--amber);
            }

            .timeline strong {
              display: block;
              margin-bottom: 6px;
            }

            .timeline p,
            .diagram p {
              margin: 0;
              color: var(--muted);
            }

            .callout {
              margin-top: 18px;
              padding: 16px;
              border-left: 5px solid var(--rose);
              background: #fff6f7;
              border-radius: var(--radius);
              color: #6d2430;
              font-weight: 650;
            }

            .transcript-wrap {
              margin-top: 34px;
            }

            .reveal-section,
            .transcript-wrap details {
              padding: 0;
              overflow: hidden;
            }

            .reveal-section summary {
              cursor: pointer;
              list-style: none;
              display: flex;
              align-items: center;
              justify-content: space-between;
              gap: 16px;
              padding: 18px 22px;
              background: #f1f5f8;
              border: 0;
            }

            .reveal-section summary::-webkit-details-marker {
              display: none;
            }

            .reveal-section summary span {
              display: grid;
              gap: 3px;
              min-width: 0;
            }

            .reveal-section summary strong {
              color: var(--ink);
              font-size: 18px;
              font-weight: 850;
              line-height: 1.25;
            }

            .reveal-section summary small {
              color: var(--muted);
              font-size: 13px;
              font-weight: 650;
              line-height: 1.35;
            }

            .reveal-section summary::after {
              content: "펼치기";
              flex: 0 0 auto;
              min-width: 72px;
              min-height: 34px;
              display: inline-flex;
              align-items: center;
              justify-content: center;
              padding: 0 12px;
              border-radius: var(--radius);
              background: var(--green);
              color: #ffffff;
              font-size: 13px;
              font-weight: 850;
            }

            .reveal-section[open] summary::after {
              content: "접기";
              background: #e7f3ee;
              color: var(--green-dark);
            }

            .reveal-body {
              padding: 24px;
              border-top: 1px solid var(--line);
            }

            .reveal-body > p:first-child {
              margin-top: 0;
            }

            .transcript-text {
              padding: 24px;
              max-height: 520px;
              overflow: auto;
              white-space: pre-wrap;
              overflow-wrap: anywhere;
              color: var(--muted);
              font-size: 14px;
              line-height: 1.8;
              border-top: 1px solid var(--line);
            }

            .readable-transcript {
              margin-top: 18px;
              padding: 20px;
              background: #ffffff;
              border: 1px solid var(--soft-line);
              border-radius: var(--radius);
              color: #263246;
              font-size: 15px;
              line-height: 1.82;
            }

            .transcript-text .readable-transcript {
              margin-top: 0;
            }

            .readable-transcript p {
              margin: 0;
            }

            .readable-transcript p + p {
              margin-top: 14px;
              padding-top: 14px;
              border-top: 1px solid var(--soft-line);
            }

            .page-nav {
              display: flex;
              justify-content: center;
              gap: 10px;
              flex-wrap: wrap;
              margin-top: 30px;
            }

            .content-wrap,
            .note-block,
            .note-section,
            .lecture-card,
            .course-item,
            .toc-box,
            .timeline,
            .diagram,
            .course-map {
              min-width: 0;
            }

            .note-block,
            .note-section,
            .lecture-card,
            .course-item,
            .toc-box {
              overflow-wrap: anywhere;
            }

            .note-section p,
            .note-block p,
            .lecture-card p,
            .course-item p,
            .note-section strong,
            .note-block strong,
            .lecture-card strong,
            .course-item strong {
              min-width: 0;
              overflow-wrap: anywhere;
            }

            @media (max-width: 980px) {
              .index-hero,
              .lecture-hero,
              .intro-grid {
                grid-template-columns: 1fr;
              }

              .course-map,
              .track-grid,
              .lecture-grid {
                grid-template-columns: repeat(2, 1fr);
              }

              .section-heading-row {
                grid-template-columns: 1fr;
              }

              .toc-box {
                display: grid;
                grid-template-columns: repeat(2, 1fr);
                gap: 0 16px;
              }

              .toc-box strong {
                grid-column: 1 / -1;
              }
            }

            @media (max-width: 680px) {
              .top-nav {
                gap: 14px;
                overflow-x: auto;
              }

              .index-hero,
              .lecture-hero {
                padding: 34px 0 38px;
              }

              h1 {
                font-size: 34px;
              }

              .course-map,
              .track-grid,
              .lecture-grid,
              .diagram.two-col,
              .diagram.three-col,
              .toc-box {
                grid-template-columns: 1fr;
              }

              .course-item {
                grid-template-columns: 1fr;
              }

              .diagram {
                flex-direction: column;
              }

              .arrow {
                justify-content: center;
              }

              .note-section,
              .note-block {
                padding: 20px;
              }

              table {
                display: block;
                overflow-x: auto;
                max-width: 100%;
                white-space: nowrap;
              }
            }
            """
        ).strip()
        + "\n",
        encoding="utf-8",
    )


def write_code_highlighter() -> None:
    ASSET_DIR.mkdir(exist_ok=True)
    (ASSET_DIR / "code-highlight.js").write_text(
        dedent(
            r"""
            (() => {
              const labels = {
                asm: "Assembly",
                bash: "Bash",
                c: "C",
                cpp: "C++",
                javascript: "JavaScript",
                js: "JavaScript",
                python: "Python",
                py: "Python",
                shell: "Shell",
                sh: "Shell",
                sql: "SQL",
                text: "Text",
                txt: "Text",
              };

              const escapeMap = {
                "&": "&amp;",
                "<": "&lt;",
                ">": "&gt;",
                '"': "&quot;",
                "'": "&#39;",
              };

              const escapeHtml = (value) => value.replace(/[&<>"']/g, (char) => escapeMap[char]);

              const escapeRegex = (value) => value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");

              const keywordRegex = (words) => new RegExp(`\\b(?:${words.map(escapeRegex).join("|")})\\b`, "g");

              const splitByRegex = (segments, regex, className) => {
                const next = [];
                for (const segment of segments) {
                  if (segment.className !== "plain") {
                    next.push(segment);
                    continue;
                  }

                  let lastIndex = 0;
                  let matched = false;
                  for (const match of segment.text.matchAll(regex)) {
                    const value = match[0];
                    const index = match.index ?? 0;
                    if (!value) {
                      continue;
                    }
                    if (index > lastIndex) {
                      next.push({ className: "plain", text: segment.text.slice(lastIndex, index) });
                    }
                    next.push({ className, text: value });
                    lastIndex = index + value.length;
                    matched = true;
                  }

                  if (lastIndex < segment.text.length) {
                    next.push({ className: "plain", text: segment.text.slice(lastIndex) });
                  }
                  if (!matched && segment.text.length === 0) {
                    next.push(segment);
                  }
                }
                return next;
              };

              const renderSegments = (segments) =>
                segments
                  .map((segment) => {
                    const text = escapeHtml(segment.text);
                    return segment.className === "plain" ? text : `<span class="tok-${segment.className}">${text}</span>`;
                  })
                  .join("");

              const highlightWithRules = (line, rules) => {
                let segments = [{ className: "plain", text: line }];
                for (const [regex, className] of rules) {
                  segments = splitByRegex(segments, regex, className);
                }
                return renderSegments(segments);
              };

              const cRules = [
                [/^\s*#\s*[A-Za-z_]\w*[^\n]*/g, "preprocessor"],
                [/\/\*.*?\*\/|\/\/.*/g, "comment"],
                [/"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*'/g, "string"],
                [/\b(?:0x[0-9A-Fa-f]+|\d+(?:\.\d+)?(?:[uUlLfF]+)?)\b/g, "number"],
                [
                  keywordRegex([
                    "auto",
                    "break",
                    "case",
                    "char",
                    "const",
                    "continue",
                    "default",
                    "do",
                    "double",
                    "else",
                    "enum",
                    "extern",
                    "float",
                    "for",
                    "goto",
                    "if",
                    "int",
                    "long",
                    "register",
                    "return",
                    "short",
                    "signed",
                    "sizeof",
                    "static",
                    "struct",
                    "switch",
                    "typedef",
                    "union",
                    "unsigned",
                    "void",
                    "volatile",
                    "while",
                  ]),
                  "keyword",
                ],
                [/\b[A-Za-z_]\w*(?=\s*\()/g, "function"],
                [/[{}()[\];,.+\-*/%=&|!<>^~?:]+/g, "operator"],
              ];

              const pythonRules = [
                [/"{3}.*?"{3}|'{3}.*?'{3}|"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*'/g, "string"],
                [/#.*/g, "comment"],
                [/^\s*@\w+(?:\.\w+)*/g, "preprocessor"],
                [/\b(?:0x[0-9A-Fa-f]+|\d+(?:\.\d+)?)\b/g, "number"],
                [
                  keywordRegex([
                    "False",
                    "None",
                    "True",
                    "and",
                    "as",
                    "assert",
                    "async",
                    "await",
                    "break",
                    "class",
                    "continue",
                    "def",
                    "del",
                    "elif",
                    "else",
                    "except",
                    "finally",
                    "for",
                    "from",
                    "global",
                    "if",
                    "import",
                    "in",
                    "is",
                    "lambda",
                    "nonlocal",
                    "not",
                    "or",
                    "pass",
                    "raise",
                    "return",
                    "try",
                    "while",
                    "with",
                    "yield",
                  ]),
                  "keyword",
                ],
                [/\b(?:AF_INET|SOCK_DGRAM|SOCK_STREAM|print|range|len|str|int|float|list|dict|set|tuple|socket)\b/g, "type"],
                [/\b[A-Za-z_]\w*(?=\s*\()/g, "function"],
                [/[{}()[\];,.+\-*/%=&|!<>^~:]+/g, "operator"],
              ];

              const bashRules = [
                [/"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*'/g, "string"],
                [/(^|\s)#.*/g, "comment"],
                [/\$\{[^}]+\}|\$\([^)]+\)|\$[A-Za-z_][A-Za-z0-9_]*|\$[0-9?@#]/g, "variable"],
                [/(^|\s)-{1,2}[A-Za-z0-9][A-Za-z0-9_-]*/g, "option"],
                [/\b(?:sudo|apt|apt-get|systemctl|journalctl|service|ls|pwd|cd|cp|mv|rm|mkdir|rmdir|touch|cat|echo|chmod|chown|grep|find|curl|ping|kill|ps|jobs|last|users|whoami|ifconfig|arp|gcc|g\+\+|make|python|python3|conda|jupyter|docker|vim|vi|nano|vimtutor|mysql|nginx|apache2|vsftpd|ftp|put|get|break|clear|file|man|df|ssh)\b/g, "function"],
                [/\b\d+(?:\.\d+)?\b/g, "number"],
                [/[|&;<>]=?|={1,2}/g, "operator"],
              ];

              const sqlRules = [
                [/"(?:\\.|[^"\\])*"|'(?:\\.|[^'\\])*'/g, "string"],
                [/--.*|\/\*.*?\*\//g, "comment"],
                [/\b\d+(?:\.\d+)?\b/g, "number"],
                [
                  keywordRegex([
                    "ADD",
                    "ALTER",
                    "AND",
                    "AS",
                    "BY",
                    "CREATE",
                    "DATABASE",
                    "DELETE",
                    "DROP",
                    "FROM",
                    "GRANT",
                    "GROUP",
                    "IDENTIFIED",
                    "INSERT",
                    "INTO",
                    "JOIN",
                    "ON",
                    "OR",
                    "ORDER",
                    "SELECT",
                    "SET",
                    "SHOW",
                    "TABLE",
                    "TO",
                    "UPDATE",
                    "USE",
                    "USER",
                    "VALUES",
                    "WHERE",
                  ]),
                  "keyword",
                ],
                [/\b(?:sudo|apt|mysql|systemctl)\b/g, "function"],
                [/[{}()[\];,.+\-*/%=&|!<>^~]+/g, "operator"],
              ];

              const asmRules = [
                [/;.*/g, "comment"],
                [/\b(?:mov|add|sub|mul|div|push|pop|call|ret|cmp|jmp|je|jne|jg|jl|and|or|xor|lea|int|nop)\b/gi, "keyword"],
                [/\b(?:eax|ebx|ecx|edx|esi|edi|esp|ebp|rax|rbx|rcx|rdx|rsi|rdi|rsp|rbp|ax|bx|cx|dx|al|bl|cl|dl)\b/gi, "register"],
                [/\b(?:0x[0-9A-Fa-f]+|\d+)\b/g, "number"],
                [/[{}()[\];,.+\-*/%=&|!<>^~:]+/g, "operator"],
              ];

              const rulesByLanguage = {
                asm: asmRules,
                bash: bashRules,
                c: cRules,
                cpp: cRules,
                javascript: cRules,
                js: cRules,
                python: pythonRules,
                py: pythonRules,
                shell: bashRules,
                sh: bashRules,
                sql: sqlRules,
              };

              const normalizeLanguage = (code) => {
                const languageClass = [...code.classList].find((className) => className.startsWith("language-"));
                return languageClass ? languageClass.replace("language-", "").toLowerCase() : "text";
              };

              const highlightLine = (line, language) => {
                const rules = rulesByLanguage[language];
                return rules ? highlightWithRules(line, rules) : escapeHtml(line);
              };

              const highlightBlock = (code) => {
                if (code.dataset.highlighted === "true") {
                  return;
                }

                const language = normalizeLanguage(code);
                const pre = code.closest("pre");
                if (pre) {
                  pre.dataset.language = labels[language] || language.toUpperCase();
                }

                const source = code.textContent.replace(/\n$/, "");
                const lines = source.split("\n");
                code.innerHTML = lines
                  .map((line) => `<span class="code-line">${highlightLine(line, language)}</span>`)
                  .join("");
                code.dataset.highlighted = "true";
              };

              document.querySelectorAll("pre code").forEach(highlightBlock);
            })();
            """
        ).strip()
        + "\n",
        encoding="utf-8",
    )


def write_study_state_script() -> None:
    ASSET_DIR.mkdir(exist_ok=True)
    (ASSET_DIR / "study-state.js").write_text(
        dedent(
            r"""
            (() => {
              const progressStorageKey = "whitehatLectureProgress.v1";

              const safeRead = (key) => {
                try {
                  return JSON.parse(localStorage.getItem(key) || "{}");
                } catch {
                  return {};
                }
              };

              const safeWrite = (key, state) => {
                try {
                  localStorage.setItem(key, JSON.stringify(state));
                } catch {
                  // The UI still works for the current page even when storage is unavailable.
                }
              };

              const getCourseId = (lessonKey) => String(lessonKey || "").split(":")[0];

              const setButtonState = (button, isComplete) => {
                button.setAttribute("aria-pressed", String(isComplete));
                button.classList.toggle("is-complete", isComplete);
                const label = button.querySelector(".completion-label");
                if (label) {
                  label.textContent = isComplete ? "완료됨" : "완료 표시";
                }
              };

              const knownCourseTotals = () =>
                [...document.querySelectorAll("[data-course-progress-target], .course-progress-panel")]
                  .map((element) => ({
                    courseId: element.dataset.courseId,
                    total: Number(element.dataset.courseTotal || 0),
                  }))
                  .filter((item) => item.courseId && item.total > 0);

              const countCompleted = (state, courseId) =>
                Object.keys(state).filter((key) => state[key] && (!courseId || getCourseId(key) === courseId)).length;

              const updateCourseProgress = (state) => {
                for (const item of knownCourseTotals()) {
                  const completed = Math.min(countCompleted(state, item.courseId), item.total);
                  const percent = item.total ? Math.round((completed / item.total) * 100) : 0;

                  document
                    .querySelectorAll(`[data-course-id="${CSS.escape(item.courseId)}"][data-course-progress-target]`)
                    .forEach((element) => {
                      element.dataset.progressPercent = String(percent);
                      const label = element.querySelector("[data-course-progress-label]");
                      if (label) {
                        label.textContent = `${completed}/${item.total} 완료`;
                      }
                    });

                  document
                    .querySelectorAll(`.course-progress-panel[data-course-id="${CSS.escape(item.courseId)}"]`)
                    .forEach((panel) => {
                      const completedLabel = panel.querySelector("[data-course-completed]");
                      const totalLabel = panel.querySelector("[data-course-total-label]");
                      const bar = panel.querySelector("[data-course-bar]");
                      if (completedLabel) completedLabel.textContent = String(completed);
                      if (totalLabel) totalLabel.textContent = String(item.total);
                      if (bar) bar.style.setProperty("--progress", `${percent}%`);
                    });
                }
              };

              const updateOverallProgress = (state) => {
                const totalElement = document.querySelector("[data-total-lectures]");
                if (!totalElement) {
                  return;
                }

                const total = Number(totalElement.dataset.totalLectures || 0);
                const completed = Math.min(countCompleted(state), total);
                const percent = total ? Math.round((completed / total) * 100) : 0;
                const completedLabel = document.querySelector("[data-overall-completed]");
                const totalLabel = document.querySelector("[data-overall-total]");
                const bar = document.querySelector("[data-overall-bar]");
                if (completedLabel) completedLabel.textContent = String(completed);
                if (totalLabel) totalLabel.textContent = String(total);
                if (bar) bar.style.setProperty("--progress", `${percent}%`);
              };

              const applyState = (state) => {
                document.querySelectorAll("[data-lesson-key]").forEach((element) => {
                  const key = element.dataset.lessonKey;
                  const isComplete = Boolean(state[key]);
                  element.classList.toggle("is-complete", isComplete);
                });

                document.querySelectorAll(".completion-toggle[data-lesson-key]").forEach((button) => {
                  setButtonState(button, Boolean(state[button.dataset.lessonKey]));
                });

                updateCourseProgress(state);
                updateOverallProgress(state);
                document.dispatchEvent(new CustomEvent("whitehat-progress-change"));
              };

              const bindToggles = (state) => {
                document.querySelectorAll(".completion-toggle[data-lesson-key]").forEach((button) => {
                  button.addEventListener("click", () => {
                    const key = button.dataset.lessonKey;
                    if (!key) {
                      return;
                    }
                    state[key] = !state[key];
                    if (!state[key]) {
                      delete state[key];
                    }
                    safeWrite(progressStorageKey, state);
                    applyState(state);
                  });
                });
              };

              document.addEventListener("DOMContentLoaded", () => {
                const state = safeRead(progressStorageKey);
                bindToggles(state);
                applyState(state);
              });
            })();
            """
        ).strip()
        + "\n",
        encoding="utf-8",
    )


def write_study_tools_script() -> None:
    ASSET_DIR.mkdir(exist_ok=True)
    (ASSET_DIR / "study-tools.js").write_text(
        dedent(
            r"""
            (() => {
              const normalize = (value) => String(value || "").trim().toLowerCase();

              const setActive = (buttons, activeButton) => {
                buttons.forEach((button) => button.classList.toggle("is-active", button === activeButton));
              };

              const setupCourseFinder = () => {
                const root = document.querySelector("[data-course-finder]");
                if (!root) {
                  return;
                }

                const input = root.querySelector("[data-course-search]");
                const statusButtons = [...root.querySelectorAll("[data-course-status-filter]")];
                const countLabel = root.querySelector("[data-course-result-count]");
                const emptyMessage = root.querySelector("[data-course-empty]");
                const courseItems = [...document.querySelectorAll(".course-item[data-course-status]")];
                const trackSections = [...document.querySelectorAll(".track-section")];
                let activeStatus = "all";

                const apply = () => {
                  const query = normalize(input?.value);
                  let visibleCount = 0;

                  courseItems.forEach((item) => {
                    const matchesQuery = !query || normalize(item.dataset.searchText || item.textContent).includes(query);
                    const matchesStatus = activeStatus === "all" || item.dataset.courseStatus === activeStatus;
                    const visible = matchesQuery && matchesStatus;
                    item.hidden = !visible;
                    item.classList.toggle("is-filtered-out", !visible);
                    if (visible) visibleCount += 1;
                  });

                  trackSections.forEach((section) => {
                    const hasVisibleCourse = Boolean(section.querySelector(".course-item:not([hidden]), .empty-state:not([hidden])"));
                    section.hidden = !hasVisibleCourse;
                  });

                  if (countLabel) {
                    countLabel.textContent = String(visibleCount);
                  }
                  if (emptyMessage) {
                    emptyMessage.hidden = visibleCount > 0;
                  }
                };

                input?.addEventListener("input", apply);
                statusButtons.forEach((button) => {
                  button.addEventListener("click", () => {
                    activeStatus = button.dataset.courseStatusFilter || "all";
                    setActive(statusButtons, button);
                    apply();
                  });
                });

                apply();
              };

              const setupLectureFinder = () => {
                const root = document.querySelector("[data-lecture-finder]");
                if (!root) {
                  return;
                }

                const input = root.querySelector("[data-lecture-search]");
                const statusButtons = [...root.querySelectorAll("[data-lecture-status-filter]")];
                const tagButtons = [...root.querySelectorAll("[data-lecture-tag-filter]")];
                const countLabel = root.querySelector("[data-lecture-result-count]");
                const emptyMessage = root.querySelector("[data-lecture-empty]");
                const lectureCards = [...document.querySelectorAll(".lecture-card[data-lesson-key]")];
                let activeStatus = "all";
                let activeTag = "all";

                const apply = () => {
                  const query = normalize(input?.value);
                  let visibleCount = 0;

                  lectureCards.forEach((card) => {
                    const isComplete = card.classList.contains("is-complete");
                    const matchesQuery = !query || normalize(card.dataset.searchText || card.textContent).includes(query);
                    const tags = normalize(card.dataset.tags).split("|||");
                    const matchesTag = activeTag === "all" || tags.includes(activeTag);
                    const matchesStatus =
                      activeStatus === "all" ||
                      (activeStatus === "done" && isComplete) ||
                      (activeStatus === "remaining" && !isComplete);
                    const visible = matchesQuery && matchesTag && matchesStatus;
                    card.hidden = !visible;
                    card.classList.toggle("is-filtered-out", !visible);
                    if (visible) visibleCount += 1;
                  });

                  if (countLabel) {
                    countLabel.textContent = String(visibleCount);
                  }
                  if (emptyMessage) {
                    emptyMessage.hidden = visibleCount > 0;
                  }
                };

                input?.addEventListener("input", apply);
                statusButtons.forEach((button) => {
                  button.addEventListener("click", () => {
                    activeStatus = button.dataset.lectureStatusFilter || "all";
                    setActive(statusButtons, button);
                    apply();
                  });
                });
                tagButtons.forEach((button) => {
                  button.addEventListener("click", () => {
                    activeTag = button.dataset.lectureTagFilter || "all";
                    setActive(tagButtons, button);
                    apply();
                  });
                });

                document.addEventListener("whitehat-progress-change", apply);
                document.addEventListener("click", (event) => {
                  if (event.target.closest(".completion-toggle")) {
                    window.setTimeout(apply, 0);
                  }
                });

                apply();
              };

              const setupLectureSideGuide = () => {
                const guide = document.querySelector("[data-lecture-side-guide]");
                if (!guide) {
                  return;
                }

                const links = [...guide.querySelectorAll("[data-side-section-link]")];
                const current = guide.querySelector("[data-side-current]");
                const jumpSelect = document.querySelector("[data-section-jump]");
                const sections = links
                  .map((link) => document.getElementById(link.dataset.sideSectionLink || ""))
                  .filter(Boolean);

                if (!links.length || !sections.length) {
                  return;
                }

                const setActiveSection = (sectionId) => {
                  links.forEach((link) => {
                    const active = link.dataset.sideSectionLink === sectionId;
                    link.classList.toggle("is-active", active);
                    if (active && current) {
                      current.textContent = `SECTION ${link.querySelector("span")?.textContent || ""}`.trim();
                    }
                    if (active && jumpSelect) {
                      jumpSelect.value = `#${sectionId}`;
                    }
                  });
                };

                const sectionFromHash = () => {
                  const id = window.location.hash.replace("#", "");
                  return sections.some((section) => section.id === id) ? id : "";
                };

                links.forEach((link) => {
                  link.addEventListener("click", () => {
                    const sectionId = link.dataset.sideSectionLink;
                    if (sectionId) {
                      setActiveSection(sectionId);
                    }
                  });
                });

                if ("IntersectionObserver" in window) {
                  const observer = new IntersectionObserver(
                    (entries) => {
                      const visible = entries
                        .filter((entry) => entry.isIntersecting)
                        .sort((a, b) => Math.abs(a.boundingClientRect.top) - Math.abs(b.boundingClientRect.top));
                      if (visible[0]?.target?.id) {
                        setActiveSection(visible[0].target.id);
                      }
                    },
                    { rootMargin: "-18% 0px -64% 0px", threshold: [0, 0.2, 0.6] },
                  );
                  sections.forEach((section) => observer.observe(section));
                } else {
                  const updateByScroll = () => {
                    const currentSection = sections.reduce((best, section) => {
                      const top = Math.abs(section.getBoundingClientRect().top - 120);
                      return !best || top < best.top ? { id: section.id, top } : best;
                    }, null);
                    if (currentSection) {
                      setActiveSection(currentSection.id);
                    }
                  };
                  document.addEventListener("scroll", updateByScroll, { passive: true });
                  updateByScroll();
                }

                setActiveSection(sectionFromHash() || sections[0].id);
              };

              const setupLectureControls = () => {
                const sectionSelect = document.querySelector("[data-section-jump]");
                const sections = [...document.querySelectorAll("[data-note-section]")];

                sectionSelect?.addEventListener("change", () => {
                  const targetId = (sectionSelect.value || "").replace("#", "");
                  const target = targetId ? document.getElementById(targetId) : null;
                  if (!target) {
                    return;
                  }
                  if ("open" in target) {
                    target.open = true;
                  }
                  target.scrollIntoView({ behavior: "smooth", block: "start" });
                  history.replaceState(null, "", `#${targetId}`);
                });

                document.querySelectorAll("[data-section-toggle]").forEach((button) => {
                  button.addEventListener("click", () => {
                    const mode = button.dataset.sectionToggle;
                    sections.forEach((section) => {
                      section.open = mode !== "collapse";
                    });
                  });
                });
              };

              const initStudyTools = () => {
                setupCourseFinder();
                setupLectureFinder();
                setupLectureSideGuide();
                setupLectureControls();
              };

              if (document.readyState === "loading") {
                document.addEventListener("DOMContentLoaded", initStudyTools);
              } else {
                initStudyTools();
              }
            })();
            """
        ).strip()
        + "\n",
        encoding="utf-8",
    )


def main() -> None:
    generated_courses = ready_courses()
    write_styles()
    write_code_highlighter()
    write_study_state_script()
    write_study_tools_script()
    write_public_html(ROOT / "index.html", render_site_index())
    for course in generated_courses:
        transcripts = get_transcripts(course)
        output_dir = course_output_dir(course)
        output_dir.mkdir(parents=True, exist_ok=True)
        lecture_dir = lecture_output_dir(course)
        lecture_dir.mkdir(parents=True, exist_ok=True)
        write_public_html(output_dir / "index.html", render_course_index(course))
        for lecture in course.get("lectures", []):
            write_public_html(
                lecture_dir / lecture_html_file(lecture),
                render_lecture(lecture, course, transcripts),
            )


if __name__ == "__main__":
    main()
