# Skills

## classify_complaint

Input: One complaint description.

Output:
- category
- priority
- reason
- flag

Rules:
- Category must match one of the allowed schema values exactly.
- Priority is set to Urgent if severity keywords appear:
  injury, child, school, hospital, ambulance, fire, hazard, fell, collapse.
- Reason must reference words from the description.
- If category cannot be confidently determined → flag = NEEDS_REVIEW.

---

## batch_classify

Reads an input CSV file containing complaint descriptions.

Steps:
1. Load CSV file.
2. For each row call `classify_complaint`.
3. Collect:
   - category
   - priority
   - reason
   - flag
4. Write results to output CSV.

Output file format:

description | category | priority | reason | flag
