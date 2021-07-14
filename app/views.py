from django.shortcuts import render
from django.http import JsonResponse 
from .forms import *
from django.core import serializers

# Create your views here.
def homepageview(request):
    form = EmailForm()
    return render(request, "index.html", {"form": form})


def email_extractor_view(request):
    if request.method == "POST":
        textare = request.POST.get('email-text')
        print(textare)
        
    return JsonResponse ({"emails": "Django developer"}, safe=False)
