from django.views.generic.base import View
from django.http import HttpResponse

class ContactsView(View):
    """
    Handler the contacts GET/PUT/POST/DELETE request
    """
    def get(self, request, *arg, **kwargs):
        return HttpResponse("Hello Get")

    def put(self, request, *arg, **kwargs):
        return HttpResponse("Hello Put")

    def post(self, request, *arg, **kwargs):
        return HttpResponse("Hello post")

    def delete(self, request, *arg, **kwargs):
        return HttpResponse("Hello delete")

    # patch, head, option, trace are not support yet

