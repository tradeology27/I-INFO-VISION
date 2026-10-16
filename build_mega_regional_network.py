"""
Mega Regional Pincode & Locality SEO Network Generator for I Info Vision.
Covers:
1. ERODE DISTRICT (Master Directory + 8 Commercial Locality Pages)
2. KARUR DISTRICT (Master Directory + 8 Commercial Locality Pages)
3. NAMAKKAL DISTRICT (Master Directory + 7 Commercial Locality Pages)
4. RASIPURAM REGION (Master Directory + 6 Commercial Locality Pages)
5. TRICHY (TIRUCHIRAPPALLI) DISTRICT (Master Directory + 9 Commercial Locality Pages)
Total: 38 Pages generated, sitemap.xml expanded from 144 to 182 URLs!
"""

import os
import json
import re

WORKSPACE = r"c:\Users\prave\OneDrive\Desktop\office projects\I-INFO-VISION-main"

# ==================== DATASETS FOR 5 REGIONS ====================

REGIONAL_HUBS = {
    "erode": {
        "title": "Erode District IT & Software Pincode Directory (638001 - 638501)",
        "hub_file": "erode-pincode-it-directory.html",
        "city_name": "Erode",
        "geo": ("11.3410", "77.7172"),
        "pincodes": [
            ("Erode H.O (Brough Road)", "638001", "Textile Wholesale, Corporate Hub, Banking & Retail Malls"),
            ("Railway Colony Erode", "638002", "Railway Junction, Freight Logistics & Transporters"),
            ("Surampatti", "638009", "Supermarkets, Modern Retail, Healthcare & Residential"),
            ("Perundurai (SIPCOT)", "638052", "Major Industrial Estate, Chemical, Manufacturing & Logistics"),
            ("Bhavani", "638301", "Jamakkalam Carpets, Powerloom Weaving & Temple Tourism"),
            ("Gobichettipalayam", "638452", "Turmeric Processing, Banana & Rice Mills, Agro Business"),
            ("Sathyamangalam", "638401", "Tiger Reserve Gate, Silk Weaving, Colleges & Trading"),
            ("Chithode", "638102", "National Highway Warehousing, Logistics & Cold Storage"),
            ("Chennimalai", "638051", "Handloom Bedsheets, Export Weaving & Showrooms"),
            ("Modakkurichi", "638104", "Agriculture, Agro-Processing & Rural Commerce"),
            ("Kodumudi", "638151", "Cauvery Agro Trade, Temple Tourism & Riverine Commerce"),
            ("Sivagiri", "638109", "Sesame Oil Mills, Agriculture & Processing"),
            ("Nambiyur", "638458", "Agro Farming, Powerlooms & Local Commerce"),
            ("Anthiyur", "638501", "Weekly Livestock Market, Powerlooms & Agricultural Hub"),
            ("Appakudal", "638315", "Sugar Mills, Industrial Paper Board & Farming"),
            ("Kavindapadi", "638455", "Country Jaggery Wholesale Mandi & Agriculture"),
            ("Veerappanchatiram", "638004", "Textile Processing, Dyeing Units & Powerloom Clusters"),
            ("Kasipalayam", "638009", "Residential Hub, Local Retail & Commercial Stores"),
            ("Thindal", "638012", "Vellalar Engineering Colleges, Hospitals & Educational Hub"),
            ("Solar", "638002", "Intercity Bus Terminal, Highway Logistics & Transporters"),
            ("Lakkapuram", "638002", "Modern Rice Mills & Agro Processing Plants"),
            ("Kanjikovil", "638116", "Small Scale Industries, Agriculture & Weaving"),
            ("Vijayamangalam", "637056", "Highway Transport Corridor & Textile Weaving"),
            ("Olagadam", "638314", "Powerloom Weaving Units & Local Shops"),
            ("Arachalur", "638101", "Coconut & Paddy Agro Farming, Rural Commerce")
        ],
        "localities": [
            {
                "file": "textile-erp-software-erode.html",
                "locality": "Erode City & Brough Road",
                "pincode": "638001",
                "industry": "Textile Spinning, Dyeing & Processing Mills ERP",
                "headline": "Textile Mills ERP &amp; Fabric Trading Software in Erode",
                "desc": "Specialized ERP software engineered for Erode's spinning mills, yarn dyeing units, grey cloth wholesale, and fabric traders. Automated batch costing, dyehouse automation, and GST e-invoicing.",
                "keywords": "textile erp erode, spinning mill software erode, fabric billing software 638001, textile software brough road erode, I Info Vision Erode"
            },
            {
                "file": "billing-software-perundurai-erode.html",
                "locality": "Perundurai SIPCOT",
                "pincode": "638052",
                "industry": "SIPCOT Manufacturing, Chemical & Logistics Software",
                "headline": "Industrial ERP &amp; Billing Software in Perundurai SIPCOT",
                "desc": "Enterprise resource planning and GST billing software for Perundurai SIPCOT chemical plants, manufacturing units, engineering workshops, and industrial transporters.",
                "keywords": "billing software perundurai, sipcot industrial erp perundurai, chemical plant software 638052, manufacturing erp erode, I Info Vision Perundurai"
            },
            {
                "file": "carpet-textile-software-bhavani-erode.html",
                "locality": "Bhavani",
                "pincode": "638301",
                "industry": "Jamakkalam Carpets & Powerloom Weaving Software",
                "headline": "Jamakkalam Carpet &amp; Powerloom ERP Software in Bhavani",
                "desc": "End-to-end weaving production tracking, loom wage calculations, yarn consumption, and wholesale billing software for Bhavani's heritage carpet and textile manufacturers.",
                "keywords": "bhavani jamakkalam software, powerloom erp bhavani, textile billing bhavani 638301, loom wage software erode, I Info Vision Bhavani"
            },
            {
                "file": "agro-billing-software-gobichettipalayam-erode.html",
                "locality": "Gobichettipalayam",
                "pincode": "638452",
                "industry": "Turmeric, Rice & Agro Commodity Trading POS",
                "headline": "Turmeric Mandi &amp; Agro Billing Software in Gobichettipalayam",
                "desc": "Wholesale commission agent mandi billing, lot-wise turmeric auction tracking, banana trade, and paddy rice mill management software in Gobichettipalayam.",
                "keywords": "agro billing gobichettipalayam, turmeric mandi software gobi, rice mill erp 638452, billing software gobi erode, I Info Vision Gobi"
            },
            {
                "file": "software-web-development-sathyamangalam-erode.html",
                "locality": "Sathyamangalam",
                "pincode": "638401",
                "industry": "Enterprise Web Development & Institutional IT",
                "headline": "Software Company &amp; Web Development in Sathyamangalam",
                "desc": "High-performance business website design, custom ERP software, college management portals, and mobile application engineering for businesses in Sathyamangalam.",
                "keywords": "web development sathyamangalam, software company sathy 638401, website design sathyamangalam erode, mobile app development sathy, I Info Vision"
            },
            {
                "file": "retail-pos-software-surampatti-erode.html",
                "locality": "Surampatti",
                "pincode": "638009",
                "industry": "Supermarket POS & Retail Store Billing",
                "headline": "Supermarket POS &amp; Retail Billing Software in Surampatti",
                "desc": "High-speed barcode scanner billing, automated stock alerts, pharmacy batch expiry management, and customer loyalty POS software for retailers in Surampatti, Erode.",
                "keywords": "supermarket pos surampatti, retail billing software surampatti 638009, pharmacy software surampatti erode, grocery pos billing erode, I Info Vision"
            },
            {
                "file": "logistics-software-chithode-erode.html",
                "locality": "Chithode",
                "pincode": "638102",
                "industry": "Warehouse Management & Highway Logistics ERP",
                "headline": "Logistics, Transporters &amp; Warehouse WMS in Chithode",
                "desc": "Cold storage lot tracking, highway fleet dispatch, automated lorry receipts (LR), and GPS telematics software for logistics operators on the Salem-Cochin Highway at Chithode.",
                "keywords": "logistics software chithode, warehouse wms chithode 638102, cold storage software erode, transport software chithode, I Info Vision"
            },
            {
                "file": "handloom-export-software-chennimalai-erode.html",
                "locality": "Chennimalai",
                "pincode": "638051",
                "industry": "Handloom Export & Made-Ups Production ERP",
                "headline": "Handloom Bedsheet &amp; Home Linen ERP in Chennimalai",
                "desc": "Custom ERP system for Chennimalai handloom societies and exporters. Manages yarn dyeing, warp/weft inventory, weaver job works, and international export packing slips.",
                "keywords": "handloom software chennimalai, export textile erp chennimalai 638051, bedsheet billing software erode, weaver society software, I Info Vision"
            }
        ]
    },

    "karur": {
        "title": "Karur District IT & Software Pincode Directory (639001 - 639205)",
        "hub_file": "karur-pincode-it-directory.html",
        "city_name": "Karur",
        "geo": ("10.9601", "78.0766"),
        "pincodes": [
            ("Karur H.O (Jawahar Bazaar)", "639001", "Home Textile Capital, Global Exports, Banking & Commercial Hub"),
            ("Karur West", "639002", "Handloom Weaving, Dyeing Units & Export Processing"),
            ("Thanthonimalai", "639005", "Collectorate, Government Arts College, Clinics & Offices"),
            ("Vengamedu", "639006", "Bus Body Building, Coach Fabrication & Textile Ancillaries"),
            ("Gandhigramam", "639004", "Multi-Speciality Hospitals, Diagnostic Centers & Retail"),
            ("Puliyur", "639114", "Chettinad Cement, Limestone Processing & Heavy Industry"),
            ("Kulithalai", "639107", "Cauvery Agriculture, Modern Rice Mills & Sub-Division Hub"),
            ("Aravakurichi", "639201", "Moringa Drumstick Global Export & Agro Trading"),
            ("Velayuthampalayam", "639117", "TNPL Paper Mill Colony & Commercial Market"),
            ("Kagithapuram", "639136", "Asia's Premier Eco-Friendly Paper Mill (TNPL) Hub"),
            ("Mayanur", "639108", "Cauvery Barrage, Educational Institutions & Agriculture"),
            ("Krishnarayapuram", "639102", "Agricultural Farming, Weaving & Rural Commerce"),
            ("Chinnadharapuram", "639123", "Livestock, Grain Wholesale Mandi & Retail"),
            ("Pallapatti", "639205", "Pharma Wholesale Distributors, Global Expatriate Networks"),
            ("Nerur", "639004", "Spiritual Tourism, Banana Plantations & Agriculture"),
            ("Uppidamangalam", "639114", "Weekly Cattle Mandi & Agro Farming"),
            ("Tharagampatti", "621311", "Kadavur Taluk Headquarters & Forestry Farming"),
            ("Manmangalam", "639006", "Textile Printing, Powerlooms & Fabric Processing"),
            ("Inamkarur", "639002", "Commercial Outlets, Textile Dyeing & Fabrication"),
            ("Panchamadevi", "639004", "Textile Bleaching & Local Production Units")
        ],
        "localities": [
            {
                "file": "home-textile-export-software-karur.html",
                "locality": "Karur City Center",
                "pincode": "639001",
                "industry": "Home Textile & Made-Ups Export ERP",
                "headline": "Home Textile Export ERP &amp; Buying House Software in Karur",
                "desc": "Enterprise ERP engineered for Karur's home textile exporters, buying agents, and made-up manufacturers. Multi-currency export invoicing, barcode carton packing, and buyer sampling CRM.",
                "keywords": "home textile erp karur, export software karur 639001, textile buying house software karur, made-ups erp karur, I Info Vision Karur"
            },
            {
                "file": "bus-body-building-erp-karur.html",
                "locality": "Vengamedu Coach Hub",
                "pincode": "639006",
                "industry": "Bus Body Building & Coach Fabrication ERP",
                "headline": "Bus Body Building &amp; Commercial Coach Fabrication ERP in Karur",
                "desc": "Tailor-made fabrication ERP for Karur bus body builders. Manages structural steel BOM, chassis tracking, RTO homologation documents, seat fabrication, and workshop job cards.",
                "keywords": "bus body erp karur, coach building software karur 639006, fabrication erp vengamedu, automobile workshop software karur, I Info Vision"
            },
            {
                "file": "software-web-development-vengamedu-karur.html",
                "locality": "Vengamedu",
                "pincode": "639006",
                "industry": "Corporate IT, Web & Mobile App Development",
                "headline": "Software Company &amp; Web Development in Vengamedu, Karur",
                "desc": "Modern responsive corporate websites, customer web portals, Android/iOS mobile applications, and cloud software for manufacturing and commercial businesses in Vengamedu.",
                "keywords": "web development vengamedu, software company vengamedu 639006, website design karur, mobile app developer karur, I Info Vision"
            },
            {
                "file": "hospital-software-thanthonimalai-karur.html",
                "locality": "Thanthonimalai",
                "pincode": "639005",
                "industry": "Hospital Management System (HMS) & Healthcare IT",
                "headline": "Hospital Management Software (HMS) in Thanthonimalai, Karur",
                "desc": "Comprehensive clinical hospital software with OPD/IPD billing, NABH compliance, electronic health records (EHR), lab diagnostic integration, and pharmacy dispensing in Thanthonimalai.",
                "keywords": "hospital software thanthonimalai, hms software karur 639005, clinic management software thanthonimalai, doctor prescription app karur, I Info Vision"
            },
            {
                "file": "retail-billing-software-gandhigramam-karur.html",
                "locality": "Gandhigramam",
                "pincode": "639004",
                "industry": "Supermarket POS & Retail Store Billing",
                "headline": "Supermarket POS &amp; Retail Billing Software in Gandhigramam",
                "desc": "Fast thermal receipt printing, automated inventory reordering, barcode scanning, and GST e-invoicing for department stores and retail shops in Gandhigramam, Karur.",
                "keywords": "retail billing gandhigramam, supermarket pos karur 639004, barcode billing software karur, gst pos software gandhigramam, I Info Vision"
            },
            {
                "file": "cement-paper-industrial-software-puliyur-karur.html",
                "locality": "Puliyur & Kagithapuram",
                "pincode": "639114",
                "industry": "Heavy Industrial, Paper & Cement Plant ERP",
                "headline": "Industrial Plant ERP &amp; Asset Management in Puliyur &amp; TNPL",
                "desc": "Plant maintenance, raw material weighbridge automation, boiler fuel tracking, and contractor workforce management ERP for heavy industries around Puliyur and Kagithapuram.",
                "keywords": "industrial plant erp puliyur, cement factory software 639114, tnpl kagithapuram software, weighbridge automation karur, I Info Vision"
            },
            {
                "file": "software-web-development-kulithalai-karur.html",
                "locality": "Kulithalai",
                "pincode": "639107",
                "industry": "Agro-Trading, Rice Mill & Educational Software",
                "headline": "Software Company &amp; Web Development in Kulithalai, Karur",
                "desc": "Modern websites, paddy mill inventory software, educational school ERP systems, and retail GST billing for businesses and institutions across Kulithalai taluk.",
                "keywords": "web development kulithalai, software company kulithalai 639107, rice mill software kulithalai, billing software karur, I Info Vision"
            },
            {
                "file": "moringa-agro-export-software-aravakurichi-karur.html",
                "locality": "Aravakurichi",
                "pincode": "639201",
                "industry": "Drumstick & Agro Commodity Export ERP",
                "headline": "Moringa Drumstick &amp; Agro Commodity Export ERP in Aravakurichi",
                "desc": "Quality grading, farmer purchase ledgers, cold truck container dispatch, and export documentation software for drumstick and agro-commodity trading firms in Aravakurichi.",
                "keywords": "moringa export software aravakurichi, drumstick trade erp karur 639201, agro commodity billing aravakurichi, farmer purchase software, I Info Vision"
            }
        ]
    },

    "namakkal": {
        "title": "Namakkal District IT & Software Pincode Directory (637001 - 637409)",
        "hub_file": "namakkal-pincode-it-directory.html",
        "city_name": "Namakkal",
        "geo": ("11.2189", "78.1674"),
        "pincodes": [
            ("Namakkal H.O", "637001", "Poultry Capital, Egg Forwarding, Lorry Transport & Finance"),
            ("Mohanur", "637015", "Sugar Mills, Milk Chilling Plants & River Agriculture"),
            ("Paramathi Velur", "637207", "Betel Leaf Markets, Agro Trading & Cauvery River Commerce"),
            ("Tiruchengode", "637211", "Borewell Rig Drilling, Textile Powerlooms & Engineering Colleges"),
            ("Sendamangalam", "637409", "Kolli Hills Foothills, Plantation Produce & Agro Retail"),
            ("Puduchatram", "637018", "Poultry Feed Mills, Automatic Feeder Fabrication & Logistics"),
            ("Erumaipatty", "637013", "Limestone Mining, Poultry Farms & Agriculture"),
            ("Komarapalayam", "638183", "Textile Processing, Sizing Mills, Dyeing & Engineering Hub"),
            ("Velagoundampatti", "637212", "Commercial Banking, Poultry Hatcheries & Agro Shops"),
            ("Mallasamudram", "637503", "Powerloom Sarees, Handlooms & Educational Institutions"),
            ("Jedarpalayam", "637213", "Jaggery Sugar Production, Dam Tourism & Agriculture"),
            ("Kabilarmalai", "637204", "Betel Vine Plantations, Tourism & Agro Farming"),
            ("Pallipalayam", "638006", "Yarn Spinning Mills, Fabric Sizing & Dyeing Clusters"),
            ("Vengarai", "637208", "Sugarcane Farming & Local Commercial Stores"),
            ("Valavanthi", "637411", "Kolli Hills Tribal Produce, Spices & Tourism"),
            ("Alanganatham", "637013", "Poultry Farming & Agricultural Production"),
            ("Thottiyam Road", "637001", "Transport Workshops, Lorry Garages & Spares"),
            ("Mudhalaipatti", "637003", "Highway Transporters & Warehouse Infrastructure")
        ],
        "localities": [
            {
                "file": "poultry-feed-erp-software-namakkal.html",
                "locality": "Namakkal Egg & Feed Hub",
                "pincode": "637001",
                "industry": "Poultry Farm, Feed Mill & Egg Trading ERP",
                "headline": "Poultry Farm, Feed Mill &amp; NECC Egg Trading ERP in Namakkal",
                "desc": "India's premier poultry management system. Flock feed conversion ratio (FCR), daily egg collection & grading, NECC price integration, vaccine tracking, and feed batch formula ERP.",
                "keywords": "poultry erp namakkal, egg trading software 637001, feed mill software namakkal, necc egg billing software, poultry farm software, I Info Vision"
            },
            {
                "file": "lorry-transport-software-namakkal.html",
                "locality": "Namakkal Trucking Hub",
                "pincode": "637001",
                "industry": "Fleet Telematics & Lorry Transport ERP",
                "headline": "Lorry Booking, Fleet Telematics &amp; Transport ERP in Namakkal",
                "desc": "Fleet management software for Namakkal lorry owners and booking agents. GPS live tracking, driver trip advance, diesel fuel mileage analytics, tyre serial tracking, and automated e-way bill generation.",
                "keywords": "lorry transport software namakkal, fleet management namakkal 637001, truck booking erp namakkal, transport telematics software, I Info Vision"
            },
            {
                "file": "textile-powerloom-software-tiruchengode-namakkal.html",
                "locality": "Tiruchengode",
                "pincode": "637211",
                "industry": "Textile Powerloom Weaving & Sizing ERP",
                "headline": "Textile Powerloom &amp; Sizing Mills ERP in Tiruchengode",
                "desc": "Warping, sizing, weaver piece-rate wages, fabric defect grading, and grey cloth dispatch software for textile mills and weaving clusters in Tiruchengode.",
                "keywords": "powerloom software tiruchengode, textile erp tiruchengode 637211, sizing mill software namakkal, fabric billing tiruchengode, I Info Vision"
            },
            {
                "file": "sugar-agro-software-mohanur-namakkal.html",
                "locality": "Mohanur",
                "pincode": "637015",
                "industry": "Sugar Mill & Agro Industry Software",
                "headline": "Sugar Mills &amp; Dairy Processing Software in Mohanur",
                "desc": "Sugarcane weighing bridge automation, farmer recovery calculation, molasses production tracking, and bulk milk chilling ERP for agro-industries in Mohanur.",
                "keywords": "sugar mill software mohanur, dairy chilling software namakkal 637015, agro processing erp mohanur, weighbridge software, I Info Vision"
            },
            {
                "file": "retail-pos-software-paramathi-velur-namakkal.html",
                "locality": "Paramathi Velur",
                "pincode": "637207",
                "industry": "Betel Leaf & Retail Store Billing POS",
                "headline": "Betel Leaf Mandi &amp; Retail POS Billing in Paramathi Velur",
                "desc": "Specialized auction mandi billing for betel leaf growers, agricultural fertilizer stores, supermarket POS, and pharmacy software in Paramathi Velur.",
                "keywords": "betel leaf mandi software paramathi velur, retail billing velur 637207, fertilizer pos software namakkal, grocery billing velur, I Info Vision"
            },
            {
                "file": "textile-processing-software-komarapalayam-namakkal.html",
                "locality": "Komarapalayam",
                "pincode": "638183",
                "industry": "Textile Sizing, Dyeing & Export ERP",
                "headline": "Textile Dyeing, Processing &amp; Export ERP in Komarapalayam",
                "desc": "Complete dyehouse batch management, chemical formulation recipes, effluent treatment tracking, and fabric export billing software for Komarapalayam industrial units.",
                "keywords": "textile dyeing software komarapalayam, processing erp komarapalayam 638183, sizing erp namakkal, export fabric billing, I Info Vision"
            },
            {
                "file": "borewell-rig-erp-tiruchengode-namakkal.html",
                "locality": "Tiruchengode Rig Hub",
                "pincode": "637211",
                "industry": "Borewell Rig Equipment & Fabrication ERP",
                "headline": "Borewell Rig Manufacturing &amp; Drilling Operations ERP in Tiruchengode",
                "desc": "Track rig drilling meters, compressor diesel consumption, operator wages, spare parts inventory, and export rig sales for Tiruchengode's world-renowned borewell industry.",
                "keywords": "borewell rig software tiruchengode, rig operations erp 637211, drilling machine software namakkal, rig fabrication software, I Info Vision"
            }
        ]
    },

    "rasipuram": {
        "title": "Rasipuram Region IT & Software Directory (637408 - 637505)",
        "hub_file": "rasipuram-it-directory.html",
        "city_name": "Rasipuram",
        "geo": ("11.4646", "78.1772"),
        "pincodes": [
            ("Rasipuram H.O", "637408", "Pure Ghee Capital, Matriculation Schools, Colleges & Commercial Hub"),
            ("Vennandur", "637505", "Powerloom Towel Weaving, Screen Printing & Textile Made-Ups"),
            ("Namagiripettai", "637406", "Sago & Tapioca Starch Factories, Kolli Hills Foothills"),
            ("Pillanallur", "637403", "Handloom Weaving & Rural Commerce"),
            ("Pattanam", "637407", "Agricultural Produce & Local Commercial Stores"),
            ("Gurusamipalayam", "637403", "Silk & Cotton Saree Weaving Industry"),
            ("Belukurichi", "637402", "Weekly Foothill Spice & Agro Produce Market"),
            ("Singalandapuram", "637412", "Powerloom Textile Units & Agriculture"),
            ("Mangalapuram", "637503", "Rural Commercial & Small Scale Farming"),
            ("Bodamalai", "637408", "Plantations, Honey & Eco-Tourism Produce"),
            ("Attanur", "636202", "Poultry Farming & Agricultural Production")
        ],
        "localities": [
            {
                "file": "software-web-development-rasipuram.html",
                "locality": "Rasipuram Town",
                "pincode": "637408",
                "industry": "Software Company & Corporate Web Development",
                "headline": "Software Company &amp; Web Development in Rasipuram",
                "desc": "Premier web design, custom business applications, e-commerce storefronts, and cloud billing systems for growing commercial enterprises in Rasipuram.",
                "keywords": "web development rasipuram, software company rasipuram 637408, website design rasipuram, billing software rasipuram, I Info Vision"
            },
            {
                "file": "school-college-erp-rasipuram.html",
                "locality": "Rasipuram Education Hub",
                "pincode": "637408",
                "industry": "Matriculation School, College & Hostel ERP",
                "headline": "School &amp; College Management ERP in Rasipuram",
                "desc": "Digital campus platform for Rasipuram's leading matriculation schools and engineering institutions. Student attendance, fee collection, parent mobile app, and examination marks portal.",
                "keywords": "school software rasipuram, college erp rasipuram 637408, hostel management software namakkal, school fees app rasipuram, I Info Vision"
            },
            {
                "file": "ghee-agro-billing-software-rasipuram.html",
                "locality": "Rasipuram Ghee Market",
                "pincode": "637408",
                "industry": "Pure Ghee Dairy & Agro Processing POS",
                "headline": "Pure Ghee Manufacturing &amp; Wholesale Dairy Software in Rasipuram",
                "desc": "Fat-content milk procurement, butter melting batch yield, FSSAI lot tracking, tin packaging, and distributor billing software for Rasipuram's famous pure ghee industry.",
                "keywords": "ghee billing software rasipuram, dairy erp rasipuram 637408, milk procurement software namakkal, agro billing rasipuram, I Info Vision"
            },
            {
                "file": "powerloom-software-vennandur-rasipuram.html",
                "locality": "Vennandur",
                "pincode": "637505",
                "industry": "Towel & Powerloom Weaving ERP",
                "headline": "Towel Weaving &amp; Powerloom ERP in Vennandur, Rasipuram",
                "desc": "Automate jacquard towel weaving, terry fabric production, weaver wage calculation, and wholesale dispatch for textile units in Vennandur.",
                "keywords": "towel software vennandur, powerloom erp vennandur 637505, textile billing rasipuram, jacquard weaving software, I Info Vision"
            },
            {
                "file": "sago-agro-software-namagiripettai-rasipuram.html",
                "locality": "Namagiripettai",
                "pincode": "637406",
                "industry": "Sago Starch Mill & Agro Trade ERP",
                "headline": "Sago &amp; Tapioca Starch Mill ERP in Namagiripettai",
                "desc": "Raw tapioca root weighbridge entry, starch content extraction yield calculation, sago roasting batches, and SAGOSERVE auction invoice generation software.",
                "keywords": "sago software namagiripettai, starch factory erp namagiripettai 637406, tapioca mill software rasipuram, sagoserve billing, I Info Vision"
            },
            {
                "file": "spice-market-software-belukurichi-rasipuram.html",
                "locality": "Belukurichi",
                "pincode": "637402",
                "industry": "Spice Mandi & Agro Commodity Billing POS",
                "headline": "Spice Trading &amp; Weekly Mandi Software in Belukurichi",
                "desc": "Pepper, clove, coffee, and agricultural produce wholesale mandi billing for traders and farmers in the Kolli Hills foothills market at Belukurichi.",
                "keywords": "spice software belukurichi, agro mandi software 637402, pepper trading billing rasipuram, wholesale billing belukurichi, I Info Vision"
            }
        ]
    },

    "trichy": {
        "title": "Trichy District IT & Software Pincode Directory (620001 - 621601)",
        "hub_file": "trichy-pincode-it-directory.html",
        "city_name": "Trichy",
        "geo": ("10.7905", "78.7047"),
        "pincodes": [
            ("Trichy H.O (Cantonment)", "620001", "District Administration, Banking Hub & Star Hotels"),
            ("Thillai Nagar", "620018", "Doctors Hub, Corporate IT, Luxury Showrooms & Clinics"),
            ("Srirangam", "620006", "Ranganathaswamy Temple, Tourism, Heritage Crafts & Retailing"),
            ("Thuvakudi (NIT Trichy)", "620015", "NIT Trichy, BHEL Ancillary Fabrication & Industrial Estate"),
            ("Golden Rock (Ponmalai)", "620004", "Railway Locomotive Workshop, Housing & Engineering"),
            ("KK Nagar", "620021", "Trichy International Airport, Aviation Logistics & Schools"),
            ("Teppakulam", "620002", "Rockfort Temple Bazaar, NSB Road Retail & Jewellery"),
            ("Woraiyur", "620003", "Handloom Cotton Sarees, Historical Hub & Clinics"),
            ("Thiruverumbur", "620013", "BHEL Township, IT Companies & Heavy Fabrication"),
            ("Kattur", "620019", "Automobile Showrooms, Spares & Residential Suburbs"),
            ("Subramaniapuram", "620020", "Automotive Garages, Transporters & Commercial Complexes"),
            ("Lalgudi", "621601", "Cauvery Delta Agriculture, Rice Mills & Sub-Division"),
            ("Manapparai", "621306", "Famous Murukku Snacks, Cattle Market & Engineering"),
            ("Musiri", "621211", "Riverine Agriculture, Brick Kilns & Commercial Trade"),
            ("Samayapuram", "621112", "Mariamman Temple Pilgrimage, Hotels & Shopping"),
            ("Manachanallur", "621005", "World Capital of Ponni Rice Mills & Grain Wholesale"),
            ("Thuraiyur", "621010", "Cotton Ginning, Agriculture & Educational Hub"),
            ("Bikshandarkoil", "621216", "Heritage, Agriculture & Local Commercial"),
            ("Vayalur Road", "620102", "Educational Institutions & Premium Residential"),
            ("Crawford", "620012", "Highway Transporters & Logistics Infrastructure"),
            ("Khajamalai", "620023", "Bharathidasan University Campus & Institutions")
        ],
        "localities": [
            {
                "file": "software-web-development-thillai-nagar-trichy.html",
                "locality": "Thillai Nagar",
                "pincode": "620018",
                "industry": "Corporate Web Development & Healthcare IT",
                "headline": "Software Company &amp; Web Development in Thillai Nagar, Trichy",
                "desc": "Elite responsive website design, healthcare clinic software, doctor appointment apps, and enterprise cloud solutions for businesses in Thillai Nagar, Trichy.",
                "keywords": "web development thillai nagar, software company thillai nagar 620018, website design trichy, doctor appointment software trichy, I Info Vision"
            },
            {
                "file": "hospital-software-cantonment-trichy.html",
                "locality": "Cantonment",
                "pincode": "620001",
                "industry": "Multispeciality Hospital Management System (HMS)",
                "headline": "Hospital Management Software (HMS) in Cantonment, Trichy",
                "desc": "NABH-ready hospital information system for Trichy's top multispeciality hospitals and nursing homes. IPD/OPD billing, ICU monitor integrations, TPA insurance claims, and pharmacy POS.",
                "keywords": "hospital software cantonment trichy, hms software trichy 620001, clinic software trichy, tpa billing software trichy, I Info Vision"
            },
            {
                "file": "retail-billing-software-srirangam-trichy.html",
                "locality": "Srirangam",
                "pincode": "620006",
                "industry": "Tourism, Hotel PMS & Retail Store Billing",
                "headline": "Hotel PMS, Tourism &amp; Retail Billing Software in Srirangam",
                "desc": "Cloud hotel room reservation software, restaurant KOT billing, temple flower/crafts retail POS, and guest check-in software for establishments in Srirangam, Trichy.",
                "keywords": "hotel software srirangam, retail billing srirangam 620006, restaurant pos srirangam trichy, lodge billing software srirangam, I Info Vision"
            },
            {
                "file": "engineering-fabrication-erp-thuvakudi-trichy.html",
                "locality": "Thuvakudi & BHEL Zone",
                "pincode": "620015",
                "industry": "Heavy Fabrication & Boiler Ancillary ERP",
                "headline": "Heavy Engineering &amp; Boiler Fabrication ERP in Thuvakudi, Trichy",
                "desc": "Custom ERP for BHEL ancillary fabrication units. Raw plate nesting, welding quality test reports (NDT), heat number tracking, and automated dispatch challans in Thuvakudi.",
                "keywords": "fabrication erp thuvakudi, bhel ancillary software 620015, heavy engineering software trichy, boiler fabrication software, I Info Vision"
            },
            {
                "file": "railway-logistics-software-golden-rock-trichy.html",
                "locality": "Golden Rock (Ponmalai)",
                "pincode": "620004",
                "industry": "Fleet Telematics & Locomotive Logistics IT",
                "headline": "Logistics, Transporters &amp; Fleet Telematics in Golden Rock, Trichy",
                "desc": "Fleet tracking, heavy mechanical workshop job card management, equipment leasing software, and spare parts ERP in Golden Rock / Ponmalai, Trichy.",
                "keywords": "logistics software golden rock, transport telematics trichy 620004, workshop software ponmalai, fleet erp trichy, I Info Vision"
            },
            {
                "file": "school-college-erp-kk-nagar-trichy.html",
                "locality": "KK Nagar",
                "pincode": "620021",
                "industry": "Educational Institution ERP & Student Portals",
                "headline": "School &amp; College Management Software in KK Nagar, Trichy",
                "desc": "Smart campus ERP with student online admission, biometric attendance, school bus GPS tracking, LMS exam portals, and automated fee collection in KK Nagar.",
                "keywords": "school software kk nagar trichy, college erp trichy 620021, school bus gps software, education app trichy, I Info Vision"
            },
            {
                "file": "agro-fabrication-software-manapparai-trichy.html",
                "locality": "Manapparai",
                "pincode": "621306",
                "industry": "Food Processing, Snack Manufacturing & Cattle Mandi",
                "headline": "Murukku Snack Factory &amp; Cattle Mandi Billing in Manapparai",
                "desc": "Batch recipe costing, oil frying logs, retail distribution packaging, and weekly livestock auction billing software for Manapparai's famous food & cattle trade.",
                "keywords": "food processing software manapparai, murukku factory billing 621306, cattle mandi software trichy, retail pos manapparai, I Info Vision"
            },
            {
                "file": "rice-mill-erp-manachanallur-trichy.html",
                "locality": "Manachanallur",
                "pincode": "621005",
                "industry": "Ponni Rice Mill & Grain Processing ERP",
                "headline": "Ponni Rice Mill &amp; Grain Processing ERP in Manachanallur",
                "desc": "Paddy procurement weighbridge automation, moisture testing percentage, milling yield percentage, bran/husk byproduct sales, and GST e-invoicing for Manachanallur rice mills.",
                "keywords": "rice mill erp manachanallur, grain processing software 621005, paddy weighbridge software trichy, ponni rice billing software, I Info Vision"
            },
            {
                "file": "software-web-development-lalgudi-trichy.html",
                "locality": "Lalgudi",
                "pincode": "621601",
                "industry": "Agro-Trading & Commercial Web Development",
                "headline": "Software Company &amp; Web Development in Lalgudi, Trichy",
                "desc": "Custom software development, agricultural trade billing, school portals, and high-speed web design for commercial businesses across Lalgudi taluk.",
                "keywords": "web development lalgudi, software company lalgudi 621601, billing software lalgudi trichy, website design lalgudi, I Info Vision"
            }
        ]
    }
}

