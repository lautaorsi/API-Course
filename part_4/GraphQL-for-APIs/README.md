# GraphQL

### ¿Qué es?

Es un lenguaje query para APIs que permite hacer solicitudes (_requests_) específicas evitando el over-fetching y mediante un único endpoint.

### Conceptos Fundamentales

GraphQL tiene 3 conceptos cruciales respecto a su arquitectura

1.  Esquema (_Schema_) 
    Define la estructura general de la API usando un lenguaje legíble y que además aporta definiciones sobre los tipos y campos de la información.

2.  Consultas (_Queries_)
    Similar a las solicitudes _GET_ de la arquitectura REST, esta operación no hace modificaciónes sobre la información en el servidor filtrando la información necesaria.

3.  Mutaciones (_Mutations_) 
    Una especie de agrupamiento de las solicitudes _POST_,_PUT_ y _DELETE_. Esta operación es específicamente para modificar la información del servidor que se corre de manera secuencial para evitar condiciones de carrera.

>   Extra: Las suscripciones (_subscriptions_) permiten obtener información en tiempo real

## Resolvers

Son funciones que se encargan de conectar el esquema con las bases de datos, actuando de handlers para queries y mutaciones. 

### Argumentos 

-   _parent_ 
    Contiene el resultado del resolver anterior, esto es útil para consultas anidadas. 
-   _args_
    Contiene la información necesaria para ejecutar las consultas/mutaciones.    
-   _context_
    Contiene las credenciales de autenticación necesarias para la conexión a la base de datos u operación 
-   _info_ 
    Contiene información sobre la ejecución de la consulta/mutación

## Suscripciones

Similar a los web sockets, permiten la comunicación en tiempo real entre servidor y cliente 

## Federación

Un metodo de escalado basado en combinar múltiples servicios GraphQL en una única API. Esto permite esquemas descentralizados y puntos de acceso unificados.  

## Técniacas de Escalado

-   Escalado Horizontal

    Correr múltiples servidores de GraphQL manejados por un orquestrador de cargas.

-   Federación

-   Rate Limiting

    Limitar la cantidad de consultas por un mismo cliente e impedir queries pesadas que bloquen al sistema.

## Cacheo y Manejo de Errores 

-   Cacheo
    -   Client-Side 

        Mantener la información consultada recientemente en el cliente. (Débil a ataques)

    -   Server-Side

        Mantener la información cacheada en el servidor.
        (Carga extra en el servidor pero más fuerte contra ataques)

    -   Field-Level

        Mantener la información en los resolvers, siempre y cuando la información cambie muy pocas veces.


-   Errores
    
    Siempre debemos devolver objetos JSON válidos y estructurados acorde al error para permitir debugging más sencillo y handleo adecuado por parte del cliente.

## Testing

-   Testeo Unitario de Resolvers

    Testear indivdualmente cada resolver para asegurar que tengan el comportamiento esperado

-   Testeo Integral

    Validar consultas y mutaciones en un servidor de prueba

-   Testeo End-to-End 

    Simular interacciones por parte de un cliente a la API

