from django.urls import path

from api.views import PublicationsView


urlpatterns = [
    # path("create/<str:name>", create, name="register")
    path("publications", PublicationsView.as_view(), name="publications")
]