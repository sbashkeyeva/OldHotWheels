from api.models import Seller, Customer, Meetingpoint, Store, Car
from api.serializers import UserSerializer, SellerSerializer, CustomerSerializer, MeetingpointSerializer, CarSerializer, StoreSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import authentication
from rest_framework import authtoken
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser



class SellerList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Seller.objects.all()
    serializer_class = SellerSerializer
    http_method_names = ['get', 'post']

class Seller_detail(APIView):
    def get_object(selfs, pk):
        try:
            return Seller.objects.get(id=pk)
        except Seller.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        seller = self.get_object(pk)
        serializer = SellerSerializer(seller)
        return Response(serializer.data)


    def put(self, request, pk):
        seller = self.get_object(pk)
        serializer = SellerSerializer(instance=seller, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def delete(self, request, pk):
        seller = self.get_object(pk)
        seller.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CustomerList(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser, )
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    http_method_names = ['get', 'post']


class Customer_detail(APIView):
    def get_object(selfs, pk):
        try:
            return Customer.objects.get(id=pk)
        except Customer.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(patient)
        return Response(serializer.data)

    def put(self, request, pk):
        customer = self.get_object(pk)
        serializer = CustomerSerializer(instance=patient, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def delete(self, request, pk):
        customer = self.get_object(pk)
        customer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class StoreList(APIView):
    permission_classes = (AllowAny,)
    def get(self, request):
        storeList = Store.objects.all()
        serializer = StoreSerializer(storeList, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StoreSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class Store_detail(APIView):
    def get_object(selfs, pk):
        try:
            return Store.objects.get(id=pk)
        except Store.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        store = self.get_object(pk)
        serializer = StoreSerializer(store)
        return Response(serializer.data)


    def put(self, request, pk):
        store = self.get_object(pk)
        serializer = StoreSerializer(instance=store, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def delete(self, request, pk):
        store = self.get_object(pk)
        store.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



class CarList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    http_method_names = ['get', 'post']


class Car_detail(APIView):
    def get_object(selfs, pk):
        try:
            return Car.objects.get(id=pk)
        except Car.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        seller = self.get_object(pk)
        serializer = CarSerializer(seller)
        return Response(serializer.data)


    def put(self, request, pk):
        seller = self.get_object(pk)
        serializer = CarSerializer(instance=seller, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def delete(self, request, pk):
        seller = self.get_object(pk)
        seller.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MeetingpointtList(APIView):
    permission_classes = (IsAuthenticated,)
    def get(self, request):
        sellerList = Meetingpoint.objects.filter(user=self.user)
        serializer = MeetingpointSerializer(sellerList, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = MeetingpointSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class Meetingpoint_detail(APIView):
    def get_object(selfs, pk):
        try:
            return Meetingpoint.objects.get(id=pk)
        except Meetingpoint.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        seller = self.get_object(pk)
        serializer = MeetingpointSerializer(seller)
        return Response(serializer.data)


    def put(self, request, pk):
        seller = self.get_object(pk)
        serializer = MeetingpointSerializer(instance=seller, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    def delete(self, request, pk):
        seller = self.get_object(pk)
        seller.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

