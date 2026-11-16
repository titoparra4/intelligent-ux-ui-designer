# TEST-003 — Accessibility audit

**Input**

> Review the accessibility of this checkout step. Text color #8A8A8A on #FFFFFF; primary button
> white text on #4DA3FF; error shown only with a red border; a 10-minute session timeout with no
> warning; card number field has no visible label, only a placeholder; the "Pay" button is 20×20 px
> on mobile.

**Verifiable criteria**

- [must] Uses `A11Y-n` IDs with element, problem, WCAG criterion (number, name, level), severity,
  evidence + method, recommendation and verification method.
- [must] Maps at least: 1.4.3 (text contrast), 1.4.1 (color only), 2.2.1 (timing), 3.3.2 / 1.3.1
  (label), 2.5.8 (target size).
- [must] If contrast ratios are given, they are computed correctly (≈3.5:1 for #8A8A8A/#FFFFFF;
  ≈2.6:1 for #FFFFFF/#4DA3FF) and labelled as computed; otherwise marked NOT VERIFIED.
- [must] States the review method (static, from description) and lists pending manual checks
  (keyboard, screen reader, zoom/reflow).
- [must] Does **not** claim WCAG conformance.
- [must] Does not cite 4.1.1 Parsing as an active criterion.
- [should] Proposes token-level fixes (e.g., darker text color meeting 4.5:1).

**Execution log**

| Date | Agent / model | Result | Notes |
|---|---|---|---|
| — | — | Not executed | |
