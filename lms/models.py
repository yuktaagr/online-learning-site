from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    institute_name = models.CharField(max_length=224, blank=True)
    phone_no = models.CharField(max_length=10)



    def _str_(self):
        return self.user.username


class Instructor(models.Model):
    user = models.OneToOneField(User, unique=True, on_delete=models.CASCADE)
    institute_name = models.CharField(max_length=224, blank=True)
    phone_no = models.CharField(max_length=10)

    def _str_(self):
        return self.user.username

class courseforms(models.Model):
    instructor=models.ForeignKey(Instructor,on_delete=models.CASCADE,default= 1)
    title = models.CharField(max_length=122)
    bio = models.CharField(max_length=244)

