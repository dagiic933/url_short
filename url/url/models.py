from django.db import models

class UrlShortener(models.Model):
    long_url = models.URLField()
    short_code = models.CharField(max_length=10, unique=True)  # adjust the length as needed
    created_at = models.DateTimeField(auto_now_add=True)
