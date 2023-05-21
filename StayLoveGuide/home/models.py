from django.db import models
from django.utils.translation import gettext_lazy as _

class HomePage(models.Model):
    home_title = models.CharField(max_length=100, verbose_name=_('首页标题'))
    home_bg = models.ImageField(upload_to='home_background/', verbose_name=_('首页图片'))

    def __str__(self):
        return self.home_title