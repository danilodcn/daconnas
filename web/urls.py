from django.urls import path
from .views import cadastrar_diarista, listar_diaristas, update_diarista, delete_diarista

urlpatterns = [
    path("cadastrar_diarista", cadastrar_diarista, name="cadastrar_diarista"),
    path("listar_diaristas", listar_diaristas, name="listar_diaristas"),
    path("editar_diarista/<int:id>", update_diarista, name="editar_diarista"),
    path("deletar_diarista/<int:id>", delete_diarista, name="deletar_diarista")
]

