"""Execute Part 1 notebook and save outputs."""
import os, shutil

os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Clean up previous runs
for d in ["chromadb_udaplay", "test_check"]:
    if os.path.exists(d):
        shutil.rmtree(d)

import nbformat
from nbconvert.preprocessors import ExecutePreprocessor

with open("Udaplay_01_solution_project.ipynb", "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

ep = ExecutePreprocessor(timeout=120, kernel_name="python3")
ep.preprocess(nb, {"metadata": {"path": "."}})

with open("Udaplay_01_solution_project.ipynb", "w", encoding="utf-8") as f:
    nbformat.write(nb, f)

print("Part 1 executed and saved successfully!")
