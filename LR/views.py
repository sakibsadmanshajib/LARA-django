from django.shortcuts import render

from .models import Laptop
#from django.http import HttpResponse

def lists(request):
    latest_laptop_list = Laptop.objects.order_by('-price')[:30]
    context = {'latest_laptop_list': latest_laptop_list}
    return render(request, 'LR/lists.html', context)