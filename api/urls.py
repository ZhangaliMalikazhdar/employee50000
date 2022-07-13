from django.urls import path
from .views import *
from rest_framework.authtoken import views

urlpatterns = [
    path('', EmployeeList.as_view()),
    path('search/', EmployeeSearch.as_view()),
    path('login/', example_view),
    path('registration/', create_auth_token),
    path('api-token-auth/', views.obtain_auth_token),
    path('auth/', CustomAuthToken.as_view()),
]
