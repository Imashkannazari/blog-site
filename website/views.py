from django.http import HttpResponse
from django.shortcuts import render

def home(requests):
    return render(requests, "index.html")

def about(requests):
    return render(requests, "about.html")

def contact(requests):
    return render(requests, "contact.html")