from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Book, Review


# Create your tests here.
class BookTests(TestCase):

    user = None
    book = None

    @classmethod
    def setUpTestData(cls):
        # The class-level atomic block described above allows the creation of initial data at the class level,
        # once for the whole TestCase.
        cls.user = get_user_model().objects.create_user(username="reviewuser", email="reviewuser@email.com", password="testpass123")
        cls.book = Book.objects.create(title='Harry Potter', author='J.K. Rowling', price='25.00')
        cls.review = Review.objects.create(book=cls.book, author=cls.user, review="An excellent review")

    def test_book_listing(self):
        self.assertEqual(f'{self.book.title}', 'Harry Potter')
        self.assertEqual(f'{self.book.author}', 'J.K. Rowling')
        self.assertEqual(f'{self.book.price}', '25.00')

    def test_book_list_view(self):
        response = self.client.get(reverse('book_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Harry Potter')
        self.assertTemplateUsed(response, 'books/book_list.html')

    def test_book_detail_view(self):
        response = self.client.get(self.book.get_absolute_url())
        no_response = self.client.get("/books/12345/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Harry Potter")
        self.assertContains(response, "An excellent review")
        self.assertTemplateUsed(response, "books/book_detail.html")
