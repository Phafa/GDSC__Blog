from django.db import models
from Blogapp.models import post
# Create your models here.
class comment(models.Model):
    content = models.TextField()
    Author = models.CharField(max_length=50)
    Published_Date = models.DateTimeField(auto_now_add=True)
    Post = models.ForeignKey(post, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.author} on {self.post.title}' 
