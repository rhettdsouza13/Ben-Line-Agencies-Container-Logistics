from django.shortcuts import render
from django.contrib.auth.decorators import *
# Create your views here.


def Home(request):
    return render(request,"index.html")

@login_required
def dashboard(request):
    return render(request, "first.html")
