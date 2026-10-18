# Historial de versiones

## 2.0.0 · 18 de octubre de 2026

- Prompt completo `INICIO-RAPIDO.md` para utilizar el recurso mediante texto en distintos clientes.
- Skill canónica trasladada de `.cursor/skills/` a `skills/`, sin campos de proveedor.
- Rol de agente portable en `agents/`; adaptador de Cursor separado y de solo lectura.
- Entradas `AGENTS.md`, `CLAUDE.md` y `GEMINI.md` que dirigen al mismo método.
- Instalación nativa opcional por cliente, límites de compatibilidad y migración desde 1.x.
- Continuidad explícita entre sesiones, tratamiento de conflictos de mapas y entrega en chat cuando no hay escritura.
- Ejemplo ficticio de cambio de cliente, validación y generador del prompt para evitar divergencias.
- Se conservan la portada, las cuatro preguntas, la guía del equipo y los ejemplos anteriores.

**Cambio de rutas:** las instalaciones que leían `.cursor/skills/proxima-exploracion/` deben seguir la [migración](docs/instalacion.md#migrar-desde-la-versión-1x). Los mapas 1.x siguen siendo válidos.

## 1.1 · 18 de octubre de 2026

Paquete inicial centrado en Cursor, con skill, agente de solo lectura, documentación, portada y ejemplo completo ficticio.
