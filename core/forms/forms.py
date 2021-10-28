from django import forms
from core.models import User, Speaker, Topic, Post, Publication


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        exclude = ["id", "posts"]


class SpeakerForm(forms.ModelForm):
    class Meta:
        model = Speaker
        exclude = ["id", "posts", "published"]


class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        exclude = ["id", "posts"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ["id"]


class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        exclude = ["id", "visualizations", "code"]
