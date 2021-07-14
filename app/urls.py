from django.urls import path
from .views import *

urlpatterns = [
    path('', homepageview),
    path('extract/', email_extractor_view, name="extract-email")
]