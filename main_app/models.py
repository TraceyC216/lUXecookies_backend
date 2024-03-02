from django.db import models
from django.urls import reverse

# Create your models here.
class Cookie(models.Model):
    image = models.CharField(max_length=240)
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    price = models.CharField(max_length=100)
    category = models.CharField(max_length=20, default='traditional')

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'cookie_id': self.id})
    
