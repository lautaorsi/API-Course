
## SETUP
Para correr los 3 proyectos debemos simplemente ejecutar el comando

```bash
docker-compose up --build
```
Esto se encarga automaticamente de instalar las dependencias y levantar los servidores de todos los codigos!



## Esquema de la database
| Column Name    | Data Type     | Constraints          | Example Value                |
| :------------- | :------------ | :------------------- | :--------------------------- |
| **course_id** | `INT`         | PRIMARY KEY, AI      | `1`                          |
| **subject** | `VARCHAR(10)` | NOT NULL             | `CS101`                      |
| **title** | `VARCHAR(100)`| NOT NULL             | `Intro to Computer Science`  |
| **credits** | `DECIMAL`     | DEFAULT 3.0          | `4.0`                        |
| **description**| `TEXT`        | -                    | `Fundamentals of programming`|
| **professor** | `VARCHAR(100)`| -                    | `Dr. Alan Turing`            |
| **capacity** | `INT`         | DEFAULT 30           | `50`                         |

--- 

**Importante:** <br>
La base de datos va a contener además una tabla predeterminada creada por Django.
Incluyo la base de datos en el repositorio dado que contiene simplemente 12 registros dummy para fines demostrativos
