from django.db import models
from django.utils import timezone

class ItemInfo(models.Model):
    shopname = models.CharField(max_length = 20)
    url = models.URLField(max_length=250)
    pub_time = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.shopid
