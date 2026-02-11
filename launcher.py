"""Desktop launcher entry-point for packaging the Streamlit app as an executable."""

from __future__ import annotations

import sys
from pathlib import Path

from streamlit.web import cli as stcli


def resolve_app_path() -> Path:
    """Resolve streamlit_app.py path for source and PyInstaller builds."""
    if getattr(sys, "frozen", False):
        base_dir = Path(getattr(sys, "_MEIPASS", Path(sys.executable).resolve().parent))
    else:
        base_dir = Path(__file__).resolve().parent

    app_path = base_dir / "streamlit_app.py"
    if not app_path.exists():
        raise FileNotFoundError(
            "streamlit_app.py was not found in the packaged app. "
            "Rebuild using build_exe.bat so the file is bundled."
        )
    return app_path


def main() -> None:
    app_path = resolve_app_path()
    sys.argv = [
        "streamlit",
        "run",
        str(app_path),
        "--browser.gatherUsageStats=false",
        "--server.headless=true",
    ]
    sys.exit(stcli.main())


if __name__ == "__main__":
    main()
