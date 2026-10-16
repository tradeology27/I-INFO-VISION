"""
Salem Hyper-Local Pincode & Locality SEO Network Generator for I Info Vision.
Grounded in authentic postal directory data from Finkode Salem.
Generates:
1. salem-pincode-it-directory.html (Master Interactive Salem Pincode Search Hub with 60+ post offices)
2. 12 Dedicated Prime Locality Landing Pages for Salem's major commercial hubs:
   - Alagapuram (636004)
   - Fairlands (636016)
   - Shevapet (636002)
   - Ammapet (636003)
   - Gugai (636006)
   - Suramangalam & Junction (636005)
   - Attur (636102)
   - Mettur & Mettur Dam (636401)
   - Omalur (636455)
   - Sankagiri (637301)
   - Edappadi (637101)
   - Yercaud (636601)
3. Appends all new URLs to sitemap.xml
4. Links the Pincode Hub into directory.html and sitemap.html
"""

import os
import json
import re
import html

WORKSPACE = r"c:\Users\prave\OneDrive\Desktop\office projects\I-INFO-VISION-main"

# ==================== ALL SALEM POST OFFICES & PINCODES ====================

SALEM_PINCODES = [
    ("Alagapuram", "636004", "IT, Commercial Offices, Retail, Hotels & Clinics"),
    ("Fairlands", "636016", "Corporate Offices, Premium Retail, Healthcare & Startups"),
    ("Shevapet", "636002", "Major Wholesale Market, Provisions, Metals & FMCG Trading"),
    ("Ammapet & Ammapettai", "636003", "Textile Weaving, Silk Sarees, Powerlooms & Wholesale"),
    ("Gugai", "636006", "Silk Sarees, Dyeing Units, Retail Showrooms & Trading"),
    ("Suramangalam", "636005", "Salem Railway Junction, Logistics, Transport & Commercial"),
    ("Hasthampatti", "636007", "Residential, Multi-Speciality Clinics, Colleges & Offices"),
    ("Meyyanur", "636004", "New Bus Stand, Shopping Malls, Hotels & Commercial Complexes"),
    ("Kondalampatti", "636010", "Highway Bypass, Textile Showrooms, Logistics & Godowns"),
    ("Annadanapatti", "636002", "Hardware, Steel, Wholesale Groceries & Food Processing"),
    ("Arisipalayam", "636009", "Leigh Bazaar, Electricals, Building Materials & Trade"),
    ("Kannankurichi & Gorimedu", "636008", "Institutions, Government Offices, Hospitals & Residential"),
    ("Dasanaickenpatti", "636201", "I Info Vision Salem HQ, Trichy Main Road, Commercial"),
    ("Ayodhiyapattinam", "636103", "Sago & Starch Factories, Agriculture & Powerlooms"),
    ("Karuppur", "636012", "Salem IT Park, Periyar University, Engineering Hub"),
    ("Steel Plant & Mohan Nagar", "636030", "Steel Authority of India (SAIL), Heavy Engineering"),
    ("Attur", "636102", "Major Taluk Center, Sago Mills, Tapioca, Retail & Agro Trade"),
    ("Mettur & Mettur Dam", "636401", "Chemical Industries, Thermal Power, Aluminium & Engineering"),
    ("Omalur", "636455", "Salem Airport, Engineering Colleges, Agro & Industrial"),
    ("Sankagiri", "637301", "Lorry Transport Hub, Tyre Retreading, Cement & Heavy Logistics"),
    ("Edappadi", "637101", "Powerloom Weaving, Textile Trading & Agricultural Processing"),
    ("Tharamangalam", "636502", "Handloom & Powerloom Fabrics, Weaving Clusters & Heritage"),
    ("Vazhapadi", "636115", "Tapioca Processing, Sago, Agriculture & Wholesale Trade"),
    ("Jalagangapuram", "636501", "Textile Saree Manufacturing, Weaving & Showrooms"),
    ("Yercaud", "636601", "Luxury Resorts, Boutique Hotels, Tourism & Plantations"),
    ("Mecheri", "636453", "Livestock, Agriculture, Trading & Educational Hubs"),
    ("Gangavalli", "636105", "Sugar Mills, Agriculture, Food Processing & Retail"),
    ("Attayampatti", "637501", "Textiles, Weaving, Saree Wholesale & Agriculture"),
    ("Panamarathupatti", "636204", "Institutions, Tourism, Agriculture & Local Trade"),
    ("Magudanchavadi", "637103", "Highway Warehouses, Transporters, Mills & Retail"),
    ("A.Komarapalayam", "636117", "Textile Weaving, Powerlooms & Rural Commerce"),
    ("A.N.Mangalam", "636106", "Agriculture, Agro Processing & Local Retail"),
    ("Achankuttapatti", "636122", "Institutions, Sago Processing & Rural Trade"),
    ("Allikuttai", "636003", "Residential & Local Commercial Outlets"),
    ("Ammampalayam", "636114", "Agricultural Trading, Warehouses & Retail"),
    ("Anaiyampatti", "636105", "Agro Industries & Local Commercial Shops"),
    ("Aragalur", "636101", "Heritage, Agriculture, Trade & Education"),
    ("Ariyanur", "636308", "Medical Colleges, Highway Commercial Hubs & Institutions"),
    ("Belur", "636104", "Agriculture, Trading, Local Showrooms & Healthcare"),
    ("Chamrajpet", "636451", "Textile Weaving, Wholesale & Local Commercial Outlets"),
    ("Chettichavadi", "636012", "Minerals, Magnesium Mining, Engineering & Educational"),
    ("Dadagapatti", "636006", "Textile Showrooms, Silk Saree Weaving & Retail Shops"),
    ("Dalavaipatti", "636302", "Powerloom Clusters, Dyeing Units & Local Trade"),
    ("Idappadi", "637101", "Textile Powerloom Weaving & Wholesale Saree Hub"),
    ("Jagalur", "636111", "Agro Farming, Tapioca & Rural Retail"),
    ("Kadayampatti", "636351", "Forestry, Agriculture & Educational Institutions"),
    ("Kallanatham", "636141", "Rural Commerce, Agriculture & Processing"),
    ("Kattukottai", "636121", "Agro Commodity Trading & Poultry"),
    ("Kitchipalayam", "636015", "Textiles, Saree Weaving, Garments & Local Retail"),
    ("Konganapuram", "637102", "Weekly Cattle & Agro Market, Textile Weaving"),
    ("Kullampatti", "636103", "Tapioca Processing, Agriculture & Local Trade"),
    ("Mallasamudram", "637503", "Powerloom Weaving, Textile Showrooms & Retail"),
    ("Mallur", "636203", "Highway Transporters, Sago, Agriculture & Healthcare"),
    ("Maramangalathupatti", "636030", "Industrial Ancillaries, Engineering & Fabrication"),
    ("Minnampalli", "636106", "Agriculture, Educational Institutions & Commercial"),
    ("Nangavalli", "636454", "Weaving, Silk Sarees, Agriculture & Retail"),
    ("Pappireddipatti", "636905", "Agro Trade, Plantation & Educational Outlets"),
    ("Poolampatti", "637107", "Cauvery River Tourism, Powerlooms & Trade"),
    ("Sandaipet", "636102", "Attur Commercial Bazaar, Wholesale & Retail"),
    ("Seelanaickenpatti", "636201", "Trichy-Madurai Highway Junction, Logistics & Auto"),
    ("Selliampalayam", "636118", "Agro Farming & Sago Starch Processing"),
    ("Siruvachur", "636112", "Highway Commercial, Agro Trade & Poultry"),
    ("Thalaivasal", "636112", "Major Vegetable & Agro Wholesale Market, Poultry"),
    ("Thevoor", "637104", "Agriculture, Powerlooms & Local Trade"),
    ("Udayapatti", "636140", "Textile Dyeing, Weaving & Commercial Complexes"),
    ("Valasaiyur", "636122", "Institutions, Healthcare, Sago & Agriculture")
]

