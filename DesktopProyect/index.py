import csv
from datetime import datetime, date
import tkinter as tk
from tkinter import messagebox

def calcular_edad(fecha_nacimiento):
    """
    Calcula la edad de una persona basándose en su fecha de nacimiento.
    
    Args:
        fecha_nacimiento (str): Fecha de nacimiento en formato DD/MM/AAAA
    
    Returns:
        int: Edad calculada
    """
    try:
        # Convertir la fecha de nacimiento a un objeto date
        fecha_nac = datetime.strptime(fecha_nacimiento, "%d/%m/%Y").date()
        
        # Fecha actual (27 de noviembre de 2024)
        fecha_actual = date(2024, 11, 27)
        
        # Calcular la edad
        edad = fecha_actual.year - fecha_nac.year
        
        # Ajustar la edad si aún no ha cumplido años en el año actual
        if (fecha_actual.month, fecha_actual.day) < (fecha_nac.month, fecha_nac.day):
            edad -= 1
        
        return edad
    except ValueError:
        messagebox.showerror("Error", "Formato de fecha inválido. Use DD/MM/AAAA")
        return None

def capitalize_fields():
    """Capitaliza la primera letra de los campos ingresados y convierte ciertos campos a mayúscula."""
    
    # Capitalizar los campos donde la primera letra debe ser mayúscula
    campos_titulo = [
        primer_nombre_entry, 
        segundo_nombre_entry, 
        primer_apellido_entry, 
        segundo_apellido_entry
    ]
    
    for campo in campos_titulo:
        valor = campo.get().strip()  # Obtén el valor antes de eliminar
        campo.delete(0, tk.END)      # Borra el valor actual del campo
        campo.insert(0, valor.title())  # Inserta el valor capitalizado (Primera letra en mayúscula)
    
    # Campos que deben estar completamente en mayúsculas
    campos_mayusculas = [
        domicilio_entry, 
        direccion_entry, 
        barrio_entry,
        documento_entry
    ]
    
    for campo in campos_mayusculas:
        valor = campo.get().strip().upper()
        campo.delete(0, tk.END)
        campo.insert(0, valor)
    
    # Sexo debe ser solo M o F en mayúsculas
    sexo = sexo_entry.get().strip().upper()
    if len(sexo) > 0:  # Solo si el campo no está vacío
        sexo_entry.delete(0, tk.END)
        sexo_entry.insert(0, sexo[0])  # Asegura que solo la primera letra sea tomada

def add_new_entry():
    """Agrega una nueva entrada a un archivo CSV usando datos del formulario."""
    
    # Capitaliza los campos antes de hacer cualquier cosa
    capitalize_fields()
    
    filename = "datos_personales.csv"
    fieldnames = [
        'Primer Nombres', 'Segundo nombre', 'Primer Apellidos', 'Segundo Apellido', 
        'Documento', 'Numero de Identificacion', 'Domicilio', 'Fecha de nacimiento', 
        'Edad', 'Sexo', 'Numero Celular', 'Direccion', 'Barrio', 'Email'
    ]
    
    # Verificar si el archivo existe para escribir el encabezado solo una vez
    try:
        with open(filename, 'x', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
            writer.writeheader()
    except FileExistsError:
        pass
    
    # Obtener los valores de los campos
    fecha_nacimiento = fecha_entry.get()
    edad = calcular_edad(fecha_nacimiento)
    if edad is None:
        return  # Si hay un error con la fecha, detenemos el proceso.
    
    # Escribir los datos en el archivo CSV
    with open(filename, 'a', newline='', encoding='utf-8') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
        writer.writerow({
            'Primer Nombres': primer_nombre_entry.get(),
            'Segundo nombre': segundo_nombre_entry.get(),
            'Primer Apellidos': primer_apellido_entry.get(),
            'Segundo Apellido': segundo_apellido_entry.get(),
            'Documento': documento_entry.get(),
            'Numero de Identificacion': numero_identificacion_entry.get(),
            'Domicilio': domicilio_entry.get(),
            'Fecha de nacimiento': fecha_nacimiento,
            'Edad': edad,
            'Sexo': sexo_entry.get(),
            'Numero Celular': celular_entry.get(),
            'Direccion': direccion_entry.get(),
            'Barrio': barrio_entry.get(),
            'Email': email_entry.get()
        })
        messagebox.showinfo("Éxito", "Registro guardado exitosamente")
        clear_form()

def clear_form():
    """Limpia todos los campos del formulario."""
    primer_nombre_entry.delete(0, tk.END)
    segundo_nombre_entry.delete(0, tk.END)
    primer_apellido_entry.delete(0, tk.END)
    segundo_apellido_entry.delete(0, tk.END)
    documento_entry.delete(0, tk.END)
    numero_identificacion_entry.delete(0, tk.END)
    
    # Restablecer campos con valores por defecto
    domicilio_entry.delete(0, tk.END)
    domicilio_entry.insert(0, "Puerto Colombia")
    
    direccion_entry.delete(0, tk.END)
    direccion_entry.insert(0, "Finca Nuevo Amanecer")
    
    barrio_entry.delete(0, tk.END)
    barrio_entry.insert(0, "Sierra Alta")
    
    fecha_entry.delete(0, tk.END)
    sexo_entry.delete(0, tk.END)
    celular_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)

