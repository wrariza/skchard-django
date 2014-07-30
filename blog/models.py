from django.db import models

# Create your models here.


class Post(models.Model):
    title_name = models.CharField(max_length=150, unique=True)
    content = models.TextField()
    autor = models.CharField(max_length=50)


