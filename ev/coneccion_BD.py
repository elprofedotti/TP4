import psycopg2

def conectar_BD():
    try:
        conn = psycopg2.connect(
            user="postgres",
            password="Helito&2018",
            host="localhost",
            port="5432",
            database="tp4"
        )

        return conn
        
    except (Exception, psycopg2.Error) as error:
        print("**************************")
        print("Error al conectar, LPTM!!", error)
        print("**************************")