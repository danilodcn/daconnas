from django.urls import path
from .views import DiaristasCidadeList
from django.views.generic import TemplateView

urlpatterns = [
    path("diaristas-cidade", DiaristasCidadeList.as_view(), name="diarista-cidade-list"),
    path("doc",
         TemplateView.as_view(
            template_name="swagger-doc.html",
            extra_context = {'schema_url':'openapi-schema'},
        ),
        name='swagger-ui'
    )
]

