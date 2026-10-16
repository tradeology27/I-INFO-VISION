"""
Industry-vertical software solutions definitions.
18 specialized software products.
"""

INDUSTRY_DATA = [
    {
        "filename": "hospital-management-software.html",
        "name": "Hospital Management Software (HMS)",
        "category": "Healthcare IT & HMS",
        "title": "Best Hospital Management Software (HMS) in Tamil Nadu | I Info Vision",
        "desc": "Enterprise NABH-ready Hospital Management Software. Manage OPD queue, IPD admissions, pharmacy inventory, laboratory test reporting, and doctor scheduling.",
        "keywords": "hospital management software, hms software tamil nadu, hospital erp software, clinic software, doctor prescription software, pharmacy billing, laboratory software",
        "badge": "NABH-Compliant Healthcare ERP",
        "hero_title": "Enterprise <span class='highlight'>Hospital Management Software</span>",
        "hero_desc": "Digitize patient journeys from reception registration to discharge summary. Accelerate consultations, eliminate pharmacy stock-outs, and ensure 100% NABH compliance.",
        "client_ref": "project-kumar-hospital-billing.html",
        "client_name": "Kumar Hospital Billing & HMS",
        "client_summary": "Engineered automated bed allocation, lab test integration, and daily revenue reconciliation.",
        "deliverables": [
            ("Digital OPD Registration & EMR", "Fast patient lookup by mobile number, digital queue token display, vitals capture, and paperless prescription writing with IC-10 codes."),
            ("IPD Admission, Bed Grid & Nursing", "Visual bed occupancy matrix, room tariff automation, daily nursing drug administration sheets, and automated discharge bill consolidation."),
            ("Laboratory Information System (LIS)", "Custom test report templates with automatic normal/abnormal parameter highlighting, barcode sample labels, and WhatsApp report delivery."),
            ("Pharmacy POS & Expiry Management", "Prescription auto-fetching, batch number and expiry date enforcement, narcotics register, and automated purchase reorder triggers."),
            ("Insurance & Cashless TPA Module", "Track pre-authorization approvals, co-pay calculations, TPA documentation, and pending insurance claims settlement aging."),
            ("Doctor Scheduling & Telemedicine", "Doctor duty roster, online consultation slot booking via hospital website, and video consultation capabilities.")
        ],
        "faqs": [
            ("Is your Hospital Management Software NABH compliant?", "Yes, our HMS includes standard clinical audit trails, patient consent archiving, incident reporting, and role-based data encryption required for NABH accreditation."),
            ("Can it integrate with our diagnostic laboratory machines (Biochemistry, Hematology)?", "Yes, we interface directly via ASTM / HL7 protocols with automated analyzer machines to capture test results directly without manual typing errors."),
            ("Does it support WhatsApp integration for patient reports?", "Yes, once authorized by the lab technician, patients receive automated WhatsApp messages with direct PDF download links."),
            ("Can the software handle multiple hospital branches?", "Yes, centralized multi-hospital architecture lets management view consolidated patient census, doctor occupancy, and pharmacy inventory across all branches.")
        ]
    },
    {
        "filename": "clinic-management-software.html",
        "name": "Clinic Management Software",
        "category": "Healthcare IT",
        "title": "Best Clinic Management Software for Doctors in Tamil Nadu | I Info Vision",
        "desc": "Smart clinic management software for single and multi-doctor polyclinics. Fast digital prescriptions, appointment scheduling, patient history, and billing.",
        "keywords": "clinic management software, doctor prescription software, opd software for doctors, polyclinic software, patient appointment software",
        "badge": "Smart Clinic OS",
        "hero_title": "Smart <span class='highlight'>Clinic Management Software</span>",
        "hero_desc": "Designed specifically for doctors and polyclinics. Write digital prescriptions in 30 seconds, manage patient queues, and access complete medical history on any device.",
        "client_ref": "project-knch-karur.html",
        "client_name": "KNCH Karur Clinical Portal",
        "client_summary": "Integrated patient therapy scheduling, doctor consultation archives, and appointment confirmations.",
        "deliverables": [
            ("30-Second Prescription Builder", "Pre-configured medicine templates with dosage, frequency, instructions in Tamil/English, and print on branded doctor letterhead."),
            ("Patient Appointment & Queue Display", "Online booking via website/WhatsApp, automated SMS appointment reminders, and waiting room TV token display."),
            ("Complete Patient EMR History", "Instant chronological timeline of all past visits, vitals trends, uploaded X-rays/scans, and chronic condition alerts (Diabetes, BP)."),
            ("Quick Consultation Billing", "Instant thermal or A5 consultation fee receipts with UPI QR code payment and daily collection reports."),
            ("Vaccination & Follow-Up Tracker", "Automated pediatric immunization schedules and patient follow-up reminders via WhatsApp."),
            ("Multi-Doctor Polyclinic Accounts", "Individual doctor revenue sharing calculations, consultation fee splits, and procedure billing.")
        ],
        "faqs": [
            ("Can I use this software on an iPad or Android tablet?", "Yes, the doctor interface is fully touch-optimized for tablets, iPads, laptops, and desktop computers."),
            ("Can I print prescriptions in Tamil for patients?", "Yes, medicine dosage instructions (e.g., காலை, மதியம், இரவு சாப்பாட்டிற்கு பின்) print clearly in Tamil or English."),
            ("How secure is my patients' confidential medical data?", "Data is protected with bank-grade 256-bit AES encryption, strictly accessible only by authorized clinic doctors."),
            ("Does it need high-speed internet to work?", "No, it features offline failover mode so you can continue consulting patients even during internet dropouts.")
        ]
    },
    {
        "filename": "pharmacy-billing-software.html",
        "name": "Pharmacy Billing Software",
        "category": "Retail & Pharma",
        "title": "Best Pharmacy Billing Software & Medical Shop POS | I Info Vision",
        "desc": "Top pharmacy billing software in Tamil Nadu. Fast barcode checkout, batch-wise expiry tracking, schedule H/H1 drug register, and automated purchase import.",
        "keywords": "pharmacy billing software, medical shop software, chemist billing pos, drug expiry management software, gst pharmacy software",
        "badge": "Sub-Second Pharma POS",
        "hero_title": "GST <span class='highlight'>Pharmacy Billing Software</span>",
        "hero_desc": "Eliminate medicine expiry losses, speed up counter billing, and manage 50,000+ medicine master records with I Info Vision's advanced pharmacy billing software.",
        "client_ref": "project-kumar-hospital-billing.html",
        "client_name": "Hospital Pharmacy Counter Deployments",
        "client_summary": "Handled batch-wise price variants, automatic substitute drug suggestions, and schedule drug logs.",
        "deliverables": [
            ("Generic Substitute Drug Finder", "Instantly recommend alternative generic brands sharing identical chemical compositions when prescribed medicines are out of stock."),
            ("Batch & Expiry Date Enforcement", "FIFO (First In First Out) inventory enforcement automatically selects near-expiry batches first, blocking expired medicines at checkout."),
            ("Schedule H & H1 Regulatory Register", "Automated statutory register tracking patient name, doctor registration number, and prescription copy uploads for drug inspector audits."),
            ("1-Click Purchase CSV/XML Import", "Upload distributor invoices directly via CSV/Excel without manually entering individual medicine names, batches, and prices."),
            ("Rack & Shelf Locator", "Shows exact shelf and rack location on the billing screen so counter boys fetch medicines in seconds."),
            ("Customer WhatsApp Invoicing & Refill Alerts", "Send paperless bills directly to WhatsApp and trigger automated refill reminders for chronic medicine patients.")
        ],
        "faqs": [
            ("Does it include a pre-loaded medicine master database?", "Yes, it comes with over 60,000+ pre-loaded medicine brands, generic molecules, manufacturers, and GST rates ready for instant use."),
            ("How does it notify me of expiring medicines?", "You receive automated dashboard alerts 30, 60, and 90 days before expiry, allowing you to return stock to distributors on time."),
            ("Can it handle cut-strip (loose tablet) billing?", "Yes, it accurately calculates loose tablet prices and deducts exact strip fractions from inventory."),
            ("Can it connect with thermal receipt printers and barcode scanners?", "Yes, natively compatible with all 2-inch and 3-inch thermal printers, laser scanners, and barcode label sticker printers.")
        ]
    },
    {
        "filename": "supermarket-pos-billing-software.html",
        "name": "Supermarket POS Billing Software",
        "category": "Retail POS",
        "title": "Supermarket POS Billing Software in Tamil Nadu | I Info Vision",
        "desc": "High-speed supermarket POS software. Weighing scale integration, multi-counter billing, loyalty points, barcode scanning, and inventory control.",
        "keywords": "supermarket billing software, grocery pos software, retail pos system tamil nadu, weighing scale billing software, multi counter pos",
        "badge": "High-Volume Grocery POS",
        "hero_title": "Superfast <span class='highlight'>Supermarket POS Billing</span>",
        "hero_desc": "Keep checkout queues moving fast. Sub-second barcode scanning, weighing scale connectivity, and centralized multi-godown stock management for supermarkets.",
        "client_ref": "project-kumar-hospital-billing.html",
        "client_name": "High-Throughput Checkout Architecture",
        "client_summary": "Engineered sub-500ms transaction printing and daily cashier drawer balancing across multiple counters.",
        "deliverables": [
            ("Sub-Second Barcode Scanning", "Optimized checkout screen with hotkeys, barcode scanning, and multi-mode payment splits (Cash + UPI + Card)."),
            ("Electronic Weighing Scale Sync", "Automatic weight reading over RS232 / USB from scales for vegetables, fruits, grains, and dry fruits with zero manual typing."),
            ("Centralized Multi-Counter Balancing", "Manage 10+ billing counters simultaneously with individual cashier shift opening/closing cash drawer reconciliation."),
            ("Promotions, Offers & Combos Engine", "Automated Buy-1-Get-1, happy hour discounts, weekend flash sales, and customer membership loyalty reward points."),
            ("Purchase Order & Vendor Reorder Alerts", "Auto-generate purchase orders based on minimum stock levels and supplier lead times to prevent out-of-stock items."),
            ("Owner Mobile Real-Time App", "Monitor live daily sales, gross margin percentages, cash in hand, and cashier performance from your smartphone.")
        ],
        "faqs": [
            ("Can it handle continuous billing when the internet is disconnected?", "Yes, full offline-first functionality ensures checkout counters never stop billing even during total internet blackouts."),
            ("Can we print barcode price stickers for loose pulses and grains?", "Yes, print custom barcode stickers with item name, packed date, weight, and price directly from the software."),
            ("Does it prevent staff theft and cash drawer mismatches?", "Yes, cashier shift closing requires blind cash tallying, and voids/deletions require manager password authorization."),
            ("Can customers pay with split payments (Cash + UPI)?", "Yes, cashiers can split single bills across multiple tender modes including Google Pay, PhonePe, cash, and sodexo cards.")
        ]
    },
    {
        "filename": "textile-garment-erp-software.html",
        "name": "Textile & Garment ERP Software",
        "category": "Textile & Manufacturing",
        "title": "Textile & Garment Manufacturing ERP Software in Tamil Nadu | I Info Vision",
        "desc": "Comprehensive textile and apparel ERP software. Manage yarn procurement, weaving, dyeing batches, cutting lay, sewing lines, and export documentation.",
        "keywords": "textile erp software, garment erp software, apparel manufacturing erp, spinning mill software, weaving software, dyeing erp",
        "badge": "End-to-End Textile ERP",
        "hero_title": "Comprehensive <span class='highlight'>Textile & Garment ERP</span>",
        "hero_desc": "Engineered specifically for Tamil Nadu's textile hubs in Salem, Tirupur, Erode, and Karur. Eliminate yarn wastage, balance production lines, and meet export ship dates.",
        "client_ref": "project-knch-karur.html",
        "client_name": "Textile Enterprise Automation",
        "client_summary": "Automated order milestone tracking with real-time exception alerts and fulfillment validation.",
        "deliverables": [
            ("Yarn & Raw Material Inventory", "Track yarn inward by count, mill name, lot number, bag weight, and issue yarn to warping/sizing with shrinkage tracking."),
            ("Loom Weaving & Grey Fabric Audit", "Monitor powerloom and auto-loom efficiency, fabric roll inspection, 4-point defect grading, and weaver piece-rate wages."),
            ("Processing & Dyeing Recipe Management", "Formulate chemical recipes, track dyeing lot shades, shrinkage variances, and processing house delivery challans."),
            ("Garment Cutting & Sewing Line Efficiency", "Marker planning, lay sheet cut percentage, hourly bundle scanning, and real-time operator efficiency metrics."),
            ("Subcontractor Job Work Tracking", "Issue and track fabric sent to external printing, embroidery, and washing vendors with wastage reconciliation."),
            ("Export Shipment Packing Lists & Invoices", "Automated solid/assorted carton packing lists, container CBM calculations, HS code classification, and export commercial invoices.")
        ],
        "faqs": [
            ("Can it handle fabric stock in both meters and kilograms?", "Yes, our dual-unit conversion system tracks fabrics and yarns seamlessly in meters, rolls, and kilograms."),
            ("Does it generate detailed Pre-Costing vs Actual Costing reports?", "Yes, compare your initial target cost against actual fabric consumed, trim costs, overheads, and freight to calculate net order profitability."),
            ("Can it monitor power loom efficiency and weaver wages?", "Yes, track meters woven per shift, compute piece-rate wages for weavers, and identify loom breakdown hours."),
            ("Can multiple branches or godowns across Tamil Nadu be monitored?", "Yes, cloud synchronization allows owners to view consolidated stocks across multiple godowns and mills in real-time.")
        ]
    },
    {
        "filename": "school-management-software.html",
        "name": "School Management Software",
        "category": "Education IT",
        "title": "Smart School Management Software & Mobile App | I Info Vision",
        "desc": "Complete smart school management software with mobile app for parents and teachers. Online fee payment, student attendance, exams, and bus GPS tracking.",
        "keywords": "school management software, school erp software, student attendance app, online school fee payment, school bus gps tracking software",
        "badge": "Smart Campus Operating System",
        "hero_title": "Smart <span class='highlight'>School Management Software</span>",
        "hero_desc": "Empower your school with digital student admissions, automated fee receipting, biometric student attendance, examination report cards, and parent mobile apps.",
        "client_ref": "project-school-management.html",
        "client_name": "School Management System & App",
        "client_summary": "Deployed automated timetable generator, digital fee receipting, and parent mobile notification gateway.",
        "deliverables": [
            ("Online Admission & Student Records", "Paperless online admission forms, automated student roll number generation, document vaults, and TC generation."),
            ("Digital Fee Collection & Online Payment", "Automated fee due notifications, UPI and Net Banking payments with instant printable receipts and concession management."),
            ("Teacher & Parent Mobile Apps", "Dedicated mobile apps for Android and iOS with daily homework assignments, circulars, and direct teacher-parent chat."),
            ("Biometric & RFID Student Attendance", "Automated SMS and app push notifications sent to parents the instant their child enters the school gate."),
            ("CBSE & State Board Report Card Engine", "Customizable report cards compliant with NEP and board standards with automatic grade, mark, and rank calculations."),
            ("School Bus GPS Live Telematics", "Parents track school buses in real-time on Google Maps with ETA notifications when the bus approaches their stop.")
        ],
        "faqs": [
            ("Can parents pay school fees online through UPI or Credit Cards?", "Yes, integrated payment gateways allow parents to pay school fees directly from their mobile app with instant receipt generation."),
            ("Does it reduce administrative workload for school teachers?", "Yes, attendance marking takes 30 seconds per class, homework is uploaded with 1 click, and marks auto-calculate into report cards."),
            ("Can it handle complex fee concession and installment structures?", "Yes, easily set up sibling discounts, staff concessions, and customizable quarterly/monthly fee payment installments."),
            ("Can we send urgent circulars or holiday notices to parents?", "Yes, broadcast announcements, circulars, and photo galleries to all parents via WhatsApp and app notifications in seconds.")
        ]
    },
    {
        "filename": "college-university-erp-system.html",
        "name": "College & University ERP System",
        "category": "Higher Education IT",
        "title": "College & University ERP Management System | NAAC Ready | I Info Vision",
        "desc": "Enterprise college ERP system for arts, engineering, and autonomous institutions. Autonomous examination grading, admissions, NAAC reporting, and hostel management.",
        "keywords": "college erp software, university management system, autonomous exam software, naac college erp, higher education erp software",
        "badge": "NAAC & Autonomous ERP",
        "hero_title": "Comprehensive <span class='highlight'>College & University ERP</span>",
        "hero_desc": "Engineered for engineering, arts, medical, and autonomous polytechnic colleges. Unify academic planning, COE examination grading, faculty appraisals, and NAAC data collection.",
        "client_ref": "project-college-management.html",
        "client_name": "College Management System & App",
        "client_summary": "Engineered autonomous exam grading, online fees with receipt generation, and biometric staff attendance.",
        "deliverables": [
            ("Autonomous COE Examination Module", "Hall ticket generation, question paper bank encryption, dummy numbering, OMR barcoding, and automated GPA/CGPA computation."),
            ("Choice-Based Credit System (CBCS)", "Students select elective courses and open electives online with automated batch splitting and timetable allocation."),
            ("NAAC & NBA Accreditation Reporting", "Pre-configured data templates for Criterion 1 to 7 with student progression records, faculty publications, and placement stats."),
            ("Hostel & Mess Management System", "Hostel room allocation, digital gate pass approvals, mess meal token management, and visitor logs."),
            ("Placement Cell & Campus Drives", "Student resume repository, company eligibility shortlisting, drive schedule notifications, and offer letter archives."),
            ("Digital Library Automation (OPAC)", "Barcode book issue/return, RFID security gates integration, digital repository access, and late fee tracking.")
        ],
        "faqs": [
            ("Can this ERP handle autonomous examination grading rules?", "Yes, fully configurable for autonomous regulations, supplementary exams, grace mark policies, revaluation workflows, and transcript generation."),
            ("Does it generate reports required for NAAC SSR and NIRF ranking?", "Yes, one-click export of quantitative metrics, student-faculty ratios, and research publication records formatted for NAAC portal uploads."),
            ("Can faculty enter internal assessment marks online?", "Yes, faculty enter internal test marks and assignment scores with automatic CO-PO (Course Outcome / Program Outcome) attainment calculations."),
            ("Can the ERP support multi-campus university groups?", "Yes, centralized database architecture allows chancellor trusts to manage multiple colleges from a single executive dashboard.")
        ]
    },
    {
        "filename": "hotel-resort-management-software.html",
        "name": "Hotel & Resort Management Software",
        "category": "Hospitality IT",
        "title": "Luxury Hotel & Resort Management Software (PMS) | I Info Vision",
        "desc": "All-in-one property management system (PMS) for luxury resorts, boutique hotels, and service villas. Channel manager, booking engine, room folio, and restaurant POS.",
        "keywords": "hotel management software, resort management system, hotel pms software, room booking software, resort pos software",
        "badge": "Luxury Hospitality PMS",
        "hero_title": "All-in-One <span class='highlight'>Hotel & Resort Management</span>",
        "hero_desc": "Deliver 5-star guest experiences. Connect direct website room bookings, OTA channel sync (Booking.com, Agoda), restaurant billing, spa management, and housekeeping.",
        "client_ref": "project-luxeresort-os.html",
        "client_name": "LuxeResort-OS Property Suite",
        "client_summary": "Multi-property management, live room folio engine, and integrated staff resource allocation.",
        "deliverables": [
            ("Visual Room Grid & Front Desk", "Color-coded room calendar showing clean, occupied, reserved, and maintenance status with 1-click check-in and check-out."),
            ("Integrated Room Folio Billing", "Post restaurant orders, spa charges, laundry, and mini-bar bills directly to the guest room folio for single-invoice checkout."),
            ("Direct Website Booking Engine", "Commission-free direct booking engine on your website with live room rates, seasonal promo codes, and instant payment gateway."),
            ("2-Way OTA Channel Manager", "Automatically sync room inventory and rates across Booking.com, MakeMyTrip, Agoda, and Airbnb to prevent double-booking."),
            ("Housekeeping & Maintenance App", "Housekeepers update room clean/dirty status on their mobile phones in real-time, instantly notifying reception."),
            ("Guest Profile & WhatsApp Concierge", "Send automated booking vouchers, check-in instructions, WiFi passwords, and review feedback requests via WhatsApp.")
        ],
        "faqs": [
            ("Does it prevent double bookings from OTAs like Booking.com and MakeMyTrip?", "Yes, our real-time 2-way channel manager updates inventory across all online booking sites the moment a room is sold anywhere."),
            ("Can it handle restaurant and spa billing posted to room bills?", "Yes, waitstaff and spa therapists can post bills directly to guest room numbers, signed and settled at final checkout."),
            ("Does it generate the police C-Form for foreign tourists?", "Yes, capture foreign guest passport details and visa scans to generate statutory C-Forms for government reporting."),
            ("Can multiple resort properties be managed from one account?", "Yes, centralized enterprise management lets owners monitor room revenue, ADR, and RevPAR across multiple hotels.")
        ]
    },
    {
        "filename": "restaurant-pos-billing-software.html",
        "name": "Restaurant POS & KOT Software",
        "category": "Hospitality & Food POS",
        "title": "Best Restaurant POS Billing & KOT Software | I Info Vision",
        "desc": "High-speed restaurant billing software. Kitchen Order Ticket (KOT) printing, table management, Swiggy & Zomato order integration, and inventory recipe costing.",
        "keywords": "restaurant billing software, restaurant pos software, kot software, cafe billing software, food delivery integration pos",
        "badge": "Sub-Second Restaurant POS",
        "hero_title": "Superfast <span class='highlight'>Restaurant POS & KOT Software</span>",
        "hero_desc": "Say goodbye to kitchen chaos. Route Kitchen Order Tickets (KOT) in seconds, manage dynamic table reservations, sync Swiggy/Zomato orders, and track ingredient stock.",
        "client_ref": "project-kumar-hospital-billing.html",
        "client_name": "High-Volume POS Invoicing Engine",
        "client_summary": "Sub-500ms transaction printing with automated ledger balancing and daily cash register reconciliation.",
        "deliverables": [
            ("Sub-Second Table & KOT Billing", "Visual floor layout table grid, fast item modifier selection (less spicy, no onion), and instant kitchen thermal printing."),
            ("Waiter Mobile Ordering App", "Waiters take customer food orders on Android tablets or phones tableside, instantly sending KOT tickets to the kitchen."),
            ("Swiggy & Zomato Live Sync", "Receive and manage online delivery orders directly on your POS screen without switching between multiple tablets."),
            ("Raw Material Recipe Costing", "Deduct raw chicken, oil, vegetables, and spices automatically from godown stock whenever a dish is billed to detect kitchen theft."),
            ("QR Code Digital Dine-in Menu", "Dine-in customers scan table QR codes to view photo menus, place orders, and pay through UPI directly from their phone."),
            ("Daily Cash & Sales Audit Reports", "View exact cashier collection splits (Cash, UPI, Card), cancelled KOT audits, and top grossing menu items on mobile.")
        ],
        "faqs": [
            ("Can it print KOTs to different kitchen sections (Tandoor, Chinese, Bar)?", "Yes, orders automatically split and print to designated kitchen stations (e.g., beverages to bar, gravies to main kitchen)."),
            ("Can customers pay using dynamic UPI QR codes printed on the bill?", "Yes, dynamic UPI QR codes print directly on the guest bill so customers scan and pay in 5 seconds."),
            ("How does recipe management prevent kitchen ingredient theft?", "By mapping raw ingredients to each dish, the software shows variance between expected ingredient usage and physical stock left."),
            ("Can it handle AC, Non-AC, and Parcel different price lists?", "Yes, configure separate pricing tiers for AC dine-in, non-AC dining, room service, and parcel take-away.")
        ]
    },
    {
        "filename": "fleet-transport-management-software.html",
        "name": "Fleet & Transport Management Software",
        "category": "Logistics & Fleet IT",
        "title": "Fleet Management & GPS Tracking Software | I Info Vision",
        "desc": "Enterprise fleet management and vehicle tracking software. Trip sheet accounting, diesel fuel logs, driver settlements, tyre life, and live GPS integration.",
        "keywords": "fleet management software, transport software, lorry fleet management, vehicle trip sheet software, diesel fuel tracking software",
        "badge": "Enterprise Fleet OS",
        "hero_title": "Intelligent <span class='highlight'>Fleet & Transport Management</span>",
        "hero_desc": "Take complete operational control of your trucks, buses, tankers, and delivery vans. Track trip profits, prevent diesel theft, and monitor tyre lifespans in real-time.",
        "client_ref": "project-transittrack.html",
        "client_name": "TransitTrack Fleet Telematics",
        "client_summary": "Deployed live GPS polling, automated route geofencing, and digital trip sheet accounting.",
        "deliverables": [
            ("Digital Trip Sheet Accounting", "Track trip opening odometer, loading weight, freight advances, diesel bunk receipts, toll charges, and driver balance settlement."),
            ("Diesel Fuel Monitoring & Mileage Audit", "Compare actual fuel issued against standard expected vehicle mileage to detect fuel pilferage and route diversion."),
            ("Tyre Management & Retreading Log", "Track every tyre by serial number, wheel axle position, total distance run, rotation dates, and retreading life history."),
            ("Automated Vehicle Document Expiry Alerts", "Automated SMS/WhatsApp warnings 30 days before Insurance, Fitness Certificate (FC), National Permit, and Road Tax expire."),
            ("Live GPS Tracking & Geofencing", "Live map tracking, vehicle speed alerts, unauthorized stoppage warnings, and geofenced warehouse entry/exit logs."),
            ("Transporter Freight Billing & LR Creation", "Generate Lorry Receipts (LR), transport delivery challans, and customer freight invoices with GST compliance.")
        ],
        "faqs": [
            ("Does it calculate the exact net profit made on every trip?", "Yes, calculates freight revenue minus diesel, driver beta, toll, loading charges, and maintenance to give exact net trip margin."),
            ("Can it integrate with our existing vehicle GPS trackers?", "Yes, we integrate with all major GPS tracker protocols (Concox, Teltonika, Sinotrack) via secure telemetry APIs."),
            ("How does tyre tracking save money for fleet owners?", "By tracking mileage and timely wheel rotation, tyre life increases by up to 25%, saving lakhs in replacement costs."),
            ("Can drivers submit diesel receipts and expense photos on mobile?", "Yes, drivers can snap fuel bill photos and submit expenses through the driver mobile app for instant manager verification.")
        ]
    },
    {
        "filename": "real-estate-crm-software.html",
        "name": "Real Estate CRM Software",
        "category": "Real Estate IT",
        "title": "Best Real Estate CRM Software for Builders & Brokers | I Info Vision",
        "desc": "High-converting real estate CRM for property developers, builders, and brokers. Lead pipeline, site visit scheduling, unit booking chart, and broker commission.",
        "keywords": "real estate crm software, builder crm software, property lead management, plot booking software, real estate marketing crm",
        "badge": "Real Estate Sales OS",
        "hero_title": "High-Converting <span class='highlight'>Real Estate CRM Software</span>",
        "hero_desc": "Stop losing property leads. Capture leads from Facebook, 99acres, and Google Ads, automate sales executive follow-ups, and manage plot/flat unit inventory in real-time.",
        "client_ref": "project-tradeology.html",
        "client_name": "Enterprise Order Execution Systems",
        "client_summary": "Automated order milestone tracking with real-time exception alerts and fulfillment validation.",
        "deliverables": [
            ("Omnichannel Lead Auto-Capture", "Instantly ingest leads from Facebook Ads, Google Ads, 99acres, Magicbricks, and website forms with zero lead leakage."),
            ("Automated Lead Distribution & Call Logs", "Auto-assign leads to sales executives based on project location, track follow-up calls, and schedule site visits."),
            ("Interactive Plot / Flat Booking Layout", "Visual layout master plan showing available, blocked, booked, and registered plots/apartments in live color codes."),
            ("Customer Payment Milestones & Demand Letters", "Automated generation of stage-wise construction payment demand letters, receipt vouchers, and interest calculations."),
            ("Channel Partner (Broker) Commission", "Track broker source leads, calculate commission percentages, and manage milestone payout schedules."),
            ("WhatsApp Drip Marketing Campaigns", "Send automated project brochures, construction video updates, and festive booking offers to warm prospects.")
        ],
        "faqs": [
            ("Can it prevent duplicate leads from multiple ad sources?", "Yes, intelligent deduplication recognizes existing mobile numbers and updates the original lead card with new inquiry details."),
            ("Can customers view their construction payment milestone status?", "Yes, customer portals allow property buyers to view construction progress photos and download payment receipts."),
            ("Does it track sales executive follow-up efficiency?", "Yes, managers see daily calls made, site visits conducted, overdue follow-ups, and sales conversion rates per executive."),
            ("Can we send automated project brochures on WhatsApp?", "Yes, the instant a lead fills a form, an automated WhatsApp greeting sends the project PDF brochure and floor plan.")
        ]
    },
    {
        "filename": "jewellery-billing-software.html",
        "name": "Jewellery Billing Software",
        "category": "Jewellery Retail",
        "title": "Best Jewellery Billing Software in Tamil Nadu | Barcode & HUID | I Info Vision",
        "desc": "Leading jewellery billing and inventory software in Tamil Nadu. Gold rate updates, wastage & making charges calculation, old gold exchange, and HUID tracking.",
        "keywords": "jewellery billing software, gold shop billing software, huid jewellery software, gold wastage calculation, jewellery pos software",
        "badge": "HUID & BIS-Ready POS",
        "hero_title": "Advanced <span class='highlight'>Jewellery Billing Software</span>",
        "hero_desc": "Engineered for gold, silver, and diamond jewelers. Automate daily metal rates, accurate wastage (VA) and making charges, old gold purchase exchange, and HUID barcode tracking.",
        "client_ref": "project-kumar-hospital-billing.html",
        "client_name": "High-Precision Invoicing Engine",
        "client_summary": "Accurate multi-digit decimal calculations with automated tax splitting and digital certificate logging.",
        "deliverables": [
            ("Daily Gold & Silver Rate Sync", "Set 22K, 24K, 18K gold and silver rates once in the morning, updating prices across all billing counters automatically."),
            ("Wastage (VA) & Making Charges", "Flexible calculation of value addition (VA percentage), flat making charges per gram, or piece-rate pricing per ornament."),
            ("BIS 6-Digit HUID Tracking", "Mandatory BIS hallmark HUID tracking records unique 6-digit alphanumeric codes per ornament for government compliance."),
            ("Old Gold Purchase & Exchange", "Accurate testing purity deduction, melting loss percentage, and net exchange credit calculation for old customer gold."),
            ("Jewellery Barcode Tag Printing", "Print heat-resistant dumbbell barcode tags with ornament weight, gross weight, stone weight, net weight, and purity."),
            ("Monthly Gold Savings Scheme (Chit Fund)", "Manage customer monthly gold installment schemes, passbook updates, bonus months, and redemption settlement.")
        ],
        "faqs": [
            ("Does it support 6-digit BIS Hallmark Unique Identification (HUID)?", "Yes, fully compliant with BIS guidelines, capturing and printing HUID codes on customer invoices."),
            ("Can it connect with high-precision digital carat weighing balances?", "Yes, connects directly to electronic weighing balances to capture gross and net weight with 3-decimal milligram accuracy."),
            ("Can we manage customer monthly Gold Savings Schemes?", "Yes, tracks monthly payments, sends SMS payment reminders, records gold weight accumulated, and settles bonus maturities."),
            ("How does it handle stone weight and diamond certification?", "Separate stone weight deduction from gross weight ensures customers are only billed for net gold weight plus stone charges.")
        ]
    },
    {
        "filename": "manufacturing-production-erp.html",
        "name": "Manufacturing & Production ERP",
        "category": "Industrial Manufacturing",
        "title": "Manufacturing & Production ERP Software in Tamil Nadu | I Info Vision",
        "desc": "Enterprise manufacturing ERP software. Bill of Materials (BOM), shop floor work orders, machine maintenance, scrap control, and job costing.",
        "keywords": "manufacturing erp software, production planning software, shop floor control erp, bill of materials software, industrial erp tamil nadu",
        "badge": "Industrial Industry 4.0 ERP",
        "hero_title": "Enterprise <span class='highlight'>Manufacturing & Production ERP</span>",
        "hero_desc": "Eliminate shop floor bottlenecks. Unify raw material procurement, multi-level BOMs, machine utilization, subcontractor challans, and actual job costing.",
        "client_ref": "project-luxeresort-os.html",
        "client_name": "Enterprise Manufacturing Suites",
        "client_summary": "Deployed automated machine maintenance schedules, multi-level BOMs, and real-time scrap tracking.",
        "deliverables": [
            ("Multi-Level Bill of Materials (BOM)", "Hierarchical engineering BOMs with sub-assembly routings, raw material specifications, and scrap allowances."),
            ("Shop Floor Work Orders & Routing", "Generate job cards with stage-wise routing (Lathe, Milling, Heat Treatment, Assembly) and worker shift time tracking."),
            ("Subcontractor Job Work Challans", "Automate Annexure-IV / Rule 55 delivery challans, track raw material dispatched to job workers, and verify processed receipts."),
            ("Quality Control & Inspection (PQC / FQC)", "Record inwards inspection, in-process testing, and Final Quality Control (FQC) rejection analytics with root-cause tracking."),
            ("Preventive Machine Maintenance", "Schedule routine lubrication, spare part changeover alerts, and calculate Mean Time Between Failures (MTBF)."),
            ("Actual vs Estimated Job Costing", "Calculate exact production cost per batch combining raw materials, direct labor, power consumption, and machine hour rates.")
        ],
        "faqs": [
            ("Can this ERP integrate with industrial barcode scanners on the shop floor?", "Yes, workers scan job card barcodes at each machine station to record start time, completion time, and piece counts."),
            ("Can it track raw material batch numbers for automotive traceability?", "Yes, complete forward and backward heat number / batch traceability from raw material suppliers to finished dispatches."),
            ("Does it handle rejection and rework tracking?", "Yes, log rework hours and material re-issue to identify high-defect production stages and improve plant yield."),
            ("Can it export financial data to Tally or SAP?", "Yes, automated ledger synchronization exports purchases, sales, and inventory valuations to Tally or external accounting systems.")
        ]
    },
    {
        "filename": "automobile-service-center-software.html",
        "name": "Automobile Workshop & Garage Software",
        "category": "Automotive Aftermarket",
        "title": "Automobile Workshop & Garage Management Software | I Info Vision",
        "desc": "Best automobile service center and garage management software. Job card creation, spare parts inventory, mechanic commission, and service reminders.",
        "keywords": "automobile workshop software, garage management software, car service billing software, bike service center software, auto repair pos",
        "badge": "Automotive Garage OS",
        "hero_title": "Intelligent <span class='highlight'>Automobile Workshop Software</span>",
        "hero_desc": "Streamline vehicle servicing. Digital job cards with customer signature, spare parts inventory, mechanic labor commissions, and automated service reminders.",
        "client_ref": "project-transittrack.html",
        "client_name": "Fleet & Vehicle Diagnostic Systems",
        "client_summary": "Engineered real-time vehicle status logging and maintenance schedules.",
        "deliverables": [
            ("Digital Vehicle Job Card", "Capture vehicle number, odometer km, fuel gauge level, dent/scratch diagram, and customer complaint checklist on a tablet."),
            ("Spare Parts Inventory & Part Search", "Instant part lookup by OEM number, model compatibility, brand, and rack location with automated stock replenishment."),
            ("Mechanic Labor Tracking & Commission", "Assign repair tasks to technicians, track labor hours, and calculate mechanic incentives and productivity."),
            ("Automated Service Due Reminders", "Send automated WhatsApp and SMS reminders 6 months or 5,000 km after the last service to bring customers back."),
            ("Insurance Claim Accidental Repair", "Manage insurance survey estimates, photo documentation, approval tracking, and customer salvage deductions."),
            ("Customer Live Service Status Portal", "Customers receive SMS tracking links showing live vehicle status: Inspection, In Repair, Washing, Ready for Delivery.")
        ],
        "faqs": [
            ("Can service advisors create job cards on a mobile phone or tablet?", "Yes, service advisors walk around the vehicle inspecting scratches and capturing customer signatures on any smartphone or tablet."),
            ("Does it prevent mechanics from using spare parts without billing?", "Yes, spare parts can only be issued from the store against an authorized job card number, preventing inventory leakage."),
            ("How does it boost customer retention?", "Automated WhatsApp service reminders bring back over 35% of past customers whose vehicle service is due."),
            ("Can it generate GST invoices with separate labor and parts tax rates?", "Yes, automatically calculates 18% GST on labor services and 28%/18% GST on spare parts on a single consolidated invoice.")
        ]
    },
    {
        "filename": "wholesale-distribution-software.html",
        "name": "Wholesale & Distribution Software",
        "category": "Wholesale & FMCG",
        "title": "Wholesale & FMCG Distribution Management Software | I Info Vision",
        "desc": "Leading wholesale distribution and FMCG billing software. Salesman mobile order booking, route planning, scheme discounts, and credit management.",
        "keywords": "wholesale billing software, fmcg distribution software, salesman order booking app, wholesale inventory software, distributor erp",
        "badge": "FMCG Distribution OS",
        "hero_title": "Scalable <span class='highlight'>Wholesale & Distribution Software</span>",
        "hero_desc": "Accelerate wholesale turnover. Equip field salesmen with mobile order booking apps, manage beat routes, enforce retailer credit limits, and print bulk invoices.",
        "client_ref": "project-tradeology.html",
        "client_name": "High-Volume Order Execution Systems",
        "client_summary": "Integrated real-time checkout, automated customer invoicing, and digital product licensing.",
        "deliverables": [
            ("Salesman Mobile Order Booking App", "Salesmen visit retail shops, view live stock, book orders, and collect outstanding payments on their mobile phones."),
            ("Beat Route & Van Sales Management", "Optimize daily delivery vehicle routes, load vans according to booked orders, and reconcile evening returns."),
            ("Scheme & Trade Discount Matrix", "Automate complex company schemes: Buy 10 Get 1 Free, slab-based quantity discounts, and primary cash discounts."),
            ("Retailer Credit Limit Enforcement", "Block order booking or dispatch automatically when a retailer's credit days or credit balance exceeds agreed limits."),
            ("Batch & Expiry Inward / Outward", "Manage FMCG and commodity expiry dates, supplier claim debit notes for damaged goods, and short-expiry returns."),
            ("Automated E-Way Bill & E-Invoicing", "Generate bulk E-Way bills and government E-Invoices for hundreds of daily delivery routes in a single click.")
        ],
        "faqs": [
            ("Can salesmen book orders without internet connectivity?", "Yes, the salesman app works completely offline, syncing orders with the central office whenever internet is available."),
            ("How does it prevent bad debts from retail shops?", "Strict credit limit controls block new billing to retailers who have overdue unpaid invoices beyond the credit period."),
            ("Can it handle multi-company distribution (e.g., HUL, ITC, Britannia)?", "Yes, manage multiple FMCG agencies separately with company-wise sales targets, purchase claims, and margin reports."),
            ("Does it track delivery driver cash collections?", "Yes, daily route settlement reconciles delivery challans against cash and UPI payments collected by drivers.")
        ]
    },
    {
        "filename": "cold-storage-warehouse-software.html",
        "name": "Cold Storage & Warehouse Software",
        "category": "Warehousing & Supply Chain",
        "title": "Cold Storage & Warehouse Management Software (WMS) | I Info Vision",
        "desc": "Best cold storage and warehouse inventory management software. Inward gate pass, chamber allocation, lot tracking, weight slips, and rental billing.",
        "keywords": "cold storage software, warehouse management software, wms software tamil nadu, chamber inventory tracking, agricultural cold store software",
        "badge": "Intelligent Warehouse WMS",
        "hero_title": "Intelligent <span class='highlight'>Cold Storage & Warehouse Software</span>",
        "hero_desc": "Engineered for cold storage facilities, agricultural godowns, and third-party logistics (3PL). Automate chamber space management, lot weight slips, and storage rental billing.",
        "client_ref": "project-luxeresort-os.html",
        "client_name": "Multi-Facility Storage & Resource ERP",
        "client_summary": "Engineered multi-batch production scheduling, raw material tracking, and automated profitability analytics.",
        "deliverables": [
            ("Weighbridge & Inward Gate Pass", "Direct integration with weighbridge scales to generate inward gate passes, capturing gross, tare, and net bag weights."),
            ("3D Chamber & Rack Allocation", "Visual chamber grid showing occupied and vacant pallet positions, temperature zones, and rack numbers."),
            ("Farmer / Trader Lot Identification", "Assign unique barcode lot numbers per customer with details on commodity variety, bag counts, and moisture levels."),
            ("Flexible Storage Rental Billing", "Compute storage rent automatically based on per bag per month, daily weight rates, or dedicated chamber monthly leases."),
            ("Delivery Outward Gate Pass with Delivery Orders (DO)", "Verify customer signature and loan clearance before issuing delivery outward passes to prevent unauthorized dispatches."),
            ("Customer WhatsApp Stock Statements", "Customers receive automated monthly stock statements and outstanding rental invoices directly on WhatsApp.")
        ],
        "faqs": [
            ("Can it handle agricultural commodities like turmeric, tamarind, chillies, and seeds?", "Yes, customized commodity master modules handle bag types (gunny bags, plastic crates, boxes) and shrinkage deductions."),
            ("Does it support bank pledge loans against stored commodity warehouse receipts?", "Yes, generate statutory Warehouse Receipts (WR) and mark bank lien pledges to ensure goods are not released without bank NOC."),
            ("Can chamber temperature and humidity logs be recorded?", "Yes, record daily temperature logs per chamber with automated alerts if temperatures deviate from required thresholds."),
            ("How does it handle partial delivery withdrawals?", "Customers can withdraw partial bag quantities, with the software recalculating remaining lot stock and adjusting rent automatically.")
        ]
    },
    {
        "filename": "gym-fitness-club-software.html",
        "name": "Gym & Fitness Club Software",
        "category": "Fitness & Lifestyle",
        "title": "Best Gym & Fitness Club Management Software | I Info Vision",
        "desc": "Premier gym and fitness center management software. Biometric fingerprint attendance, membership renewals, diet charts, and automated fee reminders.",
        "keywords": "gym management software, fitness center software, gym billing software, biometric gym attendance, membership renewal software",
        "badge": "Smart Fitness Club OS",
        "hero_title": "Smart <span class='highlight'>Gym & Fitness Club Software</span>",
        "hero_desc": "Boost membership renewals. Automate biometric turnstile gate access, track member workout progress, assign personal trainers, and send automated WhatsApp payment reminders.",
        "client_ref": "project-typing-speed-test.html",
        "client_name": "Performance Metric Platforms",
        "client_summary": "Engineered real-time metric tracking with reactive UI dashboards and progress analytics.",
        "deliverables": [
            ("Biometric Turnstile & Face Attendance", "Integrates with biometric fingerprint, RFID, and facial recognition devices to allow entry only to active paid members."),
            ("Membership Package & Recurring Billing", "Configure monthly, quarterly, annual, and couple gym packages with automated renewal invoice generation."),
            ("Automated WhatsApp Expiry Reminders", "Automated reminders sent 7 days and 3 days before membership expires with 1-click UPI renewal payment links."),
            ("Trainer Commission & PT Booking", "Assign Personal Trainers (PT), track 1-on-1 session punch-ins, and calculate trainer commission payouts."),
            ("Member Workout & Diet Plan App", "Members access customized gym workout routines and nutritional diet charts on their smartphones."),
            ("Locker Management & Supplement POS", "Manage rental lockers and sell protein supplements and fitness gear with instant thermal barcode billing.")
        ],
        "faqs": [
            ("Can it automatically block gym entry if a member's fee is overdue?", "Yes, the biometric fingerprint and face recognition turnstile automatically denies entry when a member's renewal date has passed."),
            ("Can members pay their membership renewal online via UPI?", "Yes, WhatsApp renewal reminders include direct UPI payment links that automatically renew the member's access upon payment."),
            ("Can multi-branch gyms share member access?", "Yes, cloud-based access allows members to work out at any branch within your fitness chain with centralized attendance."),
            ("Does it manage supplementary retail sales (Proteins, Shakers)?", "Yes, built-in POS billing tracks supplement inventory, profit margins, and expiry dates.")
        ]
    },
    {
        "filename": "accounting-gst-filing-software.html",
        "name": "Accounting & GST Filing Software",
        "category": "Finance & Accounting",
        "title": "GST Accounting & E-Invoicing Software in Tamil Nadu | I Info Vision",
        "desc": "Simple, powerful GST accounting software. Automated E-Way bills, E-Invoicing, GSTR-1 & GSTR-3B return filing, bank reconciliation, and balance sheets.",
        "keywords": "gst accounting software, e invoicing software, tally alternative software, gstr 1 filing software, business accounting software tamil nadu",
        "badge": "100% GST Compliant Accounting",
        "hero_title": "Simple, Powerful <span class='highlight'>GST Accounting Software</span>",
        "hero_desc": "Replace complicated accounting software with an intuitive, fast, and 100% compliant GST platform engineered for business owners, not just accountants.",
        "client_ref": "project-kumar-hospital-billing.html",
        "client_name": "Hospital & Commercial Accounting Deployments",
        "client_summary": "Engineered automated batch-wise pricing, expiry alerts, and thermal prescription receipts.",
        "deliverables": [
            ("Automated 1-Click Government E-Invoicing", "Generate QR-code embedded E-Invoices and Invoice Reference Numbers (IRN) directly from the government portal with zero manual uploads."),
            ("Real-Time E-Way Bill Generation", "Generate Part-A and Part-B E-Way bills for road transport dispatches directly while printing sales invoices."),
            ("Automated GSTR-1, GSTR-2B & GSTR-3B Reports", "Instant export of error-free GST JSON returns matching government portal requirements for monthly filing."),
            ("Smart Bank Statement Auto-Reconciliation", "Import bank Excel/CSV statements to automatically match customer receipts and vendor payments in seconds."),
            ("Comprehensive Financial Statements", "Real-time Profit & Loss statement, Balance Sheet, Trial Balance, and Cash Flow reports updated with every transaction."),
            ("Multi-Company & Multi-Branch Consolidation", "Manage multiple GSTIN business registrations and view consolidated group financial health on a single dashboard.")
        ],
        "faqs": [
            ("Do I need advanced accounting knowledge to use this software?", "No, unlike Tally, our software uses simple business language (Sales, Purchases, Cash In, Cash Out) that anyone can use without formal training."),
            ("Can my Chartered Accountant (CA) access my accounts directly?", "Yes, you can give your CA a secure read-only login to review ledgers, download GST reports, and finalize tax audits remotely."),
            ("Does it automatically calculate Input Tax Credit (ITC)?", "Yes, it matches purchase bills against GSTR-2B data to maximize your eligible Input Tax Credit and prevent ITC loss."),
            ("How secure is my financial data?", "Financial databases are protected with bank-grade 256-bit encryption and automated daily off-site cloud backups.")
        ]
    }
]
