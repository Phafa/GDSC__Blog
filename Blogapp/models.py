from django.db import models

# Create your models here.

class post(models.Model):
    title = models.CharField(max_length=255, unique=True)
    content = models.TextField()
    category = models.CharField(max_length=50)
    image = models.ImageField(upload_to='bLog_image/')
    tags = models.BinaryField(models.CharField(max_length=50))
    
    def __str__(self):
        return self.title

