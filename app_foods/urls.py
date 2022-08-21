from xxlimited import foo
from django.urls import path
from .views import food

urlpatterns = [
    path(" ",view=food, name="food"),
]