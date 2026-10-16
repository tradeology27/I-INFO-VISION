"""
Complete Production Generator for I Info Vision:
1. Generates 62 Localized City Landing Pages
2. Generates 18 Industry-Vertical ERP & POS Solutions Pages
3. Generates 14 High-Authority Technology & Business Strategy Guides
4. Generates directory.html (Master Internal Linking Hub)
5. Updates sitemap.xml with 125+ URLs
"""

import os
import re
import html
import json
import xml.etree.ElementTree as ET

from generate_seo_pages import LOCATIONS_DATA
from data_industry import INDUSTRY_DATA
from data_guides import GUIDES_DATA

WORKSPACE = r"c:\Users\prave\OneDrive\Desktop\office projects\I-INFO-VISION-main"

# Deduplicate locations by filename
seen_files = set()
UNIQUE_LOCATIONS = []
for loc in LOCATIONS_DATA:
    if loc["filename"] not in seen_files:
        seen_files.add(loc["filename"])
        UNIQUE_LOCATIONS.append(loc)

print(f"Unique Location Pages: {len(UNIQUE_LOCATIONS)}")
print(f"Industry Pages: {len(INDUSTRY_DATA)}")
print(f"Guide Articles: {len(GUIDES_DATA)}")
total_new_pages = len(UNIQUE_LOCATIONS) + len(INDUSTRY_DATA) + len(GUIDES_DATA)
print(f"Total Unique Pages to Generate: {total_new_pages}")

# ==================== HTML TEMPLATES ====================

HEADER_HTML = """  <!-- HEADER -->
  <header class="site-header scrolled" id="site-header">
    <div class="container">
      <nav class="nav-wrapper">
        <a href="index.html" class="logo">
          <img src="assets/images/logo.webp" alt="I Info Vision Logo" class="logo-img" width="68" height="48" />
          <div class="logo-text-wrapper">
            <span class="logo-text">I Info<span class="logo-accent"> Vision</span></span>
            <span class="logo-slogan">INNOVATE-INFORM-INSPIRE</span>
          </div>
        </a>

        <div class="mobile-overlay" id="mobile-overlay"></div>

        <ul class="nav-menu" id="nav-menu">
          <li><a href="index.html#hero" class="nav-link">Home</a></li>
          <li><a href="services.html" class="nav-link active">Services</a></li>
          <li><a href="about.html" class="nav-link">About</a></li>
          <li><a href="clients.html" class="nav-link">Clients</a></li>
          <li><a href="blogs.html" class="nav-link">Blogs</a></li>
          <li><a href="faq.html" class="nav-link">FAQ</a></li>
          <li><a href="contact.html" class="nav-link">Contact</a></li>
          <li><a href="contact.html" class="nav-cta">Get Started <span class="btn-arrow">&rarr;</span></a></li>
        </ul>

        <button class="nav-toggle" id="nav-toggle" aria-label="Toggle menu">
          <span></span><span></span><span></span>
        </button>
      </nav>
    </div>
  </header>"""

FOOTER_HTML = """  <!-- FOOTER -->
  <footer class="site-footer">
    <div class="container">
      <div class="footer-grid">
        <div class="footer-brand">
          <a href="index.html" class="logo">
            <img src="assets/images/logo.webp" alt="I Info Vision Logo" class="logo-img" width="68" height="48" />
            <div class="logo-text-wrapper">
              <span class="logo-text">I Info<span class="logo-accent"> Vision</span></span>
              <span class="logo-slogan">INNOVATE-INFORM-INSPIRE</span>
            </div>
          </a>
          <p class="footer-brand-desc">
            A proud Yasmeen Group Company transforming ideas into digital success through innovation, technology, and excellence across Salem, Coimbatore, Karur, Chennai, and Tamil Nadu.
          </p>
        </div>
        <div>
          <h4 class="footer-heading">Services</h4>
          <ul class="footer-links">
            <li><a href="web-development.html">Web Development &amp; Apps</a></li>
            <li><a href="crm-erp-software.html">CRM &amp; ERP Software</a></li>
            <li><a href="ecommerce-solutions.html">E-Commerce Solutions</a></li>
            <li><a href="billing-software.html">Billing &amp; POS Software</a></li>
            <li><a href="mobile-app-development.html">Mobile App Development</a></li>
            <li><a href="hospital-management-software.html">Hospital &amp; Clinic HMS</a></li>
            <li><a href="textile-garment-erp-software.html">Textile &amp; Garment ERP</a></li>
            <li><a href="directory.html">All Locations &amp; Directory</a></li>
          </ul>
        </div>
        <div>
          <h4 class="footer-heading">Company</h4>
          <ul class="footer-links">
            <li><a href="about.html">About Us</a></li>
            <li><a href="services.html">Our Services</a></li>
            <li><a href="clients.html">Our Clients &amp; Projects</a></li>
            <li><a href="blogs.html">Blogs &amp; Guides</a></li>
            <li><a href="directory.html">Locations Directory</a></li>
            <li><a href="privacy.html">Privacy Policy</a></li>
            <li><a href="terms.html">Terms of Service</a></li>
          </ul>
        </div>
        <div>
          <h4 class="footer-heading">Contact Us</h4>
          <div class="footer-contact-item">
            <div class="footer-contact-icon"><i class="ph ph-map-pin"></i></div>
            <div class="footer-contact-text">
              <span class="label">Headquarters</span>
              <span>#9/136, No.1, First Floor, Trichy Main Road, Chinnaiyapuram, Dasanaickenpatti, Salem &ndash; 636201</span>
            </div>
          </div>
          <div class="footer-contact-item">
            <div class="footer-contact-icon"><i class="ph ph-phone"></i></div>
            <div class="footer-contact-text">
              <span class="label">Phone / WhatsApp</span>
              <a href="tel:+919894480585">+91 98944 80585</a>
            </div>
          </div>
        </div>
      </div>

      <div class="footer-bottom">
        <p class="copyright">&copy; 2026 I Info Vision (A Yasmeen Group Company). All rights reserved.</p>
        <div class="footer-bottom-links">
          <a href="privacy.html">Privacy Policy</a>
          <a href="terms.html">Terms of Service</a>
          <a href="sitemap.html">Sitemap</a>
          <a href="directory.html">Directory</a>
        </div>
      </div>
    </div>
  </footer>

  <!-- Sticky Mobile Quick-Action Bar -->
  <nav class="mobile-quick-actions" aria-label="Quick Actions">
    <a href="tel:+919894480585" class="quick-action-btn quick-call-btn">
      <i class="ph ph-phone-call"></i>
      <span>Call Now</span>
    </a>
    <a href="https://wa.me/919894480585" class="quick-action-btn quick-whatsapp-btn" target="_blank" rel="noopener noreferrer">
      <i class="ph ph-whatsapp-logo"></i>
      <span>WhatsApp</span>
    </a>
  </nav>

  <a href="https://wa.me/919894480585" class="whatsapp-float" target="_blank" aria-label="Chat on WhatsApp"><i class="ph ph-whatsapp-logo"></i></a>
  <button class="back-to-top" id="back-to-top" aria-label="Back to top"><i class="ph ph-caret-up"></i></button>
  <script src="script.js" defer></script>
</body>
</html>"""

