from urllib import request
from django.db import models
from django.db.models.base import Model
from django.contrib.auth.models import User

class room(models.Model):
    room_id=models.AutoField(primary_key=True)
    host1=models.CharField(max_length=20)
    host2=models.CharField(max_length=20)

class msg(models.Model):
    room_id=models.CharField(max_length=20)
    message=models.TextField(max_length=150)

class hosting(models.Model):
    status=models.BooleanField()
    pub_date = models.DateTimeField('date published')
    ip=models.CharField(max_length=20)

    def __str__(self):
        return self.ip
