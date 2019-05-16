from django.urls import path
from api import views



urlpatterns = [
    path('sellers/', views.SellerList.as_view()),
    path('sellers/<int:pk>/', views.Seller_detail.as_view()),
    path('vsellers/', views.ViewSellerList.as_view()),
    path('customers/', views.CustomerList.as_view()),
    path('customers/<int:pk>/', views.Customer_detail.as_view()),
    path('stores/', views.StoreList.as_view()),
    path('stores/<int:pk>/', views.Store_detail.as_view()),
    path('vstores/', views.ViewStoreList.as_view()),
    path('cars/', views.CarList.as_view()),
    path('cars/<int:pk>/', views.Car_detail.as_view()),
    path('vcars/', views.ViewCarList.as_view()),
    path('meetingpoints/', views.MeetingpointList.as_view()),
    path('meetingpoints/<int:pk>/', views.Meetingpoint_detail.as_view()),
    path('pmeetingpoints/', views.PostMeetingpointList.as_view()),
    path('users/', views.UserList.as_view()),
    path('login/', views.login),
    path('logout/', views.logout),
    path('signup/', views.signup),
]
