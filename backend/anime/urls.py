from django.urls import path
from .views import AnimeListView,AnimeUserInfoView

urlpatterns = [
    path('<str:username>/', AnimeListView.as_view(), name='anime-list'),
    path('<str:username>/<str:subresource>/', AnimeUserInfoView.as_view()),

    
]
