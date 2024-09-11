from django import forms
from main.models import *
from .models import *
from django.apps import apps

def get_all_models():
    models = apps.get_models()
    return models

