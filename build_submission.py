import zipfile
from pathlib import Path

files = [
    Path("src/README.md"),
    Path("src/load_data.py"),
    Path("src/requirements.txt"),
]

# src/*.ipynb
files += list(Path("src").glob("*.ipynb"))

# src/data/*.csv
files += list(Path("src/data").glob("*.csv"))

# src/data/*.tsv
files += list(Path("src/data").glob("*.tsv"))

# src/data/variables.json
files.append(Path("src/data/variables.json"))

# create a zip file containing the files
with zipfile.ZipFile("05-kotsuka-salnaser-annecao_2026winter.zip", "w", zipfile.ZIP_DEFLATED) as z:
    for f in files:
        z.write(f, f.as_posix())

print("submission zip created successfully.")
