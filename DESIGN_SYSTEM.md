# 화이트햇 강의 UI 디자인 기준

이 문서는 새 강의자료가 추가되어도 현재 강의 사이트의 UI와 학습 경험을 일관되게 유지하기 위한 기준이다. 실제 구현 기준은 `assets/styles.css`, `build_lecture_html.py`, `assets/study-tools.js`가 담당한다.

## 핵심 원칙

- 강의 내용은 삭제하거나 축소하지 않는다.
- 학생이 본문을 읽는 흐름을 최우선으로 둔다.
- 사진, 인포그래픽, 코드, 표는 이해가 필요할 때만 넣는다.
- 장식용 카드, 반복 설명 박스, 과한 미니 인포그래픽은 만들지 않는다.
- 새 강의도 기존 생성기 구조를 사용한다. 생성된 HTML을 직접 대량 수정하지 않는다.
- PC 화면을 주 타겟으로 한다. 모바일은 깨지지 않게 유지하되 PC 가독성과 정렬을 우선한다.

## 현재 강의 페이지 구조

강의 페이지는 다음 순서를 유지한다.

1. 상단 내비게이션
2. 강의 헤더: 강의 번호, 제목, 요약, 태그, 페이지 목차
3. 강의 탐색 도구: 섹션 드롭다운, 섹션 접기, 전체 펼치기, 복습 체크, 강의 원문
4. 학습 목표
5. 본문 레이아웃: 왼쪽 섹션 길잡이, 오른쪽 본문 섹션
6. 복습 체크
7. 강의 원문
8. 이전/목록/다음 이동

본문 섹션은 `details.note-section.section-disclosure` 구조를 사용한다. 기본 상태는 반드시 열린 상태인 `open`이어야 한다.

## 본문 작성 기준

새 강의의 `sections`는 다음 기준으로 작성한다.

- 한 섹션은 하나의 학습 주제만 다룬다.
- 섹션이 너무 길어지면 내용을 줄이지 말고 주제를 나누어 섹션을 추가한다.
- 일반 설명은 `<p>`를 기본으로 쓴다.
- 체크형 정리는 `<ul class="check-list">`를 쓴다.
- 비교가 필요한 내용은 `<table>`을 쓴다.
- 순서나 흐름이 중요한 내용은 `.timeline`을 쓴다.
- 두세 개 개념을 나란히 비교할 때만 `.diagram.two-col` 또는 `.diagram.three-col`을 쓴다.
- 실습 코드가 있을 때만 `code_block(source, lang)` 또는 `<pre><code class="language-...">`를 쓴다.
- 강의 화면 캡처는 `screen_figure(...)`를 사용하고, 공개 경로는 `screenshots/common-development/...` 아래로 생성한다.
- 코드, 표, 다이어그램을 같은 섹션에 과하게 몰아넣지 않는다.
- 핵심 개념어, 표준명, 방법론, 취약점 이름, 프로토콜, 함수명은 필요한 만큼만 `<strong>`으로 강조한다.
- 한 문단의 볼드 강조는 1-2개 정도로 제한한다. 이미 한 번 강조한 개념을 같은 섹션에서 과하게 반복하지 않는다.
- 자동 강조가 부족한 새 과목은 `build_lecture_html.py`의 `EMPHASIS_TERMS`에 과목 핵심어를 추가한 뒤 전체 HTML을 다시 생성한다.
- 코드 블록, 링크, 버튼, 내비게이션, 운영 설명 문구에는 본문 핵심어 강조를 넣지 않는다.

## 금지 요소

다음 요소는 학생의 집중을 분산시키므로 새 강의에 다시 추가하지 않는다.

- 본문 위에 떠 있는 플로팅 진행 카드
- 완료 상태 표시, 완료 토글, 과목 진행률 패널
- 과목 페이지 상단 학습 루틴 카드
- 과목 학습 개요 패널
- 과목 페이지 강의 찾기/태그 필터 패널
- `learning-aids-panel`
- `study-strategy-panel`
- `exam-recap-panel`
- `classroom-lens`
- `section-visual-flow`
- `section-practice`
- `section-study-map`
- `quick-take`
- `section-term-strip`
- 제작 방식, 자동 변환 과정, 파일 관리 방식 같은 운영 설명
- OS별로 다르게 보이는 이모지 아이콘
- 장식 목적만 있는 이미지, 카드, 배지, 아이콘

## 레이아웃 기준

현재 PC 기준 레이아웃 토큰은 `assets/styles.css`의 마지막 보정 레이어에 저장되어 있다.

- 페이지 최대 폭: `--page-max: 1180px`
- 본문 읽기 폭: `--reader-max: 872px`
- 패널 간격: `--panel-gap: 24px`
- 패널 반경: `--ui-radius: 8px`
- 컨트롤 높이: `--control-height: 46px`
- 강의 본문 그리드: 왼쪽 길잡이 248px, 오른쪽 본문

새 UI 요소를 추가해야 할 때는 이 토큰을 우선 사용한다. 별도의 큰 반경, 큰 그림자, 한 색상 계열만 반복되는 팔레트는 피한다.

## 스타일 수정 기준

- 공통 디자인은 `assets/styles.css`에 둔다.
- 새 보정은 파일 뒤쪽의 현재 보정 레이어 근처에 추가한다.
- 기존 강의 본문 텍스트를 줄이거나 숨기는 CSS를 넣지 않는다.
- 버튼, 드롭다운, 입력창, 필터 칩은 같은 높이와 반경을 유지한다.
- 카드 안에 또 다른 카드처럼 보이는 중첩 UI를 만들지 않는다.
- 새 아이콘은 가능하면 `official-assets/`의 기존 이미지 스타일과 맞춘다.

## 새 강의 추가 절차

1. `course_data/`에 기존 과목 파일과 같은 형식으로 강의 데이터를 추가한다.
2. 강의별 `objectives`, `sections`, `checks`, `tags`, `subtitle`을 채운다.
3. 본문은 이 문서의 본문 작성 기준을 따른다.
4. STT 파일은 `stt/<track>/<course>/과목명-순서-강의제목.txt` 규칙으로 둔다.
5. 새 과목 핵심어가 자동 강조 목록에 없으면 `build_lecture_html.py`의 `EMPHASIS_TERMS`에 추가한다.
6. `python3 build_lecture_html.py`를 실행한다.
7. 생성된 HTML에서 강의 내용이 빠지지 않았는지, 볼드가 과하지 않은지, 캡처 이미지가 `screenshots/` 경로를 바라보는지 확인한다.
8. 아래 검증 명령을 실행한다.

```bash
python3 -m py_compile build_lecture_html.py
node --check assets/study-tools.js
```

링크와 생성 구조는 필요할 때 다음 기준으로 점검한다.

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

## 완료 기준

새 강의자료 추가 작업은 다음 조건을 만족해야 완료로 본다.

- 강의 본문 내용이 삭제되거나 축소되지 않았다.
- 본문 핵심어는 중요한 용어 중심으로만 볼드 처리되어 있고 과하게 반복되지 않았다.
- 모든 강의 페이지에 강의 탐색 도구가 있다.
- 본문 섹션은 기본적으로 열린 접이식 구조다.
- 과한 보조 패널과 플로팅 카드가 없다.
- 깨진 내부 링크와 이미지가 없다.
- README와 이 문서의 기준에서 벗어난 새 UI 패턴이 없다.
