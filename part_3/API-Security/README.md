# Protección de APIs

Dentro de la protección de las APIs tenemos una gama de elementos a tener en cuenta, entre ellos:


# Autenticación de Usuarios

A la hora de llevar una API a producción es importante tener una forma de controlar el acceso al servicio, es por esto que generalmente se implementa algún método de autenticación sobre el servicio, por ejemplo:


- ### Autenticación Básica 
    El método mas arcaico dentro de los nombrados, básicamente funciona con el principio de que cualquier request enviada por un usuario e estar acompañada por sus credenciales (usuario y contraseña en general). Esto es problematico en caso de ataques man-in-the-middle o comunicaciones no encriptadas como HTTP. 

- ### LLaves API 
    Es una llave única de acceso a la API que se envía en cada request, es más propensa a errores de usuario donde accidentalmente se divulga por no mantenerla en archivos '.env' pero particularmente útil en casos de comunicación entre máquinas.


- ### OAUTH 2.0
    OAUTH permite a usuarios obtener acceso a servicios mediante sus cuentas de plataformas seguras, la idea esta en evitar enviar datos sensibles a terceros delegandole la seguridad a la plataforma. Generalmente lo que ocurre detras de escena es que dichas plataformas envian tokens de acceso con limitaciones específicas. 

- ### JWT
    JWT básicamente permite al usuario obtener un token que luego envía al servidor cuando quiere realizar una request, este token contiene toda la información necesaria para que el servidor determine si el usuario tiene permitido el acceso. 

# Autorización

Una parte fundamental del manejo de API's (y servicios en general) es el principio de autorización mínima requerida, la idea es básicamente limitar a cualquier usuario con acceso a la API para que tenga los mínimos permisos requeridos para realizar su labor. Obviamente manejar ese _least privilege_ no es trivial en empresas de gran escala o cuando tenemos contextos cambiantes. Es por esto que existen métodos de roles tales como:

- ### Control de Acceso Basado en Roles (RBAC en inglés)
    Los permisos estan ligados a roles y el usuario hereda dichos permisos en base a su rol, esto facilita el otorgamiento agrupado de permisos, acelerando procesos. <br>
    Por otro lado una gran ventaja que aporta es el claro mapeo 1 a 1 con el dominio, esto permite que se le pueda delegar la carga de actualizar los roles de usuarios sin necesidad de un conocimiento técnico muy elevado. <br>
    Por último, algo que es interesante también es la idea de implementaciones jerárquicas, esto le agrega un grado de estructura a los roles para evitar ser repetitivos y agilizar procesos.

- ### Control de Acceso Basado en Atributos (ABAC en inglés)
    Los permisos basados en atributos tienen la particularidad de estar ligados al contexto de la acción y no únicamente a quien la realiza (a diferencia de RBAC). Esto pérmite un hilado más fino en el otorgamiento de permisos para situaciones específicas, por ejemplo uno podría tener el escenario en el cual un usuario puede acceder a un archivo únicamente estando conectado desde una máquina en la oficina (y no vía _home office_) por lo tanto habría que poder diferenciar esos dos casos de simplemente ser un usuario "permitido".

> En general no es que se implementa uno u otro, sino que se parte de RBAC para un prototipado rápido y sencillo y despues se extiende el hilado fino mediante ABAC.



# Encriptado

Encriptar la información sensible que maneja la empresa es fundamental y un no-brainer de cualquier negocio serio. No solo es crucial el encriptado para poder enviar esta data via canales públicos e internet, si no que además es indispensable para almacenar en las propias bases de datos sin riesgo a que sean accedidos por actores maliciosos. <br>
> Protocolos como HTTPS para comunicaciones, encriptados simétricos/asimétricos, verificaciones hash y ZKPfs son los pilares de las buenas prácticas de seguridad, permitiendo que las empresas funcionen sin riesgos legales y acatando normativas de menjo de información sensible. 



# Amenazas

Siempre es importante tener una idea de que tipos de amenazas nos podemos encontrar cuando trabajamos con APIs y el manejo de información, estas abarcan distintos ejes de impacto y con consecuencias de diferentes indoles. 

- ## Ataques técnicos

    -   **Ataque de Inyección**  <br>
            Este tipo de ataques se dan principalmente en el contexto de consultas a bases de datos, lo que se explota es la falta de sanitización de inputs de usuario para combinar caracteres que rompan el funcionamiento normal del servidor a fin de obtener registros confidenciales o modificar valores. Esto se puede solucionar utilizando sanitizaciones o inputs predefindos. 

    -   **Man-In-The-Middle** <br>
            Los ataques de Man in the Middle se centran en robar datos comunicados por canales comprometidos o no encriptados, un tercero ajeno a la comunicación recibe la información y puede o no alterarla en el transcurso sin que ninguna de las partes se entere. Esto en general se evita utilizando encriptados de extremo a extremo, cifrado simétrico/asimétrico y comunicación via HTTPS.

    -   **DoS** <br>
            Los ataques DoS o Denial of Service son los más enfocados en APIs, tienen como objetivo saturar al servidor para impedir que requests legítimas sean procesadas. Esto es particularmente difícil de evitar si los atacantes emplean máquinas zombies o descentralizadas desde distintos puntos geográficos. Algunas de las técnicas para disuadir este tipo de ataques son bloqueo de IPs y cooldown de requests.

- ## Ataques Sociales o User Error

    Si bien en general uno tiende a pensar en los hackeos como el mayor punto débil de una empresa, la mayo problematica a la que se enfrenta es el user error (en particular si la empresa no esta centrada en software y no toda su fuerza de trabajo esta capacitada en aspectos informáticos). Dentro de los vectores de ataque tenemos:

    -   **Estafas** <br>
            Phishing, chantaje o imitacion de personas en posiciones de poder
        
    -   **Errores de Usuario** <br>
            Contraseñas débiles o deducibles, compartir información sensible, dejar dispositivos sin asegurar, no eliminar correctamente información o desechar dispositivos que contienen datos sensibles.

    
