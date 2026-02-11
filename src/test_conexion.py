from conexion import sql_conn

with sql_conn() as conn:
    cursor = conn.cursor()
    cursor.execute("""
                INSERT INTO staging.stg_horas_estudio (
                    dia,
                    turno,
                    horas_raw,
                    area_conocimiento,
                    curso,
		            tema
                )
                VALUES (?, ?, ?, ?, ?, ?)
            """,
            '2025-01-01', 'mañana', '1:00', 'Python', 'Test Curso', 'Test Tema')