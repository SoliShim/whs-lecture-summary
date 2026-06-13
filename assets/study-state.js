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
