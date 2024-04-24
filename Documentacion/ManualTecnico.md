# Laboratorio de Lenguajes Formales y de Programación B-

### Primer Semestre 2024

```js
Universidad San Carlos de Guatemala
Programador: Angel Samuel González Velásquez
Carne: 202200263
Correo: angelprogonza2107@gmail.com
```

---

## Manual Técnico del Proyecto No. 2

### Interfaz Gráfica

En el archivo .py principal se utiliza la librería TKinter para crear y modificar la interfaz gráfica del programa, esta interfaz gráfica se compone básicamente de solo 2 ventanas, una para la carátula que muestra información básica pero importante del programa, y otra para el propio traductor.
Para esto se necesitó importar la librería TKinter y la propiedad “filedialog” y “messagebox” para poder utilizar el selector de archivos y los mensajes de texto en caja de la misma librería.

![Intefaz Gráfica](https://i.ibb.co/n628ZK4/image.png)
![Intefaz Gráfica](https://i.ibb.co/4dWsq3g/image.png)

### Analizadores

Para poder realizar estas clases se tuvo que seguir un proceso antes, es decir, para la creación de la clase del analizador léxico se tuvo que realizar primero un autómata finito, el cual se adjunta en este mismo manual, para así poder organizar y analizar correctamente cada carácter dentro del archivo de entrada, y así localizar patrones, lexemas o posibles errores dentro de este. Y luego, para la realización del analizador sintáctico se necesito seguir la estructura de una gramática libre de contexto, y así verificar el orden de los lexemas del archivo de entrada.

**Analizador Léxico**
![Analizador Lexico](https://i.ibb.co/vvbzvwK/image.png)
![Analizador Lexico](https://i.ibb.co/D8cGpMY/image.png)

**Analizador Sintáctico**
![Analizador Lexico](https://i.ibb.co/TKmVh3z/image.png)
![Analizador Lexico](https://i.ibb.co/8X9h4Fg/image.png)

### Traducción

Para realizar la traducción, se analiza la lista de lexemas y su orden, para poder encontrar todos las instrucciones que contiene el archivo de entrada y así poder almacenar las propiedades dentro de un diccionario, y así, instrucción por instrucción, añadir las líneas dentro de una cadena, y finalmente, imprimir esta cadena final en el área de texto correspondiente.

![Traducción](https://i.ibb.co/2dVbYy4/image.png)

### Reportes

Para generar las tablas de reportes se tuvo que crear una clase específica para cada tipo de tabla, tanto para los lexemas, como también para la tabla de errores recopilados por el programa. Y luego, en un archivo HTML, se detalló cada una de estas tablas.

**Tabla de Lexemas**

![Tabla de Lexemas](https://i.ibb.co/x6KGwQZ/image.png)
![Tabla de Lexemas](https://i.ibb.co/SJWQ8g0/image.png)

**Tabla de Errores**

![Tabla de Errores](https://i.ibb.co/G2MBhbp/image.png)
![Tabla de Errores](https://i.ibb.co/h2g3qzJ/image.png)

### Tabla de Tokens

| No  |       Token        |                                                                       Valor                                                                        |
| :-: | :----------------: | :------------------------------------------------------------------------------------------------------------------------------------------------: |
|  1  | palabrasReservadas | {"CrearBD", "EliminarBD", "CrearColeccion", "EliminarColeccion", "InsertarUnico", "ActualizarUnico", "EliminarUnico", "BuscarTodo", "BuscarUnico"} |
|  2  |   signosValidos    |                                                              {"., ",", ":", "{", "}"}                                                              |
|  3  |       igual        |                                                                       {"="}                                                                        |
|  4  |      P_abrir       |                                                                       {"("}                                                                        |
|  5  |      P_cerrar      |                                                                       {")"}                                                                        |
|  6  |      C_abrir       |                                                                       {"“"}                                                                        |
|  7  |      C_cerrar      |                                                                       {"”"}                                                                        |
|  8  |     puntoComa      |                                                                       {";"}                                                                        |
|  8  |        coma        |                                                                       {","}                                                                        |
|  9  |       nueva        |                                                                     {"nueva"}                                                                      |
| 10  |  signosNoValidos   |                                 {“!”, “¡”, “#”, “%”, “&”, “/”, “?”, “¿”, “\_”, “>”, “<”, “`”, “+”, “´”, “'”, “^”}                                  |
| 11  |      alfanum       |                                                                    [0-9a-zA-Z]                                                                     |

### Autómata Finito

![AFD](https://i.ibb.co/7jWxS3z/image.png)
![AFD](https://i.ibb.co/zG9mshW/image.png)

### Gramática Libre de contexto

![Gramatica Libre](https://i.ibb.co/jH39ryg/image.png)