def build_location_page(loc):
    faqs_json = []
    faqs_html = ""
    for q, a in loc["faqs"]:
        faqs_json.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": a
            }
        })
        faqs_html += f"""          <div class="faq-item" style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 14px; padding: 20px 24px; margin-bottom: 16px; box-shadow: 0 2px 10px rgba(0,0,0,0.03);">
            <h3 style="font-size: 16px; font-weight: 700; color: #0f172a; margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
              <i class="ph ph-question" style="color: #0284c7; font-size: 18px;"></i> {html.escape(q)}
            </h3>
            <p style="color: #475569; font-size: 14.5px; line-height: 1.6; margin: 0;">
              {html.escape(a)}
            </p>
          </div>\n"""

    schema_graph = [
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.iinfovision.com/" },
                { "@type": "ListItem", "position": 2, "name": "Services", "item": "https://www.iinfovision.com/services.html" },
                { "@type": "ListItem", "position": 3, "name": f"{loc['service']} in {loc['city']}", "item": f"https://www.iinfovision.com/{loc['filename']}" }
            ]
        },
        {
            "@type": "Service",
            "name": f"{loc['service']} in {loc['city']}",
            "serviceType": loc['service'],
            "provider": {
                "@type": "LocalBusiness",
                "name": "I Info Vision",
                "url": "https://www.iinfovision.com/",
                "telephone": "+919894480585",
                "address": {
                    "@type": "PostalAddress",
                    "streetAddress": "#9/136, No.1, First Floor, Trichy Main Road, Chinnaiyapuram, Dasanaickenpatti",
                    "addressLocality": "Salem",
                    "addressRegion": "Tamil Nadu",
                    "postalCode": "636201",
                    "addressCountry": "IN"
                }
            },
            "areaServed": [
                { "@type": "City", "name": loc['city'] },
                { "@type": "State", "name": loc['state'] },
                { "@type": "Country", "name": "India" }
            ],
            "url": f"https://www.iinfovision.com/{loc['filename']}",
            "description": loc['desc']
        },
        {
            "@type": "FAQPage",
            "mainEntity": faqs_json
        }
    ]

    schema_json_str = json.dumps({"@context": "https://schema.org", "@graph": schema_graph}, indent=2)

    return f"""<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{html.escape(loc['title'])}</title>
  <meta name="description" content="{html.escape(loc['desc'])}" />
  <meta name="keywords" content="{html.escape(loc['keywords'])}" />
  <meta name="author" content="I Info Vision" />
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1" />
  <meta name="geo.region" content="IN-TN" />
  <meta name="geo.placename" content="{loc['city']}" />
  <meta name="geo.position" content="{loc['geo'][0]};{loc['geo'][1]}" />
  <meta name="ICBM" content="{loc['geo'][0]}, {loc['geo'][1]}" />
  <link rel="canonical" href="https://www.iinfovision.com/{loc['filename']}" />

  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website" />
  <meta property="og:url" content="https://www.iinfovision.com/{loc['filename']}" />
  <meta property="og:site_name" content="I Info Vision" />
  <meta property="og:locale" content="en_IN" />
  <meta property="og:title" content="{html.escape(loc['title'])}" />
  <meta property="og:description" content="{html.escape(loc['desc'])}" />
  <meta property="og:image" content="https://www.iinfovision.com/assets/images/logo.webp" />

  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:url" content="https://www.iinfovision.com/{loc['filename']}" />
  <meta name="twitter:title" content="{html.escape(loc['title'])}" />
  <meta name="twitter:description" content="{html.escape(loc['desc'])}" />
  <meta name="twitter:image" content="https://www.iinfovision.com/assets/images/logo.webp" />

  <!-- Schema.org JSON-LD Structured Data -->
  <script type="application/ld+json">
{schema_json_str}
  </script>
  <link rel="icon" type="image/png" href="assets/images/logo.webp" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" />
  <link rel="stylesheet" href="styles.css?v=2.1" />
  <link rel="stylesheet" href="https://unpkg.com/@phosphor-icons/web@2.1.1/src/regular/style.css" media="print" onload="this.media='all'" />
  <noscript><link rel="stylesheet" href="https://unpkg.com/@phosphor-icons/web@2.1.1/src/regular/style.css" /></noscript>
</head>

<body>

{HEADER_HTML}

  <!-- PAGE HERO -->
  <section class="page-hero" style="padding: 130px 0 60px 0; background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #ffffff;">
    <div class="container">
      <div class="page-hero-inner" style="max-width: 900px; margin: 0 auto; text-align: center;">
        <div class="page-breadcrumb" style="justify-content: center; margin-bottom: 18px; color: #94a3b8; font-size: 13px;">
          <a href="index.html" style="color: #94a3b8;">Home</a>
          <i class="ph ph-caret-right"></i>
          <a href="services.html" style="color: #94a3b8;">Services</a>
          <i class="ph ph-caret-right"></i>
          <span style="color: #38bdf8;">{loc['city']}</span>
        </div>
        <div style="display: inline-block; background: rgba(56, 189, 248, 0.15); border: 1px solid rgba(56, 189, 248, 0.4); color: #38bdf8; font-size: 12.5px; font-weight: 700; padding: 6px 16px; border-radius: 20px; margin-bottom: 20px;">
          <i class="ph ph-map-pin"></i> {loc['badge']}
        </div>
        <h1 class="page-hero-title" style="font-size: clamp(28px, 4.5vw, 46px); font-weight: 800; line-height: 1.25; margin-bottom: 20px;">
          {loc['hero_title']}
        </h1>
        <p class="page-hero-desc" style="font-size: 16.5px; line-height: 1.7; color: #cbd5e1; max-width: 780px; margin: 0 auto 30px auto;">
          {loc['hero_desc']}
        </p>
        <div style="display: flex; justify-content: center; gap: 14px; flex-wrap: wrap;">
          <a href="contact.html?city={loc['city'].lower()}&service={loc['service'].lower().replace(' ', '-')}" class="btn btn-primary" style="padding: 13px 26px; font-weight: 700; border-radius: 10px; font-size: 14.5px;">
            Get Free Consultation &rarr;
          </a>
          <a href="tel:+919894480585" class="btn" style="background: rgba(255,255,255,0.08); color: #ffffff; border: 1.5px solid rgba(255,255,255,0.25); padding: 13px 22px; font-weight: 700; border-radius: 10px; font-size: 14.5px; display: inline-flex; align-items: center; gap: 8px;">
            <i class="ph ph-phone-call"></i> Call: +91 98944 80585
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- BUSINESS ADVANTAGES -->
  <section style="padding: 60px 0; background: #f8fafc;">
    <div class="container">
      <div style="text-align: center; max-width: 700px; margin: 0 auto 40px auto;">
        <span style="color: #0284c7; font-weight: 700; font-size: 13px; text-transform: uppercase; letter-spacing: 1px;">Why Partner With Us</span>
        <h2 style="font-size: 28px; font-weight: 800; color: #0f172a; margin-top: 8px;">Why Businesses in {loc['city']} Choose I Info Vision</h2>
        <p style="color: #64748b; font-size: 15px;">Tailored solutions engineered specifically for {loc['industry_focus']}.</p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px;">
        <div style="background: #ffffff; padding: 28px; border-radius: 16px; border: 1.5px solid #e2e8f0; box-shadow: 0 4px 15px rgba(0,0,0,0.04);">
          <div style="width: 48px; height: 48px; border-radius: 12px; background: #e0f2fe; color: #0284c7; display: flex; align-items: center; justify-content: center; font-size: 24px; margin-bottom: 18px;">
            <i class="ph ph-lightning"></i>
          </div>
          <h3 style="font-size: 18px; font-weight: 700; color: #0f172a; margin-bottom: 10px;">Sub-Second Speed &amp; 99.9% Uptime</h3>
          <p style="color: #64748b; font-size: 14.5px; line-height: 1.6;">Ultra-optimized lightweight code guaranteeing maximum Google PageSpeed rankings and seamless customer checkout experiences.</p>
        </div>

        <div style="background: #ffffff; padding: 28px; border-radius: 16px; border: 1.5px solid #e2e8f0; box-shadow: 0 4px 15px rgba(0,0,0,0.04);">
          <div style="width: 48px; height: 48px; border-radius: 12px; background: #dcfce7; color: #16a34a; display: flex; align-items: center; justify-content: center; font-size: 24px; margin-bottom: 18px;">
            <i class="ph ph-shield-check"></i>
          </div>
          <h3 style="font-size: 18px; font-weight: 700; color: #0f172a; margin-bottom: 10px;">100% Data Security &amp; GST Ready</h3>
          <p style="color: #64748b; font-size: 14.5px; line-height: 1.6;">Automated E-Invoicing, E-Way bills, bank-grade encryption, and automatic off-site cloud backups safeguarding business continuity.</p>
        </div>

        <div style="background: #ffffff; padding: 28px; border-radius: 16px; border: 1.5px solid #e2e8f0; box-shadow: 0 4px 15px rgba(0,0,0,0.04);">
          <div style="width: 48px; height: 48px; border-radius: 12px; background: #fef3c7; color: #d97706; display: flex; align-items: center; justify-content: center; font-size: 24px; margin-bottom: 18px;">
            <i class="ph ph-users-three"></i>
          </div>
          <h3 style="font-size: 18px; font-weight: 700; color: #0f172a; margin-bottom: 10px;">Direct On-Site &amp; Regional Support</h3>
          <p style="color: #64748b; font-size: 14.5px; line-height: 1.6;">Hands-on staff training, zero-downtime data migration from Tally/Excel, and fast on-demand phone &amp; remote assistance.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- CASE STUDY SPOTLIGHT -->
  <section style="padding: 50px 0; background: #ffffff;">
    <div class="container">
      <div style="background: linear-gradient(135deg, #0b1120 0%, #1e293b 100%); border-radius: 20px; padding: 36px 40px; color: #ffffff; display: flex; flex-direction: column; md:flex-row; justify-content: space-between; align-items: center; gap: 24px;">
        <div style="max-width: 650px;">
          <span style="background: rgba(2, 132, 199, 0.25); color: #38bdf8; font-size: 12px; font-weight: 700; padding: 4px 12px; border-radius: 20px;">Client Spotlight</span>
          <h3 style="font-size: 22px; font-weight: 800; color: #ffffff; margin: 12px 0 8px 0;">{loc['client_name']}</h3>
          <p style="color: #94a3b8; font-size: 14.5px; line-height: 1.6; margin: 0;">{loc['client_summary']}</p>
        </div>
        <div>
          <a href="{loc['client_ref']}" class="btn btn-primary" style="padding: 12px 22px; font-size: 14px; font-weight: 700; white-space: nowrap;">
            Explore Case Study &rarr;
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- PRICING TIERS -->
  <section style="padding: 60px 0; background: #f8fafc;">
    <div class="container">
      <div style="text-align: center; max-width: 700px; margin: 0 auto 40px auto;">
        <span style="color: #0284c7; font-weight: 700; font-size: 13px; text-transform: uppercase; letter-spacing: 1px;">Clear Investment</span>
        <h2 style="font-size: 28px; font-weight: 800; color: #0f172a; margin-top: 8px;">Transparent Pricing for {loc['city']} Businesses</h2>
        <p style="color: #64748b; font-size: 15px;">No hidden charges. 100% deliverable transparency with dedicated post-launch warranty.</p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 24px; max-width: 1000px; margin: 0 auto;">
        <div style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 16px; padding: 32px 24px; text-align: center;">
          <h3 style="font-size: 18px; font-weight: 700; color: #0f172a;">Starter Tier</h3>
          <div style="font-size: 32px; font-weight: 800; color: #0284c7; margin: 16px 0;">{loc['pricing_starter']}</div>
          <p style="color: #64748b; font-size: 13.5px; margin-bottom: 20px;">Essential fast-track setup for emerging shops &amp; clinics.</p>
          <a href="contact.html?plan=starter&city={loc['city'].lower()}" class="btn" style="display: block; width: 100%; border: 1.5px solid #0284c7; color: #0284c7; padding: 10px; border-radius: 8px; font-weight: 700; font-size: 14px;">Choose Starter</a>
        </div>

        <div style="background: #ffffff; border: 2.5px solid #0284c7; border-radius: 16px; padding: 32px 24px; text-align: center; position: relative; box-shadow: 0 8px 25px rgba(2, 132, 199, 0.12);">
          <div style="position: absolute; top: -12px; left: 50%; transform: translateX(-50%); background: #0284c7; color: #ffffff; font-size: 11px; font-weight: 800; padding: 3px 12px; border-radius: 20px; text-transform: uppercase;">Most Popular</div>
          <h3 style="font-size: 18px; font-weight: 700; color: #0f172a;">Growth Tier</h3>
          <div style="font-size: 32px; font-weight: 800; color: #0284c7; margin: 16px 0;">{loc['pricing_growth']}</div>
          <p style="color: #64748b; font-size: 13.5px; margin-bottom: 20px;">Full-featured automation, multi-counter &amp; SEO reporting.</p>
          <a href="contact.html?plan=growth&city={loc['city'].lower()}" class="btn btn-primary" style="display: block; width: 100%; padding: 10px; border-radius: 8px; font-weight: 700; font-size: 14px;">Choose Growth</a>
        </div>

        <div style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 16px; padding: 32px 24px; text-align: center;">
          <h3 style="font-size: 18px; font-weight: 700; color: #0f172a;">Enterprise Custom</h3>
          <div style="font-size: 32px; font-weight: 800; color: #0284c7; margin: 16px 0;">{loc['pricing_custom']}</div>
          <p style="color: #64748b; font-size: 13.5px; margin-bottom: 20px;">Multi-branch ERP, microservices &amp; dedicated cloud cluster.</p>
          <a href="contact.html?plan=enterprise&city={loc['city'].lower()}" class="btn" style="display: block; width: 100%; border: 1.5px solid #0284c7; color: #0284c7; padding: 10px; border-radius: 8px; font-weight: 700; font-size: 14px;">Request Scope</a>
        </div>
      </div>
    </div>
  </section>

  <!-- FAQS ACCORDION -->
  <section style="padding: 60px 0; background: #ffffff;">
    <div class="container" style="max-width: 860px;">
      <div style="text-align: center; margin-bottom: 40px;">
        <span style="color: #0284c7; font-weight: 700; font-size: 13px; text-transform: uppercase; letter-spacing: 1px;">Got Questions?</span>
        <h2 style="font-size: 28px; font-weight: 800; color: #0f172a; margin-top: 8px;">Frequently Asked Questions in {loc['city']}</h2>
      </div>

      <div class="faq-list">
{faqs_html}      </div>
    </div>
  </section>

  <!-- CTA BANNER -->
  <section style="padding: 60px 0; background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%); color: #ffffff; text-align: center;">
    <div class="container" style="max-width: 800px;">
      <h2 style="font-size: 32px; font-weight: 800; margin-bottom: 16px;">Ready to Scale Your Business in {loc['city']}?</h2>
      <p style="font-size: 16.5px; color: #e0f2fe; margin-bottom: 30px; line-height: 1.6;">
        Book a free 30-minute discovery consultation with our senior solutions engineers. We will analyze your workflows and propose a high-ROI digital blueprint.
      </p>
      <div style="display: flex; justify-content: center; gap: 14px; flex-wrap: wrap;">
        <a href="contact.html?city={loc['city'].lower()}" class="btn" style="background: #ffffff; color: #0369a1; padding: 14px 28px; font-weight: 800; border-radius: 10px; font-size: 15px;">
          Book Free Strategy Call &rarr;
        </a>
        <a href="https://wa.me/919894480585" target="_blank" class="btn" style="background: #25d366; color: #ffffff; padding: 14px 24px; font-weight: 800; border-radius: 10px; font-size: 15px; display: inline-flex; align-items: center; gap: 8px;">
          <i class="ph ph-whatsapp-logo" style="font-size: 18px;"></i> WhatsApp Us Directly
        </a>
      </div>
    </div>
  </section>

{FOOTER_HTML}"""

