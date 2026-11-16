# TEST-005 — Responsive specification

**Input**

> Define el comportamiento responsive de un panel de pedidos con: barra lateral de navegación
> (8 secciones), tabla de pedidos (9 columnas), filtros y un panel de detalle.

**Verifiable criteria**

- [must] Breakpoint matrix for at least compact, medium and expanded, with a content-based
  justification for each change (not just device names).
- [must] Table strategy on small screens that avoids squeezing 9 columns (cards, priority
  columns, or labelled scroll region as last resort) with rationale.
- [must] Navigation adaptation (e.g., drawer / bottom nav limits) and filters adaptation.
- [must] Touch targets ≥ 24×24 CSS px (2.5.8) and reflow at 320 CSS px (1.4.10) considered.
- [must] Sticky elements do not obscure focus (2.4.11) — mentioned.
- [must] Responsive checks not run in a real viewport are marked NOT VERIFIED.
- [should] Responsive wireframes for compact and expanded.

**Execution log**

| Date | Agent / model | Result | Notes |
|---|---|---|---|
| — | — | Not executed | |
