from django.urls import path
from .views import LoginAPIView, RefreshAPIView, RegisterAPIView, UserAPIView,LogoutAPIView,ResetAPIView


urlpatterns = [
    path('register', RegisterAPIView.as_view()),
    path('login', LoginAPIView.as_view()),
    path('user', UserAPIView.as_view()),
    path('refresh', RefreshAPIView.as_view()),
    path('logout', LogoutAPIView.as_view()),
    path('reset', ResetAPIView.as_view()),

]
