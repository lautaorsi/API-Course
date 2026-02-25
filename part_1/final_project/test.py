import pytest
from app import app

valid_new_book = {
    "book_id": "B840",
    "isbn": "978-0141183848",
    "title": "Ficciones",
    "author": "Jorge Luis Borges",
    "genre": "Philosophical Fiction",
    "publisher": "Penguin Classics",
    "published_year": "1944",
    "price": "15.50",
    "stock_quantity": "25",
    "pages": "210",
    "language": "Spanish",
    "rating": "4.9",
    "description": "A mind-bending collection of short stories featuring labyrinths, infinite libraries, and philosophical puzzles."
}


invalid_new_book_invalid_field = {
    "book_id": "B840",
    "isbn": "978-0141183848",
    "title": "Ficciones",
    "author": "Jorge Luis Borges",
    "last_bought": "24/2/2026",
    "description": "A mind-bending collection of short stories featuring labyrinths, infinite libraries, and philosophical puzzles."
}

invalid_new_book_null_attributes = {
    "book_id": "B840",
    "isbn": "978-0141183848",
    "title": "Ficciones",
    "author": "Jorge Luis Borges",
    "description": "A mind-bending collection of short stories featuring labyrinths, infinite libraries, and philosophical puzzles."
}

existing_book = {
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

not_found=({
    "error": "Resource not found",
    "message": "Item with ID was not found in the database"
    })

bad_request=({
    "error": "Bad request",
    "message": "Incorrect format"
})

conflict=({
    "error": "Conflict",
    "message": "Item already exists"
})



@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_crud(client):

    # GET existent single book returns book
    response = client.get("/books/B001")
    body = response.get_json()
    assert body["book"][0] == existing_book
    assert response.status_code == 200

    # GET non-existent single book returns 404
    response = client.get("/books/B840")
    body = response.get_json()
    assert response.status_code == 404
    assert body == not_found



    # POST valid book returns correct status
    response = client.post("/books", json=valid_new_book)
    client.delete("/books/B840")
    assert response.status_code == 201
    
    # POST valid book is added to database
    client.post("/books", json=valid_new_book)
    response = client.get("/books/B840")
    body = response.get_json()
    assert body["book"][0] == valid_new_book
    assert response.status_code == 200

    # POST already existing book fails
    client.post("/books", json=valid_new_book)
    response = client.post("/books", json=valid_new_book)
    body = response.get_json()
    assert response.status_code == 409
    assert body == conflict


    # POST malformatted book fails, extra attributes
    response = client.post("/books", json=invalid_new_book_invalid_field)
    body = response.get_json()
    assert response.status_code == 400
    assert body == bad_request

    # POST malformatted book fails, empty attributes
    response = client.post("/books", json=invalid_new_book_null_attributes)
    body = response.get_json()
    assert response.status_code == 400
    assert body == bad_request

    # DELETE existing book
    response = client.delete("/books/B840")
    assert response.status_code == 200

    # DELETE non-existing book fails
    response = client.delete("/books/B840")
    body = response.get_json()
    assert response.status_code == 404
    assert body == not_found


    # PATCH existing book successfull
    modification = {"stock_quantity":"44"}
    response = client.patch("/books/B001", json=modification)
    assert response.status_code == 200

    # PATCH existing book modifies db
    response = client.get("/books/B001")
    body = response.get_json()
    book = body["book"][0]
    assert book["stock_quantity"] == "44" 

