

from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('signup',views.signup,name="signup"),
    path('signout',views.signout,name="signout"),
   
    
]
