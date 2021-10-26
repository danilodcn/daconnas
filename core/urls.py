from django.urls import path
from core.views import create, list, update, delete


urlpatterns = [
    path("create/<str:name>", create, name="register"),
    path("list/<str:name>", list, name="lists"),
    path("update/<str:name>/<str:id>", update, name="update"),
    path("delete/<str:name>/<str:id>", delete, name="delete"),
]
