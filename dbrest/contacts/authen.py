from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout

class Authenticate(View):
    """
    Handler the authenticate relate
    """
    def get(self, request, *arg, **kwargs):
        logout(request)
        return redirect("/")

    @csrf_exempt
    def post(self, request, *arg, **kwargs):
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse("Login Success!")
            else:
                return HttpResponse("You have been blocked!")
        else:
            return HttpResponse("Are you kidding?")

