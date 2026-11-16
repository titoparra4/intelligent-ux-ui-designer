# Ejemplo — Handoff (extracto) · Contratación de póliza de auto

Alcance: US-001 · FLOW-001 · SCR-003, SCR-004, SCR-007, SCR-008. Estado: Draft.

## Matriz de validaciones (SCR-003)

| Campo | Obligatorio | Formato / restricción | Validar en | Mensaje | Fuente |
|---|---|---|---|---|---|
| Matrícula | Sí | Formato a confirmar | Blur + envío | "Introduce una matrícula, p. ej. 1234 ABC" | DEC-01 |
| Marca | Sí | Valor de catálogo | Envío | "Elige la marca" | DEC-01 |
| Modelo | Sí | Depende de Marca | Envío | "Elige el modelo" | DEC-01 |
| Año | Sí | Entero; rango pendiente | Blur + envío | "Introduce un año entre {min} y {max}" | DEC-01 / DEC-02 |
| Uso | Sí | Particular / Profesional | Envío | "Indica el uso del vehículo" | DEC-01 |

## Dependencias técnicas

| Dependencia | Datos | Fallos | Tratamiento UX |
|---|---|---|---|
| API de cotización (REQ-004, futura) | Datos de SCR-003 → precio, validez, id de cotización | Timeout, 5xx, sin cotización | E2 reintentar; E3 salida asistida |
| Pasarela de pago (DEC-03) | Importe, id de cotización | Rechazo, pendiente | E5, E6 |
| Borrador | Estado del formulario | Fallo al guardar | Aviso no bloqueante "No se ha podido guardar" |

## Criterios de aceptación UX

**AC-001 — Validación de campos obligatorios**
Given el usuario está completando el formulario de datos del vehículo (SCR-003)
When intenta continuar sin completar un campo obligatorio
Then el sistema impide el avance
And muestra un resumen de errores que recibe el foco y enumera cada campo pendiente con enlace al campo
And cada campo pendiente muestra un mensaje en línea asociado programáticamente
And los datos ya introducidos se conservan

**AC-002 — Formato inválido**
Given el usuario ha escrito un año fuera del rango permitido (DEC-01)
When el campo pierde el foco
Then se muestra el mensaje "Introduce un año entre {min} y {max}" junto al campo
And el mensaje no depende solo del color

**AC-003 — Fallo de la API de cotización**
Given el usuario ha enviado datos válidos en SCR-003
When la API devuelve error o no responde en el tiempo límite definido (DEC-04)
Then se muestra un mensaje que indica que no se ha podido calcular el precio y que los datos están guardados
And se ofrece la acción "Reintentar" con el foco sobre ella
And los datos del formulario se conservan

**AC-004 — Aviso de sesión**
Given el usuario está en cualquier paso entre SCR-003 y SCR-008
When faltan 2 minutos para que expire la sesión
Then aparece un diálogo accesible que anuncia el tiempo restante y permite ampliar la sesión con una sola acción

**AC-005 — Navegación por teclado**
Given el usuario navega solo con teclado en SCR-003
When recorre la página con Tab
Then el orden de foco sigue el orden visual
And cada elemento enfocado muestra un indicador visible

**AC-006 — Aceptación de condiciones**
Given el usuario está en SCR-007
When intenta ir al pago sin aceptar las condiciones
Then no avanza y se indica en texto que debe aceptar las condiciones para continuar

**AC-007 — Pago rechazado**
Given el usuario confirma el pago en SCR-008
When la pasarela rechaza el pago
Then se muestra un mensaje que explica que el pago no se ha completado y no se ha realizado ningún cargo (a confirmar DEC-03)
And se ofrece reintentar o usar otro medio sin volver a introducir los datos previos

## Escenarios QA

| QA | AC | Tipo | Pasos | Resultado esperado | Prioridad |
|---|---|---|---|---|---|
| QA-001 | AC-001 | Negativo | Dejar Matrícula vacía → "Ver mi precio" | Resumen con foco + error en línea; resto de datos intactos | Alta |
| QA-002 | AC-001 | Positivo | Completar todos los campos válidos → enviar | Estado loading y navegación a SCR-004 | Alta |
| QA-003 | AC-002 | Límite | Año = min−1, min, max, max+1 | Error solo en min−1 y max+1 | Media |
| QA-004 | AC-003 | Resiliencia | Simular timeout de la API | Mensaje + Reintentar con foco; datos conservados | Alta |
| QA-005 | AC-004 | Accesibilidad | Esperar al aviso; ampliar con teclado | Diálogo anunciado; sesión ampliada | Alta |
| QA-006 | AC-005 | Accesibilidad | Recorrer SCR-003 con Tab / Shift+Tab | Orden lógico, foco visible | Alta |
| QA-007 | AC-001 | Responsive | Repetir QA-001 a 320 CSS px y 200% zoom | Sin scroll horizontal; resumen visible | Media |
| QA-008 | AC-006 | Negativo | Pagar sin aceptar condiciones | Bloqueo con mensaje | Alta |
| QA-009 | AC-007 | Negativo | Tarjeta de prueba rechazada | Mensaje + reintento sin perder datos | Alta |

## Trazabilidad

| REQ | US | FLOW | SCR | CMP | AC | QA | DD |
|---|---|---|---|---|---|---|---|
| REQ-003 | US-001 | FLOW-001 | SCR-003 | CMP-001..004, 012, 013 | AC-001, AC-002, AC-005 | QA-001..003, 006, 007 | DD-001 |
| REQ-004 | US-001 | FLOW-001 | SCR-003, SCR-004 | CMP-001 | AC-003 | QA-004 | — |
| REQ-005 | US-001 | FLOW-001 | SCR-003…SCR-008 | todos | AC-004, AC-005 | QA-005..007 | — |
| REQ-006 | US-001 | FLOW-001 | SCR-007, SCR-008 | CMP-001 | AC-006, AC-007 | QA-008, QA-009 | DD-001 |

## Quality gates

| Gate | Estado | Evidencia | Pendiente |
|---|---|---|---|
| G1 Cobertura de requisitos | PASS | REQ-003…006 trazados; REQ-001/002 cubiertos por alcance y responsive | — |
| G2 Coherencia UX | PASS | Patrón de error, progreso y CTA idénticos en SCR-003…008 | — |
| G3 Accesibilidad | NOT VERIFIED | Solo revisión estática del diseño | Prueba con teclado y lector de pantalla tras implementar |
| G4 Consistencia del sistema de diseño | PASS | Componentes CMP-001…013 y tokens de `design-tokens-example.json` | — |
| G5 Responsive | PASS | Compact y expanded definidos para SCR-003; resto pendiente de detalle | Completar medium |
| G6 Preparado para desarrollo | FAIL | DEC-01…DEC-04 abiertas afectan validaciones y tiempos | Resolver decisiones con negocio |
| G7 Preparado para QA | PASS | Cada AC tiene escenario; positivos y negativos | — |
| G8 Evidencia y honestidad | PASS | Personas marcadas como proto-personas; sin métricas inventadas | — |
