
import tkinter as tk
from tkinter import Tk
from tkinter import filedialog

from tkinter import Tk, filedialog, ttk

def cargar_pozo(tree):
    archivos = filedialog.askopenfilenames(filetypes=[("Archivos LAS", "*.las")])
    for archivo in archivos:
        tree.insert("", "end", text=archivo)
        

def crear_menu_principal(ventana, acciones):
    menu_principal = tk.Menu(ventana)

    # Crear el menú "Pozo"
    menu_pozo = tk.Menu(menu_principal, tearoff=0)
    menu_pozo.add_command(label="Cargar Pozo", command=acciones["cargar_pozo"])
    menu_pozo.add_command(label="Grabar Pozo", command=acciones["grabar_pozo"])
    menu_pozo.add_command(label="Borrar Pozo", command=acciones["borrar_pozo"])
    menu_pozo.add_command(label="Manejar Topes", command=acciones["manejar_topes"])
    menu_pozo.add_command(label="Exportar datos", command=acciones["exportar_datos"])
    menu_pozo.add_command(label="Imprimir Pozo", command=acciones["imprimir_pozo"])
    menu_principal.add_cascade(label="Pozo", menu=menu_pozo)

    # Crear el menú "Calcular"
    menu_calcular = tk.Menu(menu_principal, tearoff=0)
    menu_calcular.add_command(label="Volumen de arcilla", command=acciones["volumen_arcilla"])
    menu_calcular.add_command(label="Porosidad", command=acciones["porosidad"])
    menu_calcular.add_command(label="Saturación de agua", command=acciones["saturacion_agua"])
    menu_calcular.add_command(label="Fórmula de Usuario", command=acciones["formula_usuario"])
    menu_calcular.add_command(label="Reporte", command=acciones["reporte"])
    menu_principal.add_cascade(label="Calcular", menu=menu_calcular)

    # Crear el menú "Ver"
    menu_ver = tk.Menu(menu_principal, tearoff=0)
    menu_ver.add_command(label="Graficar Registro", command=acciones["graficar_registro"])
    menu_ver.add_command(label="Estadística de curvas", command=acciones["estadistica_curvas"])
    menu_principal.add_cascade(label="Ver", menu=menu_ver)

    # Crear el menú "Machine Learning"
    menu_ml = tk.Menu(menu_principal, tearoff=0)
    menu_ml.add_command(label="Regresión Multilineal", command=acciones["regresion_multilineal"])
    menu_principal.add_cascade(label="Machine Learning", menu=menu_ml)

    ventana.config(menu=menu_principal)
    ventana.children['menu'] = menu_principal  # Agrega explícitamente el menú principal a ventana.children

if __name__ == "__main__":
    ventana = Tk()

    # Crear un panel izquierdo con un Treeview
    panel_izquierdo = tk.Frame(ventana)
    panel_izquierdo.pack(side="left", fill="y")

    tree = ttk.Treeview(panel_izquierdo)
    tree.pack(fill="both", expand=True)
    
    
    acciones = {
        "cargar_pozo": cargar_pozo,
        # ... otras acciones para las opciones de menú ...
    }
    
 # Cambiar el color de la ventana a azul claro
    ventana.config(bg="#ADD8E6")
    
    acciones = {
        "cargar_pozo": lambda: print("Cargar Pozo seleccionado"),
        "grabar_pozo": lambda: print("Grabar Pozo seleccionado"),
        "borrar_pozo": lambda: print("Borrar Pozo seleccionado"),
        "manejar_topes": lambda: print("Manejar Topes seleccionado"),
        "exportar_datos": lambda: print("Exportar datos seleccionado"),
        "imprimir_pozo": lambda: print("Imprimir Pozo seleccionado"),
        "volumen_arcilla": lambda: print("Volumen de arcilla seleccionado"),
        "porosidad": lambda: print("Porosidad seleccionada"),
        "saturacion_agua": lambda: print("Saturación de agua seleccionada"),
        "formula_usuario": lambda: print("Fórmula de Usuario seleccionada"),
        "reporte": lambda: print("Reporte seleccionado"),
        "graficar_registro": lambda: print("Graficar Registro seleccionado"),
        "estadistica_curvas": lambda: print("Estadística de curvas seleccionada"),
        "regresion_multilineal": lambda: print("Regresión Multilineal seleccionada"),
        # ... agregar más acciones para las opciones de menú según sea necesario ...
    }
    crear_menu_principal(ventana, acciones)
    ventana.mainloop()
