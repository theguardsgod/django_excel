from django.shortcuts import render

# Create your views here.


def toIndex(request):
    return render(request, 'index.html')

