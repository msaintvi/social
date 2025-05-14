from django.urls import path
from .views import (
    AnimeListView,
    AnimeUserInfoView,
    FetchAndStoreAnimeHistoryView  # <-- import your new view
)

urlpatterns = [
    path('<str:username>/', AnimeListView.as_view(), name='anime-list'),
    path('<str:username>/<str:subresource>/', AnimeUserInfoView.as_view()),
    path('<str:username>/history/anime/', FetchAndStoreAnimeHistoryView.as_view(), name='history-anime'),  # <-- ADD THIS
    path('<str:username>/fetch-and-store/', FetchAndStoreAnimeHistoryView.as_view(), name='fetch-store-anime'),
]
