from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("The Teams Page is here")
def match(request,match_id):
    return render(request,'team/index.html',{"match_id": match_id})