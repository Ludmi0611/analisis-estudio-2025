import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DIR = BASE_DIR / "data" / "raw"

cursos_2025 = RAW_DIR / "cursos_2025.csv"
cursos_inscripcion_2025 = RAW_DIR / "cursos_inscripcion_2025.csv"
horas_estudio = RAW_DIR / "horas_estudio.csv"

