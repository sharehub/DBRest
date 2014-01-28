from django.views.generic.base import View
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import redirect
from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from tools import ToolKits

class Authenticate(View):
    """
    Handler the authenticate relate
    """
    def get(self, request, *arg, **kwargs):
        """
        User logout
        """
        logout(request)
        return redirect("/")

    def post(self, request, *arg, **kwargs):
        """
        User login
        """
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse("Login Success!")
            else:
                return HttpResponse("You have been blocked!")
        else:
            return HttpResponse("Are you kidding?")

    def put(self, request, *arg, **kwargs):
        """
        Register for user
        """
        ToolKits.coerce_put(request)
        username = request.PUT['username']
        password = request.PUT['password']
        email = request.PUT['email']
        if None in (username, password, email):
            return HttpResponse("What's the matter? why information not full")
        
        user = User.objects.create_user(username, email=email, password=password)
        if user is None:
            return HttpResponse("information not correctly!")

        user.save()
        login(request, authenticate(username=username, password=password))
        return HttpResponse("Hello, welcome "+username)

    @csrf_exempt
    def dispatch(self, *args, **kwargs):
        """
        The dispatch handler
        """
        return super(Authenticate, self).dispatch(*args, **kwargs)
