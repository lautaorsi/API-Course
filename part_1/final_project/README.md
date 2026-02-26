# Documentation

## Overview

This API provides access to the city's database (see [*database documentation*](./db/README.md) for schema).

Users will be able to look up, update, delete and add books and services to the database itself. Here you will find a list of [Endpoints](#endpoints), [Responses](#Responses) and [Examples](#Examples)

---

## Endpoints

The city's database consists of 2 tables, [*books*](./db/README.md/#books) and [*services*](./db/README.md/#services) we have thus created separate routes to ensure clear operational distinctions.

---

### Books

---

#### `GET /books`

Returns a list of all the (JSON-encoded) books available in the table.

---

#### `GET /books/<bookId>`

If existent, returns `200 OK` response with JSON object corresponding to the book where `book_id=bookId`.

```json
{
    "book": book
}
```

Otherwise response will be `404` with body:

```json
{
    "error": "Resource not found",
    "message": "Item with ID not found in the database"
}
```

---

#### `POST /books`

This endpoint adds a book to the *books* table.

If successful, returns an empty `201 Created` response.

Otherwise, if book is poorly formatted response will be `400` with body:

```json
{
    "error": "Bad request",
    "message": "Incorrect format"
}
```

Or if the book already exists, `409` response with body:

```json
{
    "error": "Conflict",
    "message": "Item already exists"
}
```

---

#### `DELETE /books/<bookId>`

This endpoint deletes the book where `book_id=bookId` from the *books* table.

If existent, returns an empty `200 OK` response.

Otherwise, a `404` response is sent with body:

```json
{
    "error": "Resource not found",
    "message": "Item with ID not found in the database"
}
```

---

#### `PATCH /books/<bookId>`

This endpoint updates the book where `book_id=bookId` from the *books* table. It must contain in its body the updated information in JSON format.

If existent, returns an empty `200 OK` response.

Otherwise, if new data is poorly formatted, response will be `400` with body:

```json
{
    "error": "Bad request",
    "message": "Incorrect format"
}
```

Or if the book is not found, `404` with body:

```json
{
    "error": "Resource not found",
    "message": "Item with ID not found in the database"
}
```

---

### Services

---

#### `GET /services`

Returns a list of all the (JSON-encoded) services available in the table.

---

#### `GET /services/<serviceId>`

If existent, returns `200 OK` response with JSON object corresponding to the service where `service_id=serviceId`.

```json
{
    "service": service
}
```

Otherwise response will be `404` with body:

```json
{
    "error": "Resource not found",
    "message": "Item with ID not found in the database"
}
```

---

#### `POST /services`

This endpoint adds a service to the *services* table.

If successful, returns an empty `201 Created` response.

Otherwise, if service is poorly formatted response will be `400` with body:

```json
{
    "error": "Bad request",
    "message": "Incorrect format"
}
```

Or if the service already exists, `409` response with body:

```json
{
    "error": "Conflict",
    "message": "Item already exists"
}
```

---

#### `DELETE /services/<serviceId>`

This endpoint deletes the service where `service_id=serviceId` from the *services* table.

If existent, returns an empty `200 OK` response.

Otherwise, a `404` response is sent with body:

```json
{
    "error": "Resource not found",
    "message": "Item with ID not found in the database"
}
```

---

#### `PATCH /services/<serviceId>`

This endpoint updates the service where `service_id=serviceId` from the *services* table. It must contain in its body the updated information in JSON format.

If existent, returns an empty `200 OK` response.

Otherwise, if new data is poorly formatted, response will be `400` with body:

```json
{
    "error": "Bad request",
    "message": "Incorrect format"
}
```

Or if the service is not found, `404` with body:

```json
{
    "error": "Resource not found",
    "message": "Item with ID not found in the database"
}
```

---

## Examples

-   Valid GET single book <br>
    -   Request: /books/B001
    -   Response: 
```json 
    {
        "book_id": "B001", 
        "isbn": "978-0-06-112008-4",
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": "Fiction",
        "publisher": "HarperCollins",
        "published_year": "1960",
        "price": "12.99",
        "stock_quantity": "45",
        "pages": "336",
        "language": "English",
        "rating": "4.8",
        "description": "A novel about racial injustice and childhood in the American South"
    }
```
-   Invalid PATCH book <br>
    -   Request: /books/B001
        >Body:{"language" : 45}
    -   Response: 
```json 
    {
        "error": "Bad request",
        "message": "Incorrect format"
    }
```
- DELETE sevice <br>
    -   Request: /services/CS015

    -   Response:
        > HEADER: 200 OK