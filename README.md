# Próxima exploración

### Aprender juntos para cambiar cómo trabajamos.

![Tres personas exploran un mapa y entrenan juntas, rodeadas por un recorrido rosa que vuelve sobre sí mismo.](docs/assets/portada.png)

**Un recurso de _Cartografías de lo liminal_ · Raúl Marín · Shift+R**

Un marco sencillo para convertir las dificultades del día a día en pruebas compartidas, aprendizajes y decisiones. Incluye un mapa editable, una skill y un agente que ayuda a preparar y revisar cada exploración.

[Empezar](#empieza-con-una-dificultad-real) · [Instalación](docs/instalacion.md) · [Ejemplo completo](ejemplos/caso-completo.md) · [Guía del equipo](docs/guia-del-equipo.md) · [Fuentes y conectores](docs/fuentes-y-conectores.md)

## ¿Qué visión propone?

Aprender dentro del trabajo: con otras personas, sobre dificultades concretas y conectando lo aprendido con las decisiones.

Cuando cambia el territorio, el mapa necesita revisarse. Lo que aparece en una entrega, una conversación o una comunidad puede convertirse en una pregunta; esa pregunta, en una prueba pequeña; y lo observado, en una decisión sobre cómo trabajar.

**Como en el gimnasio, la constancia importa.** Elegimos algo asumible, lo practicamos y volvemos a revisarlo. La siguiente exploración parte de lo aprendido.

Este recurso es un punto de partida que cada equipo puede adaptar.

## Cuatro preguntas para empezar

| Pregunta | Qué deja por escrito |
| --- | --- |
| **¿Qué nos está costando?** | Una dificultad real y un ejemplo que la haga visible. |
| **¿Qué queremos averiguar?** | Una pregunta que podamos poner a prueba. |
| **¿Cómo podemos probarlo juntos?** | Una tarea pequeña, participantes, tiempo y qué observar. |
| **¿Qué nos hará cambiar de rumbo?** | Señales para seguir, ajustar o parar. |

Después de la prueba, el mismo mapa recoge evidencias, aprendizajes, decisiones y el próximo paso.

## Empieza con una dificultad real

1. Descarga el repositorio desde **Code → Download ZIP** y descomprímelo, o clónalo.
2. Abre la carpeta en **Cursor** y entra en un chat en modo **Agent**.
3. Copia este mensaje y completa los corchetes:

```text
Usa el agente acompanante-exploracion y la skill proxima-exploracion.

Nos está costando: [dificultad].
Un ejemplo real es: [situación y fuente].
Podemos dedicar: [tiempo].
Participan: [personas o funciones].

Prepara una prueba pequeña y guarda el borrador en mapas/mapa.md.
Deja pendientes los datos que todavía no tenemos.
```

Revisa la propuesta con el equipo antes de probarla. Si prefieres trabajar en un chat, sigue la [ruta sin instalación](docs/instalacion.md#usarlo-en-un-chat).

## Mira un caso ya completado

**Caso ilustrativo: detectar antes los estados que faltan en un formulario.**

| Momento | Qué ocurre en el ejemplo |
| --- | --- |
| Dificultad | Dos entregas tuvieron omisiones detectadas tarde. |
| Prueba | Diseño y desarrollo revisan juntos un formulario antes de implementar. |
| Evidencias | Detectan un error de conexión ausente, emplean 27 minutos y aparece otra duda sobre el foco. |
| Revisión | La prueba aporta una señal útil, pero supera el límite de tiempo y deja una cuestión abierta. |
| Decisión del caso | Ajustar el formato y repetir en otro formulario. |
| Siguiente paso | Preparar la versión de referencia y revisar también el comportamiento del foco. |

[**Leer el caso completo, con sus evidencias y el mapa revisado →**](ejemplos/caso-completo.md)

Todos los datos de ese caso son ficticios. Sirve para enseñar el proceso; no es un caso de éxito real ni una medición del rendimiento de un equipo.

## Qué aporta cada pieza

| Pieza | Función |
| --- | --- |
| **Equipo** | Aporta experiencias, interpreta lo observado y decide. |
| **Persona que acompaña** | Facilita la conversación y sostiene la continuidad. |
| **Skill** | Organiza el método y mantiene las cuatro preguntas. |
| **Agente** | Reúne el contexto disponible y prepara una propuesta de mapa o revisión. |
| **Mapa** | Conserva evidencias, decisiones e historial entre sesiones. |

En la charla proponemos explorar el perfil **Forward-Deployed Learning Designer** para acompañar este trabajo desde dentro de la organización. El agente es una herramienta a su servicio.

## Contenido del repositorio

| Recurso | Enlace |
| --- | --- |
| Instrucciones del agente para Cursor | [acompanante-exploracion.md](.cursor/agents/acompanante-exploracion.md) |
| Skill del método | [SKILL.md](.cursor/skills/proxima-exploracion/SKILL.md) |
| Plantilla reutilizable | [plantilla-mapa.md](.cursor/skills/proxima-exploracion/assets/plantilla-mapa.md) |
| Primer mapa editable | [mapas/mapa.md](mapas/mapa.md) |
| Ejemplo completo y revisado | [caso-completo.md](ejemplos/caso-completo.md) |
| Material de entrada para una demo | [exploracion-demo.md](ejemplos/exploracion-demo.md) |
| Instalación y primeros mensajes | [instalacion.md](docs/instalacion.md) |
| Cómo sostener la práctica | [guia-del-equipo.md](docs/guia-del-equipo.md) |
| Uso de fuentes y conectores | [fuentes-y-conectores.md](docs/fuentes-y-conectores.md) |
| Orientación para el asistente del proyecto | [AGENTS.md](AGENTS.md) |

## Alcance de esta primera versión

Funciona a petición del equipo. No instala conectores, programa reuniones ni vigila canales. Se pueden aportar notas manualmente o usar fuentes delimitadas si el entorno ya dispone de acceso.

El agente de Cursor trabaja en modo de solo lectura: devuelve su propuesta al asistente principal, que puede guardarla cuando se lo pidas. La memoria del proceso vive en el mapa y su historial.

Validación realizada: estructura de archivos, metadatos YAML, referencias locales y coherencia del ejemplo. Queda pendiente comprobarlo en cada instalación de Cursor y con los conectores de cada equipo.

## Autoría

**Raúl Marín · Shift+R**  
Recurso preparado para **Cartografías de lo liminal**.  
Portada creada con IA para este recurso. Versión 1.1 · octubre de 2026.
