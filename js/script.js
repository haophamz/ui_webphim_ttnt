/* N4 Episodes Module – script.js */
/* Minimal JS, giao diện chủ yếu CSS */

(function () {
  // Highlight nav link active dựa theo URL hiện tại
  var links = document.querySelectorAll('.nav-links a');
  links.forEach(function (a) {
    if (a.href === window.location.href) {
      a.style.color = 'var(--accent)';
    }
  });
})();
