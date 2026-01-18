const hide = () => {
  document
    .querySelectorAll('#content.ytd-rich-section-renderer')
    .forEach((e) => (e.style.display = 'none'));
};

const setup = () => {
  hide();
  new MutationObserver(hide).observe(document.body, {
    childList: true,
    subtree: true,
  });
};

if (document.readyState === 'loading') {
  const trySetup = () => {
    if (document.body) {
      setup();
    } else {
      requestAnimationFrame(trySetup);
    }
  };
  trySetup();
} else {
  setup();
}
