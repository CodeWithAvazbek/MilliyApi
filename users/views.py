from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    ctx = {
        "name": "Avazbek"
    }
    return render (request, 'hello.html', ctx)
