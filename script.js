/* ===================================================
   i Info Vision — Enterprise Landing Page
   Interactive JavaScript
   =================================================== */

document.addEventListener('DOMContentLoaded', () => {
  // ── HERO CAROUSEL ──
  initCarousel();
  // ── HEADER SCROLL ──
  initHeaderScroll();
  // ── MOBILE NAV ──
  initMobileNav();
  // ── SERVICE TABS ──
  initServiceTabs();
  // ── SCROLL REVEAL ──
  initScrollReveal();
  // ── STAT COUNTER ──
  initStatCounters();
  // ── BACK TO TOP ──
  initBackToTop();
  // ── SMOOTH SCROLL ──
  initSmoothScroll();
  // ── ACTIVE NAV ──
  initActiveNav();
  // ── SERVICE CARD ANIMATIONS ──
  initServiceCardAnimations();
  // ── CONTACT FORM ANIMATION ──
  initContactFormAnimation();
});


/* ───────────────────────────────────────────
   HERO CAROUSEL
   ─────────────────────────────────────────── */
function initCarousel() {
  const slides = document.querySelectorAll('.carousel-slide');
  const dots = document.querySelectorAll('.carousel-dot');
  const prevBtn = document.getElementById('carousel-prev');
  const nextBtn = document.getElementById('carousel-next');
  let current = 0;
  let interval;
  const DURATION = 6000;

  function goTo(index) {
    // Deactivate current
    slides[current].classList.remove('active');
    dots[current].classList.remove('active');

    // Force reflow for dot animation restart
    void dots[index].offsetWidth;

    current = index;

    // Activate new
    slides[current].classList.add('active');
    dots[current].classList.add('active');

    resetTimer();
  }

  function next() {
    goTo((current + 1) % slides.length);
  }

  function prev() {
    goTo((current - 1 + slides.length) % slides.length);
  }

  function resetTimer() {
    clearInterval(interval);
    interval = setInterval(next, DURATION);
  }

  // Event listeners
  nextBtn.addEventListener('click', next);
  prevBtn.addEventListener('click', prev);

  dots.forEach(dot => {
    dot.addEventListener('click', () => {
      const idx = parseInt(dot.dataset.index);
      if (idx !== current) goTo(idx);
    });
  });

  // Touch/swipe support
  let touchStartX = 0;
  let touchEndX = 0;
  const carousel = document.getElementById('hero-carousel');

  carousel.addEventListener('touchstart', e => {
    touchStartX = e.changedTouches[0].screenX;
  }, { passive: true });

  carousel.addEventListener('touchend', e => {
    touchEndX = e.changedTouches[0].screenX;
    const diff = touchStartX - touchEndX;
    if (Math.abs(diff) > 60) {
      diff > 0 ? next() : prev();
    }
  }, { passive: true });

  // Keyboard navigation
  document.addEventListener('keydown', e => {
    if (e.key === 'ArrowRight') next();
    if (e.key === 'ArrowLeft') prev();
  });

  // Start auto-play
  goTo(0);
}


/* ───────────────────────────────────────────
   HEADER SCROLL EFFECT
   ─────────────────────────────────────────── */
function initHeaderScroll() {
  // Navigation bar is always visible (white background), so no scroll toggle needed.
}


/* ───────────────────────────────────────────
   MOBILE NAVIGATION
   ─────────────────────────────────────────── */
function initMobileNav() {
  const toggle = document.getElementById('nav-toggle');
  const menu = document.getElementById('nav-menu');
  const overlay = document.getElementById('mobile-overlay');
  const links = menu.querySelectorAll('.nav-link, .nav-cta');

  function closeMenu() {
    toggle.classList.remove('active');
    menu.classList.remove('open');
    overlay.classList.remove('open');
    document.body.style.overflow = '';
  }


  function openMenu() {
    toggle.classList.add('active');
    menu.classList.add('open');
    overlay.classList.add('open');
    document.body.style.overflow = 'hidden';
  }

  toggle.addEventListener('click', () => {
    menu.classList.contains('open') ? closeMenu() : openMenu();
  });

  document.addEventListener('click', (e) => {
    if (menu.classList.contains('open') && !menu.contains(e.target) && !toggle.contains(e.target)) {
      closeMenu();
    }
  });

  links.forEach(link => {
    link.addEventListener('click', closeMenu);
  });
}


