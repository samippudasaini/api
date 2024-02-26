from django.db import models

# Create your models here.
class Students(models.Model):
    first_name=models.CharField(max_length=10)
    middle_name=models.CharField(max_length=10)
    last_name=models.CharField(max_length=10)
    email=models.EmailField(max_length=30)
    user_name=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    upload_image=models.ImageField()
    