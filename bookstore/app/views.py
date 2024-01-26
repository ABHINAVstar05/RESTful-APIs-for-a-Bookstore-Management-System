# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

from app.models import *
from app.serializers import *

# Create your views here.

  
"""
** API endpoint for adding a new book. ** 
used to add new books to the database.
"""

@api_view(['POST', ])
def addBook(request) :
    data = request.data
    deserialized = bookDetailsSerializer(data = data)
    if deserialized.is_valid() :
        deserialized.save()
        return Response({'Message' : 'Book with the below details added successfully.', 'Details': deserialized.data})
    else :
        return Response(deserialized.errors)
        
    
"""
** API endpoint for retrieving all books. **
used to retrieve information of all books stored in the database.
"""

@api_view(['GET', ])
def retrieveAllBooks(request) :
    books = bookDetails.objects.all()
    serialized = bookDetailsSerializer(books, many = True)
    return Response(serialized.data)


"""
** API endpoint for retrieving specific book. **
used to retrieve a specific book by its ISBN number.
"""
@api_view(['POST', ])
def retrieveSpecificBook(request) :
    data = request.data
    isbn = data['ISBN']
    
    if bookDetails.objects.filter(ISBN = isbn) :
        obj = bookDetails.objects.get(ISBN = isbn)
        serialized = bookDetailsSerializer(obj)
        return Response({'Book details corresponding to the given ISBN number are' : serialized.data})
        
    return Response({'message': 'No book found having given ISBN number.'})


"""
** API endpoint for updating book details. **
used to updating book details by its ISBN number.
"""
@api_view(['PUT', ])
def updateBookDetails(request) :
    data = request.data
    isbn = data['ISBN']

    if bookDetails.objects.filter(ISBN = isbn) :
        obj = bookDetails.objects.get(ISBN = isbn)
        serialized = bookDetailsSerializer(obj, data)
        
        if serialized.is_valid() :
            serialized.save()
            return Response({'Data updated successfully' : serialized.data})
        
        return Response(serialized.errors)
        
    return Response({'message': 'No book found having given ISBN number.'})


"""
** API endpoint for deleting a book. **
used to delete a book by its ISBN number.
"""
@api_view(['DELETE', ])
def deleteBook(request) :
    data = request.data
    isbn = data['ISBN']

    try :
        obj = bookDetails.objects.get(ISBN = isbn)
        obj.delete()
        return Response({'Message': 'Book deleted successfully.'})
    
    except bookDetails.DoesNotExist :
        errorMessage = 'Book with given ISBN number does not exist.'
        return Response(errorMessage)
