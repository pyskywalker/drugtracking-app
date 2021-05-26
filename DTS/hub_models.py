from django.db import models

# Create your models here.
class Location(models.Model):
    zone=models.CharField(max_length=30)
    region=models.CharField(max_length=30)
    city=models.CharField(max_length=30)
    region=models.CharField(max_length=30)
    area=models.CharField(max_length=30)
    date_added=models.DateTimeField(auto_now_add=True)
    date_modified=models.DateTimeField(auto_now=True)
    def __str__(self):
        return f'{self.area},{self.city},{self.region}'