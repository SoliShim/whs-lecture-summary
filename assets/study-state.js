(() => {
  const progressStorageKey = "whitehatLectureProgress.v1";
  const notesStorageKey = "whitehatLectureNotes.v1";

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

  const getNoteText = (entry) => {
    if (typeof entry === "string") {
      return entry;
    }
    return String(entry?.text || "");
  };

  const hasNote = (notes, key) => getNoteText(notes[key]).trim().length > 0;

  const formatSavedAt = (value) => {
    const date = new Date(value);
    if (Number.isNaN(date.getTime())) {
      return "방금 저장";
    }
    return `${date.toLocaleDateString("ko-KR", {
      month: "numeric",
      day: "numeric",
    })} ${date.toLocaleTimeString("ko-KR", {
      hour: "2-digit",
      minute: "2-digit",
    })}`;
  };

  const clipNote = (text) => {
    const normalized = text.replace(/\s+/g, " ").trim();
    return normalized.length > 120 ? `${normalized.slice(0, 120)}...` : normalized;
  };

  const collectLectureMeta = () => {
    const meta = new Map();
    document.querySelectorAll(".lecture-card[data-lesson-key]").forEach((card) => {
      const key = card.dataset.lessonKey;
      if (!key) {
        return;
      }
      meta.set(key, {
        label: card.querySelector(".lecture-id")?.textContent.trim() || key.split(":")[1],
        title: card.querySelector("h3")?.textContent.trim() || "강의 메모",
        href: card.querySelector(".card-actions a")?.getAttribute("href") || "#lectures",
      });
    });
    return meta;
  };

  const updateNoteIndicators = (notes) => {
    document.querySelectorAll(".lecture-card[data-lesson-key], body[data-lesson-key]").forEach((element) => {
      const key = element.dataset.lessonKey;
      element.classList.toggle("has-note", hasNote(notes, key));
    });

    document.querySelectorAll(".lecture-card[data-lesson-key]").forEach((card) => {
      const indicator = card.querySelector("[data-note-presence]");
      if (indicator) {
        indicator.hidden = !hasNote(notes, card.dataset.lessonKey);
      }
    });
  };

  const updateCourseNotePanel = (notes) => {
    const panel = document.querySelector("[data-course-note-panel]");
    if (!panel) {
      return;
    }

    const courseId = panel.dataset.courseId;
    const list = panel.querySelector("[data-course-note-list]");
    if (!courseId || !list) {
      return;
    }

    const meta = collectLectureMeta();
    const entries = Object.entries(notes)
      .map(([key, entry]) => ({
        key,
        entry,
        text: getNoteText(entry).trim(),
      }))
      .filter((item) => item.text && getCourseId(item.key) === courseId)
      .sort((a, b) => {
        const aTime = new Date(a.entry?.updatedAt || 0).getTime();
        const bTime = new Date(b.entry?.updatedAt || 0).getTime();
        return bTime - aTime;
      })
      .slice(0, 6);

    list.replaceChildren();
    if (!entries.length) {
      const empty = document.createElement("p");
      empty.className = "empty-study-note";
      empty.textContent = "아직 이 과목에 저장한 메모가 없습니다.";
      list.append(empty);
      return;
    }

    entries.forEach(({ key, entry, text }) => {
      const fallback = meta.get(key) || {};
      const item = document.createElement("a");
      item.className = "course-note-item";
      item.href = fallback.href || "#lectures";

      const title = document.createElement("strong");
      const label = entry?.label || fallback.label || key.split(":")[1] || "강의";
      title.textContent = `${label} · ${entry?.title || fallback.title || "강의 메모"}`;

      const body = document.createElement("p");
      body.textContent = clipNote(text);

      const saved = document.createElement("span");
      saved.textContent = formatSavedAt(entry?.updatedAt);

      item.append(title, body, saved);
      list.append(item);
    });
  };

  const applyNotes = (notes) => {
    updateNoteIndicators(notes);
    updateCourseNotePanel(notes);
    document.dispatchEvent(new CustomEvent("whitehat-notes-change"));
  };

  const bindPersonalNote = (notes) => {
    const textarea = document.querySelector("[data-lesson-note]");
    if (!textarea) {
      return;
    }

    const key = document.body.dataset.lessonKey;
    const status = document.querySelector("[data-note-save-status]");
    const clearButton = document.querySelector("[data-note-clear]");
    if (!key) {
      textarea.disabled = true;
      if (status) {
        status.textContent = "이 강의 정보를 찾을 수 없어 메모를 저장할 수 없습니다";
      }
      return;
    }

    const updateStatus = () => {
      const text = getNoteText(notes[key]).trim();
      if (!status) {
        return;
      }
      if (!text) {
        status.textContent = "아직 저장된 메모가 없습니다";
        return;
      }
      status.textContent = `자동 저장됨 · ${text.length}자 · ${formatSavedAt(notes[key]?.updatedAt)}`;
    };

    const save = () => {
      const rawText = textarea.value;
      const text = rawText.trim();
      if (text) {
        notes[key] = {
          text: rawText,
          updatedAt: new Date().toISOString(),
          courseId: document.body.dataset.courseId || getCourseId(key),
          lessonId: document.body.dataset.lessonId || key.split(":")[1],
          title: document.body.dataset.lessonTitle || document.querySelector(".lecture-hero h1")?.textContent.trim() || "강의 메모",
          label: document.body.dataset.lessonLabel || document.querySelector(".lecture-hero .small-label")?.textContent.trim() || key.split(":")[1],
        };
      } else {
        delete notes[key];
      }
      safeWrite(notesStorageKey, notes);
      updateStatus();
      applyNotes(notes);
    };

    textarea.value = getNoteText(notes[key]);
    updateStatus();
    textarea.addEventListener("input", save);
    clearButton?.addEventListener("click", () => {
      textarea.value = "";
      save();
      textarea.focus();
    });
  };

  document.addEventListener("DOMContentLoaded", () => {
    const state = safeRead(progressStorageKey);
    const notes = safeRead(notesStorageKey);
    bindToggles(state);
    applyState(state);
    bindPersonalNote(notes);
    applyNotes(notes);
  });
})();
