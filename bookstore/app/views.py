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
