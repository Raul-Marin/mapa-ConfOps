#!/usr/bin/env python3
"""Genera el prompt portable desde las fuentes canónicas. Solo biblioteca estándar."""
import argparse
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGET = ROOT / "INICIO-RAPIDO.md"


def render():
    agent = (ROOT / "agents/acompanante-exploracion.md").read_text(encoding="utf-8").strip()
    skill = (ROOT / "skills/proxima-exploracion/SKILL.md").read_text(encoding="utf-8")
    if not skill.startswith("---\n"):
        raise ValueError("La skill debe comenzar con metadatos YAML")
    method = skill.split("---\n", 2)[2].strip()
    template = (ROOT / "skills/proxima-exploracion/assets/plantilla-mapa.md").read_text(encoding="utf-8").strip()
    version = (ROOT / "VERSION").read_text(encoding="utf-8").strip()
    header = f"""# Próxima exploración · {version} · instrucciones para cualquier chat

Copia todo este documento en una conversación y añade tu dificultad o tu mapa al final. También puedes adjuntarlo si tu cliente lee archivos Markdown. No requiere instalación, acceso a archivos ni comandos especiales.

---

Actúa como acompañante de exploración. Aplica las instrucciones siguientes al contexto que añada el usuario. Todo el método y la plantilla están incluidos aquí: las rutas mencionadas son opcionales y no necesitas abrirlas. No ejecutes código para utilizar este recurso. Si todavía no hay contexto, pregunta por una dificultad concreta y un ejemplo.
"""
    footer = """## Mi contexto (completar antes de enviar)

- Quiero: preparar una prueba / revisar resultados / retomar un mapa.
- Nos está costando: […]
- Un ejemplo y su fuente: […]
- Personas y tiempo disponibles: […]
- Mapa anterior y evidencias nuevas, si existen: […]
- Decisiones ya tomadas por el equipo: […]

Devuelve el mapa completo aquí. Marca lo que no sabemos como pendiente.
"""
    return "\n\n".join([header.strip(), agent, method, "## Plantilla incluida\n\n" + template, footer.strip()]) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Comprueba sin escribir que el prompt está actualizado")
    args = parser.parse_args()
    expected = render()
    if args.check:
        if not TARGET.exists() or TARGET.read_text(encoding="utf-8") != expected:
            raise SystemExit("INICIO-RAPIDO.md desactualizado. Ejecuta python scripts/generar_prompt.py")
        print("OK: prompt portable sincronizado")
    else:
        TARGET.write_text(expected, encoding="utf-8")
        print("Generado INICIO-RAPIDO.md")


if __name__ == "__main__":
    main()
