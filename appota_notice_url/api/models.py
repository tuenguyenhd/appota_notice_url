from django.db import models

# Create your models here.
class AppotaGameUser(models.Model):
    username = models.CharField(max_length=200)
    server = models.CharField(max_length=100, default="1")
    coin = models.IntegerField(default=0)
    gold = models.IntegerField(default=0)
    ruby = models.IntegerField(default=0)
    diamond = models.IntegerField(default=0)
    vip = models.FloatField(default=0)
    month_card = models.IntegerField(default=0)
