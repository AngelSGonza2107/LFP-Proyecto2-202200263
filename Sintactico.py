def imprimir(tituloEncabezado, listaElementos, textAreaFinal):
    textoFinal = ''
    
    htmlInicio = '''<!DOCTYPE html>
<html>
  <head>
    <meta charset="UTF-8">
'''
    
    html1 = '''  </head>
  <body>
    <br>
    <br>
    <br>
'''

                 
    htmlFinal = '''  </body>
</html> 
'''
    
    textoFinal += htmlInicio

    if tituloEncabezado != '':
        textoFinal += f'''    <title>
      {tituloEncabezado} 
    </title>
'''
    else:
        textoFinal += f'''    <title> 
      Página sin título 
    </title>
'''
    textoFinal += html1

    for i in range(len(listaElementos)):
      if "Fondo" in listaElementos[i].keys():
          colorFondo = listaElementos[i]["Fondo"]
          if colorFondo.startswith("#"):
              color = colorFondo
          else:
              coloresHTML = {
                  "rojo": "red",
                  "amarillo": "yellow",
                  "azul": "blue",
              }
              color = coloresHTML.get(colorFondo.lower(), "#FFFFFF")  # Por defecto blanco si no se encuentra el color
          textoFinal += f'''    <style>
      body {{
        background-color: {color};
      }}
    </style>
'''
      if "Negrita" in listaElementos[i].keys():
          textoNegrita = listaElementos[i]["Negrita"]
          textoFinal += f'    <strong>{textoNegrita}</strong>\n'
      if "Subrayado" in listaElementos[i].keys():
          textoSubrayado = listaElementos[i]["Subrayado"]
          textoFinal += f'    <u>{textoSubrayado}</u>\n'
      if "Tachado" in listaElementos[i].keys():
          textoTachado = listaElementos[i]["Tachado"]
          textoFinal += f'    <del>{textoTachado}</del>\n'
      if "Cursiva" in listaElementos[i].keys():
          textoCursiva = listaElementos[i]["Cursiva"]
          textoFinal += f'    <em>{textoCursiva}</em>\n'
      if "Salto" in listaElementos[i].keys():
          numeroSaltos = listaElementos[i]["Salto"]
          numeroSaltos = int(numeroSaltos)
          for saltos in range(numeroSaltos):
              textoFinal += f'    <br>\n'
      if "Titulo" in listaElementos[i].keys():
          textoTitulo = listaElementos[i]["Titulo"]["texto"]
          posicionTitulo = listaElementos[i]["Titulo"]["posicion"]
          tamanoTitulo = listaElementos[i]["Titulo"]["tamaño"]
          colorTitulo = listaElementos[i]["Titulo"]["color"]
          tamanoTitulo = tamanoTitulo.replace("t", "h")
          if colorTitulo.startswith("#"):
              color = colorTitulo
          else:
              coloresHTML = {
                  "rojo": "red",
                  "amarillo": "yellow",
                  "azul": "blue",
              }
              color = coloresHTML.get(colorTitulo.lower())
          if posicionTitulo == "izquierda":
              posicionTitulo = "left"
          elif posicionTitulo == "derecha":
              posicionTitulo = "right"
          elif posicionTitulo == "centro":
              posicionTitulo = "center"
          textoFinal += f'    <{tamanoTitulo} style="text-align: {posicionTitulo}; color: {color};">{textoTitulo}</{tamanoTitulo}>\n'
      if "Parrafo" in listaElementos[i].keys():
          textoParrafo = listaElementos[i]["Parrafo"]["texto"]
          posicionParrafo = listaElementos[i]["Parrafo"]["posicion"]
          if posicionParrafo == "izquierda":
              posicionParrafo = "left"
          elif posicionParrafo == "derecha":
              posicionParrafo = "right"
          elif posicionParrafo == "centro":
              posicionParrafo = "center"
          textoFinal += f'    <p style="text-align: {posicionParrafo};">{textoParrafo}</p>\n'
      if "Texto" in listaElementos[i].keys():
          textoTexto = listaElementos[i]["Texto"]["texto"]
          fuenteTexto = listaElementos[i]["Texto"]["fuente"]
          tamanoTexto = listaElementos[i]["Texto"]["tamaño"]
          colorTexto = listaElementos[i]["Texto"]["color"]
          tamanoTexto += "px"
          if colorTexto.startswith("#"):
              color = colorTexto
          else:
              coloresHTML = {
                  "rojo": "red",
                  "amarillo": "yellow",
                  "azul": "blue",
              }
              color = coloresHTML.get(colorTexto.lower())
          textoFinal += f'    <span style="font-family: {fuenteTexto}; color: {color}; font-size: {tamanoTexto};">{textoTexto}</span>\n'
      if "Codigo" in listaElementos[i].keys():
          textoCodigo = listaElementos[i]["Codigo"]["texto"]
          posicionCodigo = listaElementos[i]["Codigo"]["posicion"]
          if posicionCodigo == "izquierda":
              posicionCodigo = "left"
          elif posicionCodigo == "derecha":
              posicionCodigo = "right"
          elif posicionCodigo == "centro":
              posicionCodigo = "center"
          textoFinal += f'    <pre style="text-align: {posicionCodigo}; font-family: monospace;">{textoCodigo}</pre>\n'
      if "Tabla" in listaElementos[i].keys():
          tabla = listaElementos[i]["Tabla"]
          if "filas" in tabla and "columnas" in tabla:
              numFilas = tabla["filas"]
              numColumnas = tabla["columnas"]
              elementos = {}
              for elemento in tabla.get("elemento", []):
                  fila = elemento.get("fila")
                  columna = elemento.get("columna")
                  texto = elemento.get("texto")
                  elementos[(fila, columna)] = {"texto": texto}
              tablaHTML = "    <table>\n"
              for fila in range(int(numFilas)):
                  tablaHTML += "      <tr>\n"
                  for columna in range(int(numColumnas)):
                      elementoCelda = elementos.get((fila+1, columna+1))
                      if elementoCelda:
                          texto = elemento.get("texto", '')
                          tablaHTML += f"        <td> {texto} </td>\n"
                      else:
                          tablaHTML += f"        <td> </td>\n"
                  tablaHTML += "      </tr>\n"
              tablaHTML += "    </table>\n"
              textoFinal += tablaHTML
                    
    textoFinal += htmlFinal
    textAreaFinal.delete("1.0", "end")
    textAreaFinal.insert("end", textoFinal)
    
    
