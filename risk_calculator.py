import csv
import os

RATING_VALUES = {
    "Low": 1,
    "Medium": 2,
    "High": 3
}

def convert_rating(value):
    return RATING_VALUES.get(value, 0)

def calculate_risk_score(likelihood, impact):
    return likelihood * impact

def classify_risk(score):
    if score >= 9:
        return "High"
    elif score >= 4:
        return "Medium"
    else:
        return "Low"

base_path = os.path.dirname(__file__)
csv_path = os.path.join(base_path, "risk_register.csv")

with open(csv_path, "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    risks = list(reader)

print("\nCybersecurity Risk Register Report\n")
print("=" * 50)

scored_risks = []
mismatches = []

for risk in risks:
    likelihood_text = risk["Likelihood"]
    impact_text = risk["Impact"]
    given_rating = risk["Risk Rating"]

    likelihood_score = convert_rating(likelihood_text)
    impact_score = convert_rating(impact_text)

    numeric_score = calculate_risk_score(likelihood_score, impact_score)
    calculated_rating = classify_risk(numeric_score)

    scored_risks.append({
        "Risk ID": risk["Risk ID"],
        "Asset/Area": risk["Asset/Area"],
        "Threat": risk["Threat"],
        "Score": numeric_score
    })

    if given_rating != calculated_rating:
        mismatches.append({
            "Risk ID": risk["Risk ID"],
            "Given": given_rating,
            "Calculated": calculated_rating
        })

    print(f"Risk ID: {risk['Risk ID']}")
    print(f"Asset/Area: {risk['Asset/Area']}")
    print(f"Threat: {risk['Threat']}")
    print(f"Vulnerability: {risk['Vulnerability']}")
    print(f"Likelihood: {likelihood_text} ({likelihood_score})")
    print(f"Impact: {impact_text} ({impact_score})")
    print(f"Given Risk Rating: {given_rating}")
    print(f"Calculated Risk Score: {numeric_score}")
    print(f"Calculated Risk Level: {calculated_rating}")
    print(f"Existing Controls: {risk['Existing Controls']}")
    print(f"Recommended Mitigation: {risk['Recommended Mitigation']}")
    print(f"Owner: {risk['Owner']}")
    print(f"Status: {risk['Status']}")
    print("-" * 50)

scored_risks.sort(key=lambda x: x["Score"], reverse=True)

print("\nTop 3 Highest Risks")
print("=" * 50)
for i, risk in enumerate(scored_risks[:3], start=1):
    print(f"{i}. {risk['Asset/Area']} - {risk['Threat']} (Score: {risk['Score']})")

print("\nRating Mismatch Check")
print("=" * 50)
if mismatches:
    for mismatch in mismatches:
        print(
            f"{mismatch['Risk ID']}: Given = {mismatch['Given']}, "
            f"Calculated = {mismatch['Calculated']}"
        )
else:
    print("No rating mismatches found.")