# Crear la ventana principal
root = tk.Tk()
root.title("Data Base Cabildo Chimila")

# Crear los campos de entrada
tk.Label(root, text="Primer Nombre").grid(row=0, column=0)
primer_nombre_entry = tk.Entry(root)
primer_nombre_entry.grid(row=0, column=1)

tk.Label(root, text="Segundo Nombre").grid(row=1, column=0)
segundo_nombre_entry = tk.Entry(root)
segundo_nombre_entry.grid(row=1, column=1)

tk.Label(root, text="Primer Apellido").grid(row=2, column=0)
primer_apellido_entry = tk.Entry(root)
primer_apellido_entry.grid(row=2, column=1)

tk.Label(root, text="Segundo Apellido").grid(row=3, column=0)
segundo_apellido_entry = tk.Entry(root)
segundo_apellido_entry.grid(row=3, column=1)

tk.Label(root, text="Documento (TI/CC)").grid(row=4, column=0)
documento_entry = tk.Entry(root)
documento_entry.grid(row=4, column=1)

tk.Label(root, text="Número de Identificación").grid(row=5, column=0)
numero_identificacion_entry = tk.Entry(root)
numero_identificacion_entry.grid(row=5, column=1)

tk.Label(root, text="Domicilio").grid(row=6, column=0)
domicilio_entry = tk.Entry(root)
domicilio_entry.insert(0, "Puerto Colombia")  # Valor por defecto en mayúsculas
domicilio_entry.grid(row=6, column=1)

tk.Label(root, text="Fecha de Nacimiento (DD/MM/AAAA)").grid(row=7, column=0)
fecha_entry = tk.Entry(root)
fecha_entry.grid(row=7, column=1)

tk.Label(root, text="Sexo (M/F)").grid(row=8, column=0)
sexo_entry = tk.Entry(root)
sexo_entry.grid(row=8, column=1)

tk.Label(root, text="Número de Celular").grid(row=9, column=0)
celular_entry = tk.Entry(root)
celular_entry.grid(row=9, column=1)

tk.Label(root, text="Dirección").grid(row=10, column=0)
direccion_entry = tk.Entry(root)
direccion_entry.insert(0, "Finca Nuevo Amanecer")  # Valor por defecto en mayúsculas
direccion_entry.grid(row=10, column=1)

tk.Label(root, text="Barrio").grid(row=11, column=0)
barrio_entry = tk.Entry(root)
barrio_entry.insert(0, "Sierra Alta")  # Valor por defecto en mayúsculas
barrio_entry.grid(row=11, column=1)

# Campo para el correo electrónico
tk.Label(root, text="Email").grid(row=12, column=0)
email_entry = tk.Entry(root)
email_entry.grid(row=12, column=1)

# Botón para agregar la entrada
tk.Button(root, text="Guardar Registro", command=add_new_entry).grid(row=13, column=0, columnspan=2)

# Ejecutar la aplicación
root.mainloop()
