from django.shortcuts import render
from django.http import HttpResponse
from .models import Category,Transaction

def index(request):
    context = {
        'category_list': Category.objects.all()
    }
    return render(request,'transactions/index.html',context)

def details(request,category_id):
    return HttpResponse(f"Estas viendo el detalle de la categoria {category_id}")

def details_dates(request,category_id):
    return HttpResponse(f"Estas viendo el detalle de la categoria por rango de fecha {category_id}")