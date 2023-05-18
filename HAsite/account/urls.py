from django.urls import path

from account.views import forget_password

urlpatterns = [
    path('forget_password/', forget_password, name='forget_password'),
]
