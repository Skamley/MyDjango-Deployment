from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileInfo(models.Model):
    """
        Django provides default model User which has fields like Username,Password, Email
        Here we are extending default User model and adding another couple of attributes
        like Portfolio site, user's profile photo etc.
    """
    user = models.OneToOneField(User, on_delete='Cascade')

    #Add additional fields you want to have for user profiles
    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to="profile_pics", blank=True)
    """
        Here setting blank=True means this field is not mandatory for the user 
        for the profile_pic field we have set the value of "upload_to" to "profile_pics"
        which means when user uploads a pic it'd stored in media/profile_pics directory
        so we have to have a directory named "profile_pics" under media
        For images install Pillow by running the command - pip install pillow
    """

    def __str__(self):
        return self.user.username



class Topic(models.Model):

    top_name= models.CharField(max_length=264, unique=True)

    def __str__(self):
        return self.top_name

class WebPage(models.Model):

    topic= models.ForeignKey(Topic,on_delete=models.CASCADE)
    name = models.CharField(max_length=264,unique=True)
    url= models.URLField(unique=True)

    def __str__(self):
        return  self.name
class AccessRecord(models.Model):
    #name= models.ForeignKey(WebPage,on_delete=models.CASCADE)
    date= models.DateField()

    def __str__(self):
        return self.date
class Access_Record(models.Model):
    name= models.ForeignKey(WebPage,on_delete=models.CASCADE)
    date= models.DateField()

    def __str__(self):
        return self.date

class Employee(models.Model):
    Name= models.CharField(max_length=100)
    Organisation=models.CharField(max_length=100)
    Email= models.CharField(max_length=100, unique=True)