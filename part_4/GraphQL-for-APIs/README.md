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

