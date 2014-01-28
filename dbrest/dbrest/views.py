from django.http import HttpResponse
from django.core.context_processors import csrf
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def home(request):
    response = HttpResponse("Error! API browser only!")
    response.set_cookie('cookie-test', 'testvalue', domain='.djan.cf')
    #response.set_cookie('cookie-testbbb', 'testvalueaaa') 
    # user should use ['X-CSRFToken'] HTTP header, from cookie
    return response


