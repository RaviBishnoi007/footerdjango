import imp
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Search

# Create your views here.


def footer(request):
    if request.method == "POST":
        searchdata = request.POST.get('search')
        datasearch = Search(searchdata=searchdata)
        datasearch.save()

    return render(request, "ecommakonbackend/footer.html")
