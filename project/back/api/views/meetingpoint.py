from api.models import Seller, Customer, Meetingpoint, Store, Car
from api.serializers import UserSerializer, StoreSerializer, SellerSerializer, CustomerSerializer, CarSerializer, MeetingpointSerializer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import authentication
from rest_framework import authtoken
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser

class PostMeetingpointList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Meetingpoint.objects.all()
    serializer_class = MeetingpointSerializer
    http_method_names = ['post']

class MeetingpointList(generics.ListCreateAPIView):
    permission_classes = (IsAdminUser,)
    queryset = Meetingpoint.objects.all()
    serializer_class = MeetingpointSerializer
    http_method_names = ['get', 'post']

class Meetingpoint_detail(APIView):
    permission_classes = (IsAdminUser)
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

