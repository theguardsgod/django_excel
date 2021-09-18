from django.shortcuts import render

# Create your views here.
from django.views import generic
from .models import UserInfo

def toIndex(request):

    return render(request, 'index.html')

