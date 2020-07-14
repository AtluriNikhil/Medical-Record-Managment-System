from django.db import models
from django.contrib.auth.models import User

class UserProfileInfo(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    gender = models.CharField(max_length=1)
    dob = models.DateField()
    Bloodgroup = models.CharField(max_length=2)
    phoneno = models.IntegerField()
    profile_pic = models.ImageField(default="default.jpg",upload_to='profile_pics',blank=True)

    def __str__(self):
        return self.user.username

