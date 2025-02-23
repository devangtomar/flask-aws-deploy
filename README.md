# Flask REST API

## Overview

This is a simple Flask-based REST API that allows CRUD operations on an `items` collection. The API supports multiple HTTP methods including `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, and `OPTIONS`.

## Endpoints

### 1. Home

**Endpoint:** `/`
**Method:** `GET`

- Returns a welcome message.

#### Example Request:

```sh
curl http://127.0.0.1:5000/
```

#### Example Response:

```json
{ "message": "Welcome to the API" }
```

---

### 2. Get All Items

**Endpoint:** `/items`
**Method:** `GET`

- Returns all stored items.

#### Example Request:

```sh
curl http://127.0.0.1:5000/items
```

#### Example Response:

```json
{}
```

---

### 3. Get a Specific Item

**Endpoint:** `/items/<item_id>`
**Method:** `GET`

- Retrieves an item by its `item_id`.

#### Example Request:

```sh
curl http://127.0.0.1:5000/items/1
```

#### Example Response:

```json
{ "name": "Item 1", "price": 100 }
```

---

### 4. Create a New Item

**Endpoint:** `/items`
**Method:** `POST`
**Payload:** JSON object containing item details.

#### Example Request:

```sh
curl -X POST http://127.0.0.1:5000/items \
    -H "Content-Type: application/json" \
    -d '{"name": "NewItem", "price": 200}'
```

#### Example Response:

```json
{ "id": "1", "data": { "name": "NewItem", "price": 200 } }
```

---

### 5. Update an Item (Full Update)

**Endpoint:** `/items/<item_id>`
**Method:** `PUT`
**Payload:** JSON object containing updated details.

#### Example Request:

```sh
curl -X PUT http://127.0.0.1:5000/items/1 \
    -H "Content-Type: application/json" \
    -d '{"name": "Updated Item", "price": 300}'
```

#### Example Response:

```json
{ "id": "1", "data": { "name": "Updated Item", "price": 300 } }
```

---

### 6. Update an Item (Partial Update)

**Endpoint:** `/items/<item_id>`
**Method:** `PATCH`
**Payload:** JSON object with partial updates.

#### Example Request:

```sh
curl -X PATCH http://127.0.0.1:5000/items/1 \
    -H "Content-Type: application/json" \
    -d '{"price": 250}'
```

#### Example Response:

```json
{ "id": "1", "data": { "name": "Updated Item", "price": 250 } }
```

---

### 7. Delete an Item

**Endpoint:** `/items/<item_id>`
**Method:** `DELETE`

- Deletes an item by `item_id`.

#### Example Request:

```sh
curl -X DELETE http://127.0.0.1:5000/items/1
```

#### Example Response:

```json
{ "message": "Item deleted" }
```

---

### 8. Get Allowed Methods for an Item

**Endpoint:** `/items/<item_id>`
**Method:** `OPTIONS`

- Returns allowed methods for an item.

#### Example Request:

```sh
curl -X OPTIONS http://127.0.0.1:5000/items/1
```

#### Example Response:

```json
{ "methods": ["GET", "POST", "PUT", "PATCH", "DELETE", "OPTIONS"] }
```

## Running the API

### Install Dependencies

```sh
pip install flask
```

### Run the Application

```sh
python app.py
```

The API will be accessible at `http://127.0.0.1:5000/`.
