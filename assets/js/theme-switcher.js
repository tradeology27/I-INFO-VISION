/* ===================================================
   I INFO VISION — THEMES INTERACTIVE HELPER SCRIPT
   Universal Drawer, Swatch Copying & Micro-interactions
   =================================================== */

document.addEventListener('DOMContentLoaded', () => {
  // Select drawer elements supporting both kebab-case and camelCase IDs
  const inspectBtns = document.querySelectorAll('#theme-inspect-btn, .theme-inspect-btn');
  const drawer = document.getElementById('theme-drawer') || document.getElementById('themeDrawer');
  const overlay = document.getElementById('theme-drawer-overlay') || document.getElementById('themeDrawerOverlay');
  const closeBtn = document.getElementById('theme-drawer-close') || document.querySelector('#themeDrawer button');

  function openDrawer() {
    if (drawer) {
      drawer.classList.add('open');
      drawer.style.right = '0px';
    }
    if (overlay) {
      overlay.classList.add('open');
      overlay.style.display = 'block';
    }
    document.body.style.overflow = 'hidden';
  }

  function closeDrawer() {
    if (drawer) {
      drawer.classList.remove('open');
      drawer.style.right = '-480px';
    }
    if (overlay) {
      overlay.classList.remove('open');
      overlay.style.display = 'none';
    }
    document.body.style.overflow = '';
  }

  inspectBtns.forEach(btn => {
    btn.addEventListener('click', (e) => {
      e.preventDefault();
      const isOpen = drawer && (drawer.classList.contains('open') || drawer.style.right === '0px');
      if (isOpen) {
        closeDrawer();
      } else {
        openDrawer();
      }
    });
  });

  if (closeBtn) closeBtn.addEventListener('click', closeDrawer);
  if (overlay) overlay.addEventListener('click', closeDrawer);

  // Expose global toggleThemeDrawer for inline onclick handlers
  window.toggleThemeDrawer = function() {
    const d = document.getElementById('theme-drawer') || document.getElementById('themeDrawer');
    const o = document.getElementById('theme-drawer-overlay') || document.getElementById('themeDrawerOverlay');
    const isOpen = d && (d.classList.contains('open') || d.style.right === '0px');
    if (isOpen) {
      closeDrawer();
    } else {
      openDrawer();
    }
  };

  // Esc key closes drawer
  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') closeDrawer();
  });

  // Swatch color copy to clipboard
  const swatches = document.querySelectorAll('.theme-swatch');
  swatches.forEach(swatch => {
    swatch.addEventListener('click', () => {
      const hex = swatch.getAttribute('data-hex') || swatch.querySelector('.theme-swatch-hex')?.textContent;
      if (hex) {
        navigator.clipboard.writeText(hex.trim()).then(() => {
          showToast(`Copied color ${hex.trim()} to clipboard!`);
        });
      }
    });
  });

  // Toast notification helper
  function showToast(message) {
    let toast = document.getElementById('theme-toast');
    if (!toast) {
      toast = document.createElement('div');
      toast.id = 'theme-toast';
      toast.style.cssText = `
        position: fixed;
        bottom: 24px;
        left: 50%;
        transform: translateX(-50%);
        background: #0f172a;
        color: #ffffff;
        padding: 10px 20px;
        border-radius: 999px;
        font-size: 13.5px;
        font-weight: 600;
        z-index: 100000;
        box-shadow: 0 4px 16px rgba(0,0,0,0.3);
        opacity: 0;
        transition: opacity 0.25s ease;
        pointer-events: none;
      `;
      document.body.appendChild(toast);
    }
    toast.textContent = message;
    toast.style.opacity = '1';
    setTimeout(() => {
      toast.style.opacity = '0';
    }, 2200);
  }
});
