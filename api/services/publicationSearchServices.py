from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector, TrigramSimilarity
from core import models

def search_by_speaker(speaker_name: str):
    search = SearchVector("speaker__name")
    search =  models.Publication.objects.annotate(search=search).filter(search=speaker_name)
    
    # print(search)

    return search


def search_by_topic(topic_name: str):
    search = SearchVector("topic__name")
    search =  models.Publication.objects.annotate(search=search).filter(search=topic_name)
    
    # print(search)
    return search


def search_by_title(title: str):
    search = SearchVector("post__title")
    search =  models.Publication.objects.annotate(search=search).filter(search=title)
    # print(search)
    return search

def search_by_text(text: str):
    search = SearchVector("post__content", "post__description")
    search =  models.Publication.objects.annotate(search=search).filter(search=text)
    # print(search)
    return search