# Instalación y primeros pasos · 2.0

[← Inicio](../README.md) · [Compatibilidad](compatibilidad.md) · [Cambios](../CHANGELOG.md)

## 1. Cualquier chat: sin instalación

1. Abre [INICIO-RAPIDO.md](../INICIO-RAPIDO.md) y copia **todo su contenido** en un mensaje. En GitHub, la vista Raw facilita copiar el texto.
2. Completa «Mi contexto» al final. Para revisar una exploración, añade también el último mapa y las nuevas evidencias.
3. Envía el mensaje a Gemini, Claude, ChatGPT o a otro asistente que acepte instrucciones de texto.
4. Conserva el mapa que devuelva y valídalo con el equipo.

También puedes adjuntar el archivo si el cliente lee `.md`. Si no permite adjuntos, usa copiar y pegar. No basta con pegar una URL si el asistente no puede abrirla. Esta ruta no requiere comandos, archivos locales, plugins ni APIs.

Si el texto supera el límite de entrada del cliente, utiliza un entorno con más capacidad de contexto. No recortes el historial o las decisiones sin conservar una copia original.

## 2. Trabajar dentro de este repositorio

Descarga **Code → Download ZIP** y descomprime el recurso, o clona el repositorio. Abre su carpeta raíz en tu cliente con acceso a archivos.

| Cliente | Entrada del proyecto | Petición inicial |
| --- | --- | --- |
| Codex | `AGENTS.md` | «Lee AGENTS.md y prepara una exploración con este contexto: […]». |
| Claude Code | `CLAUDE.md` | «Lee CLAUDE.md y prepara una exploración con este contexto: […]». |
| Gemini CLI | `GEMINI.md` | «Lee GEMINI.md y prepara una exploración con este contexto: […]». |
| Cursor | `.cursor/agents/acompanante-exploracion.md` | «Usa el agente acompanante-exploracion con este contexto: […]». |
| Otro cliente con lectura de archivos | `INICIO-RAPIDO.md` | «Lee INICIO-RAPIDO.md y aplica el método a este contexto: […]». |

Las entradas remiten al mismo agente y a la misma skill. **En esta ruta no hace falta registrar una skill nativa.** Si el cliente no carga las instrucciones automáticamente, pide la lectura explícita. Si tampoco puede leer archivos, usa la ruta 1.

## 3. Instalar la skill nativa (opcional)

Copia la carpeta completa [skills/proxima-exploracion](../skills/proxima-exploracion), incluidos `SKILL.md` y `assets/`, a **una** ubicación de proyecto:

| Cliente | Carpeta de destino dentro del proyecto |
| --- | --- |
| Codex | `.agents/skills/proxima-exploracion/` |
| Gemini CLI | `.agents/skills/proxima-exploracion/` (compartida con Codex) |
| Claude Code | `.claude/skills/proxima-exploracion/` |
| Cursor | `.agents/skills/proxima-exploracion/` (también admite `.cursor/skills/`) |

No copies solo `SKILL.md`: incluye la plantilla. Puedes hacerlo con el explorador de archivos, mostrando carpetas ocultas. Conserva cualquier configuración o skill que ya exista. Si hay otra versión con el mismo nombre, compara y respáldala antes de sustituirla.

**Si usas varios clientes en el mismo proyecto:** Codex, Gemini CLI y Cursor pueden compartir la copia de `.agents/skills/`. Claude Code usa su copia de `.claude/skills/`. Cursor también descubre esa carpeta; si muestra dos entradas, utiliza la lectura explícita del método en vez de instalar copias adicionales. El repositorio distribuye una única fuente en `skills/` para evitar duplicados por defecto.

Abre una sesión nueva si la skill no aparece. Pide en lenguaje natural: «Usa la skill proxima-exploracion para preparar una prueba». Para confirmar, pide que muestre sus cuatro preguntas y la ruta de su plantilla antes de trabajar. No presupongas que los comandos con `/` o `$` son iguales en todos los clientes.