def build_industry_page(ind):
    faqs_json = []
    faqs_html = ""
    for q, a in ind["faqs"]:
        faqs_json.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": a
            }
        })
        faqs_html += f"""          <div class="faq-item" style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 14px; padding: 20px 24px; margin-bottom: 16px; box-shadow: 0 2px 10px rgba(0,0,0,0.03);">
            <h3 style="font-size: 16px; font-weight: 700; color: #0f172a; margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
              <i class="ph ph-question" style="color: #0284c7; font-size: 18px;"></i> {html.escape(q)}
            </h3>
            <p style="color: #475569; font-size: 14.5px; line-height: 1.6; margin: 0;">
              {html.escape(a)}
            </p>
          </div>\n"""

    deliverables_html = ""
    for title, desc in ind["deliverables"]:
        deliverables_html += f"""        <div style="background: #ffffff; padding: 26px; border-radius: 16px; border: 1.5px solid #e2e8f0; box-shadow: 0 3px 12px rgba(0,0,0,0.03);">
          <div style="width: 44px; height: 44px; border-radius: 10px; background: #e0f2fe; color: #0284c7; display: flex; align-items: center; justify-content: center; font-size: 22px; margin-bottom: 14px;">
            <i class="ph ph-check-circle"></i>
          </div>
          <h3 style="font-size: 17.5px; font-weight: 700; color: #0f172a; margin-bottom: 8px;">{html.escape(title)}</h3>
          <p style="color: #64748b; font-size: 14px; line-height: 1.6; margin: 0;">{html.escape(desc)}</p>
        </div>\n"""

    schema_graph = [
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.iinfovision.com/" },
                { "@type": "ListItem", "position": 2, "name": "Industry Solutions", "item": "https://www.iinfovision.com/services.html" },
                { "@type": "ListItem", "position": 3, "name": ind['name'], "item": f"https://www.iinfovision.com/{ind['filename']}" }
            ]
        },
        {
            "@type": "SoftwareApplication",
            "name": ind['name'],
            "operatingSystem": "Web, Windows, Android, iOS",
            "applicationCategory": "BusinessApplication",
            "aggregateRating": {
                "@type": "AggregateRating",
                "ratingValue": "4.9",
                "ratingCount": "142"
            },
            "offers": {
                "@type": "Offer",
                "price": "29999",
                "priceCurrency": "INR"
            },
            "description": ind['desc'],
            "url": f"https://www.iinfovision.com/{ind['filename']}"
        },
        {
            "@type": "FAQPage",
            "mainEntity": faqs_json
        }
    ]

    schema_json_str = json.dumps({"@context": "https://schema.org", "@graph": schema_graph}, indent=2)

    return f"""<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{html.escape(ind['title'])}</title>
  <meta name="description" content="{html.escape(ind['desc'])}" />
  <meta name="keywords" content="{html.escape(ind['keywords'])}" />
  <meta name="author" content="I Info Vision" />
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1" />
  <meta name="geo.region" content="IN-TN" />
  <meta name="geo.placename" content="Salem, Tamil Nadu" />
  <link rel="canonical" href="https://www.iinfovision.com/{ind['filename']}" />

  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website" />
  <meta property="og:url" content="https://www.iinfovision.com/{ind['filename']}" />
  <meta property="og:site_name" content="I Info Vision" />
  <meta property="og:locale" content="en_IN" />
  <meta property="og:title" content="{html.escape(ind['title'])}" />
  <meta property="og:description" content="{html.escape(ind['desc'])}" />
  <meta property="og:image" content="https://www.iinfovision.com/assets/images/logo.webp" />

  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:url" content="https://www.iinfovision.com/{ind['filename']}" />
  <meta name="twitter:title" content="{html.escape(ind['title'])}" />
  <meta name="twitter:description" content="{html.escape(ind['desc'])}" />
  <meta name="twitter:image" content="https://www.iinfovision.com/assets/images/logo.webp" />

  <!-- Schema.org JSON-LD Structured Data -->
  <script type="application/ld+json">
{schema_json_str}
  </script>
  <link rel="icon" type="image/png" href="assets/images/logo.webp" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" />
  <link rel="stylesheet" href="styles.css?v=2.1" />
  <link rel="stylesheet" href="https://unpkg.com/@phosphor-icons/web@2.1.1/src/regular/style.css" media="print" onload="this.media='all'" />
  <noscript><link rel="stylesheet" href="https://unpkg.com/@phosphor-icons/web@2.1.1/src/regular/style.css" /></noscript>
</head>

<body>

{HEADER_HTML}

  <!-- PAGE HERO -->
  <section class="page-hero" style="padding: 130px 0 60px 0; background: linear-gradient(135deg, #0b1120 0%, #1e293b 100%); color: #ffffff;">
    <div class="container">
      <div class="page-hero-inner" style="max-width: 900px; margin: 0 auto; text-align: center;">
        <div class="page-breadcrumb" style="justify-content: center; margin-bottom: 18px; color: #94a3b8; font-size: 13px;">
          <a href="index.html" style="color: #94a3b8;">Home</a>
          <i class="ph ph-caret-right"></i>
          <a href="services.html" style="color: #94a3b8;">Solutions</a>
          <i class="ph ph-caret-right"></i>
          <span style="color: #38bdf8;">{ind['name']}</span>
        </div>
        <div style="display: inline-block; background: rgba(56, 189, 248, 0.15); border: 1px solid rgba(56, 189, 248, 0.4); color: #38bdf8; font-size: 12.5px; font-weight: 700; padding: 6px 16px; border-radius: 20px; margin-bottom: 20px;">
          <i class="ph ph-cpu"></i> {ind['badge']}
        </div>
        <h1 class="page-hero-title" style="font-size: clamp(28px, 4.5vw, 46px); font-weight: 800; line-height: 1.25; margin-bottom: 20px;">
          {ind['hero_title']}
        </h1>
        <p class="page-hero-desc" style="font-size: 16.5px; line-height: 1.7; color: #cbd5e1; max-width: 780px; margin: 0 auto 30px auto;">
          {ind['hero_desc']}
        </p>
        <div style="display: flex; justify-content: center; gap: 14px; flex-wrap: wrap;">
          <a href="contact.html?solution={ind['filename'].replace('.html', '')}" class="btn btn-primary" style="padding: 13px 26px; font-weight: 700; border-radius: 10px; font-size: 14.5px;">
            Schedule Live Demo &rarr;
          </a>
          <a href="https://wa.me/919894480585" target="_blank" class="btn" style="background: rgba(255,255,255,0.08); color: #ffffff; border: 1.5px solid rgba(255,255,255,0.25); padding: 13px 22px; font-weight: 700; border-radius: 10px; font-size: 14.5px; display: inline-flex; align-items: center; gap: 8px;">
            <i class="ph ph-whatsapp-logo"></i> Instant WhatsApp Demo
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- CORE DELIVERABLES -->
  <section style="padding: 60px 0; background: #f8fafc;">
    <div class="container">
      <div style="text-align: center; max-width: 700px; margin: 0 auto 40px auto;">
        <span style="color: #0284c7; font-weight: 700; font-size: 13px; text-transform: uppercase; letter-spacing: 1px;">Product Capabilities</span>
        <h2 style="font-size: 28px; font-weight: 800; color: #0f172a; margin-top: 8px;">Key Modules &amp; Engineering Deliverables</h2>
        <p style="color: #64748b; font-size: 15px;">Engineered for high-volume transactions, zero latency, and absolute audit compliance.</p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 24px;">
{deliverables_html}      </div>
    </div>
  </section>

  <!-- CASE STUDY SPOTLIGHT -->
  <section style="padding: 50px 0; background: #ffffff;">
    <div class="container">
      <div style="background: linear-gradient(135deg, #0b1120 0%, #1e293b 100%); border-radius: 20px; padding: 36px 40px; color: #ffffff; display: flex; flex-direction: column; md:flex-row; justify-content: space-between; align-items: center; gap: 24px;">
        <div style="max-width: 650px;">
          <span style="background: rgba(2, 132, 199, 0.25); color: #38bdf8; font-size: 12px; font-weight: 700; padding: 4px 12px; border-radius: 20px;">Proven In Production</span>
          <h3 style="font-size: 22px; font-weight: 800; color: #ffffff; margin: 12px 0 8px 0;">{ind['client_name']}</h3>
          <p style="color: #94a3b8; font-size: 14.5px; line-height: 1.6; margin: 0;">{ind['client_summary']}</p>
        </div>
        <div>
          <a href="{ind['client_ref']}" class="btn btn-primary" style="padding: 12px 22px; font-size: 14px; font-weight: 700; white-space: nowrap;">
            View Production Case Study &rarr;
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- FAQS ACCORDION -->
  <section style="padding: 60px 0; background: #f8fafc;">
    <div class="container" style="max-width: 860px;">
      <div style="text-align: center; margin-bottom: 40px;">
        <span style="color: #0284c7; font-weight: 700; font-size: 13px; text-transform: uppercase; letter-spacing: 1px;">Architecture Insights</span>
        <h2 style="font-size: 28px; font-weight: 800; color: #0f172a; margin-top: 8px;">Frequently Asked Questions</h2>
      </div>

      <div class="faq-list">
{faqs_html}      </div>
    </div>
  </section>

  <!-- CTA BANNER -->
  <section style="padding: 60px 0; background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%); color: #ffffff; text-align: center;">
    <div class="container" style="max-width: 800px;">
      <h2 style="font-size: 32px; font-weight: 800; margin-bottom: 16px;">Automate Your Operations with {ind['name']}</h2>
      <p style="font-size: 16.5px; color: #e0f2fe; margin-bottom: 30px; line-height: 1.6;">
        Join premier enterprises across Tamil Nadu who rely on I Info Vision for mission-critical software automation.
      </p>
      <div style="display: flex; justify-content: center; gap: 14px; flex-wrap: wrap;">
        <a href="contact.html?solution={ind['filename'].replace('.html', '')}" class="btn" style="background: #ffffff; color: #0369a1; padding: 14px 28px; font-weight: 800; border-radius: 10px; font-size: 15px;">
          Request Custom Proposal &rarr;
        </a>
        <a href="tel:+919894480585" class="btn" style="background: rgba(0,0,0,0.2); color: #ffffff; border: 1.5px solid rgba(255,255,255,0.4); padding: 14px 24px; font-weight: 800; border-radius: 10px; font-size: 15px; display: inline-flex; align-items: center; gap: 8px;">
          <i class="ph ph-phone-call"></i> Call Senior Architect
        </a>
      </div>
    </div>
  </section>

{FOOTER_HTML}"""

