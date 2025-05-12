from django.db import models

class BookReview(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    review = models.TextField()
    rating = models.IntegerField()
    
    def __str__(self):
        return self.title