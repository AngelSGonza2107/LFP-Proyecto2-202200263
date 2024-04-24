from Error import Error
from TablaErrores import *

def imprimir(listaElementos, textAreaFinal):
    textoFinal = ''

    for i in range(len(listaElementos)):
      if "CrearBD" in listaElementos[i].keys():
          nombreBD = listaElementos[i]["CrearBD"]
          textoFinal += f'use(\'{nombreBD}\');\n\n'
      if "EliminarBD" in listaElementos[i].keys():
          textoFinal += 'db.dropDatabase();\n\n'
      if "CrearColeccion" in listaElementos[i].keys():
          nombreColeccion = listaElementos[i]["CrearColeccion"]
          textoFinal += f'db.createCollection(\'{nombreColeccion}\');\n\n'
      if "EliminarColeccion" in listaElementos[i].keys():
          nombreColeccionDel = listaElementos[i]["EliminarColeccion"]
          textoFinal += f'db.{nombreColeccionDel}.drop();\n\n'
      if "BuscarTodo" in listaElementos[i].keys():
          buscarColTodo = listaElementos[i]["BuscarTodo"]
          textoFinal += f'db.{buscarColTodo}.find();\n\n'
      if "BuscarUnico" in listaElementos[i].keys():
          buscarColUnico = listaElementos[i]["BuscarUnico"]
          textoFinal += f'db.{buscarColUnico}.findOne();\n\n'
      if "InsertarUnico" in listaElementos[i].keys():
          nombreInsert = listaElementos[i]["InsertarUnico"]["nombreColeccion"]
          jsonInsert = listaElementos[i]["InsertarUnico"]["JSON"]
          textoFinal += f'db.{nombreInsert}.insertOne({jsonInsert});\n\n'
      if "ActualizarUnico" in listaElementos[i].keys():
          nombreInsert = listaElementos[i]["ActualizarUnico"]["nombreColeccion"]
          jsonInsert = listaElementos[i]["ActualizarUnico"]["JSON"]
          textoFinal += f'db.{nombreInsert}.updateOne({jsonInsert});\n\n'
      if "EliminarUnico" in listaElementos[i].keys():
          nombreInsert = listaElementos[i]["EliminarUnico"]["nombreColeccion"]
          jsonInsert = listaElementos[i]["EliminarUnico"]["JSON"]
          textoFinal += f'db.{nombreInsert}.deleteOne({jsonInsert});\n\n'

    textAreaFinal.delete("1.0", "end")
    textAreaFinal.insert("end", textoFinal)
    
    
