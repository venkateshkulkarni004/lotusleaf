import os
import json
import xml.etree.ElementTree as ET

SITE_ROOT = r"D:\soical media\ssm\saveweb2zip-com-pdf-site-builder-33-preview-emergentagent-com\leafcollection"

SERVICES = [
    {
        "slug": "Hotel-Management",
        "title": "Hotel and resort management",
        "service_type": "Hotel and resort management",
        "eyebrow": "Hotel and resort management",
        "h1": "Practical management for distinctive hospitality assets",
        "desc": "Management support for hotel and resort owners, investors and developers, connecting operations, guest experience and commercial priorities.",
        "cards": [
            ("Operating discipline", "Coordinate front office, housekeeping, food and beverage, maintenance, and back-of-house functions around clear routines and accountability."),
            ("Guest experience", "Shape arrival, stay, and departure experiences that match the property's brand promise and guest expectations."),
            ("Commercial strategy", "Manage pricing, distribution, corporate accounts, and direct-booking priorities to protect margins and occupancy."),
            ("Owner reporting", "Provide clear visibility into performance, costs, and progress against agreed priorities."),
        ],
        "cta": "Discuss a property",
        "faq": [
            ("What does hotel management support cover?", "The scope is agreed for each property and may connect operating plans, service standards, team readiness, guest experience, commercial priorities, and owner reporting."),
            ("How can hotel owners discuss management support?", "Hotel and resort owners, investors, and developers can contact The LotusLeaf Collection to discuss a property's requirements and confirm service fit and availability."),
            ("Does hotel management guarantee financial results?", "No. Hospitality performance depends on property, market, investment, and operating conditions. A management engagement should define scope, assumptions, responsibilities, and measurable review processes rather than promise guaranteed outcomes."),
        ],
    },
    {
        "slug": "Hospitality-Consulting",
        "title": "Hospitality consulting and hotel feasibility",
        "service_type": "Hospitality consulting",
        "eyebrow": "Hospitality consulting and feasibility",
        "h1": "Practical advice for hospitality concepts and investment decisions",
        "desc": "Structured hospitality advice to test concepts, demand assumptions, and hotel operating models.",
        "cards": [
            ("Concept testing", "Review the proposed hospitality concept against target guest needs, market evidence, and operating implications."),
            ("Demand and feasibility", "Assess access, competitive set, demand drivers, seasonality, pricing assumptions, and operating scenarios."),
            ("Operating model review", "Evaluate department design, staffing, service standards, systems, and cost structures before launch or repositioning."),
            ("Investment advisory", "Align investment assumptions, risk factors, and implementation priorities with the project's goals."),
        ],
        "cta": "Discuss feasibility",
        "faq": [
            ("What is included in hotel feasibility consulting?", "A feasibility review may examine the proposed concept, demand assumptions, competitive accommodation, access, facilities, operating costs, pricing assumptions, and scenarios. Scope and evidence requirements should be agreed for each project."),
            ("When should a developer speak with a hospitality consultant?", "Early engagement can help owners and developers test concepts and operating implications while plans can still be adjusted. The right timing depends on project stage, available information, and decisions to be made."),
            ("Does a feasibility study guarantee hotel investment returns?", "No. Feasibility work assesses assumptions and scenarios; it cannot guarantee demand, operating performance, approvals, or investment returns. Decisions should also use current market evidence and advice from relevant professional advisers."),
        ],
    },
    {
        "slug": "Hotel-Pre-Opening",
        "title": "Hotel and resort pre-opening solutions",
        "service_type": "Hospitality pre-opening planning and readiness",
        "eyebrow": "Hotel and resort pre-opening solutions",
        "h1": "Plan for a confident hotel or resort opening",
        "desc": "A coordinated approach to hotel and resort opening plans, team readiness, systems, suppliers, and guest journey testing.",
        "cards": [
            ("Operating readiness", "Define operating procedures, standards, and handover processes before the first guest arrives."),
            ("Recruitment and onboarding", "Plan role profiles, selection, inductions, and early team support aligned with the service promise."),
            ("Systems and suppliers", "Align property management systems, procurement, IT, safety, and vendor onboarding with opening milestones."),
            ("Guest journey testing", "Use soft openings, mock arrivals, and feedback to refine service delivery before full launch."),
        ],
        "cta": "Plan an opening",
        "faq": [
            ("What does a hotel pre-opening plan include?", "A project-specific plan can coordinate operating procedures, procurement, systems, recruitment, training, approvals tracking, sales setup, guest journey tests, and readiness reviews."),
            ("When should hotel pre-opening planning begin?", "Planning should begin while concept, design, and operating decisions can still be influenced. Timing varies by project, approvals, procurement lead times, construction progress, and scope."),
            ("Can a pre-opening consultant guarantee an opening date?", "No. Opening depends on construction, approvals, procurement, staffing, systems, and verified readiness. A plan helps coordinate dependencies and surface risks but cannot guarantee a date."),
        ],
    },
    {
        "slug": "Hospitality-Training",
        "title": "Hospitality training and team development",
        "service_type": "Hospitality training",
        "eyebrow": "Training and team development",
        "h1": "Build confident teams through practical hospitality training",
        "desc": "Practical, role-based hospitality learning for hotel and resort teams.",
        "cards": [
            ("Guest care and communication", "Practice clear, thoughtful interactions across arrival, stay, dining, requests, and departure."),
            ("Role-based operational skills", "Connect department tasks to safe, consistent routines and practical service expectations."),
            ("Service recovery", "Help team members respond calmly, take ownership, and escalate issues through agreed processes."),
            ("Team leadership", "Strengthen briefing, coaching, handovers, and feedback habits that support daily operations."),
        ],
        "cta": "Discuss team training",
        "faq": [
            ("What does hospitality training cover?", "Training can cover guest communication, service standards, practical role skills, service recovery, teamwork, and operating procedures, based on the property's needs."),
            ("Can hotel staff training be tailored to a property?", "Yes. Learning priorities should reflect the property's concept, guest profile, operating procedures, team roles, and current capability gaps."),
            ("How can owners assess whether training is useful?", "Agree learning objectives in advance and review participation, demonstrated skills, guest feedback, and relevant operating observations over time. Training does not guarantee business results."),
        ],
    },
    {
        "slug": "Hospitality-Commercial",
        "title": "Hospitality commercial strategy",
        "service_type": "Hospitality commercial strategy",
        "eyebrow": "Commercial strategy",
        "h1": "Connect today's performance with tomorrow's opportunities",
        "desc": "Commercial strategies that connect business today with tomorrow's opportunities.",
        "cards": [
            ("Revenue and pricing", "Balance rate positioning, demand patterns, and distribution costs with property and market realities."),
            ("Sales and accounts", "Develop corporate accounts, travel trade relationships, and direct-booking priorities that support sustainable occupancy."),
            ("Marketing positioning", "Clarify target guest segments, value proposition, messaging, and channel priorities for the property."),
            ("Performance tracking", "Use actionable reports to connect commercial decisions to operating feedback and owner priorities."),
        ],
        "cta": "Discuss commercial strategy",
        "faq": [
            ("What is hospitality commercial strategy?", "It connects pricing, distribution, sales, marketing, and performance reporting to the property's commercial goals and guest mix."),
            ("How can a hotel improve direct bookings?", "Direct booking performance depends on website experience, rate competitiveness, package clarity, channel mix, and guest trust. The right mix varies by property, market, and competition."),
            ("Does commercial strategy guarantee higher revenue?", "No. Commercial performance is influenced by market demand, competition, seasonality, operating quality, and guest preferences. Strategy should define assumptions, targets, and review cadence rather than promise outcomes."),
        ],
    },
    {
        "slug": "Hospitality-Audit",
        "title": "Hospitality operational and financial audit",
        "service_type": "Hospitality audit",
        "eyebrow": "Operational and financial audit",
        "h1": "Review operations and financial controls with clarity",
        "desc": "Operational and financial reviews that identify opportunities and support informed decisions.",
        "cards": [
            ("Operational review", "Evaluate workflows, standards, maintenance, safety, and controls against the property's objectives."),
            ("Financial controls", "Review revenue integrity, cost management, procurement, and reporting clarity for owners and operators."),
            ("Compliance and risk", "Identify statutory, safety, licensing, and operational risks that could affect performance or continuity."),
            ("Improvement roadmap", "Translate findings into prioritized actions, owners, and review points that support steady improvement."),
        ],
        "cta": "Request an audit",
        "faq": [
            ("What does a hospitality audit cover?", "An audit can cover operations, guest experience, financial controls, procurement, compliance, safety, and reporting, depending on scope."),
            ("When should a hotel undergo an operational audit?", "Key moments include ownership changes, performance review cycles, pre-sale or refinancing, and when operating assumptions or controls need independent scrutiny."),
            ("Does an audit guarantee better results?", "No. An audit identifies observations and recommendations. Results depend on management decisions, implementation quality, market conditions, and sustained execution."),
        ],
    },
    {
        "slug": "Hotel-Revenue-Management",
        "title": "Hotel revenue management and pricing strategy",
        "service_type": "Hotel revenue management",
        "eyebrow": "Revenue management and pricing strategy",
        "h1": "Insight-led pricing and forecasting for sustainable revenue growth",
        "desc": "Insight-led pricing, forecasting, and optimization to build sustainable revenue growth.",
        "cards": [
            ("Demand forecasting", "Use booking patterns, market intelligence, and property data to anticipate demand and adjust planning."),
            ("Pricing and inventory", "Balance rate positioning, length-of-stay controls, and channel mix with market and cost realities."),
            ("Distribution efficiency", "Review direct and indirect channel performance, commissions, and conversion to improve margin."),
            ("Reporting and review", "Connect revenue decisions to operating feedback and owner reporting with clear metrics and review cadence."),
        ],
        "cta": "Discuss revenue strategy",
        "faq": [
            ("What does hotel revenue management include?", "Revenue management can cover demand forecasting, pricing strategy, inventory control, distribution review, performance reporting, and aligned commercial actions."),
            ("How can a hotel improve RevPAR?", "RevPAR improvement depends on rate, occupancy, mix, market demand, guest experience, and distribution choices. Recommendations should be grounded in the property's data and market context."),
            ("Does revenue management guarantee profitability?", "No. Revenue management supports better commercial decisions, but profitability also depends on costs, operating quality, market conditions, and investment decisions."),
        ],
    },
    {
        "slug": "Resort-Management",
        "title": "Resort and destination management",
        "service_type": "Resort and destination operations management",
        "eyebrow": "Resort management",
        "h1": "Create resort experiences rooted in place and thoughtful hospitality",
        "desc": "Thoughtful resort operations that connect place, guest experience, teams and business priorities.",
        "cards": [
            ("Guest journey", "Coordinate pre-arrival information, welcome, activities, dining, service recovery, and departure."),
            ("Teams and service standards", "Align roles, training, communication, and operating routines with the resort's service promise."),
            ("Facilities and daily operations", "Bring housekeeping, maintenance, food service, safety checks, and activity operations into a clear rhythm."),
            ("Place-led programming", "Consider the setting and local knowledge when shaping activities, interpretation, and guest experiences."),
        ],
        "cta": "Discuss a resort project",
        "faq": [
            ("What does resort management involve?", "Resort management may coordinate daily operations, guest experience, team readiness, facilities, activities, service standards, and commercial priorities according to the asset and agreed scope."),
            ("How can a resort connect its setting with guest experience?", "Start with the property's natural and cultural context, guest needs, responsible operating practices, and local professional guidance, then reflect these in services and activities."),
            ("Does resort management guarantee occupancy or revenue?", "No. Resort performance is affected by market demand, access, seasonality, competition, operating choices, and other factors. Engagements should set clear scope and review assumptions without promising results."),
        ],
    },
]

