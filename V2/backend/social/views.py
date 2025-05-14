from rest_framework.generics import ListAPIView
from .models import Post
from .serializers import SocialSerializer

class SocialListView(ListAPIView):
    queryset = Post.objects.all()
    serializer_class = SocialSerializer