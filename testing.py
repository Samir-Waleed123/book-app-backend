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

# upload library database form excel sheet like this schema 1	9036402	Spear, Robert J.	Introduction to computer programming in Visual Basic 4.0 /

import pandas as pd
import requests
import time

def upload_library_database(excel_file_path):
    url = "https://book-app-backend-production-304e.up.railway.app/library/add"
    headers = {"Content-Type": "application/json"}

    # Read Excel file (columns: [index, id, author, title])
    df = pd.read_excel(excel_file_path)
    
    print(f"\nTotal books in Excel: {len(df)}\n")

    for index, row in df.iterrows():
        # Extract data and replace NaN/empty values with "N/A"
        book_id = str(int(row[1])) if pd.notna(row[1]) else 0
        author = str(row[2]) if pd.notna(row[2]) else "N/A"
        title = str(row[3]) if pd.notna(row[3]) else "N/A"

        book = {
            "bookid": book_id,
            "author": author,
            "title": title
        }

        # Print the book data (for debugging)
        print(f"Book {index + 1}: {book}")

        try:
            response = requests.post(url, headers=headers, json=book)
            if response.status_code == 200:
                print(f"✅ Uploaded: {title}")
            else:
                print(f"❌ Failed (Status {response.status_code}): {title}\nResponse: {response.text}")
        except Exception as e:
            print(f"🚨 Error uploading '{title}': {str(e)}")
        
        time.sleep(0.3)  # Small delay to avoid rate-limiting

    print("\nAll books processed. Check logs for errors.\n")



if __name__ == "__main__":
    excel_file_path = "library_database.xlsx"  # Path to your Excel file
    upload_library_database(excel_file_path)
    
