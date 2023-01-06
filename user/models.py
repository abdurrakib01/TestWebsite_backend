from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    sector = models.CharField(max_length=200)
    tc = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name