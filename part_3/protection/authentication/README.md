# Autenticación de Usuarios

A la hroa de llevar una API a producción es importante tener una forma de controlar el acceso al servicio, es por esto que generalmente se implementa algún método de autenticación sobre el servicio, por ejemplo:


## Autenticación Básica

El método mas arcaico dentro de los nombrados, básicamente funciona con el principio de que cualquier request enviada por un usuario e estar acompañada por sus credenciales (usuario y contraseña en general). Esto es problematico en caso de ataques man-in-the-middle o comunicaciones no encriptadas como HTTP. 

## API KEYS

Es una llave única de acceso a la API que se envía en cada request, es más propensa a errores de usuario donde accidentalmente se divulga por no mantenerla en archivos '.env' pero particularmente útil en casos de comunicación entre máquinas.


## OAUTH 2.0

OAUTH permite a usuarios obtener acceso a servicios mediante sus cuentas de plataformas seguras, la idea esta en evitar enviar datos sensibles a terceros delegandole la seguridad a la plataforma. Generalmente lo que ocurre detras de escena es que dichas plataformas envian tokens de acceso con limitaciones específicas. 

## JWT

JWT básicamente permite al usuario obtener un token que luego envía al servidor cuando quiere realizar una request, este token contiene toda la información necesaria para que el servidor determine si el usuario tiene permitido el acceso. 