# TEST-001 — User story to design · TEST-007 — Incomplete requirements

## TEST-001 — User story to design

**Input**

> Como cliente, quiero contratar una póliza de seguros desde una aplicación web para proteger mi
> vehículo sin necesidad de visitar una oficina. Contexto: experiencia responsive, integración
> futura con APIs de cotización, requisitos de accesibilidad, objetivo: facilitar la contratación
> digital.

**Expected:** Mode A; output comparable in scope to `assets/examples/insurance-*.md`.

**Verifiable criteria**

- [must] States Mode A and the modules it will run.
- [must] Responds in Spanish.
- [must] Personas are labelled proto-personas / assumptions; no invented research or metrics.
- [must] Flow covers: tipo de seguro → vehículo → cotización → cobertura → datos personales →
  revisión → pago → confirmación.
- [must] Alternative paths include at least: datos incompletos, formato inválido, fallo de API,
  cotización no disponible, sesión expirada, pago rechazado, pago pendiente, cancelación,
  recuperación.
- [must] Each documented screen has an `SCR-n` ID, states table and accessibility notes.
- [must] At least one AC in Given/When/Then equivalent to AC-001 (required fields, data kept,
  accessible messages).
- [must] Does not invent underwriting, pricing or coverage rules; marks them pending.
- [must] Ends with a quality gate summary (PASS / FAIL / NOT VERIFIED); G3 is not PASS without
  executed accessibility checks.
- [should] Mermaid syntax valid (passes `validate_skill.py` lint if saved to a file).

## TEST-007 — Incomplete requirements

**Input**

> Necesito una pantalla para que los usuarios gestionen sus suscripciones.

**Verifiable criteria**

- [must] Does not block: produces a useful first proposal (flow and/or wireframe).
- [must] Lists explicit assumptions (`ASM-n`) — e.g., subscription types, payment provider,
  cancellation rules.
- [must] Asks at most 3 targeted questions, only for gaps that change the design.
- [must] Marks pending decisions (`DEC-n — PENDING`), e.g., cancellation and refund policy.
- [must] Does not invent business rules as facts.
- [should] Uses Mode F or a reduced Mode A and says why.

**Execution log**

| Test | Date | Agent / model | Result | Notes |
|---|---|---|---|---|
| TEST-001 | — | — | Not executed | |
| TEST-007 | — | — | Not executed | |
