from django.db import models

class Note(models.Model):
    content = models.TextField()
    time = models.DateTimeField()
    url = models.CharField(max_length=8)
