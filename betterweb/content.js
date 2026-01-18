const hide = () => {
  const selectors = [
    '#content.ytd-rich-section-renderer',
    'ytd-reel-shelf-renderer',
    '.style-scope.ytd-reel-shelf-renderer'
  ];
  selectors.forEach((sel) => {
    document.querySelectorAll(sel).forEach((e) => {
      e.style.display = 'none';
    });
  });
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