REGIONS = {
    "Indian Subcontinent": {
        "cities": [
            ("Mumbai", "Maharashtra"),
            ("Delhi", "Delhi"),
            ("Bangalore", "Karnataka"),
            ("Hyderabad", "Telangana"),
            ("Chennai", "Tamil Nadu"),
            ("Kolkata", "West Bengal"),
            ("Pune", "Maharashtra"),
            ("Ahmedabad", "Gujarat"),
            ("Jaipur", "Rajasthan"),
            ("Kochi", "Kerala"),
            ("Chandigarh", "Punjab"),
            ("Indore", "Madhya Pradesh"),
            ("Lucknow", "Uttar Pradesh"),
            ("Surat", "Gujarat"),
            ("Vadodara", "Gujarat"),
            ("Nagpur", "Maharashtra"),
            ("Coimbatore", "Tamil Nadu"),
            ("Visakhapatnam", "Andhra Pradesh"),
            ("Trivandrum", "Kerala"),
            ("Goa", "Goa"),
            ("Mysore", "Karnataka"),
        ]
    },
    "Middle East": {
        "cities": [
            ("Dubai", "UAE"),
            ("Abu Dhabi", "UAE"),
            ("Riyadh", "Saudi Arabia"),
            ("Jeddah", "Saudi Arabia"),
            ("Doha", "Qatar"),
            ("Muscat", "Oman"),
        ]
    },
    "Africa": {
        "cities": [
            ("Nairobi", "Kenya"),
            ("Cape Town", "South Africa"),
            ("Johannesburg", "South Africa"),
            ("Lagos", "Nigeria"),
        ]
    },
    "USA": {
        "cities": [
            ("New York", "USA"),
            ("Los Angeles", "USA"),
            ("Chicago", "USA"),
            ("Miami", "USA"),
            ("Dallas", "USA"),
            ("San Francisco", "USA"),
            ("Las Vegas", "USA"),
            ("Houston", "USA"),
            ("Washington DC", "USA"),
            ("Boston", "USA"),
        ]
    },
    "Europe": {
        "cities": [
            ("London", "UK"),
            ("Paris", "France"),
            ("Berlin", "Germany"),
            ("Madrid", "Spain"),
            ("Rome", "Italy"),
            ("Amsterdam", "Netherlands"),
            ("Vienna", "Austria"),
            ("Zurich", "Switzerland"),
            ("Istanbul", "Turkey"),
            ("Lisbon", "Portugal"),
        ]
    },
}

