from django.db import models
 
 
class User(models.Model):
    
    firstname = models.CharField(max_length=20, blank=False, default='')
    lastname = models.CharField(max_length=20, blank=False, default='')
    email = models.EmailField(max_length=40, blank=False, default='')
    role = models.CharField(max_length=40,blank=False, default='')
    password = models.CharField(max_length=20, blank=False, default='')
