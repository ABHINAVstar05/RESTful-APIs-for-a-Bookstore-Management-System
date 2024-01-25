from django.db import models

# Create your models here.

"""  
Model to define structure of table for storing book details in the DB.
"""
class bookDetails(models.Model) :
    ISBN = models.IntegerField(primary_key = True)
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    price = models.FloatField()
    quantity = models.IntegerField()
    
    def __str__(self):
        return f"{self.title} -by ({self.author})"
    
    
"""  
Model to define structure of table for storing user details in the DB.
"""
class users(models.Model) :

    ROLE_CHOICES = [
        ('Owner', 'Owner'),
        ('Customers', 'Customers'),
    ]

    name = models.CharField(max_length = 100)
    role = models.CharField(max_length = 20, choices = ROLE_CHOICES)

    def __str__(self):
        return f"{self.name} ({self.role})"