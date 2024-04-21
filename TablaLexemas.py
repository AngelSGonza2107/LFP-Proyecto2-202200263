def generarTablaLexemas(listaLexemas):
    
    encabezado = '''
        <!DOCTYPE html>
        <html>
        <head>
	      <meta charset="UTF-8">
	      <title>Tabla de Lexemas</title>
        <link rel="stylesheet" type="text/css" href="estilo.css">
        </head>
        <body>
        <h1> TABLA DE LEXEMAS </h1>
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
            <th scope="col"> # </th>
            <th align=center scope="col"> Token </th>
            <th align=center scope="col"> No. Token </th>
            <th align=center scope="col"> Lexema </th>
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
    
    file = open('TablaLexemas.html', "w", encoding='utf-8')
    file.write(encabezado)
    file.write(tabla)
    
    contadorFila = 1
    for lexema in listaLexemas:      
        fila = f'''
                   <tr>
                   <th scope="row"> {contadorFila} </th>
                   <td align=center> {lexema.tipo} </td>
                   <td align=center> {lexema.noLex} </td>
                   <td align=center> {lexema.lexema} </td>
                   <td align=center> {lexema.fila} </td>
                   <td align=center> {lexema.columna} </td>
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