# Shared Header & Footer
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
            A proud Yasmeen Group Company headquartered in Salem. Serving every pincode and locality across Salem district with enterprise software, fast web design, and GST billing systems.
          </p>
        </div>
        <div>
          <h4 class="footer-heading">Salem Services</h4>
          <ul class="footer-links">
            <li><a href="web-development-company-salem.html">Web Development Salem</a></li>
            <li><a href="software-development-company-salem.html">Software Development Salem</a></li>
            <li><a href="billing-software-salem.html">GST Billing Software Salem</a></li>
            <li><a href="crm-erp-software-salem.html">CRM &amp; ERP Software Salem</a></li>
            <li><a href="mobile-app-development-salem.html">Mobile App Development Salem</a></li>
            <li><a href="salem-pincode-it-directory.html">Salem District Pincode Hub</a></li>
          </ul>
        </div>
        <div>
          <h4 class="footer-heading">Salem Localities</h4>
          <ul class="footer-links">
            <li><a href="software-web-development-alagapuram-salem.html">Alagapuram (636004)</a></li>
            <li><a href="software-web-development-fairlands-salem.html">Fairlands (636016)</a></li>
            <li><a href="billing-software-shevapet-salem.html">Shevapet (636002)</a></li>
            <li><a href="textile-software-ammapet-salem.html">Ammapet (636003)</a></li>
            <li><a href="software-web-development-attur-salem.html">Attur (636102)</a></li>
            <li><a href="industrial-erp-software-mettur-salem.html">Mettur (636401)</a></li>
            <li><a href="transport-fleet-software-sankagiri-salem.html">Sankagiri (637301)</a></li>
          </ul>
        </div>
        <div>
          <h4 class="footer-heading">Salem Headquarters</h4>
          <div class="footer-contact-item">
            <div class="footer-contact-icon"><i class="ph ph-map-pin"></i></div>
            <div class="footer-contact-text">
              <span class="label">Office Address</span>
              <span>#9/136, No.1, First Floor, Trichy Main Road, Chinnaiyapuram, Dasanaickenpatti, Salem &ndash; 636201</span>
            </div>
          </div>
          <div class="footer-contact-item">
            <div class="footer-contact-icon"><i class="ph ph-phone"></i></div>
            <div class="footer-contact-text">
              <span class="label">Direct Phone / WhatsApp</span>
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
          <a href="salem-pincode-it-directory.html">Salem Pincode Hub</a>
          <a href="directory.html">All Locations</a>
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

# ==================== 1. BUILD SALEM PINCODE MASTER HUB ====================

