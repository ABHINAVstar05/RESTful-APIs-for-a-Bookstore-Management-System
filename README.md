# RESTful-APIs-for-a-Bookstore-Management-System
**FarmwiseAI - backend**

## Setup
*Follow the below commands in terminal for a successful setup*

```
python3 -m venv virtual_env

virtual_env/Scripts/activate

python -m pip install django

python -m pip install -r requirements.txt

django-admin startproject bookstore

cd bookstore

python manage.py startapp app

python manage.py runserver
```

## Overview:
Developed RESTful APIs using Python-Django for *bookstore management system* which allows users to add, retrieve, update, and delete book information.

### Database Design:
![BookStore DB](https://github.com/ABHINAVstar05/RESTful-APIs-for-a-Bookstore-Management-System/assets/75786072/981a1ab8-c3e2-4152-a278-bb4591031aa0)

### APIs

1. API endpoint for adding a new book.
2. API endpoint for retrieving all books.
3. API endpoint for retrieving a specific book by ISBN.
4. API endpoint for updating book details.
5. API endpoint for deleting a book.

* API endpoint for adding a new book.

  On adding a new book successfully.
  ![POSTMAN add_book success](https://github.com/ABHINAVstar05/RESTful-APIs-for-a-Bookstore-Management-System/assets/75786072/068ac794-ac9f-427d-95ed-218151c7e2d8)

  On adding an already existing book.
  ![POSTMAN add_book already exists](https://github.com/ABHINAVstar05/RESTful-APIs-for-a-Bookstore-Management-System/assets/75786072/cb36795b-9cf5-4a28-9b68-c69d8c045b09)


* API endpoint for retrieving all books.
 
  ![POSTMAN get_all_books](https://github.com/ABHINAVstar05/RESTful-APIs-for-a-Bookstore-Management-System/assets/75786072/0faecca3-ee87-4146-a059-2fc5b3861c73)


* API endpoint for retrieving a specific book by ISBN.

  On searching for an existing book
  ![POSTMAN get_specific success](https://github.com/ABHINAVstar05/RESTful-APIs-for-a-Bookstore-Management-System/assets/75786072/03ef7536-1be0-4efd-abc4-ed086df47f3a)

  On searching for a non-existing book
  ![POSTMAN get_specific not_found](https://github.com/ABHINAVstar05/RESTful-APIs-for-a-Bookstore-Management-System/assets/75786072/0e518db4-cc3f-40ac-bbb4-d1b19bfbf9ab)


* API endpoint for updating book details.

  On successfully updating a book details
  ![POSTMAN update success](https://github.com/ABHINAVstar05/RESTful-APIs-for-a-Bookstore-Management-System/assets/75786072/f268812c-59c1-4581-95ec-0f73f9159716)


* API endpoint for deleting a book.

  On deleting an existing book
  ![POSTMAN delete success](https://github.com/ABHINAVstar05/RESTful-APIs-for-a-Bookstore-Management-System/assets/75786072/d6996f0b-f530-4ecf-989f-d7edd059a0e2)

  On deleting a non-existing book
  ![POSTMAN delete not_found](https://github.com/ABHINAVstar05/RESTful-APIs-for-a-Bookstore-Management-System/assets/75786072/2fb73a7b-edc3-4631-9f23-c0fad3df5e0d)


### Authentication: Implemented a basic authentication to restrict access to certain endpoints based on user role (Owner or Customers)

1. A customer cannot add a book.
2. A customer cannot update any book details.
3. A customer cannot delete any book.

* A customer cannot add a book.
  ![POSTMAN add_book cust auth](https://github.com/ABHINAVstar05/RESTful-APIs-for-a-Bookstore-Management-System/assets/75786072/271c1dbb-a168-4f6e-a8c5-5ba5404399b8)

* A customer cannot update any book details.
  ![POSTMAN update auth](https://github.com/ABHINAVstar05/RESTful-APIs-for-a-Bookstore-Management-System/assets/75786072/611e2ae8-de85-490f-a161-4840f840ff59)

* A customer cannot delete any book.
  ![POSTMAN delete auth](https://github.com/ABHINAVstar05/RESTful-APIs-for-a-Bookstore-Management-System/assets/75786072/acf5ffe8-4125-4408-8da0-d6ef228baee0)


### Testing 
*Kindly have a look at tests.py*
