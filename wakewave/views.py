from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


def home(request):
    return render(request, 'home.html')


def signup(request):
    return render(request, 'signup.html')

def change_theme(request, **kwargs):
    if 'is_dark_theme' in request.session:
        request.session["is_dark_theme"] = not request.session.get('is_dark_theme')
    else:
        request.session["is_dark_theme"] = True
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

