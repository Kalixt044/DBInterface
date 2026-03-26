import pandas as pd

def separar_por_genero(archivo_entrada='datos_personales.csv'):
    """
    Lee un archivo CSV y separa los datos por género en dos archivos diferentes
    
    Parámetros:
    archivo_entrada (str): Nombre del archivo CSV de entrada
    """
    try:
        # Leer el archivo CSV con punto y coma como separador
        df = pd.read_csv(archivo_entrada, sep=';')
        
        # Separar por género
        hombres = df[df['Sexo'].str.upper() == 'M']  # Considera 'M' como masculino
        mujeres = df[df['Sexo'].str.upper() == 'F']  # Considera 'F' como femenino
        
        # Guardar en archivos separados
        hombres.to_csv('hombres.csv', sep=';', index=False)
        mujeres.to_csv('mujeres.csv', sep=';', index=False)
        
        # Imprimir resumen
        print(f"Proceso completado:")
        print(f"- Total registros: {len(df)}")
        print(f"- Hombres: {len(hombres)} registros guardados en 'hombres.csv'")
        print(f"- Mujeres: {len(mujeres)} registros guardados en 'mujeres.csv'")
        
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo '{archivo_entrada}'")
    except Exception as e:
        print(f"Error al procesar el archivo: {str(e)}")

if __name__ == "__main__":
    separar_por_genero()
