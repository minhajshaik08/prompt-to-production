import pandas as pd
import argparse

# Allowed schema
CATEGORIES = [
    "Pothole",
    "Flooding",
    "Streetlight",
    "Waste",
    "Noise",
    "Road Damage",
    "Heritage Damage",
    "Heat Hazard",
    "Drain Blockage",
    "Other"
]

SEVERITY_KEYWORDS = [
    "injury", "child", "school", "hospital", "ambulance",
    "fire", "hazard", "fell", "collapse"
]


def classify_complaint(description):
    text = description.lower()

    category = "Other"
    priority = "Standard"
    flag = ""
    reason = ""

    # CATEGORY RULES
    if "pothole" in text:
        category = "Pothole"
        reason = "Description contains the word 'pothole'."

    elif "flood" in text or "waterlogging" in text:
        category = "Flooding"
        reason = "Description mentions 'flood' or 'waterlogging'."

    elif "streetlight" in text or "light not working" in text:
        category = "Streetlight"
        reason = "Description contains 'streetlight' or lighting failure."

    elif "garbage" in text or "waste" in text or "trash" in text:
        category = "Waste"
        reason = "Description mentions garbage or waste."

    elif "noise" in text or "loud" in text:
        category = "Noise"
        reason = "Description mentions noise disturbance."

    elif "road damage" in text or "road broken" in text:
        category = "Road Damage"
        reason = "Description refers to road damage."

    elif "heritage" in text or "monument" in text:
        category = "Heritage Damage"
        reason = "Description references heritage site damage."

    elif "heat" in text or "temperature" in text:
        category = "Heat Hazard"
        reason = "Description mentions extreme heat."

    elif "drain" in text or "sewer" in text or "blocked drain" in text:
        category = "Drain Blockage"
        reason = "Description mentions drain blockage."

    else:
        category = "Other"
        reason = "No clear category keywords found."

    # PRIORITY RULE
    for word in SEVERITY_KEYWORDS:
        if word in text:
            priority = "Urgent"
            reason += f" Severity keyword '{word}' detected."
            break

    # Ambiguity flag
    if category == "Other":
        flag = "NEEDS_REVIEW"

    return category, priority, reason, flag


def batch_classify(input_file, output_file):
    df = pd.read_csv(input_file)

    categories = []
    priorities = []
    reasons = []
    flags = []

    for desc in df["description"]:
        cat, pri, rea, flg = classify_complaint(desc)

        categories.append(cat)
        priorities.append(pri)
        reasons.append(rea)
        flags.append(flg)

    df["category"] = categories
    df["priority"] = priorities
    df["reason"] = reasons
    df["flag"] = flags

    df.to_csv(output_file, index=False)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)

    args = parser.parse_args()

    batch_classify(args.input, args.output)
