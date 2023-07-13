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

def details_consult_transaction(request,category_id):
    category = get_object_or_404(Category,pk=category_id)
    try:
        #Toma el valor de value del input, en base al name, request.POST['transaction']
        transaction = category.transaction_set.get(pk=request.POST['transaction'])
    #Controlar estos 2 tipos de errores
    except (KeyError,Transaction.DoesNotExist):
        context = { 
            'category': category,
            'error_message':'No se ha seleccionado una transacción antes de mandar a consultar.'
        }
        return render(request,'transactions/details_category.html',context)
    else:
        transaction.counter += 1
        transaction.save()
        return HttpResponseRedirect(reverse('transactionsApp:details_results_category',args=(category.id,)))
    
def details_results_category(request,category_id):
    return HttpResponse(f"Estas viendo el detalle de la categoria {category_id} para ver cuantas veces ha sido consultada esta transaccion por el contador")