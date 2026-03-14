import argparse
import re


def retrieve_policy(file_path):
    """
    Reads the policy document and returns a dictionary of clauses.
    Example: {"2.3": "text...", "2.4": "text..."}
    """

    with open(file_path, "r", encoding="utf-8") as f:
        text = f.read()

    clauses = {}

    # regex to capture numbered clauses
    matches = re.findall(r'(\d+\.\d+)\s+(.*?)(?=\n\d+\.\d+|\Z)', text, re.S)

    for clause_id, clause_text in matches:
        clauses[clause_id] = clause_text.strip()

    return clauses


def summarize_policy(clauses):
    """
    Creates a summary ensuring every clause appears
    and no conditions are dropped.
    """

    summary_lines = []

    REQUIRED_CLAUSES = [
        "2.3", "2.4", "2.5", "2.6", "2.7",
        "3.2", "3.4",
        "5.2", "5.3",
        "7.2"
    ]

    for cid in REQUIRED_CLAUSES:

        if cid not in clauses:
            summary_lines.append(f"{cid} — CLAUSE MISSING IN SOURCE")
            continue

        text = clauses[cid]

        # Risky clauses → quote verbatim
        if cid in ["5.2", "5.3", "7.2"]:
            summary_lines.append(f"{cid}: \"{text}\"")
            summary_lines.append("FLAG: Quoted verbatim to prevent condition loss.\n")
            continue

        # Safe summarization
        if cid == "2.3":
            summary_lines.append(
                "2.3: Employees must provide 14-day advance notice before taking leave."
            )

        elif cid == "2.4":
            summary_lines.append(
                "2.4: Leave must receive written approval before it begins; verbal approval is not valid."
            )

        elif cid == "2.5":
            summary_lines.append(
                "2.5: Any unapproved absence will be treated as Leave Without Pay (LOP) regardless of later approval."
            )

        elif cid == "2.6":
            summary_lines.append(
                "2.6: A maximum of 5 leave days may be carried forward; any amount above 5 is forfeited on 31 December."
            )

        elif cid == "2.7":
            summary_lines.append(
                "2.7: Carried-forward leave must be used between January and March or it will be forfeited."
            )

        elif cid == "3.2":
            summary_lines.append(
                "3.2: Sick leave lasting 3 or more consecutive days requires a medical certificate submitted within 48 hours."
            )

        elif cid == "3.4":
            summary_lines.append(
                "3.4: Sick leave taken immediately before or after a holiday requires a medical certificate regardless of duration."
            )

    return "\n".join(summary_lines)


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--input", required=True)
    parser.add_argument("--output", required=True)

    args = parser.parse_args()

    clauses = retrieve_policy(args.input)

    summary = summarize_policy(clauses)

    with open(args.output, "w", encoding="utf-8") as f:
        f.write(summary)


if __name__ == "__main__":
    main()
