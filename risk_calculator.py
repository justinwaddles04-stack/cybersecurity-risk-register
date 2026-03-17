import csv

LIKELIHOOD_VALUES = {
    "Low": 1,
    "Medium": 2,
    "High": 3
}

IMPACT_VALUES = {
    "Low": 1,
    "Medium": 2,
    "High": 3
}

def convert_rating(value):
    return LIKELIHOOD_VALUES.get(value, 0)

def calculate_risk_score(likelihood, impact):
    return likelihood * impact

def classify_risk(score):
    if score >= 9:
        return "High"
    elif score >= 4:
        return "Medium"
    else:
        return "Low"

with open("risk_register.csv", "r", newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    risks = list(reader)

print("\nCybersecurity Risk Register Report\n")
print("=" * 50)

for risk in risks:
    likelihood_text = risk["Likelihood"]
    impact_text = risk["Impact"]

    likelihood_score = convert_rating(likelihood_text)
    impact_score = convert_rating(impact_text)

    numeric_score = calculate_risk_score(likelihood_score, impact_score)
    calculated_rating = classify_risk(numeric_score)

    print(f"Risk ID: {risk['Risk ID']}")
    print(f"Asset/Area: {risk['Asset/Area']}")
    print(f"Threat: {risk['Threat']}")
    print(f"Vulnerability: {risk['Vulnerability']}")
    print(f"Likelihood: {likelihood_text} ({likelihood_score})")
    print(f"Impact: {impact_text} ({impact_score})")
    print(f"Given Risk Rating: {risk['Risk Rating']}")
    print(f"Calculated Risk Score: {numeric_score}")
    print(f"Calculated Risk Level: {calculated_rating}")
    print(f"Existing Controls: {risk['Existing Controls']}")
    print(f"Recommended Mitigation: {risk['Recommended Mitigation']}")
    print(f"Owner: {risk['Owner']}")
    print(f"Status: {risk['Status']}")
    print("-" * 50)
