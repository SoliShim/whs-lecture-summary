# 화이트햇 강의 HTML 정리 프로젝트

이 프로젝트는 화이트햇 과정의 강의 STT 원문을 과목별 HTML 강의 노트로 정리한다.

## 디렉토리 구조

```text
.
├── index.html
├── assets/
│   └── styles.css
├── build_lecture_html.py
├── courses/
│   └── common-development/
│       └── programming-basics-c/
│           ├── index.html
│           └── lectures/
│               ├── lesson-01.html
│               └── ...
├── stt/
│   └── common-development/
│       ├── programming-basics-c/
│       │   ├── 프로그래밍 기초(C)-01-산업별-소프트웨어-품질-기준.txt
│       │   └── ...
│       └── computer-architecture-1/
└── videos/
    └── common-development/
        └── computer-architecture-1/
            ├── 컴퓨터 구조 1-01-강의-목차.mp4
            └── ...
```

## 파일명 규칙

- 트랙 폴더는 영문 slug로 쓴다. 예: `common-development`
- 과목 폴더도 영문 slug로 쓴다. 예: `programming-basics-c`
- 생성된 HTML 강의 파일은 내부 링크 안정성을 위해 `lesson-01.html`, `lesson-02.html` 형식을 쓴다.
- STT 원문은 `stt/<track>/<course>/과목명-01-강의-제목.txt`처럼 과목, 순서, 제목이 보이게 둔다.
- 영상 원본은 `videos/<track>/<course>/과목명-01-강의-제목.mp4`처럼 과목, 순서, 제목이 보이게 둔다.
- 생성된 HTML은 `courses/<track>/<course>/` 아래에 저장된다.

## 새 과목 추가 흐름

1. 영상 또는 STT 파일을 위 규칙에 맞춰 과목 폴더에 넣는다.
2. `build_lecture_html.py`의 `COURSES`에 과목 정보를 추가한다.
3. 강의별 정리 내용은 기존 `LECTURES`와 같은 형식의 리스트로 만든다.
4. 아래 명령으로 HTML을 다시 생성한다.

```bash
python3 build_lecture_html.py
```

## 현재 등록 상태

- `공통/개발 > 프로그래밍 기초(C)`: 8개 강의 HTML 생성 완료
- `공통/개발 > 컴퓨터 구조 I`: 영상 6개 정리 완료, STT 대기
