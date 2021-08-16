from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .forms import UserRegisterForm
from .models import Usuario
from django.views import generic
from django.urls import reverse_lazy
# Create your views here.

@login_required()
def home(request):
    return render(request,"base.html")

@login_required()
def logoutUsuario(request):
    logout(request)
    return redirect('/accounts/login/')