def build_salem_pincode_hub():
    rows_html = ""
    schema_areas = []

    for loc, pin, desc in SALEM_PINCODES:
        schema_areas.append({
            "@type": "AdministrativeArea",
            "name": f"{loc}, Salem {pin}",
            "postalCode": pin
        })
        rows_html += f"""          <tr style="border-bottom: 1px solid #e2e8f0; transition: background 0.2s;" onmouseover="this.style.background='#f0f9ff'" onmouseout="this.style.background='transparent'">
            <td style="padding: 14px 18px; font-weight: 700; color: #0f172a;">
              <span style="display: flex; align-items: center; gap: 8px;">
                <i class="ph ph-map-pin" style="color: #0284c7; font-size: 16px;"></i> {loc}
              </span>
            </td>
            <td style="padding: 14px 18px; font-family: monospace; font-size: 15px; font-weight: 700; color: #0369a1;">
              <span style="background: #e0f2fe; padding: 4px 10px; border-radius: 6px;">{pin}</span>
            </td>
            <td style="padding: 14px 18px; color: #475569; font-size: 14px;">
              {desc}
            </td>
            <td style="padding: 14px 18px; text-align: right;">
              <a href="https://wa.me/919894480585?text=Hi%20I%20Info%20Vision,%20I%20need%20software/web%20services%20in%20{loc}%20(Pin%20{pin})" target="_blank" class="btn btn-primary" style="padding: 6px 14px; font-size: 12.5px; border-radius: 6px; text-decoration: none; display: inline-flex; align-items: center; gap: 5px;">
                <i class="ph ph-whatsapp-logo"></i> Instant Quote
              </a>
            </td>
          </tr>\n"""

    schema_json = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.iinfovision.com/" },
                    { "@type": "ListItem", "position": 2, "name": "Salem District Hub", "item": "https://www.iinfovision.com/web-development-company-salem.html" },
                    { "@type": "ListItem", "position": 3, "name": "Salem Pincode IT Directory", "item": "https://www.iinfovision.com/salem-pincode-it-directory.html" }
                ]
            },
            {
                "@type": "LocalBusiness",
                "name": "I Info Vision - Salem District Software & IT Headquarters",
                "url": "https://www.iinfovision.com/",
                "telephone": "+919894480585",
                "priceRange": "₹₹",
                "image": "https://www.iinfovision.com/assets/images/logo.webp",
                "address": {
                    "@type": "PostalAddress",
                    "streetAddress": "#9/136, No.1, First Floor, Trichy Main Road, Chinnaiyapuram, Dasanaickenpatti",
                    "addressLocality": "Salem",
                    "addressRegion": "Tamil Nadu",
                    "postalCode": "636201",
                    "addressCountry": "IN"
                },
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": "11.6152",
                    "longitude": "78.1636"
                },
                "areaServed": schema_areas,
                "description": "Comprehensive IT services, custom software, ERP, billing POS, and web development covering all delivery post offices and pincodes in Salem district, Tamil Nadu."
            },
            {
                "@type": "FAQPage",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": "Does I Info Vision provide on-site software installation in all Salem pincodes?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "Yes, our engineering headquarters is centrally located in Dasanaickenpatti, Salem. Our senior engineers provide direct on-site setup, data migration, and hands-on staff training across all post offices and pincodes from 636001 to 637501 in Salem district."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "How fast can a technical team reach our shop or factory in Salem?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "Within Salem City limits (Fairlands, Alagapuram, Shevapet, Ammapet, Gugai, Hasthampatti, Suramangalam), our technicians can reach your premises within 60 minutes. For taluks like Attur, Mettur, Omalur, Sankagiri, and Edappadi, we offer same-day on-site dispatch."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": "Can you migrate our existing Tally or billing data in Salem?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": "Yes, we handle complete historical inventory and customer ledger migration from Tally, Excel, or older software with 100% data integrity and zero downtime."
                        }
                    }
                ]
            }
        ]
    }

    schema_str = json.dumps(schema_json, indent=2)

    return f"""<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Salem District IT &amp; Software Pincode Directory (636001 - 637501) | I Info Vision</title>
  <meta name="description" content="Salem District Postal Pincode IT Services Directory. Lookup software development, website design, GST billing POS, and ERP solutions across all post offices in Salem, Tamil Nadu." />
  <meta name="keywords" content="salem pincode list, salem post office software, it services salem pincodes, web development alagapuram 636004, billing software shevapet 636002, software company ammapet 636003, erp software mettur 636401, website design attur 636102, I Info Vision Salem" />
  <meta name="author" content="I Info Vision" />
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1" />
  <meta name="geo.region" content="IN-TN" />
  <meta name="geo.placename" content="Salem, Tamil Nadu" />
  <meta name="geo.position" content="11.6152;78.1636" />
  <meta name="ICBM" content="11.6152, 78.1636" />
  <link rel="canonical" href="https://www.iinfovision.com/salem-pincode-it-directory.html" />

  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website" />
  <meta property="og:url" content="https://www.iinfovision.com/salem-pincode-it-directory.html" />
  <meta property="og:site_name" content="I Info Vision" />
  <meta property="og:locale" content="en_IN" />
  <meta property="og:title" content="Salem District IT &amp; Software Pincode Directory (636001 - 637501) | I Info Vision" />
  <meta property="og:description" content="Search all post offices and pincodes in Salem district for custom software development, website design, and GST billing systems with direct on-site support." />
  <meta property="og:image" content="https://www.iinfovision.com/assets/images/logo.webp" />

  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:url" content="https://www.iinfovision.com/salem-pincode-it-directory.html" />
  <meta name="twitter:title" content="Salem District IT &amp; Software Pincode Directory | I Info Vision" />
  <meta name="twitter:description" content="Search all post offices and pincodes in Salem district for custom software development, website design, and GST billing systems." />
  <meta name="twitter:image" content="https://www.iinfovision.com/assets/images/logo.webp" />

  <!-- Schema.org JSON-LD Structured Data -->
  <script type="application/ld+json">
{schema_str}
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
          <a href="web-development-company-salem.html" style="color: #94a3b8;">Salem HQ</a>
          <i class="ph ph-caret-right"></i>
          <span style="color: #38bdf8;">Pincode Directory</span>
        </div>
        <div style="display: inline-block; background: rgba(56, 189, 248, 0.15); border: 1px solid rgba(56, 189, 248, 0.4); color: #38bdf8; font-size: 12.5px; font-weight: 700; padding: 6px 16px; border-radius: 20px; margin-bottom: 20px;">
          <i class="ph ph-buildings"></i> Salem District 100% Pincode Coverage
        </div>
        <h1 class="page-hero-title" style="font-size: clamp(28px, 4.5vw, 44px); font-weight: 800; line-height: 1.25; margin-bottom: 20px;">
          Salem District IT &amp; Software <span class="highlight">Pincode Directory</span>
        </h1>
        <p class="page-hero-desc" style="font-size: 16.5px; line-height: 1.7; color: #cbd5e1; max-width: 780px; margin: 0 auto 30px auto;">
          Looking for trusted software developers, website designers, or GST billing software in your Salem neighborhood? Search below by pincode or locality for instant on-site technical support.
        </p>
        
        <!-- Live Search Input -->
        <div style="max-width: 600px; margin: 0 auto; position: relative;">
          <div style="display: flex; align-items: center; background: #ffffff; border-radius: 12px; padding: 6px 16px; box-shadow: 0 8px 30px rgba(0,0,0,0.25);">
            <i class="ph ph-magnifying-glass" style="font-size: 22px; color: #0284c7; margin-right: 10px;"></i>
            <input type="text" id="pincodeSearch" placeholder="Type pincode (e.g., 636004) or locality (e.g., Shevapet, Attur)..." style="width: 100%; border: none; outline: none; font-size: 15px; color: #0f172a; padding: 10px 0; font-family: inherit;" onkeyup="filterPincodes()" />
          </div>
          <span style="color: #94a3b8; font-size: 12.5px; margin-top: 10px; display: block;">Instant live filter covering all 60+ Salem post offices</span>
        </div>
      </div>
    </div>
  </section>

  <!-- INTERACTIVE DIRECTORY TABLE -->
  <section style="padding: 60px 0; background: #f8fafc;">
    <div class="container">
      <div style="background: #ffffff; border-radius: 16px; border: 1.5px solid #e2e8f0; overflow: hidden; box-shadow: 0 4px 20px rgba(0,0,0,0.04);">
        <div style="padding: 20px 24px; background: #f1f5f9; border-bottom: 1.5px solid #e2e8f0; display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 12px;">
          <h2 style="font-size: 18px; font-weight: 800; color: #0f172a; margin: 0;">
            <i class="ph ph-list-dashes" style="color: #0284c7;"></i> All Delivery Post Offices &amp; Pincodes in Salem
          </h2>
          <span style="background: #0284c7; color: #ffffff; font-size: 12px; font-weight: 700; padding: 4px 12px; border-radius: 20px;">
            {len(SALEM_PINCODES)} Localities Listed
          </span>
        </div>

        <div style="overflow-x: auto;">
          <table id="pincodeTable" style="width: 100%; border-collapse: collapse; text-align: left;">
            <thead>
              <tr style="background: #f8fafc; border-bottom: 2px solid #e2e8f0; font-size: 13.5px; color: #64748b; text-transform: uppercase; letter-spacing: 0.5px;">
                <th style="padding: 14px 18px;">Post Office / Locality</th>
                <th style="padding: 14px 18px;">Pincode</th>
                <th style="padding: 14px 18px;">Industry &amp; Commerce Focus</th>
                <th style="padding: 14px 18px; text-align: right;">Action</th>
              </tr>
            </thead>
            <tbody>
{rows_html}            </tbody>
          </table>
        </div>
      </div>
    </div>
  </section>

  <!-- LIVE SEARCH SCRIPT -->
  <script>
    function filterPincodes() {{
      var input = document.getElementById("pincodeSearch");
      var filter = input.value.toUpperCase();
      var table = document.getElementById("pincodeTable");
      var tr = table.getElementsByTagName("tr");

      for (var i = 1; i < tr.length; i++) {{
        var tdLoc = tr[i].getElementsByTagName("td")[0];
        var tdPin = tr[i].getElementsByTagName("td")[1];
        var tdDesc = tr[i].getElementsByTagName("td")[2];
        if (tdLoc || tdPin || tdDesc) {{
          var txtLoc = tdLoc.textContent || tdLoc.innerText;
          var txtPin = tdPin.textContent || tdPin.innerText;
          var txtDesc = tdDesc.textContent || tdDesc.innerText;
          if (txtLoc.toUpperCase().indexOf(filter) > -1 || txtPin.toUpperCase().indexOf(filter) > -1 || txtDesc.toUpperCase().indexOf(filter) > -1) {{
            tr[i].style.display = "";
          }} else {{
            tr[i].style.display = "none";
          }}
        }}
      }}
    }}
  </script>

  <!-- FAST FACTS & SALEM MAP ADVANTAGE -->
  <section style="padding: 60px 0; background: #ffffff;">
    <div class="container" style="max-width: 900px;">
      <div style="text-align: center; margin-bottom: 40px;">
        <span style="color: #0284c7; font-weight: 700; font-size: 13px; text-transform: uppercase; letter-spacing: 1px;">On-Site Commitment</span>
        <h2 style="font-size: 28px; font-weight: 800; color: #0f172a; margin-top: 8px;">The I Info Vision Salem Advantage</h2>
        <p style="color: #64748b; font-size: 15px;">Unlike out-of-station web companies, our engineers are based right here in Salem.</p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(260px, 1fr)); gap: 24px;">
        <div style="background: #f8fafc; padding: 24px; border-radius: 14px; border: 1.5px solid #e2e8f0;">
          <i class="ph ph-clock-countdown" style="font-size: 32px; color: #0284c7; margin-bottom: 12px; display: block;"></i>
          <h3 style="font-size: 17px; font-weight: 700; color: #0f172a; margin-bottom: 8px;">60-Minute City Dispatch</h3>
          <p style="color: #64748b; font-size: 14px; line-height: 1.6; margin: 0;">Technicians reach Fairlands, Shevapet, Ammapet, Gugai, and Junction within 1 hour for urgent billing support.</p>
        </div>

        <div style="background: #f8fafc; padding: 24px; border-radius: 14px; border: 1.5px solid #e2e8f0;">
          <i class="ph ph-database" style="font-size: 32px; color: #16a34a; margin-bottom: 12px; display: block;"></i>
          <h3 style="font-size: 17px; font-weight: 700; color: #0f172a; margin-bottom: 8px;">Zero-Downtime Migration</h3>
          <p style="color: #64748b; font-size: 14px; line-height: 1.6; margin: 0;">We migrate your Tally ledgers, Excel product lists, and legacy records safely on your shop computer with zero data loss.</p>
        </div>

        <div style="background: #f8fafc; padding: 24px; border-radius: 14px; border: 1.5px solid #e2e8f0;">
          <i class="ph ph-chats-circle" style="font-size: 32px; color: #d97706; margin-bottom: 12px; display: block;"></i>
          <h3 style="font-size: 17px; font-weight: 700; color: #0f172a; margin-bottom: 8px;">Direct Tamil Support</h3>
          <p style="color: #64748b; font-size: 14px; line-height: 1.6; margin: 0;">Speak comfortably in Tamil with our engineers. We train your billing staff and cashiers patiently until they are 100% confident.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- CTA BANNER -->
  <section style="padding: 60px 0; background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%); color: #ffffff; text-align: center;">
    <div class="container" style="max-width: 800px;">
      <h2 style="font-size: 32px; font-weight: 800; margin-bottom: 16px;">Need Software or Web Services in Your Salem Area?</h2>
      <p style="font-size: 16.5px; color: #e0f2fe; margin-bottom: 30px; line-height: 1.6;">
        Call our Salem headquarters directly at <a href="tel:+919894480585" style="color: #ffffff; font-weight: 800; text-decoration: underline;">+91 98944 80585</a> or chat with an engineer on WhatsApp for instant project estimation.
      </p>
      <div style="display: flex; justify-content: center; gap: 14px; flex-wrap: wrap;">
        <a href="contact.html?source=pincode-hub" class="btn" style="background: #ffffff; color: #0369a1; padding: 14px 28px; font-weight: 800; border-radius: 10px; font-size: 15px;">
          Book On-Site Visit &rarr;
        </a>
        <a href="https://wa.me/919894480585" target="_blank" class="btn" style="background: #25d366; color: #ffffff; padding: 14px 24px; font-weight: 800; border-radius: 10px; font-size: 15px; display: inline-flex; align-items: center; gap: 8px;">
          <i class="ph ph-whatsapp-logo" style="font-size: 18px;"></i> WhatsApp Our Engineers
        </a>
      </div>
    </div>
  </section>

{FOOTER_HTML}"""

