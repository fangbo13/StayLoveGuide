from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    nickname = models.CharField(max_length=100)

class UserProfile(models.Model):
    # 这是一个到 CustomUser 的 OneToOneLink，每个用户只有一个个人资料
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    # 下面是一些额外的字段
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    bio = models.TextField(blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    location = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.user.username
