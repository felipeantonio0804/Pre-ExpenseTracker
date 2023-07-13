from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Category,Transaction

def index(request):
    context = {
        'category_list': Category.objects.all()
    }
    return render(request,'transactions/index.html',context)

def details(request,category_id):
    context = {
        'category': get_object_or_404(Category,pk=category_id)
    }
    return render(request,'transactions/details.html',context)

def details_dates(request,category_id):
    return HttpResponse(f"Estas viendo el detalle de la categoria por rango de fecha {category_id}")