/* ───────────────────────────────────────────
   SERVICE TABS
   ─────────────────────────────────────────── */
function initServiceTabs() {
  const tabs = document.querySelectorAll('.services-tab');
  const panels = document.querySelectorAll('.services-panel');

  tabs.forEach(tab => {
    tab.addEventListener('click', () => {
      const target = tab.dataset.tab;

      // Deactivate all
      tabs.forEach(t => t.classList.remove('active'));
      panels.forEach(p => p.classList.remove('active'));

      // Activate target
      tab.classList.add('active');
      const panel = document.getElementById(`panel-${target}`);
      panel.classList.add('active');

      // Re-trigger reveal for new panel's cards
      const cards = panel.querySelectorAll('.reveal');
      cards.forEach(card => {
        card.classList.remove('visible');
        void card.offsetWidth; // Force reflow
      });

      // Stagger reveal
      setTimeout(() => {
        cards.forEach((card, i) => {
          setTimeout(() => card.classList.add('visible'), i * 80);
        });
      }, 50);
    });
  });
}


/* ───────────────────────────────────────────
   SCROLL REVEAL (Intersection Observer)
   ─────────────────────────────────────────── */
function initScrollReveal() {
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
        }
      });
    },
    {
      threshold: 0.1,
      rootMargin: '0px 0px -40px 0px'
    }
  );

  document.querySelectorAll('.reveal').forEach(el => observer.observe(el));

  // Word-by-word text reveal observer
  const textRevealObserver = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          entry.target.classList.add('is-visible');
        }
      });
    },
    {
      threshold: 0.2,
      rootMargin: '0px 0px -40px 0px'
    }
  );

  document.querySelectorAll('.text-reveal-words').forEach(el => textRevealObserver.observe(el));
}


/* ───────────────────────────────────────────
   STAT COUNTER ANIMATION
   ─────────────────────────────────────────── */
function initStatCounters() {
  const counters = document.querySelectorAll('.stat-number[data-count]');
  let animated = false;

  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting && !animated) {
          animated = true;
          counters.forEach(counter => animateCounter(counter));
        }
      });
    },
    { threshold: 0.3 }
  );

  counters.forEach(counter => observer.observe(counter));

  function animateCounter(el) {
    const target = parseInt(el.dataset.count);
    const duration = 2000;
    const startTime = performance.now();

    function easeOutExpo(t) {
      return t === 1 ? 1 : 1 - Math.pow(2, -10 * t);
    }

    function update(currentTime) {
      const elapsed = currentTime - startTime;
      const progress = Math.min(elapsed / duration, 1);
      const easedProgress = easeOutExpo(progress);
      const currentValue = Math.round(easedProgress * target);

      el.textContent = currentValue + '+';

      if (progress < 1) {
        requestAnimationFrame(update);
      }
    }

    requestAnimationFrame(update);
  }
}


/* ───────────────────────────────────────────
   BACK TO TOP
   ─────────────────────────────────────────── */
function initBackToTop() {
  const btn = document.getElementById('back-to-top');

  window.addEventListener('scroll', () => {
    btn.classList.toggle('visible', window.scrollY > 500);
  }, { passive: true });

  btn.addEventListener('click', () => {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });
}


/* ───────────────────────────────────────────
   SMOOTH SCROLL FOR ANCHOR LINKS
   ─────────────────────────────────────────── */
function initSmoothScroll() {
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const href = this.getAttribute('href');
      if (href === '#') return;

      const target = document.querySelector(href);
      if (target) {
        e.preventDefault();
        const offset = 72; // Header height
        const top = target.getBoundingClientRect().top + window.scrollY - offset;
        window.scrollTo({ top, behavior: 'smooth' });
      }
    });
  });
}

