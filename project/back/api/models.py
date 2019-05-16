from django.db import models
from django.contrib.auth.models import User
import datetime

class ShopUser(models.Manager):
    def for_user(self, user):
        return self.filter(sender=user)

class Store(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=20)
    description = models.TextField()
    place = models.CharField(max_length=50)
    address = models.CharField(max_length=100)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'type': self.type,
            'description': self.description,
            'place': self.place,
            'address': self.address
        }
class Seller(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=30)
    address = models.CharField(max_length=100)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'mobile': self.mobile,
            'address': self.address
        }


class Car(models.Model):
    name = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    cost = models.IntegerField()
    type = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'company': self.company,
            'cost': self.cost,
            'type': self.type,
            'description': self.description,
        }
class Customer(models.Model):
    name = models.CharField(max_length=50)
    mobile = models.CharField(max_length=30)
    address = models.CharField(max_length=100)

    def __str__(self):
        return '{}: {}'.format(self.id, self.name)

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'mobile': self.mobile,
            'address': self.address
        }

class Meetingpoint(models.Model):
    type = models.CharField(max_length=100)
    description = models.TextField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer')
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE, related_name='seller')

    def __str__(self):
        return '{}: {}'.format(self.id, self.type)

    def to_json(self):
        return {
            'id': self.id,
            'description': self.description,
            'customer': self.customer.to_json(),
            'seller': self.seller.to_json()
        }