CITY_CONTEXT = {
    "Mumbai": "business properties near BKC and Nariman Point to boutique stays in South Mumbai and suburban hubs",
    "Delhi": "properties near Connaught Place, Nehru Place, and Aerocity with strong corporate and transit demand",
    "Bangalore": "corporate properties near Electronic City and Whitefield, boutique stays in Koramangala and Indiranagar, and airport transit properties",
    "Hyderabad": "tech-hub properties near HITEC City and Madhapur, business hotels in Banjara Hills, and midscale assets in Secunderabad",
    "Chennai": "business hotels near Tidel Park and Anna Nagar, beachfront properties in ECR, and airport transit accommodations",
    "Kolkata": "heritage and business properties around Park Street, Salt Lake, and New Town with cultural and corporate demand",
    "Pune": "properties near Koregaon Park, Hinjewadi, and Kalyani Nagar with IT, manufacturing, and weekend-leisure demand",
    "Ahmedabad": "properties along SG Highway and Bodakdev with growing corporate, MICE, and retail hospitality demand",
    "Jaipur": "heritage and business hotels near MI Road, Malviya Nagar, and C-Scheme with strong tourism and MICE segments",
    "Kochi": "properties near Marine Drive, Fort Kochi, and Ernakulam with backwater tourism and port-related demand",
    "Chandigarh": "hotels in Sector 17, Sector 35, and Mohali with government, education, and leisure demand",
    "Indore": "properties along Vijay Nagar, AB Road, and MG Road with commercial, textile, and educational demand",
    "Lucknow": "heritage-inspired and business hotels near Hazratganj, Gomti Nagar, and Aminabad",
    "Surat": "business and midscale hotels in Vesu, Athwa, and Textile Park areas with strong corporate and diamond-trade demand",
    "Vadodara": "properties in Alkapuri, Fatehgunj, and Kalyani Road with education, pharmaceutical, and industrial demand",
    "Nagpur": "hotels near Sitabuldi, Civil Lines, and Hingna with central India transit, education, and manufacturing demand",
    "Coimbatore": "properties in RS Puram, Peelamedu, and Saravanampatti with textile, engineering, and educational demand",
    "Visakhapatnam": "properties on Beach Road, MVP Colony, and Dwaraka Nagar with port, tourism, and steel-city demand",
    "Trivandrum": "hotels in Kowdiar, Vazhuthacaud, and Ulloor with government, tourism, and technology-park demand",
    "Goa": "beachfront resorts, boutique properties, and heritage hotels with strong leisure and MICE demand",
    "Mysore": "heritage-inspired hotels in Devaraja Mohalla, Hebbal, and Gokulam with tourism and culture-led demand",
    "Dubai": "luxury and business hotels in Downtown, Marina, Business Bay, and JBR with strong tourism, MICE, and transit demand",
    "Abu Dhabi": "properties on Corniche, Yas Island, and Al Maryah Island with government, energy, and leisure demand",
    "Riyadh": "business and luxury hotels in Olaya, King Abdullah Financial District, and diplomatic quarter",
    "Jeddah": "properties along Corniche, Al Balad, and Obhur with pilgrimage, trade, and coastal tourism demand",
    "Doha": "hotels in West Bay, The Pearl, and Lusail with financial, sports, and premium tourism demand",
    "Muscat": "properties in Muttrah, Al Khuwair, and Shati Al Qurum with trade, government, and coastal tourism demand",
    "Nairobi": "hotels in Westlands, Kilimani, and CBD with regional headquarters, conference, and safari-transit demand",
    "Cape Town": "properties in V&A Waterfront, City Bowl, and Camps Bay with tourism, events, and lifestyle demand",
    "Johannesburg": "hotels in Sandton, Rosebank, and OR Tambo corridor with business, mining, and conference demand",
    "Lagos": "properties on Victoria Island, Ikoyi, and Lekki with corporate, entertainment, and regional business demand",
    "New York": "hotels in Manhattan, Midtown, Brooklyn, and near JFK with business, leisure, and MICE demand",
    "Los Angeles": "properties in Beverly Hills, Santa Monica, Downtown LA, and Hollywood with entertainment and tourism demand",
    "Chicago": "hotels in The Loop, River North, and Magnificent Mile with business, conventions, and dining demand",
    "Miami": "properties in South Beach, Brickell, and Wynwood with leisure, Latin American business, and events demand",
    "Dallas": "hotels in Uptown, Downtown, and Las Colinas with corporate, conventions, and healthcare demand",
    "San Francisco": "properties in Union Square, SoMa, and Mission District with tech, finance, and tourism demand",
    "Las Vegas": "resorts and hotels on The Strip and Downtown with entertainment, conventions, and leisure demand",
    "Houston": "hotels in Downtown, Galleria, and Medical Center with energy, medical, and space-industry demand",
    "Washington DC": "properties in Dupont Circle, Capitol Hill, and Tyson's Corner with government, lobbying, and conference demand",
    "Boston": "hotels in Back Bay, Seaport, and Cambridge with education, healthcare, finance, and tourism demand",
    "London": "hotels in Mayfair, Canary Wharf, Covent Garden, and Shoreditch with finance, tourism, and MICE demand",
    "Paris": "properties in Champs-Élysées, Le Marais, and La Défense with luxury, tourism, and business demand",
    "Berlin": "hotels in Mitte, Charlottenburg, and Alexanderplatz with government, culture, and events demand",
    "Madrid": "properties in Salamanca, Gran Vía, and Castellana with business, tourism, and government demand",
    "Rome": "hotels in Trastevere, Historic Centre, and EUR with heritage, religion, and tourism demand",
    "Amsterdam": "properties in Canal Ring, Zuidas, and Jordaan with tourism, finance, and creative-events demand",
    "Vienna": "hotels in Innere Stadt, Leopoldstadt, and Donau City with government, culture, and MICE demand",
    "Zurich": "properties in Bahnhofstrasse, Altstadt, and Wollishofen with finance, pharma, and lake-tourism demand",
    "Istanbul": "hotels in Sultanahmet, Beyoğlu, and Levent with heritage, Bosphorus tourism, and business demand",
    "Lisbon": "properties in Baixa, Chiado, and Parque das Nações with tourism, tech, and Atlantic-coast demand",
}