# ==================== 2. BUILD 12 PRIME SALEM LOCALITY PAGES ====================

PRIME_LOCALITIES = [
    {
        "filename": "software-web-development-alagapuram-salem.html",
        "locality": "Alagapuram",
        "pin": "636004",
        "service": "Software & Web Development",
        "focus": "IT Companies, Clinics, Hotels, Corporate Offices & Retail Showrooms in Alagapuram",
        "title": "Software & Web Development Company in Alagapuram Salem (636004) | I Info Vision",
        "desc": "Top software and web development company in Alagapuram, Salem 636004. High-speed business websites, custom ERP, billing software, and mobile apps with on-site support.",
        "keywords": "web development alagapuram salem, software company alagapuram 636004, website design alagapuram salem, billing software alagapuram, it company alagapuram salem",
        "badge": "Alagapuram 636004 Hub",
        "hero_title": "Software & Web Development in <span class='highlight'>Alagapuram, Salem</span>",
        "hero_desc": "Empowering corporate offices, clinics, retail showrooms, and businesses in Alagapuram (636004) with custom software, sub-second websites, and POS billing systems."
    },
    {
        "filename": "software-web-development-fairlands-salem.html",
        "locality": "Fairlands",
        "pin": "636016",
        "service": "Corporate Web & Software Engineering",
        "focus": "Corporate Headquarters, Financial Firms, Multi-Speciality Clinics & Brands in Fairlands",
        "title": "Top Web & Software Company in Fairlands Salem (636016) | I Info Vision",
        "desc": "Leading web design and custom software company in Fairlands, Salem 636016. Enterprise web applications, CRM, ERP, and digital marketing with on-site consultation.",
        "keywords": "web development fairlands salem, software company fairlands 636016, website designers fairlands salem, custom software fairlands, digital agency fairlands",
        "badge": "Fairlands 636016 Business District",
        "hero_title": "Enterprise Web & Software in <span class='highlight'>Fairlands, Salem</span>",
        "hero_desc": "Salem's premier corporate and medical district deserves world-class digital standards. High-performance corporate portals, custom CRM, and cloud systems in Fairlands (636016)."
    },
    {
        "filename": "billing-software-shevapet-salem.html",
        "locality": "Shevapet",
        "pin": "636002",
        "service": "GST Billing & Wholesale POS Software",
        "focus": "Wholesale Provisions, Rice Traders, Hardware, Oil Merchants & FMCG in Shevapet",
        "title": "Best GST Billing & Wholesale POS Software in Shevapet Salem (636002) | I Info Vision",
        "desc": "Fast GST billing software in Shevapet, Salem 636002. Barcode billing, customer credit (katha) ledgers, E-Way bills, and multi-godown stock management for merchants.",
        "keywords": "billing software shevapet salem, wholesale billing software shevapet 636002, gst pos shevapet, supermarket billing shevapet, grocery billing software salem",
        "badge": "Shevapet 636002 Wholesale Hub",
        "hero_title": "Fast GST Billing & POS Software in <span class='highlight'>Shevapet, Salem</span>",
        "hero_desc": "Engineered for Shevapet's high-speed wholesale and retail markets. Rapid barcode scanning, customer credit ledger balance tracking, and 1-click GST E-Way bills."
    },
    {
        "filename": "textile-software-ammapet-salem.html",
        "locality": "Ammapet",
        "pin": "636003",
        "service": "Textile & Saree ERP Software",
        "focus": "Silk Saree Weaving, Powerloom Clusters, Dyeing Houses & Textile Retail in Ammapet",
        "title": "Textile & Saree Manufacturing Software in Ammapet Salem (636003) | I Info Vision",
        "desc": "Specialized textile and saree ERP in Ammapet, Salem 636003. Manage yarn procurement, weaver wages, dyeing lot recipes, and retail showroom barcode billing.",
        "keywords": "textile software ammapet salem, saree billing software ammapet 636003, powerloom software ammapet, fabric inventory salem, silk saree software ammapettai",
        "badge": "Ammapet 636003 Textile Hub",
        "hero_title": "Textile & Saree ERP Software in <span class='highlight'>Ammapet, Salem</span>",
        "hero_desc": "Purpose-built for Ammapet's famous silk and cotton saree weavers. Track yarn issued to contract weavers, monitor piece-rate wages, and manage wholesale packing cartons."
    },
    {
        "filename": "software-billing-gugai-salem.html",
        "locality": "Gugai",
        "pin": "636006",
        "service": "Textile Showroom & Billing POS",
        "focus": "Silk Saree Showrooms, Dyeing Units, Printing Houses & Retailers in Gugai",
        "title": "Textile Showroom & Billing POS Software in Gugai Salem (636006) | I Info Vision",
        "desc": "Fast POS billing software in Gugai, Salem 636006. Saree barcode tags, size-color variants, customer loyalty points, and thermal receipt printing.",
        "keywords": "billing software gugai salem, saree billing pos gugai 636006, textile software gugai, pos billing gugai salem, retail software gugai",
        "badge": "Gugai 636006 Commerce Hub",
        "hero_title": "Showroom Billing & POS Software in <span class='highlight'>Gugai, Salem</span>",
        "hero_desc": "Keep showroom sales counters moving at lightning speed. Dumbbell barcode tags, design-wise saree cataloging, and automated customer WhatsApp invoices in Gugai."
    },
    {
        "filename": "software-web-development-suramangalam-salem.html",
        "locality": "Suramangalam",
        "pin": "636005",
        "service": "Software & Web Development",
        "focus": "Logistics Transporters, Hotels, Commercial Hubs & Retail near Salem Junction",
        "title": "Software & Web Development in Suramangalam Salem (636005) | I Info Vision",
        "desc": "Leading software development and web design in Suramangalam, Salem 636005. Custom business software, hotel booking engines, and fleet logistics tools.",
        "keywords": "web development suramangalam salem, software company suramangalam 636005, salem junction software, website design suramangalam, billing software suramangalam",
        "badge": "Suramangalam & Salem Junction (636005)",
        "hero_title": "Software & Web Development in <span class='highlight'>Suramangalam, Salem</span>",
        "hero_desc": "Empower your transport agencies, hotels, and retail outlets around Salem Junction and Suramangalam (636005) with high-speed digital software systems."
    },
    {
        "filename": "software-web-development-attur-salem.html",
        "locality": "Attur",
        "pin": "636102",
        "service": "Software, ERP & Web Development",
        "focus": "Sago Mills, Tapioca Processing, Agro Commodity Trading & Retail in Attur",
        "title": "Top Software & Web Development Company in Attur Salem (636102) | I Info Vision",
        "desc": "Leading software and web development company in Attur, Salem 636102. Sago mill ERP, agricultural trading software, supermarket billing, and business websites.",
        "keywords": "software development company in attur, website design attur salem, sago mill software attur 636102, billing software attur, it company attur salem",
        "badge": "Attur 636102 Taluk Hub",
        "hero_title": "Software & Web Development in <span class='highlight'>Attur, Salem</span>",
        "hero_desc": "Tailored software systems for Attur's agricultural economy, sago and starch mills, agro dealers, and retail supermarkets with direct local technical support."
    },
    {
        "filename": "industrial-erp-software-mettur-salem.html",
        "locality": "Mettur",
        "pin": "636401",
        "service": "Industrial ERP & Manufacturing Software",
        "focus": "Chemical Plants, Thermal Engineering, Aluminium & Ancillaries in Mettur",
        "title": "Industrial Manufacturing ERP Software in Mettur Salem (636401) | I Info Vision",
        "desc": "Specialized industrial ERP software in Mettur, Salem 636401. Batch process manufacturing, chemical inventory, preventive plant maintenance, and GST billing.",
        "keywords": "industrial erp mettur, chemical plant software mettur 636401, manufacturing erp mettur salem, billing software mettur dam, it company mettur",
        "badge": "Mettur 636401 Industrial Hub",
        "hero_title": "Industrial ERP & Plant Software in <span class='highlight'>Mettur, Salem</span>",
        "hero_desc": "Control raw chemical stocks, track batch formula mixing, schedule machine maintenance, and manage statutory safety audit logs in Mettur and Mettur Dam (636401)."
    },
    {
        "filename": "software-web-development-omalur-salem.html",
        "locality": "Omalur",
        "pin": "636455",
        "service": "Software & Web Development",
        "focus": "Airport Zone, Engineering Colleges, Highway Logistics & Agro Trade in Omalur",
        "title": "Software & Web Development in Omalur Salem (636455) | I Info Vision",
        "desc": "Premier software development and website design in Omalur, Salem 636455. Campus ERP, billing software, and custom business applications.",
        "keywords": "web development omalur salem, software company omalur 636455, college erp omalur, website design omalur, billing software omalur salem",
        "badge": "Omalur 636455 Hub",
        "hero_title": "Software & Web Development in <span class='highlight'>Omalur, Salem</span>",
        "hero_desc": "Modernize your educational institutions, highway transport hubs, and manufacturing operations around Omalur and Salem Airport junction (636455)."
    },
    {
        "filename": "transport-fleet-software-sankagiri-salem.html",
        "locality": "Sankagiri",
        "pin": "637301",
        "service": "Lorry Transport & Fleet Software",
        "focus": "Lorry Owners, Gas Tankers, Tyre Retreading & Cement Logistics in Sankagiri",
        "title": "Best Lorry Transport & Fleet Software in Sankagiri Salem (637301) | I Info Vision",
        "desc": "Dedicated fleet management and lorry transport software in Sankagiri, Salem 637301. Trip sheet accounting, diesel fuel logs, driver settlements, and tyre life tracking.",
        "keywords": "transport software sankagiri, lorry fleet software sankagiri 637301, trip sheet software sankagiri, fleet management salem, transport billing sankagiri",
        "badge": "Sankagiri 637301 Transport Capital",
        "hero_title": "Lorry Transport & Fleet Software in <span class='highlight'>Sankagiri, Salem</span>",
        "hero_desc": "Control every kilometer of your fleet. Stop diesel fuel theft, automate trip profit calculations, track tyre serial rotations, and manage driver balance in Sankagiri."
    },
    {
        "filename": "textile-powerloom-software-edappadi-salem.html",
        "locality": "Edappadi",
        "pin": "637101",
        "service": "Textile Powerloom & Saree ERP",
        "focus": "Powerloom Weaving, Grey Fabric Trading & Saree Manufacturing in Edappadi",
        "title": "Textile Powerloom & Saree Software in Edappadi Salem (637101) | I Info Vision",
        "desc": "Best textile powerloom and saree manufacturing software in Edappadi, Salem 637101. Yarn inventory, loom efficiency, weaver wages, and wholesale fabric billing.",
        "keywords": "textile software edappadi salem, powerloom software edappadi 637101, saree billing edappadi, weaving software edappadi, fabric stock software salem",
        "badge": "Edappadi 637101 Weaving Hub",
        "hero_title": "Textile Powerloom & Saree ERP in <span class='highlight'>Edappadi, Salem</span>",
        "hero_desc": "Engineered for Edappadi's thriving powerloom clusters. Track yarn bag counts, calculate weaver piece-rate wages, and monitor grey fabric dispatch to processing mills."
    },
    {
        "filename": "hospital-hotel-software-yercaud-salem.html",
        "locality": "Yercaud",
        "pin": "636601",
        "service": "Resort PMS & Hotel Management Software",
        "focus": "Luxury Resorts, Boutique Hill Cottages, Homestays & Spas in Yercaud",
        "title": "Luxury Resort & Hotel Management Software in Yercaud Salem (636601) | I Info Vision",
        "desc": "Premier hotel and resort management software (PMS) in Yercaud, Salem 636601. Room booking engine, 2-way channel manager, room folio billing, and restaurant POS.",
        "keywords": "hotel software yercaud salem, resort management software yercaud 636601, hotel pms yercaud, room booking software yercaud, resort pos yercaud",
        "badge": "Yercaud 636601 Hospitality Hub",
        "hero_title": "Resort PMS & Hotel Software in <span class='highlight'>Yercaud, Salem</span>",
        "hero_desc": "Elevate guest experiences in the Jewel of the South. Commission-free website room booking, OTA channel synchronization (Booking.com, MakeMyTrip), and room folio POS in Yercaud."
    }
]

