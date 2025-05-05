## upload the books to the database

import requests
import json
import os 
import time


def upload_books_to_db():
    url = "https://book-app-backend-production-304e.up.railway.app/books/add"
    headers = {
        "Content-Type": "application/json"
    }

    with open("books_data.json", "r") as file:
        books_data = json.load(file)
    
    print(f"Number of books to upload: {len(books_data)}")

    for book in books_data:
        response = requests.post(url, headers=headers, json=book)  # Use `json=` instead of `data=`
        if response.status_code == 200:
            print(f"Uploaded book: {book['title']}")
        else:
            print(f"Failed to upload book: {book['title']}, Status Code: {response.status_code}, Response: {response.text}")
        time.sleep(1)  # Optional delay

    print("All books processed.")

if __name__ == "__main__":
    upload_books_to_db()
