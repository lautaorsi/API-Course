# OAUTH 

En este mini código tenemos un caso de uso de OAUTH via Github para otorgar acceso a usuarios sin solicitar ni manejar credenciales por parte del servidor. <br>
Esta "aplicación" es reproducible utilizando los siguientes comandos:

- `docker build -t oauth .` *Construimos la imagen* <br>
- `docker run -d -p 3000:3000 --name oauth oauth:latest` *Levantamos el contenedor y conectamos los puertos*

> Estos comandos solo funcionan si tenemos docker instalado y estamos parados en la ruta `./oauth`

Algo interesante para ver es como determinamos que información del usuario le solicitamos a la plataforma (la cual luego delega la decisión al usuario) para usar después.


