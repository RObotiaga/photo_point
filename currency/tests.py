import time

from django.test import TestCase, Client


class GetCurrentUSDViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_get_current_usd_returns_200(self):
        """
        Проверка статуса и формата запроса
        """
        response = self.client.get('/get-current-usd/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/json')
