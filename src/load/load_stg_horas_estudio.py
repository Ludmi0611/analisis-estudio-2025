import pandas as pd
from conexion import sql_conn
from utils import log

def iniciar_proceso(nombre_proceso, etapa):
    """
    
    """

    with sql_conn() as conn:
        cursor = conn.cursor()

        query = """
            INSERT INTO control.control_procesos 
            (nombre_proceso, etapa, fecha_inicio, estado)
            VALUES (?, ?, GETDATE(), 'INICIADO');

            SELECT SCOPE_IDENTITY();
            """
        
        cursor.execute(query, (nombre_proceso, etapa))
        id_proceso = cursor.fetchone()[0]

        return int(id_proceso)
    
def finalizar_proceso_ok(id_proceso, registros_procesados):
    with sql_conn as conn:
        cursor = conn.cursor()

        query = """
            UPDATE control.control_procesos
            SET 
                estado = 'OK',
                fecha_fin = GETDATE(),
                registros_procesados = ?
            WHERE id_proceso = ?;

            """
        
        cursor.execute(query, (registros_procesados, id_proceso))

def finalizar_proceso_error(id_proceso, mensaje_error):
    with sql_conn as conn:
        cursor = conn.cursor()

        query = """
            UPDATE control.control_procesos
            SET
                estado = 'ERROR',
                fecha_fin = GETDATE(),
                mensaje_error = ?
            WHERE id_proceso = ?;
            """