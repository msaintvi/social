from rest_framework.generics import ListAPIView
from .models import BookReview
from .serializers import BookReviewSerializer

class BookReviewListView(ListAPIView):
    queryset = BookReview.objects.all()
    serializer_class = BookReviewSerializer