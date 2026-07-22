# Policy Assistant Dashboard — v4 Enhancements

Short reference for the functions added in `CMAP_PolicyAssistant_v4.html` (built on v3). v3 stays intact; v4 adds broker-facing clarity and team-facing analytics.

## Broker side — understanding the AI output

- **Confidence badge** — every answer is tagged High / Medium / Low. Medium is shown for OCR-sourced chunks (e.g. Metro balloon) or hedged answers; Low when no policy chunk matched. Hover for the reason.
- **Per-chunk sources** — when an answer draws on more than one chunk, each retrieved chunk is listed on its own line with a rank, so the broker sees exactly what it was built from.
- **Why this answer?** — a button that explains the grounding and confirms retrieval was filtered to a single lender (guards against cross-lender mixing).
- **Ambiguity flags** — auto-warns on the three documented conflicts (Angle Start-Up score 500 vs 550, Angle prime-mover rate 8.99% vs 9.39%, Metro OCR balloon figures) instead of asserting one number.
- **Copy button** — one-click copy of the answer text.
- **Inline metric chips** — response time and estimated cost shown on each answer.

## Team side — collecting and comparing output

- **Thumbs up / down feedback** — rate each answer correct/wrong; feeds a broker-rated accuracy figure.
- **Add to compare + side-by-side modal** — tick answers into a tray, then open a column-by-column comparison showing each answer's latency, cost, confidence, and chunks.
- **Analytics tiles** (Usage & cost panel) — broker-rated accuracy %, answers rated (👍/👎), average API latency, and total tokens.
- **Coverage by lender** — a bar chart of how many queries hit each lender this session.
- **Export session** — download the full session log as CSV or JSON for offline analysis.

## Notes

- All state is in-session (resets on reload); no backend changes required.
- The three ambiguity flags are hard-coded to the known documented conflicts — extend `detectAmbiguity()` if new ones appear.
- Confidence is a heuristic (`assessConfidence()`), not a model score; treat it as a prompt to double-check, not a guarantee.
