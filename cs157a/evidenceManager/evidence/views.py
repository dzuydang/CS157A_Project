from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def landingPage(request):
    return render(request, 'evidence/landingpage.html')