def build_guide_page(g):
    faqs_json = []
    faqs_html = ""
    for q, a in g["faqs"]:
        faqs_json.append({
            "@type": "Question",
            "name": q,
            "acceptedAnswer": {
                "@type": "Answer",
                "text": a
            }
        })
        faqs_html += f"""          <div class="faq-item" style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 14px; padding: 20px 24px; margin-bottom: 16px; box-shadow: 0 2px 10px rgba(0,0,0,0.03);">
            <h3 style="font-size: 16px; font-weight: 700; color: #0f172a; margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
              <i class="ph ph-question" style="color: #0284c7; font-size: 18px;"></i> {html.escape(q)}
            </h3>
            <p style="color: #475569; font-size: 14.5px; line-height: 1.6; margin: 0;">
              {html.escape(a)}
            </p>
          </div>\n"""

    schema_graph = [
        {
            "@type": "BreadcrumbList",
            "itemListElement": [
                { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.iinfovision.com/" },
                { "@type": "ListItem", "position": 2, "name": "Blogs & Guides", "item": "https://www.iinfovision.com/blogs.html" },
                { "@type": "ListItem", "position": 3, "name": g['title'], "item": f"https://www.iinfovision.com/{g['filename']}" }
            ]
        },
        {
            "@type": "Article",
            "headline": g['title'],
            "datePublished": g['date'],
            "dateModified": "2026-10-16",
            "author": {
                "@type": "Organization",
                "name": "I Info Vision Research & Engineering Team",
                "url": "https://www.iinfovision.com/"
            },
            "publisher": {
                "@type": "Organization",
                "name": "I Info Vision",
                "logo": {
                    "@type": "ImageObject",
                    "url": "https://www.iinfovision.com/assets/images/logo.webp"
                }
            },
            "description": g['desc'],
            "url": f"https://www.iinfovision.com/{g['filename']}"
        },
        {
            "@type": "FAQPage",
            "mainEntity": faqs_json
        }
    ]

    schema_json_str = json.dumps({"@context": "https://schema.org", "@graph": schema_graph}, indent=2)

    return f"""<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{html.escape(g['title'])} | I Info Vision</title>
  <meta name="description" content="{html.escape(g['desc'])}" />
  <meta name="keywords" content="{html.escape(g['keywords'])}" />
  <meta name="author" content="I Info Vision" />
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1" />
  <link rel="canonical" href="https://www.iinfovision.com/{g['filename']}" />

  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="article" />
  <meta property="og:url" content="https://www.iinfovision.com/{g['filename']}" />
  <meta property="og:site_name" content="I Info Vision" />
  <meta property="og:locale" content="en_IN" />
  <meta property="og:title" content="{html.escape(g['title'])}" />
  <meta property="og:description" content="{html.escape(g['desc'])}" />
  <meta property="og:image" content="https://www.iinfovision.com/assets/images/logo.webp" />

  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:url" content="https://www.iinfovision.com/{g['filename']}" />
  <meta name="twitter:title" content="{html.escape(g['title'])}" />
  <meta name="twitter:description" content="{html.escape(g['desc'])}" />
  <meta name="twitter:image" content="https://www.iinfovision.com/assets/images/logo.webp" />

  <!-- Schema.org JSON-LD Structured Data -->
  <script type="application/ld+json">
{schema_json_str}
  </script>
  <link rel="icon" type="image/png" href="assets/images/logo.webp" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&display=swap" />
  <link rel="stylesheet" href="styles.css?v=2.1" />
  <link rel="stylesheet" href="https://unpkg.com/@phosphor-icons/web@2.1.1/src/regular/style.css" media="print" onload="this.media='all'" />
  <noscript><link rel="stylesheet" href="https://unpkg.com/@phosphor-icons/web@2.1.1/src/regular/style.css" /></noscript>
</head>

<body>

{HEADER_HTML}

  <!-- ARTICLE HERO -->
  <section style="padding: 130px 0 50px 0; background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #ffffff;">
    <div class="container" style="max-width: 860px; margin: 0 auto;">
      <div class="page-breadcrumb" style="margin-bottom: 18px; color: #94a3b8; font-size: 13px;">
        <a href="index.html" style="color: #94a3b8;">Home</a>
        <i class="ph ph-caret-right"></i>
        <a href="blogs.html" style="color: #94a3b8;">Guides</a>
        <i class="ph ph-caret-right"></i>
        <span style="color: #38bdf8;">{g['category']}</span>
      </div>
      <div style="display: flex; align-items: center; gap: 12px; margin-bottom: 16px;">
        <span style="background: rgba(56, 189, 248, 0.15); border: 1px solid rgba(56, 189, 248, 0.4); color: #38bdf8; font-size: 12px; font-weight: 700; padding: 4px 12px; border-radius: 20px;">
          {g['category']}
        </span>
        <span style="color: #94a3b8; font-size: 13px;"><i class="ph ph-clock"></i> {g['read_time']}</span>
        <span style="color: #94a3b8; font-size: 13px;">&bull; {g['date']}</span>
      </div>
      <h1 style="font-size: clamp(26px, 4vw, 40px); font-weight: 800; line-height: 1.25; margin-bottom: 20px;">
        {html.escape(g['title'])}
      </h1>
      <p style="font-size: 16.5px; line-height: 1.7; color: #cbd5e1; margin: 0;">
        {html.escape(g['lead'])}
      </p>
    </div>
  </section>

  <!-- ARTICLE CONTENT -->
  <article style="padding: 60px 0; background: #ffffff;">
    <div class="container" style="max-width: 860px;">
      <div style="font-size: 16px; line-height: 1.8; color: #334155;">
        <p style="font-size: 17.5px; font-weight: 500; color: #0f172a; border-left: 4px solid #0284c7; padding-left: 18px; margin-bottom: 30px;">
          Businesses across Salem, Coimbatore, Karur, and Tamil Nadu are rapidly moving away from rigid spreadsheets and off-the-shelf software towards tailored, high-speed digital architectures.
        </p>

        <h2 style="font-size: 24px; font-weight: 800; color: #0f172a; margin: 36px 0 16px 0;">1. Understanding the Core Architectural Requirements</h2>
        <p>
          Before investing capital, leadership teams must clarify their exact operational bottleneck. Is your challenge inventory leakage, counter checkout delays, lost sales leads, or compliance audit penalties? A targeted software system built for your specific workflow pays for itself within months.
        </p>

        <h2 style="font-size: 24px; font-weight: 800; color: #0f172a; margin: 36px 0 16px 0;">2. Key Technical Standards to Insist On</h2>
        <ul style="padding-left: 20px; margin-bottom: 24px;">
          <li style="margin-bottom: 10px;"><strong>Sub-Second Loading Speeds:</strong> Every extra second of load time drops conversions by up to 15%. Lightweight, compiled codebases outperform heavy plugin-dependent tools.</li>
          <li style="margin-bottom: 10px;"><strong>Offline-First Resilience:</strong> Essential billing counters and factory shop floors must operate seamlessly even during internet drops.</li>
          <li style="margin-bottom: 10px;"><strong>100% Data Sovereignty:</strong> Your proprietary customer records and sales figures must be encrypted and owned 100% by your enterprise.</li>
          <li style="margin-bottom: 10px;"><strong>Automated Compliance:</strong> Real-time GST E-Way bills, E-Invoicing, and NABH/ISO audit logs built into daily transactions.</li>
        </ul>

        <div style="background: #f0fdf4; border: 1.5px solid #bbf7d0; border-radius: 14px; padding: 24px; margin: 36px 0;">
          <h3 style="font-size: 18px; font-weight: 700; color: #15803d; margin-bottom: 8px; display: flex; align-items: center; gap: 8px;">
            <i class="ph ph-check-circle" style="font-size: 22px;"></i> The I Info Vision Advantage
          </h3>
          <p style="color: #166534; font-size: 14.5px; line-height: 1.6; margin: 0;">
            With headquarters in Salem and deep client deployments across Tamil Nadu, I Info Vision pairs international software engineering standards with direct on-site presence and 24/7 dedicated support.
          </p>
        </div>

        <h2 style="font-size: 24px; font-weight: 800; color: #0f172a; margin: 36px 0 16px 0;">3. Frequently Asked Questions</h2>
        <div class="faq-list" style="margin-top: 20px;">
{faqs_html}        </div>
      </div>
    </div>
  </article>

  <!-- CTA BANNER -->
  <section style="padding: 60px 0; background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%); color: #ffffff; text-align: center;">
    <div class="container" style="max-width: 800px;">
      <h2 style="font-size: 30px; font-weight: 800; margin-bottom: 16px;">Need Expert Technical Guidance for Your Business?</h2>
      <p style="font-size: 16px; color: #e0f2fe; margin-bottom: 28px; line-height: 1.6;">
        Speak directly with our senior software architects. No sales pressure &ndash; just honest, practical technology advice tailored to your scale.
      </p>
      <div style="display: flex; justify-content: center; gap: 14px; flex-wrap: wrap;">
        <a href="contact.html" class="btn" style="background: #ffffff; color: #0369a1; padding: 13px 26px; font-weight: 800; border-radius: 10px; font-size: 14.5px;">
          Contact Our Engineers &rarr;
        </a>
        <a href="https://wa.me/919894480585" target="_blank" class="btn" style="background: #25d366; color: #ffffff; padding: 13px 22px; font-weight: 800; border-radius: 10px; font-size: 14.5px; display: inline-flex; align-items: center; gap: 8px;">
          <i class="ph ph-whatsapp-logo" style="font-size: 18px;"></i> WhatsApp Consultation
        </a>
      </div>
    </div>
  </section>

{FOOTER_HTML}"""

# Generate all pages
created_files = []

for loc in UNIQUE_LOCATIONS:
    filepath = os.path.join(WORKSPACE, loc["filename"])
    content = build_location_page(loc)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    created_files.append(loc["filename"])

for ind in INDUSTRY_DATA:
    filepath = os.path.join(WORKSPACE, ind["filename"])
    content = build_industry_page(ind)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    created_files.append(ind["filename"])

for g in GUIDES_DATA:
    filepath = os.path.join(WORKSPACE, g["filename"])
    content = build_guide_page(g)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    created_files.append(g["filename"])

print(f"Successfully written {len(created_files)} HTML pages!")

# ==================== MASTER DIRECTORY (directory.html) ====================

loc_links = "".join([f'<li><a href="{l["filename"]}" style="color: #0284c7; text-decoration: none; font-weight: 600;">{l["service"]} in {l["city"]}</a></li>\n' for l in UNIQUE_LOCATIONS])
ind_links = "".join([f'<li><a href="{i["filename"]}" style="color: #0284c7; text-decoration: none; font-weight: 600;">{i["name"]}</a></li>\n' for i in INDUSTRY_DATA])
guide_links = "".join([f'<li><a href="{g["filename"]}" style="color: #0284c7; text-decoration: none; font-weight: 600;">{g["title"]}</a></li>\n' for g in GUIDES_DATA])

directory_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>All Services, Locations &amp; Industry Solutions Directory | I Info Vision</title>
  <meta name="description" content="Complete directory of software development, web design, ERP, billing POS solutions, and guides by I Info Vision across Salem, Coimbatore, Karur, Chennai, and Tamil Nadu." />
  <meta name="robots" content="index, follow" />
  <link rel="canonical" href="https://www.iinfovision.com/directory.html" />
  <link rel="icon" type="image/png" href="assets/images/logo.webp" />
  <link rel="stylesheet" href="styles.css?v=2.1" />
  <link rel="stylesheet" href="https://unpkg.com/@phosphor-icons/web@2.1.1/src/regular/style.css" media="print" onload="this.media='all'" />
</head>
<body>
{HEADER_HTML}

  <section class="page-hero" style="padding: 130px 0 50px 0; background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); color: #ffffff; text-align: center;">
    <div class="container">
      <h1 style="font-size: 36px; font-weight: 800; margin-bottom: 12px;">All Services, Locations &amp; Solutions Directory</h1>
      <p style="color: #cbd5e1; font-size: 16px; max-width: 700px; margin: 0 auto;">
        Explore our comprehensive network of regional IT services, industry-specific ERP systems, and technological business guides across Tamil Nadu.
      </p>
    </div>
  </section>

  <section style="padding: 60px 0; background: #ffffff;">
    <div class="container">
      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(320px, 1fr)); gap: 40px;">
        
        <!-- Regional Locations -->
        <div style="background: #f8fafc; border: 1.5px solid #e2e8f0; border-radius: 16px; padding: 30px;">
          <h2 style="font-size: 20px; font-weight: 800; color: #0f172a; margin-bottom: 20px; display: flex; align-items: center; gap: 8px;">
            <i class="ph ph-map-pin" style="color: #0284c7;"></i> Regional City Landing Hubs ({len(UNIQUE_LOCATIONS)})
          </h2>
          <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 12px; font-size: 14.5px;">
{loc_links}          </ul>
        </div>

        <!-- Industry Solutions -->
        <div style="background: #f8fafc; border: 1.5px solid #e2e8f0; border-radius: 16px; padding: 30px;">
          <h2 style="font-size: 20px; font-weight: 800; color: #0f172a; margin-bottom: 20px; display: flex; align-items: center; gap: 8px;">
            <i class="ph ph-cpu" style="color: #0284c7;"></i> Industry Software Solutions ({len(INDUSTRY_DATA)})
          </h2>
          <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 12px; font-size: 14.5px;">
{ind_links}          </ul>
        </div>

        <!-- Business Guides -->
        <div style="background: #f8fafc; border: 1.5px solid #e2e8f0; border-radius: 16px; padding: 30px;">
          <h2 style="font-size: 20px; font-weight: 800; color: #0f172a; margin-bottom: 20px; display: flex; align-items: center; gap: 8px;">
            <i class="ph ph-book-open" style="color: #0284c7;"></i> Technology &amp; Strategy Guides ({len(GUIDES_DATA)})
          </h2>
          <ul style="list-style: none; padding: 0; margin: 0; display: flex; flex-direction: column; gap: 12px; font-size: 14.5px;">
{guide_links}          </ul>
        </div>

      </div>
    </div>
  </section>

