from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from .models import Profile
from django.http import HttpResponse
from .forms import ProfileForm

# Create your views here.


def home(request):
    return HttpResponse('<h1>Hello /ᐠ｡‸｡ᐟ\ﾉ</h1>')


def about(request):
    return render(request, 'about.html')


def profile_create(request):
    profile_form = ProfileForm()

    return render(request, 'main_app/profile_form.html', {'form': profile_form})
