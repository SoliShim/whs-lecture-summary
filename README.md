# 화이트햇 강의 HTML 정리 프로젝트

화이트햇 과정 강의를 과목별 HTML 강의 노트로 정리하는 프로젝트다. 학생이 실제로 강의를 듣는 입장에서 본문을 편하게 읽고, 필요한 경우에만 표, 코드, 다이어그램, 강의 원문을 확인할 수 있도록 구성한다.

현재 디자인과 UI 기준은 [DESIGN_SYSTEM.md](DESIGN_SYSTEM.md)에 저장되어 있다. 새 강의자료를 추가할 때는 이 기준을 먼저 확인한다.

## 현재 상태

- 총 9개 과목
- 총 72개 강의 HTML 생성 완료
- 모든 강의 페이지에 섹션 드롭다운, 섹션 접기/전체 펼치기, 왼쪽 섹션 길잡이, 복습 체크, 강의 원문 영역 적용
- 강의 본문 섹션은 기본적으로 열린 접이식 구조 유지
- 강의 페이지의 플로팅 진행 카드와 과한 보조 패널 제거 상태 유지
- 강의 본문, 학습 목표, 복습 체크에 핵심 개념어 자동 볼드 처리 적용

## 디렉토리 구조

```text
.
├── README.md
├── DESIGN_SYSTEM.md
├── CODE_HIGHLIGHTING_README.md
├── index.html
├── build_lecture_html.py
├── assets/
│   ├── styles.css
│   ├── code-highlight.js
│   ├── study-state.js
│   └── study-tools.js
├── course_data/
│   ├── programming_basics_c.py
│   ├── hackers_programming.py
│   └── ...
├── courses/
│   └── common-development/
│       ├── programming-basics-c/
│       │   ├── index.html
│       │   └── lectures/
│       │       ├── lesson-01.html
│       │       └── ...
│       └── ...
├── official-assets/
│   ├── logo.png
│   ├── fonts/
│   └── ...
└── stt/
    └── common-development/
        ├── programming-basics-c/
        ├── hackers-programming/
        └── ...
```

## 핵심 파일 역할

- `build_lecture_html.py`: 사이트 전체 HTML, 공통 스크립트, 기본 자산, 핵심어 자동 강조를 생성한다.
- `course_data/*.py`: 과목별 강의 내용 원본이다. 새 강의 본문은 여기서 관리한다.
- `assets/styles.css`: 현재 UI와 디자인 기준의 실제 스타일 파일이다.
- `assets/study-tools.js`: 검색, 필터, 섹션 드롭다운, 접기/펼치기, 현재 섹션 표시를 담당한다.
- `assets/study-state.js`: 완료 상태 저장을 담당한다.
- `DESIGN_SYSTEM.md`: 앞으로 새 강의를 추가할 때 지켜야 할 UI/디자인 기준이다.
- `CODE_HIGHLIGHTING_README.md`: 코드 블록 작성과 색상 강조 기준이다.

## 새 강의자료 추가 흐름

1. STT 파일을 `stt/<track>/<course>/과목명-순서-강의제목.txt` 규칙으로 넣는다.
2. `course_data/`에 과목 데이터 파일을 추가하거나 기존 과목 파일을 수정한다.
3. 강의 데이터는 기존 파일과 같은 형식으로 `title`, `subtitle`, `tags`, `objectives`, `sections`, `checks`를 채운다.
4. 본문 HTML은 [DESIGN_SYSTEM.md](DESIGN_SYSTEM.md)의 본문 작성 기준을 따른다.
5. 핵심 개념어는 생성기가 자동으로 일부 볼드 처리한다. 자동으로 잡히지 않는 강사 강조 문장은 본문 원본에 `<strong>...</strong>`을 직접 넣는다.
6. 코드 예시는 `code_block(source, lang)` 또는 `<pre><code class="language-언어명">` 형식으로 넣는다.
7. 운영 설명, 제작 과정, 자동 변환 방식, 파일 관리 방식은 학생 화면에 넣지 않는다.
8. 아래 명령으로 전체 HTML을 다시 생성한다.

```bash
python3 build_lecture_html.py
```

생성된 HTML은 `courses/<track>/<course>/` 아래에 저장된다. 생성된 HTML을 직접 대량 수정하지 말고, 원본 데이터와 공통 스타일을 수정한 뒤 다시 생성한다.

## 핵심어 볼드 처리 기준

