from django.views.generic.base import View
from django.http import HttpResponse

from django.conf import settings

URL_USER=settings.CONTACT_URL['user']
URL_STRID=settings.CONTACT_URL['strid']
URL_CONTACT=settings.CONTACT_URL['contact']

class ContactsView(View):
    """
    Handler the contacts GET/PUT/POST/DELETE request
    """
    def get_admin(self, request, arg, kwargs):
        return HttpResponse("Hello Get User "+kwargs[URL_USER])

    def get_api(self, request, arg, kwargs):
        return HttpResponse("Hello Get browser "+kwargs[URL_STRID])

    def get(self, request, *arg, **kwargs):
        if (URL_USER in kwargs):
            return self.get_admin(request, arg, kwargs)
        else:
            return self.get_api(request, arg, kwargs)

    def put(self, request, *arg, **kwargs):
        return HttpResponse("Hello Put")

    def post(self, request, *arg, **kwargs):
        return HttpResponse("Hello post")

    def delete(self, request, *arg, **kwargs):
        return HttpResponse("Hello delete")

    # patch, head, option, trace are not support yet

