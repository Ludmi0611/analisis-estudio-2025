import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

RAW_DIR = BASE_DIR / "data" / "raw"

cursos_2025 = RAW_DIR / "cursos_2025.csv"
cursos_inscripcion_2025 = RAW_DIR / "cursos_inscripcion_2025.csv"
horas_estudio = RAW_DIR / "horas_estudio.csv"

df_cursos_2025 = pd.read_csv(cursos_2025)
df_cursos_inscripcion_2025 = pd.read_csv(cursos_inscripcion_2025)
df_horas_estudio = pd.read_csv(horas_estudio, header=1)

# print(df_cursos_2025.head())
# print(df_cursos_2025.info())

# print(df_cursos_inscripcion_2025.head())
# print(df_cursos_inscripcion_2025.info())

# print(df_horas_estudio.head())
# print(df_horas_estudio.info())

def clean_columns(df):
    df = df.copy()
    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
        .str.replace(" ", "_")
    )
    return df

def clean_text(df):
    df = df.copy()
    for col in df.select_dtypes(include=["object", "string"]).columns:
        df[col] = (
            df[col]
            .astype("string")
            .str.strip()
            .str.title()
            .replace("Nan", pd.NA)
        )
    return df

df_objetivos = clean_columns(df_cursos_2025)
df_inscripcion = clean_columns(df_cursos_inscripcion_2025)
df_estudio = clean_columns(df_horas_estudio)
df_objetivos = clean_text(df_objetivos)
df_inscripcion = clean_text(df_inscripcion)
df_estudio = clean_text(df_estudio)
print(df_objetivos.head())

print(df_inscripcion.head())
print(df_estudio.head())

df_objetivos["fecha_de_inicio"] = pd.to_datetime(
    df_objetivos["fecha_de_inicio"], 
    dayfirst=True,
    errors="coerce"
)

df_objetivos["fecha_de_finalización"] = pd.to_datetime(
    df_objetivos["fecha_de_finalización"],
    dayfirst=True,
    errors="coerce"
)

df_estudio["dia"] = pd.to_datetime(
    df_estudio["dia"],
    dayfirst=True,
    errors="coerce"
)

df_inscripcion["fecha_limpia"] = df_inscripcion["fecha"].str.extract(r"(\d{1,2}/\d{1,2})")
df_inscripcion["fecha_limpia"] += "/2025"


mask_sin_anio = df_inscripcion["fecha"].str.match(r"^\d{1,2}/\d{1,2}$")
df_inscripcion.loc[mask_sin_anio, "fecha"] = (df_inscripcion.loc[mask_sin_anio, "fecha"] + "/2025")


# !! corregir fecha de inscripcion ya que no le puse año, y tiene texto !!
df_inscripcion["fecha_limpia"] = pd.to_datetime(
    df_inscripcion["fecha_limpia"],
    dayfirst=True,
    errors="coerce"
)

