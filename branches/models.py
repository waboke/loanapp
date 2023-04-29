from django.db import models

# Create your models here.
class Branches(models.Model):
    name = models.CharField(max_length=200, unique=True)
    Address = models.CharField(max_length=200, blank=True, null=True)
    Phone = models.CharField(max_length=200,blank=True, null=True)
    country = models.CharField(max_length=200,blank=True, null=True)
    state = models.CharField(max_length=200,blank=True, null=True)
    city = models.CharField(max_length=200,blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    edited_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name