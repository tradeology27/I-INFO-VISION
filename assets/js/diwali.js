/**
 * I INFO VISION — Festive Diwali Engine & 6 Interactive Features
 * 
 * Features Included:
 *  1. 🚀 Rocket "Back-to-Top" Blastoff Transition
 *  2. 🪔 "Light a Diya" Interactive Hero Widget & Secret Bonus Reveal
 *  3. ✨ Sparkler Shimmer Card Borders (CSS)
 *  4. 🏵️ Hanging Marigold & Mango Leaf Toran Garland
 *  5. 🌀 Rotating Geometric Rangoli Watermark
 *  6. 🎆 Scroll-triggered Fountain (பூந்தொட்டி) & Ground Chakkar (தரைச்சக்கரம்)
 *  + Continuous Auto Crackers Loop & Responsive Header Offset
 */

(function () {
  'use strict';

  const BANNER_DISMISS_KEY = 'iinfo_diwali_banner_dismissed';
  const DIYA_LIT_KEY = 'iinfo_diwali_diya_lit';

  // ── DIWALI FESTIVE WEB AUDIO SYNTHESIZER (DEFAULT: ON) ──
  let diwaliAudioCtx = null;
  let isDiwaliSoundEnabled = true; // DEFAULT: SOUND ON!

  function getDiwaliAudio() {
    try {
      if (!diwaliAudioCtx) {
        const AudioClass = window.AudioContext || window.webkitAudioContext;
        if (AudioClass) {
          diwaliAudioCtx = new AudioClass();
        }
      }
      if (diwaliAudioCtx && diwaliAudioCtx.state === 'suspended') {
        diwaliAudioCtx.resume().catch(() => {});
      }
    } catch (e) {
      console.warn('AudioContext not supported', e);
    }
    return diwaliAudioCtx;
  }

  function unlockDiwaliAudio() {
    try {
      const ctx = getDiwaliAudio();
      if (ctx && ctx.state === 'suspended') {
        ctx.resume().catch(() => {});
      }
    } catch (e) {}
  }

  // Auto-unlock audio context on any user interaction (browser autoplay compliance)
  ['click', 'touchstart', 'touchend', 'keydown', 'scroll'].forEach(evt => {
    window.addEventListener(evt, unlockDiwaliAudio, { passive: true });
  });

  function createNoiseBuffer(ctx, duration) {
    const bufferSize = Math.floor(ctx.sampleRate * duration);
    const buffer = ctx.createBuffer(1, bufferSize, ctx.sampleRate);
    const data = buffer.getChannelData(0);
    for (let i = 0; i < bufferSize; i++) {
      data[i] = Math.random() * 2 - 1;
    }
    return buffer;
  }

  function playCrackerAudio(type) {
    if (!isDiwaliSoundEnabled) return;
    const ctx = getDiwaliAudio();
    if (!ctx) return;

    if (ctx.state === 'suspended') {
      ctx.resume().catch(() => {});
    }

    const now = ctx.currentTime;

    try {
      if (type === 'skyshot' || type === 'willow') {
        // Whistle ascent
        const whistleOsc = ctx.createOscillator();
        const whistleGain = ctx.createGain();
        whistleOsc.type = 'sine';
        whistleOsc.frequency.setValueAtTime(320, now);
        whistleOsc.frequency.exponentialRampToValueAtTime(1100, now + 0.18);
        whistleGain.gain.setValueAtTime(0.2, now);
        whistleGain.gain.exponentialRampToValueAtTime(0.01, now + 0.18);
        whistleOsc.connect(whistleGain);
        whistleGain.connect(ctx.destination);
        whistleOsc.start(now);
        whistleOsc.stop(now + 0.18);

        // Heavy Sub-Bass Boom
        const boomTime = now + 0.18;
        const boomOsc = ctx.createOscillator();
        const boomGain = ctx.createGain();
        boomOsc.type = 'triangle';
        boomOsc.frequency.setValueAtTime(160, boomTime);
        boomOsc.frequency.exponentialRampToValueAtTime(32, boomTime + 0.45);
        boomGain.gain.setValueAtTime(0.7, boomTime);
        boomGain.gain.exponentialRampToValueAtTime(0.001, boomTime + 0.45);
        boomOsc.connect(boomGain);
        boomGain.connect(ctx.destination);
        boomOsc.start(boomTime);
        boomOsc.stop(boomTime + 0.45);

        // Crackling noise burst
        const noise = ctx.createBufferSource();
        noise.buffer = createNoiseBuffer(ctx, 0.4);
        const filter = ctx.createBiquadFilter();
        filter.type = 'lowpass';
        filter.frequency.setValueAtTime(1400, boomTime);
        filter.frequency.exponentialRampToValueAtTime(400, boomTime + 0.4);
        const noiseGain = ctx.createGain();
        noiseGain.gain.setValueAtTime(0.45, boomTime);
        noiseGain.gain.exponentialRampToValueAtTime(0.001, boomTime + 0.4);
        noise.connect(filter);
        filter.connect(noiseGain);
        noiseGain.connect(ctx.destination);
        noise.start(boomTime);
        noise.stop(boomTime + 0.4);
      }
      else if (type === 'flowerpot' || type === 'sparkler') {
        const noise = ctx.createBufferSource();
        noise.buffer = createNoiseBuffer(ctx, 0.65);
        const filter = ctx.createBiquadFilter();
        filter.type = 'bandpass';
        filter.frequency.setValueAtTime(3200, now);
        filter.Q.setValueAtTime(1.8, now);
        const gain = ctx.createGain();
        gain.gain.setValueAtTime(0.35, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.65);
        noise.connect(filter);
        filter.connect(gain);
        gain.connect(ctx.destination);
        noise.start(now);
        noise.stop(now + 0.65);
      }
      else if (type === 'chakkar') {
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = 'sawtooth';
        osc.frequency.setValueAtTime(180, now);
        osc.frequency.linearRampToValueAtTime(420, now + 0.25);
        osc.frequency.linearRampToValueAtTime(160, now + 0.5);

        const filter = ctx.createBiquadFilter();
        filter.type = 'lowpass';
        filter.frequency.setValueAtTime(800, now);

        gain.gain.setValueAtTime(0.25, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.5);

        osc.connect(filter);
        filter.connect(gain);
        gain.connect(ctx.destination);
        osc.start(now);
        osc.stop(now + 0.5);
      }
      else if (type === 'saravedi') {
        for (let i = 0; i < 8; i++) {
          const t = now + i * 0.048;
          const popNoise = ctx.createBufferSource();
          popNoise.buffer = createNoiseBuffer(ctx, 0.035);
          const filter = ctx.createBiquadFilter();
          filter.type = 'bandpass';
          filter.frequency.setValueAtTime(2800 + (Math.random() - 0.5) * 800, t);
          filter.Q.setValueAtTime(2, t);
          const popGain = ctx.createGain();
          popGain.gain.setValueAtTime(0.4, t);
          popGain.gain.exponentialRampToValueAtTime(0.001, t + 0.035);
          popNoise.connect(filter);
          filter.connect(popGain);
          popGain.connect(ctx.destination);
          popNoise.start(t);
          popNoise.stop(t + 0.035);
        }
      }
      else if (type === 'peacock') {
        const noise = ctx.createBufferSource();
        noise.buffer = createNoiseBuffer(ctx, 0.45);
        const filter = ctx.createBiquadFilter();
        filter.type = 'bandpass';
        filter.frequency.setValueAtTime(2400, now);
        const gain = ctx.createGain();
        gain.gain.setValueAtTime(0.3, now);
        gain.gain.exponentialRampToValueAtTime(0.001, now + 0.45);
        noise.connect(filter);
        filter.connect(gain);
        gain.connect(ctx.destination);
        noise.start(now);
        noise.stop(now + 0.45);
      }
    } catch (e) {
      console.warn('Audio play error', e);
    }
  }

  window.playDiwaliCrackerSound = playCrackerAudio;


  // 1. ALWAYS-ON DIWALI MODE & BANNER OFFSET
  function initDiwaliBannerAndHeader() {
    document.body.classList.add('diwali-mode');
    document.body.classList.remove('diwali-midnight');
    try { localStorage.removeItem('iinfo_diwali_midnight'); } catch(e) {}

    const banner = document.getElementById('diwali-top-banner');
    if (!banner) return;

    if (sessionStorage.getItem(BANNER_DISMISS_KEY) === 'true') {
      banner.style.display = 'none';
      document.body.classList.remove('has-diwali-banner');
      return;
    }

    document.body.classList.add('has-diwali-banner');
    function updateBannerHeight() {
      if (banner && banner.style.display !== 'none') {
        const h = banner.offsetHeight || 42;
        document.documentElement.style.setProperty('--diwali-banner-h', h + 'px');
      }
    }

    updateBannerHeight();
    window.addEventListener('resize', updateBannerHeight, { passive: true });

    const closeBtn = banner.querySelector('.diwali-close-btn');
    if (closeBtn) {
      closeBtn.addEventListener('click', () => {
        banner.style.opacity = '0';
        banner.style.transform = 'translateY(-100%)';
        document.body.classList.remove('has-diwali-banner');
        setTimeout(() => {
          banner.style.display = 'none';
          sessionStorage.setItem(BANNER_DISMISS_KEY, 'true');
        }, 320);
      });
    }
  }

  // 2. FEATURE 4: HANGING MARIGOLD & MANGO LEAF TORAN
  function initHangingToran() {
    const header = document.querySelector('.site-header');
    if (header && !header.querySelector('.diwali-toran')) {
      const toran = document.createElement('div');
      toran.className = 'diwali-toran';
      toran.setAttribute('aria-hidden', 'true');
      header.appendChild(toran);
    }
  }

  // 3. FEATURE 5: ROTATING GEOMETRIC RANGOLI WATERMARK
  function initRangoliWatermark() {
    const hero = document.querySelector('.hero');
    if (hero && !hero.querySelector('.diwali-rangoli-bg')) {
      const rangoli = document.createElement('div');
      rangoli.className = 'diwali-rangoli-bg';
      rangoli.setAttribute('aria-hidden', 'true');
      rangoli.innerHTML = `
        <svg viewBox="0 0 200 200" fill="none" xmlns="http://www.w3.org/2000/svg" style="width: 100%; height: 100%;">
          <circle cx="100" cy="100" r="95" stroke="#fbbf24" stroke-width="1.2" stroke-dasharray="4 4"/>
          <circle cx="100" cy="100" r="75" stroke="#f59e0b" stroke-width="1.5"/>
          <circle cx="100" cy="100" r="50" stroke="#ffd700" stroke-width="1.2"/>
          <circle cx="100" cy="100" r="25" stroke="#ea580c" stroke-width="1"/>
          <!-- 8-fold Symmetry Petals -->
          <g stroke="#fbbf24" stroke-width="1.2">
            <path d="M100 25 C115 55 115 75 100 100 C85 75 85 55 100 25 Z"/>
            <path d="M100 175 C115 145 115 125 100 100 C85 125 85 145 100 175 Z"/>
            <path d="M25 100 C55 115 75 115 100 100 C75 85 55 85 25 100 Z"/>
            <path d="M175 100 C145 115 125 115 100 100 C125 85 145 85 175 100 Z"/>
            <path d="M47 47 C72 68 86 82 100 100 C82 86 68 72 47 47 Z"/>
            <path d="M153 153 C128 132 114 118 100 100 C118 114 132 128 153 153 Z"/>
            <path d="M153 47 C132 72 118 86 100 100 C114 82 128 68 153 47 Z"/>
            <path d="M47 153 C68 128 82 114 100 100 C86 118 72 132 47 153 Z"/>
          </g>
          <!-- Center Lotus Motif -->
          <polygon points="100,85 105,95 115,100 105,105 100,115 95,105 85,100 95,95" fill="#f59e0b" opacity="0.4"/>
        </svg>
      `;
      hero.appendChild(rangoli);
    }
  }

  // 4. FEATURE 1: 🚀 ROCKET "BACK-TO-TOP" TRANSITION
  function initRocketBackToTop() {
    const btn = document.getElementById('back-to-top');
    if (!btn) return;

    btn.title = "Diwali Rocket: Launch to Top!";

    btn.addEventListener('click', (e) => {
      e.preventDefault();
      if (btn.classList.contains('launching')) return;

      btn.classList.add('launching');

      // Spawn fiery rocket exhaust engine sparks on canvas
      const rect = btn.getBoundingClientRect();
      const originX = rect.left + rect.width / 2;
      const originY = rect.top + rect.height;

      if (window.triggerRocketEngineSparks) {
        window.triggerRocketEngineSparks(originX, originY);
      }

      // Smooth scroll to top
      window.scrollTo({ top: 0, behavior: 'smooth' });

      // Reset rocket after arrival
      setTimeout(() => {
        btn.classList.remove('launching');
      }, 950);
    });
  }

  // 5. FEATURE 2: 🪔 "LIGHT A DIYA" INTERACTIVE WIDGET & SECRET BONUS
  function initLightADiya() {
    // Look for existing widget or mount one in hero slide actions
    let btn = document.getElementById('diwali-interactive-diya');
    const heroActions = document.querySelector('.hero .carousel-slide.active .slide-actions, .hero .slide-actions');

    if (!btn && heroActions) {
      const wrap = document.createElement('div');
      wrap.className = 'diwali-light-diya-wrap';
      wrap.innerHTML = `
        <button class="diwali-diya-interactive-btn" id="diwali-interactive-diya" aria-label="Light a Diya for Diwali Luck">
          <span class="diya-flame-icon">🪔</span>
          <span id="diya-btn-text">Light a Diya for Secret Perk ✨</span>
        </button>
      `;
      heroActions.parentNode.insertBefore(wrap, heroActions.nextSibling);
      btn = document.getElementById('diwali-interactive-diya');
    }

    if (!btn) return;

    // Secret Bonus Toast
    let toast = document.getElementById('diwali-secret-bonus-toast');
    if (!toast) {
      toast = document.createElement('div');
      toast.id = 'diwali-secret-bonus-toast';
      toast.className = 'diwali-secret-bonus-toast';
      toast.setAttribute('aria-hidden', 'true');
      toast.innerHTML = `
        <div class="bonus-toast-inner">
          <button class="bonus-toast-close" id="bonus-toast-close-btn" aria-label="Close">&times;</button>
          <div class="bonus-toast-icon">🪔</div>
          <div class="bonus-toast-content">
            <span class="bonus-toast-badge">Secret Diwali Blessing Unlocked!</span>
            <h4>Extra ₹2,000 OFF on Any Project</h4>
            <p>You lit the sacred Diwali Diya! Use special bonus code: <strong style="color: #fbbf24; letter-spacing: 1px;">DIYA2026</strong></p>
            <div class="bonus-toast-actions">
              <a href="https://wa.me/919894480585?text=Hello%20I%20Info%20Vision,%20I%20lit%20the%20Diwali%20Diya%20and%20unlocked%20Secret%20Bonus%20Code%20DIYA2026%20for%20extra%20Rs.2000%20OFF!" target="_blank" rel="noopener noreferrer" class="bonus-toast-wa">
                <i class="ph ph-whatsapp-logo" style="font-size: 16px;"></i> Claim ₹2,000 Discount via WhatsApp
              </a>
            </div>
          </div>
        </div>
      `;
      document.body.appendChild(toast);

      const closeToastBtn = document.getElementById('bonus-toast-close-btn');
      if (closeToastBtn) {
        closeToastBtn.addEventListener('click', () => {
          toast.classList.remove('show');
        });
      }
    }

    btn.addEventListener('click', (e) => {
      e.preventDefault();
      btn.classList.add('lit');
      const textEl = document.getElementById('diya-btn-text');
      if (textEl) textEl.innerHTML = 'Diya Radiant &amp; Blessed 🔥';

      // Celebratory sparks at diya
      const rect = btn.getBoundingClientRect();
      if (window.triggerDiwaliCracker) {
        window.triggerDiwaliCracker(rect.left + rect.width / 2, rect.top);
      }

      // Show secret reward toast
      if (toast) {
        setTimeout(() => {
          toast.classList.add('show');
        }, 500);
      }
    });
  }

    // 6. MAIN MULTI-CRACKER FIREWORKS ENGINE (7 AUTHENTIC CRACKER TYPES)
  function initFireworksEngine() {
    if (window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;

    let canvas = document.getElementById('diwali-fireworks-canvas');
    if (!canvas) {
      canvas = document.createElement('canvas');
      canvas.id = 'diwali-fireworks-canvas';
      document.body.appendChild(canvas);
    }

    const ctx = canvas.getContext('2d');
    let width = (canvas.width = window.innerWidth);
    let height = (canvas.height = window.innerHeight);

    window.addEventListener('resize', () => {
      width = canvas.width = window.innerWidth;
      height = canvas.height = window.innerHeight;
    }, { passive: true });

    const rockets = [];
    const particles = [];

    const COLOR_PALETTES = [
      ['#ffd700', '#fbbf24', '#f59e0b', '#ffffff'],
      ['#ff3b30', '#ff9500', '#ffd700', '#ffffff'],
      ['#00e5ff', '#3b82f6', '#93c5fd', '#ffffff'],
      ['#a855f7', '#ec4899', '#f43f5e', '#ffffff'],
      ['#10b981', '#34d399', '#fde047', '#ffffff'],
    ];

    class Particle {
      constructor(x, y, palette, opts = {}) {
        this.x = x;
        this.y = y;
        const angle = opts.angle !== undefined ? opts.angle : (Math.random() * Math.PI * 2);
        const speed = opts.speed !== undefined ? opts.speed : (Math.random() * 4.5 + 1.2);
        this.vx = Math.cos(angle) * speed + (opts.vxOffset || 0);
        this.vy = Math.sin(angle) * speed + (opts.vyOffset || 0);
        this.color = opts.color || (palette ? palette[Math.floor(Math.random() * palette.length)] : '#ffd700');
        this.alpha = 1;
        this.decay = opts.decay || (Math.random() * 0.022 + 0.012);
        this.size = opts.size || (Math.random() * 2.8 + 1.2);
        this.gravity = opts.gravity !== undefined ? opts.gravity : 0.08;
        this.drag = opts.drag !== undefined ? opts.drag : 0.96;
        this.flicker = opts.flicker !== undefined ? opts.flicker : Math.random() > 0.4;
        this.jitter = opts.jitter || 0;
        this.hasTrail = !!opts.hasTrail;
        this.trail = this.hasTrail ? [] : null;
        this.isSmoke = !!opts.isSmoke;
      }

      update() {
        if (this.hasTrail) {
          this.trail.push({ x: this.x, y: this.y, alpha: this.alpha });
          if (this.trail.length > 6) this.trail.shift();
        }
        if (this.jitter) {
          this.vx += (Math.random() - 0.5) * this.jitter;
          this.vy += (Math.random() - 0.5) * this.jitter;
        }
        this.x += this.vx;
        this.y += this.vy;
        this.vy += this.gravity;
        this.vx *= this.drag;
        this.vy *= this.drag;
        this.alpha -= this.decay;
      }

      draw() {
        if (this.alpha <= 0) return;
        ctx.save();
        let currentAlpha = this.alpha;
        if (this.flicker && Math.random() > 0.45) currentAlpha *= 0.6;
        ctx.globalAlpha = Math.max(0, currentAlpha);

        if (this.hasTrail && this.trail.length > 1) {
          ctx.beginPath();
          ctx.moveTo(this.trail[0].x, this.trail[0].y);
          for (let i = 1; i < this.trail.length; i++) {
            ctx.lineTo(this.trail[i].x, this.trail[i].y);
          }
          ctx.strokeStyle = this.color;
          ctx.lineWidth = Math.max(1, this.size * 0.7);
          ctx.shadowBlur = 6;
          ctx.shadowColor = this.color;
          ctx.stroke();
        }

        ctx.fillStyle = this.color;
        if (!this.isSmoke) {
          ctx.shadowBlur = 8;
          ctx.shadowColor = this.color;
        }
        ctx.beginPath();
        ctx.arc(this.x, this.y, this.size, 0, Math.PI * 2);
        ctx.fill();
        ctx.restore();
      }
    }

    class Rocket {
      constructor(targetX, targetY, opts = {}) {
        this.x = targetX || (Math.random() * (width - 160) + 80);
        this.y = height + 10;
        this.targetY = targetY || (Math.random() * (height * 0.38) + height * 0.12);
        this.speed = Math.random() * 4 + 7.5;
        this.angle = -Math.PI / 2 + (Math.random() - 0.5) * 0.18;
        this.vx = Math.cos(this.angle) * this.speed;
        this.vy = Math.sin(this.angle) * this.speed;
        this.palette = opts.palette || COLOR_PALETTES[Math.floor(Math.random() * COLOR_PALETTES.length)];
        this.doubleBreak = !!opts.doubleBreak;
        this.isWillow = !!opts.isWillow;
        this.trail = [];
        this.dead = false;
      }

      update() {
        this.trail.push({ x: this.x, y: this.y });
        if (this.trail.length > 6) this.trail.shift();

        this.x += this.vx;
        this.y += this.vy;
        this.vy += 0.05;

        if (this.y <= this.targetY || this.vy >= 0) {
          this.explode();
          this.dead = true;
        }
      }

      explode() {
        if (this.isWillow) {
          // Kamuro Willow Golden Cascade
          const count = 55;
          const willowColors = ['#ffd700', '#fbbf24', '#fef08a', '#ffffff'];
          for (let i = 0; i < count; i++) {
            particles.push(new Particle(this.x, this.y, willowColors, {
              speed: Math.random() * 4.2 + 1,
              drag: 0.985,
              gravity: 0.045,
              decay: Math.random() * 0.008 + 0.005,
              hasTrail: true,
              size: Math.random() * 2.2 + 1.2,
              flicker: true
            }));
          }
          return;
        }

        // Primary outer burst
        const count = this.doubleBreak ? 42 : Math.floor(Math.random() * 25 + 35);
        for (let i = 0; i < count; i++) {
          particles.push(new Particle(this.x, this.y, this.palette));
        }

        // Secondary inner break
        if (this.doubleBreak) {
          setTimeout(() => {
            if (document.hidden) return;
            const corePalette = ['#ffffff', '#ffd700', '#f59e0b'];
            for (let j = 0; j < 30; j++) {
              particles.push(new Particle(this.x, this.y, corePalette, {
                speed: Math.random() * 5.5 + 2,
                decay: 0.02,
                size: Math.random() * 2.5 + 1.2
              }));
            }
          }, 140);
        }
      }

      draw() {
        ctx.save();
        for (let i = 0; i < this.trail.length; i++) {
          const pt = this.trail[i];
          ctx.beginPath();
          ctx.arc(pt.x, pt.y, 2, 0, Math.PI * 2);
          ctx.fillStyle = `rgba(251, 191, 36, ${(i + 1) / this.trail.length})`;
          ctx.shadowBlur = 8;
          ctx.shadowColor = '#fbbf24';
          ctx.fill();
        }
        ctx.beginPath();
        ctx.arc(this.x, this.y, 2.5, 0, Math.PI * 2);
        ctx.fillStyle = '#ffffff';
        ctx.shadowBlur = 12;
        ctx.shadowColor = '#ffd700';
        ctx.fill();
        ctx.restore();
      }
    }

    // ── 7 AUTHENTIC DIWALI CRACKER GENERATORS (VISIBLE SCREEN POSITIONS) ──

    // 1. Double-Break Sky Shot (வானவெடி)
    window.triggerSkyShot = function (targetX, targetY) {
      playCrackerAudio('skyshot');
      const destX = targetX !== undefined ? targetX : (Math.random() * (width - 240) + 120);
      const destY = targetY !== undefined ? targetY : (Math.random() * (height * 0.25) + height * 0.12);
      rockets.push(new Rocket(destX, destY, { doubleBreak: true }));
    };

    // 2. Mega Flower Pot / Anar (பூந்தொட்டி)
    window.triggerFlowerPot = function (originX, originY) {
      playCrackerAudio('flowerpot');
      const ox = originX !== undefined ? originX : (Math.random() * (width - 200) + 100);
      const oy = originY !== undefined ? originY : (height * 0.78);
      const goldPalette = ['#ffd700', '#fbbf24', '#f59e0b', '#ffffff', '#fed7aa'];
      for (let i = 0; i < 80; i++) {
        setTimeout(() => {
          if (document.hidden) return;
          const angle = -Math.PI / 2 + (Math.random() - 0.5) * 0.55;
          particles.push(new Particle(ox, oy, goldPalette, {
            angle: angle,
            speed: Math.random() * 9 + 6,
            gravity: 0.22,
            drag: 0.98,
            decay: Math.random() * 0.02 + 0.015,
            size: Math.random() * 3.2 + 1.5,
            flicker: true
          }));
        }, i * 14);
      }
    };
    window.triggerDiwaliFountain = window.triggerFlowerPot;

    // 3. Ground Spinning Chakkar (தரைச்சக்கரம்)
    window.triggerChakkar = function (centerX, centerY) {
      playCrackerAudio('chakkar');
      const cx = centerX !== undefined ? centerX : (Math.random() * (width - 200) + 100);
      const cy = centerY !== undefined ? centerY : (height * 0.74);
      for (let i = 0; i < 90; i++) {
        setTimeout(() => {
          if (document.hidden) return;
          const angle = (i * 0.42) % (Math.PI * 2);
          let color = '#ffd700';
          if (i >= 30 && i < 60) color = '#00e5ff';
          else if (i >= 60) color = '#ef4444';

          particles.push(new Particle(cx, cy, null, {
            color: color,
            angle: angle,
            speed: Math.random() * 5.5 + 3.2,
            gravity: 0.03,
            drag: 0.96,
            decay: 0.024,
            size: Math.random() * 2.8 + 1.2,
            flicker: true
          }));
        }, i * 16);
      }
    };
    window.triggerDiwaliChakkar = window.triggerChakkar;

    // 4. Twinkling Hand Sparklers (கம்பி மத்தாப்பூ)
    window.triggerSparklers = function (centerX, centerY) {
      const cx = centerX !== undefined ? centerX : (Math.random() * (width - 240) + 120);
      const cy = centerY !== undefined ? centerY : (height * 0.48);
      const palette = ['#ffffff', '#fef08a', '#ffd700', '#fbbf24'];
      for (let i = 0; i < 75; i++) {
        setTimeout(() => {
          if (document.hidden) return;
          const branchAngle = Math.floor(Math.random() * 6) * (Math.PI / 3) + (Math.random() - 0.5) * 0.4;
          particles.push(new Particle(cx, cy, palette, {
            angle: branchAngle,
            speed: Math.random() * 4.5 + 1.5,
            gravity: 0.06,
            drag: 0.94,
            decay: Math.random() * 0.02 + 0.012,
            size: Math.random() * 2.6 + 1.2,
            jitter: 0.35,
            flicker: true
          }));
        }, i * 10);
      }
    };

    // 5. 100-Wala Garland Saravedi (சரவெடி)
    window.triggerSaravedi = function (startX, startY) {
      playCrackerAudio('saravedi');
      const sx = startX !== undefined ? startX : (Math.random() * (width - 260) + 130);
      const sy = startY !== undefined ? startY : (height * 0.22);
      const popCount = 20;
      for (let i = 0; i < popCount; i++) {
        setTimeout(() => {
          if (document.hidden) return;
          const curX = sx + Math.sin(i * 0.7) * 22;
          const curY = sy + i * 16;
          // Mini flash
          particles.push(new Particle(curX, curY, null, {
            color: '#ffffff',
            speed: 0.1,
            size: 8,
            decay: 0.25,
            gravity: 0
          }));
          // Spark bursts
          const popColors = ['#ef4444', '#f97316', '#ffd700', '#ffffff'];
          for (let s = 0; s < 14; s++) {
            particles.push(new Particle(curX, curY, popColors, {
              speed: Math.random() * 4.2 + 1.5,
              gravity: 0.12,
              decay: 0.045,
              size: Math.random() * 2.2 + 1
            }));
          }
          // Smoke puff
          if (i % 2 === 0) {
            particles.push(new Particle(curX, curY, null, {
              color: 'rgba(200, 200, 200, 0.45)',
              speed: Math.random() * 0.8 + 0.3,
              gravity: -0.04,
              drag: 0.92,
              decay: 0.018,
              size: Math.random() * 6 + 4,
              isSmoke: true
            }));
          }
        }, i * 65);
      }
    };

    // 6. Peacock Feather Fan (மயில் தோகை)
    window.triggerPeacockFan = function (originX, originY) {
      playCrackerAudio('peacock');
      const ox = originX !== undefined ? originX : (width * 0.5);
      const oy = originY !== undefined ? originY : (height * 0.76);
      const peacockStreams = [
        { angle: -Math.PI / 2 - 0.55, color: '#00e5ff' },
        { angle: -Math.PI / 2 - 0.38, color: '#10b981' },
        { angle: -Math.PI / 2 - 0.18, color: '#a3e635' },
        { angle: -Math.PI / 2,        color: '#ffd700' },
        { angle: -Math.PI / 2 + 0.18, color: '#a3e635' },
        { angle: -Math.PI / 2 + 0.38, color: '#10b981' },
        { angle: -Math.PI / 2 + 0.55, color: '#a855f7' }
      ];
      for (let wave = 0; wave < 3; wave++) {
        setTimeout(() => {
          peacockStreams.forEach(stream => {
            for (let p = 0; p < 4; p++) {
              const spread = (Math.random() - 0.5) * 0.08;
              particles.push(new Particle(ox, oy, null, {
                color: stream.color,
                angle: stream.angle + spread,
                speed: Math.random() * 8 + 6,
                gravity: 0.16,
                decay: 0.022,
                size: Math.random() * 3 + 1.5,
                flicker: true
              }));
            }
          });
        }, wave * 140);
      }
    };

    // 7. Kamuro Golden Willow Shower (தங்க அருவி)
    window.triggerKamuroWillow = function (targetX, targetY) {
      playCrackerAudio('willow');
      const destX = targetX !== undefined ? targetX : (Math.random() * (width - 240) + 120);
      const destY = targetY !== undefined ? targetY : (Math.random() * (height * 0.22) + height * 0.12);
      rockets.push(new Rocket(destX, destY, { isWillow: true }));
    };

    // Unified Master Cracker Trigger
    window.triggerDiwaliCracker = function (x, y, type) {
      if (type === 'skyshot') return window.triggerSkyShot(x, y);
      if (type === 'flowerpot' || type === 'anar') return window.triggerFlowerPot(x, y);
      if (type === 'chakkar') return window.triggerChakkar(x, y);
      if (type === 'sparkler') return window.triggerSparklers(x, y);
      if (type === 'saravedi') return window.triggerSaravedi(x, y);
      if (type === 'peacock') return window.triggerPeacockFan(x, y);
      if (type === 'willow') return window.triggerKamuroWillow(x, y);

      // Intelligent random selector based on click position
      const isTopHalf = y < height * 0.5;
      if (isTopHalf) {
        const r = Math.random();
        if (r < 0.45) window.triggerSkyShot(x, y);
        else if (r < 0.75) window.triggerKamuroWillow(x, y);
        else window.triggerPeacockFan(x, height * 0.76);
      } else {
        const r = Math.random();
        if (r < 0.3) window.triggerFlowerPot(x, y);
        else if (r < 0.6) window.triggerChakkar(x, y);
        else if (r < 0.82) window.triggerSparklers(x, y);
        else window.triggerSaravedi(x, y - 60);
      }
    };

    // Rocket Exhaust sparks for Feature 1 (Rocket Back to Top)
    window.triggerRocketEngineSparks = function (x, y) {
      const palette = ['#ffd700', '#f59e0b', '#ea580c', '#ffffff'];
      for (let i = 0; i < 35; i++) {
        const angle = Math.PI / 2 + (Math.random() - 0.5) * 0.8;
        particles.push(new Particle(x, y, palette, {
          angle: angle,
          speed: Math.random() * 6 + 3,
          gravity: 0.15,
          decay: 0.035,
          size: Math.random() * 3 + 2
        }));
      }
    };

    
    // Feature: ✨ Magical Sparkler Cursor Trail (Desktop fine pointer only)
    if (window.matchMedia && window.matchMedia('(pointer: fine)').matches) {
      let lastSparkTime = 0;
      window.addEventListener('pointermove', (e) => {
        const now = performance.now();
        if (now - lastSparkTime < 32) return;
        lastSparkTime = now;

        if (e.target.closest('input, textarea, select')) return;

        const goldColors = ['#ffd700', '#fde047', '#fbbf24', '#ffffff', '#f59e0b'];
        for (let i = 0; i < 2; i++) {
          const angle = Math.random() * Math.PI * 2;
          const speed = Math.random() * 1.6 + 0.4;
          particles.push(new Particle(e.clientX, e.clientY, goldColors, {
            angle: angle,
            speed: speed,
            gravity: 0.08,
            drag: 0.95,
            decay: 0.045,
            size: Math.random() * 2.2 + 0.8,
            flicker: true
          }));
        }
      }, { passive: true });
    }

    // Click anywhere on empty space to burst crackers
    window.addEventListener('click', (e) => {
      if (e.target.closest('a, button, input, textarea, select, .diwali-modal-content')) return;
      window.triggerDiwaliCracker(e.clientX, e.clientY);
    });

    // ── ANIMATION LOOP (CAP TO SMOOTH 60 FPS) ──
    let isRunning = true;
    function animate() {
      if (!isRunning) return;

      ctx.clearRect(0, 0, width, height);

      for (let i = rockets.length - 1; i >= 0; i--) {
        const r = rockets[i];
        r.update();
        r.draw();
        if (r.dead) rockets.splice(i, 1);
      }

      // Cap max particles to prevent any device lag
      if (particles.length > 400) {
        particles.splice(0, particles.length - 400);
      }

      for (let i = particles.length - 1; i >= 0; i--) {
        const p = particles[i];
        p.update();
        p.draw();
        if (p.alpha <= 0) particles.splice(i, 1);
      }

      requestAnimationFrame(animate);
    }
    animate();

    // ── CONTINUOUS AUTO MULTI-CRACKERS LOOP (CHOREOGRAPHED ROTATION OF ALL 7 TYPES) ──
    const AUTO_CRACKER_SEQUENCE = [
      { id: 'skyshot', name: '🚀 Sky Shot', tamil: 'வானவெடி' },
      { id: 'flowerpot', name: '🪔 Flower Pot', tamil: 'பூந்தொட்டி' },
      { id: 'chakkar', name: '🌀 Chakkar', tamil: 'தரைச்சக்கரம்' },
      { id: 'sparkler', name: '✨ Sparklers', tamil: 'மத்தாப்பூ' },
      { id: 'saravedi', name: '🧨 Saravedi', tamil: 'சரவெடி' },
      { id: 'peacock', name: '🦚 Peacock Fan', tamil: 'மயில் தோகை' },
      { id: 'willow', name: '👑 Willow Rain', tamil: 'தங்க அருவி' }
    ];

    let autoSequenceStep = 0;
    let autoLaunchTimer = null;

    function fireNextAutoCracker() {
      if (document.hidden) return;

      const cracker = AUTO_CRACKER_SEQUENCE[autoSequenceStep % AUTO_CRACKER_SEQUENCE.length];
      autoSequenceStep++;

      // Alternating responsive screen positions
      const leftX = width * (0.16 + Math.random() * 0.12);
      const rightX = width * (0.72 + Math.random() * 0.12);
      const midX = width * (0.42 + Math.random() * 0.16);
      const isLeft = autoSequenceStep % 2 === 0;
      const targetSideX = isLeft ? leftX : rightX;

      switch (cracker.id) {
        case 'skyshot':
          window.triggerSkyShot(targetSideX, height * (0.18 + Math.random() * 0.12));
          break;
        case 'flowerpot':
          window.triggerFlowerPot(targetSideX, height * 0.78);
          break;
        case 'chakkar':
          window.triggerChakkar(isLeft ? rightX : leftX, height * 0.74);
          break;
        case 'sparkler':
          window.triggerSparklers(midX, height * (0.42 + Math.random() * 0.12));
          break;
        case 'saravedi':
          window.triggerSaravedi(isLeft ? leftX : rightX, height * 0.22);
          break;
        case 'peacock':
          window.triggerPeacockFan(midX, height * 0.76);
          break;
        case 'willow':
          window.triggerKamuroWillow(midX, height * 0.16);
          break;
      }



      // Grand Double Celebration after completing full 7-cracker round
      if (autoSequenceStep % 7 === 0) {
        setTimeout(() => {
          if (!document.hidden) {
            window.triggerFlowerPot(leftX, height * 0.8);
            window.triggerChakkar(rightX, height * 0.75);
          }
        }, 900);
      }
    }

    function scheduleNextLaunch() {
      // Elegant 2.2s to 2.8s timing between cracker types
      const interval = Math.random() * 600 + 2200;
      autoLaunchTimer = setTimeout(() => {
        fireNextAutoCracker();
        scheduleNextLaunch();
      }, interval);
    }

    // Festive welcome salvo on initial load
    setTimeout(() => {
      window.triggerSkyShot(width * 0.25, height * 0.22);
      setTimeout(() => window.triggerKamuroWillow(width * 0.75, height * 0.20), 400);
      setTimeout(() => window.triggerFlowerPot(width * 0.5, height * 0.78), 800);
    }, 600);

    scheduleNextLaunch();

    document.addEventListener('visibilitychange', () => {
      if (document.hidden) {
        isRunning = false;
        clearTimeout(autoLaunchTimer);
      } else {
        isRunning = true;
        animate();
        scheduleNextLaunch();
      }
    });
  }

    // 7. FEATURE 6: SCROLL-TRIGGERED FOUNTAIN & CHAKKAR DETECTOR
  function initScrollFountains() {
    if (!('IntersectionObserver' in window)) return;

    const targetSections = document.querySelectorAll('.stats-bar, #featured-projects, .cta-banner');
    if (!targetSections.length) return;

    let firedSections = new Set();

    const observer = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting && !firedSections.has(entry.target)) {
          firedSections.add(entry.target);

          const rect = entry.target.getBoundingClientRect();
          const groundY = Math.min(window.innerHeight * 0.85, rect.top + rect.height * 0.7);

          // Trigger twin fountains on left and right
          if (window.triggerDiwaliFountain) {
            window.triggerDiwaliFountain(Math.max(40, window.innerWidth * 0.15), groundY);
            window.triggerDiwaliFountain(Math.min(window.innerWidth - 40, window.innerWidth * 0.85), groundY);
          }

          // Trigger spinning chakkar in the center
          if (window.triggerDiwaliChakkar) {
            setTimeout(() => {
              window.triggerDiwaliChakkar(window.innerWidth * 0.5, groundY);
            }, 300);
          }
        }
      });
    }, { threshold: 0.25 });

    targetSections.forEach(sec => observer.observe(sec));
  }

  // 8. COUNTDOWN TIMER
  function initCountdown() {
    const daysEl = document.getElementById('diwali-days');
    const hoursEl = document.getElementById('diwali-hours');
    const minsEl = document.getElementById('diwali-mins');
    const secsEl = document.getElementById('diwali-secs');

    if (!daysEl || !hoursEl || !minsEl || !secsEl) return;

    const now = new Date();
    const targetDate = new Date(now.getFullYear(), 10, 15, 23, 59, 59);
    if (targetDate.getTime() <= now.getTime()) {
      targetDate.setDate(now.getDate() + 7);
    }

    function update() {
      const current = new Date().getTime();
      const diff = targetDate.getTime() - current;

      if (diff <= 0) {
        daysEl.textContent = '00';
        hoursEl.textContent = '00';
        minsEl.textContent = '00';
        secsEl.textContent = '00';
        return;
      }

      const d = Math.floor(diff / (1000 * 60 * 60 * 24));
      const h = Math.floor((diff % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
      const m = Math.floor((diff % (1000 * 60 * 60)) / (1000 * 60));
      const s = Math.floor((diff % (1000 * 60)) / 1000);

      daysEl.textContent = String(d).padStart(2, '0');
      hoursEl.textContent = String(h).padStart(2, '0');
      minsEl.textContent = String(m).padStart(2, '0');
      secsEl.textContent = String(s).padStart(2, '0');
    }

    update();
    setInterval(update, 1000);
  }

  // 9. OFFER MODAL LOGIC
  function initOfferModal() {
    const modal = document.getElementById('diwali-modal-backdrop');
    if (!modal) return;

    const openBtns = document.querySelectorAll('[data-diwali-modal-open]');
    const closeBtns = modal.querySelectorAll('.diwali-modal-close, [data-diwali-modal-close]');

    function openModal() {
      modal.classList.add('open');
      modal.setAttribute('aria-hidden', 'false');
      document.body.style.overflow = 'hidden';
      if (window.triggerDiwaliCracker) {
        window.triggerDiwaliCracker(window.innerWidth / 2, window.innerHeight * 0.35);
      }
    }

    function closeModal() {
      modal.classList.remove('open');
      modal.setAttribute('aria-hidden', 'true');
      document.body.style.overflow = '';
    }

    openBtns.forEach(btn => {
      btn.addEventListener('click', (e) => {
        e.preventDefault();
        openModal();
      });
    });

    closeBtns.forEach(btn => btn.addEventListener('click', closeModal));

    modal.addEventListener('click', (e) => {
      if (e.target === modal) closeModal();
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && modal.classList.contains('open')) {
        closeModal();
      }
    });

    const copyBtn = document.getElementById('diwali-copy-btn');
    const codeEl = document.getElementById('diwali-promo-code');
    if (copyBtn && codeEl) {
      copyBtn.addEventListener('click', async () => {
        const textToCopy = codeEl.textContent.trim();
        try {
          if (navigator.clipboard && navigator.clipboard.writeText) {
            await navigator.clipboard.writeText(textToCopy);
          } else {
            const temp = document.createElement('textarea');
            temp.value = textToCopy;
            document.body.appendChild(temp);
            temp.select();
            document.execCommand('copy');
            document.body.removeChild(temp);
          }
          const origHtml = copyBtn.innerHTML;
          copyBtn.innerHTML = '<i class="ph ph-check"></i> Copied!';
          copyBtn.style.background = '#22c55e';
          copyBtn.style.color = '#ffffff';

          setTimeout(() => {
            copyBtn.innerHTML = origHtml;
            copyBtn.style.background = '';
            copyBtn.style.color = '';
          }, 2500);
        } catch (err) {
          console.warn('Copy error', err);
        }
      });
    }
  }

  // 10. BOOTSTRAP ALL FEATURES
  
  // ── ELEGANT CORNER DIYAS ON CARDS (கார்டுகளில் அகல் விளக்கு) ──
  function initCardDiyas() {
    const cards = document.querySelectorAll('.tech-card, .premium-card, .case-study-card, .client-card, .testimonial-card');
    if (!cards.length) return;

    const diyaSvg = `
      <div class="diwali-card-diya" aria-hidden="true" title="Diwali Diya">
        <svg viewBox="0 0 32 30" width="26" height="24" fill="none" xmlns="http://www.w3.org/2000/svg">
          <ellipse cx="16" cy="11" rx="5" ry="8" fill="url(#flame-halo-card)" class="diya-glow"/>
          <path d="M16 3C15 7 12 10 12 13C12 16.5 13.8 18 16 18C18.2 18 20 16.5 20 13C20 10 17 7 16 3Z" fill="url(#flame-grad-card)" class="diya-flame"/>
          <ellipse cx="16" cy="13.5" rx="1.8" ry="3" fill="#ffffff"/>
          <path d="M6 18C8 24 24 24 26 18H6Z" fill="url(#clay-grad-card)"/>
          <ellipse cx="16" cy="18" rx="10" ry="2" fill="#78350f"/>
          <path d="M8 18.5C12 21 20 21 24 18.5" stroke="#fbbf24" stroke-width="1"/>
          <defs>
            <radialGradient id="flame-halo-card" cx="0.5" cy="0.5" r="0.5">
              <stop offset="0%" stop-color="#fbbf24" stop-opacity="0.6"/>
              <stop offset="100%" stop-color="#ea580c" stop-opacity="0"/>
            </radialGradient>
            <linearGradient id="flame-grad-card" x1="16" y1="3" x2="16" y2="18" gradientUnits="userSpaceOnUse">
              <stop offset="0%" stop-color="#ffffff"/>
              <stop offset="30%" stop-color="#fde047"/>
              <stop offset="70%" stop-color="#f59e0b"/>
              <stop offset="100%" stop-color="#dc2626"/>
            </linearGradient>
            <linearGradient id="clay-grad-card" x1="6" y1="18" x2="26" y2="24" gradientUnits="userSpaceOnUse">
              <stop stop-color="#ea580c"/>
              <stop offset="1" stop-color="#9a3412"/>
            </linearGradient>
          </defs>
        </svg>
      </div>
    `;

    cards.forEach(card => {
      if (card.querySelector('.diwali-card-diya')) return;
      card.insertAdjacentHTML('beforeend', diyaSvg);
    });
  }

  // ── TWINKLING FESTIVE FAIRY LIGHTS STRING (சீரியல் பல்பு மாலை) ──
  function initFairyLights() {
    const header = document.querySelector('.site-header');
    if (!header || header.querySelector('.diwali-fairy-lights')) return;
    const target = header;

    const fairyContainer = document.createElement('div');
    fairyContainer.className = 'diwali-fairy-lights';
    fairyContainer.id = 'diwali-fairy-lights';
    fairyContainer.setAttribute('aria-hidden', 'true');

    const bulbColors = ['bulb-gold', 'bulb-ruby', 'bulb-emerald', 'bulb-amber', 'bulb-cyan', 'bulb-magenta'];
    const bulbCount = 28;
    let bulbsHtml = '';

    for (let i = 0; i < bulbCount; i++) {
      const colorClass = bulbColors[i % bulbColors.length];
      bulbsHtml += `
        <div class="fairy-bulb-unit">
          <div class="fairy-socket"></div>
          <div class="fairy-bulb ${colorClass}"></div>
        </div>
      `;
    }

    fairyContainer.innerHTML = `
      <div class="fairy-cable"></div>
      <div class="fairy-bulbs-track">${bulbsHtml}</div>
    `;

    target.appendChild(fairyContainer);
  }

  
  // Track internal page navigation link clicks so preloader is skipped when browsing between pages
  document.addEventListener('click', (e) => {
    const link = e.target.closest('a[href]');
    if (!link || link.target === '_blank') return;
    const href = link.getAttribute('href');
    if (!href) return;
    if (href.startsWith('#') || href.startsWith('mailto:') || href.startsWith('tel:') || href.startsWith('javascript:')) return;
    if (link.origin === window.location.origin || !href.startsWith('http')) {
      try {
        sessionStorage.setItem('iinfo_internal_nav', 'true');
      } catch (err) {}
    }
  }, { capture: true, passive: true });

  // ── 0. FESTIVE DIWALI PRELOADER & OPENING GREETING SCREEN ──
  function initDiwaliPreloader() {
    if (document.getElementById('diwali-preloader')) return;

    // Check if this was a reload / refresh
    const navEntries = (window.performance && typeof window.performance.getEntriesByType === 'function') 
      ? window.performance.getEntriesByType('navigation') 
      : [];
    const isReload = (navEntries.length > 0 && navEntries[0].type === 'reload') ||
                     (window.performance && window.performance.navigation && window.performance.navigation.type === 1);

    // Check if user came via internal page navigation
    let isInternalNav = false;
    try {
      isInternalNav = sessionStorage.getItem('iinfo_internal_nav') === 'true';
      sessionStorage.removeItem('iinfo_internal_nav');
    } catch (e) {}

    // ONLY show wishes when site is first opened or refreshed!
    // Skip if navigating between pages inside the site.
    if (isInternalNav && !isReload) {
      return;
    }

    const preloader = document.createElement('div');
    preloader.className = 'diwali-preloader';
    preloader.id = 'diwali-preloader';
    preloader.setAttribute('role', 'dialog');
    preloader.setAttribute('aria-label', 'Diwali Festive Greeting');

    preloader.innerHTML = `
      <div class="preloader-bg-glow"></div>
      <div class="preloader-spark-layer"></div>
      
      <div class="preloader-content">
        <!-- Radiant Glowing Diya -->
        <div class="preloader-diya-wrap">
          <svg viewBox="0 0 100 85" fill="none" xmlns="http://www.w3.org/2000/svg">
            <ellipse cx="50" cy="28" rx="20" ry="26" fill="url(#preload-halo)" class="preloader-halo"/>
            <!-- Flame -->
            <path d="M50 8C47 20 38 29 38 38C38 48 43.5 53 50 53C56.5 53 62 48 62 38C62 29 53 20 50 8Z" fill="url(#preload-flame-grad)" class="preloader-flame"/>
            <ellipse cx="50" cy="40" rx="5.5" ry="9" fill="#ffffff"/>
            <!-- Terracotta Base -->
            <path d="M20 53C26 72 74 72 80 53H20Z" fill="url(#preload-clay-grad)"/>
            <ellipse cx="50" cy="53" rx="30" ry="6" fill="#78350f"/>
            <!-- Gold Ornaments -->
            <path d="M26 55C38 64 62 64 74 55" stroke="#fbbf24" stroke-width="2.5"/>
            <circle cx="50" cy="65" r="3" fill="#fef08a"/>
            <circle cx="36" cy="61" r="2.5" fill="#ffd700"/>
            <circle cx="64" cy="61" r="2.5" fill="#ffd700"/>
            <defs>
              <radialGradient id="preload-halo" cx="0.5" cy="0.5" r="0.5">
                <stop offset="0%" stop-color="#fbbf24" stop-opacity="0.8"/>
                <stop offset="45%" stop-color="#f59e0b" stop-opacity="0.4"/>
                <stop offset="100%" stop-color="#ea580c" stop-opacity="0"/>
              </radialGradient>
              <linearGradient id="preload-flame-grad" x1="50" y1="8" x2="50" y2="53" gradientUnits="userSpaceOnUse">
                <stop offset="0%" stop-color="#ffffff"/>
                <stop offset="25%" stop-color="#fef08a"/>
                <stop offset="65%" stop-color="#f59e0b"/>
                <stop offset="100%" stop-color="#dc2626"/>
              </linearGradient>
              <linearGradient id="preload-clay-grad" x1="20" y1="53" x2="80" y2="72" gradientUnits="userSpaceOnUse">
                <stop stop-color="#ea580c"/>
                <stop offset="0.5" stop-color="#c2410c"/>
                <stop offset="1" stop-color="#78350f"/>
              </linearGradient>
            </defs>
          </svg>
        </div>

        <span class="preloader-pill">🪔 இனிய தீபாவளி நல்வாழ்த்துகள் 2026 🪔</span>
        <h1 class="preloader-title">HAPPY DIWALI</h1>
        <p class="preloader-subtext">I Info Vision Wishes You &amp; Your Family Abundant Light, Success &amp; Prosperity!</p>

        <!-- Progress Tracker -->
        <div class="preloader-progress-wrap">
          <div class="preloader-progress-fill"></div>
        </div>

        <!-- Enter Button -->
        <button class="preloader-enter-btn" id="diwali-preloader-skip">
          <span>Enter Website</span>
          <span class="btn-chevron">→</span>
        </button>
        <span class="preloader-hint">Click anywhere or wait to enter</span>
      </div>
    `;

    document.body.appendChild(preloader);

    let dismissed = false;
    function dismissPreloader() {
      if (dismissed) return;
      dismissed = true;

      // Unlock Audio context immediately
      unlockDiwaliAudio();

      preloader.classList.add('dismissing');

      // Trigger celebratory welcome salvo in the background!
      setTimeout(() => {
        if (window.triggerSkyShot) {
          window.triggerSkyShot(window.innerWidth * 0.28, window.innerHeight * 0.24);
          setTimeout(() => {
            if (window.triggerKamuroWillow) {
              window.triggerKamuroWillow(window.innerWidth * 0.72, window.innerHeight * 0.22);
            }
          }, 350);
        }
      }, 250);

      setTimeout(() => {
        if (preloader.parentNode) {
          preloader.parentNode.removeChild(preloader);
        }
      }, 700);
    }

    // Auto-dismiss after 2.0s
    const autoTimer = setTimeout(dismissPreloader, 2000);

    // Click anywhere to dismiss immediately
    preloader.addEventListener('click', () => {
      clearTimeout(autoTimer);
      dismissPreloader();
    });
  }

  
  // ── OPTION 5: 🪙 FLOATING LAKSHMI GOLD COIN & FORTUNE BLESSING ──
  function playGoldChimeSound() {
    if (!isDiwaliSoundEnabled) return;
    const ctx = getDiwaliAudio();
    if (!ctx) return;
    const now = ctx.currentTime;
    try {
      [880, 1320, 1760].forEach((freq, idx) => {
        const osc = ctx.createOscillator();
        const gain = ctx.createGain();
        osc.type = 'sine';
        osc.frequency.setValueAtTime(freq, now + idx * 0.08);
        gain.gain.setValueAtTime(0.25, now + idx * 0.08);
        gain.gain.exponentialRampToValueAtTime(0.001, now + idx * 0.08 + 0.8);
        osc.connect(gain);
        gain.connect(ctx.destination);
        osc.start(now + idx * 0.08);
        osc.stop(now + idx * 0.08 + 0.8);
      });
    } catch (e) {}
  }

  function initLakshmiGoldCoin() {
    if (document.getElementById('diwali-gold-coin-widget')) return;

    // 1. Create Floating Gold Coin Widget
    const coinWidget = document.createElement('div');
    coinWidget.className = 'diwali-gold-coin-widget';
    coinWidget.id = 'diwali-gold-coin-widget';
    coinWidget.setAttribute('role', 'button');
    coinWidget.setAttribute('aria-label', 'Click for Diwali Fortune Blessing');
    coinWidget.setAttribute('title', 'Click for Diwali Fortune Blessing!');

    coinWidget.innerHTML = `
      <div class="gold-coin-tooltip">🪙 Click for Diwali Fortune!</div>
      <div class="gold-coin-inner">
        <span class="gold-coin-emblem">🪙</span>
      </div>
    `;

    document.body.appendChild(coinWidget);

    // 2. Create Fortune Blessing Modal
    const modal = document.createElement('div');
    modal.className = 'diwali-fortune-modal';
    modal.id = 'diwali-fortune-modal';
    modal.innerHTML = `
      <div class="fortune-card-box">
        <button class="fortune-modal-close" id="fortune-close-btn" aria-label="Close modal">&times;</button>
        <div class="fortune-emblem-wrap">🪙</div>
        <span class="fortune-pill">✨ மஹாலக்ஷ்மி திருவருள் ✨</span>
        <h3 class="fortune-title">Auspicious Diwali Fortune</h3>
        <p class="fortune-message">
          May the divine light of Deepavali illuminate your home and business with financial abundance, vibrant health, and unstoppable digital success!
        </p>
        <div class="fortune-coupon-box">
          <div class="fortune-coupon-title">Special Festive Voucher &bull; 25% OFF + 1-Yr Support</div>
          <div class="fortune-coupon-code">DIWALI-FORTUNE26</div>
        </div>
        <div class="fortune-actions">
          <a href="https://wa.me/919894480585?text=Hello%20I%20Info%20Vision,%20I%20unlocked%20the%20DIWALI-FORTUNE26%20voucher%20and%20want%20to%20discuss%20my%20project!" target="_blank" rel="noopener noreferrer" class="btn btn-primary">
            <i class="ph ph-whatsapp-logo"></i> Claim on WhatsApp
          </a>
          <button class="btn btn-outline" id="fortune-ok-btn" style="background: rgba(255,255,255,0.08); border-color: rgba(251,191,36,0.4); color: #fef08a;">
            Thank You 🪔
          </button>
        </div>
      </div>
    `;

    document.body.appendChild(modal);

    const closeBtn = modal.querySelector('#fortune-close-btn');
    const okBtn = modal.querySelector('#fortune-ok-btn');

    function closeModal() {
      modal.classList.remove('show');
    }

    closeBtn.addEventListener('click', closeModal);
    okBtn.addEventListener('click', closeModal);
    modal.addEventListener('click', (e) => {
      if (e.target === modal) closeModal();
    });

    // 3. Gold Coin Shower Animation on Click
    function triggerCoinShower() {
      const coinCount = 35;
      const symbols = ['🪙', '✨', '🪙', '🌟', '🪙'];
      for (let i = 0; i < coinCount; i++) {
        setTimeout(() => {
          const coin = document.createElement('div');
          coin.className = 'diwali-falling-coin';
          coin.textContent = symbols[i % symbols.length];

          const startX = Math.random() * (window.innerWidth - 60) + 30;
          const startY = -40;
          const fallSpeed = Math.random() * 2.5 + 2.5;
          const drift = (Math.random() - 0.5) * 1.5;
          let curY = startY;
          let curX = startX;
          let rotation = 0;
          const rotSpeed = (Math.random() - 0.5) * 10;

          coin.style.left = curX + 'px';
          coin.style.top = curY + 'px';
          document.body.appendChild(coin);

          const anim = setInterval(() => {
            curY += fallSpeed;
            curX += drift;
            rotation += rotSpeed;
            coin.style.top = curY + 'px';
            coin.style.left = curX + 'px';
            coin.style.transform = `rotate(${rotation}deg)`;

            if (curY > window.innerHeight + 40) {
              clearInterval(anim);
              if (coin.parentNode) coin.parentNode.removeChild(coin);
            }
          }, 16);
        }, i * 45);
      }
    }

    coinWidget.addEventListener('click', (e) => {
      e.stopPropagation();
      unlockDiwaliAudio();
      playGoldChimeSound();
      triggerCoinShower();
      setTimeout(() => {
        modal.classList.add('show');
      }, 400);
    });
  }

  
  // ── OPTION 7: 🎆 FESTIVE FOOTER SKYLINE & WISHES ──
  function initFooterSkyline() {
    const footer = document.querySelector('.site-footer');
    if (!footer) return;

    if (!footer.querySelector('.diwali-footer-skyline')) {
      const skyline = document.createElement('div');
      skyline.className = 'diwali-footer-skyline';
      skyline.setAttribute('aria-hidden', 'true');
      footer.insertBefore(skyline, footer.firstChild);
    }

    const footerBottom = footer.querySelector('.footer-bottom');
    if (footerBottom && !footer.querySelector('.diwali-footer-wishes')) {
      const wishes = document.createElement('div');
      wishes.className = 'diwali-footer-wishes';
      wishes.innerHTML = '<span class="wishes-diya">🪔</span> Celebrate the Festival of Lights with I Info Vision &bull; Wishing You Abundant Growth &amp; Prosperity! <span class="wishes-diya">🪔</span>';
      footerBottom.parentNode.insertBefore(wishes, footerBottom);
    }
  }

  function bootstrap() {
    initDiwaliPreloader();
    initDiwaliBannerAndHeader();
    initHangingToran();
    initRangoliWatermark();
    initRocketBackToTop();
    initLightADiya();
    initCountdown();
    initOfferModal();
    initFireworksEngine();
    initScrollFountains();
    initCardDiyas();
    initFairyLights();
    initLakshmiGoldCoin();
    initFooterSkyline();
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', bootstrap);
  } else {
    bootstrap();
  }

})();
