import pandas as pd
import sqlite3
import os

def csv_to_sqlite(archivo_csv='datos_personales.csv', db_nombre='personas.db'):
    """
    Convierte un archivo CSV a una base de datos SQLite
    
    Parámetros:
    archivo_csv (str): Nombre del archivo CSV de entrada
    db_nombre (str): Nombre de la base de datos SQLite a crear
    """
    try:
        # Leer el archivo CSV
        df = pd.read_csv(archivo_csv, sep=';')
        
        # Verificar las columnas del DataFrame
        print(f"Columnas en el archivo CSV: {df.columns.tolist()}")
        
        # Crear conexión a SQLite
        conn = sqlite3.connect(db_nombre)
        
        # Definir el esquema de la tabla basado en las columnas del CSV
        crear_tabla_sql = '''
        CREATE TABLE IF NOT EXISTS personas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            primer_nombres TEXT,
            segundo_nombre TEXT,
            primer_apellidos TEXT,
            segundo_apellido TEXT,
            documento TEXT,
            numero_identificacion TEXT,
            domicilio TEXT,
            fecha_nacimiento TEXT,
            edad INTEGER,
            sexo TEXT,
            numero_celular TEXT,
            direccion TEXT,
            barrio TEXT,
            email TEXT
        )
        '''
        
        # Ejecutar creación de tabla
        conn.execute(crear_tabla_sql)
        
        # Verificar cuántas columnas hay en el archivo CSV
        columnas_csv = df.columns.tolist()
        print(f"Columnas en el archivo CSV: {columnas_csv}")
        
        # Renombrar las columnas para que coincidan con los nombres en SQLite
        if len(columnas_csv) == 15:
            df.columns = [
                'primer_nombres',
                'segundo_nombre',
                'primer_apellidos',
                'segundo_apellido',
                'documento',
                'numero_identificacion',
                'domicilio',
                'fecha_nacimiento',
                'edad',
                'sexo',
                'numero_celular',
                'direccion',
                'barrio',
                'email',
                'columna_extra'  # Si hay una columna extra, la agregamos
            ]
        else:
            # Si las columnas no coinciden, mostrar un mensaje de error
            print(f"Error: El número de columnas en el CSV no coincide con el esperado ({len(columnas_csv)} vs 15).")
            return
        
        # Insertar datos en la tabla
        df.to_sql('personas', conn, if_exists='replace', index=False)

        # Verificar si se insertaron registros correctamente
        cursor = conn.cursor()
        cursor.execute('SELECT COUNT(*) FROM personas')
        total_registros = cursor.fetchone()[0]

        # Cerrar la conexión a la base de datos
        conn.commit()
        conn.close()

        # Imprimir mensaje de éxito
        print(f"Proceso completado exitosamente:")
        print(f"- Base de datos creada: {db_nombre}")
        print(f"- Tabla creada: personas")
        print(f"- Total registros importados: {total_registros}")
        
        # Verificar el tamaño del archivo de base de datos
        db_size = os.path.getsize(db_nombre) / 1024  # Tamaño en KB
        print(f"- Tamaño de la base de datos: {db_size:.2f} KB")
        
        # Mostrar ejemplo de consulta
        print("\nPuedes consultar los datos usando SQL, por ejemplo:")
        print("SELECT * FROM personas LIMIT 5;")
        
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{archivo_csv}'")
    except pd.errors.ParserError:
        print(f"Error: No se pudo procesar el archivo CSV '{archivo_csv}', verifica el formato")
    except sqlite3.Error as e:
        print(f"Error en la base de datos: {e}")
    except Exception as e:
        print(f"Error durante la conversión: {str(e)}")

def mostrar_ejemplo_consulta():
    """
    Muestra un ejemplo de cómo consultar la base de datos
    """
    try:
        conn = sqlite3.connect('personas.db')
        cursor = conn.cursor()

        # Ejecutar consulta para obtener los primeros 5 registros
        print("\nEjemplo de primeros 5 registros:")
        cursor.execute('''
            SELECT 
                primer_nombres, 
                primer_apellidos, 
                edad, 
                sexo, 
                barrio 
            FROM personas 
            LIMIT 5
        ''')

        registros = cursor.fetchall()
        for registro in registros:
            print(registro)

        # Cerrar conexión
        conn.close()

    except sqlite3.Error as e:
        print(f"Error al consultar la base de datos: {str(e)}")
    except Exception as e:
        print(f"Error inesperado: {str(e)}")

if __name__ == "__main__":
    csv_to_sqlite()  # Llamada para convertir el CSV a la base de datos
    mostrar_ejemplo_consulta()  # Muestra ejemplo de consulta a la base de datos
