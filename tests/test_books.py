from tests import client

BASE_URL = "/api/v1/books"  # ✅ This must match settings.API_PREFIX

def test_get_all_books():
    response = client.get(f"{BASE_URL}/")  # ✅ Corrected path
    assert response.status_code == 200
    assert len(response.json()) == 3

def test_get_single_book():
    response = client.get(f"{BASE_URL}/1")  # ✅ Corrected path
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "The Hobbit"
    assert data["author"] == "J.R.R. Tolkien"

def test_create_book():
    new_book = {
        "id": 4,
        "title": "Harry Potter and the Sorcerer's Stone",
        "author": "J.K. Rowling",
        "publication_year": 1997,
        "genre": "Fantasy",
    }
    response = client.post(f"{BASE_URL}/", json=new_book)  # ✅ Corrected path
    assert response.status_code == 201
    data = response.json()
    assert data["id"] == 4
    assert data["title"] == "Harry Potter and the Sorcerer's Stone"

def test_update_book():
    updated_book = {
        "id": 1,
        "title": "The Hobbit: An Unexpected Journey",
        "author": "J.R.R. Tolkien",
        "publication_year": 1937,
        "genre": "Fantasy",
    }
    response = client.put(f"{BASE_URL}/1", json=updated_book)  # ✅ Corrected path
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "The Hobbit: An Unexpected Journey"

def test_delete_book():
    response = client.delete(f"{BASE_URL}/3")  # ✅ Corrected path
    assert response.status_code == 204

    response = client.get(f"{BASE_URL}/3")  # ✅ Corrected path
    assert response.status_code == 404
