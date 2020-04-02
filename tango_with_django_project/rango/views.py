from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    aboutLink = '<a href="/rango/about/">About</a>'
    return HttpResponse("Rango says hey there partner!" + aboutLink)


def about(request):
    indexLink = '<a href="/rango/index/">Index</a>'
    return HttpResponse("Rango says here is the about page." + indexLink)
