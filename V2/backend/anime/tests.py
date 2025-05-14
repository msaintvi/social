from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient
from unittest.mock import patch

class AnimeHistoryFetchTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.username = "Luffydou"

    @patch("anime.views.requests.get")
    def test_fetch_and_store_anime_history(self, mock_get):
        # Mock the history response
        mock_get.side_effect = [
            # First call: user history
            MockResponse({
                "data": [
                    {"entry": {"mal_id": 1}},
                    {"entry": {"mal_id": 2}},
                ]
            }, 200),
            # Second call: anime detail for mal_id=1
            MockResponse({"data": {
                "title": "Anime 1", "synopsis": "Story", "images": {"jpg": {"image_url": "url"}}, "score": 8.0
            }}, 200),
            # Third call: anime detail for mal_id=2
            MockResponse({"data": {
                "title": "Anime 2", "synopsis": "Story", "images": {"jpg": {"image_url": "url"}}, "score": 7.5
            }}, 200),
        ]

        response = self.client.get(f"/api/anime/{self.username}/fetch-and-store/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data["inserted"], 0)  # We didn't save to DB in this test
        self.assertTrue(response.data["success"])

# --- Helper class for mocking requests.get
class MockResponse:
    def __init__(self, json_data, status_code):
        self._json_data = json_data
        self.status_code = status_code

    def json(self):
        return self._json_data
