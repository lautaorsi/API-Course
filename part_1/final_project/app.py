from flask import Flask, jsonify, request
import db.functions as db
app = Flask(__name__)

@app.get("/books")
def books_return():
    return db.select("*","books")

@app.get("/books/<bookId>")
def book_search(bookId):
    book = db.select("*","books",f"WHERE book_id='{bookId}'")
    return book

@app.post("/books/<book>")
def book_add(book):
    db.insert("books",book)
    return book

@app.delete("/books/<bookId>")
def book_remove(bookId):
    return db.remove("books",f"book_id='{bookId}'")

@app.patch("/books/<bookId>")
def book_update(bookId):
    data = request.get_json()
    return db.update("books",f"book_id='{bookId}'",data)


@app.get("/services")
def services_return():
    return db.select("*","services")

@app.get("/services/<serviceId>")
def service_search(serviceId):
    service = db.select("*","services",f"WHERE service_id='{serviceId}'")
    return service

@app.post("/services/<service>")
def service_add(service):
    db.insert("services",service)
    return service

@app.delete("/services/<serviceId>")
def service_remove(serviceId):
    return db.remove("services",f"service_id='{serviceId}'")

@app.patch("/services/<serviceId>")
def service_update(serviceId):
    data = request.get_json()
    return db.update("services",f"service_id='{serviceId}'",data)



if __name__ == '__main__':
    app.run(debug=True)