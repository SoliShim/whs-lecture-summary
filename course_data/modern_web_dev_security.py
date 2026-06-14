def build_modern_web_dev_security_lectures(code_block, screen_figure):
    course_id = "modern-web-dev"

    def fig(stem, no, title, note):
        return screen_figure(course_id, stem, no, title, note)

    l01 = "모던 웹 개발 및 보안-01-Node.js-개요"
    l02 = "모던 웹 개발 및 보안-02-Node.js-설치-및-개발환경-구축"
    l03 = "모던 웹 개발 및 보안-03-ExpressJS-개요와-웹앱-구현"
    l04 = "모던 웹 개발 및 보안-04-HTTP-요청-처리"
    l05 = "모던 웹 개발 및 보안-05-Express-라우팅"
    l06 = "모던 웹 개발 및 보안-06-Express-미들웨어"
    l07 = "모던 웹 개발 및 보안-07-Node.js-전역-객체와-내장-모듈"
    l08 = "모던 웹 개발 및 보안-08-EJS-템플릿-엔진"
    l09 = "모던 웹 개발 및 보안-09-Prototype-Pollution"
    l10 = "모던 웹 개발 및 보안-10-EJS-템플릿-원격-코드-실행"

    express_minimal = code_block(
        """
        // index.js

        const express = require('express')
        const app = express()
        const port = 3000

        app.get('/', (req, res) => {
          res.send('Hello World!')
        })

        app.listen(port, () => {
          console.log(`Example app listening on port ${port}`)
        })
        """,
        "javascript",
    )

    request_parser_setup = code_block(
        """
        const port = 3000;
        const express = require("express");
        const app = express();

        app.use(express.json());
        app.use(express.static("public"));
        app.use(express.urlencoded({ extended: true }));

        // ...
        """,
        "javascript",
    )

    request_parts = code_block(
        """
        app.use(express.urlencoded({ extended: true }));
        app.use(express.json());

        app.get("/search", (req, res) => {
          console.log(req.query.keyword);
          res.send(`keyword = ${req.query.keyword}`);
        });

        app.get("/users/:userId", (req, res) => {
          console.log(req.params.userId);
          res.send(`user id = ${req.params.userId}`);
        });

        app.post("/users", (req, res) => {
          console.log(req.body);
          res.json({ ok: true, received: req.body });
        });
        """,
        "javascript",
    )

    basic_routing_code = code_block(
        """
        app.METHOD(PATH, HANDLER)

        app.get('/', function (req, res) {
          res.send('Got a GET request');
        });

        app.post('/', function (req, res) {
          res.send('Got a POST request');
        });

        app.put('/user', function (req, res) {
          res.send('Got a PUT request at /user');
        });
        """,
        "javascript",
    )

    router_example = code_block(
        """
        const express = require("express");
        const router = express.Router();

        router.get("/", (req, res) => res.send("user list"));
        router.get("/:id", (req, res) => res.send(`user ${req.params.id}`));
        router.post("/", (req, res) => res.status(201).send("created"));
        router.put("/:id", (req, res) => res.send(`updated ${req.params.id}`));
        router.delete("/:id", (req, res) => res.send(`deleted ${req.params.id}`));

        module.exports = router;
        """,
        "javascript",
    )

    middleware_chain = code_block(
        """
        const logger = (req, res, next) => {
          console.log(`Request ${req.path}`);
          next();
        }

        const auth = (req, res, next) => {
          if(!isAdmin(req)) {
            next(new Error ('Not Authorized'));
            return;
          }
          next();
        }
        """,
        "javascript",
    )

    node_globals = code_block(
        """
        console.log(__dirname);
        console.log(__filename);
        console.log(process.cwd());
        console.log(process.env.NODE_ENV);

        const path = require("path");
        const fs = require("fs");

        const filePath = path.join(__dirname, "data.txt");
        fs.readFile(filePath, "utf8", (err, data) => {
          if (err) throw err;
          console.log(data);
        });
        """,
        "javascript",
    )

    ejs_basic = code_block(
        """
        app.set("view engine", "ejs");
        app.set("views", "./views");

        app.get("/notes", (req, res) => {
          res.render("notes", {
            title: "Current Notes",
            notes: ["공통 루틴 영역", "보안 점검", "배포 전 확인"],
          });
        });
        """,
        "javascript",
    )

    ejs_template = code_block(
        """
        <h1><%= title %></h1>

        <% if (notes.length === 0) { %>
          <p>Empty Notes.</p>
        <% } else { %>
          <ul>
            <% notes.forEach((note) => { %>
              <li><%= note %></li>
            <% }) %>
          </ul>
        <% } %>
        """,
        "ejs",
    )

    prototype_pollution_demo = code_block(
        """
        function unsafeMerge(target, source) {
          for (const key in source) {
            if (typeof source[key] === "object") {
              target[key] = target[key] || {};
              unsafeMerge(target[key], source[key]);
            } else {
              target[key] = source[key];
            }
          }
          return target;
        }

        const payload = JSON.parse('{"__proto__": {"isAdmin": true}}');
        unsafeMerge({}, payload);

        console.log({}.isAdmin); // true가 나오면 Object.prototype이 오염된 상태
        """,
        "javascript",
    )

    prototype_pollution_guard = code_block(
        """
        const BLOCKED_KEYS = new Set(["__proto__", "prototype", "constructor"]);

        function safeMerge(target, source) {
          for (const [key, value] of Object.entries(source)) {
            if (BLOCKED_KEYS.has(key)) continue;

            if (value && typeof value === "object" && !Array.isArray(value)) {
              target[key] = safeMerge(Object.create(null), value);
            } else {
              target[key] = value;
            }
          }
          return target;
        }
        """,
        "javascript",
    )

    ejs_rce_unsafe = code_block(
        """
        // 위험한 예: 사용자 입력을 템플릿 또는 렌더 옵션처럼 다루면 안 된다.
        app.get("/preview", (req, res) => {
          const template = req.query.template;
          const name = req.query.name;

          res.send(ejs.render(template, { name }));
        });
        """,
        "javascript",
    )

    ejs_rce_safe = code_block(
        """
        // 안전한 방향: 템플릿은 서버 파일로 고정하고, 사용자는 데이터로만 전달한다.
        app.get("/profile", (req, res) => {
          res.render("profile", {
            name: String(req.query.name || ""),
          });
        });
        """,
        "javascript",
    )

    return [
        {
            "id": "1-1",
            "title": "Node.js 개요",
            "subtitle": "Node.js가 브라우저 밖에서 JavaScript를 실행하는 런타임이라는 점과 비동기, 논블로킹, 싱글 스레드, 이벤트 기반 구조를 정리한다.",
            "tags": ["Node.js", "비동기", "이벤트 루프"],
            "objectives": [
                "Node.js가 Chrome V8 엔진 위에서 동작하는 서버 사이드 JavaScript 실행 환경임을 설명한다.",
                "동기와 비동기, 블로킹과 논블로킹을 구분한다.",
                "싱글 스레드 모델과 이벤트 기반 처리 방식이 Node.js의 장점과 한계에 어떤 영향을 주는지 이해한다.",
                "Node.js가 웹 보안 실습에서 왜 필요한지 연결한다.",
            ],
            "sections": [
                {
                    "heading": "Node.js의 위치",
                    "body": """
                    """ + fig(l01, 2, "Node.js 활용 분야", "Node.js가 여러 산업과 웹 서비스 개발에서 쓰인다는 점을 먼저 보여준다.") + """
                    <p>강의는 Node.js를 “브라우저 밖에서도 JavaScript를 실행할 수 있게 해 주는 런타임”으로 설명한다. 원래 JavaScript는 웹 브라우저에서 동작하는 언어로 출발했지만, Node.js는 Chrome V8 엔진을 기반으로 서버, 명령행 도구, 자동화 도구, 웹 애플리케이션 백엔드에서 JavaScript를 실행할 수 있게 만든다.</p>
                    <p>웹 보안 관점에서 Node.js를 공부하는 이유는 Express, EJS, npm 패키지, 서버 라우팅, 미들웨어, 템플릿 렌더링 같은 실제 공격 표면이 Node.js 생태계에서 자주 등장하기 때문이다. 이 과목은 단순히 문법을 배우는 것이 아니라 이후 Prototype Pollution과 EJS RCE를 이해하기 위한 기반을 쌓는 흐름이다.</p>
                    """,
                },
                {
                    "heading": "주요 특징",
                    "body": """
                    """ + fig(l01, 12, "Node.js 주요 특징", "비동기 논블로킹 I/O, 싱글 스레드, 이벤트 기반 구조가 핵심 특징으로 제시된다.") + """
                    <p>Node.js의 핵심 특징은 비동기 논블로킹 I/O, 싱글 스레드, 이벤트 기반 구조다. I/O는 파일 읽기, 네트워크 요청, 데이터베이스 접근처럼 외부 자원과 데이터를 주고받는 작업을 말한다. 서버 프로그램은 CPU 계산보다 I/O 대기가 많은 경우가 많기 때문에, 대기 시간 동안 다른 요청을 처리할 수 있으면 효율이 높아진다.</p>
                    <table>
                      <thead><tr><th>특징</th><th>의미</th><th>주의점</th></tr></thead>
                      <tbody>
                        <tr><td>비동기</td><td>작업을 요청한 뒤 완료를 기다리는 동안 다음 작업을 진행한다.</td><td>콜백, Promise, async/await 흐름을 읽을 수 있어야 한다.</td></tr>
                        <tr><td>논블로킹 I/O</td><td>입출력 완료 전까지 실행 흐름 전체를 멈추지 않는다.</td><td>CPU 계산이 길면 이벤트 루프를 막을 수 있다.</td></tr>
                        <tr><td>싱글 스레드</td><td>JavaScript 실행은 주로 하나의 스레드에서 순차적으로 처리된다.</td><td>무거운 연산은 워커나 별도 프로세스로 분리해야 한다.</td></tr>
                        <tr><td>이벤트 기반</td><td>요청, 응답, 파일 완료 같은 사건이 발생하면 등록된 함수가 실행된다.</td><td>이벤트 흐름을 놓치면 디버깅이 어려워진다.</td></tr>
                      </tbody>
                    </table>
                    """,
                },
                {
                    "heading": "동기와 비동기",
                    "body": """
                    """ + fig(l01, 24, "동기와 비동기 실행 흐름", "동기 처리에서는 작업이 차례로 끝나야 다음 작업으로 넘어가지만, 비동기 처리에서는 기다리는 동안 다른 작업을 진행한다.") + """
                    <p>동기 처리에서는 Job A가 끝나야 Job B를 시작하고, Job B가 끝나야 Job C를 시작한다. 실행 순서를 이해하기 쉽지만, 어떤 작업이 오래 걸리면 뒤의 모든 작업이 기다린다. 반대로 비동기 처리에서는 오래 걸리는 작업을 요청해 둔 뒤 다음 작업을 먼저 진행하고, 완료 시점에 결과를 받아 처리한다.</p>
                    <p>서버는 동시에 많은 클라이언트의 요청을 받는다. 요청마다 파일, DB, 외부 API 응답을 기다리는 시간이 생긴다. Node.js는 이 대기 시간에 다른 요청 처리를 이어갈 수 있어 네트워크 중심 애플리케이션에 적합하다.</p>
                    """,
                },
                {
                    "heading": "블로킹과 논블로킹",
                    "body": """
                    """ + fig(l01, 29, "블로킹과 논블로킹", "블로킹은 다른 작업을 멈추게 하고, 논블로킹은 대기 작업과 다음 작업을 분리한다.") + """
                    <p>동기/비동기는 작업 완료 통지를 어떻게 다루는지에 가깝고, 블로킹/논블로킹은 호출한 쪽의 실행 흐름이 멈추는지에 가깝다. 블로킹 호출은 결과가 나올 때까지 다음 줄로 넘어가지 않는다. 논블로킹 호출은 요청만 전달하고 즉시 제어권을 돌려받아 다른 일을 할 수 있다.</p>
                    <p>강의는 이 개념을 서버 성능과 연결한다. 모든 요청이 블로킹으로 처리되면 느린 파일 읽기나 네트워크 응답 하나가 전체 처리량을 떨어뜨린다. Node.js의 장점은 이벤트 루프와 비동기 API를 통해 이런 대기를 효율적으로 다루는 데 있다.</p>
                    """,
                },
                {
                    "heading": "싱글 스레드와 이벤트 기반",
                    "body": """
                    """ + fig(l01, 53, "싱글 스레드와 논블로킹 I/O", "JavaScript 실행은 싱글 스레드이지만 파일 시스템, 네트워크, 프로세스 같은 I/O는 내부 작업자 흐름과 이벤트로 처리된다.") + """
                    <p>Node.js가 싱글 스레드라는 말은 모든 일을 하나의 줄에서만 처리한다는 뜻이 아니다. JavaScript 코드 실행은 한 줄기 흐름으로 관리되지만, 파일 시스템·네트워크 같은 I/O는 내부적으로 운영체제와 libuv의 도움을 받아 처리되고 완료 이벤트가 다시 JavaScript 영역으로 전달된다.</p>
                    <p>장점은 구조가 가볍고 많은 I/O 요청을 효율적으로 받을 수 있다는 점이다. 단점은 CPU를 오래 붙잡는 계산, 무한 루프, 무거운 암호 연산 같은 작업이 이벤트 루프를 막으면 전체 응답성이 떨어진다는 점이다. 따라서 서버 코드는 “짧게 실행하고, 오래 기다리는 일은 비동기로 맡긴다”는 원칙으로 작성해야 한다.</p>
                    """ + fig(l01, 64, "Node.js의 장단점", "I/O 중심 서버에는 강하지만 CPU 중심 작업에는 주의가 필요하다는 장단점이 정리된다.") + """
                    """,
                },
            ],
            "checks": [
                "Node.js를 런타임이라고 부르는 이유를 설명할 수 있는가?",
                "동기/비동기와 블로킹/논블로킹을 예시로 구분할 수 있는가?",
                "싱글 스레드인데도 많은 요청을 처리할 수 있는 이유를 말할 수 있는가?",
                "CPU 중심 작업이 Node.js 서버에 위험한 이유를 설명할 수 있는가?",
            ],
        },
        {
            "id": "1-2",
            "title": "Node.js 설치 및 개발환경 구축",
            "subtitle": "Node.js LTS, npm, VS Code, 터미널, 실습 프로젝트 폴더, package.json을 준비한다.",
            "tags": ["개발환경", "npm", "package.json"],
            "objectives": [
                "Node.js와 npm 설치 상태를 확인한다.",
                "VS Code와 터미널을 이용해 Node 프로젝트를 생성한다.",
                "npm 명령과 package.json의 역할을 이해한다.",
                "Express 실습을 위한 기본 프로젝트 구조를 만든다.",
            ],
            "sections": [
                {
                    "heading": "설치 대상",
                    "body": """
                    """ + fig(l02, 2, "개발환경 구축 항목", "Unix 계열 환경과 Node.js LTS 설치가 먼저 제시된다.") + """
                    <p>강의는 개발환경 구축을 Unix 환경과 Node.js LTS 설치에서 시작한다. 실습은 Ubuntu, macOS, WSL 같은 Unix 계열 터미널 흐름을 기준으로 진행된다. Node.js는 최신 기능만 따라가기보다 안정적으로 유지되는 LTS 버전을 설치하는 편이 실습과 운영에 적합하다.</p>
                    <p>설치 후에는 터미널에서 버전을 확인한다. `node`는 JavaScript 실행기이고, `npm`은 패키지 설치와 프로젝트 스크립트 실행을 담당한다.</p>
                    """ + code_block(
                        """
                        node -v
                        npm -v
                        """,
                        "bash",
                    ) + """
                    """,
                },
                {
                    "heading": "npm의 역할",
                    "body": """
                    """ + fig(l02, 4, "패키지 매니저 npm", "npm은 Node.js 생태계의 패키지를 다운로드하고 설치하는 패키지 매니저다.") + """
                    <p>npm은 Node Package Manager의 약자로, 외부 라이브러리를 프로젝트에 설치하고 버전을 기록하며 실행 스크립트를 관리한다. Express, EJS, nodemon 같은 도구도 npm을 통해 설치한다.</p>
                    <table>
                      <thead><tr><th>명령</th><th>의미</th></tr></thead>
                      <tbody>
                        <tr><td><code>npm init -y</code></td><td>기본 설정으로 package.json을 만든다.</td></tr>
                        <tr><td><code>npm install express</code></td><td>Express를 dependencies에 설치한다.</td></tr>
                        <tr><td><code>npm install -D nodemon</code></td><td>개발용 도구로 nodemon을 설치한다.</td></tr>
                        <tr><td><code>npm run dev</code></td><td>package.json에 등록한 dev 스크립트를 실행한다.</td></tr>
                      </tbody>
                    </table>
                    """,
                },
                {
                    "heading": "VS Code와 실습 도구",
                    "body": """
                    """ + fig(l02, 25, "VS Code 확장 설치", "강의는 VS Code와 필요한 확장을 설치하며 실습 환경을 맞춘다.") + """
                    <p>VS Code는 파일 탐색기, 터미널, 코드 편집, 확장 설치를 한 화면에서 처리할 수 있어 Node.js 실습에 편하다. 강의에서는 VS Code를 설치하고, 필요한 확장과 터미널을 준비한 뒤 프로젝트 폴더를 열어 실습한다. PortSwigger 같은 보안 학습 사이트도 함께 열어 이후 웹 보안 흐름과 연결할 준비를 한다.</p>
                    <p>실습 환경에서 중요한 점은 명령을 실행하는 현재 위치다. `npm init`, `npm install`, `node index.js`는 프로젝트 폴더에서 실행해야 package.json과 node_modules가 올바른 위치에 생성된다.</p>
                    """,
                },
                {
                    "heading": "프로젝트 생성",
                    "body": """
                    """ + fig(l02, 38, "npm install express", "터미널에서 npm으로 Express를 설치하고 의존성 파일이 생성되는 장면이다.") + """
                    <p>프로젝트는 폴더 생성, 초기화, 패키지 설치 순서로 만든다. 설치가 끝나면 `package.json`, `package-lock.json`, `node_modules`가 생긴다. `package.json`은 프로젝트 이름, 버전, 실행 스크립트, 의존성 목록을 담는 핵심 파일이다.</p>
                    """ + code_block(
                        """
                        mkdir web-practice
                        cd web-practice
                        npm init -y
                        npm install express
                        touch index.js
                        node index.js
                        """,
                        "bash",
                    ) + fig(l02, 49, "package.json 확인", "package.json에 Express 의존성이 기록된 상태를 확인한다.") + """
                    """,
                },
            ],
            "checks": [
                "Node.js LTS와 npm의 역할을 구분할 수 있는가?",
                "프로젝트 폴더에서 npm init과 npm install을 실행해야 하는 이유를 설명할 수 있는가?",
                "package.json에 어떤 정보가 들어가는지 말할 수 있는가?",
                "VS Code 터미널에서 Node 실습 파일을 실행할 수 있는가?",
            ],
        },
        {
            "id": "1-3",
            "title": "ExpressJS 개요와 웹앱 구현",
            "subtitle": "Node 기본 http 모듈과 Express를 비교하고, 최소 웹 서버를 구현해 요청과 응답 흐름을 확인한다.",
            "tags": ["Express", "웹 서버", "실습"],
            "objectives": [
                "Express가 Node.js 웹 서버 개발을 단순화하는 프레임워크임을 이해한다.",
                "http 모듈만 쓸 때와 Express를 쓸 때의 차이를 비교한다.",
                "app 객체, route handler, listen 흐름을 작성한다.",
                "브라우저에서 localhost로 접속해 응답을 확인한다.",
            ],
            "sections": [
                {
                    "heading": "Express의 역할",
                    "body": """
                    """ + fig(l03, 2, "Express.js 개요", "Express는 Node.js를 위한 빠르고 간결한 웹 프레임워크로 소개된다.") + """
                    <p>Express.js는 Node.js에서 웹 애플리케이션과 API 서버를 만들 때 자주 쓰는 프레임워크다. Node.js 기본 `http` 모듈만으로도 서버를 만들 수 있지만, 요청 URL 분기, 메서드별 처리, 정적 파일, 미들웨어, 에러 처리 등을 직접 많이 작성해야 한다. Express는 이런 반복 작업을 간결한 API로 제공한다.</p>
                    <p>강의 흐름은 먼저 `http` 모듈로 서버가 동작하는 원리를 보고, 그다음 Express가 같은 일을 더 읽기 쉬운 형태로 만들어 준다는 점을 확인한다.</p>
                    """ + fig(l03, 6, "http 모듈 기반 서버", "Node 기본 http 모듈만 사용하면 요청 처리 코드를 직접 구성해야 한다.") + """
                    """,
                },
                {
                    "heading": "최소 Express 서버",
                    "body": """
                    """ + fig(l03, 11, "Express 기본 코드", "express 모듈을 가져오고 app 객체에 라우트를 등록한 뒤 서버를 연다.") + express_minimal + """
                    <p>코드의 흐름은 네 단계다. 첫째, `require("express")`로 Express 모듈을 가져온다. 둘째, `express()`를 호출해 애플리케이션 객체 `app`을 만든다. 셋째, `app.get("/", handler)`처럼 특정 요청에 응답할 함수를 등록한다. 넷째, `app.listen()`으로 포트를 열어 요청을 받는다.</p>
                    <p>이 구조는 이후 라우팅, 미들웨어, 템플릿 렌더링에서도 계속 반복된다. Express 코드를 읽을 때는 “어떤 메서드와 경로에 어떤 handler가 연결되어 있는가”를 먼저 보면 된다.</p>
                    """,
                },
                {
                    "heading": "패키지 설치와 실행",
                    "body": """
                    """ + fig(l03, 18, "Express 설치와 실행 순서", "package.json을 만들고 Express를 설치한 뒤 index.js를 실행하는 실습 순서다.") + """
                    <p>Express는 기본 내장 모듈이 아니므로 프로젝트마다 npm으로 설치한다. 설치 후 `node index.js`를 실행하면 서버가 켜지고, 브라우저에서 `http://localhost:3000`으로 접속해 결과를 확인한다. 서버가 계속 실행 중인 상태에서는 터미널을 닫거나 중단하지 않는 한 요청을 계속 받을 수 있다.</p>
                    """ + code_block(
                        """
                        npm init -y
                        npm install express
                        node index.js
                        """,
                        "bash",
                    ) + """
                    """,
                },
                {
                    "heading": "웹앱 구현 실습",
                    "body": """
                    """ + fig(l03, 26, "실습 1: 웹앱 구현", "강의는 실제 파일을 만들고 localhost에서 결과를 확인하는 실습으로 이어진다.") + """
                    <p>실습에서는 Express 서버가 브라우저 요청을 받아 문자열이나 HTML을 응답하는 과정을 확인한다. 이때 중요한 것은 서버 코드와 브라우저 화면이 분리되어 있다는 점이다. 서버는 요청을 받아 응답을 만들고, 브라우저는 그 응답을 화면에 그린다.</p>
                    """ + fig(l03, 56, "브라우저 출력 확인", "작성한 Express 응답이 브라우저에서 표시되는지 확인한다.") + """
                    <p>웹 보안에서 이 구조는 매우 중요하다. 서버가 요청을 해석하는 방식, 사용자의 입력을 응답에 섞는 방식, 템플릿을 렌더링하는 방식이 모두 취약점으로 이어질 수 있기 때문이다.</p>
                    """,
                },
            ],
            "checks": [
                "Express가 기본 http 모듈보다 편한 이유를 설명할 수 있는가?",
                "app.get과 app.listen의 역할을 구분할 수 있는가?",
                "localhost와 포트 번호의 의미를 설명할 수 있는가?",
                "서버 응답이 브라우저 화면으로 나타나는 흐름을 설명할 수 있는가?",
            ],
        },
        {
            "id": "1-4",
            "title": "HTTP 요청 처리",
            "subtitle": "Express에서 req.query, req.params, req.body를 사용해 HTTP 요청의 데이터를 읽는 방법을 정리한다.",
            "tags": ["HTTP", "req.query", "req.body"],
            "objectives": [
                "HTTP 요청의 경로, 쿼리 문자열, 본문을 구분한다.",
                "Express에서 req.query, req.params, req.body를 읽는다.",
                "GET과 POST 요청에서 데이터가 전달되는 위치를 이해한다.",
                "본문 파싱 미들웨어가 필요한 이유를 설명한다.",
            ],
            "sections": [
                {
                    "heading": "요청 데이터의 위치",
                    "body": """
                    """ + fig(l04, 2, "req.query, params, body", "HTTP 요청 처리 실습의 핵심은 요청 데이터가 어디에 들어오는지 구분하는 것이다.") + """
                    <p>HTTP 요청에는 메서드, 경로, 헤더, 본문이 있다. Express에서는 이 요청을 `req` 객체로 받고, 응답을 `res` 객체로 만든다. 강의는 실습을 통해 `req.query`, `req.params`, `req.body`를 차례로 확인한다.</p>
                    <p>실습의 공통 준비 코드는 화면처럼 JSON 본문, 정적 파일, URL-encoded 폼 본문을 읽을 수 있는 미들웨어를 먼저 등록한다. 이 세 줄이 있어야 이후 라우트에서 `req.body`와 정적 파일 제공이 의도대로 동작한다.</p>
                    """ + request_parser_setup + """
                    <table>
                      <thead><tr><th>위치</th><th>예시</th><th>Express 접근</th></tr></thead>
                      <tbody>
                        <tr><td>쿼리 문자열</td><td><code>/search?keyword=node</code></td><td><code>req.query.keyword</code></td></tr>
                        <tr><td>경로 파라미터</td><td><code>/users/7</code></td><td><code>req.params.userId</code></td></tr>
                        <tr><td>요청 본문</td><td>POST body의 JSON 또는 form 값</td><td><code>req.body</code></td></tr>
                      </tbody>
                    </table>
                    """,
                },
                {
                    "heading": "query와 params",
                    "body": """
                    """ + fig(l04, 14, "req.query 실습", "쿼리 문자열을 읽고 콘솔과 응답으로 확인하는 코드 장면이다.") + request_parts + """
                    <p>`req.query`는 URL의 `?` 뒤에 붙은 키-값 쌍을 객체처럼 읽는다. 검색어, 필터, 페이지 번호처럼 리소스 조회 조건에 자주 사용된다. `req.params`는 라우트 경로에 `:userId`처럼 선언한 동적 구간을 읽는다. 사용자의 상세 페이지, 게시글 상세 페이지처럼 특정 리소스를 가리킬 때 많이 쓴다.</p>
                    """ + fig(l04, 26, "req.params 실습", "경로의 일부를 변수처럼 받아 처리하는 params 실습으로 이어진다.") + """
                    """,
                },
                {
                    "heading": "body와 파싱 미들웨어",
                    "body": """
                    """ + fig(l04, 39, "req.body 실습", "POST 요청의 본문을 읽기 위해 express.urlencoded 또는 express.json이 필요하다.") + """
                    <p>`req.body`는 POST, PUT, PATCH 요청처럼 본문에 담긴 데이터를 읽을 때 사용한다. 단, Express가 본문을 자동으로 항상 해석해 주는 것은 아니다. 폼 데이터는 `express.urlencoded`, JSON 데이터는 `express.json` 미들웨어가 먼저 등록되어야 한다.</p>
                    <p>보안 관점에서는 `req.body`를 읽는 순간부터 사용자가 보낸 값이 서버 로직 안으로 들어온다. 따라서 길이, 타입, 허용 값, 필수 값, 특수 문자, 권한을 검증하지 않으면 인젝션, 권한 우회, 서버 오류로 이어질 수 있다.</p>
                    """ + fig(l04, 54, "curl로 POST 요청 확인", "터미널에서 curl로 본문을 보내고 서버가 읽는지 검증한다.") + """
                    """,
                },
            ],
            "checks": [
                "query, params, body가 각각 어떤 상황에서 쓰이는지 설명할 수 있는가?",
                "Express에서 JSON body를 읽기 위해 필요한 미들웨어를 말할 수 있는가?",
                "GET 요청과 POST 요청의 데이터 전달 위치 차이를 설명할 수 있는가?",
                "요청 데이터 검증이 보안상 중요한 이유를 말할 수 있는가?",
            ],
        },
        {
            "id": "1-5",
            "title": "Express 라우팅",
            "subtitle": "HTTP 메서드와 URL 경로를 기준으로 handler를 나누고, 정적 파일과 CRUD 라우팅, 라우팅 체인을 정리한다.",
            "tags": ["라우팅", "CRUD", "정적 파일"],
            "objectives": [
                "Express 기본 라우팅 형식을 이해한다.",
                "정적 파일 라우팅과 동적 API 라우팅을 구분한다.",
                "CRUD 동작을 HTTP 메서드와 연결한다.",
                "express.Router로 라우트를 모듈화하는 이유를 설명한다.",
            ],
            "sections": [
                {
                    "heading": "기본 라우팅",
                    "body": """
                    """ + fig(l05, 2, "Express 기본 라우팅", "app.METHOD(PATH, HANDLER) 형식으로 요청을 처리한다.") + """
                    <p>라우팅은 “어떤 요청을 어떤 함수가 처리할 것인가”를 정하는 일이다. Express의 기본 형태는 `app.METHOD(PATH, HANDLER)`다. METHOD에는 GET, POST, PUT, DELETE 같은 HTTP 메서드가 들어가고, PATH에는 `/`, `/users`, `/users/:id` 같은 경로가 들어간다.</p>
                    """ + basic_routing_code + """
                    <p>같은 경로라도 메서드가 다르면 다른 의미를 가질 수 있다. `/users`에 대한 GET은 목록 조회, POST는 생성으로 해석하는 식이다.</p>
                    """,
                },
                {
                    "heading": "정적 파일 라우팅",
                    "body": """
                    """ + fig(l05, 21, "Express 정적 라우팅", "express.static을 사용하면 public 폴더의 이미지, CSS, JS를 브라우저에 제공할 수 있다.") + """
                    <p>정적 파일은 서버가 계산해서 만드는 응답이 아니라 이미 존재하는 파일이다. 이미지, CSS, 클라이언트 JavaScript, 다운로드 파일이 여기에 해당한다. Express에서는 `express.static("public")`으로 특정 폴더를 정적 파일 루트로 공개할 수 있다.</p>
                    <p>정적 파일 공개는 편리하지만 보안상 주의가 필요하다. 공개하면 안 되는 설정 파일, 소스 코드, 백업 파일이 정적 폴더에 들어가면 브라우저로 노출될 수 있다. 공개 폴더와 서버 내부 폴더를 명확히 분리해야 한다.</p>
                    """ + fig(l05, 33, "정적 파일 브라우저 확인", "정적 이미지 파일이 브라우저에 직접 표시되는 것을 확인한다.") + """
                    """,
                },
                {
                    "heading": "CRUD 라우팅",
                    "body": """
                    """ + fig(l05, 34, "Express 라우팅 CRUD", "강의는 생성, 조회, 수정, 삭제를 HTTP 메서드와 연결해 구현한다.") + router_example + """
                    <p>CRUD는 Create, Read, Update, Delete의 줄임말이다. REST 스타일 API에서는 보통 POST가 생성, GET이 조회, PUT/PATCH가 수정, DELETE가 삭제에 대응된다. Express 라우팅을 설계할 때 이 대응을 지키면 API를 읽는 사람이 동작을 예측하기 쉽다.</p>
                    <p>라우트가 많아지면 모든 코드를 `index.js` 하나에 둘 수 없다. 이때 `express.Router()`를 사용해 사용자 라우트, 게시글 라우트, 관리자 라우트처럼 파일을 나누고 `app.use("/users", userRouter)`처럼 연결한다.</p>
                    """ + fig(l05, 56, "라우팅 체인", "여러 라우트와 handler가 순서대로 연결되는 라우팅 체인 개념을 확인한다.") + """
                    """,
                },
            ],
            "checks": [
                "app.METHOD(PATH, HANDLER)의 각 요소를 설명할 수 있는가?",
                "정적 파일 공개에서 주의할 점을 말할 수 있는가?",
                "CRUD와 HTTP 메서드를 연결할 수 있는가?",
                "express.Router로 라우트를 분리하는 이유를 설명할 수 있는가?",
            ],
        },
        {
            "id": "1-6",
            "title": "Express 미들웨어",
            "subtitle": "요청과 응답 사이에 끼어 순차적으로 실행되는 미들웨어의 동작 원리, next, 에러 처리, 인증 미들웨어를 정리한다.",
            "tags": ["미들웨어", "next", "에러 처리"],
            "objectives": [
                "미들웨어가 요청과 응답 사이의 처리 함수라는 점을 이해한다.",
                "req, res, next의 역할과 실행 순서를 설명한다.",
                "애플리케이션 레벨, 라우터 레벨, 오류 처리 미들웨어를 구분한다.",
                "인증·로깅·파싱 같은 공통 처리를 미들웨어로 분리하는 이유를 이해한다.",
            ],
            "sections": [
                {
                    "heading": "미들웨어 개념",
                    "body": """
                    """ + fig(l06, 2, "요청, 미들웨어, 응답", "미들웨어는 요청을 받고 응답을 보내기 전 중간에서 공통 작업을 수행한다.") + """
                    <p>미들웨어는 요청과 응답 사이에서 실행되는 함수다. 사용자인증, 권한 검증, 요청 본문 파싱, 로깅, 에러 처리처럼 여러 라우트에서 반복되는 작업을 공통 처리로 분리한다. Express 앱은 요청이 들어오면 등록된 순서대로 미들웨어를 통과시키고, 최종 라우트 handler 또는 응답 처리로 이어진다.</p>
                    """ + fig(l06, 4, "미들웨어 실행 파이프라인", "HTTP 요청이 여러 미들웨어를 차례로 지나 응답으로 이어지는 구조다.") + """
                    """,
                },
                {
                    "heading": "req, res, next",
                    "body": """
                    """ + fig(l06, 19, "req, res, next", "미들웨어 함수는 요청 객체, 응답 객체, 다음 미들웨어로 넘기는 next를 받는다.") + middleware_chain + """
                    <p>`req`는 클라이언트가 보낸 요청 정보, `res`는 서버가 보낼 응답, `next`는 다음 미들웨어로 제어를 넘기는 함수다. 미들웨어가 응답을 끝내지 않고 `next()`도 호출하지 않으면 요청은 중간에서 멈춘다.</p>
                    <p>등록 순서도 중요하다. body를 읽는 라우트보다 `express.json()`이 뒤에 등록되면 해당 라우트에서는 `req.body`가 준비되지 않는다. 인증 미들웨어도 보호해야 할 라우트보다 앞에 있어야 한다.</p>
                    """,
                },
                {
                    "heading": "미들웨어 유형",
                    "body": """
                    """ + fig(l06, 23, "애플리케이션 미들웨어", "app.use로 전체 앱에 적용되는 미들웨어를 작성한다.") + """
                    <table>
                      <thead><tr><th>유형</th><th>사용 위치</th><th>예시</th></tr></thead>
                      <tbody>
                        <tr><td>애플리케이션 레벨</td><td><code>app.use()</code></td><td>전체 요청 로깅, 공통 파싱</td></tr>
                        <tr><td>라우터 레벨</td><td><code>router.use()</code></td><td>특정 기능 영역의 권한 검증</td></tr>
                        <tr><td>내장 미들웨어</td><td><code>express.static</code>, <code>express.json</code></td><td>정적 파일, JSON body 처리</td></tr>
                        <tr><td>오류 처리</td><td><code>(err, req, res, next)</code></td><td>예외와 실패 응답 처리</td></tr>
                      </tbody>
                    </table>
                    """ + fig(l06, 31, "라우터 레벨 미들웨어", "특정 라우터에만 공통 처리를 적용하는 장면이다.") + """
                    """,
                },
                {
                    "heading": "에러와 인증",
                    "body": """
                    """ + fig(l06, 35, "오류 처리 미들웨어", "에러 처리 미들웨어는 네 개의 인자를 받아 실패 응답을 중앙에서 관리한다.") + """
                    <p>에러 처리 미들웨어는 일반 미들웨어와 달리 첫 번째 인자로 `err`를 받는다. 라우트마다 try/catch와 응답 코드를 흩뿌리지 않고 중앙에서 일관된 오류 응답을 만들 수 있다. 운영 환경에서는 내부 스택 트레이스나 파일 경로를 사용자에게 그대로 보여주지 않는 것이 중요하다.</p>
                    """ + fig(l06, 61, "인증 미들웨어 작성", "로그인 여부나 권한을 확인하는 미들웨어를 라우트 앞에 배치한다.") + """
                    <p>인증 미들웨어는 보안 실습에서 특히 중요하다. 사용자가 로그인했는지, 어떤 권한을 갖는지, 요청한 리소스에 접근 가능한지 확인한 뒤 허용해야 한다. 검증이 끝나지 않은 요청을 다음 단계로 넘기면 접근 제어 취약점이 생긴다.</p>
                    """,
                },
            ],
            "checks": [
                "미들웨어와 라우트 handler의 차이를 설명할 수 있는가?",
                "next()를 호출하지 않으면 어떤 일이 생기는지 말할 수 있는가?",
                "에러 처리 미들웨어의 인자가 네 개인 이유를 이해하는가?",
                "인증 미들웨어를 어느 위치에 등록해야 하는지 설명할 수 있는가?",
            ],
        },
        {
            "id": "1-7",
            "title": "Node.js 전역 객체와 내장 모듈",
            "subtitle": "global, process, require, __dirname, __filename 같은 전역 객체와 fs, path, child_process 등 내장 모듈을 정리한다.",
            "tags": ["전역 객체", "내장 모듈", "process"],
            "objectives": [
                "Node.js에서 브라우저와 다른 전역 객체를 이해한다.",
                "require와 모듈 로딩 방식을 설명한다.",
                "process, __dirname, __filename의 용도를 익힌다.",
                "fs, path, child_process 같은 내장 모듈이 보안상 어떤 의미를 갖는지 이해한다.",
            ],
            "sections": [
                {
                    "heading": "전역 객체",
                    "body": """
                    """ + fig(l07, 2, "Node.js 전역 객체", "global, process, console, require, __dirname, __filename 등이 Node.js 전역 객체로 소개된다.") + """
                    <p>브라우저 JavaScript에는 `window`가 있지만 Node.js에는 서버 실행 환경에 맞는 전역 객체들이 있다. `global`은 전역 공간, `process`는 현재 Node 프로세스 정보, `console`은 로그 출력, `require`는 모듈 로딩, `__dirname`과 `__filename`은 현재 파일 위치를 알려준다.</p>
                    """ + node_globals + """
                    <p>보안 실습에서는 파일 경로, 환경 변수, 실행 인자, 현재 작업 디렉터리가 자주 등장한다. 특히 환경 변수에는 비밀 키나 API 토큰이 들어갈 수 있으므로 로그로 그대로 출력하거나 클라이언트에 노출하면 안 된다.</p>
                    """,
                },
                {
                    "heading": "require와 모듈",
                    "body": """
                    """ + fig(l07, 8, "require 사용", "require로 내장 모듈이나 설치된 패키지를 가져오는 방식이 제시된다.") + """
                    <p>`require()`는 CommonJS 방식의 모듈 로딩 함수다. Node.js 내장 모듈, npm으로 설치한 외부 패키지, 직접 만든 파일을 가져올 수 있다. 강의에서는 `child_process`처럼 명령 실행과 관련된 모듈도 예시로 등장한다.</p>
                    <p>내장 모듈은 강력하다. `fs`는 파일을 읽고 쓰며, `path`는 경로를 안전하게 조합하고, `child_process`는 외부 프로세스를 실행한다. 사용자의 입력이 이 모듈들로 직접 흘러 들어가면 Path Traversal, 임의 파일 읽기, Command Injection으로 이어질 수 있다.</p>
                    """ + fig(l07, 15, "child_process 출력", "외부 명령 실행 결과가 버퍼로 반환되는 모습을 확인한다.") + """
                    """,
                },
                {
                    "heading": "process와 디버깅",
                    "body": """
                    """ + fig(l07, 23, "process 객체", "process 객체는 실행 경로, 환경 변수, 플랫폼, 버전 같은 Node 프로세스 정보를 담는다.") + """
                    <p>`process`는 현재 실행 중인 Node 프로세스의 상태를 다룬다. `process.argv`는 실행 인자, `process.env`는 환경 변수, `process.cwd()`는 현재 작업 디렉터리, `process.exit()`는 종료를 제어한다. 서버 운영에서는 환경 변수로 포트, DB 주소, 비밀 키를 주입하는 일이 많다.</p>
                    """ + fig(l07, 31, "Node.js 디버깅", "VS Code 디버깅을 사용해 코드 실행 흐름과 변수 상태를 확인한다.") + """
                    <p>디버깅은 단순한 편의 기능이 아니라 보안 분석에도 중요하다. 라우트가 어떤 요청값을 받는지, 미들웨어가 어떤 순서로 실행되는지, 템플릿에 어떤 데이터가 전달되는지 중단점으로 확인하면 취약점 흐름을 훨씬 정확히 이해할 수 있다.</p>
                    """,
                },
            ],
            "checks": [
                "브라우저의 window와 Node.js의 global 차이를 설명할 수 있는가?",
                "require가 어떤 종류의 모듈을 가져올 수 있는지 말할 수 있는가?",
                "process.env에 민감 정보가 들어갈 수 있음을 이해하는가?",
                "fs, path, child_process 사용 시 입력 검증이 필요한 이유를 설명할 수 있는가?",
            ],
        },
        {
            "id": "1-8",
            "title": "EJS 템플릿 엔진",
            "subtitle": "Express에서 EJS를 등록하고, 데이터를 HTML에 삽입하며, include와 조건문·반복문으로 화면을 구성한다.",
            "tags": ["EJS", "템플릿", "렌더링"],
            "objectives": [
                "템플릿 엔진이 HTML과 동적 데이터를 결합하는 도구임을 이해한다.",
                "Express에서 EJS를 view engine으로 등록한다.",
                "<%= %>, <% %>, include의 차이를 설명한다.",
                "템플릿 출력과 보안의 관계를 이해한다.",
            ],
            "sections": [
                {
                    "heading": "템플릿 엔진의 역할",
                    "body": """
                    """ + fig(l08, 2, "템플릿 엔진 EJS", "EJS는 HTML 안에 JavaScript 구문을 넣어 동적 HTML을 생성하는 템플릿 엔진이다.") + """
                    <p>템플릿 엔진은 서버의 데이터와 HTML 구조를 결합해 최종 HTML을 만든다. EJS는 Embedded JavaScript Template의 약자로, HTML 안에 JavaScript 표현식과 제어문을 넣을 수 있다. Express에서는 `res.render()`를 호출하면 EJS 템플릿에 데이터를 넣어 응답 HTML을 만든다.</p>
                    <p>강의는 EJS의 장점으로 익숙한 문법, 서버 사이드 렌더링, 적은 학습 부담을 설명한다. JavaScript를 이미 알고 있다면 템플릿 문법을 빠르게 읽을 수 있다.</p>
                    """ + fig(l08, 16, "EJS의 장점", "익숙한 문법, 서버 사이드 렌더링, 비교적 낮은 의존성이 장점으로 정리된다.") + """
                    """,
                },
                {
                    "heading": "Express에 EJS 등록",
                    "body": """
                    """ + fig(l08, 19, "EJS 미들웨어 등록", "app.set으로 view engine과 views 경로를 등록한다.") + ejs_basic + """
                    <p>`app.set("view engine", "ejs")`는 Express가 `.ejs` 파일을 템플릿으로 렌더링하도록 설정한다. `views` 경로를 지정하면 Express는 그 폴더에서 템플릿 파일을 찾는다. 라우트에서는 `res.render("notes", data)`처럼 파일 이름과 데이터 객체를 넘긴다.</p>
                    """,
                },
                {
                    "heading": "EJS 문법",
                    "body": """
                    """ + fig(l08, 23, "EJS 실습", "템플릿 파일을 만들고 서버 데이터가 HTML에 출력되는지 확인한다.") + ejs_template + """
                    <table>
                      <thead><tr><th>문법</th><th>의미</th><th>주의</th></tr></thead>
                      <tbody>
                        <tr><td><code>&lt;%= value %&gt;</code></td><td>값을 HTML 이스케이프하여 출력한다.</td><td>사용자 입력 출력에 기본적으로 더 안전하다.</td></tr>
                        <tr><td><code>&lt;%- value %&gt;</code></td><td>값을 이스케이프하지 않고 원문 HTML로 출력한다.</td><td>XSS 위험이 커서 신뢰된 HTML에만 사용한다.</td></tr>
                        <tr><td><code>&lt;% code %&gt;</code></td><td>조건문, 반복문 등 실행 코드를 넣는다.</td><td>출력은 하지 않는다.</td></tr>
                        <tr><td><code>&lt;%- include("file") %&gt;</code></td><td>다른 템플릿 조각을 포함한다.</td><td>공통 헤더, 푸터, 메뉴에 자주 사용한다.</td></tr>
                      </tbody>
                    </table>
                    """ + fig(l08, 43, "include 실습", "공통 템플릿 조각을 분리해 include로 재사용한다.") + fig(l08, 53, "조건문과 반복문", "EJS 안에서 조건문과 반복문으로 데이터 목록을 화면에 구성한다.") + """
                    """,
                },
                {
                    "heading": "출력과 보안",
                    "body": """
                    """ + fig(l08, 83, "렌더링 결과 확인", "브라우저에서 EJS 템플릿이 HTML로 렌더링된 결과를 확인한다.") + """
                    <p>EJS는 서버에서 HTML을 만드는 도구이므로 사용자의 입력이 템플릿으로 들어갈 때 주의해야 한다. 사용자 입력은 템플릿 코드가 아니라 데이터로만 전달해야 한다. 출력할 때는 기본적으로 이스케이프되는 `<%= %>`를 사용하고, `<%- %>`는 반드시 신뢰 가능한 HTML에만 제한해야 한다.</p>
                    <p>다음 강의의 EJS RCE는 이 경계가 깨질 때 어떤 일이 생기는지 다룬다. 템플릿 파일, 렌더 옵션, 사용자 데이터의 경계를 분명히 구분하는 것이 핵심이다.</p>
                    """,
                },
            ],
            "checks": [
                "템플릿 엔진이 필요한 이유를 설명할 수 있는가?",
                "res.render에 전달되는 템플릿 이름과 데이터 객체의 역할을 구분할 수 있는가?",
                "<%= %>와 <%- %>의 보안상 차이를 말할 수 있는가?",
                "include, 조건문, 반복문을 EJS에서 어떻게 쓰는지 이해하는가?",
            ],
        },
        {
            "id": "1-9",
            "title": "Prototype Pollution",
            "subtitle": "JavaScript Prototype 체인을 이해하고, __proto__나 constructor.prototype 조작이 전체 객체 동작을 바꾸는 취약점으로 이어지는 과정을 정리한다.",
            "tags": ["Prototype Pollution", "__proto__", "JavaScript 보안"],
            "objectives": [
                "JavaScript 객체가 Prototype을 통해 속성과 메서드를 찾는 방식을 이해한다.",
                "Prototype chain, constructor, __proto__의 관계를 설명한다.",
                "Prototype Pollution이 어떤 입력 처리에서 발생하는지 이해한다.",
                "취약 병합 로직과 방어 방법을 정리한다.",
            ],
            "sections": [
                {
                    "heading": "JavaScript Prototype",
                    "body": """
                    """ + fig(l09, 2, "JavaScript Prototype", "문자열, 배열, 숫자 같은 객체도 Prototype을 통해 공통 기능을 참조한다.") + """
                    <p>JavaScript의 객체는 자기 자신에게 없는 속성이나 메서드를 Prototype 체인을 따라 위쪽 객체에서 찾는다. 예를 들어 문자열 객체는 String.prototype의 메서드를, 배열은 Array.prototype의 메서드를 사용할 수 있다. 이 구조 덕분에 모든 배열이 `map`, `filter`, `push` 같은 공통 기능을 공유한다.</p>
                    """ + fig(l09, 19, "Prototype 관계 도식", "기존 객체와 새 객체가 prototype 관계로 이어지는 구조를 시각화한다.") + """
                    <p>Prototype은 재사용을 가능하게 하지만, 그만큼 전역적인 영향도 크다. 많은 객체가 공유하는 상위 Prototype이 오염되면 새로 만든 평범한 객체까지 오염된 속성을 가진 것처럼 동작할 수 있다.</p>
                    """,
                },
                {
                    "heading": "Prototype chain과 constructor",
                    "body": """
                    """ + fig(l09, 28, "Prototype chain", "Object.prototype 아래에 String, Array, Number prototype이 연결되고 개별 값이 다시 연결된다.") + """
                    <p>Prototype chain은 특정 객체에서 시작해 그 객체의 Prototype, 그 위의 Prototype으로 이어지는 검색 경로다. 속성 조회는 현재 객체에서 먼저 시도되고, 없으면 체인을 따라 올라간다. `constructor`는 객체를 만든 함수와 연결되며, `constructor.prototype`을 통해 Prototype 객체에 접근할 수 있다.</p>
                    """ + fig(l09, 35, "Constructor와 Prototype", "constructor와 prototype의 관계를 이용하면 객체 생성 구조를 이해할 수 있다.") + """
                    """,
                },
                {
                    "heading": "Prototype Pollution의 의미",
                    "body": """
                    """ + fig(l09, 42, "Prototype Pollution 정의", "Object.prototype에 임의 속성을 추가할 수 있게 하는 JavaScript 취약점으로 정의된다.") + """
                    <p>Prototype Pollution은 공격자가 일반 객체의 데이터만 바꾸는 것이 아니라 Prototype 객체, 특히 Object.prototype 같은 상위 객체에 속성을 심어 전체 객체 동작에 영향을 주는 취약점이다. 강의에서는 이를 “객체 전체의 Prototype에 임의 속성을 추가할 수 있게 하는 취약점”으로 설명한다.</p>
                    <p>대표적인 위험 키는 `__proto__`, `prototype`, `constructor`다. 안전하지 않은 병합 함수, 쿼리 파서, JSON 처리 로직이 이 키를 필터링하지 않고 재귀적으로 객체에 반영하면 Prototype이 오염될 수 있다.</p>
                    """ + fig(l09, 45, "__proto__ 접근", "__proto__를 통해 Prototype 경로에 접근하는 실습 화면이다.") + """
                    """,
                },
                {
                    "heading": "취약 실습과 영향",
                    "body": """
                    """ + fig(l09, 55, "Prototype Pollution 개요", "오염된 속성이 새 객체 조회 결과에 영향을 주는 흐름을 확인한다.") + prototype_pollution_demo + """
                    <p>예제에서 공격자는 `{"__proto__": {"isAdmin": true}}` 같은 데이터를 보낸다. 취약한 병합 함수가 이를 재귀적으로 처리하면 `Object.prototype.isAdmin`이 생기고, 이후 `{}`처럼 새로 만든 객체도 `isAdmin`이 있는 것처럼 평가될 수 있다. 권한 검사를 `if (user.isAdmin)`처럼 느슨하게 작성했다면 관리자 권한 우회로 이어질 수 있다.</p>
                    """ + fig(l09, 61, "Prototype Pollution 실습", "실제 코드에서 병합과 입력 데이터가 Prototype 오염으로 이어지는 흐름을 따라간다.") + """
                    <p>영향은 권한 우회에만 그치지 않는다. 템플릿 옵션 오염, 로깅 설정 변경, 요청 처리 분기 변경, DoS, 경우에 따라 RCE 체인까지 이어질 수 있다. 다음 강의의 EJS RCE 분석도 이런 Prototype Pollution 관점과 연결된다.</p>
                    """,
                },
                {
                    "heading": "방어 방법",
                    "body": """
                    """ + prototype_pollution_guard + """
                    <p>방어의 기본은 위험 키 차단, 입력 스키마 검증, 안전한 병합 함수 사용, 의존성 업데이트다. 객체 병합이 필요할 때는 `__proto__`, `constructor`, `prototype`을 거부하고, 가능한 경우 허용 목록 방식으로 필요한 필드만 받는다. 민감한 객체는 `Object.create(null)`처럼 Prototype이 없는 객체로 만들 수도 있다.</p>
                    <p>또한 라이브러리 취약점이 자주 공개되므로 npm 패키지 버전 관리가 중요하다. `npm audit` 결과를 맹목적으로 믿기보다 실제 공격 가능성과 패치 영향을 함께 검토해야 한다.</p>
                    """,
                },
            ],
            "checks": [
                "Prototype chain을 따라 속성이 검색되는 과정을 설명할 수 있는가?",
                "__proto__, constructor, prototype이 왜 위험 키인지 말할 수 있는가?",
                "Prototype Pollution이 권한 우회로 이어지는 과정을 설명할 수 있는가?",
                "안전한 병합 로직의 핵심 방어 방법을 정리할 수 있는가?",
            ],
        },
        {
            "id": "1-10",
            "title": "EJS 템플릿 원격 코드 실행",
            "subtitle": "EJS 템플릿과 렌더 옵션이 사용자 입력 또는 Prototype Pollution과 섞일 때 원격 코드 실행으로 이어질 수 있는 흐름을 분석한다.",
            "tags": ["EJS RCE", "템플릿 인젝션", "RCE"],
            "objectives": [
                "RCE가 서버에서 공격자 의도 코드가 실행되는 상황임을 이해한다.",
                "EJS 템플릿, 데이터, 렌더 옵션의 경계를 구분한다.",
                "사용자 입력을 템플릿으로 렌더링하는 위험을 설명한다.",
                "EJS RCE를 막기 위한 안전한 렌더링 원칙을 정리한다.",
            ],
            "sections": [
                {
                    "heading": "RCE 분석의 출발점",
                    "body": """
                    """ + fig(l10, 1, "EJS RCE 분석", "마지막 강의는 EJS 템플릿 렌더링이 원격 코드 실행으로 이어지는 조건을 분석한다.") + """
                    <p>RCE(Remote Code Execution)는 원격 공격자가 서버에서 자신이 원하는 코드를 실행하게 만드는 취약점이다. 웹 애플리케이션에서 RCE는 파일 읽기, 명령 실행, 환경 변수 탈취, 내부망 접근 같은 심각한 영향으로 이어질 수 있다.</p>
                    <p>EJS는 템플릿 안에서 JavaScript 구문을 실행해 HTML을 만든다. 정상 사용에서는 템플릿 파일은 개발자가 작성하고, 사용자는 데이터만 제공한다. 위험은 이 경계가 깨져 사용자의 입력이 템플릿 코드나 렌더 옵션에 영향을 줄 때 생긴다.</p>
                    """ + fig(l10, 8, "실습 애플리케이션 확인", "브라우저와 코드 편집기를 함께 보며 취약 흐름을 추적한다.") + """
                    """,
                },
                {
                    "heading": "위험한 렌더링 경계",
                    "body": """
                    """ + ejs_rce_unsafe + """
                    <p>위험한 패턴은 사용자가 보낸 문자열을 템플릿 자체로 렌더링하는 것이다. 템플릿은 실행 가능한 코드 조각을 포함할 수 있으므로, 사용자 입력이 템플릿이 되면 서버가 공격자 코드를 해석하는 구조가 된다. 또한 일부 취약한 흐름에서는 사용자가 렌더 옵션을 오염시켜 템플릿 컴파일 방식에 영향을 줄 수 있다.</p>
                    <p>강의의 긴 실습 화면은 코드에서 어떤 값이 EJS로 전달되는지, 에러 스택이 어디를 가리키는지, 템플릿 컴파일 과정에서 어떤 옵션이 참조되는지를 추적하는 방식으로 진행된다. 보안 분석에서는 오류 메시지와 스택 트레이스를 단서로 입력이 어느 함수까지 도달했는지 확인해야 한다.</p>
                    """ + fig(l10, 68, "에러 스택 확인", "렌더링 실패와 스택 정보를 통해 EJS 내부 처리 흐름을 추적한다.") + """
                    """,
                },
                {
                    "heading": "Prototype Pollution과의 연결",
                    "body": """
                    <p>이전 강의의 Prototype Pollution은 EJS RCE와 연결될 수 있다. 만약 애플리케이션이나 라이브러리가 렌더 옵션을 만들 때 평범한 객체를 사용하고, 공격자가 Object.prototype에 특정 속성을 심을 수 있다면, EJS가 옵션을 읽는 과정에서 공격자가 심은 값이 사용될 수 있다.</p>
                    <p>즉 공격 흐름은 보통 한 단계로 끝나지 않는다. 먼저 입력 병합, 쿼리 파싱, 객체 처리 취약점으로 Prototype을 오염시키고, 그 다음 템플릿 엔진이 오염된 옵션을 참조하게 만들어 코드 실행에 가까워진다. 이런 체인형 취약점은 각 단계만 따로 보면 사소해 보일 수 있어 더 위험하다.</p>
                    """ + fig(l10, 74, "템플릿 옵션 추적", "코드와 실행 결과를 번갈아 보며 어떤 값이 템플릿 처리 옵션으로 들어가는지 확인한다.") + """
                    """,
                },
                {
                    "heading": "안전한 EJS 사용 원칙",
                    "body": """
                    """ + ejs_rce_safe + """
                    <ul class="check-list">
                      <li>사용자 입력을 템플릿 문자열로 렌더링하지 않는다.</li>
                      <li>템플릿 파일은 서버 코드와 함께 고정하고, 사용자는 데이터 객체로만 전달한다.</li>
                      <li><code>&lt;%- %&gt;</code>처럼 이스케이프하지 않는 출력은 신뢰된 HTML에만 제한한다.</li>
                      <li>렌더 옵션을 사용자 입력에서 만들지 않고, 허용 목록으로 필요한 옵션만 명시한다.</li>
                      <li>Prototype Pollution 방어를 적용하고 EJS와 관련 패키지를 최신 보안 버전으로 유지한다.</li>
                      <li>운영 환경에서는 스택 트레이스와 내부 경로를 사용자에게 노출하지 않는다.</li>
                    </ul>
                    """ + fig(l10, 104, "최종 동작 검증", "수정한 흐름이 의도한 데이터 렌더링으로만 동작하는지 확인한다.") + """
                    <p>핵심은 템플릿, 옵션, 데이터의 경계를 끝까지 유지하는 것이다. EJS 자체가 위험한 도구라기보다, 실행 가능한 템플릿 영역에 사용자가 개입할 수 있을 때 위험해진다.</p>
                    """,
                },
            ],
            "checks": [
                "RCE가 왜 웹 취약점 중에서도 심각한지 설명할 수 있는가?",
                "템플릿 파일과 사용자 데이터의 경계를 구분할 수 있는가?",
                "Prototype Pollution이 템플릿 옵션 오염으로 이어질 수 있음을 이해하는가?",
                "EJS를 안전하게 사용하는 원칙을 정리할 수 있는가?",
            ],
        },
    ]
