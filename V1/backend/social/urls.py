from django.urls import path
from .views import SocialListView

urlpatterns = [
    path('social/', SocialListView.as_view(), name='test-database'),
]