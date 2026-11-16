# TEST-002 — Existing interface review

**Input** (fixture provided inline):

> Haz una evaluación heurística de este formulario de login:
>
> ```html
> <div class="login">
>   <img src="logo.png">
>   <input type="text" placeholder="Usuario">
>   <input type="password" placeholder="Contraseña">
>   <div class="btn" onclick="login()">Entrar</div>
>   <span style="color:#ff0000;display:none" id="err">Error 401</span>
>   <a href="#">¿Problemas?</a>
> </div>
> ```

**Expected:** Mode B (or F with module 09, plus 07 offered or applied).

**Verifiable criteria**

- [must] Findings use `UX-n` IDs and include heuristic, evidence (quoting the code), severity 0–4
  with rationale, user impact, recommendation and validation method.
- [must] Detects at least: error message "Error 401" not understandable (H9); no password
  recovery path clarity / vague "¿Problemas?" link (H10/H3); placeholders as labels (H6 and
  accessibility); clickable `div` instead of button (H4 and accessibility).
- [must] Business impact is qualitative; no invented conversion or abandonment figures.
- [must] Findings are prioritized (e.g., Now / Next / Later).
- [should] Provides before/after for at least the top 2 findings.
- [should] Notes accessibility issues and cites WCAG criteria (1.1.1, 1.3.1/3.3.2, 2.1.1, 4.1.2).

**Execution log**

| Date | Agent / model | Result | Notes |
|---|---|---|---|
| — | — | Not executed | |
