# Skills

## retrieve_policy

Input:
Policy document (.txt)

Process:
1. Load text file
2. Identify numbered clauses using regex pattern (\d+\.\d+)
3. Extract clause id and full text
4. Return structured dictionary

Output Example:
{
  "2.3": "Employees must provide 14-day notice...",
  "2.4": "Written approval is required..."
}

---

## summarize_policy

Input:
Structured clause dictionary.

Rules:
- Every required clause must appear in the summary.
- Clause IDs must be preserved.
- Multi-condition obligations must retain ALL conditions.
- If summarizing risks meaning loss → quote clause verbatim and flag it.
- No external information may be added.

Output:
A compliant summary referencing each clause.
