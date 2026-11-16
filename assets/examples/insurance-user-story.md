# Ejemplo — Contratación de póliza de auto (entrada y análisis)

> Ejemplo de referencia del Modo A (Full Product Design). Todos los datos son ficticios. Las
> personas son proto-personas sin investigación real detrás.

## Entrada

**US-001** — "Como cliente, quiero contratar una póliza de seguros desde una aplicación web para
proteger mi vehículo sin necesidad de visitar una oficina." [SRC-1]

Contexto proporcionado [SRC-2]:

- REQ-001 Producto digital de seguros.
- REQ-002 Experiencia responsive.
- REQ-003 Formulario de contratación.
- REQ-004 Integración futura con APIs de cotización.
- REQ-005 Requisitos de accesibilidad.
- REQ-006 Objetivo de negocio: facilitar la contratación digital.

## Marco

- **Modo:** A — Full Product Design.
- **Módulos:** 01 (breve) → 02 → 04 → 05 → 06 (tokens base) → 07 → 08 → 10. Módulo 03 reducido a
  la estructura del flujo (no hay sitio completo en alcance).

## Supuestos y decisiones pendientes

| ID | Supuesto / decisión | Impacto | Cómo resolver |
|---|---|---|---|
| ASM-01 | Solo seguro de automóvil particular en esta fase | Pantalla de tipo de seguro con una opción activa | Confirmar con negocio |
| ASM-02 | El usuario puede cotizar sin registrarse; la cuenta se crea al pagar | Flujo de autenticación tardío | Confirmar con negocio / legal |
| ASM-03 | La API de cotización puede tardar varios segundos o fallar | Estados de carga y reintento | Contrato de API (REQ-004) |
| DEC-01 — PENDIENTE | Datos mínimos requeridos para cotizar | Campos de SCR-003 | Equipo de tarificación |
| DEC-02 — PENDIENTE | Reglas de suscripción (edad, antigüedad del vehículo, siniestralidad) | Validaciones y rechazos | Equipo de suscripción |
| DEC-03 — PENDIENTE | Medios de pago y gestión de pago pendiente | SCR-008 | Equipo de pagos |
| DEC-04 — PENDIENTE | Duración de sesión y política de borradores | Timeout / recuperación | Seguridad / negocio |

No se asumen reglas de tarificación, suscripción ni coberturas concretas (ver `insurance-user-flow.md`).

## Proto-personas [ASSUMPTION]

**PER-01 — Laura, conductora que renueva** · Contrata desde el móvil en ratos libres, quiere
comparar precio y coberturas sin llamadas, teme letra pequeña y cargos ocultos.
Validar con: entrevistas (5–8) a clientes que contrataron en el último año.

**PER-02 — Andrés, primer vehículo** · Poca experiencia con seguros; necesita entender términos
(franquicia, terceros, todo riesgo). Usa escritorio para trámites "serios".
Validar con: test de usabilidad del glosario contextual.

## JTBD

- JTBD-01: Cuando compro o renuevo un coche, quiero asegurarlo rápido y con confianza, para poder
  circular legalmente sin desplazarme a una oficina.
- JTBD-02: Cuando comparo opciones, quiero entender qué cubre cada una, para no pagar por algo que
  no necesito ni quedarme sin protección.

## Hipótesis

| ID | Hipótesis | Validación | Señal (umbral a definir) |
|---|---|---|---|
| H-01 | Mostrar una cotización orientativa antes de pedir datos personales reduce el abandono temprano | A/B test | Diferencia de tasa de llegada a SCR-004 |
| H-02 | Guardar el progreso automáticamente aumenta la finalización tras interrupciones | Analítica de reanudación | % de borradores reanudados |
| H-03 | Un comparador de coberturas en tabla reduce consultas al soporte | Test de usabilidad | ≥4/5 participantes eligen cobertura sin ayuda |

## Pain points y oportunidades (TO-BE, hipotéticos)

| ID | Pain point | Oportunidad | Prioridad |
|---|---|---|---|
| PP-01 | Formularios largos antes de ver el precio | OPP-01 Cotizar con datos mínimos (DEC-01) | Alta |
| PP-02 | Pérdida de datos al expirar la sesión | OPP-02 Borrador automático + aviso previo | Alta |
| PP-03 | Términos de cobertura confusos | OPP-03 Ayuda contextual y comparador | Media |
| PP-04 | Incertidumbre tras el pago | OPP-04 Confirmación con número de póliza y envío por email | Alta |

Siguientes artefactos: [insurance-user-flow.md](insurance-user-flow.md),
[insurance-wireframes.md](insurance-wireframes.md), [insurance-handoff.md](insurance-handoff.md),
[design-tokens-example.json](design-tokens-example.json).
