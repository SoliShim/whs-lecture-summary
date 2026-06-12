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

  document.addEventListener("DOMContentLoaded", () => {
    setupCourseFinder();
    setupLectureFinder();
  });
})();
