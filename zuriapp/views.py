from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("This is my first django project. Thank you MENTOR Enny. For our sake, please prepare a sequential guide for your next class so that we can follow step-by-step. Cheers")
