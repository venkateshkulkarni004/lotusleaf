import os
import re
from bs4 import BeautifulSoup
from collections import Counter

SITE_ROOT = r"D:\soical media\ssm\saveweb2zip-com-pdf-site-builder-33-preview-emergentagent-com\leafcollection"

# Keywords to always highlight
SERVICE_KEYWORDS = [
    "Hotel Management", "Hospitality Consulting", "Hotel Pre-Opening",
    "Hospitality Training", "Hospitality Commercial", "Hospitality Audit",
    "Hotel Revenue Management", "Resort Management"
]

CITIES = [
    "AbuDhabi", "Ahmedabad", "Amsterdam", "Bangalore", "Berlin", "Boston",
    "CapeTown", "Chandigarh", "Chennai", "Chicago", "Coimbatore", "Dallas",
    "Delhi", "Doha", "Dubai", "Goa", "Houston", "Hyderabad", "Indore",
    "Istanbul", "Jaipur", "Jeddah", "Johannesburg", "Kochi", "Kolkata",
    "Lagos", "LasVegas", "Lisbon", "London", "LosAngeles", "Lucknow",
    "Madrid", "Miami", "Mumbai", "Muscat", "Mysore", "Nagpur", "Nairobi",
    "NewYork", "Paris", "Pune", "Riyadh", "Rome", "SanFrancisco", "Surat",
    "Trivandrum", "Vadodara", "Vienna", "Visakhapatnam", "WashingtonDC", "Zurich"
]

def extract_keywords_from_file(filepath):
    filename = os.path.basename(filepath)
    keywords = set()
    content_words = []
    
    try:
        with open(filepath, "r", encoding="utf-8", errors="ignore") as f:
            soup = BeautifulSoup(f.read(), "lxml")
    except Exception as e:
        return {"file": filename, "error": str(e)}
    
    # Title
    title = ""
    if soup.title and soup.title.string:
        title = soup.title.string.strip()
        keywords.add(title)
    
    # Meta description
    meta_desc = ""
    desc_tag = soup.find("meta", attrs={"name": "description"})
    if desc_tag:
        meta_desc = desc_tag.get("content", "").strip()
        keywords.add(meta_desc)
    
    # Meta keywords
    meta_keywords = ""
    kw_tag = soup.find("meta", attrs={"name": "keywords"})
    if kw_tag:
        meta_keywords = kw_tag.get("content", "").strip()
        for kw in meta_keywords.split(","):
            kw = kw.strip()
            if kw:
                keywords.add(kw)
    
    # H1
    for h1 in soup.find_all("h1"):
        text = h1.get_text(strip=True)
        if text:
            keywords.add(text)
            content_words.append(text)
    
    # H2
    for h2 in soup.find_all("h2"):
        text = h2.get_text(strip=True)
        if text:
            keywords.add(text)
            content_words.append(text)
    
    # H3
    for h3 in soup.find_all("h3"):
        text = h3.get_text(strip=True)
        if text:
            keywords.add(text)
            content_words.append(text)
    
    # Detect service type from filename or content
    service_type = ""
    for svc in SERVICE_KEYWORDS:
        svc_slug = svc.lower().replace(" ", "-")
        if svc_slug in filename.lower() or svc.lower() in filename.lower() or svc.lower() in title.lower():
            service_type = svc
            keywords.add(svc)
            break
    
    # Detect city
    city = ""
    for c in CITIES:
        if c.lower() in filename.lower() or c in title:
            city = c
            keywords.add(c)
            break
    
    # Extract some body text (first few paragraphs)
    body_text = ""
    for p in soup.find_all("p"):
        text = p.get_text(strip=True)
        if len(text) > 20:
            body_text += " " + text
        if len(body_text) > 500:
            break
    
    # Clean up and split body text into words
    body_words = re.findall(r'[A-Za-z][A-Za-z\s\-]+', body_text)
    body_words = [w.strip() for w in body_words if len(w.strip()) > 3]
    
    return {
        "file": filename,
        "title": title,
        "meta_description": meta_desc,
        "meta_keywords": meta_keywords,
        "service_type": service_type,
        "city": city,
        "h1_tags": [h.get_text(strip=True) for h in soup.find_all("h1") if h.get_text(strip=True)],
        "h2_tags": [h.get_text(strip=True) for h in soup.find_all("h2") if h.get_text(strip=True)],
        "h3_tags": [h.get_text(strip=True) for h in soup.find_all("h3") if h.get_text(strip=True)],
        "content_words": body_words[:50],
        "all_keywords": sorted([k for k in keywords if k])
    }

def main():
    html_files = []
    for root, dirs, files in os.walk(SITE_ROOT):
        # Skip hidden dirs and assets
        dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ('css', 'fonts', 'images', 'js')]
        for f in files:
            if f.lower().endswith('.html'):
                html_files.append(os.path.join(root, f))
    
    html_files.sort()
    
    results = []
    for fp in html_files:
        results.append(extract_keywords_from_file(fp))
    
    # Write report
    report_path = os.path.join(SITE_ROOT, "keyword_report.txt")
    with open(report_path, "w", encoding="utf-8") as out:
        out.write(f"LotusLeaf Collection — Keyword Report\n")
        out.write(f"Total pages analyzed: {len(results)}\n")
        out.write("=" * 80 + "\n\n")
        
        for r in results:
            if "error" in r:
                out.write(f"FILE: {r['file']}\n")
                out.write(f"  ERROR: {r['error']}\n\n")
                continue
            
            out.write(f"FILE: {r['file']}\n")
            out.write(f"  Title: {r['title']}\n")
            out.write(f"  Service: {r['service_type']}\n")
            out.write(f"  City: {r['city']}\n")
            out.write(f"  Meta Description: {r['meta_description'][:200]}\n")
            out.write(f"  Meta Keywords: {r['meta_keywords'][:200]}\n")
            out.write(f"  H1: {', '.join(r['h1_tags'])}\n")
            out.write(f"  H2: {', '.join(r['h2_tags'][:5])}\n")
            out.write(f"  H3: {', '.join(r['h3_tags'][:5])}\n")
            out.write(f"  Keywords ({len(r['all_keywords'])}): {', '.join(r['all_keywords'][:20])}\n")
            out.write(f"  Content words: {', '.join(r['content_words'][:15])}\n")
            out.write("\n" + "-" * 80 + "\n\n")
        
        # Summary stats
        service_counts = Counter(r.get("service_type", "") for r in results if r.get("service_type"))
        city_counts = Counter(r.get("city", "") for r in results if r.get("city"))
        
        out.write("\n\nSUMMARY STATISTICS\n")
        out.write("=" * 80 + "\n")
        out.write("Service types distribution:\n")
        for svc, count in service_counts.most_common():
            out.write(f"  {svc}: {count}\n")
        out.write("\nCities distribution (top 20):\n")
        for city, count in city_counts.most_common(20):
            out.write(f"  {city}: {count}\n")
    
    print(f"Report written to: {report_path}")
    print(f"Total pages: {len(results)}")
    
    # Print quick summary to console
    print("\nQuick Summary:")
    for r in results[:10]:
        print(f"  {r['file']} | {r.get('service_type','')} | {r.get('city','')} | {r.get('title','')[:60]}")
    print(f"  ... and {len(results)-10} more")

if __name__ == "__main__":
    main()
