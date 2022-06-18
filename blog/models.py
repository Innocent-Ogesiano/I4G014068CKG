import django.contrib.auth
from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200)
    text = models.TextField
    author = models.ForeignKey(django.contrib.auth.get_user_model(), on_delete=models.DO_NOTHING)
    created_date = models.DateTimeField('Date created')
    published_date = models.DateTimeField('Date published')
