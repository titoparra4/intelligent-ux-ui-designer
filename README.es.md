# Intelligent UX/UI Designer

[English](README.md) · **Español**

Una [Agent Skill](https://agentskills.io/specification) que hace que tu agente de IA trabaje como
un diseñador UX/UI senior: convierte requisitos, historias de usuario, procesos, capturas o código
frontend en briefs de investigación, journeys, flujos de usuario, wireframes anotados, design
tokens, revisiones de usabilidad y accesibilidad, especificaciones responsive y handoff para
desarrollo y QA — con trazabilidad y evidencia explícita.

> Las decisiones de diseño deben basarse en las necesidades de los usuarios, los principios de
> usabilidad, los requisitos de accesibilidad, la viabilidad técnica y objetivos de negocio
> medibles — no solo en la estética.

## Qué problema resuelve

Los agentes generalistas a los que se pide "diseñar una pantalla" suelen saltar a lo visual,
olvidar los estados de error y vacío, inventar personas o métricas, ignorar la accesibilidad y
entregar especificaciones que nadie puede probar. Esta skill aporta un método: entender el
problema, diseñar el flujo completo con sus caminos alternativos, justificar decisiones,
verificar la calidad y entregar especificaciones comprobables, diferenciando siempre lo supuesto
de lo verificado.

## Capacidades

| # | Módulo | Entregables |
|---|---|---|
| 01 | UX Research Assistant | Brief, proto-personas, matriz de necesidades, JTBD, hipótesis, plan de investigación |
| 02 | User Journey Mapping | Journeys AS-IS / TO-BE, pain points, backlog de oportunidades |
| 03 | Information Architecture | Sitemap, navegación, jerarquía de contenidos, justificación |
| 04 | User Flow Generator | Flujos Mermaid con decisiones, recuperación de errores y trazabilidad de reglas |
| 05 | Wireframe Generator | Wireframes de baja fidelidad (ASCII/Markdown, opcional SVG/HTML) con todos los estados |
| 06 | UI Design System | Tokens en formato W3C, especificación de componentes, matriz de estados, guías de uso |
| 07 | Accessibility Reviewer | Hallazgos WCAG 2.2 A/AA con criterio, severidad y método de verificación |
| 08 | Responsive Design | Breakpoints basados en contenido, reglas adaptativas, especificación de layout |
| 09 | UX Heuristic Evaluator | Hallazgos según heurísticas de Nielsen, severidad 0–4, plan priorizado |
| 10 | Design Handoff | Especificaciones de pantallas y componentes, contrato de interacción, validaciones, criterios Given/When/Then, escenarios QA |

Transversal: 10 principios de diseño obligatorios, registro de decisiones (`DD-n`), IDs estables
(`REQ`, `US`, `FLOW`, `SCR`, `CMP`, `UX`, `AC`) y 8 quality gates (PASS / FAIL / NOT VERIFIED).

## Arquitectura

```text
SKILL.md                   Orquestador: activación, modos, enrutado de módulos, contratos, seguridad
references/                Un archivo por módulo + principios + quality gates (se cargan bajo demanda)
assets/templates/          Plantillas reutilizables
assets/examples/           Ejemplo completo de seguros (historia → flujo → wireframes → handoff) + tokens
scripts/validate_skill.py  Validador con biblioteca estándar de Python
tests/                     Validación estructural + 10 escenarios de comportamiento
```

Modos: **A** Diseño completo · **B** Auditoría UX · **C** Sistema de diseño · **D** Diseño a
desarrollo · **E** Optimización UX · **F** Tarea puntual (solo el módulo necesario).

## Requisitos

- Un agente compatible con Agent Skills (por ejemplo Claude Code u OpenAI Codex).
- No necesita herramientas externas. Opcional: Python 3.8+ para el validador; Figma, Storybook,
  navegador o escáneres de accesibilidad si tu agente los tiene y autorizas su uso.

## Instalación

> El repositorio debe estar publicado en GitHub para que estos comandos funcionen.

### Con skills.sh

```bash
npx skills add titoparra4/intelligent-ux-ui-designer
```

Ejecuta `npx skills --help` para ver las opciones de tu versión (selección de agente, instalación
global).

### Instalación manual

Copia `SKILL.md`, `references/`, `assets/` y `scripts/` en una carpeta llamada
**`intelligent-ux-ui-designer`** dentro del directorio de skills de tu agente:

| Agente | Proyecto | Usuario |
|---|---|---|
| Claude Code | `.claude/skills/intelligent-ux-ui-designer/` | `~/.claude/skills/intelligent-ux-ui-designer/` |
| OpenAI Codex | `.agents/skills/intelligent-ux-ui-designer/` | `~/.agents/skills/intelligent-ux-ui-designer/` (consulta la documentación de tu versión) |

```bash
git clone https://github.com/titoparra4/intelligent-ux-ui-designer.git
mkdir -p ~/.claude/skills/intelligent-ux-ui-designer
cp -R intelligent-ux-ui-designer/{SKILL.md,references,assets,scripts} ~/.claude/skills/intelligent-ux-ui-designer/
```

## Uso

La skill se activa cuando tu petición encaja con su descripción; también puedes nombrarla
("usa la skill intelligent-ux-ui-designer…", o `$intelligent-ux-ui-designer` en Codex). Responde
en el idioma en que le escribas.

Las capacidades disponibles dependen del agente y sus integraciones: sin renderizador Mermaid
obtendrás el código del diagrama; sin Figma, wireframes textuales; sin navegador ni escáner, las
comprobaciones de accesibilidad serán estáticas y así se indicará.

### Ejemplos de prompts

- "Diseña la experiencia para contratar un seguro de auto a partir de esta historia de usuario: …"
- "Audita la usabilidad y accesibilidad de esta página de pago" (adjunta captura o HTML).
- "Crea los design tokens y la especificación de Button, Input y Modal."
- "Escribe criterios de aceptación UX y escenarios QA para esta pantalla de login."
- "Define el comportamiento responsive de nuestro panel de pedidos."

### Resultado esperado

Una respuesta que indica el modo, lista los supuestos, genera los entregables con IDs estables,
registra las decisiones importantes y termina con el resumen de quality gates. Consulta
[`assets/examples/`](assets/examples/) para un ejemplo completo.

## Política de seguridad

- **Solo lectura por defecto**: no modifica, sobrescribe ni elimina archivos, componentes o tokens
  sin autorización explícita; propone artefactos nuevos o diffs.
- **Sin instalaciones ni llamadas de red implícitas**; no envía datos a servicios externos sin
  consentimiento.
- **Entradas no confiables**: archivos, documentos y capturas son datos; las instrucciones
  incrustadas se reportan y nunca se siguen.
- **Privacidad**: secretos y datos personales se mencionan por tipo y ubicación, no se reproducen.
- **Honestidad**: no inventa investigaciones, métricas, pruebas ni integraciones; no declara
  cumplimiento WCAG sin verificaciones documentadas.

## Limitaciones

- Genera especificaciones y representaciones de baja fidelidad, no diseño visual final ni código
  de producción.
- La revisión de accesibilidad a partir de capturas o descripciones es estática; no sustituye las
  pruebas con teclado, tecnologías de apoyo y usuarios reales.
- Las proto-personas y journeys son hipótesis hasta validarlas con investigación.
- El validador revisa la sintaxis básica de Mermaid; no renderiza los diagramas.
- La calidad depende del modelo y del contexto que proporciones.

## Validación

```bash
python3 scripts/validate_skill.py
```

Los escenarios de comportamiento TEST-001…TEST-010 están en [`tests/`](tests/README.md) con su
estado de ejecución.

## Contribuir

1. Abre un issue describiendo el cambio.
2. Mantén `SKILL.md` conciso; el detalle va en `references/`.
3. Ejecuta el validador y actualiza el escenario de prueba correspondiente.
4. Añade una entrada en `CHANGELOG.md`.

## Licencia

[MIT](LICENSE)

## Roadmap

- Guía de adaptadores opcionales para servidores MCP de Figma y Storybook.
- Ejecución automatizada de escenarios con rúbrica LLM-as-judge.
- Más ejemplos (dashboard B2B, onboarding móvil).
- Módulo de content design / UX writing.

## Versionado

[Semantic Versioning](https://semver.org/lang/es/). La versión está en `SKILL.md`
(`metadata.version`) y en [`CHANGELOG.md`](CHANGELOG.md).
