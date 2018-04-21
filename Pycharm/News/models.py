from django.db import models
from django.utils import timezone

class News(models.Model):
    title = models.CharField(max_length=200)
    link = models.TextField()
    image = models.TextField()
    info = models.TextField()
    create_time = models.DateTimeField(default=timezone.now)

    class Meta:
        db_table = "news"