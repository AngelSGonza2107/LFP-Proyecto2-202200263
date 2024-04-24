from Lexema import Lexema
from Error import Error
from Sintactico import *
from TablaErrores import *
from TablaLexemas import *

listaLexemas = []
listaErrores = []

def analizadorLexico(textAreaInicial, textAreaFinal):
  listaLexemas.clear()
  listaErrores.clear()
  textAreaFinal.delete("1.0", "end")
  textAreaInicial = textAreaInicial.get("1.0", "end")
  fila = 1
  columna = 0
  signosValidos = {".": "Punto", ",": "Coma", ":": "Dos Puntos", ";": "Punto y coma", "{": "Llave abrir", "}": "Llave cerrar", "(": "Paréntesis abrir", ")": "Paréntesis cerrar", "=": "Igual"}
  signosNoValidos = "!¡#%&?¿|_><`+´'^"

  i = 0
  while i < len(textAreaInicial):
    char = textAreaInicial[i]

    if char == "\n":
      fila += 1
      columna = 0
    else:
      columna += 1

    if char.isspace() or char in [" ", "\t", "\n", "\r"]:
      i += 1
      continue

    if char in signosValidos:
      listaLexemas.append(Lexema(signosValidos[char], char, "1", fila, columna))
      i += 1
      continue

    if char in signosNoValidos:
      listaErrores.append(Error("Error Léxico", f"Carácter no válido: {char}", fila, columna))
      i += 1
      continue

    palabraAnalizar = ""
    if char.isalnum():
      while i < len(textAreaInicial) and textAreaInicial[i].isalnum():
        palabraAnalizar += textAreaInicial[i]
        i += 1
      palabrasReservadas = {
        "CrearBD": "Etiqueta crear base de datos",
        "EliminarBD": "Etiqueta eliminar base de datos",
        "CrearColeccion": "Etiqueta crear colección",
        "EliminarColeccion": "Etiqueta eliminar colección",
        "InsertarUnico": "Etiqueta insertar registro",
        "ActualizarUnico": "Etiqueta actualizar registro",
        "EliminarUnico": "Etiqueta eliminar registro",
        "BuscarTodo": "Etiqueta buscar todos los registros",
        "BuscarUnico": "Etiqueta buscar registro simple",
        "nueva": "Palabra reservada",
      }
      if palabraAnalizar in palabrasReservadas:
        listaLexemas.append(Lexema(palabrasReservadas[palabraAnalizar], palabraAnalizar, "2", fila, columna))
      elif palabraAnalizar.isdigit():
        listaLexemas.append(Lexema("Número", palabraAnalizar, "3", fila, columna))
      else:
        listaLexemas.append(Lexema("Nombre función", palabraAnalizar, "4", fila, columna))
      columna += len(palabraAnalizar)
      palabraAnalizar = ""
    
    elif char == '"':
      palabraAnalizar += char
      columnaInicial = columna
      i += 1
      while i < len(textAreaInicial) and textAreaInicial[i] != '"':
        palabraAnalizar += textAreaInicial[i]
        i += 1
      if i < len(textAreaInicial):
        palabraAnalizar += textAreaInicial[i]
      listaLexemas.append(Lexema("Cadena", palabraAnalizar, "5", fila, columnaInicial))
      palabraAnalizar = ""
      columnaInicial += len(palabraAnalizar)
      i += 1

    elif char == '“':
      palabraAnalizar += char
      columnaInicial = columna
      i += 1
      while i < len(textAreaInicial) and textAreaInicial[i] != '”':
        palabraAnalizar += textAreaInicial[i]
        i += 1
      if i < len(textAreaInicial):
        palabraAnalizar += textAreaInicial[i]
      if "{" in palabraAnalizar:
        listaLexemas.append(Lexema("JSON", palabraAnalizar, "5", fila, columnaInicial))
      else:
        listaLexemas.append(Lexema("Cadena", palabraAnalizar, "5", fila, columnaInicial))
      palabraAnalizar = ""
      columnaInicial += len(palabraAnalizar)
      i += 1

    elif char == '$':
      palabraAnalizar += char
      columnaInicial = columna
      i += 1
      while i < len(textAreaInicial) and textAreaInicial[i] != ' ':
        palabraAnalizar += textAreaInicial[i]
        i += 1
      if i < len(textAreaInicial):
        palabraAnalizar += textAreaInicial[i]
      listaLexemas.append(Lexema("Cadena", palabraAnalizar, "6", fila, columnaInicial))
      palabraAnalizar = ""
      columnaInicial += len(palabraAnalizar)
      i += 1

    elif char == "/":
      charPrueba = textAreaInicial[i+1]
      if charPrueba == "*":
        verificador = True
        palabraAnalizar += char
        columnaInicial = columna
        i += 1
        while textAreaInicial[i] != '*' or textAreaInicial[i+1] != '/':
          if (i+1) == len(textAreaInicial):
            verificador = False
            break
          palabraAnalizar += textAreaInicial[i]
          i += 1
        if verificador == True:
          if i < len(textAreaInicial):
            palabraAnalizar += textAreaInicial[i]
            palabraAnalizar += textAreaInicial[i+1]
          listaLexemas.append(Lexema("Comentario multilínea", palabraAnalizar, "7", fila, columnaInicial))
          palabraAnalizar = ""
          columnaInicial += len(palabraAnalizar)
          i += 2
        else:
          listaErrores.append(Error("Error Sintáctico", f"Se esperaba: */", fila, columna))
      else:
        listaErrores.append(Error("Error Léxico", f"Carácter no válido: {char}", fila, columna))
        i += 1

    elif char == "-":
      charPrueba1 = ""
      charPrueba2 = ""
      if i != (len(textAreaInicial) - 2):
        charPrueba1 = textAreaInicial[i+1]
        charPrueba2 = textAreaInicial[i+2]
      if charPrueba1 == "-" and charPrueba2 == "-":
        palabraAnalizar += char
        columnaInicial = columna
        i += 1
        while i < len(textAreaInicial) and textAreaInicial[i] != '\n':
          palabraAnalizar += textAreaInicial[i]
          i += 1
        listaLexemas.append(Lexema("Comentario simple", palabraAnalizar, "8", fila, columnaInicial))
        palabraAnalizar = ""
        columnaInicial += len(palabraAnalizar)
        i += 1
      else:
        listaErrores.append(Error("Error Léxico", f"Carácter no válido: {char}", fila, columna))
        i += 1

    else:
      listaErrores.append(Error("Error Léxico", f"Carácter no válido: {char}", fila, columna))
      i += 1

  analizadorSintactico(listaLexemas, listaErrores, textAreaFinal)
  

  generarTablaLexemas(listaLexemas)