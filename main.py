from tkinter import *
from tkinter import ttk
from tkinter import filedialog, messagebox

from Lexico import *

def cargarArchivo(textArea):
  archivo = filedialog.askopenfilename(filetypes=[("Archivo de texto", "*.txt")])
  if archivo:
    with open(archivo, 'r', encoding='utf-8') as f:
      contenido = f.read()
    textArea.delete("1.0", END)
    textArea.insert(END, contenido)

def guardarTexto(textArea):
  texto = textArea.get("1.0", "end")
  if texto != "\n":
    filePath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])
    if filePath:
      with open(filePath, "w") as archivo:
        archivo.write(texto)
        print("¡El archivo se ha guardado exitosamente!")
  else:
    messagebox.showinfo("Alerta", "¡El área de texto debe contener texto!")

def segundaVentana():
  root = Tk()
  root.title("Compilador para MongoDB")
  frm = ttk.Frame(root, padding=10)
  frm.grid()
  textAreaInicial = Text(frm, width=55, height=30)
  textAreaInicial.grid(column=0, row=2)
  ttk.Button(frm, text="Seleccionar archivo", command=lambda:cargarArchivo(textAreaInicial)).grid(column=0, row=0)
  ttk.Button(frm, text="Guardar", command=lambda:guardarTexto(textAreaInicial)).grid(column=4, row=0)
  ttk.Button(frm, text="Regresar", command=root.destroy).grid(column=2, row=4)
  ttk.Label(frm, text="").grid(column=0, row=1)
  ttk.Label(frm, text="").grid(column=0, row=3)
  ttk.Label(frm, text=" ").grid(column=1, row=2)
  ttk.Label(frm, text=" ").grid(column=3, row=2)
  textAreaFinal = Text(frm, width=55, height=30)
  textAreaFinal.grid(column=4, row=2)
  ttk.Button(frm, text="Compilar", command=lambda:analizadorLexico(textAreaInicial, textAreaFinal)).grid(column=2, row=2)
  root.mainloop()

def main():
  root = Tk()
  root.title("Proyecto 2 LFP")
  frm = ttk.Frame(root, padding=20)
  frm.grid()
  ttk.Label(frm, text="Proyecto No. 2").grid(column=0, row=0)
  ttk.Label(frm, text="").grid(column=0, row=1)
  ttk.Label(frm, text="Nombre: Angel Samuel González Velásquez").grid(column=0, row=2)
  ttk.Label(frm, text="Carnet: 202200263").grid(column=0, row=3)
  ttk.Label(frm, text="Curso: Lenguajes Formales y de Programación").grid(column=0, row=4)
  ttk.Label(frm, text="").grid(column=0, row=5)
  ttk.Button(frm, text="Abrir Compilador", command=segundaVentana).grid(column=0, row=6)
  root.mainloop()

main()