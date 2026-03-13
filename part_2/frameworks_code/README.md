
## SETUP
Para correr los 3 proyectos debemos simplemente ejecutar el comando

```bash
docker-compose up --build
```
Esto se encarga automaticamente de instalar las dependencias y levantar los servidores de todos los codigos! 

**Ejemplo de acceso:** <br> Si ahora queremos -por ejemplo- obtener la lista de todos los cursos en cada framework deberiamos acceder a estos endpoints

-   [localhost:8080/api/v1/courses](http://localhost:8080/api/v1/courses) &rarr; Springboot
-   [localhost:3000/api/v1/courses](http://localhost:3000/api/v1/courses) &rarr; Node
-   [localhost:5000/api/v1/courses](http://localhost:5000/api/v1/courses) &rarr; Django

Notese que las primeras dos fallan dado que no

## Esquema de la database
| Column Name    | Data Type     | Constraints          | Example Value                |
| :------------- | :------------ | :------------------- | :--------------------------- |
| **course_id** | `INT`         | PRIMARY KEY, AI      | `1`                          |
| **course_title** | `VARCHAR(100)`| NOT NULL             | `Intro to Computer Science`  |
| **credits** | `DECIMAL`     | DEFAULT 3.0          | `4.0`                        |

--- 

**Importante:** <br>
La base de datos va a contener además una tabla predeterminada creada por Django.
Incluyo la base de datos en el repositorio dado que contiene simplemente 12 registros dummy para fines demostrativos
