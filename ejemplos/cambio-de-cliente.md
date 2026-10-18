# Continuar una exploración en otro cliente

[← Inicio](../README.md) · [Caso completo](caso-completo.md)

**Ejemplo ficticio de uso.** Ilustra el relevo entre conversaciones; no es una transcripción de pruebas ejecutadas en Gemini, Claude o Codex.

## 1. Preparar en el primer chat

Pega `INICIO-RAPIDO.md` y el contexto de [exploracion-demo.md](exploracion-demo.md). El equipo revisa la propuesta y guarda su mapa. En el caso de demostración, se acuerda una revisión conjunta de estados del formulario, con un máximo de 20 minutos y sin relajar calidad ni accesibilidad.

## 2. Conservar el registro

Después de la prueba se añaden cuatro observaciones ficticias:

- E1: la revisión duró 27 minutos.
- E2: se detectó antes de implementar un estado de error de conexión que faltaba.
- E3: una duda sobre restaurar el foco apareció durante la implementación.
- E4: se perdió tiempo buscando la versión correcta del diseño.

No se midió ahorro total de tiempo. El equipo todavía no ha decidido qué hacer. Conserva el mapa completo con sus criterios originales y añade estas evidencias con sus fuentes cuando existan.

## 3. Retomar en otro cliente

Abre, por ejemplo, Claude, Gemini o Codex. Aporta **las instrucciones de `INICIO-RAPIDO.md` y el mapa completo conservado**. No presupongas que el cliente puede leer el chat anterior.

```text
Retoma esta exploración que empezamos en otro asistente.
Adjunto las instrucciones, el mapa con sus criterios originales y E1–E4.
La decisión del equipo sigue pendiente.
Compara las evidencias con lo acordado y propón el siguiente paso.
No cambies el límite original para que el resultado parezca satisfactorio.
Devuelve el mapa completo con su historial para poder continuar después.
```

La revisión debería reconocer que hubo una detección temprana, que se superaron los 20 minutos y que quedó una cuestión de foco abierta. Puede recomendar ajustar. La decisión del equipo debe continuar pendiente y no debe atribuir un ahorro que no se midió.

## 4. Registrar la decisión humana

En la siguiente conversación del ejemplo, el equipo comunica:

```text
Hemos decidido ajustar y repetir. Prepararemos la versión de referencia
antes y revisaremos también el comportamiento del foco.
Mantenemos el límite de 20 minutos. Registra la preparación por separado.
Todavía no hemos realizado la segunda prueba.
```

El mapa incorpora esa decisión, conserva los criterios y evidencias anteriores y deja pendientes los resultados de la segunda prueba. La fecha y la persona que acompaña siguen pendientes si el equipo no las ha acordado.

## Qué llevar al cambiar de asistente

El prompt y el mapa completo suelen bastar. Incluye la pregunta actual, los criterios originales y sus cambios, las evidencias y sus fuentes, las decisiones confirmadas, los pendientes y el próximo paso. Si el nuevo cliente no admite adjuntos, pega su contenido. Si tienes dos versiones contradictorias, resuelve cuál es la vigente con el equipo antes de fusionarlas.
