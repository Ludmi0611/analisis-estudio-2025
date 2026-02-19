from conexion import sql_conn
from utils import log


def iniciar_proceso(nombre_proceso):
    with sql_conn() as conn:
        cursor = conn.cursor()

        query = """
            INSERT INTO control.control_procesos 
            (nombre_proceso, fecha_inicio, estado)
            VALUES (?, GETDATE(), 0); 
            
            SELECT SCOPE_IDENTITY() AS id_proceso;
            """
        cursor.execute(query, (nombre_proceso,))

        resultado = cursor.fetchone()
        id_proceso = int(resultado[0])

        cursor.close()
        
        log(f"Proceso iniciado: {nombre_proceso} (ID: {id_proceso})")

        return id_proceso
    
def actualizar_estado(id_proceso, estado, mensaje=None, registros_procesados=None):
    with sql_conn() as conn:
        cursor = conn.cursor()

        query = """
            UPDATE control.control_procesos
            SET 
                estado = ?,
                mensaje = ?,
                registros_procesdados = ?,
                fecha_fin = CASE
                    WHEN ? IN (2,3,4) THEN GETDATE()
                    ELSE fecha_fin
                END
            WHERE id_proceso = ?;
            """
        
        cursor.execute(query, (estado, mensaje, registros_procesados, estado, id_proceso))

        cursor.close()

        log(f"Estado actualizado: ID {id_proceso} -> Estado {estado}")

def finalizar_proceso_ok(id_proceso, estado, mensaje=None, registros_procesados=None):
    with sql_conn() as conn:
        cursor = conn.cursor()

        query = """
            UPDATE control.control_procesos
            SET



            """