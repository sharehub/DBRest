from django.http import HttpResponse

def home(request):
    return HttpResponse("Error! API browser only!")


