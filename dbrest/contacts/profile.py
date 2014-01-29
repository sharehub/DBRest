from django.views.generic.base import View
from django.http import HttpResponse
from django.conf import settings
from models import Profile 

# code avaiable for USTRID
URL_USER=settings.CONTACT_URL['user']
URL_STRID=settings.CONTACT_URL['strid']
URL_CONTACT=settings.CONTACT_URL['contact']

class ProfileView(View):
    """
    Handler the contacts GET/PUT/POST/DELETE request
    """
    def get_admin(self, request, arg, kwargs):
        return HttpResponse("Hello Get Profile " + Profile.uusid(kwargs[URL_USER].encode()))

    def get_api(self, request, arg, kwargs):
        return HttpResponse("Hello Get "+ kwargs[URL_STRID] +" Profile")

    def get(self, request, *arg, **kwargs):
        if (URL_USER in kwargs):
            return self.get_admin(request, arg, kwargs)
        else:
            return self.get_api(request, arg, kwargs)

    def put(self, request, *arg, **kwargs):
        return HttpResponse("Hello Put Profile")

    def post(self, request, *arg, **kwargs):
        username=request.POST('username')
        if (None == username):
            return HttpResponse("Error, username should not NULL")
        ustrid = self.uusid(username)

        return HttpResponse("Hello post"+ustrid+"Profile")

    def delete(self, request, *arg, **kwargs):
        return HttpResponse("Hello delete Profile")

    # patch, head, option, trace are not support yet

