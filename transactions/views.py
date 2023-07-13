from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world! This is the home page. of transactions app")

def details(request,category_id):
    return HttpResponse(f"Estas viendo el detalle de la categoria {category_id}")

def details_dates(request,category_id):
    return HttpResponse(f"Estas viendo el detalle de la categoria por rango de fecha {category_id}")