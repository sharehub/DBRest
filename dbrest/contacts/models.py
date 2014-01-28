from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

IDCODE_LEN=len(settings.PROFILE_CODE)

# Create your models here.
class Profile(models.Model):
    uid = models.OneToOneField(User)
    ustrid = models.SlugField()
    nickname = models.CharField(max_length=64)
    
    @staticmethod
    def uusid(uname):
        """
        return the uniq SN of user, uname should use ''.encode() to make it ascii 
        """
        ustrid = []
        uuids = ''.join(str(uuid.uuid5(uuid.NAMESPACE_X500, uname)).split('-'))
        str1, str2 = uuids[::2], uuids[1::2]
        for id in zip(str1, str2):
            idx = int(id[0], 16)*settings.PROFILE_MULTI[0]+int(id[1], 16)*settings.PROFILE_MULTI[1]
            ustrid.append(settings.PROFILE_CODE[idx%IDCODE_LEN])

        return ''.join(ustrid)

class Contacts(models.Model):
    owner = models.ForeignKey(User)
    person = models.CharField(max_length=64)
    email = models.EmailField()
    mobile = models.CharField(max_length=18)

