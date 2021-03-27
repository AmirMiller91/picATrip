from django.shortcuts import render


def addPost(request):
    return render(request, 'picogram/addPost.html')


def viewPosts(request):
    return render(request, 'picogram/viewPosts.html')
