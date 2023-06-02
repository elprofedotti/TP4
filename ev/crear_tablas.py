from coneccion_BD import conectar_BD

def crear_tablas():
    conn = conectar_BD()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE areas (
            id SERIAL PRIMARY KEY,
            nombre TEXT NOT NULL,
            ubicacion TEXT NOT NULL
        )
    """)

    cursor.execute("""
        CREATE TABLE empleados (
            id SERIAL PRIMARY KEY,
            nombre TEXT NOT NULL,
            area_id INTEGER,
            FOREIGN KEY(area_id) REFERENCES areas(id)
        )
    """)

    conn.commit()

if __name__ == "__main__":
    crear_tablas()
