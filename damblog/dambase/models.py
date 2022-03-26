from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    
    blockquote_author_name = models.CharField(max_length=100, default='Miracle')
    
    blockquote = models.TextField(max_length=500)
    
    classheading = models.TextField(max_length=100)
    classheading_content = models.TextField()
    
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)