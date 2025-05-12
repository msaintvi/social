import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class AnimeUserInfoView(APIView):
    def get(self, request, username, subresource=None):
        base_url = f"https://api.jikan.moe/v4/users/{username}"
        if subresource:
            base_url += f"/{subresource}"

        response = requests.get(base_url)

        if response.status_code == 404:
            return Response({"error": "Not found"}, status=404)
        if response.status_code != 200:
            return Response({"error": "Jikan API failed"}, status=502)

        return Response(response.json())


class AnimeListView(APIView):
    def get(self, request, username):
        url = f"https://api.jikan.moe/v4/users/{username}"
        response = requests.get(url)
        
        if response.status_code == 404:
            return Response({
                "error": f"User '{username}' not found on MyAnimeList."
            }, status=status.HTTP_404_NOT_FOUND)
        
        if response.status_code != 200:
            return Response({
                "error": "Failed to fetch data from Jikan API.",
                "status_code": response.status_code
            }, status=status.HTTP_502_BAD_GATEWAY)
        
        return Response(response.json())
