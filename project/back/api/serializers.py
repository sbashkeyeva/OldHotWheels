from rest_framework import serializers
from api.models import Store, Seller, Customer, Meetingpoint, Car
from django.contrib.auth.models import User

import datetime

class UserSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    is_staff = serializers.BooleanField(required=False, default=False)
    password = serializers.CharField(write_only=True)
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password', 'is_staff')


class StoreSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    type = serializers.CharField()
    description = serializers.CharField()
    place = serializers.CharField()
    address = serializers.CharField()

    class Meta:
        model = Store
        fields = '__all__'


class SellerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    mobile = serializers.CharField()
    address = serializers.CharField()

    class Meta:
        model = Seller
        fields = '__all__'


class CustomerSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    mobile = serializers.CharField()
    address = serializers.CharField()

    class Meta:
        model = Customer
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    company = serializers.CharField()
    cost = serializers.IntegerField()
    type = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = Car
        fields = '__all__'

class MeetingpointSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(read_only=True)
    type = serializers.CharField()
    description = serializers.CharField()

    class Meta:
        model = Meetingpoint
        fields = '__all__'

    def create(self, validated_data):
        meetingpoint = Meetingpoint(**validated_data)
        meetingpoint.save()
        return meetingpoint


