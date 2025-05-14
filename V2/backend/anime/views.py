import requests
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .models import Anime  # your model

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


# class FetchAndStoreAnimeHistoryView(APIView):
#     def get(self, request, username):
#         history_url = f"https://api.jikan.moe/v4/users/{username}/history/anime"
#         history_res = requests.get(history_url)
#         if history_res.status_code != 200:
#             return Response({"error": "Failed to fetch history"}, status=history_res.status_code)

#         history = history_res.json().get("data", [])

#         anime_data = []
#         for item in history:
#             mal_id = item["entry"]["mal_id"]

#             # Fetch full anime details
#             anime_url = f"https://api.jikan.moe/v4/anime/{mal_id}"
#             detail_res = requests.get(anime_url)
#             if detail_res.status_code != 200:
#                 continue

#             anime_info = detail_res.json().get("data")

#             # Save in database (uncomment and adapt when ready)
#             # Anime.objects.update_or_create(
#             #     mal_id=mal_id,
#             #     defaults={
#             #         "title": anime_info["title"],
#             #         "synopsis": anime_info.get("synopsis"),
#             #         "image_url": anime_info["images"]["jpg"]["image_url"],
#             #         "score": anime_info.get("score"),
#             #         # Add other fields as needed
#             #     }
#             # )
#             # anime_data.append(anime_info)

#         return Response({"success": True, "inserted": len(anime_data)})

class FetchAndStoreAnimeHistoryView(APIView):
    def get(self, request, username):
        history_url = f"https://api.jikan.moe/v4/users/{username}/history/anime"
        history_res = requests.get(history_url)

        if history_res.status_code != 200:
            return Response({"error": "Failed to fetch history"}, status=history_res.status_code)

        history = history_res.json().get("data", [])

        anime_data = []

        for item in history:
            mal_id = item["entry"]["mal_id"]
            anime_url = f"https://api.jikan.moe/v4/anime/{mal_id}"
            detail_res = requests.get(anime_url)

            if detail_res.status_code != 200:
                continue

            anime_info = detail_res.json().get("data")
            if anime_info:
                anime_data.append({
                    "mal_id": anime_info.get("mal_id"),
                    "title": anime_info.get("title"),
                    "image_url": anime_info.get("images", {}).get("jpg", {}).get("image_url"),
                    "score": anime_info.get("score"),
                    "synopsis": anime_info.get("synopsis")
                })
            

        return Response({
            "success": True,
            "data": anime_data
        })