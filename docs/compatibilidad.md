# Compatibilidad y fuentes

[← Inicio](../README.md) · [Instalación](instalacion.md)

## Qué significa «compatible»

El núcleo es texto Markdown en español. Un asistente que acepte ese texto completo y siga instrucciones puede usar el método en una conversación. Es una vía portable de interacción, no una garantía de respuestas idénticas ni de instalación nativa en todas las aplicaciones.

| Entorno | Vía común | Integración que ofrece este paquete |
| --- | --- | --- |
| Gemini en chat | Pegar `INICIO-RAPIDO.md` y el contexto | No depende de Gems ni de Gemini CLI. |
| Claude en chat | Pegar el mismo archivo y el contexto | No requiere Claude Code ni carga de skills en la cuenta. |
| ChatGPT en chat | Pegar el mismo archivo y el contexto | No requiere GPT personalizado ni función de Skills. |
| Codex con archivos | Lectura explícita del método | `AGENTS.md`; skill opcional en `.agents/skills/`. |
| Claude Code | Lectura explícita del método | `CLAUDE.md`; skill opcional en `.claude/skills/`. |
| Gemini CLI | Lectura explícita del método | `GEMINI.md`; skill opcional en `.agents/skills/`. |
| Cursor | Lectura explícita del método | Subagente de solo lectura; skill opcional en `.agents/skills/`. |
| Otros asistentes y modelos locales | Pegar el texto si cabe en su contexto | Sin configuración nativa específica ni ejecución verificada. |

Gemini y Gemini CLI son entornos distintos; lo mismo ocurre con Claude y Claude Code. La compatibilidad con un modelo no implica que todas las aplicaciones que lo usan admitan los mismos archivos.

## Capacidades y alternativa

| Capacidad del cliente | Uso | Si no está disponible |
| --- | --- | --- |
| Instrucciones de texto | Aplicar el método | Requisito mínimo. |
| Lectura de `.md` | Adjuntar prompt y mapa | Copiar y pegar el texto. |
| Lectura del proyecto | Cargar agente, skill y mapa | Usar `INICIO-RAPIDO.md`. |
| Escritura | Guardar el mapa cuando se solicita | Copiar la respuesta manualmente. |
| Skills nativas | Descubrir el método según la tarea | Pedir su lectura explícita. |
| Subagentes | Delegar la preparación en Cursor | El asistente principal asume el rol. |
| Conectores | Leer las fuentes autorizadas | Aportar extractos con su procedencia. |
| Memoria entre sesiones | No necesaria | Aportar siempre el último mapa. |

No se requieren llamadas de API, dependencias de proveedor, MCP, ejecución de scripts ni seguimiento automático para aplicar el método. Los límites de contexto, planes, permisos y políticas del cliente siguen aplicando.

## Fuentes oficiales consultadas

Revisión documental: **18 de octubre de 2026**. Las rutas pueden cambiar; esta tabla no certifica versiones instaladas.

- [OpenAI: skills](https://learn.chatgpt.com/docs/build-skills): formato `SKILL.md` y descubrimiento local en `.agents/skills/`.
- [OpenAI: AGENTS.md](https://learn.chatgpt.com/docs/agent-configuration/agents-md): instrucciones de proyecto.
- [Anthropic: skills de Claude Code](https://code.claude.com/docs/en/skills): instalación de proyecto en `.claude/skills/`.
- [Anthropic: memoria de Claude Code](https://code.claude.com/docs/en/memory): contexto de proyecto mediante `CLAUDE.md`.
- [Google: Agent Skills de Gemini CLI](https://geminicli.com/docs/cli/skills/): `.gemini/skills/` y alias `.agents/skills/`.
- [Google: GEMINI.md](https://geminicli.com/docs/cli/gemini-md/): instrucciones contextuales del proyecto.
- [Cursor: skills](https://cursor.com/help/customization/skills): ubicaciones de descubrimiento, incluida `.agents/skills/`.
- [Cursor: subagentes](https://cursor.com/docs/subagents): configuración del adaptador de Cursor.

La vía de copiar y pegar es una decisión de diseño de este recurso; no representa una certificación de los proveedores. Consulta el alcance de las comprobaciones en [validacion.md](validacion.md).
