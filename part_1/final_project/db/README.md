# SCHEMA

Acá presento el esquema usado en la base de datos

* [books](#books)
* [services](#services)
* [book_orders](#book_orders)
* [service_events](#service_events)

---


## books

| Column | Data Type |
| :--- | :--- |
|"book_id" |TEXT|
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

## book_orders
| Column Name | Data Type |
| :--- | :--- |
| order_id | TEXT |
| customer_id | TEXT |
| customer_name | TEXT |
| customer_email | TEXT |
| book_id | TEXT |
| book_title | TEXT |
| quantity | TEXT |
| unit_price | TEXT |
| total_price | TEXT |
| order_date | TEXT |
| status | TEXT |
| shipping_address | TEXT |
| payment_method | TEXT |
| tracking_number | TEXT |

## service_events
| Column Name | Data Type |
| :--- | :--- |
| event_id | TEXT |
| service_id | TEXT |
| service_name | TEXT |
| event_type | TEXT |
| timestamp | TEXT |
| old_value | TEXT |
| new_value | TEXT |
| triggered_by | TEXT |
| description | TEXT |