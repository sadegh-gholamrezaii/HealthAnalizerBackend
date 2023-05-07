from django.contrib import admin
from django.urls import path,include
from .views import signup,signin,signout,books
 
urlpatterns = [
    path('books/', books),
    path('books/signup/', signup, name ='signup'),
    path('books/signin/', signin, name = 'login'),
    path('books/signout/', signout, name = 'logout'),
]