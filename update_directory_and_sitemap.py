"""
Updates directory.html and sitemap.html with:
- Erode District Pincode Hub & 8 Localities
- Karur District Pincode Hub & 8 Localities
- Namakkal District Pincode Hub & 7 Localities
- Rasipuram Region IT Hub & 6 Localities
- Trichy District Pincode Hub & 9 Localities
- Salem District Hub & 12 Localities
"""

import os

WORKSPACE = r"c:\Users\prave\OneDrive\Desktop\office projects\I-INFO-VISION-main"

# ==================== 1. UPDATE DIRECTORY.HTML ====================

directory_path = os.path.join(WORKSPACE, "directory.html")
with open(directory_path, "r", encoding="utf-8") as f:
    dir_content = f.read()

# Replace the single Salem banner with a comprehensive Regional Pincode & Locality Hubs Showcase
new_directory_banner = """      <!-- Mega Regional Pincode & Locality Hubs Showcase (Salem, Erode, Karur, Namakkal, Rasipuram, Trichy) -->
      <div style="background: linear-gradient(135deg, #0f172a 0%, #1e293b 100%); border-radius: 20px; padding: 36px; color: #ffffff; margin-bottom: 40px; box-shadow: 0 15px 35px -5px rgba(15, 23, 42, 0.4); border: 1px solid #334155;">
        <div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 20px; margin-bottom: 28px;">
          <div>
            <span style="background: rgba(56, 189, 248, 0.2); color: #38bdf8; border: 1px solid rgba(56, 189, 248, 0.4); padding: 4px 14px; border-radius: 9999px; font-size: 13px; font-weight: 700; text-transform: uppercase; letter-spacing: 0.5px;">Tamil Nadu Hyper-Local IT Hubs</span>
            <h2 style="font-size: 28px; font-weight: 800; margin-top: 10px; margin-bottom: 8px; color: #ffffff;">Regional Postal Pincode &amp; Commercial Directories</h2>
            <p style="color: #cbd5e1; font-size: 15px; max-width: 700px; margin: 0;">
              Targeting every delivery post office across Salem, Erode, Karur, Namakkal, Rasipuram, and Trichy with direct on-site engineer dispatch, GST billing POS, custom ERP, and web development.
            </p>
          </div>
        </div>

        <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(290px, 1fr)); gap: 18px;">
          <!-- Salem Hub -->
          <div style="background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.12); border-radius: 14px; padding: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
              <h3 style="font-size: 18px; font-weight: 800; color: #38bdf8; margin: 0;">Salem District</h3>
              <span style="background: #0284c7; color: #fff; font-size: 11.5px; font-weight: 700; padding: 2px 8px; border-radius: 6px;">60+ Post Offices</span>
            </div>
            <p style="color: #94a3b8; font-size: 13px; line-height: 1.5; margin-bottom: 12px;">Alagapuram, Fairlands, Shevapet, Ammapet, Gugai, Suramangalam, Attur, Mettur, Omalur, Sankagiri, Edappadi, Yercaud.</p>
            <a href="salem-pincode-it-directory.html" style="color: #38bdf8; font-weight: 700; font-size: 13.5px; text-decoration: none; display: inline-flex; align-items: center; gap: 5px;">
              Open Salem Directory &rarr;
            </a>
          </div>

          <!-- Erode Hub -->
          <div style="background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.12); border-radius: 14px; padding: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
              <h3 style="font-size: 18px; font-weight: 800; color: #38bdf8; margin: 0;">Erode District</h3>
              <span style="background: #0284c7; color: #fff; font-size: 11.5px; font-weight: 700; padding: 2px 8px; border-radius: 6px;">25+ Post Offices</span>
            </div>
            <p style="color: #94a3b8; font-size: 13px; line-height: 1.5; margin-bottom: 12px;">Erode City, Perundurai SIPCOT, Bhavani Carpets, Gobichettipalayam Turmeric, Sathyamangalam, Surampatti, Chithode, Chennimalai.</p>
            <a href="erode-pincode-it-directory.html" style="color: #38bdf8; font-weight: 700; font-size: 13.5px; text-decoration: none; display: inline-flex; align-items: center; gap: 5px;">
              Open Erode Directory &rarr;
            </a>
          </div>

          <!-- Karur Hub -->
          <div style="background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.12); border-radius: 14px; padding: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
              <h3 style="font-size: 18px; font-weight: 800; color: #38bdf8; margin: 0;">Karur District</h3>
              <span style="background: #0284c7; color: #fff; font-size: 11.5px; font-weight: 700; padding: 2px 8px; border-radius: 6px;">20+ Post Offices</span>
            </div>
            <p style="color: #94a3b8; font-size: 13px; line-height: 1.5; margin-bottom: 12px;">Home Textile Exports, Vengamedu Bus Body, Thanthonimalai Hospital, Gandhigramam POS, Puliyur Cement, Kulithalai, Aravakurichi Moringa.</p>
            <a href="karur-pincode-it-directory.html" style="color: #38bdf8; font-weight: 700; font-size: 13.5px; text-decoration: none; display: inline-flex; align-items: center; gap: 5px;">
              Open Karur Directory &rarr;
            </a>
          </div>

          <!-- Namakkal Hub -->
          <div style="background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.12); border-radius: 14px; padding: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
              <h3 style="font-size: 18px; font-weight: 800; color: #38bdf8; margin: 0;">Namakkal District</h3>
              <span style="background: #0284c7; color: #fff; font-size: 11.5px; font-weight: 700; padding: 2px 8px; border-radius: 6px;">18+ Post Offices</span>
            </div>
            <p style="color: #94a3b8; font-size: 13px; line-height: 1.5; margin-bottom: 12px;">Poultry Feed &amp; Egg Trading, Lorry Fleet Telematics, Tiruchengode Rig &amp; Weaving, Mohanur Sugar, Paramathi Velur, Komarapalayam.</p>
            <a href="namakkal-pincode-it-directory.html" style="color: #38bdf8; font-weight: 700; font-size: 13.5px; text-decoration: none; display: inline-flex; align-items: center; gap: 5px;">
              Open Namakkal Directory &rarr;
            </a>
          </div>

          <!-- Rasipuram Hub -->
          <div style="background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.12); border-radius: 14px; padding: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
              <h3 style="font-size: 18px; font-weight: 800; color: #38bdf8; margin: 0;">Rasipuram Region</h3>
              <span style="background: #0284c7; color: #fff; font-size: 11.5px; font-weight: 700; padding: 2px 8px; border-radius: 6px;">11+ Post Offices</span>
            </div>
            <p style="color: #94a3b8; font-size: 13px; line-height: 1.5; margin-bottom: 12px;">Rasipuram Pure Ghee Dairy, Matriculation School &amp; College ERP, Vennandur Towel Weaving, Namagiripettai Sago, Belukurichi Spice Mandi.</p>
            <a href="rasipuram-it-directory.html" style="color: #38bdf8; font-weight: 700; font-size: 13.5px; text-decoration: none; display: inline-flex; align-items: center; gap: 5px;">
              Open Rasipuram Directory &rarr;
            </a>
          </div>

          <!-- Trichy Hub -->
          <div style="background: rgba(255,255,255,0.06); border: 1px solid rgba(255,255,255,0.12); border-radius: 14px; padding: 20px;">
            <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
              <h3 style="font-size: 18px; font-weight: 800; color: #38bdf8; margin: 0;">Trichy District</h3>
              <span style="background: #0284c7; color: #fff; font-size: 11.5px; font-weight: 700; padding: 2px 8px; border-radius: 6px;">21+ Post Offices</span>
            </div>
            <p style="color: #94a3b8; font-size: 13px; line-height: 1.5; margin-bottom: 12px;">Thillai Nagar Web Dev, Cantonment Hospital HMS, Srirangam Hotel PMS, Thuvakudi Boiler Fabrication, Golden Rock, KK Nagar, Manachanallur Ponni Rice Mills.</p>
            <a href="trichy-pincode-it-directory.html" style="color: #38bdf8; font-weight: 700; font-size: 13.5px; text-decoration: none; display: inline-flex; align-items: center; gap: 5px;">
              Open Trichy Directory &rarr;
            </a>
          </div>
        </div>
      </div>"""

