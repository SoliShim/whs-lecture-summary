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
