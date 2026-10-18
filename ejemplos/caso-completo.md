# Caso completo · Revisar estados antes de implementar

[← Volver al inicio](../README.md) · [Material de entrada de la demo](exploracion-demo.md)

> **Ejemplo ficticio, completamente desarrollado.** Personas, observaciones, tiempos y acuerdos se han creado para mostrar el método. No documenta una experiencia real de Shift+R ni demuestra eficacia del recurso.

## El contexto de partida

Un equipo de producto observa que algunas entregas de formularios vuelven a diseño porque falta definir un estado. Diseño y desarrollo quieren entender si una revisión conjunta previa ayuda.

La persona que acompaña recoge dos notas y una idea compartida en una comunidad:

| Referencia ficticia | Observación o aportación |
| --- | --- |
| Nota A | En una entrega se detectó tarde que faltaba definir un estado de error. |
| Nota B | Otra entrega volvió a diseño por una omisión similar. |
| Idea C | En una conversación de comunidad, alguien propuso recorrer los estados antes de implementar. |

Las notas aportan ejemplos. La idea de la comunidad aporta una posible prueba. Todavía no se conoce la frecuencia del problema ni su causa.

## 1. El mapa inicial

**Equipo:** diseño y desarrollo del producto ficticio.  
**Estado:** prueba acordada dentro de esta simulación.  
**Acompaña:** una persona del equipo, pendiente de designar.  
**Revisión:** al terminar la implementación del formulario elegido.

### ¿Qué nos está costando?

Dos entregas requirieron volver a diseño tras detectar omisiones de estados. Referencias: notas A y B.

No sabemos si el origen es la documentación, el momento de la conversación o alguna otra condición.

### ¿Qué queremos averiguar?

**¿Revisar juntos los estados antes de implementar permite detectar omisiones antes de la entrega?**

- Hechos del caso: las notas A y B mencionan omisiones tardías.
- Hipótesis: una revisión conjunta previa puede adelantar la detección.
- Pendiente: comprobar qué ocurre en otros formularios y si el esfuerzo es sostenible.

### ¿Cómo podemos probarlo juntos?

Una persona de diseño y otra de desarrollo revisarán un formulario de su trabajo.

1. Abrir la versión que se va a implementar.
2. Recorrer los estados vacío, carga, éxito y error.
3. Revisar también foco y navegación con teclado.
4. Anotar omisiones, dudas y tiempo empleado.
5. Comprobar después de implementar si aparecieron omisiones nuevas.

**Límite:** 20 minutos, asumidos como acordados en este caso ficticio.  
**Comparación:** notas A y B, reconociendo que la complejidad de los formularios puede ser distinta.  
**Calidad:** mantener los criterios de accesibilidad y calidad del producto.

### ¿Qué nos hará cambiar de rumbo?

| Decisión posible | Señal acordada en la simulación |
| --- | --- |
| Seguir | Detectar una omisión antes de implementar y resolverla dentro del límite de tiempo. |
| Ajustar | Detectar omisiones, pero exceder el tiempo o dejar sin resolver quién decide. |
| Parar esta forma de prueba | Interferir con una entrega crítica o no poder mantener los criterios de calidad. |

## 2. Lo que ocurrió en la prueba

Estas evidencias proceden del material ficticio de la demo:

| ID | Evidencia | Qué permite afirmar |
| --- | --- | --- |
| E1 | La revisión duró 27 minutos. | Superó el límite acordado en 7 minutos. |
| E2 | Se detectó antes de implementar que faltaba el mensaje de error de conexión. | La revisión hizo visible una omisión de forma temprana. |
| E3 | Durante la implementación apareció una duda sobre dónde devolver el foco tras cerrar el aviso. | Quedó una cuestión de interacción que la revisión inicial no resolvió. |
| E4 | El equipo anotó que perdió tiempo buscando la versión correcta del diseño. | Existe una fricción concreta que podría reducirse en la próxima prueba. |

No se dispone del tiempo total de implementación ni de retrabajo posterior. Tampoco se ha medido la calidad final del formulario. No podemos afirmar que se ahorró tiempo o que el problema quedó resuelto.

## 3. La revisión propuesta por el agente

**Recomendación: ajustar y repetir una prueba pequeña.**

Hay una señal favorable para la pregunta inicial: se detectó una omisión antes de implementar. Sin embargo, no se cumple la condición completa de seguir: se superaron los 20 minutos y falta evidencia de que la omisión quedara resuelta dentro de ese tiempo.

Se cumple la señal de ajustar por exceso de tiempo. No hay evidencia aportada de interferencia con una entrega crítica o incumplimiento de calidad; eso no demuestra por sí solo que no ocurrieran.

**Qué se aprende:**

