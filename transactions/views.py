from datetime import date

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import  reverse
from django.views import generic
from .models import Category,Transaction

class IndexView(generic.ListView):
    template_name = 'transactions/index.html'
    context_object_name = 'category_list'
    
    def get_queryset(self):
        return Category.objects.order_by("name")
        #Para obtener las 5 primeras categorias por fecha ordenada y de mas recientes a mas antiguas
        #return Category.objects.order_by("-pub_date")[:5]

# ListView
# def index(request):
#     context = {
#         'category_list': Category.objects.all()
#     }
#     return render(request,'transactions/index.html',context)

# class DetailsView(generic.DetailView):
#     model = Category
#     template_name = 'transactions/details.html'
#     slug_field = 'id'


#DetailView
def details(request,category_id):
    context = {
        'category': get_object_or_404(Category,pk=category_id),
        'transactions': get_object_or_404(Category,pk=category_id).transaction_set.filter(date__lte=date.today()).order_by('-date')
    }
    return render(request,'transactions/details.html',context)

class DetailsCategoryView(generic.DetailView):
    model = Category
    template_name = 'transactions/details_category.html'
    slug_field = 'id'

#DetailView
# def details_category(request,category_id):
#     context = {
#         'category': get_object_or_404(Category,pk=category_id)
#     }
#     return render(request,'transactions/details_category.html',context)

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

class DetailsResultsCategoryView(generic.DetailView):
    model = Category
    template_name = 'transactions/results.html'
    slug_field = 'id' 

#DetailView    
# def details_results_category(request,category_id):
#     context = {
#         'category': get_object_or_404(Category,pk=category_id)
#     }
#     return render(request,'transactions/results.html',context)