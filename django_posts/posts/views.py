from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    data = {"a":9}
    data = {"b":5}
    return render(request,"index.html",context=data)