# Mantener el recurso

[← Inicio](../README.md)

## Fuentes de verdad

- `skills/proxima-exploracion/SKILL.md`: método, revisión y límites de actuación.
- `skills/proxima-exploracion/assets/plantilla-mapa.md`: formato del mapa.
- `agents/acompanante-exploracion.md`: rol de acompañamiento.
- `VERSION`: versión del paquete.

`INICIO-RAPIDO.md` reúne esos contenidos para que un chat no necesite resolver dependencias. Es un archivo generado; modifica sus fuentes y regénéralo. No añadas claves, comandos ni dependencias de un proveedor al núcleo. Los adaptadores de cliente solo conectan las instrucciones con el entorno.

## Regenerar y comprobar

Solo quienes mantienen el paquete necesitan Python 3. No hay dependencias externas.

```bash
python scripts/generar_prompt.py
python scripts/generar_prompt.py --check
```

Comprueba también los enlaces relativos, que las tres entradas de proyecto remitan a los archivos existentes, que el adaptador Cursor preserve solo lectura y que todos los ejemplos sigan identificados como ficticios. Si cambia el método, realiza los casos de [validación](validacion.md).

Actualiza la versión, el README y el changelog al publicar. Revisa las rutas nativas frente a la documentación oficial. No declares probada una aplicación por haber comprobado únicamente sus documentos.

## Copias instaladas

Las carpetas de skills que cada persona copia en `.agents/skills/`, `.claude/skills/` o `.cursor/skills/` son instalaciones, no fuentes alternativas del método. Actualízalas desde `skills/proxima-exploracion/` conservando primero los cambios propios. Evita que dos versiones con el mismo nombre compitan en un cliente.

No uses los mapas del equipo como datos de demostración públicos. `mapas/mapa.md` es una plantilla inicial: al actualizar un proyecto en uso, conserva el mapa que contiene su historial.
