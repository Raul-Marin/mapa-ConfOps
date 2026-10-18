# Validación de la versión 2.0

[← Inicio](../README.md) · [Compatibilidad](compatibilidad.md)

Fecha: **18 de octubre de 2026**. Se distinguen la comprobación del paquete, la evaluación de sus instrucciones y la ejecución en aplicaciones concretas.

## Comprobaciones del paquete

- Metadatos `name` y `description` de la skill: válidos con el validador de creación de skills.
- Prompt portable: generado desde agente, skill y plantilla; comprobado mediante `python scripts/generar_prompt.py --check`.
- Entradas `AGENTS.md`, `CLAUDE.md` y `GEMINI.md`: mismo contenido y referencias al núcleo común.
- Enlaces locales de Markdown y archivos requeridos: comprobados.
- Portada y mapas de ejemplo anteriores: conservados.

## Evaluación de las instrucciones

Se utilizaron conversaciones independientes de agentes en el entorno de desarrollo, sin el historial de elaboración del recurso. Recibieron los archivos y una tarea concreta. Estas evaluaciones no equivalen a pruebas en las aplicaciones de los proveedores.

| Caso ejecutado | Entrada | Comportamiento observado |
| --- | --- | --- |
| Preparar con información incompleta | Prompt portable; dos formularios con problemas relatados por el usuario; disponibilidad de 20 minutos | Entregó las cuatro preguntas, distinguió el relato de notas no leídas, propuso una prueba pequeña y dejó persona acompañante, revisión y decisión pendientes. Marcó los criterios nuevos como propuestas. |
| Revisar desde otra conversación | Skill y ejemplo ficticio con E1–E4; decisión del equipo pendiente | Conservó el límite original de 20 minutos, contrastó los 27 minutos observados y distinguió recomendación de decisión. No afirmó ahorro total ni resultados de una segunda prueba. |

## Comprobación en tu cliente

La instalación nativa en Codex, Claude Code, Gemini CLI y Cursor se ha contrastado documentalmente, pero **no se ha ejecutado una sesión real de cada aplicación para esta entrega**. Tampoco se ha probado cada modelo ni cada plan de chat.

Después de instalar o adjuntar el recurso, pide:

```text
Identifica las cuatro preguntas de Próxima exploración.
¿Qué información tienes realmente y cuál falta?
¿Puedes leer y guardar archivos en esta sesión?
No guardes nada todavía.
```

Para comprobar el proceso, utiliza [exploracion-demo.md](../ejemplos/exploracion-demo.md) como material ficticio y compáralo con el [caso completo](../ejemplos/caso-completo.md). Comprueba que mantenga el límite de tiempo, que no invente resultados y que deje pendiente la decisión si tú no la has aportado.

Casos adicionales recomendados al cambiar de modelo: prueba no realizada, dos mapas con decisiones contradictorias y fuente externa inaccesible. El resultado debe señalar la ausencia de evidencia, pedir resolver el conflicto o trabajar con el material disponible, respectivamente. Estos casos adicionales no se han ejecutado como evaluaciones independientes en esta entrega.

Si el cliente falla al descubrir archivos o skills, utiliza el prompt completo por texto. Si la respuesta pierde criterios o inventa decisiones, conserva el mapa original y corrige la revisión con el equipo antes de usarla.
