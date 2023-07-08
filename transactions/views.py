from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world! This is the home page. of transactions app")