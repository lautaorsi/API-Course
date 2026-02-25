# SCHEMA

Acá presento el esquema usado en la base de datos, todos los campos deben ser not-null.

* [books](#books)
* [services](#services)

---


## books

| Column | Data Type |
| :--- | :--- |
|"book_id" |TEXT (UNIQUE)|
|"isbn" |TEXT|
|"title" |TEXT|
|"author" |TEXT|
|"genre" |TEXT |
|"publisher" |TEXT |
|"published_year" |TEXT |
|"price" |TEXT|
|"stock_quantity" |TEXT |
|"pages" |TEXT |
|"language" |TEXT |
|"rating" |TEXT|
|"description"|TEXT|


## services
| Column Name | Data Type |
| :--- | :--- |
| service_id | TEXT |
| name | TEXT |
| category | TEXT |
| address | TEXT |
| district | TEXT |
| city | TEXT |
| zip_code | TEXT |
| latitude | TEXT |
| longitude | TEXT |
| phone | TEXT |
| email | TEXT |
| opening_hours | TEXT |
| capacity | TEXT |
| current_occupancy | TEXT |
| is_accessible | TEXT |
| parking_available | TEXT |
| rating | TEXT |
| status | TEXT |
| last_updated | TEXT |
| description | TEXT |