/* ───────────────────────────────────────────
   ACTIVE NAVIGATION HIGHLIGHT
   ─────────────────────────────────────────── */
function initActiveNav() {
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-link');
  let isClickScrolling = false;

  function updateActiveState() {
    if (isClickScrolling) return;

    let current = '';
    const scrollY = window.scrollY;

    sections.forEach(section => {
      const sectionTop = section.offsetTop - 120; // Offset for header
      const sectionHeight = section.offsetHeight;
      if (scrollY >= sectionTop && scrollY < sectionTop + sectionHeight) {
        current = section.getAttribute('id');
      }
    });

    navLinks.forEach(link => {
      link.classList.remove('active');
      if (current && link.getAttribute('href') === '#' + current) {
        link.classList.add('active');
      }
    });
  }

  window.addEventListener('scroll', updateActiveState, { passive: true });
  updateActiveState();

  navLinks.forEach(link => {
    link.addEventListener('click', () => {
      navLinks.forEach(l => l.classList.remove('active'));
      link.classList.add('active');

      isClickScrolling = true;
      setTimeout(() => {
        isClickScrolling = false;
      }, 1000);
    });
  });
}


/* ───────────────────────────────────────────
   SERVICE CARDS — Click-Triggered Entrance
   ─────────────────────────────────────────── */
function initServiceCardAnimations() {
  const servicesNavLink = document.querySelector('.nav-link[href="#services"]');
  const servicesSection = document.getElementById('services');
  if (!servicesNavLink || !servicesSection) return;

  const cards = servicesSection.querySelectorAll('.premium-card');
  if (cards.length === 0) return;

  const animClasses = ['anim-left', 'anim-center', 'anim-right'];

  function triggerAnimations() {
    cards.forEach((card, index) => {
      // Remove existing animation classes
      animClasses.forEach(cls => card.classList.remove(cls));
      card.style.removeProperty('--row-delay');
      card.style.removeProperty('--col-delay');

      // Force reflow so animation restarts
      void card.offsetWidth;

      // Determine column position (0, 1, 2) in a 3-column grid
      const col = index % 3;
      const row = Math.floor(index / 3);

      // Set row/col delay CSS variables for stagger
      const colDelay = col * 200; // 0ms, 200ms, 400ms
      const rowDelay = row * 350; // 0ms, 350ms, 700ms, ...
      card.style.setProperty('--row-delay', rowDelay + 'ms');
      card.style.setProperty('--col-delay', colDelay + 'ms');

      // Add the appropriate animation class
      if (col === 0) card.classList.add('anim-left');
      else if (col === 1) card.classList.add('anim-center');
      else card.classList.add('anim-right');
    });
  }

  servicesNavLink.addEventListener('click', (e) => {
    e.preventDefault();

    // Smooth scroll to services section
    const offset = 72; // Header height
    const top = servicesSection.getBoundingClientRect().top + window.scrollY - offset;
    window.scrollTo({ top, behavior: 'smooth' });

    // Trigger animations after a small delay so scroll starts first
    setTimeout(triggerAnimations, 300);
  });
}

/* ───────────────────────────────────────────
   CONTACT FORM — Fall-In Animation
   ─────────────────────────────────────────── */
function initContactFormAnimation() {
  const contactSection = document.getElementById('contact');
  const fieldGroups = document.querySelectorAll('.contact-field-group');

  if (!contactSection || fieldGroups.length === 0) return;

  // Add a class so CSS knows JS is ready and hides the fields initially (progressive enhancement)
  contactSection.classList.add('js-contact-anim-ready');

  const observer = new IntersectionObserver((entries, obs) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        fieldGroups.forEach(group => group.classList.add('drop-in'));
        obs.unobserve(entry.target); // Play once
      }
    });
  }, { threshold: 0.25 });

  observer.observe(contactSection);
}
