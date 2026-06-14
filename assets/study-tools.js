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
    setupLectureSideGuide();
    setupLectureControls();
  };

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initStudyTools);
  } else {
    initStudyTools();
  }
})();