REGION_LABEL = {
    "Indian Subcontinent": "Indian Subcontinent",
    "Middle East": "Middle East",
    "Africa": "Africa",
    "USA": "USA",
    "Europe": "Europe",
}

SERVICE_SLUGS = [s["slug"] for s in SERVICES]


def make_hotel_management_page(city, state):
    context = CITY_CONTEXT[city]
    city_clean = city.replace(" ", "")
    title = f"Hotel Management {city} | The LotusLeaf Collection"
    h1 = f"Hotel management support for {city} owners and operators"
    desc = f"Hotel management support for {city} owners and operators. We connect operations, guest experience, teams and commercial priorities."
    keywords = f"hotel management {city}, hotel management company {city}, hotel management services {city}, {city} hotel operations, hospitality management {state}, hotel management {state}"
    cta = f"Discuss a {city} property"
    city_faq_q = f"What does hotel management support cover in {city}?"
    city_faq_a = f"The scope is agreed for each property and may connect operating plans, service standards, team readiness, guest experience, commercial priorities, and owner reporting tailored to the {city} market."
    engage_q = f"How can {city} hotel owners discuss management support?"
    engage_a = f"Hotel and resort owners, investors, and developers in {city} can contact The LotusLeaf Collection to discuss a property's requirements and confirm service fit and availability."
    local_section = f"For hotel projects in {city}, local market conditions, regulatory requirements, and competitive set should be verified for the specific property. Statutory approvals, licensing, and compliance questions require current advice from qualified professionals and relevant authorities."
    note = f"Service scope and availability are confirmed for each project. Mentions of {city} do not imply a local office or guaranteed engagement."
    hero_p = f"{city.capitalize()}'s hospitality market demands sharp operations, strong commercial focus, and a guest experience that matches the city's pace. The LotusLeaf Collection works with owners, investors and developers to align operating discipline with each property's goals."
    ops_p = f"{city} hotels range from {context}. Each segment has different guest expectations, competitive dynamics, and cost pressures. Management support should respond to the specific asset, market position, and ownership priorities."
    market_p = f"{city} owners should evaluate demand drivers, competitive positioning, and operating standards against the property's concept and ownership goals. Practical support should connect local market realities with the service promise and commercial priorities."
    return {
        "slug": f"Hotel-Management-{city_clean}",
        "title": title,
        "h1": h1,
        "desc": desc,
        "keywords": keywords,
        "canonical": f"https://www.lotusleafcollection.com/Hotel-Management-{city_clean}.html",
        "og_title": title,
        "og_desc": desc,
        "twitter_title": title,
        "twitter_desc": desc,
        "eyebrow": "Hotel management",
        "hero_p": hero_p,
        "ops_p": ops_p,
        "market_p": market_p,
        "cards": [
            ("Operating discipline", "Coordinate front office, housekeeping, food and beverage, maintenance, and back-of-house functions around clear routines and accountability."),
            ("Guest experience", "Shape arrival, stay, and departure experiences that match the property's brand promise and guest expectations."),
            ("Commercial strategy", "Manage pricing, distribution, corporate accounts, and direct-booking priorities to protect margins and occupancy."),
            ("Owner reporting", "Provide clear visibility into performance, costs, and progress against agreed priorities."),
        ],
        "local_section": local_section,
        "note": note,
        "cta": cta,
        "faq": [
            (city_faq_q, city_faq_a),
            (engage_q, engage_a),
            ("Does hotel management guarantee financial results?", "No. Hospitality performance depends on property, market, investment, and operating conditions. A management engagement should define scope, assumptions, responsibilities, and measurable review processes rather than promise guaranteed outcomes."),
        ],
        "area_served": f'["{state}", "{city}", "India", "Middle East", "Africa"]',
        "audience": f'Hotel owners, investors, and developers in {city}',
        "service_name": f"Hotel management in {city}",
        "service_desc": f"Management support for {city} hotel and resort owners, investors and developers, connecting operations, guest experience, and commercial performance.",
        "service_type": "Hotel and resort management",
    }


