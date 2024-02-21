from django.test import TestCase


class WebViews(TestCase):
    def test_ping(self):
        response = self.client.get("/ping/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "pong - v1")