def analizadorSintactico(listaLexemas, textAreaFinal):
    listaElementos = []
    tituloEncabezado = ''
    for i in range(len(listaLexemas)):
        if listaLexemas[i].tipo == "Etiqueta Encabezado":
            tituloEncabezado =  listaLexemas[i+5].lexema
            tituloEncabezado = tituloEncabezado.replace('"', '')
        if listaLexemas[i].tipo == "Etiqueta Fondo":
            aux = {}
            fondoValor = listaLexemas[i+5].lexema
            aux[listaLexemas[i].lexema] = fondoValor.replace('"', '')
            listaElementos.append(aux)
        if listaLexemas[i].tipo == "Etiqueta Negrita":
            aux = {}
            negritaTexto = listaLexemas[i+5].lexema
            aux[listaLexemas[i].lexema] = negritaTexto.replace('"', '')
            listaElementos.append(aux)
        if listaLexemas[i].tipo == "Etiqueta Subrayado":
            aux = {}
            subrayadoTexto = listaLexemas[i+5].lexema
            aux[listaLexemas[i].lexema] = subrayadoTexto.replace('"', '')
            listaElementos.append(aux)
        if listaLexemas[i].tipo == "Etiqueta Tachado":
            aux = {}
            tachadoTexto = listaLexemas[i+5].lexema
            aux[listaLexemas[i].lexema] = tachadoTexto.replace('"', '')
            listaElementos.append(aux)
        if listaLexemas[i].tipo == "Etiqueta Cursiva":
            aux = {}
            cursivaTexto = listaLexemas[i+5].lexema
            aux[listaLexemas[i].lexema] = cursivaTexto.replace('"', '')
            listaElementos.append(aux)
        if listaLexemas[i].tipo == "Etiqueta Salto":
            aux = {}
            saltoTexto = listaLexemas[i+5].lexema
            aux[listaLexemas[i].lexema] = saltoTexto.replace('"', '')
            listaElementos.append(aux)
        if listaLexemas[i].tipo == "Etiqueta Titulo":
            aux = {}
            aux1 = {}
            clave = listaLexemas[i].lexema
            i += 1
            while listaLexemas[i].lexema != '}':
                if listaLexemas[i].lexema == "texto":
                    textoValor = listaLexemas[i+2].lexema
                    aux1[listaLexemas[i].lexema] = textoValor.replace('"', '')
                if listaLexemas[i].lexema == "posicion":
                    posicionValor = listaLexemas[i+2].lexema
                    aux1[listaLexemas[i].lexema] = posicionValor.replace('"', '')
                if listaLexemas[i].lexema == "tamaño":
                    tamanoValor = listaLexemas[i+2].lexema
                    aux1[listaLexemas[i].lexema] = tamanoValor.replace('"', '')
                if listaLexemas[i].lexema == "color":
                    colorValor = listaLexemas[i+2].lexema
                    aux1[listaLexemas[i].lexema] = colorValor.replace('"', '')
                i += 1
            aux[clave] = aux1
            listaElementos.append(aux)
        if listaLexemas[i].tipo == "Etiqueta Parrafo":
            aux = {}
            aux1 = {}
            clave = listaLexemas[i].lexema
            i += 1
            while listaLexemas[i].lexema != '}':
                if listaLexemas[i].lexema == "texto":
                    textoValor = listaLexemas[i+2].lexema
                    aux1[listaLexemas[i].lexema] = textoValor.replace('"', '')
                if listaLexemas[i].lexema == "posicion":
                    posicionValor = listaLexemas[i+2].lexema
                    aux1[listaLexemas[i].lexema] = posicionValor.replace('"', '')
                i += 1
            aux[clave] = aux1
            listaElementos.append(aux)
        if listaLexemas[i].tipo == "Etiqueta Texto":
            aux = {}
            aux1 = {}
            clave = listaLexemas[i].lexema
            i += 1
            while listaLexemas[i].lexema != '}':
                if listaLexemas[i].lexema == "texto":
                    textoValor = listaLexemas[i+2].lexema
                    aux1[listaLexemas[i].lexema] = textoValor.replace('"', '')
                if listaLexemas[i].lexema == "fuente":
                    fuenteValor = listaLexemas[i+2].lexema
                    aux1[listaLexemas[i].lexema] = fuenteValor.replace('"', '')
                if listaLexemas[i].lexema == "tamaño":
                    tamanoValor = listaLexemas[i+2].lexema
                    aux1[listaLexemas[i].lexema] = tamanoValor.replace('"', '')
                if listaLexemas[i].lexema == "color":
                    colorValor = listaLexemas[i+2].lexema
                    aux1[listaLexemas[i].lexema] = colorValor.replace('"', '')
                i += 1
            aux[clave] = aux1
            listaElementos.append(aux)
        if listaLexemas[i].tipo == "Etiqueta Codigo":
            aux = {}
            aux1 = {}
            clave = listaLexemas[i].lexema
            i += 1
            while listaLexemas[i].lexema != '}':
                if listaLexemas[i].lexema == "texto":
                    textoValor = listaLexemas[i+2].lexema
                    aux1[listaLexemas[i].lexema] = textoValor.replace('"', '')
                if listaLexemas[i].lexema == "posicion":
                    posicionValor = listaLexemas[i+2].lexema
                    aux1[listaLexemas[i].lexema] = posicionValor.replace('"', '')
                i += 1
            aux[clave] = aux1
            listaElementos.append(aux)
        if listaLexemas[i].tipo == "Etiqueta Tabla":
            aux = {}
            aux1 = {}
            elementos = []
            clave = listaLexemas[i].lexema
            i += 1
            while not (listaLexemas[i-1].lexema == ';' and listaLexemas[i].lexema == '}'):
                if listaLexemas[i].lexema == "filas":
                    filaValor = listaLexemas[i+2].lexema
                    aux1[listaLexemas[i].lexema] = filaValor.replace('"', '')
                if listaLexemas[i].lexema == "columnas":
                    columnaValor = listaLexemas[i+2].lexema
                    aux1[listaLexemas[i].lexema] = columnaValor.replace('"', '')
                if listaLexemas[i].lexema == "elemento":
                    aux2 = {}
                    filaElementoValor = listaLexemas[i+5].lexema
                    aux2["fila"] = int(filaElementoValor.replace('"', ''))
                    columnaElementoValor = listaLexemas[i+9].lexema
                    aux2["columna"] = int(columnaElementoValor.replace('"', ''))
                    textoElementoValor = listaLexemas[i+11].lexema
                    aux2["texto"] = textoElementoValor.replace('"', '')
                    elementos.append(aux2)
                    aux1[listaLexemas[i].lexema] = elementos
                i += 1
            aux[clave] = aux1
            listaElementos.append(aux)

    imprimir(tituloEncabezado, listaElementos, textAreaFinal)