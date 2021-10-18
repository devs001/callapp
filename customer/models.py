from django.db import models
from django.contrib.auth.models import User

# Create your models here.




class Customer(models.Model):
    name = models.CharField(max_length=40)
    phone_no = models.CharField(max_length=14)
    remarks = models.TextField(null=True, blank=True)
    called_before = models.BooleanField(default=False)
    last_call_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return str(self.name) + ' ' + str(self.phone_no)