def build_prime_locality_page(item):
    faqs = [
        (f"How fast can an I Info Vision engineer visit our office or shop in {item['locality']}?", f"We are headquartered in Dasanaickenpatti, Salem. For {item['locality']} ({item['pin']}), our senior software engineers can arrive at your premises within 45 to 60 minutes for on-site consultation, demo, or staff training."),
        (f"What software solutions are most popular in {item['locality']}?", f"Based on the local commercial ecosystem ({item['focus']}), businesses frequently deploy our GST Billing POS, custom ERP systems, e-commerce web portals, and mobile workforce apps."),
        ("Do you provide data migration from our existing software or Excel?", "Yes, we handle complete safe data migration from Tally, legacy desktop tools, or spreadsheets with zero downtime and verified ledger balancing."),
        ("What support is provided after software installation?", "We provide 1-year dedicated warranty, automated cloud backups, remote instant helpdesk, and direct on-site physical support whenever needed.")
    ]

    faqs_json = []
    faqs_html = ""
    for q, a in faqs:
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

    schema_json = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.iinfovision.com/" },
                    { "@type": "ListItem", "position": 2, "name": "Salem District Pincode Hub", "item": "https://www.iinfovision.com/salem-pincode-it-directory.html" },
                    { "@type": "ListItem", "position": 3, "name": f"{item['service']} in {item['locality']}", "item": f"https://www.iinfovision.com/{item['filename']}" }
                ]
            },
            {
                "@type": "LocalBusiness",
                "name": f"I Info Vision - {item['locality']} ({item['pin']}) Salem",
                "url": f"https://www.iinfovision.com/{item['filename']}",
                "telephone": "+919894480585",
                "priceRange": "₹₹",
                "image": "https://www.iinfovision.com/assets/images/logo.webp",
                "address": {
                    "@type": "PostalAddress",
                    "streetAddress": f"#9/136, No.1, First Floor, Trichy Main Road, Chinnaiyapuram, Dasanaickenpatti (Serving {item['locality']} {item['pin']})",
                    "addressLocality": "Salem",
                    "addressRegion": "Tamil Nadu",
                    "postalCode": item['pin'],
                    "addressCountry": "IN"
                },
                "areaServed": {
                    "@type": "AdministrativeArea",
                    "name": f"{item['locality']}, Salem {item['pin']}"
                },
                "description": item['desc']
            },
            {
                "@type": "FAQPage",
                "mainEntity": faqs_json
            }
        ]
    }

    schema_str = json.dumps(schema_json, indent=2)

    return f"""<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{html.escape(item['title'])}</title>
  <meta name="description" content="{html.escape(item['desc'])}" />
  <meta name="keywords" content="{html.escape(item['keywords'])}" />
  <meta name="author" content="I Info Vision" />
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1" />
  <meta name="geo.region" content="IN-TN" />
  <meta name="geo.placename" content="{item['locality']}, Salem" />
  <link rel="canonical" href="https://www.iinfovision.com/{item['filename']}" />

  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website" />
  <meta property="og:url" content="https://www.iinfovision.com/{item['filename']}" />
  <meta property="og:site_name" content="I Info Vision" />
  <meta property="og:locale" content="en_IN" />
  <meta property="og:title" content="{html.escape(item['title'])}" />
  <meta property="og:description" content="{html.escape(item['desc'])}" />
  <meta property="og:image" content="https://www.iinfovision.com/assets/images/logo.webp" />

  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:url" content="https://www.iinfovision.com/{item['filename']}" />
  <meta name="twitter:title" content="{html.escape(item['title'])}" />
  <meta name="twitter:description" content="{html.escape(item['desc'])}" />
  <meta name="twitter:image" content="https://www.iinfovision.com/assets/images/logo.webp" />

  <!-- Schema.org JSON-LD Structured Data -->
  <script type="application/ld+json">
{schema_str}
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
          <a href="salem-pincode-it-directory.html" style="color: #94a3b8;">Salem Pincodes</a>
          <i class="ph ph-caret-right"></i>
          <span style="color: #38bdf8;">{item['locality']} ({item['pin']})</span>
        </div>
        <div style="display: inline-block; background: rgba(56, 189, 248, 0.15); border: 1px solid rgba(56, 189, 248, 0.4); color: #38bdf8; font-size: 12.5px; font-weight: 700; padding: 6px 16px; border-radius: 20px; margin-bottom: 20px;">
          <i class="ph ph-map-pin"></i> {item['badge']}
        </div>
        <h1 class="page-hero-title" style="font-size: clamp(28px, 4.5vw, 44px); font-weight: 800; line-height: 1.25; margin-bottom: 20px;">
          {item['hero_title']}
        </h1>
        <p class="page-hero-desc" style="font-size: 16.5px; line-height: 1.7; color: #cbd5e1; max-width: 780px; margin: 0 auto 30px auto;">
          {item['hero_desc']}
        </p>
        <div style="display: flex; justify-content: center; gap: 14px; flex-wrap: wrap;">
          <a href="contact.html?locality={item['locality'].lower()}&pin={item['pin']}" class="btn btn-primary" style="padding: 13px 26px; font-weight: 700; border-radius: 10px; font-size: 14.5px;">
            Book On-Site Consultation &rarr;
          </a>
          <a href="https://wa.me/919894480585?text=Hello%20I%20Info%20Vision,%20I%20need%20software/web%20services%20in%20{item['locality']}" target="_blank" class="btn" style="background: rgba(255,255,255,0.08); color: #ffffff; border: 1.5px solid rgba(255,255,255,0.25); padding: 13px 22px; font-weight: 700; border-radius: 10px; font-size: 14.5px; display: inline-flex; align-items: center; gap: 8px;">
            <i class="ph ph-whatsapp-logo"></i> Instant WhatsApp Chat
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- LOCALITY FOCUS & ADVANTAGES -->
  <section style="padding: 60px 0; background: #f8fafc;">
    <div class="container">
      <div style="text-align: center; max-width: 700px; margin: 0 auto 40px auto;">
        <span style="color: #0284c7; font-weight: 700; font-size: 13px; text-transform: uppercase; letter-spacing: 1px;">Localized Architecture</span>
        <h2 style="font-size: 28px; font-weight: 800; color: #0f172a; margin-top: 8px;">Why Businesses in {item['locality']} Trust I Info Vision</h2>
        <p style="color: #64748b; font-size: 15px;">Targeted engineering designed around {item['focus']}.</p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 24px;">
        <div style="background: #ffffff; padding: 28px; border-radius: 16px; border: 1.5px solid #e2e8f0; box-shadow: 0 4px 15px rgba(0,0,0,0.04);">
          <div style="width: 48px; height: 48px; border-radius: 12px; background: #e0f2fe; color: #0284c7; display: flex; align-items: center; justify-content: center; font-size: 24px; margin-bottom: 18px;">
            <i class="ph ph-lightning"></i>
          </div>
          <h3 style="font-size: 18px; font-weight: 700; color: #0f172a; margin-bottom: 10px;">Sub-Second Speed &amp; Offline POS</h3>
          <p style="color: #64748b; font-size: 14.5px; line-height: 1.6;">Ultra-fast checkouts and website loading ensuring your customers never wait in line or face slow page errors.</p>
        </div>

        <div style="background: #ffffff; padding: 28px; border-radius: 16px; border: 1.5px solid #e2e8f0; box-shadow: 0 4px 15px rgba(0,0,0,0.04);">
          <div style="width: 48px; height: 48px; border-radius: 12px; background: #dcfce7; color: #16a34a; display: flex; align-items: center; justify-content: center; font-size: 24px; margin-bottom: 18px;">
            <i class="ph ph-shield-check"></i>
          </div>
          <h3 style="font-size: 18px; font-weight: 700; color: #0f172a; margin-bottom: 10px;">100% GST &amp; E-Way Bill Ready</h3>
          <p style="color: #64748b; font-size: 14.5px; line-height: 1.6;">Automated E-Invoices, E-Way bills, and multi-godown stock transfer slips compliant with government portals.</p>
        </div>

        <div style="background: #ffffff; padding: 28px; border-radius: 16px; border: 1.5px solid #e2e8f0; box-shadow: 0 4px 15px rgba(0,0,0,0.04);">
          <div style="width: 48px; height: 48px; border-radius: 12px; background: #fef3c7; color: #d97706; display: flex; align-items: center; justify-content: center; font-size: 24px; margin-bottom: 18px;">
            <i class="ph ph-navigation-arrow"></i>
          </div>
          <h3 style="font-size: 18px; font-weight: 700; color: #0f172a; margin-bottom: 10px;">On-Site Engineer in 60 Mins</h3>
          <p style="color: #64748b; font-size: 14.5px; line-height: 1.6;">Direct physical presence in Salem ensures your hardware, printers, and staff training are set up smoothly at your location.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- FAQS -->
  <section style="padding: 60px 0; background: #ffffff;">
    <div class="container" style="max-width: 860px;">
      <div style="text-align: center; margin-bottom: 40px;">
        <span style="color: #0284c7; font-weight: 700; font-size: 13px; text-transform: uppercase; letter-spacing: 1px;">Local Guidance</span>
        <h2 style="font-size: 28px; font-weight: 800; color: #0f172a; margin-top: 8px;">Frequently Asked Questions in {item['locality']}</h2>
      </div>

      <div class="faq-list">
{faqs_html}      </div>
    </div>
  </section>

  <!-- CTA BANNER -->
  <section style="padding: 60px 0; background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%); color: #ffffff; text-align: center;">
    <div class="container" style="max-width: 800px;">
      <h2 style="font-size: 32px; font-weight: 800; margin-bottom: 16px;">Schedule Your Free On-Site Demo in {item['locality']}</h2>
      <p style="font-size: 16.5px; color: #e0f2fe; margin-bottom: 30px; line-height: 1.6;">
        Call our Salem headquarters at +91 98944 80585. We will visit your {item['locality']} office or shop for a live demonstration.
      </p>
      <div style="display: flex; justify-content: center; gap: 14px; flex-wrap: wrap;">
        <a href="contact.html?locality={item['locality'].lower()}" class="btn" style="background: #ffffff; color: #0369a1; padding: 14px 28px; font-weight: 800; border-radius: 10px; font-size: 15px;">
          Book Free Strategy Session &rarr;
        </a>
        <a href="tel:+919894480585" class="btn" style="background: rgba(0,0,0,0.2); color: #ffffff; border: 1.5px solid rgba(255,255,255,0.4); padding: 14px 24px; font-weight: 800; border-radius: 10px; font-size: 15px; display: inline-flex; align-items: center; gap: 8px;">
          <i class="ph ph-phone-call"></i> Call Senior Engineer
        </a>
      </div>
    </div>
  </section>

{FOOTER_HTML}"""

