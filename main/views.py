from django.shortcuts import render

def index(request):
# Render index template
    return render(request, 'index.html')
# Create your views here.
