import subprocess
import sys
from pathlib import Path


def find_app_path(project_dir: Path) -> Path:
    """
    Busca el archivo app.py de Streamlit en las ubicaciones habituales del proyecto.
    """

    possible_paths = [
        project_dir / "scouting_multiagent" / "ui" / "app.py",
    ]

    for path in possible_paths:
        if path.exists():
            return path

    searched = "\n".join(str(path) for path in possible_paths)

    raise FileNotFoundError(
        "No se ha encontrado la aplicación Streamlit.\n\n"
        "Rutas revisadas:\n"
        f"{searched}"
    )


def main():
    """
    Punto de entrada del proyecto.

    Lanza la interfaz gráfica de Streamlit.
    """

    project_dir = Path(__file__).resolve().parent
    app_path = find_app_path(project_dir)

    print(f"Lanzando Streamlit desde: {app_path}")

    subprocess.run(
        [
            sys.executable,
            "-m",
            "streamlit",
            "run",
            str(app_path),
        ],
        check=True,
    )


if __name__ == "__main__":
    main()