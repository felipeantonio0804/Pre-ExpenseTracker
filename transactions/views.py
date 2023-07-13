from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import  reverse
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

def details_category(request,category_id):
    context = {
        'category': get_object_or_404(Category,pk=category_id)
    }
    return render(request,'transactions/details_category.html',context)

def details_results_transaction(request,category_id):
    return HttpResponse(f"Estas viendo el detalle de la categoria {category_id} para ver cuantas veces ha sido consultada esta transaccion por el contador")