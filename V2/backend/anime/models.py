from django.db import models

class Anime(models.Model):
    mal_id = models.IntegerField(unique=True)
    title = models.CharField(max_length=255)
    synopsis = models.TextField(blank=True)
    image_url = models.URLField(blank=True)
    score = models.FloatField(null=True, blank=True)
    # ...more fields
