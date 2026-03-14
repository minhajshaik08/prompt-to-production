# Policy Summarization Agent Rules

1. Every numbered clause must appear in the final summary.
2. Multi-condition obligations must preserve all conditions.
3. Conditions must never be silently removed.
4. No external knowledge may be added.
5. If summarization risks meaning loss:
   - Quote the clause verbatim
   - Add a flag explaining why.
6. Clause references (e.g., 2.3, 5.2) must remain visible in the summary.