# Replace the previous Salem banner in directory.html
import re
pattern = r'<!-- Hyper-Local Salem District Pincode & Locality Hub Featured Banner -->.*?</div>\s*</div>'
if re.search(pattern, dir_content, flags=re.DOTALL):
    dir_content = re.sub(pattern, new_directory_banner, dir_content, flags=re.DOTALL)
    with open(directory_path, "w", encoding="utf-8") as f:
        f.write(dir_content)
    print("Updated directory.html with 6 regional directories showcase!")
else:
    print("Could not find Salem banner pattern in directory.html")

# ==================== 2. UPDATE SITEMAP.HTML ====================

sitemap_html_path = os.path.join(WORKSPACE, "sitemap.html")
with open(sitemap_html_path, "r", encoding="utf-8") as f:
    sm_content = f.read()

new_sitemap_regional_blocks = """          <!-- Regional Postal Pincode & Locality Networks -->
          <div class="sitemap-group" style="background: #f8fafc; border: 1.5px solid #cbd5e1; border-radius: 14px; padding: 24px; margin-bottom: 30px;">
            <h2 style="color: #0f172a; border-bottom: 2px solid #0284c7; padding-bottom: 10px; margin-bottom: 16px;">Regional Postal Pincode &amp; Locality Networks (Salem, Erode, Karur, Namakkal, Rasipuram, Trichy)</h2>
            <p style="color: #475569; font-size: 14px; margin-bottom: 20px;">Dedicated hyper-local software development, GST billing POS, and ERP hubs covering every delivery post office and commercial center.</p>

            <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px;">
              <!-- Salem Network -->
              <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; padding: 16px;">
                <h3 style="font-size: 16px; font-weight: 700; color: #0284c7; margin-bottom: 8px;">
                  <a href="salem-pincode-it-directory.html" style="text-decoration: underline; color: #0284c7;">Salem District (60+ Pincodes) &rarr;</a>
                </h3>
                <ul style="display: flex; flex-direction: column; gap: 6px; font-size: 13.5px; list-style: none; padding: 0;">
                  <li><a href="software-web-development-alagapuram-salem.html">&bull; Alagapuram (636004)</a></li>
                  <li><a href="software-web-development-fairlands-salem.html">&bull; Fairlands (636016)</a></li>
                  <li><a href="billing-software-shevapet-salem.html">&bull; Shevapet Wholesale (636002)</a></li>
                  <li><a href="textile-software-ammapet-salem.html">&bull; Ammapet Textile (636003)</a></li>
                  <li><a href="software-billing-gugai-salem.html">&bull; Gugai Silk Saree (636006)</a></li>
                  <li><a href="software-web-development-suramangalam-salem.html">&bull; Suramangalam (636005)</a></li>
                  <li><a href="software-web-development-attur-salem.html">&bull; Attur Sago &amp; Agro (636102)</a></li>
                  <li><a href="industrial-erp-software-mettur-salem.html">&bull; Mettur Heavy Industrial (636401)</a></li>
                  <li><a href="software-web-development-omalur-salem.html">&bull; Omalur Airport &amp; Tech (636455)</a></li>
                  <li><a href="transport-fleet-software-sankagiri-salem.html">&bull; Sankagiri Lorry Fleet (637301)</a></li>
                  <li><a href="textile-powerloom-software-edappadi-salem.html">&bull; Edappadi Powerloom (637101)</a></li>
                  <li><a href="hospital-hotel-software-yercaud-salem.html">&bull; Yercaud Resort PMS (636601)</a></li>
                </ul>
              </div>

              <!-- Erode Network -->
              <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; padding: 16px;">
                <h3 style="font-size: 16px; font-weight: 700; color: #0284c7; margin-bottom: 8px;">
                  <a href="erode-pincode-it-directory.html" style="text-decoration: underline; color: #0284c7;">Erode District (25+ Pincodes) &rarr;</a>
                </h3>
                <ul style="display: flex; flex-direction: column; gap: 6px; font-size: 13.5px; list-style: none; padding: 0;">
                  <li><a href="textile-erp-software-erode.html">&bull; Erode Textile Mills (638001)</a></li>
                  <li><a href="billing-software-perundurai-erode.html">&bull; Perundurai SIPCOT (638052)</a></li>
                  <li><a href="carpet-textile-software-bhavani-erode.html">&bull; Bhavani Jamakkalam (638301)</a></li>
                  <li><a href="agro-billing-software-gobichettipalayam-erode.html">&bull; Gobi Turmeric &amp; Rice (638452)</a></li>
                  <li><a href="software-web-development-sathyamangalam-erode.html">&bull; Sathyamangalam (638401)</a></li>
                  <li><a href="retail-pos-software-surampatti-erode.html">&bull; Surampatti Retail (638009)</a></li>
                  <li><a href="logistics-software-chithode-erode.html">&bull; Chithode Logistics (638102)</a></li>
                  <li><a href="handloom-export-software-chennimalai-erode.html">&bull; Chennimalai Handloom (638051)</a></li>
                </ul>
              </div>

              <!-- Karur Network -->
              <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; padding: 16px;">
                <h3 style="font-size: 16px; font-weight: 700; color: #0284c7; margin-bottom: 8px;">
                  <a href="karur-pincode-it-directory.html" style="text-decoration: underline; color: #0284c7;">Karur District (20+ Pincodes) &rarr;</a>
                </h3>
                <ul style="display: flex; flex-direction: column; gap: 6px; font-size: 13.5px; list-style: none; padding: 0;">
                  <li><a href="home-textile-export-software-karur.html">&bull; Karur Home Textile Export (639001)</a></li>
                  <li><a href="bus-body-building-erp-karur.html">&bull; Bus Body Coach Building (639006)</a></li>
                  <li><a href="software-web-development-vengamedu-karur.html">&bull; Vengamedu Corporate IT (639006)</a></li>
                  <li><a href="hospital-software-thanthonimalai-karur.html">&bull; Thanthonimalai Hospital (639005)</a></li>
                  <li><a href="retail-billing-software-gandhigramam-karur.html">&bull; Gandhigramam POS (639004)</a></li>
                  <li><a href="cement-paper-industrial-software-puliyur-karur.html">&bull; Puliyur &amp; TNPL Paper (639114)</a></li>
                  <li><a href="software-web-development-kulithalai-karur.html">&bull; Kulithalai Rice &amp; Agro (639107)</a></li>
                  <li><a href="moringa-agro-export-software-aravakurichi-karur.html">&bull; Aravakurichi Moringa Export (639201)</a></li>
                </ul>
              </div>

              <!-- Namakkal Network -->
              <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; padding: 16px;">
                <h3 style="font-size: 16px; font-weight: 700; color: #0284c7; margin-bottom: 8px;">
                  <a href="namakkal-pincode-it-directory.html" style="text-decoration: underline; color: #0284c7;">Namakkal District (18+ Pincodes) &rarr;</a>
                </h3>
                <ul style="display: flex; flex-direction: column; gap: 6px; font-size: 13.5px; list-style: none; padding: 0;">
                  <li><a href="poultry-feed-erp-software-namakkal.html">&bull; Poultry &amp; NECC Egg Trading (637001)</a></li>
                  <li><a href="lorry-transport-software-namakkal.html">&bull; Lorry Fleet Telematics (637001)</a></li>
                  <li><a href="textile-powerloom-software-tiruchengode-namakkal.html">&bull; Tiruchengode Weaving (637211)</a></li>
                  <li><a href="sugar-agro-software-mohanur-namakkal.html">&bull; Mohanur Sugar &amp; Milk (637015)</a></li>
                  <li><a href="retail-pos-software-paramathi-velur-namakkal.html">&bull; Paramathi Velur Betel (637207)</a></li>
                  <li><a href="textile-processing-software-komarapalayam-namakkal.html">&bull; Komarapalayam Dyeing (638183)</a></li>
                  <li><a href="borewell-rig-erp-tiruchengode-namakkal.html">&bull; Borewell Rig Fabrication (637211)</a></li>
                </ul>
              </div>

              <!-- Rasipuram Network -->
              <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; padding: 16px;">
                <h3 style="font-size: 16px; font-weight: 700; color: #0284c7; margin-bottom: 8px;">
                  <a href="rasipuram-it-directory.html" style="text-decoration: underline; color: #0284c7;">Rasipuram Region (11+ Pincodes) &rarr;</a>
                </h3>
                <ul style="display: flex; flex-direction: column; gap: 6px; font-size: 13.5px; list-style: none; padding: 0;">
                  <li><a href="software-web-development-rasipuram.html">&bull; Rasipuram Web Development (637408)</a></li>
                  <li><a href="school-college-erp-rasipuram.html">&bull; Matriculation School ERP (637408)</a></li>
                  <li><a href="ghee-agro-billing-software-rasipuram.html">&bull; Pure Ghee Dairy Billing (637408)</a></li>
                  <li><a href="powerloom-software-vennandur-rasipuram.html">&bull; Vennandur Towel Weaving (637505)</a></li>
                  <li><a href="sago-agro-software-namagiripettai-rasipuram.html">&bull; Namagiripettai Sago Starch (637406)</a></li>
                  <li><a href="spice-market-software-belukurichi-rasipuram.html">&bull; Belukurichi Spice Mandi (637402)</a></li>
                </ul>
              </div>

              <!-- Trichy Network -->
              <div style="background: #ffffff; border: 1px solid #e2e8f0; border-radius: 10px; padding: 16px;">
                <h3 style="font-size: 16px; font-weight: 700; color: #0284c7; margin-bottom: 8px;">
                  <a href="trichy-pincode-it-directory.html" style="text-decoration: underline; color: #0284c7;">Trichy District (21+ Pincodes) &rarr;</a>
                </h3>
                <ul style="display: flex; flex-direction: column; gap: 6px; font-size: 13.5px; list-style: none; padding: 0;">
                  <li><a href="software-web-development-thillai-nagar-trichy.html">&bull; Thillai Nagar Web &amp; IT (620018)</a></li>
                  <li><a href="hospital-software-cantonment-trichy.html">&bull; Cantonment Hospital HMS (620001)</a></li>
                  <li><a href="retail-billing-software-srirangam-trichy.html">&bull; Srirangam Tourism &amp; Hotel (620006)</a></li>
                  <li><a href="engineering-fabrication-erp-thuvakudi-trichy.html">&bull; Thuvakudi Boiler Fabrication (620015)</a></li>
                  <li><a href="railway-logistics-software-golden-rock-trichy.html">&bull; Golden Rock Locomotive (620004)</a></li>
                  <li><a href="school-college-erp-kk-nagar-trichy.html">&bull; KK Nagar School Campus (620021)</a></li>
                  <li><a href="agro-fabrication-software-manapparai-trichy.html">&bull; Manapparai Murukku &amp; Cattle (621306)</a></li>
                  <li><a href="rice-mill-erp-manachanallur-trichy.html">&bull; Manachanallur Ponni Rice (621005)</a></li>
                  <li><a href="software-web-development-lalgudi-trichy.html">&bull; Lalgudi Delta Agriculture (621601)</a></li>
                </ul>
              </div>
            </div>
          </div>"""

# Replace the Salem group in sitemap.html with this master regional block
sm_pattern = r'<div class="sitemap-group" style="background: #eff6ff;.*?</div>\s*</div>'
if re.search(sm_pattern, sm_content, flags=re.DOTALL):
    sm_content = re.sub(sm_pattern, new_sitemap_regional_blocks, sm_content, flags=re.DOTALL)
    with open(sitemap_html_path, "w", encoding="utf-8") as f:
        f.write(sm_content)
    print("Updated sitemap.html with complete regional pincode networks!")
else:
    print("Could not find pattern in sitemap.html")