Esta instalación añade el método. El **rol de agente** está en [agents/acompanante-exploracion.md](../agents/acompanante-exploracion.md): puedes aportar su contenido como contexto. No se instala automáticamente como subagente de todos los productos.

## 4. Añadir el acompañante a otro proyecto

Para usar las entradas de proyecto, copia `agents/` y `skills/` con sus rutas originales. Añade solo el bloque que necesites de `AGENTS.md`, `CLAUDE.md` o `GEMINI.md` a la configuración existente; no la reemplaces entera. Copia `mapas/mapa.md` con un nombre libre o utiliza tu mapa anterior.

En Cursor puedes copiar además `.cursor/agents/acompanante-exploracion.md` a la misma ruta. Ese adaptador necesita los archivos de `agents/` y `skills/`. Devuelve una propuesta de solo lectura: el asistente principal guarda cuando se lo pidas.

## Tres mensajes útiles

### Preparar

```text
Aplica Próxima exploración al contexto que te doy.
Nos cuesta [dificultad]. Tenemos este ejemplo [evidencia y fuente].
Participan [funciones] y podemos dedicar [tiempo].
Devuelve un mapa completo aquí y deja pendientes los datos que faltan.
```

### Revisar

```text
Retoma el mapa que adjunto. Las nuevas evidencias son […].
Compara con la pregunta y los criterios originales.
Propón seguir, ajustar o parar y conserva el historial.
La decisión del equipo sigue pendiente. Devuelve el mapa completo.
```

### Registrar la decisión y guardar

```text
El equipo ha decidido [decisión] por [motivo].
El siguiente paso acordado es [acción, responsable y revisión].
Actualiza el mapa conservando las evidencias y los criterios anteriores.
Guárdalo en [ruta] si puedes escribir y comprobar el archivo.
Si no puedes, entrega el texto completo para copiarlo.
```

## Migrar desde la versión 1.x

1. Guarda una copia del mapa de tu equipo; **no lo sustituyas por la plantilla vacía**. El formato de las cuatro preguntas sigue siendo válido.
2. Conserva los cambios propios que hayas hecho en el agente o la skill antes de actualizar.
3. La fuente del método pasa de `.cursor/skills/proxima-exploracion/` a `skills/proxima-exploracion/`. El agente común está ahora en `agents/`.
4. Actualiza el adaptador `.cursor/agents/acompanante-exploracion.md` y sus dependencias. Si tu actualización ha dejado la skill antigua de `.cursor/skills/`, retírala después de respaldarla o reemplázala con la v2 si prefieres la instalación nativa. No mantengas una copia v1 activa junto a la v2.
5. Combina las instrucciones nuevas con la configuración de tu proyecto. Para trabajar en un chat basta con sustituir las instrucciones por `INICIO-RAPIDO.md` y aportar el mapa conservado.

## Si algo no funciona

| Situación | Qué hacer |
| --- | --- |
| No reconoce la skill | Comprueba la ruta y que se copió también `assets/`; reinicia la sesión o usa lectura explícita. |
| No puede abrir un enlace o adjunto | Pega el contenido del prompt y del mapa en el chat. |
| No reconoce AGENTS.md, CLAUDE.md o GEMINI.md | Pide que lo lea explícitamente; sin lectura de archivos, usa el prompt. |
| Dice que ha guardado pero no encuentras el archivo | Pide que verifique la ruta; si no tiene escritura, conserva el texto manualmente. |
| No recuerda otra sesión | Aporta el último mapa y su historial. |
| Mezcla la demo con tu equipo | Recuerda que `ejemplos/` es ficticio y aporta tus fuentes. |
| No accede a Jira, Slack u otra fuente | Pega las notas disponibles o configura el acceso en tu cliente; el recurso no instala conectores. |

Para desinstalar la skill nativa, elimina solo la carpeta de esta skill que copiaste y el bloque de instrucciones que añadiste. Conserva tus mapas. El modo chat no instala nada que desinstalar.
