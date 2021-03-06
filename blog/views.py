from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt, csrf_protect

from validate_email import validate_email

from .models import Blogs, Profile

import random
import re


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
    # https://simpleisbetterthancomplex.com/tutorial/2017/02/18/how-to-create-user-sign-up-view.html#sign-up-with-confirmation-mail
    return render(request, 'signup.html', {})

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

def loginUser(request):
    # Login User
    return render(request, 'login.html', {})


@csrf_protect
def signupUserCheck(request):
    # Get variables from post
    user_name = request.POST.get('username', '')
    email = request.POST.get('email', '')
    password = request.POST.get('password', '')

    data = {}

    # Check username is not in use, case insensitive
    if user_name != '':
        data['exists'] = False

        if User.objects.filter(username__iexact=user_name).exists():
            data['exists'] = True

    # Check email is valid
    if email != '':
        data['correct'] = False
        if validate_email(email):
            data['correct'] = True

    # Check password conforms
    if password != '':
        data['correct'] = True
        if (len(password)<6):
            data['correct'] = False
            data['error'] = "Length must be at least 6 characters"
        elif password.isalnum():
            data['correct'] = False
            data['error'] = "Must include non alpha numeric characters"
        elif not re.search("[a-z]",password):
            data['correct'] = False
            data['error'] = "Must include lower case characters"
        elif not re.search("[A-Z]",password):
            data['correct'] = False
            data['error'] = "Must include uppercase characters"
        elif not re.search("[0-9]",password):
            data['correct'] = False
            data['error'] = "Must include numeric characters"
        elif re.search("\s",password):
            data['correct'] = False
            data['error'] = "Must not include spaces"
        # Todo, check the first, last and user names are not incorporated in the password

    return JsonResponse(data)


@csrf_protect
def loginUserCheck(request):
    # Get variables from post
    user_name = request.POST.get('username', '')
    mem_one = request.POST.get('memone', '')
    mem_two = request.POST.get('memtwo', '')
    mem_thr = request.POST.get('memthr', '')
    password = request.POST.get('password', '')

    # Test username is valid
    if user_name != '':
        data = {
            'username': user_name,
        }

        if User.objects.filter(username=user_name).exists():
            data['exists'] = True

            # Generate 3 random integers
            user_profile = Profile.objects.get(user__username=user_name)
            login_three_characters = random.sample(range(0, len(user_profile.secret_word) - 1), 3)
            login_three_characters.sort()
            data['digits'] = login_three_characters

            request.session['user_name'] = user_name
            request.session['login_three_characters'] = login_three_characters

        else:
            data['exists'] = False

    # Test if memorable characters are correct
    if mem_one != '':
        user_profile = Profile.objects.get(user__username=request.session['user_name'])
        login_three_characters = request.session['login_three_characters']

        if (user_profile.secret_word[login_three_characters[0]] == mem_one and
            user_profile.secret_word[login_three_characters[1]] == mem_two and
            user_profile.secret_word[login_three_characters[2]] == mem_thr):

            data = { 'correct': True, }

        else:
            login_three_characters = random.sample(range(0, len(user_profile.secret_word) - 1), 3)
            login_three_characters.sort()
            data = { 'correct': False, 'digits': login_three_characters }

    # Try to login
    if password != '':
        data = { 'correct': False, }
        user = authenticate(request, username=request.session['user_name'], password=password)
        if user is not None:
            login(request, user)
            data = { 'correct': True, }

    return JsonResponse(data)


def logoutUser(request):
    # Logout User
    logout(request)
    return redirect('home',)
