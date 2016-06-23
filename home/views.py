from django.shortcuts import render
from django.contrib.auth.decorators import *
# Create your views here.

@login_required(login_url = "/login/")
def Home(request):
    return render(request,"index.html")
