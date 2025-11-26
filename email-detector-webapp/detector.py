from bs4 import BeautifulSoup
import json

# Step 1: Read HTML file
def read_html_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        content = file.read()
    return content

# Step 2: Find suspicious tags with severity
def find_suspicious_tags(html):
    soup = BeautifulSoup(html, 'html.parser')
    suspicious = []

    for tag in soup.find_all(True):  # Loop through all tags
        reason = ""
        severity = None

        # Check for display: none
        if "style" in tag.attrs and "display:none" in tag["style"].replace(" ", "").lower():
            reason = "Hidden using display:none"
            severity = "Medium"

        # Check for 1x1 image
        if tag.name == "img":
            width = tag.get("width", "")
            height = tag.get("height", "")
            if width == "1" and height == "1":
                reason = "Tracking image (1x1 pixel)"
                severity = "High"

        # Check for tiny font
        if "style" in tag.attrs and "font-size" in tag["style"].lower():
            style = tag["style"].lower()
            if "font-size:1px" in style or "font-size:2px" in style:
                reason = "Very small font-size"
                severity = "Low"

        if reason:  # If anything suspicious found
            suspicious.append({
                "tag": str(tag),
                "reason": reason,
                "severity": severity
            })

    return suspicious

# Step 3: Save result to JSON
def save_results_to_json(data, filename="report.json"):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    print(f"✅ Report saved")