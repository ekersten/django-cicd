from django.test import TestCase
from django.urls import reverse

class HomePageTest(TestCase):
    def test_home_page_exists(self):
        response = self.client.get(reverse('website:index'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_uses_correct_template(self):
        response = self.client.get(reverse('website:index'))
        self.assertTemplateUsed(response, 'website/index.html')


class ContactoPageTest(TestCase):
    def test_contacto_page_exists(self):
        response = self.client.get(reverse('website:contacto'))
        self.assertEqual(response.status_code, 200)

    def test_contacto_page_uses_correct_template(self):
        response = self.client.get(reverse('website:contacto'))
        self.assertTemplateUsed(response, 'website/contacto.html')