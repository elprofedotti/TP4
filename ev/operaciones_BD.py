def insertar_areas(conn, area_nombre, area_ubicacion):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO areas (nombre, ubicacion) 
        VALUES (%s, %s)
    """, (area_nombre, area_ubicacion))
    conn.commit()

def insertar_empleados(conn, empleados_nombre, area_id):
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO empleados (nombre, area_id) 
        VALUES (%s, %s)
    """, (empleados_nombre, area_id))
    conn.commit()

def listar_areas(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM areas")
    areas = cursor.fetchall()
    return areas

def listar_empleados(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT empleados.id, empleados.nombre, areas.nombre FROM empleados INNER JOIN areas ON empleados.area_id = areas.id")
    empleados = cursor.fetchall()
    return empleados

def update_area(conn, area_id, nuevo_nombre, nueva_ubicacion):
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE areas 
        SET nombre = %s, ubicacion = %s
        WHERE id = %s
    """, (nuevo_nombre, nueva_ubicacion, area_id))
    conn.commit()

def update_empleado(conn, empleado_id, nuevo_nombre, nevo_id_area):
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE empleados 
        SET nombre = %s, area_id = %s
        WHERE id = %s
    """, (nuevo_nombre, nevo_id_area, empleado_id))
    conn.commit()

