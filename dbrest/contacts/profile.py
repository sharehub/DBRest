from django.views.generic.base import View
from django.http import HttpResponse

class ProfileView(View):
    """
    Handler the contacts GET/PUT/POST/DELETE request
    """
    def get(self, request, *arg, **kwargs):
        return HttpResponse("Hello Get Profile")

    def put(self, request, *arg, **kwargs):
        return HttpResponse("Hello Put Profile")

    def post(self, request, *arg, **kwargs):
        return HttpResponse("Hello post Profile")

    def delete(self, request, *arg, **kwargs):
        return HttpResponse("Hello delete Profile")

    # patch, head, option, trace are not support yet