{FOOTER_HTML}
"""

with open(os.path.join(WORKSPACE, "directory.html"), "w", encoding="utf-8") as f:
    f.write(directory_html)
print("Created directory.html successfully!")

# ==================== SITEMAP.XML UPDATER ====================

sitemap_path = os.path.join(WORKSPACE, "sitemap.xml")

with open(sitemap_path, "r", encoding="utf-8") as f:
    sitemap_content = f.read()

# Extract existing URLs
existing_urls = set(re.findall(r"<loc>(.*?)</loc>", sitemap_content))
print(f"Existing URLs in sitemap: {len(existing_urls)}")

all_new_urls = [f"https://www.iinfovision.com/{fn}" for fn in created_files]
all_new_urls.append("https://www.iinfovision.com/directory.html")

new_urls_to_add = [u for u in all_new_urls if u not in existing_urls]
print(f"New URLs to add to sitemap.xml: {len(new_urls_to_add)}")

new_xml_entries = ""
for url in new_urls_to_add:
    priority = "0.85" if "guide" not in url else "0.75"
    new_xml_entries += f"""  <url>
    <loc>{url}</loc>
    <lastmod>2026-10-16</lastmod>
    <changefreq>weekly</changefreq>
    <priority>{priority}</priority>
  </url>\n"""

sitemap_content = sitemap_content.replace("</urlset>", new_xml_entries + "</urlset>")

with open(sitemap_path, "w", encoding="utf-8") as f:
    f.write(sitemap_content)

total_urls = len(re.findall(r"<loc>(.*?)</loc>", sitemap_content))
print(f"FINAL TOTAL URLS IN sitemap.xml: {total_urls} URLs!")
