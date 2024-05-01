from django.urls import path
from webpage import views 

urlpatterns = [
    path("", views.home, name = "home"),
    path("analyze/", views.analyze, name = "analyze"),
    path("group/", views.group, name= "group"),
]

