from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("view2", views.viewTwo, name="viewTwo"),
    path("view3", views.viewThree, name="viewThree"),
    path("<str:name>", views.greet, name="greet")
    
]
