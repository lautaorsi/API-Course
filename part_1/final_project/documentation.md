# Documentation

## Overview

This API provides access to the city's database (see [*database documentation*](./db/README.md) for schema).

Users will be able to look up, update, delete and add books and services to the database itself. Here you will find a list of [Endpoints](#endpoints), [Responses](#Responses), [Examples](#Examples) and [Testing](#Testing)

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
    "message": "Book with ID bookId was not found in the database"
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
    "message": "Incorrect book format"
}
```

Or if the book already exists, `409` response with body:

```json
{
    "error": "Conflict",
    "message": "Book already exists"
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
    "message": "Book with ID bookId was not found in the database"
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
    "message": "Incorrect data format"
}
```

Or if the book is not found, `404` with body:

```json
{
    "error": "Resource not found",
    "message": "Book was not found in the database"
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
    "message": "Service with ID serviceId was not found in the database"
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
    "message": "Incorrect service format"
}
```

Or if the service already exists, `409` response with body:

```json
{
    "error": "Conflict",
    "message": "Service already exists"
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
    "message": "Service with ID serviceId was not found in the database"
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
    "message": "Incorrect data format"
}
```

Or if the service is not found, `404` with body:

```json
{
    "error": "Resource not found",
    "message": "Service was not found in the database"
}
```

---

## Error Handling

## Examples

## Testing Instructions