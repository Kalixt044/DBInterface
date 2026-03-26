import csv
import os
import pandas as pd

class GestorRegistros:
    def __init__(self, nombre_archivo):
        self.nombre_archivo = nombre_archivo
        self.columnas = [
            "Primer Nombres", "Segundo nombre", "Primer Apellidos", 
            "Segundo Apellido", "Documento", "Numero de Identificacion", 
            "Domicilio", "Fecha de nacimiento", "Edad", "Sexo", 
            "Numero Celular", "Direccion", "Barrio", "Email"
        ]

    def buscar_registro(self, campo, valor):
        """
        Busca registros por un campo específico
        
        Args:
            campo (str): Campo de búsqueda
            valor (str): Valor a buscar
        
        Returns:
            list: Lista de registros coincidentes
        """
        if campo not in self.columnas:
            print(f"El campo {campo} no es válido.")
            return []

        # Usar pandas para facilitar la búsqueda
        df = pd.read_csv(self.nombre_archivo, sep=';', encoding='utf-8')
        resultados = df[df[campo].astype(str).str.contains(valor, case=False, na=False)]
        
        return resultados.to_dict('records')

    def editar_registro(self, campo_busqueda, valor_busqueda, campo_edicion, nuevo_valor):
        """
        Edita un registro específico
        
        Args:
            campo_busqueda (str): Campo para encontrar el registro
            valor_busqueda (str): Valor para encontrar el registro
            campo_edicion (str): Campo a editar
            nuevo_valor (str): Nuevo valor para el campo
        
        Returns:
            bool: True si se editó, False si no
        """
        # Leer el archivo
        df = pd.read_csv(self.nombre_archivo, sep=';', encoding='utf-8')
        
        # Encontrar registros que coincidan
        mascara = df[campo_busqueda].astype(str).str.contains(valor_busqueda, case=False, na=False)
        
        if mascara.sum() == 0:
            print("No se encontraron registros.")
            return False
        
        # Mostrar registros encontrados para confirmar
        print("Registros encontrados:")
        print(df[mascara])
        
        confirmacion = input("¿Desea editar estos registros? (s/n): ").lower()
        if confirmacion != 's':
            return False
        
        # Realizar la edición
        df.loc[mascara, campo_edicion] = nuevo_valor
        
        # Guardar el archivo
        df.to_csv(self.nombre_archivo, sep=';', index=False, encoding='utf-8')
        
        print(f"Registros editados exitosamente en el campo {campo_edicion}")
        return True

# Ejemplo de uso
def main():
    nombre_archivo = 'datos_personales.csv'  # Nombre de archivo específico
    
    # Crear instancia del gestor
    gestor = GestorRegistros(nombre_archivo)
    
    while True:
        print("\n--- MENÚ ---")
        print("1. Buscar Registro")
        print("2. Editar Registro")
        print("3. Salir")
        
        opcion = input("Elija una opción (1-3): ")
        
        if opcion == '1':
            campo = input("Ingrese el campo de búsqueda: ")
            valor = input("Ingrese el valor a buscar: ")
            resultados = gestor.buscar_registro(campo, valor)
            
            if resultados:
                print("Registros encontrados:")
                for registro in resultados:
                    print(registro)
            else:
                print("No se encontraron registros.")
        
        elif opcion == '2':
            campo_busqueda = input("Ingrese el campo para buscar el registro: ")
            valor_busqueda = input("Ingrese el valor de búsqueda: ")
            campo_edicion = input("Ingrese el campo a editar: ")
            nuevo_valor = input("Ingrese el nuevo valor: ")
            
            gestor.editar_registro(campo_busqueda, valor_busqueda, campo_edicion, nuevo_valor)
        
        elif opcion == '3':
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
