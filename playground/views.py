from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q, F
from store.models import Customer, Collection, Product
# Create your views here.

def say_hello(request):
       
    queyset = Collection.objects.all()

    return render(request, 'hello.html', {'name': 'Mosh', 'collections': list(queyset)})