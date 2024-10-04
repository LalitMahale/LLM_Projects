import os
from pathlib import Path

list_file = [
    "src/__init__.py",
    "src/pipeline.py",
    "src/model_config.py",
    "utils/__init__.py",
    "utils/prompts.py",
    "utils/logs.log",
    "utils/api_connection.py",
    "test_images/.gitkeep",
    "app.py",
    "experiments/experiments.ipynb",
    ".env",
    "Dockerfile",
    "requirements.txt",
    ".gitignore",
    "README.md",


]


for file in list_file:
    file = Path(file)
    folder, filename = os.path.split(file)

    if not os.path.exists(folder) and folder != "":
        os.makedirs(folder,exist_ok=True)

    if not os.path.exists(file) or (os.path.getsize(file)==0):
        with open(file=file,mode="w") as f:
            pass

