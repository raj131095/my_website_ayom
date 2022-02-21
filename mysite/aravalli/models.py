from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

class Create_Shop(models.Model):
    owner= models.CharField(max_length=64)
    shopname=models.CharField(max_length=64)
    shopadd1=models.CharField(max_length=100)
    shopadd2=models.CharField(max_length=100)
    latitude=models.TextField()
    longitude=models.TextField()
    contactno=models.IntegerField()
    altcontact=models.CharField(max_length=12)
    website=models.CharField(max_length=64)
    opentime=models.TimeField()
    closetime=models.TimeField()
    describe=models.TextField()
    users=models.ForeignKey(User, related_name="name", on_delete=models.CASCADE)
    def __str__(self):
        return self.owner

class UploadedImage(models.Model):
    owner=models.ForeignKey(Create_Shop, related_name="imgs", on_delete=models.CASCADE)
    title=models.CharField(max_length=100)

    image= models.ImageField(upload_to='images/')
    price=models.CharField(max_length=64)
    products=models.TextField()
    pieces=models.IntegerField()
    offer=models.CharField(max_length=64)
    name=models.CharField(max_length=64)
    shopname=models.CharField(max_length=64)
    shopadd1=models.CharField(max_length=100)
    shopadd2=models.CharField(max_length=100)
    latitude=models.TextField()
    longitude=models.TextField()
    contactno=models.IntegerField()
    altcontact=models.CharField(max_length=12)
    website=models.CharField(max_length=64)
    opentime=models.TimeField()
    closetime=models.TimeField()
    describe=models.TextField()
    def __str__(self):
        return self.title

class Watchlist(models.Model):
    image=models.ForeignKey(UploadedImage,related_name="upload", on_delete=models.CASCADE)
    user = models.CharField(max_length=64)
    def __str__(self):
        return self.user

class Comment(models.Model):
    user = models.CharField(max_length=64)
    time = models.CharField(max_length=64)
    comment = models.TextField()
    image=models.ForeignKey(UploadedImage,related_name="uploadimages",on_delete=models.CASCADE)
    def __str__(self):
        return self.user