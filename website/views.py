from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index_view(request):
    return render(request, 'website/index.html')

def contacto_view(request):
    return render(request, 'website/contacto.html')