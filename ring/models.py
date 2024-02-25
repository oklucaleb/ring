from django.db import models

# Create your models here.
class HomeTestimonials(models.Model):
    name = models.CharField(max_length=20)
    content = models.TextField()