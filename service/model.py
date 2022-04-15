from urllib import request
from django.db import models
from django.db.models.base import Model

# Create your models here.
class room(models.Model):
    room_id=models.CharField(max_length=20)
    host1=models.GenericIPAddressField()
    host2=models.GenericIPAddressField()

class msg(models.Model):
    room_id=models.CharField(max_length=20)
    message=models.TextField(max_length=150)

class Thread(models.Model):
    thread_type=models.CharField(max_length=20)

class hosting(models.Model):
    status=models.BooleanField()
    pub_date = models.DateTimeField('date published')
    ip=models.GenericIPAddressField()

    def __str__(self):
        return self.ip
