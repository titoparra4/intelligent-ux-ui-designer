# Ejemplo — Wireframes de baja fidelidad (representación textual)

> Estos wireframes son **representaciones textuales ASCII**, no archivos de Figma ni imágenes.
> Se documentan en detalle SCR-003 y SCR-004; el resto sigue el mismo formato en un proyecto real.

## SCR-003 — Información del vehículo

| Campo | Valor |
|---|---|
| Objetivo del usuario | Dar los datos mínimos para obtener un precio |
| Historia | US-001 · FLOW-001 paso 2 |

### Expanded (≥1024px)

```text
+----------------------------------------------------------------------+
| ==== Logo                                   Ayuda ▸    Acceder ▸ ==== |
| Paso 2 de 7 · Tu vehículo                     [■■□□□□□]              |
|                                                                      |
| H1 Cuéntanos sobre tu vehículo              | Resumen                |
|                                             | Seguro: Automóvil      |
| Matrícula *            [__________]         | Precio: tras este paso |
|   Ej.: 1234 ABC                             |                        |
| Marca *                [v Selecciona  ]     | ¿Dudas? Ayuda ▸        |
| Modelo *               [v Selecciona  ]     |                        |
| Año de matriculación * [____]               |                        |
| Uso del vehículo *  ( ) Particular          |                        |
|                     ( ) Profesional         |                        |
|                                             |                        |
| [ ← Atrás ]                    [ Ver mi precio → ]                   |
| Guardado automáticamente · hace 1 min                                |
+----------------------------------------------------------------------+
```

### Compact (<600px)

```text
+------------------------------+
| ☰  Logo              Ayuda ▸ |
| Paso 2 de 7  [■■□□□□□]       |
| H1 Tu vehículo               |
| Matrícula *                  |
| [__________________________] |
| Marca *                      |
| [v Selecciona             ]  |
| Modelo *                     |
| [v Selecciona             ]  |
| Año de matriculación *       |
| [____]                       |
| Uso *                        |
| ( ) Particular               |
| ( ) Profesional              |
| ▸ Ver resumen                |
| [ Ver mi precio →          ] |
| [ ← Atrás                  ] |
+------------------------------+
```

### Estado: error de validación

```text
| ⚠ Revisa 2 campos para continuar:            |
|   ▸ Matrícula: introduce una matrícula        |
|   ▸ Año: introduce un año entre 1950 y 2026   |   (rango: DEC-01)
| ...                                          |
| Matrícula *            [__________] ⚠        |
|   Introduce una matrícula, p. ej. 1234 ABC   |
```

### Componentes

| CMP | Uso | Variante |
|---|---|---|
| CMP-001 Button | "Ver mi precio" / "Atrás" | primary / secondary |
| CMP-002 Input | Matrícula, Año | default |
| CMP-003 Select | Marca, Modelo (Modelo depende de Marca) | default |
| CMP-004 Radio group | Uso | default |
| CMP-012 Progress indicator | Paso 2 de 7 | stepper |
| CMP-013 Error summary | Resumen de errores | — |

### Interacciones

| ID | Elemento | Disparador | Comportamiento | Foco después |
|---|---|---|---|---|
| INT-01 | Marca | Cambio | Carga modelos; Modelo se reinicia y anuncia "Modelos actualizados" | Permanece en Marca |
| INT-02 | Ver mi precio | Click / Enter | Valida; si OK, llama a API y muestra carga | Resumen de errores o H1 de SCR-004 |
| INT-03 | Atrás | Click / Enter | Vuelve a SCR-002 conservando datos | H1 de SCR-002 |

### Estados

| Estado | Comportamiento |
|---|---|
| Default | Campos vacíos (o prellenados si hay borrador); foco en H1 al cargar |
| Loading | Tras enviar: botón en estado loading, texto "Calculando tu precio…" anunciado (live region); formulario no editable |
| Empty | N/A — formulario |
| Error | Fallo de API: mensaje "No hemos podido calcular tu precio ahora. Tus datos están guardados." + Reintentar |
| Success | Navega a SCR-004 |
| Disabled | Modelo deshabilitado hasta elegir Marca, con texto de ayuda "Elige primero la marca" |
| Validation error | Resumen + mensajes en línea; datos conservados (AC-001) |
| Partial completion | Indicador "Guardado automáticamente" (OPP-02) |
| Timeout | Aviso 2 min antes de expirar con "Seguir aquí" (WCAG 2.2.1); plazo según DEC-04 |
| Unauthorized | N/A — paso anónimo (ASM-02) |

### Accesibilidad

- `<form>` con `<h1>` único; radio en `<fieldset>`/`<legend>`.
- Etiquetas visibles asociadas; ejemplo de formato vinculado con `aria-describedby`.
- `autocomplete` no aplica a datos del vehículo; sí en SCR-006 (1.3.5).
- Mensajes de error: texto + icono, no solo color (1.4.1); resumen enfocable (3.3.1).
- Objetivos táctiles ≥ 44×44 px en compact (supera 2.5.8).
- Barra de progreso con texto "Paso 2 de 7", no solo gráfico.

### Justificación

- DD-001 — Precio antes de datos personales (H-01, P1, P9).
- DD-003 — Resumen lateral en expanded y colapsable en compact para no desplazar el formulario (P6).

## SCR-004 — Resumen de cotización

```text
+----------------------------------------------------------------------+
| Paso 3 de 7 · Tu precio                       [■■■□□□□]              |
| H1 Tu precio orientativo                                             |
|                                                                      |
|   Desde  XXX,XX €/año            (valor devuelto por la API)         |
|   Válido hasta: DD/MM/AAAA                                           |
|   Basado en: Marca X · Modelo Y · 2021 · Particular [ Editar ]       |
|                                                                      |
|   ⓘ El precio final puede variar según la cobertura elegida.         |
|                                                                      |
| [ ← Atrás ]                         [ Elegir cobertura → ]           |
+----------------------------------------------------------------------+
```

| Estado | Comportamiento |
|---|---|
| Loading | Skeleton del bloque de precio; `aria-busy="true"` |
| Error | Ver E2 en FLOW-001 |
| Cotización no disponible | E3: explicación neutra + teléfono/chat; sin culpar al usuario |
| Cotización caducada | Mensaje + "Recalcular" conservando datos |

## SCR-001, SCR-002, SCR-005 … SCR-009

Mismo formato. Puntos clave a documentar:

- SCR-005: comparador de coberturas en tabla (expanded) y tarjetas apilables (compact); coberturas
  según catálogo real — no inventadas.
- SCR-007: resumen editable por bloques, aceptación explícita de condiciones (3.3.4).
- SCR-008: sin redirecciones inesperadas; pago pendiente y rechazado según FLOW-001.
- SCR-009: número de póliza, descarga, envío por email, siguiente paso.
