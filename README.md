# 💚 She-Hulk Transformation Game

A Streamlit game where you can transform Jennifer Walters into She-Hulk in Story Mode or Sandbox Mode.

## Run locally

1. Install requirements

   ```bash
   pip install -r requirements.txt
   ```

2. Start the app

   ```bash
   streamlit run streamlit_app.py
   ```

## Build a Windows `.exe`

This repo includes a launcher and build script so you can package the app as a Windows executable.

### Option A (quick build with batch file)

On **Windows**, run:

```bat
build_exe.bat
```

This will:

- create a virtual environment (`venv`)
- install dependencies + `pyinstaller`
- bundle `streamlit_app.py` into the executable
- generate:

`dist\SheHulkTransformationGame.exe`

### Option B (manual PyInstaller command)

```bash
pip install -r requirements.txt pyinstaller
pyinstaller --noconfirm --clean --onefile --name SheHulkTransformationGame --add-data "streamlit_app.py;." launcher.py
```

### Notes

- Build the executable on Windows to produce a native `.exe`.
- `requirements.txt` includes both `streamlit` and `pillow`, which the app needs.
- The launcher entrypoint is `launcher.py`, which runs `streamlit_app.py` internally.
- If you need custom PyInstaller behavior, add your own `.spec` file and run `pyinstaller your_file.spec`.
