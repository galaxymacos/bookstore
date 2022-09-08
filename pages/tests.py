from django.test import SimpleTestCase  # For pages that don't require a model
from django.urls import reverse, resolve

from pages.views import HomePageView


# Create your tests here.
class HomePageTests(SimpleTestCase):
    def setUp(self) -> None:
        url = reverse("pages:home")
        self.response = self.client.get(url)

    def test_url_exists_at_correct_location(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_url_name(self):
        self.assertEqual(self.response.status_code, 200)

    def test_homepage_template(self):
        self.assertTemplateUsed(self.response, "home.html")

    def test_contains_correct_html(self):
        self.assertContains(self.response, "home page")

    def test_does_not_contain_incorrect_html(self):
        self.assertNotContains(self.response, "Not on home page")

    def test_resolve(self):
        view = resolve("/")
        self.assertEqual(view.func.__name__, HomePageView.as_view().__name__)
