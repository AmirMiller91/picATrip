# from django.shortcuts import render
from django.http import HttpResponse


def addPost(request):
    return HttpResponse('<h1>Add a Post</h1>')
