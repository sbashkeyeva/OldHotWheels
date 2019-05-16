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


class ViewStoreList(generics.ListCreateAPIView):
    permission_classes = (AllowAny,)
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    http_method_names = ['get']

class StoreList(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Store.objects.all()
    serializer_class = StoreSerializer
    http_method_names = ['get', 'post']


class Store_detail(APIView):
    permission_classes = (IsAdminUser, )
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


