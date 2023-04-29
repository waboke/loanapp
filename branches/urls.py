from django.urls import path
from .import views


urlpatterns = [
    path('add-branche', views.add_branche, name='add-branche'),
    path('view-branches', views.view_branches, name='view-branches'),
   
]