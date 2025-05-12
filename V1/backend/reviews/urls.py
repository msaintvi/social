from django.urls import path
from .views import BookReviewListView

urlpatterns = [
    path('reviews/', BookReviewListView.as_view(), name='book-reviews'),
]