# ==================== SHARED HEADER & FOOTER ====================

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

def get_footer_html(city_name, hub_link):
    return f"""  <!-- FOOTER -->
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
            A proud Yasmeen Group Company transforming business operations across {city_name} and Tamil Nadu through enterprise software, custom ERP, GST POS billing systems, and responsive website development.
          </p>
        </div>
        <div>
          <h4 class="footer-heading">Regional Services</h4>
          <ul class="footer-links">
            <li><a href="services.html">All Software Solutions</a></li>
            <li><a href="billing-software.html">GST Billing &amp; POS</a></li>
            <li><a href="crm-erp-software.html">Custom ERP Systems</a></li>
            <li><a href="web-development.html">Website &amp; Web Apps</a></li>
            <li><a href="mobile-app-development.html">Mobile App Engineering</a></li>
            <li><a href="{hub_link}">{city_name} Pincode Hub</a></li>
          </ul>
        </div>
        <div>
          <h4 class="footer-heading">Regional Directories</h4>
          <ul class="footer-links">
            <li><a href="salem-pincode-it-directory.html">Salem Pincode Hub</a></li>
            <li><a href="erode-pincode-it-directory.html">Erode Pincode Hub</a></li>
            <li><a href="karur-pincode-it-directory.html">Karur Pincode Hub</a></li>
            <li><a href="namakkal-pincode-it-directory.html">Namakkal Pincode Hub</a></li>
            <li><a href="rasipuram-it-directory.html">Rasipuram Directory</a></li>
            <li><a href="trichy-pincode-it-directory.html">Trichy Pincode Hub</a></li>
          </ul>
        </div>
        <div>
          <h4 class="footer-heading">Headquarters &amp; Support</h4>
          <div class="footer-contact-item">
            <div class="footer-contact-icon"><i class="ph ph-map-pin"></i></div>
            <div class="footer-contact-text">
              <span class="label">Tamil Nadu Operations</span>
              <span>#9/136, No.1, First Floor, Trichy Main Road, Dasanaickenpatti, Salem &ndash; 636201</span>
            </div>
          </div>
          <div class="footer-contact-item">
            <div class="footer-contact-icon"><i class="ph ph-phone"></i></div>
            <div class="footer-contact-text">
              <span class="label">Direct Hotline / WhatsApp</span>
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
          <a href="directory.html">All Locations Directory</a>
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

# ==================== BUILD MASTER HUB PAGE FOR EACH REGION ====================

def generate_regional_hub(region_key, data):
    city_name = data["city_name"]
    hub_file = data["hub_file"]
    title = data["title"]
    lat, lng = data["geo"]
    pincodes = data["pincodes"]
    localities = data["localities"]

    rows_html = ""
    schema_areas = []

    for loc, pin, desc in pincodes:
        schema_areas.append({
            "@type": "AdministrativeArea",
            "name": f"{loc}, {city_name} {pin}",
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
              <a href="https://wa.me/919894480585?text=Hi%20I%20Info%20Vision,%20I%20need%20software/web%20services%20in%20{loc}%20({city_name}%20Pin%20{pin})" target="_blank" class="btn btn-primary" style="padding: 6px 14px; font-size: 12.5px; border-radius: 6px; text-decoration: none; display: inline-flex; align-items: center; gap: 5px;">
                <i class="ph ph-whatsapp-logo"></i> Instant Quote
              </a>
            </td>
          </tr>\n"""

    prime_cards_html = ""
    for loc in localities:
        prime_cards_html += f"""        <div style="background: #ffffff; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 22px; transition: transform 0.2s, box-shadow 0.2s;" onmouseover="this.style.transform='translateY(-4px)';this.style.boxShadow='0 10px 20px rgba(0,0,0,0.06)'" onmouseout="this.style.transform='translateY(0)';this.style.boxShadow='none'">
          <div style="display: flex; justify-content: space-between; align-items: flex-start; margin-bottom: 12px;">
            <span style="background: #e0f2fe; color: #0369a1; font-weight: 700; font-size: 12px; padding: 4px 10px; border-radius: 6px;">PIN: {loc['pincode']}</span>
            <i class="ph ph-seal-check" style="color: #0284c7; font-size: 20px;"></i>
          </div>
          <h3 style="font-size: 17px; font-weight: 800; color: #0f172a; margin-bottom: 8px;">{loc['locality']}</h3>
          <p style="color: #64748b; font-size: 13.5px; line-height: 1.5; margin-bottom: 16px;">{loc['headline']}</p>
          <a href="{loc['file']}" style="color: #0284c7; font-weight: 700; font-size: 13.5px; text-decoration: none; display: inline-flex; align-items: center; gap: 6px;">
            View Dedicated Locality Solutions <i class="ph ph-arrow-right"></i>
          </a>
        </div>\n"""

    schema_json = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.iinfovision.com/" },
                    { "@type": "ListItem", "position": 2, "name": f"{city_name} Hub", "item": f"https://www.iinfovision.com/{hub_file}" }
                ]
            },
            {
                "@type": "LocalBusiness",
                "name": f"I Info Vision - {city_name} District Software & IT Hub",
                "url": f"https://www.iinfovision.com/{hub_file}",
                "telephone": "+919894480585",
                "priceRange": "₹₹",
                "image": "https://www.iinfovision.com/assets/images/logo.webp",
                "address": {
                    "@type": "PostalAddress",
                    "streetAddress": "Regional Operations Hub",
                    "addressLocality": city_name,
                    "addressRegion": "Tamil Nadu",
                    "addressCountry": "IN"
                },
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": lat,
                    "longitude": lng
                },
                "areaServed": schema_areas,
                "description": f"Comprehensive IT services, custom software, ERP, billing POS, and website development covering all delivery post offices and pincodes in {city_name} district, Tamil Nadu."
            },
            {
                "@type": "FAQPage",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": f"Does I Info Vision provide direct on-site software installation in {city_name}?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": f"Yes, I Info Vision deploys technical engineers directly to shops, factories, schools, and offices across all localities and postal codes in {city_name} district for hands-on setup, staff training, and data migration."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": f"What software solutions are provided in {city_name}?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": f"We deliver GST billing software, supermarket POS, custom manufacturing and textile ERP, hospital management systems (HMS), fleet logistics software, and responsive web design tailored to {city_name}'s leading industries."
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
  <title>{title} | I Info Vision</title>
  <meta name="description" content="{city_name} District Postal Pincode IT Services Directory. Lookup software development, website design, GST billing POS, and ERP solutions across all post offices in {city_name}, Tamil Nadu." />
  <meta name="keywords" content="{city_name.lower()} pincode list, {city_name.lower()} post office software, software company {city_name.lower()}, web development {city_name.lower()}, billing software {city_name.lower()}, erp software {city_name.lower()}, I Info Vision" />
  <meta name="author" content="I Info Vision" />
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1" />
  <meta name="geo.region" content="IN-TN" />
  <meta name="geo.placename" content="{city_name}, Tamil Nadu" />
  <meta name="geo.position" content="{lat};{lng}" />
  <meta name="ICBM" content="{lat}, {lng}" />
  <link rel="canonical" href="https://www.iinfovision.com/{hub_file}" />

  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website" />
  <meta property="og:url" content="https://www.iinfovision.com/{hub_file}" />
  <meta property="og:site_name" content="I Info Vision" />
  <meta property="og:locale" content="en_IN" />
  <meta property="og:title" content="{title} | I Info Vision" />
  <meta property="og:description" content="Search all post offices and pincodes in {city_name} district for custom software development, website design, and GST billing systems with direct on-site support." />
  <meta property="og:image" content="https://www.iinfovision.com/assets/images/logo.webp" />

  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:url" content="https://www.iinfovision.com/{hub_file}" />
  <meta name="twitter:title" content="{city_name} District IT &amp; Software Pincode Directory | I Info Vision" />
  <meta name="twitter:description" content="Search all post offices and pincodes in {city_name} district for custom software development, website design, and GST billing systems." />
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
          <a href="directory.html" style="color: #94a3b8;">Directories</a>
          <i class="ph ph-caret-right"></i>
          <span style="color: #38bdf8;">{city_name} Pincode Hub</span>
        </div>
        <div style="display: inline-block; background: rgba(56, 189, 248, 0.15); border: 1px solid rgba(56, 189, 248, 0.4); color: #38bdf8; font-size: 12.5px; font-weight: 700; padding: 6px 16px; border-radius: 20px; margin-bottom: 20px;">
          <i class="ph ph-buildings"></i> {city_name} District 100% Pincode Coverage
        </div>
        <h1 class="page-hero-title" style="font-size: clamp(28px, 4.5vw, 44px); font-weight: 800; line-height: 1.25; margin-bottom: 20px;">
          {city_name} District IT &amp; Software <span class="highlight">Pincode Directory</span>
        </h1>
        <p class="page-hero-desc" style="font-size: 16.5px; line-height: 1.7; color: #cbd5e1; max-width: 780px; margin: 0 auto 30px auto;">
          Looking for trusted software developers, website designers, or GST billing software in your {city_name} neighborhood? Search below by pincode or locality for instant on-site technical support.
        </p>
        
        <!-- Live Search Input -->
        <div style="max-width: 600px; margin: 0 auto; position: relative;">
          <div style="display: flex; align-items: center; background: #ffffff; border-radius: 12px; padding: 6px 16px; box-shadow: 0 8px 30px rgba(0,0,0,0.25);">
            <i class="ph ph-magnifying-glass" style="font-size: 22px; color: #0284c7; margin-right: 10px;"></i>
            <input type="text" id="pincodeSearch" placeholder="Type pincode or locality name..." style="width: 100%; border: none; outline: none; font-size: 15px; color: #0f172a; padding: 10px 0; font-family: inherit;" onkeyup="filterPincodes()" />
          </div>
          <span style="color: #94a3b8; font-size: 12.5px; margin-top: 10px; display: block;">Instant live filter covering all delivery post offices in {city_name} district</span>
        </div>
      </div>
    </div>
  </section>

  <!-- ON-SITE SERVICE GUARANTEE BADGE -->
  <section style="background: #f0fdf4; border-bottom: 1.5px solid #bbf7d0; padding: 18px 0;">
    <div class="container" style="display: flex; flex-wrap: wrap; align-items: center; justify-content: center; gap: 24px; text-align: center;">
      <div style="display: flex; align-items: center; gap: 8px; color: #166534; font-weight: 700; font-size: 14.5px;">
        <i class="ph ph-lightning" style="font-size: 22px; color: #15803d;"></i> Same-Day On-Site Engineer Dispatch
      </div>
      <div style="display: flex; align-items: center; gap: 8px; color: #166534; font-weight: 700; font-size: 14.5px;">
        <i class="ph ph-shield-check" style="font-size: 22px; color: #15803d;"></i> 100% Data Migration &amp; GST Compliance
      </div>
      <div style="display: flex; align-items: center; gap: 8px; color: #166534; font-weight: 700; font-size: 14.5px;">
        <i class="ph ph-phone-call" style="font-size: 22px; color: #15803d;"></i> Direct Engineer Support: +91 98944 80585
      </div>
    </div>
  </section>

  <!-- PRIME COMMERCIAL HUBS SHOWCASE -->
  <section style="padding: 60px 0 40px 0; background: #f8fafc;">
    <div class="container">
      <div style="text-align: center; max-width: 700px; margin: 0 auto 40px auto;">
        <h2 style="font-size: 28px; font-weight: 800; color: #0f172a; margin-bottom: 12px;">Prime Commercial &amp; Industrial Hubs in {city_name}</h2>
        <p style="color: #64748b; font-size: 15.5px;">Specialized software architectures built for {city_name}'s largest economic clusters.</p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 20px;">
{prime_cards_html}
      </div>
    </div>
  </section>

  <!-- MASTER PINCODE DIRECTORY TABLE -->
  <section style="padding: 60px 0; background: #ffffff;">
    <div class="container">
      <div style="display: flex; justify-content: space-between; align-items: center; flex-wrap: wrap; gap: 15px; margin-bottom: 25px;">
        <div>
          <h2 style="font-size: 24px; font-weight: 800; color: #0f172a;">All Delivery Post Offices &amp; Pincodes in {city_name}</h2>
          <p style="color: #64748b; font-size: 14px; margin-top: 4px;">Verified directory of active post offices, commercial sectors, and direct IT support.</p>
        </div>
        <div style="font-size: 13.5px; font-weight: 600; color: #0284c7; background: #f0f9ff; padding: 6px 14px; border-radius: 20px; border: 1px solid #bae6fd;">
          Showing: <span id="matchCount">{len(pincodes)}</span> Localities
        </div>
      </div>

      <div style="overflow-x: auto; background: #ffffff; border-radius: 12px; border: 1.5px solid #e2e8f0; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.02);">
        <table style="width: 100%; border-collapse: collapse; text-align: left;" id="pincodeTable">
          <thead>
            <tr style="background: #0f172a; color: #ffffff; font-size: 13.5px; text-transform: uppercase; letter-spacing: 0.5px;">
              <th style="padding: 16px 18px;">Post Office / Locality</th>
              <th style="padding: 16px 18px;">Pincode</th>
              <th style="padding: 16px 18px;">Commercial &amp; Industry Profile</th>
              <th style="padding: 16px 18px; text-align: right;">Action</th>
            </tr>
          </thead>
          <tbody>
{rows_html}
          </tbody>
        </table>
      </div>
    </div>
  </section>

  <!-- FAQ SECTION -->
  <section style="padding: 60px 0; background: #f8fafc; border-top: 1px solid #e2e8f0;">
    <div class="container" style="max-width: 800px;">
      <h2 style="font-size: 28px; font-weight: 800; color: #0f172a; text-align: center; margin-bottom: 30px;">Frequently Asked Questions ({city_name} IT Services)</h2>
      
      <div style="display: flex; flex-direction: column; gap: 16px;">
        <div style="background: #ffffff; padding: 22px; border-radius: 12px; border: 1px solid #e2e8f0;">
          <h3 style="font-size: 17px; font-weight: 700; color: #0f172a; margin-bottom: 8px;">Does I Info Vision provide on-site software installation in {city_name}?</h3>
          <p style="color: #475569; font-size: 14.5px; line-height: 1.6; margin: 0;">Yes, our senior engineers provide direct on-site setup, hardware integration (barcode scanners, thermal printers, weighing scales), and staff training across all localities in {city_name} district.</p>
        </div>
        <div style="background: #ffffff; padding: 22px; border-radius: 12px; border: 1px solid #e2e8f0;">
          <h3 style="font-size: 17px; font-weight: 700; color: #0f172a; margin-bottom: 8px;">How can I migrate my existing business data to I Info Vision ERP?</h3>
          <p style="color: #475569; font-size: 14.5px; line-height: 1.6; margin: 0;">We provide 100% seamless historical data migration from Tally, Excel sheets, Marg, or older desktop software with zero business downtime and complete accuracy validation.</p>
        </div>
      </div>
    </div>
  </section>

  <script>
    function filterPincodes() {{
      const input = document.getElementById('pincodeSearch').value.toLowerCase();
      const table = document.getElementById('pincodeTable');
      const trs = table.getElementsByTagName('tr');
      let count = 0;

      for (let i = 1; i < trs.length; i++) {{
        const rowText = trs[i].innerText.toLowerCase();
        if (rowText.includes(input)) {{
          trs[i].style.display = '';
          count++;
        }} else {{
          trs[i].style.display = 'none';
        }}
      }}
      document.getElementById('matchCount').innerText = count;
    }}
  </script>

{get_footer_html(city_name, hub_file)}"""

# ==================== BUILD INDIVIDUAL LOCALITY LANDING PAGES ====================

def generate_locality_page(region_key, region_data, loc_data):
    city_name = region_data["city_name"]
    hub_file = region_data["hub_file"]
    lat, lng = region_data["geo"]

    target_file = loc_data["file"]
    locality = loc_data["locality"]
    pincode = loc_data["pincode"]
    industry = loc_data["industry"]
    headline = loc_data["headline"]
    desc = loc_data["desc"]
    keywords = loc_data["keywords"]

    schema_json = {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    { "@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.iinfovision.com/" },
                    { "@type": "ListItem", "position": 2, "name": f"{city_name} Pincodes", "item": f"https://www.iinfovision.com/{hub_file}" },
                    { "@type": "ListItem", "position": 3, "name": locality, "item": f"https://www.iinfovision.com/{target_file}" }
                ]
            },
            {
                "@type": "LocalBusiness",
                "name": f"I Info Vision - {industry} in {locality}",
                "url": f"https://www.iinfovision.com/{target_file}",
                "telephone": "+919894480585",
                "priceRange": "₹₹",
                "image": "https://www.iinfovision.com/assets/images/logo.webp",
                "address": {
                    "@type": "PostalAddress",
                    "streetAddress": f"{locality} Commercial Zone",
                    "addressLocality": city_name,
                    "addressRegion": "Tamil Nadu",
                    "postalCode": pincode,
                    "addressCountry": "IN"
                },
                "geo": {
                    "@type": "GeoCoordinates",
                    "latitude": lat,
                    "longitude": lng
                },
                "description": desc
            },
            {
                "@type": "FAQPage",
                "mainEntity": [
                    {
                        "@type": "Question",
                        "name": f"Why choose I Info Vision for {industry} in {locality}?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": f"I Info Vision provides customized software built specifically for {locality}'s business workflows with on-site deployment, barcode/thermal printer setup, and direct WhatsApp engineer support."
                        }
                    },
                    {
                        "@type": "Question",
                        "name": f"How fast can on-site installation be completed in {locality} ({pincode})?",
                        "acceptedAnswer": {
                            "@type": "Answer",
                            "text": f"We provide same-day on-site engineer dispatch for clients in {locality} ({pincode}) with complete staff training."
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
  <title>{industry} in {locality}, {city_name} ({pincode}) | I Info Vision</title>
  <meta name="description" content="{desc}" />
  <meta name="keywords" content="{keywords}" />
  <meta name="author" content="I Info Vision" />
  <meta name="robots" content="index, follow, max-snippet:-1, max-image-preview:large, max-video-preview:-1" />
  <meta name="geo.region" content="IN-TN" />
  <meta name="geo.placename" content="{locality}, {city_name}, Tamil Nadu" />
  <meta name="geo.position" content="{lat};{lng}" />
  <meta name="ICBM" content="{lat}, {lng}" />
  <link rel="canonical" href="https://www.iinfovision.com/{target_file}" />

  <!-- Open Graph / Facebook -->
  <meta property="og:type" content="website" />
  <meta property="og:url" content="https://www.iinfovision.com/{target_file}" />
  <meta property="og:site_name" content="I Info Vision" />
  <meta property="og:locale" content="en_IN" />
  <meta property="og:title" content="{industry} in {locality}, {city_name} | I Info Vision" />
  <meta property="og:description" content="{desc}" />
  <meta property="og:image" content="https://www.iinfovision.com/assets/images/logo.webp" />

  <!-- Twitter -->
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:url" content="https://www.iinfovision.com/{target_file}" />
  <meta name="twitter:title" content="{industry} in {locality}, {city_name} | I Info Vision" />
  <meta name="twitter:description" content="{desc}" />
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
      <div class="page-hero-inner" style="max-width: 860px; margin: 0 auto; text-align: center;">
        <div class="page-breadcrumb" style="justify-content: center; margin-bottom: 18px; color: #94a3b8; font-size: 13px;">
          <a href="index.html" style="color: #94a3b8;">Home</a>
          <i class="ph ph-caret-right"></i>
          <a href="{hub_file}" style="color: #94a3b8;">{city_name} Pincodes</a>
          <i class="ph ph-caret-right"></i>
          <span style="color: #38bdf8;">{locality}</span>
        </div>
        <div style="display: inline-block; background: rgba(56, 189, 248, 0.15); border: 1px solid rgba(56, 189, 248, 0.4); color: #38bdf8; font-size: 12.5px; font-weight: 700; padding: 6px 16px; border-radius: 20px; margin-bottom: 20px;">
          <i class="ph ph-map-pin"></i> {locality} &bull; Pincode {pincode}
        </div>
        <h1 class="page-hero-title" style="font-size: clamp(28px, 4.5vw, 42px); font-weight: 800; line-height: 1.25; margin-bottom: 20px;">
          {headline}
        </h1>
        <p class="page-hero-desc" style="font-size: 16.5px; line-height: 1.7; color: #cbd5e1; max-width: 760px; margin: 0 auto 30px auto;">
          {desc}
        </p>
        <div style="display: flex; gap: 14px; justify-content: center; flex-wrap: wrap;">
          <a href="https://wa.me/919894480585?text=Hi%20I%20Info%20Vision,%20I%20need%20software%20services%20in%20{locality}%20({pincode})" target="_blank" class="btn btn-primary" style="padding: 12px 28px; border-radius: 8px; font-weight: 700;">
            <i class="ph ph-whatsapp-logo"></i> Instant WhatsApp Quote
          </a>
          <a href="tel:+919894480585" class="btn btn-secondary" style="padding: 12px 28px; border-radius: 8px; font-weight: 700; background: rgba(255,255,255,0.1); color: #ffffff; border: 1px solid rgba(255,255,255,0.2);">
            <i class="ph ph-phone"></i> Call Senior Engineer
          </a>
        </div>
      </div>
    </div>
  </section>

  <!-- FEATURES / CORE VALUE -->
  <section style="padding: 60px 0; background: #ffffff;">
    <div class="container">
      <div style="text-align: center; max-width: 700px; margin: 0 auto 40px auto;">
        <h2 style="font-size: 28px; font-weight: 800; color: #0f172a; margin-bottom: 12px;">Tailor-Made Solutions for {locality} Businesses</h2>
        <p style="color: #64748b; font-size: 15.5px;">Engineered specifically to solve the real operational, GST compliance, and growth challenges of {locality} ({pincode}).</p>
      </div>

      <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 24px;">
        <div style="background: #f8fafc; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 26px;">
          <div style="background: #e0f2fe; width: 48px; height: 48px; border-radius: 10px; display: flex; align-items: center; justify-content: center; color: #0284c7; font-size: 24px; margin-bottom: 16px;">
            <i class="ph ph-lightning"></i>
          </div>
          <h3 style="font-size: 18px; font-weight: 700; color: #0f172a; margin-bottom: 8px;">Direct On-Site Engineer Dispatch</h3>
          <p style="color: #64748b; font-size: 14px; line-height: 1.6; margin: 0;">Our technicians come directly to your shop or factory in {locality} for installation, barcode hardware integration, and complete staff training.</p>
        </div>

        <div style="background: #f8fafc; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 26px;">
          <div style="background: #e0f2fe; width: 48px; height: 48px; border-radius: 10px; display: flex; align-items: center; justify-content: center; color: #0284c7; font-size: 24px; margin-bottom: 16px;">
            <i class="ph ph-receipt"></i>
          </div>
          <h3 style="font-size: 18px; font-weight: 700; color: #0f172a; margin-bottom: 8px;">100% Automated GST &amp; E-Invoicing</h3>
          <p style="color: #64748b; font-size: 14px; line-height: 1.6; margin: 0;">Generate government-compliant GST tax invoices, QR codes, e-way bills, and automated GSTR-1 / GSTR-3B monthly reports with one click.</p>
        </div>

        <div style="background: #f8fafc; border: 1.5px solid #e2e8f0; border-radius: 12px; padding: 26px;">
          <div style="background: #e0f2fe; width: 48px; height: 48px; border-radius: 10px; display: flex; align-items: center; justify-content: center; color: #0284c7; font-size: 24px; margin-bottom: 16px;">
            <i class="ph ph-database"></i>
          </div>
          <h3 style="font-size: 18px; font-weight: 700; color: #0f172a; margin-bottom: 8px;">Zero-Downtime Data Migration</h3>
          <p style="color: #64748b; font-size: 14px; line-height: 1.6; margin: 0;">Easily migrate your full historical customer ledgers, inventory balances, and supplier accounts from Tally, Excel, or older legacy software.</p>
        </div>
      </div>
    </div>
  </section>

  <!-- CTA BANNER -->
  <section style="padding: 50px 0; background: linear-gradient(135deg, #0284c7 0%, #0369a1 100%); color: #ffffff; text-align: center;">
    <div class="container" style="max-width: 750px;">
      <h2 style="font-size: 28px; font-weight: 800; margin-bottom: 14px; color: #ffffff;">Upgrade Your Business in {locality} ({pincode}) Today</h2>
      <p style="color: #e0f2fe; font-size: 16px; margin-bottom: 24px;">Schedule a free live software demo at your premises or request an instant quotation over WhatsApp.</p>
      <a href="https://wa.me/919894480585?text=Hi%20I%20Info%20Vision,%20I%20want%20to%20schedule%20a%20demo%20in%20{locality}%20({pincode})" target="_blank" class="btn" style="background: #ffffff; color: #0369a1; padding: 14px 32px; border-radius: 8px; font-weight: 800; text-decoration: none; font-size: 15px; display: inline-flex; align-items: center; gap: 8px;">
        <i class="ph ph-whatsapp-logo"></i> Book Free Demo on WhatsApp
      </a>
    </div>
  </section>

{get_footer_html(city_name, hub_file)}"""

# ==================== MAIN RUNNER ====================

def main():
    generated_files = []

    print("Generating Regional Master Pincode Hubs and Locality Landing Pages...")

    for region_key, rdata in REGIONAL_HUBS.items():
        # 1. Master Hub
        hub_html = generate_regional_hub(region_key, rdata)
        hub_path = os.path.join(WORKSPACE, rdata["hub_file"])
        with open(hub_path, "w", encoding="utf-8") as f:
            f.write(hub_html)
        generated_files.append(rdata["hub_file"])
        print(f"Generated {rdata['hub_file']}")

        # 2. Locality Pages
        for loc_data in rdata["localities"]:
            loc_html = generate_locality_page(region_key, rdata, loc_data)
            loc_path = os.path.join(WORKSPACE, loc_data["file"])
            with open(loc_path, "w", encoding="utf-8") as f:
                f.write(loc_html)
            generated_files.append(loc_data["file"])
            print(f"  -> Generated {loc_data['file']}")

    print(f"\nTotal new Regional Pages created: {len(generated_files)}")

    # ==================== UPDATE SITEMAP.XML ====================
    sitemap_path = os.path.join(WORKSPACE, "sitemap.xml")
    if os.path.exists(sitemap_path):
        with open(sitemap_path, "r", encoding="utf-8") as f:
            sitemap_content = f.read()

        added_urls = 0
        sitemap_additions = ""
        for fn in generated_files:
            url_str = f"https://www.iinfovision.com/{fn}"
            if url_str not in sitemap_content:
                sitemap_additions += f"""  <url>
    <loc>{url_str}</loc>
    <lastmod>2026-10-16</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>\n"""
                added_urls += 1

        if added_urls > 0:
            updated_sitemap = sitemap_content.replace("</urlset>", sitemap_additions + "</urlset>")
            with open(sitemap_path, "w", encoding="utf-8") as f:
                f.write(updated_sitemap)
            print(f"Added {added_urls} URLs to sitemap.xml!")
            count = len(re.findall(r'<loc>', updated_sitemap))
            print(f"NEW TOTAL URLS IN SITEMAP: {count} URLs!")

if __name__ == "__main__":
    main()
