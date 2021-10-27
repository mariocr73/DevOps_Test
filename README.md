# DevOps Technical Test
## GENERAL QUESTIONS
- You will be in charge of running a set of JVM-based microservices connected to MongoDB, exchanging messages through a kafka broker and communicating with external clients using HTTP Restful Services.
### Teniendo en cuenta la arquitectura de microservicios se pueden monitorear varios componentes.
### Monitoreo de Kafka
Cada mensaje de Kafka tiene una compensación. La compensación es básicamente un identificador que señala dónde se encuentra el mensaje en la secuencia de mensajes. Los productores agregan mensajes a los temas, y cada uno recibe una compensación nueva. La compensación más reciente en una partición muestra la ID más reciente. Los consumidores reciben los mensajes de los temas, y la diferencia entre la compensación más reciente y la compensación que recibe el consumidor es el retraso del consumidor. Indefectiblemente, los consumidores estarán un poco por detrás de los productores. A lo que se debe prestar atención es a cuando el retraso del consumidor aumenta sin fin, debido a que esto indica que probablemente necesitas más consumidores para procesar la carga.
Se puede por tanto utilizar algunas herramientas para revisar metricas como Metribeat y Filebeat para los logs.
Tambien con herramientas opensource como ELK (ElasticSearch, Logstash y Kibana.

![Esta es una imagen] (https://dc722jrlp2zu8.cloudfront.net/media/cache/ac/fb/acfb8540e183c26ce471e0370d80d470.webp)

### Monitoreo de microservicios basados en JVM
Teniendo en cuenta la arquitectura de microservicios basados en JVM es importante realizar un monitoreo del cluster donde corren y una solución Open Source puede ser  Stagemonitor, con el puede ver los datos históricos o en directo del clúster o del servidor de desarrollo, crear alertas personalizadas y establecer umbrales para cada métrica de JVM. También permite crear cuadros de mando personalizados para visualizar y analizar las métricas.

### Monitoreo de MongoDB
Finalmente y no menos importante monitorear el motor de bases de datos MongoDB, que incluyen:
- Estadísticas de desempeño
- Uso de recursos (uso de CPU, memoria disponible y uso de red)
- Estadísticas de afirmación
- Estadísticas de reproducción
- Saturación de recursos
- Operaciones de rendimiento

- Provide a Linux command to delete all files which have been accessed between 20 and 30 days ago. Explain your command.
Para realizar la tarea propuesta una alternativa propia de UNIX es utilizar el comando find con sus opciones:

**`find / -atime 20 -atime 30 -delete `** 
or

**`find / -atime 20 -atime 30 -exec rm {} \`**

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
