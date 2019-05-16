

from django.contrib import admin
from api.models import Seller, Car, Customer, Store, Meetingpoint

@admin.register(Seller)
class RSeller(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Car)
class RCar(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Customer)
class RCustomer(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Store)
class RStore(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Meetingpoint)
class RMeetingpoint(admin.ModelAdmin):
    list_display = ('id', 'seller', 'customer')