def make_service_page(service, city, state):
    context = CITY_CONTEXT[city]
    city_clean = city.replace(" ", "")
    title = f"{service['title']} {city} | The LotusLeaf Collection"
    h1 = service["h1"]
    desc = f"{service['desc'].rstrip('.')} for {city} owners, investors and developers. Local market context for {city} and {state}."
    keywords = f"{service['slug'].lower()} {city}, {service['slug'].lower()} {state}, {service['slug'].lower()} {city_clean}, {state} hospitality services, {city} hospitality, {state} hospitality"
    cta = service["cta"]
    city_faq_q = f"What does {service['slug'].lower().replace('hotel-', 'hotel ')} cover in {city}?"
    city_faq_a = f"The scope is agreed for each project and may connect {service['slug'].lower().replace('hotel-', 'hotel ')} activities tailored to the {city} market, including local context, facilities, and guest expectations."
    engage_q = f"How can {city} owners discuss {service['slug'].lower().replace('hotel-', 'hotel ')} support?"
    engage_a = f"Hotel and resort owners, investors, and developers in {city} can contact The LotusLeaf Collection to discuss requirements, scope, and availability for {service['slug'].lower().replace('hotel-', 'hotel ')} support."
    local_section = f"For projects in {city}, local market conditions, regulatory requirements, and competitive set should be verified for the specific property. Statutory approvals, licensing, and compliance questions require current advice from qualified professionals and relevant authorities."
    note = f"Service scope and availability are confirmed for each project. Mentions of {city} do not imply a local office or guaranteed engagement."
    hero_p = f"{city.capitalize()}'s hospitality sector blends {context}. The LotusLeaf Collection works with owners, investors and developers to align {service['slug'].lower().replace('hotel-', 'hotel ')} with each property's goals."
    ops_p = f"{city} hospitality properties span {context}. Each segment has different guest expectations, competitive dynamics, and operational priorities. Support should respond to the specific asset, market position, and ownership priorities."
    market_p = f"{city} owners should evaluate demand drivers, competitive positioning, and operating standards against the property's concept and ownership goals. Practical support should connect local market realities with the service promise and commercial priorities."
    return {
        "slug": f"{service['slug']}-{city_clean}",
        "title": title,
        "h1": h1,
        "desc": desc,
        "keywords": keywords,
        "canonical": f"https://www.lotusleafcollection.com/{service['slug']}-{city_clean}.html",
        "og_title": title,
        "og_desc": desc,
        "twitter_title": title,
        "twitter_desc": desc,
        "eyebrow": service["eyebrow"],
        "hero_p": hero_p,
        "ops_p": ops_p,
        "market_p": market_p,
        "cards": service["cards"],
        "local_section": local_section,
        "note": note,
        "cta": cta,
        "faq": [
            (city_faq_q, city_faq_a),
            (engage_q, engage_a),
            service["faq"][2],
        ],
        "area_served": f'["{state}", "{city}", "India", "Middle East", "Africa"]',
        "audience": f'Hotel owners, investors, and developers in {city}',
        "service_name": service["title"],
        "service_desc": service["desc"],
        "service_type": service["service_type"],
    }


