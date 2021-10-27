from django.http.response import JsonResponse
from rest_framework.views import APIView
from api.paginations.pages import Pagination
from api.serializers.publications_serializers import PublicationsSerializer
from api.services.publicationSearchServices import (
    search_by_speaker, 
    search_by_topic, 
    search_by_title, 
    search_by_text
)
from core.models import Publication

from pprint import pprint

class SearchError(Exception):
    ...

class PublicationsView(APIView, Pagination):
    # queryset = Publication.objects.all()
    # serializer_class = PublicationsSerializer
    # pagination_class = Pagination
    
    def get(self, request, *args, **kwargs):
        "params: speaker, topic, title_post, text_post"
        # print(self.request.query_params)
        publications = []
        search_term = self.request.query_params.get("search", "")
        finished = False
        print(search_term)
        if not search_term:
            publications = Publication.objects.all().order_by("visualizations")
            finished = True
        
        speaker = self.request.query_params.get("speaker", [])
        if speaker and not finished:
            publications = search_by_speaker(speaker)
            finished = True

        topic = self.request.query_params.get("topic", "")
        if topic and not finished:
            publications = search_by_topic(topic)
            finished = True

        title = self.request.query_params.get("title", "")
        if title and not finished:
            publications = search_by_title(title)
            finished = True

        text = self.request.query_params.get("text", "")
        if text and not finished:
            publications = search_by_text(text)
            finished = True

        print(publications)
        paginated = self.paginate_queryset(publications, request)
        
        serializer = PublicationsSerializer(
            paginated,
            many=True,
            context={"request": request}
        )
        
        return self.get_paginated_response(serializer.data)
        return super().get(request, *args, **kwargs)
    
def increment_visualization(request, id:str):
    post = Publication.objects.get(id=id)
    try:
        post.visualization += 1
        post.save()
        return JsonResponse({"status", "Ok"}, status=200)
    except Exception as error:
        return JsonResponse({"error": error}, status=401)