from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
    uid = models.OneToOneField(User)
    ustrid = models.SlugField()
    nickname = models.CharField(max_length=64)

class Contacts(models.Model):
    owner = models.ForeignKey(User)
    person = models.CharField(max_length=64)
    email = models.EmailField()
    mobile = models.CharField(max_length=18)

