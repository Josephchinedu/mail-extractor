from django.shortcuts import render
from django.http import JsonResponse 
from .forms import *
from .scripts import *

# Create your views here.
def homepageview(request):
    form = EmailForm()
    return render(request, "index.html", {"form": form})


def email_extractor_view(request):
    if request.method == "POST":
        textare = request.POST.get('email-text')
        output_data = main(textare)
        print(output_data)
        
    return JsonResponse ({"emails": output_data}, safe=False)
