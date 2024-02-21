from django.test import TestCase

from faker import Faker

fake = Faker()


class WebViews(TestCase):
    def test_ping(self):
        response = self.client.get("/ping/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["message"], "pong - v1")

    def test_reviews_create(self):
        response = self.client.post("/web/reviews/", data={
            "name": fake.name(),
            "review": "I like sci-fi movies",
            "rating": 5
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual("id" in response.json(), True)

    def test_reviews_list(self):
        self.client.post("/web/reviews/", data={
            "name": fake.name(),
            "review": "I like sci-fi movies",
            "rating": 5
        })
        response = self.client.get("/web/reviews/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["count"], 1)
