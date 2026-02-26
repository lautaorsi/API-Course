from flask import Flask, jsonify, request
import db.functions as db
app = Flask(__name__)


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




@app.get("/books")
def books_return():
    return db.select("*","books")

@app.get("/books/<bookId>")
def book_search(bookId):
    book = db.select("*","books",f"WHERE book_id='{bookId}'")
    if len(book) == 0:
        return not_found, 404
    else:
        return jsonify({"book":book[0]}), 200

@app.post("/books")
def book_add():
    book = request.get_json()
    rows_modified = db.insert("books",book)
    if rows_modified == -1:
        return bad_request, 400
    if rows_modified == 0:
        return conflict, 409 
    
    return {"message": "Success"}, 201

@app.delete("/books/<bookId>")
def book_remove(bookId):
    rows_modified = db.remove("books",f"book_id='{bookId}'")
    if rows_modified:
        return {"message": "Success"}, 200
    else:
        return not_found, 404

@app.patch("/books/<bookId>")
def book_update(bookId):
    data = request.get_json()
    rows_modified = db.update("books",f"book_id='{bookId}'",data)
    if rows_modified == 0:
        return not_found, 404
    if rows_modified == -1:
        return bad_request, 400
    else:
        return {"message": "Success"}, 200




@app.get("/services")
def services_return():
    return db.select("*","services")

@app.get("/services/<serviceId>")
def service_search(serviceId):
    service = db.select("*","services",f"WHERE service_id='{serviceId}'")
    if len(service) == 0:
        return not_found, 404
    else:
        return jsonify({"service":service}), 200

@app.post("/services/<service>")
def service_add(service):
    rows_modified = db.insert("services",service)
    if rows_modified == -1:
        return bad_request, 400
    if rows_modified == 0:
        return conflict, 409 
    
    return 201

@app.delete("/services/<serviceId>")
def service_remove(serviceId):
    rows_modified = db.remove("services",f"service_id='{serviceId}'")
    if rows_modified:
        return {"message": "Success"}, 200
    else:
        return not_found, 404

@app.patch("/services/<serviceId>")
def service_update(serviceId):
    data = request.get_json()
    rows_modified = db.update("services",f"service_id='{serviceId}'",data)
    if rows_modified == 0:
        return not_found, 404
    if rows_modified == -1:
        return bad_request, 400
    else:
        return {"message": "Success"}, 200


if __name__ == '__main__':
    app.run(debug=True)