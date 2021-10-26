# DevOps Technical Test
## GENERAL QUESTIONS
- You will be in charge of running a set of JVM-based microservices connected to MongoDB, exchanging messages through a kafka broker and communicating with external clients using HTTP Restful Services











- Provide a Linux command to delete all files which have been accessed between 20 and 30 days ago. Explain your command.


## PRACTICAL SCENARIO
## DESCRIPCIÓN DE LA APLICACION
- Se solicito desarrollar un aplicativo que genere un numero aleatorio de archivos entre 10-20 en cada ejecución.
- El nombre de los archivos se debe generar de manera aleatoria preferiblmente sin sobreescribir los archivos existentes.
- Los archivos deben escribirse con caracteres aleatorios con un numero de caracteres entre 1K y 5K.
- Al final se debe imprimir un resumen de tamñano y bytes escritos.

## IMPLEMENTACIÓN
### Para implementar el aplicativo descrito anteriormente se hará de la siguiente manera:
1. Presentación del script en python que modela el aplicativo.
2. Contenedor corriendo con nginx que saca los archivos generados por el script.
3. Conversion de los programas en servicios a través de la tecnología de contenedores de Docker.
4. Como ejecutar de manera periodica el script (1 minuto) se realizará a traves del servicio cron.
5. Descripción del docker.compose.yml que permité que todos servicios se ejecuten de forma orquestada y se desarrolle la aplicación de manera operacional.
