import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_DIR = BASE_DIR/ "data" / "raw"

def leer_cursos():
    archivo = RAW_DIR / "cursos_2025.csv"
    df = pd.read_csv(archivo, encoding="utf-8")
    return df

def leer_inscripciones():
    archivo = RAW_DIR / "cursos_inscripcion_2025.csv"
    df = pd.read_csv(archivo, encoding="utf-8")
    return df

def leer_horas_estudio():
    archivo = RAW_DIR / "horas_estudio.csv"
    df = pd.read_csv(archivo, encoding="utf-8", header=1)
    return df