def build_html(page, related_links=None, other_city_links=None):
    faq_json = ",".join([
        f'{{"@type":"Question","name":"{q}","acceptedAnswer":{{"@type":"Answer","text":"{a}"}}}}'
        for q, a in page["faq"]
    ])
    cards_html = "".join([
        f'<article class="service-card"><h3>{t}</h3><p>{d}</p></article>'
        for t, d in page["cards"]
    ])
    base_related = "".join([
        '<a href="Hotel-Management.html">Hotel and resort management</a>',
        '<a href="Hospitality-Consulting.html">Consulting</a>',
        '<a href="Hotel-Pre-Opening.html">Pre-opening</a>',
        '<a href="whatwedo.html">All services</a>',
        '<a href="Contactus.html">Contact us</a>',
    ])
    related_html = base_related
    if related_links:
        related_html += "".join([f'<a href="{slug}.html">{label}</a>' for slug, label in related_links])
    other_city_html = ""
    if other_city_links:
        other_city_html = f'<div class="related" style="margin-top:1rem"><strong>Also available in:</strong> {" ".join([f"<a href=\"{slug}.html\">{label}</a>" for slug, label in other_city_links])}</div>'

    # Load index-style header/footer sections
    with open(os.path.join(SITE_ROOT, "extracted_navbar.html"), "r", encoding="utf-8") as f:
        navbar_html = f.read()
    with open(os.path.join(SITE_ROOT, "extracted_side_menu.html"), "r", encoding="utf-8") as f:
        side_menu_html = f.read()
    with open(os.path.join(SITE_ROOT, "extracted_footer.html"), "r", encoding="utf-8") as f:
        footer_html = f.read()
    with open(os.path.join(SITE_ROOT, "extracted_menu_js.js"), "r", encoding="utf-8") as f:
        menu_js = f.read()
    with open(os.path.join(SITE_ROOT, "extracted_header_footer.css"), "r", encoding="utf-8") as f:
        header_footer_css = f.read()

    html = f"""<!DOCTYPE html>
<html lang="en-IN">
<head>
  <meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="theme-color" content="#0A2A22"><link rel="icon" type="image/jpeg" href="images/WhatsApp%20Image%202026-06-19%20at%207.35.11%20PM.jpeg">
  <meta name="description" content="{page['desc']}"><meta name="robots" content="index,follow,max-image-preview:large,max-snippet:-1,max-video-preview:-1"><meta name="author" content="The LotusLeaf Collection">
  <meta name="keywords" content="{page['keywords']}">
  <link rel="canonical" href="{page['canonical']}"><meta property="og:type" content="website"><meta property="og:site_name" content="The LotusLeaf Collection"><meta property="og:locale" content="en_IN">
  <meta property="og:title" content="{page['og_title']}"><meta property="og:description" content="{page['og_desc']}"><meta property="og:url" content="{page['canonical']}">
  <meta property="og:image" content="https://www.lotusleafcollection.com/images/WhatsApp_Image_2026-06-19_at_7.55.56_PM-removebg-preview.png">
  <meta property="og:image:alt" content="The LotusLeaf Collection - Hospitality management and consulting">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:site" content="@lotusleafcollection"><meta name="twitter:title" content="{page['twitter_title']}"><meta name="twitter:description" content="{page['twitter_desc']}"><meta name="twitter:image" content="https://www.lotusleafcollection.com/images/WhatsApp_Image_2026-06-19_at_7.55.56_PM-removebg-preview.png"><meta name="twitter:image:alt" content="The LotusLeaf Collection hospitality management and consulting">
  <title>{page['title']}</title>
  <link rel="alternate" href="{page['canonical']}" hreflang="en-IN" />
  <link rel="alternate" href="{page['canonical']}" hreflang="en" />
  <link rel="alternate" href="{page['canonical']}" hreflang="x-default" />

  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet"><link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.10.0/font/bootstrap-icons.min.css" rel="stylesheet"><link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;0,700;1,400&family=Outfit:wght@300;400;500;600;700&display=swap" rel="stylesheet"><link href="service-pages.css" rel="stylesheet">
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@graph":[{{"@type":"Organization","@id":"https://www.lotusleafcollection.com/#organization","name":"The LotusLeaf Collection","url":"https://www.lotusleafcollection.com/","email":"info@lotusleafcollection.com","telephone":"+91-99235-87326"}},{{"@type":"Service","@id":"{page['canonical']}#service","name":"{page['service_name']}","serviceType":"{page['service_type']}","provider":{{"@id":"https://www.lotusleafcollection.com/#organization"}},"areaServed":{page['area_served']},"audience":{{"@type":"BusinessAudience","audienceType":"{page['audience']}"}},"description":"{page['service_desc']}"}},{{"@type":"WebPage","@id":"{page['canonical']}#webpage","url":"{page['canonical']}","name":"{page['title']}","isPartOf":{{"@id":"https://www.lotusleafcollection.com/#website"}},"mainEntity":{{"@id":"{page['canonical']}#service"}},"inLanguage":"en-IN"}},{{"@type":"BreadcrumbList","@id":"{page['canonical']}#breadcrumb","itemListElement":[{{"@type":"ListItem","position":1,"name":"Home","item":"https://www.lotusleafcollection.com/"}},{{"@type":"ListItem","position":2,"name":"Our Service Portfolio","item":"https://www.lotusleafcollection.com/whatwedo.html"}},{{"@type":"ListItem","position":3,"name":"{page['service_name']}","item":"{page['canonical']}"}}]}},{{"@type":"FAQPage","@id":"{page['canonical']}#faq","mainEntity":[{faq_json}]}}]}}
  </script>
  <style>
    :root{{color-scheme:light;--emerald:#0a2a22;--green:#123a30;--gold:#c9a24b;--cream:#f9f8f6;--ink:#243c35;--muted:#52665f}}
    *{{box-sizing:border-box}}body{{margin:0;background:var(--cream);color:var(--ink);font:16px/1.7 Arial,sans-serif}}a{{color:inherit}}
    .skip{{position:absolute;left:-9999px;top:1rem;background:white;padding:.7rem;z-index:5}}.skip:focus{{left:1rem}}
    .container{{max-width:1120px;margin:0 auto;padding:2.5rem 1.25rem}}
    .section{{padding:2.5rem 1.25rem;max-width:1120px;margin:0 auto}}
    .grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(260px,1fr));gap:1.25rem;margin-top:1.5rem}}
    .card{{background:white;border:1px solid #e6e4df;border-radius:14px;padding:1.25rem;box-shadow:0 2px 10px rgba(14,42,34,.06)}}
    .card h3{{font:600 1.05rem/1.3 Cormorant Garamond,serif;color:var(--emerald);margin:0 0 .5rem}}
    .card p{{margin:0;color:#3a4d47;font-size:.98rem;line-height:1.6}}
    .faq-item{{background:white;border:1px solid #e6e4df;border-radius:14px;padding:1.25rem;margin-bottom:1rem;box-shadow:0 2px 10px rgba(14,42,34,.06)}}
    .faq-item h3{{font:600 1.05rem/1.3 Cormorant Garamond,serif;color:var(--emerald);margin:0 0 .4rem}}
    .faq-item p{{margin:0;color:#3a4d47}}
    .cta-bar{{background:linear-gradient(135deg,var(--emerald),#1c5542);color:white;padding:2.5rem 1.25rem;text-align:center}}
    .cta-bar a{{display:inline-block;margin-top:.75rem;background:var(--gold);color:#0b1f1a;padding:.7rem 1.1rem;border-radius:10px;text-decoration:none;font-weight:600}}
    .muted{{color:var(--muted)}}
    .small{{font-size:.92rem}}
    .note{{background:#fff8e1;border-left:4px solid var(--gold);padding:1rem;border-radius:0 10px 10px 0;margin-top:1rem}}
    .related{{display:flex;flex-wrap:wrap;gap:.6rem;margin-top:1rem}}
    .related a{{background:white;border:1px solid #d8d5ce;padding:.4rem .7rem;border-radius:999px;text-decoration:none;color:var(--emerald);font-size:.92rem}}
  </style>
  {header_footer_css}
</head>
<body>
  <a class="skip" href="#main">Skip to content</a>
  {navbar_html}
  {side_menu_html}
    <main id="main">
      <section class="section">
        <p>{page['hero_p']}</p>
        <p>{page['ops_p']}</p>
        {page.get('market_p') and f"<p>{page['market_p']}</p>"}
        <div class="grid">
        {cards_html}
      </div>
      <p class="muted small">{page['note']}</p>
      <div class="note">
        <strong>Local note:</strong> {page['local_section']}
      </div>
      <div class="related">
        {related_html}
      </div>
      {other_city_html}
    </section>
    <section class="section" id="faq">
      <h2 style="font:600 1.6rem/1.2 Cormorant Garamond,serif;color:var(--emerald);margin:0 0 1rem">Frequently asked questions</h2>
      {''.join([f'<div class="faq-item"><h3>{q}</h3><p>{a}</p></div>' for q,a in page['faq']])}
    </section>
    <section class="cta-bar">
      <h2 style="font:600 1.8rem/1.2 Cormorant Garamond,serif;margin:0 0 .5rem">Ready to explore the right approach?</h2>
      <p style="opacity:.95;margin:0 auto">Share your property priorities and we will suggest a practical way forward.</p>
      <a href="Contactus.html">{page['cta']}</a>
    </section>
  </main>
  {footer_html}
  {menu_js}
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
</body>
</html>"""
    return html