def analizadorSintactico(listaLexemas, listaErrores, textAreaFinal):
    listaElementos = []
    if listaLexemas[0].lexema != "CrearBD":
       listaErrores.append(Error("Error Sintáctico", f"Se necesita crear una base de datos", 1, 1))
    else:
      for i in range(len(listaLexemas)):
          if listaLexemas[i].tipo == "Etiqueta crear base de datos" and listaLexemas[i+1].lexema != "(":
            if listaLexemas[i+2].lexema == "=" and listaLexemas[i+3].lexema == "nueva" and (listaLexemas[i+4].lexema == listaLexemas[i].lexema) and listaLexemas[i+5].lexema == "(" and listaLexemas[i+6].lexema == ")" and listaLexemas[i+7].lexema == ";":
              aux = {}
              nombreBD = listaLexemas[i+1].lexema
              nombreBD = nombreBD.replace('”', '')
              aux[listaLexemas[i].lexema] = nombreBD.replace('“', '')
              listaElementos.append(aux)
            else:
              listaErrores.append(Error("Error Sintáctico", f"Se esperaba un comando válido", listaLexemas[i].fila, listaLexemas[i].columna))
          if listaLexemas[i].tipo == "Etiqueta eliminar base de datos" and listaLexemas[i+1].lexema != "(":
            if listaLexemas[i+2].lexema == "=" and listaLexemas[i+3].lexema == "nueva" and (listaLexemas[i+4].lexema == listaLexemas[i].lexema) and listaLexemas[i+5].lexema == "("  and listaLexemas[i+6].lexema == ")" and listaLexemas[i+7].lexema == ";":
              aux = {}
              nombreEliminarBD = listaLexemas[i+1].lexema
              aux[listaLexemas[i].lexema] = nombreEliminarBD
              listaElementos.append(aux)
            else:
              listaErrores.append(Error("Error Sintáctico", f"Se esperaba un comando válido", listaLexemas[i].fila, listaLexemas[i].columna))
          if listaLexemas[i].tipo == "Etiqueta crear colección" and listaLexemas[i+1].lexema != "(":
            if listaLexemas[i+2].lexema == "=" and listaLexemas[i+3].lexema == "nueva" and (listaLexemas[i+4].lexema == listaLexemas[i].lexema) and listaLexemas[i+5].lexema == "(" and listaLexemas[i+7].lexema == ")" and listaLexemas[i+8].lexema == ";":
              aux = {}
              nombreColeccion = listaLexemas[i+6].lexema
              nombreColeccion = nombreColeccion.replace('”', '')
              aux[listaLexemas[i].lexema] = nombreColeccion.replace('“', '')
              listaElementos.append(aux)
            else:
              listaErrores.append(Error("Error Sintáctico", f"Se esperaba un comando válido", listaLexemas[i].fila, listaLexemas[i].columna))
          if listaLexemas[i].tipo == "Etiqueta eliminar colección" and listaLexemas[i+1].lexema != "(":
            if listaLexemas[i+2].lexema == "=" and listaLexemas[i+3].lexema == "nueva" and (listaLexemas[i+4].lexema == listaLexemas[i].lexema) and listaLexemas[i+5].lexema == "(" and listaLexemas[i+7].lexema == ")" and listaLexemas[i+8].lexema == ";":
              aux = {}
              nombreColeccionDel = listaLexemas[i+6].lexema
              nombreColeccionDel = nombreColeccionDel.replace('”', '')
              aux[listaLexemas[i].lexema] = nombreColeccionDel.replace('“', '')
              listaElementos.append(aux)
            else:
              listaErrores.append(Error("Error Sintáctico", f"Se esperaba un comando válido", listaLexemas[i].fila, listaLexemas[i].columna))
          if listaLexemas[i].tipo == "Etiqueta buscar todos los registros" and listaLexemas[i+1].lexema != "(":
            if listaLexemas[i+2].lexema == "=" and listaLexemas[i+3].lexema == "nueva" and (listaLexemas[i+4].lexema == listaLexemas[i].lexema) and listaLexemas[i+5].lexema == "(" and listaLexemas[i+7].lexema == ")" and listaLexemas[i+8].lexema == ";":
              aux = {}
              buscarColTodo = listaLexemas[i+6].lexema
              buscarColTodo = buscarColTodo.replace('”', '')
              aux[listaLexemas[i].lexema] = buscarColTodo.replace('“', '')
              listaElementos.append(aux)
            else:
              listaErrores.append(Error("Error Sintáctico", f"Se esperaba un comando válido", listaLexemas[i].fila, listaLexemas[i].columna))
          if listaLexemas[i].tipo == "Etiqueta buscar registro simple" and listaLexemas[i+1].lexema != "(":
            if listaLexemas[i+2].lexema == "=" and listaLexemas[i+3].lexema == "nueva" and (listaLexemas[i+4].lexema == listaLexemas[i].lexema) and listaLexemas[i+5].lexema == "(" and listaLexemas[i+7].lexema == ")" and listaLexemas[i+8].lexema == ";":
              aux = {}
              buscarColUnico = listaLexemas[i+6].lexema
              buscarColUnico = buscarColUnico.replace('”', '')
              aux[listaLexemas[i].lexema] = buscarColUnico.replace('“', '')
              listaElementos.append(aux)
            else:
              listaErrores.append(Error("Error Sintáctico", f"Se esperaba un comando válido", listaLexemas[i].fila, listaLexemas[i].columna))
          if listaLexemas[i].tipo == "Etiqueta insertar registro" and listaLexemas[i+1].lexema != "(":
            if listaLexemas[i+2].lexema == "=" and listaLexemas[i+3].lexema == "nueva" and (listaLexemas[i+4].lexema == listaLexemas[i].lexema) and listaLexemas[i+5].lexema == "(" and listaLexemas[i+7].lexema == "," and listaLexemas[i+9].lexema == ")" and listaLexemas[i+10].lexema == ";":
                aux = {}
                aux1 = {}
                nombreColInsert = listaLexemas[i+6].lexema
                nombreColInsert = nombreColInsert.replace('”', '')
                aux1["nombreColeccion"] = nombreColInsert.replace('“', '')
                jsonColInsert = listaLexemas[i+8].lexema
                jsonColInsert = jsonColInsert.replace('”', '')
                jsonColInsert = jsonColInsert.replace('\n', '')
                jsonColInsert = jsonColInsert.replace('\t', ' ')
                aux1["JSON"] = jsonColInsert.replace('“', '')
                aux[listaLexemas[i].lexema] = aux1
                listaElementos.append(aux)
            else:
              listaErrores.append(Error("Error Sintáctico", f"Se esperaba un comando válido", listaLexemas[i].fila, listaLexemas[i].columna))
          if listaLexemas[i].tipo == "Etiqueta actualizar registro" and listaLexemas[i+1].lexema != "(":
            if listaLexemas[i+2].lexema == "=" and listaLexemas[i+3].lexema == "nueva" and (listaLexemas[i+4].lexema == listaLexemas[i].lexema) and listaLexemas[i+5].lexema == "(" and listaLexemas[i+7].lexema == "," and listaLexemas[i+9].lexema == ")" and listaLexemas[i+10].lexema == ";":
                aux = {}
                aux1 = {}
                nombreColUpdate = listaLexemas[i+6].lexema
                nombreColUpdate = nombreColUpdate.replace('”', '')
                aux1["nombreColeccion"] = nombreColUpdate.replace('“', '')
                jsonColUpdate = listaLexemas[i+8].lexema
                jsonColUpdate = jsonColUpdate.replace('”', '')
                jsonColUpdate = jsonColUpdate.replace('\n', '')
                jsonColUpdate = jsonColUpdate.replace('\t', ' ')
                aux1["JSON"] = jsonColUpdate.replace('“', '')
                aux[listaLexemas[i].lexema] = aux1
                listaElementos.append(aux)
            else:
              listaErrores.append(Error("Error Sintáctico", f"Se esperaba un comando válido", listaLexemas[i].fila, listaLexemas[i].columna))
          if listaLexemas[i].tipo == "Etiqueta eliminar registro" and listaLexemas[i+1].lexema != "(":
            if listaLexemas[i+2].lexema == "=" and listaLexemas[i+3].lexema == "nueva" and (listaLexemas[i+4].lexema == listaLexemas[i].lexema) and listaLexemas[i+5].lexema == "(" and listaLexemas[i+7].lexema == "," and listaLexemas[i+9].lexema == ")" and listaLexemas[i+10].lexema == ";":
                aux = {}
                aux1 = {}
                nombreColDelete = listaLexemas[i+6].lexema
                nombreColDelete = nombreColDelete.replace('”', '')
                aux1["nombreColeccion"] = nombreColDelete.replace('“', '')
                jsonColDelete = listaLexemas[i+8].lexema
                jsonColDelete = jsonColDelete.replace('”', '')
                jsonColDelete = jsonColDelete.replace('\n', '')
                jsonColDelete = jsonColDelete.replace('\t', ' ')
                aux1["JSON"] = jsonColDelete.replace('“', '')
                aux[listaLexemas[i].lexema] = aux1
                listaElementos.append(aux)
            else:
              listaErrores.append(Error("Error Sintáctico", f"Se esperaba un comando válido", listaLexemas[i].fila, listaLexemas[i].columna))

    if len(listaErrores) == 0:
      imprimir(listaElementos, textAreaFinal)
    else:
      textAreaFinal.delete("1.0", "end")
      textAreaFinal.insert("end", "---------------- Error de compilación ----------------\n")
      textAreaFinal.insert("end", " Lista de Errores\n")
      textAreaFinal.insert("end", "\n")
      numError = 1
      for error in listaErrores:
        textAreaFinal.insert("end", f" {numError}. {error.mensaje}, Fila: {error.fila}, Columna: {error.columna}\n")
        numError += 1
    
    generarTablaErrores(listaErrores)