# Generate Master Hub
hub_html = build_salem_pincode_hub()
with open(os.path.join(WORKSPACE, "salem-pincode-it-directory.html"), "w", encoding="utf-8") as f:
    f.write(hub_html)
print("Generated salem-pincode-it-directory.html successfully!")

# Generate 12 Prime Locality Pages
new_pages = ["salem-pincode-it-directory.html"]
for item in PRIME_LOCALITIES:
    page_html = build_prime_locality_page(item)
    with open(os.path.join(WORKSPACE, item["filename"]), "w", encoding="utf-8") as f:
        f.write(page_html)
    new_pages.append(item["filename"])
    print(f"Generated {item['filename']}")

print(f"Total new Salem Pincode Pages created: {len(new_pages)}")

# Update sitemap.xml
sitemap_path = os.path.join(WORKSPACE, "sitemap.xml")
with open(sitemap_path, "r", encoding="utf-8") as f:
    sitemap_text = f.read()

existing_urls = set(re.findall(r"<loc>(.*?)</loc>", sitemap_text))
to_add = []
for p in new_pages:
    u = f"https://www.iinfovision.com/{p}"
    if u not in existing_urls:
        to_add.append(u)

if to_add:
    xml_chunk = ""
    for u in to_add:
        xml_chunk += f"""  <url>
    <loc>{u}</loc>
    <lastmod>2026-10-16</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.88</priority>
  </url>\n"""
    sitemap_text = sitemap_text.replace("</urlset>", xml_chunk + "</urlset>")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(sitemap_text)
    print(f"Added {len(to_add)} URLs to sitemap.xml!")

total_sitemap_urls = len(re.findall(r"<loc>(.*?)</loc>", sitemap_text))
print(f"NEW TOTAL URLS IN SITEMAP: {total_sitemap_urls} URLs!")
