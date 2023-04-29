from django.urls import path, include
from .import views


urlpatterns = [
    path('signup',views.signup,name='signup'),
    path('accounts/',include('django.contrib.auth.urls')),
    path('add-user', views.add_user, name='add-user'),
     path('view-users', views.view_users, name='view-users'),
   
]