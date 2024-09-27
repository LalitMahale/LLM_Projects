import os
from pathlib import Path

list_files = [
    "src/__init__.py",
    "utils/__init__.py",
    "requirements.txt",
    "streamlit_app.py",
    "experiments/experiments.ipynb"
    "credential/config.toml"
]


for file in list_files:
    folder, filename = os.path.split(file)
    if folder != "":
        os.makedirs(folder,exist_ok=True)

    if os.path.exists(folder) and (os.path.getsize(folder) == 0):
        with open(file,"wb") as f:
            pass