강의 본문은 읽는 흐름을 해치지 않는 선에서 중요한 개념어만 볼드 처리한다.

- 개념어, 표준명, 방법론, 취약점 이름, 프로토콜, 명령어, 함수명처럼 다시 봐야 할 용어를 우선한다.
- 강사가 정의하거나 비교하거나 결론으로 강조한 짧은 문장은 `<strong>...</strong>`으로 직접 감싼다.
- 한 문단 안에서 볼드는 1-2개 정도만 둔다. 같은 단어를 문단마다 반복해서 굵게 만들지 않는다.
- 코드 블록, 링크, 버튼, 내비게이션 문구에는 핵심어 강조를 넣지 않는다.
- 새 과목에서 자동 강조가 부족하면 `build_lecture_html.py`의 `EMPHASIS_TERMS`에 과목 핵심어를 추가한 뒤 전체 HTML을 다시 생성한다.
- 생성된 HTML을 직접 고치는 대신 `course_data/*.py`, `build_lecture_html.py`, `assets/styles.css` 쪽을 수정해 같은 규칙이 다음 강의에도 적용되게 한다.

## 디자인 유지 원칙

새 강의자료가 들어와도 다음 기준은 유지한다.

- 강의 내용은 삭제하거나 축소하지 않는다.
- 본문을 중심에 두고, 사진, 인포그래픽, 코드, 표는 이해가 필요할 때만 쓴다.
- 한 섹션이 너무 길면 내용을 줄이지 말고 섹션을 나눈다.
- 강의 페이지 구조는 헤더, 완료 상태, 강의 탐색 도구, 학습 목표, 본문, 복습 체크, 강의 원문 순서를 유지한다.
- 본문 섹션은 `details.note-section.section-disclosure` 구조와 `open` 기본 상태를 유지한다.
- PC 화면을 주 타겟으로 한다. 모바일은 보조 대응으로 본다.
- 새 UI 패턴을 만들기 전 기존 버튼, 드롭다운, 필터, 패널, 본문 섹션 스타일을 재사용한다.

## 다시 추가하지 말아야 할 요소

다음 요소는 학생의 집중을 분산시키므로 새 강의 페이지에 넣지 않는다.

- 본문 위에 떠 있는 플로팅 진행 카드
- 과한 학습 보조 패널
- 장식 목적만 있는 인포그래픽
- 불필요한 예시 카드
- 운영/제작 방식 설명
- OS별로 모양이 달라지는 이모지 아이콘
- 카드 안에 또 다른 카드가 반복되는 중첩 UI

구체적인 금지 클래스와 컴포넌트 목록은 [DESIGN_SYSTEM.md](DESIGN_SYSTEM.md)의 `금지 요소` 섹션을 따른다.

## 검증 명령

HTML을 다시 생성한 뒤 기본 검증을 실행한다.

```bash
python3 -m py_compile build_lecture_html.py
node --check assets/study-tools.js
node --check assets/study-state.js
```

전체 HTML 링크와 이미지 경로를 확인할 때는 다음 명령을 사용한다.

```bash
python3 -c 'exec("""from pathlib import Path
import re, urllib.parse
bad=[]
html=list(Path(".").glob("**/*.html"))
for p in html:
    text=p.read_text(encoding="utf-8")
    for attr in re.findall(r'(?:href|src)="([^"]+)"', text):
        if attr.startswith(("http://","https://","mailto:","#")):
            continue
        url=attr.split("#",1)[0].split("?",1)[0]
        if not url:
            continue
        target=(p.parent / urllib.parse.unquote(url)).resolve()
        if not target.exists():
            bad.append((str(p), attr))
print(f"checked html files: {len(html)}")
print(f"bad links/assets: {len(bad)}")
for item in bad[:20]:
    print(item[0], "=>", item[1])
""")'
```

## 현재 등록 과목

- `공통/개발 > 프로그래밍 기초(C)`: 8개 강의
- `공통/개발 > 컴퓨터 구조 I`: 6개 강의
- `공통/개발 > 운영체제 기초`: 12개 강의
- `공통/개발 > 네트워크 기초`: 8개 강의
- `공통/개발 > 암호학 기초`: 6개 강의
- `공통/개발 > 정보보안윤리 / 사이버 안보`: 8개 강의
- `공통/개발 > 최신 보안 동향`: 7개 강의
- `공통/개발 > 해커의 프로그래밍`: 9개 강의
- `공통/개발 > 시큐어코딩`: 8개 강의
