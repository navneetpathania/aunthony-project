from django.db import models


# Create your models here.

class Transactions(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    from_addr = models.CharField(max_length=200)
    to_addr = models.CharField(max_length=200)
    asset = models.CharField(max_length=20, default='EUR')
    amount = models.CharField(max_length=200)



class Accounts(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    user_name = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    seed = models.CharField(max_length=200)
    def __str__(self):
        return self.address

class Contact(models.Model):
    user_name = models.CharField(max_length=200)
    #created = models.DateTimeField(auto_now_add=True, blank=True)
    contact = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    memo = models.CharField(max_length=28, blank=True)