def make_sitemap(pages):
    urls = [
        f"""  <url>
    <loc>https://www.lotusleafcollection.com/{p['slug']}.html</loc>
    <lastmod>2026-10-07</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>"""
        for p in pages
    ]
    return "".join(urls)


if __name__ == "__main__":
    all_pages = []
    for region_name, region_data in REGIONS.items():
        for city, state in region_data["cities"]:
            page = make_hotel_management_page(city, state)
            all_pages.append(page)

    for service in SERVICES:
        for region_name, region_data in REGIONS.items():
            for city, state in region_data["cities"]:
                page = make_service_page(service, city, state)
                all_pages.append(page)

    slug_to_page = {p["slug"]: p for p in all_pages}
    for page in all_pages:
        related_links = []
        other_city_links = []
        if page["slug"].startswith("Hotel-Management-"):
            city = page["slug"].replace("Hotel-Management-", "")
            for service in SERVICES:
                sslug = f"{service['slug']}-{city}"
                if sslug in slug_to_page:
                    related_links.append((sslug, service["title"]))
        else:
            service_slug = None
            city = None
            for service in SERVICES:
                prefix = service["slug"] + "-"
                if page["slug"].startswith(prefix):
                    service_slug = service["slug"]
                    city = page["slug"].replace(prefix, "")
                    break
            if service_slug is None:
                continue
            for other in SERVICES:
                if other["slug"] != service_slug:
                    oslug = f"{other['slug']}-{city}"
                    if oslug in slug_to_page:
                        related_links.append((oslug, other["title"]))
            for region_name, region_data in REGIONS.items():
                for oc, st in region_data["cities"]:
                    oc_clean = oc.replace(" ", "")
                    if oc_clean == city:
                        continue
                    oslug = f"{service_slug}-{oc_clean}"
                    if oslug in slug_to_page and len(other_city_links) < 6:
                        other_city_links.append((oslug, oc))
        out_path = os.path.join(SITE_ROOT, f"{page['slug']}.html")
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(build_html(page, related_links=related_links, other_city_links=other_city_links))
        print(f"Wrote {out_path}")

    sitemap_path = os.path.join(SITE_ROOT, "sitemap.xml")
    with open(sitemap_path, "r", encoding="utf-8") as f:
        existing = f.read()
    new_urls = make_sitemap(all_pages)
    marker = "</urlset>"
    if marker in existing:
        existing = existing.replace(marker, new_urls + "\n" + marker)
    else:
        existing = existing.rstrip() + "\n" + new_urls + "\n</urlset>\n"
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write(existing)
    print(f"Updated sitemap with {len(all_pages)} new URLs")
