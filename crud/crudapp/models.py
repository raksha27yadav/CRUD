from django.db import models
class State(models.Model):
    title=models.CharField(max_length=100)
    def __str__(self):
        return self.title
class Address(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField()
    pincode=models.CharField(max_length=6)
    state=models.ForeignKey(State,on_delete=models.CASCADE)
    add=models.CharField(max_length=300)
# Create your models here.
