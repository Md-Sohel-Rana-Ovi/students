from django.db import models
# Create your models here.
class aboutus(models.Model):
    title= models.CharField(max_length=100, blank=False)
    description=models.TextField(max_length=700,blank=False)
    image=models.ImageField(upload_to='about',blank=False)

    def __str__(self):
        return self.title

class slider(models.Model):
    title= models.CharField(max_length=100, blank=False)
    description=models.TextField(max_length=700,blank=False)
    image=models.ImageField(upload_to='slider',blank=False)

    def __str__(self):
        return self.title

class clientinfo(models.Model):
    name= models.CharField(max_length=100, blank=False)
    link=models.CharField(max_length=400,blank=False)
    image=models.ImageField(upload_to='clientinfo',blank=False)

    def __str__(self):
        return self.name

class portfolio(models.Model):
    title= models.CharField(max_length=100, blank=False)
    link=models.CharField(max_length=400,blank=False)
    image=models.ImageField(upload_to='portfolio',blank=False)

    def __str__(self):
        return self.title