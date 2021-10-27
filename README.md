# DevOps Technical Test
## GENERAL QUESTIONS
- You will be in charge of running a set of JVM-based microservices connected to MongoDB, exchanging messages through a kafka broker and communicating with external clients using HTTP Restful Services











- Provide a Linux command to delete all files which have been accessed between 20 and 30 days ago. Explain your command.
Para realizar la tarea propuesta una alternativa propia de UNIX es utilizar el comando find con sus opciones:

**`find / -atime 10 -atime 30 -delete `** 
or

**`find / -atime 10 -atime 30 -exec rm {} \`**

- atime n
              File was last accessed n*24 hours ago.  When find figures out how many 24-hour periods ago the file was last accessed, any frac‐
              tional part is ignored, so to match -atime +1, a file has to have been accessed at least two days ago.
			  
			  
- delete
              Delete files; true if removal succeeded.  If the removal failed, an error message is issued.  If -delete fails, find's exit sta‐
              tus will be nonzero (when it eventually exits).  Use of -delete automatically turns on the `-depth' option.

- exec command {} +
              This  variant  of  the -exec action runs the specified command on the selected files, but the command line is built by appending
              each selected file name at the end; the total number of invocations of the command will be much less than the number of  matched
              files.   The  command  line is built in much the same way that xargs builds its command lines.  Only one instance of `{}' is al‐
              lowed within the command, and (when find is being invoked from a shell) it should be quoted (for example, '{}')  to  protect  it
              from  interpretation by shells.  The command is executed in the starting directory.  If any invocation with the `+' form returns
              a non-zero value as exit status, then find returns a non-zero exit status.  If find encounters  an  error,  this  can  sometimes
              cause an immediate exit, so some pending commands may not be run at all.  This variant of -exec always returns true.


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
