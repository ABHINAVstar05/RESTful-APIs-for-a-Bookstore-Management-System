from django.test import TestCase, Client
from app.models import bookDetails, users

class BookAPITestCase(TestCase):

    def setUp(self):
        # Create test user 'Owner'
        self.owner = users.objects.create(name='Test Owner', role='Owner')

        # Create a test book
        self.test_book_data = {
            'ISBN': 12345,
            'title': 'Test Book',
            'author': 'Test Author',
            'price': 100,
            'quantity': 10,
        }
        self.test_book = bookDetails.objects.create(**self.test_book_data)

        # Create a test client
        self.client = Client()

    def test_add_book(self):
        # Test addBook endpoint
        add_book_data = {
            'ISBN': 9876543210,
            'title': 'Another Test Book',
            'author': 'Another Test Author',
            'price': 29.99,
            'quantity': 5,
            'user': 'Owner',
        }
        response = self.client.post('/api/add_book/', data=add_book_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['Message'], 'Book with the below details added successfully.')

    def test_retrieve_all_books(self):
        # Test retrieveAllBooks endpoint
        response = self.client.get('/api/get_all_books/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json()) > 0)

    def test_retrieve_specific_book(self):
        # Test retrieveSpecificBook endpoint
        retrieve_specific_book_data = {'ISBN': 1234567890}
        response = self.client.post('/api/get_specific_book/', data=retrieve_specific_book_data)
        self.assertEqual(response.status_code, 200)
        self.assertIn('Test Book', response.json()['Book details corresponding to the given ISBN number are']['title'])

    def test_update_book_details(self):
        # Test updateBookDetails endpoint
        update_book_data = {
            'ISBN': 1234567890,
            'title': 'Updated Test Book',
            'author': 'Updated Test Author',
            'price': 29.99,
            'quantity': 5,
            'user': 'Owner',
        }
        response = self.client.put('/api/update_book_details/', data=update_book_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['Data updated successfully']['title'], 'Updated Test Book')

    def test_delete_book(self):
        # Test deleteBook endpoint
        delete_book_data = {
            'ISBN': 1234567890,
            'user': 'Owner',
        }
        response = self.client.delete('/api/delete_book/', data=delete_book_data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['Message'], 'Book deleted successfully')

    def tearDown(self):
        # Clean up test data
        users.objects.all().delete()
        bookDetails.objects.all().delete()
