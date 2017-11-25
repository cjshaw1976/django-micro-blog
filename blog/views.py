from django.shortcuts import render

from django.contrib.auth.models import User

from .models import Blogs

def home(request):
    return render(request, 'home.html', {})


def newPost(request):
    # User create a post
    return render(request, 'home.html', {})

def viewPost(reques, pk):
    # User view a post
    return render(request, 'home.html', {})

def editPost(request, pk):
    # User edit a post
    return render(request, 'home.html', {})

def deletePost(request, pk):
    # User delete a post
    return render(request, 'home.html', {})


def newUser(request, step=0):
    # New user
    # https://simpleisbetterthancomplex.com/tutorial/2016/08/01/how-to-upload-files-with-django.html
    return render(request, 'home.html', {})

def confirmUser(request, hashCode):
    # Confirm User Email
    return render(request, 'home.html', {})

def editUser(request):
    # Edit user
    return render(request, 'home.html', {})

def viewUser(request):
    # View User
    return render(request, 'home.html', {})

def postsUser(request):
    # List user posts
    return render(request, 'home.html', {})

def loginUser(request, username=''):
    # Login User
    return render(request, 'home.html', {})

def logoutUser(request):
    # Logout User
    return render(request, 'home.html', {})
