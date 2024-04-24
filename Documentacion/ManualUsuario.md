# Laboratorio de Lenguajes Formales y de Programación B-

### Primer Semestre 2024

```js
Universidad San Carlos de Guatemala
Programador: Angel Samuel González Velásquez
Carne: 202200263
Correo: angelprogonza2107@gmail.com
```

---

## Manual de Usuario del Proyecto No. 2

Este manual de usuario le explicará el uso del programa, el cual se diseñó con el fin de poder realizar traducciones a un formato de NoSQL teniendo como entradas instrucciones simples en un archivo “.txt”. Con una interfaz sencilla e intuitiva, el usuario podrá seleccionar el archivo base o de entrada, archivo en donde deberá de ingresar las instrucciones para poder realizar la traducción al lenguaje NoSQL, para luego utilizarlo en MongoDB.
De igual forma, al presionar el botón de “Compilar” en el programa, no solo se estará realizando la traducción de forma inmediata en un cuadro de texto dentro del mismo programa, sino también se generarán reportes con los lexemas y errores que pueda traer el archivo de entrada. Estos dos reportes se crearán dentro de la carpeta donde está guardado el programa, y serán archivos html que podrán ser visualizados dentro del navegador de su preferencia.

### Carátula

Al inicial el programa se muestra una pequeña pantalla de carátula a modo de presentación en donde se indica el nombre del estudiante, el carné del estudiante, y finalmente el nombre del curso. Y simplemente se debe presionar "Abrir Compilador" para continuar a la siguiente pantalla.

![Carátula](https://i.ibb.co/VxFdZ2T/image.png)

### Carga del archivo de entrada

Cuando el usuario presione el botón de cargar o “Seleccionar archivo”, este podrá elegir el archivo de entrada que desee traducir, es importante mencionar que solo se permitirán archivos de tipo “.txt”.

![Carga del archivo de entrada](https://i.ibb.co/rsJCRS0/image.png)

### Guardar en nuevo archivo

Si se edita, o simplemente se ingresa texto directamente desde el area de texto, es posible guardar las instrucciones ingresadas en un archivo ".txt", para luego volver a usar estas instrucciones en una futura oportunidad, simplemente se necesita presionar en el botón "Guardar". Siempre y cuando haya texto en el area de texto se podrá guardar este texto en un archivo.

![Guardar en nuevo archivo](https://i.ibb.co/YbtmQj5/image.png)

### Realizar traducción

Cuando el usuario haya cargado el archivo, este podrá comenzar la traducción al dar click en el botón de “Compilar”. Esta opción analiza el contenido mediante un autómata finito previamente definido, y posteriormente organizará la información para poder realizar la traducción a HTML de forma correcta.

![Realizar traducción](https://i.ibb.co/3C08T7k/image.png)

### Reportes

Como ya se ha mencionado, al dar click sobre el botón de “Compilar” no solo se realiza la traducción instantánea, sino también se crean dos archivos “.html” dentro de la carpeta donde se encuentra el programa. Estos reportes mostrarán todos los lexemas y errores encontrados y analizados en el archivo de entrada.

![Reportes](https://i.ibb.co/kSRJ6Y2/image.png)
![Reportes](https://i.ibb.co/XVTfxWr/image.png)
![Reportes](https://i.ibb.co/tK57PJ6/image.png)
![Reportes](https://i.ibb.co/wKjwvDS/image.png)

### Recomendaciones

A continuación, se presentarán las recomendaciones antes de comenzar a utilizar el programa, así como también los archivos compatibles por el programa para los datos de entrada:

- Se le recomienda leer el manual detenidamente antes de comenzar a utilizar el programa
- Se le recomienda seguir las instrucciones que muestra el programa en pantalla, estas son intuitivas y simples
- Se le recomienda realizar distintas pruebas para entender bien las funcionalidades del programa
- Se le recomienda verificar detenidamente el documento de entrada, si es que el programa muestra un fallo en la compilación
