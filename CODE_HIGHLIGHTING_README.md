# 코드 색상 강조 적용 규칙

이 문서는 Codex나 다음 작업자가 새 과목을 추가할 때, 브라우저에 보이는 코드 예시를 지금과 같은 방식으로 색상 강조하기 위한 기준이다.

## 현재 적용 방식

- 모든 생성 HTML은 `build_lecture_html.py`의 `shared_head()`를 통해 `assets/styles.css`와 `assets/code-highlight.js`를 불러온다.
- `assets/code-highlight.js`는 브라우저에서 `<pre><code class="language-...">` 블록을 찾아 언어 라벨, 줄 번호, 토큰 색상을 자동으로 붙인다.
- `assets/styles.css`는 코드 블록 배경, 줄 번호, 키워드, 문자열, 숫자, 함수, 변수, 주석 색상을 담당한다.
- `assets/styles.css`와 `assets/code-highlight.js`는 생성 결과물이므로, 규칙을 바꿀 때는 생성된 파일만 고치지 말고 `build_lecture_html.py`의 `write_styles()`와 `write_code_highlighter()`를 고친 뒤 다시 생성한다.

## 새 코드 예시 작성법

가능하면 파이썬 데이터 안에서는 `code_block(source, lang)`를 사용한다.

```python
code_block("""
sudo apt update
sudo apt install nginx
""", "bash")
```

HTML을 직접 작성해야 한다면 아래 형식을 지킨다.

```html
<pre><code class="language-python">print("hello")</code></pre>
```

## 지원 언어명

- `language-bash`, `language-shell`, `language-sh`
- `language-c`, `language-cpp`
- `language-python`, `language-py`
- `language-sql`
- `language-asm`
- `language-text`

## 학생 설명용 주석

코드 안에 설명이 필요하면 해당 언어의 실제 주석 문법으로 짧게 적는다. 주석은 자동으로 흐린 색으로 표시된다.

- Bash/Python: `# 설명`
- C/C++: `// 설명` 또는 `/* 설명 */`
- SQL: `-- 설명`
- Assembly: `; 설명`

명령어를 그대로 복사해서 실행해야 하는 예제에는 주석을 과하게 붙이지 않는다. 설명이 길어지면 코드 바깥의 본문 문장이나 표에서 설명한다.

## 새 과목에 적용하는 순서

1. STT와 과목 데이터를 기존 규칙대로 추가한다.
2. 코드 예시는 `code_block(source, lang)`로 넣고, 언어명을 위 지원 목록 중 하나로 지정한다.
3. 학생이 헷갈릴 만한 줄에는 실제 주석 문법으로 짧은 설명을 추가한다.
4. 루트에서 `python3 build_lecture_html.py`를 실행한다.
5. 브라우저에서 강의 HTML을 열어 언어 라벨, 줄 번호, 주석 색상, 긴 줄 가로 스크롤이 정상인지 확인한다.

## 언어를 추가해야 할 때

새 언어가 필요하면 `build_lecture_html.py`의 `write_code_highlighter()` 안에서 `labels`, `rulesByLanguage`, 토큰 규칙을 추가한다. 색상 종류가 더 필요할 때만 `write_styles()`의 토큰 CSS 변수를 늘린다.
