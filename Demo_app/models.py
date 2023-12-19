from django.db import models

# Create your models here.

class Comment(models.Model):
    title = models.CharField(max_length=50)
    message = models.TextField(max_length=150)
    
    def __str__(self):
        return self.title
