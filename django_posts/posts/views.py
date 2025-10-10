from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    data = {"n":0}
    return render(request,"index.html",context=data)