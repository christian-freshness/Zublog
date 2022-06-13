from django.db import models
from django.contrib.auth import get_user_model
from datetime import datetime

User = get_user_model()
# Create your models here.
class Post(models.Model):
    Title = models.CharField(max_length = 200)
    Text = models.TextField()
    Author = models.ForeignKey(User, on_delete=models.CASCADE)
    Created_date = models.DateTimeField(default=datetime.now)
    Published_date = models.DateTimeField(default=datetime.now)

