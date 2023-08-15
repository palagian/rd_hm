import pytest
from unittest.mock import patch
from views import *

@pytest.fixture
def client():
    return app.test_client()

@patch('views', {'username': 'testuser'})
def test_home(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'home.html' in response.data

@patch('views', {'username': 'testuser'})
def test_get_users(client):
    response = client.get('/users')
    assert response.status_code == 200
    assert b'users.html' in response.data

@patch('views', {'username': 'testuser'})
def test_get_books(client):
    response = client.get('/books')
    assert response.status_code == 200
    assert b'books.html' in response.data

@patch('views', {'username': 'testuser'})
def test_get_user(client):
    user_id = 1
    response = client.get(f'/users/{user_id}')
    assert response.status_code == 200
    assert b'users_id.html' in response.data

@patch('views', {'username': 'testuser'})
def test_get_book(client):
    book_id = 1
    response = client.get(f'/books/{book_id}')
    assert response.status_code == 200
    assert b'books_id.html' in response.data

@patch('views', {'username': 'testuser'})
def test_get_purchases(client):
    response = client.get('/purchases')
    assert response.status_code == 200
    assert b'purchases.html' in response.data

@patch('views', {'username': 'testuser'})
def test_get_purchase(client):
    purchase_id = 1
    response = client.get(f'/purchases/{purchase_id}')
    assert response.status_code == 200
    assert b'purchases_id.html' in response.data