- La conversación previa puede hacer visible una omisión en este caso.
- Preparar la versión de referencia merece una prueba.
- La revisión del foco necesita concretarse para que una duda no quede oculta detrás de «hemos revisado accesibilidad».

**Qué sigue abierto:**

- Si la siguiente revisión cabe en el tiempo disponible.
- Si las dudas detectadas se resuelven a tiempo.
- Si el comportamiento final cumple los criterios de calidad.
- Si el formato ayuda también en otro formulario.

## 4. La decisión del equipo en este ejemplo

Para completar la demostración, añadimos este acuerdo **simulado**:

> Ajustamos la preparación y repetimos en un segundo formulario. Enlazaremos la versión de referencia antes de la sesión y anotaremos explícitamente dónde debe ir el foco en cada transición que lo requiera. Mantendremos el límite de 20 minutos.

Esta decisión se añade como un acuerdo del caso ficticio. No estaba contenida en las evidencias E1–E4 y no se atribuye a un equipo real.

## 5. El mapa de la siguiente exploración

**Estado:** propuesta posterior al acuerdo simulado.  
**Acompaña:** pendiente de designar.  
**Revisión:** después de implementar el segundo formulario; fecha pendiente.

### ¿Qué nos está costando?

La primera revisión detectó una omisión, pero duró 27 minutos y dejó una duda posterior sobre el foco. Parte del tiempo se empleó en encontrar la versión correcta. Fuentes: E1–E4.

### ¿Qué queremos averiguar?

**¿Preparar la versión de referencia y concretar las transiciones de foco permite hacer una revisión útil dentro de los 20 minutos acordados?**

Hipótesis: reducir la búsqueda y precisar qué observar hará más viable la revisión. Pendiente: tiempo de preparación y resultado en un segundo caso.

### ¿Cómo podemos probarlo juntos?

1. Antes de la sesión, enlazar la versión de referencia y registrar cuánto cuesta prepararla.
2. Recorrer los estados del segundo formulario.
3. Anotar el comportamiento esperado del foco y cómo se comprobará con teclado.
4. Registrar dudas, momento de detección, resolución y tiempo.
5. Tras implementar, comprobar si aparecieron nuevas omisiones.

Mantener los criterios de calidad del producto. Contabilizar la preparación por separado para no esconder trabajo fuera de la reunión.

### ¿Qué nos hará cambiar de rumbo?

Los siguientes criterios son **propuestas pendientes de validación**, salvo el límite de sesión de 20 minutos ya recogido en el acuerdo simulado:

- **Seguir:** revisión útil dentro del límite, con dudas resueltas a tiempo y un coste de preparación que el equipo considere asumible.
- **Ajustar:** exceso de tiempo, preparación difícil de sostener o dudas relevantes pendientes.
- **Parar este formato:** interferencia con una entrega crítica o imposibilidad de mantener los criterios de calidad.

### Después de la segunda prueba

- Evidencias: pendientes.
- Aprendizajes: pendientes.
- Decisión del equipo: pendiente.
- Próximo paso: realizar la prueba cuando el equipo valide la propuesta.

## 6. Historial que se conserva

| Momento | Registro |
| --- | --- |
| Inicio | Pregunta original, límite de 20 minutos y señales para seguir, ajustar o parar. |
| Primera prueba | Evidencias E1–E4. |
| Revisión | Recomendación de ajustar; límites de lo que permiten concluir los datos. |
| Acuerdo simulado | Repetir con versión preparada y revisión explícita del foco. |
| Siguiente exploración | Nueva pregunta y criterios propuestos, sin resultados todavía. |

Los criterios iniciales no se borran ni se modifican para hacer que la primera prueba encaje.

## 7. Llevar el aprendizaje a una decisión de trabajo

Resumen que el equipo podría compartir con quien coordina las entregas:

> Probamos una revisión conjunta de estados antes de implementar. Detectamos una omisión de error de conexión, pero tardamos 27 minutos frente a los 20 acordados y apareció otra duda sobre el foco. Queremos repetir con la versión preparada y una revisión más concreta de las transiciones. Necesitamos identificar esa versión antes de la sesión y reservar un hueco compartido. Todavía no podemos afirmar que se ahorre tiempo total.

Es un borrador de comunicación. El recurso no lo envía automáticamente.

## Probar la demo

Para reproducir la revisión con el agente, aporta únicamente [el material de entrada](exploracion-demo.md) y pide:

```text
Usa el acompañante de exploración para revisar el mapa
con las nuevas evidencias del final. Conserva la pregunta
y los criterios originales en el historial.
Propón el siguiente paso y deja pendiente la decisión del equipo.
Todo el caso es ficticio.
```

El resultado puede variar en la redacción. Debería separar observaciones, interpretación, recomendación y decisión, y reconocer que la primera prueba superó el límite de tiempo.
