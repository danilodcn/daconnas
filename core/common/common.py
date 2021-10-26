from core.forms import forms
from core import models


def get_form(name: str):
    name = name.lower()
    all = dir(forms)
    for object in all:
        if object.endswith("Form") and object.lower().startswith(name):
            return getattr(forms, object)

def get_model(name: str):
    name = name.lower()
    all = dir(models)
    for object in all:
        if object.lower().startswith(name):
            return getattr(forms, object)