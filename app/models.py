from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Key(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    key = models.CharField(max_length=10000)
    enc_string = models.CharField(max_length=10000)

    def __str__(self):
        return f'{self.user} {self.enc_string}'