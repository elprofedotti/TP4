from coneccion_BD import conectar_BD
from operaciones_BD import insertar_areas,insertar_empleados, listar_areas, listar_empleados, update_area, update_empleado
import os


def main():
    conn = conectar_BD()

    while True:
        limpiar_pantalla()
        print("---- MENÚ ----")
        print("1. Cargar datos en 'areas'")
        print("2. Cargar datos en 'empleados'")
        print("3. Listar 'areas'")
        print("4. Listar 'empleados'")
        print("5. Actualizar 'area'")
        print("6. Actualizar 'empleado'")
        print("7. Salir")

        option = input("Elige una opción: ")

        if option == "1":
            limpiar_pantalla()
            area_nombre = input("Ingrese el nombre del área: ")
            area_ubicacion = input("Ingrese la ubicación del área: ")
            insertar_areas(conn, area_nombre, area_ubicacion)
            print("Area agregada correctamente")
            input('Presiona Enter para volver al menu...')

        elif option == "2":
            limpiar_pantalla()
            empleados_nombre = input("Ingrese el nombre del empleado: ")
            area_id = int(input("Ingrese el ID del área a la que pertenece el empleado: "))
            insertar_empleados(conn, empleados_nombre, area_id)
            print("Empleado agregado correctamente")
            input('Presiona Enter para volver al menu...')

        elif option == "3":
            lista_are(conn)
            input('Presiona Enter para continuar...')

        elif option == "4":
            listar_emp(conn)
            input('Presiona Enter para continuar...')
        
        elif option == "5":
            area_id = input("Ingresa el ID del área a actualizar: ")
            nuevo_nombre = input("Ingresa el nuevo nombre del área: ")
            nueva_ubicacion = input("Ingresa la nueva ubicación del área: ")
            update_area(conn, area_id, nuevo_nombre, nueva_ubicacion)
            print("Area actualizada correctamente")
            input('Presiona Enter para volver al menu...')

        elif option == "6":
            empleado_id = input("Ingresa el ID del empleado a actualizar: ")
            nuevo_nombre = input("Ingresa el nuevo nombre del empleado: ")
            nuevo_id_area = input("Ingresa el nuevo ID de área para el empleado: ")
            update_empleado(conn, empleado_id, nuevo_nombre, nuevo_id_area)
            print("Empleado actualizado correctamente")
            input('Presiona Enter para volver al menu...')

        elif option == "7":
            if conn:
                conn.close()
                limpiar_pantalla()
                print("Conexion PostgreSQL cerrada!")
                input('Presiona Enter para continuar con el cierre de la app...')
            break
            

        else:
            print("Opción inválida. Por favor, elige una opción del menú.")

def limpiar_pantalla():
    if os.name == 'nt':  # para windows
        _ = os.system('cls')
    else:  # para mac y linux
        _ = os.system('clear')

def listar_emp(conn):
    empleados = listar_empleados(conn)
    limpiar_pantalla()
    for empleado in empleados:
        print(f'ID: {empleado[0]}, Nombre: {empleado[1]}, Área: {empleado[2]}')

def lista_are(conn):
    areas = listar_areas(conn)
    limpiar_pantalla()
    for area in areas:
        print(area)


if __name__ == "__main__":
    main()
