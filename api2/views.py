from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .services.cidades_atendimento_service import listar_diaristas_cidade
from .serializers.diaristas_cidade import DiaristaCidadeSerializer
from .paginations.diaristas_cidade_pagination import DiaristasCidadePagination
import time
# Create your templates here.

class DiaristasCidadeList(APIView, DiaristasCidadePagination):
    def get(self, request, format=None):
        cep: str = self.request.query_params.get("cep", [])
        diaristas = listar_diaristas_cidade(cep)
        # time.sleep(10)
        # serializer = DiaristaCidadeSerializer(
        #             diaristas,
        #             many=True,
        #             context={"request": request}
        # )
        resultado = self.paginate_queryset(diaristas, request)
        serializer = DiaristaCidadeSerializer(
                    resultado,
                    many=True,
                    context={"request": request}
        )

        # return Response(serializer.data)
        return self.get_paginated_response(serializer.data)
