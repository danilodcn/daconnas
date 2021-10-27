from web.services.cep_services import buscar_cidade_cep
from web.models import Diarista
from rest_framework import serializers

def bucar_cidade_cep(cep):
    response = buscar_cidade_cep(cep)
    if response.status_code == 400:
        raise serializers.ValidationError("O CEP está incorreto")

    response_json = response.json()
    if "erro" in response_json:
        raise serializers.ValidationError("O CEP informado nao foi encontrado")

    return response_json

def listar_diaristas_cidade(cep: str):
    cidade_api = bucar_cidade_cep(cep)
    codigo_ibge = cidade_api["ibge"]
    try:
        diaristas = Diarista.objects.filter(codigo_ibge=codigo_ibge).order_by("id")
        return diaristas
    except Diarista.DoesNotExist:
        return []