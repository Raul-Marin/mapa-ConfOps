# Instalación y primeros pasos

[← Volver al inicio](../README.md)

Elige una de estas dos rutas: abrir el paquete en Cursor o aportar las instrucciones en un chat.

## Cursor: carpeta independiente

1. Descarga el repositorio desde **Code → Download ZIP**.
2. Descomprime el archivo y abre su carpeta principal en Cursor.
3. Comprueba que contiene `.cursor/agents/acompanante-exploracion.md` y `.cursor/skills/proxima-exploracion/SKILL.md`.
4. Abre un chat en modo Agent y pide que use el acompañante de exploración.

No requiere Node, Python, un servidor ni una base de datos. Necesitas acceso al asistente de tu entorno; su uso puede consumir los créditos o cuota de tu plan.

La carpeta `.cursor` puede estar oculta en el explorador de archivos de tu sistema. El ZIP la incluye.

### Comprobar que se ha cargado

```text
Lee la configuración de este proyecto. Identifica el agente
acompanante-exploracion y la skill proxima-exploracion.
Dime sus cuatro preguntas y qué archivo usarás como mapa.
Todavía no modifiques nada.
```

Debería identificar las cuatro preguntas del README y `mapas/mapa.md`. Si no reconoce la configuración, adjunta los archivos directamente y usa la ruta manual de abajo.

## Cursor: añadirlo a otro proyecto

Copia desde este recurso:

| Origen | Destino en tu proyecto |
| --- | --- |
| `.cursor/agents/acompanante-exploracion.md` | La misma ruta. |
| `.cursor/skills/proxima-exploracion/` | La misma carpeta completa, incluidos sus assets. |
| `mapas/mapa.md` | Una ruta disponible para el mapa del equipo. |

Combina las carpetas; no reemplaces otros agentes o skills que ya tengas. Si existe un mapa con el mismo nombre, usa uno nuevo. Si ya tienes un `AGENTS.md`, incorpora solo las instrucciones de este recurso que necesites.

El agente busca la skill desde la raíz del proyecto. Mantén esas rutas o actualiza sus referencias si reorganizas la carpeta.

## Usarlo en un chat

Adjunta o pega el contenido de:

1. [Instrucciones del acompañante](../.cursor/agents/acompanante-exploracion.md).
2. [Skill](../.cursor/skills/proxima-exploracion/SKILL.md).
3. [Plantilla](../.cursor/skills/proxima-exploracion/assets/plantilla-mapa.md).
4. El mapa anterior, si ya hubo una exploración.

Envía:

```text
Sigue las instrucciones adjuntas como acompañante de exploración.
Aplica la skill al contexto que te doy y devuelve un mapa breve aquí.
No necesitas herramientas ni guardar archivos.

Nuestra dificultad es: […]
Un ejemplo concreto: […]
Tiempo y personas disponibles: […]
```

Este uso aporta instrucciones al asistente; no instala un agente nativo. Copia el resultado al archivo donde conservéis el mapa. Para continuar en otra sesión, aporta la última versión.

## Tres mensajes útiles

### Preparar

```text
Usa el acompañante de exploración. Nos cuesta [dificultad].
Tenemos este ejemplo [evidencia] y podemos dedicar [tiempo].
Prepara una prueba y guarda el borrador en mapas/mapa.md.
```

### Revisar

```text
Usa el acompañante de exploración. Lee mapas/mapa.md.
Estas son las nuevas evidencias: […].
Compara con la pregunta y los criterios originales.
Propón seguir, ajustar o parar y conserva el historial.
La decisión del equipo sigue pendiente. Guarda la propuesta.
```

### Registrar una decisión del equipo

```text
El equipo ha decidido [decisión] por [motivo].
Actualiza mapas/mapa.md, conserva las evidencias y los criterios anteriores,
y registra como siguiente paso [acción, responsable y revisión acordados].
```

## Si algo no funciona

| Situación | Qué comprobar |
| --- | --- |
| No aparece la skill | Que la carpeta completa esté bajo `.cursor/skills/proxima-exploracion/`. |
| No aparece el agente | Que el archivo esté bajo `.cursor/agents/`. Si hace falta, abre una nueva sesión. |
| El agente no guarda | Está configurado como solo lectura. Pide al asistente principal que guarde el resultado. |
| No recuerda la prueba anterior | Adjunta o indica el mapa actualizado; no depende de una memoria automática. |
| No accede a Jira o Slack | El paquete no instala conectores. Aporta las notas o configura el acceso en tu herramienta. |
| Mezcla el ejemplo con tu equipo | Indica que `ejemplos/` contiene datos ficticios y aporta tus propias fuentes. |

## Referencias de compatibilidad

Estructura contrastada con la documentación oficial de Cursor el 18 de octubre de 2026. El funcionamiento concreto depende de la versión, el plan y la configuración del entorno.

- [Skills de Cursor](https://cursor.com/help/customization/skills).
- [Subagentes de Cursor](https://cursor.com/docs/subagents).
