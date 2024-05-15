from django.db import models

# Create your models here.

class Recipee(models.Model):
    name=models.CharField(max_length=100)
    description=models.TextField(max_length=500)
    image=models.ImageField(upload_to="uploaded")
    
    def __str__(self):
        return (f"{self.id} {self.name}")
    
class login(models.Model):
    username=models.CharField(max_length=50,null=False)
    password=models.CharField(max_length=100,null=False)
    