def generarTablaErrores(listaErrores):
    
    encabezado = '''
        <!DOCTYPE html>
        <html>
        <head>
	      <meta charset="UTF-8">
	      <title>Tabla de Errores</title>
        <link rel="stylesheet" type="text/css" href="estilo.css">
        </head>
        <body>
        <h1> TABLA DE ERRORES </h1>
        <h3>Nombre: Angel Samuel González Velásquez</h3><br>
        <h3>Carnet: 202200263</h3><br>
        <br>
        <br>
        <br>
        '''
    
    tabla = '''
            <table class="table table-hover">
            <thead>
            <tr>
            <th align=center scope="col"> # </th>
            <th align=center scope="col"> Tipo de Error </th>
            <th align=center scope="col"> Mensaje </th>
            <th align=center scope="col"> Fila </th>
            <th align=center scope="col"> Columna </th>
            </tr>
            </thead>
            <tbody>
            '''
             
    final = ''' 
           </body>
           </html> 
            '''
    
    file = open('TablaErrores.html', "w", encoding='utf-8')
    file.write(encabezado)
    file.write(tabla)
    
    contadorFila = 1
    for error in listaErrores:      
        fila = f'''
                   <tr>
                   <th align=left scope="row"> {contadorFila} </th>
                   <td align=center> {error.tipo} </td>
                   <td align=center> {error.mensaje} </td>
                   <td align=right> {error.fila} </td>
                   <td align=right> {error.columna} </td>
                   </tr>
               '''
        file.write(fila)   
        contadorFila +=1
   
    finalTabla = '''
                    </tbody>
                    </table>
                 '''
       
    file.write(finalTabla)      
  
    file.write(final)
    file.close()