import uuid
import string

from django.views.generic.base import View
from django.http import HttpResponse
from django.conf import settings 

# code avaiable for USTRID
IDCODE_LEN=len(settings.PROFILE_CODE)
URL_USER=settings.CONTACT_URL['user']
URL_STRID=settings.CONTACT_URL['strid']
URL_CONTACT=settings.CONTACT_URL['contact']

class ProfileView(View):
    """
    Handler the contacts GET/PUT/POST/DELETE request
    """
    def get_admin(self, request, arg, kwargs):
        return HttpResponse("Hello Get Profile " + self.ustrid(kwargs[URL_USER].encode()))

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
        ustrid = self.ustrid(username)

        return HttpResponse("Hello post"+ustrid+"Profile")

    def delete(self, request, *arg, **kwargs):
        return HttpResponse("Hello delete Profile")

    def ustrid(self, uname):
        """
        return the uniq SN of user, uname should use ''.encode() to make it ascii 
        """
        ustrid = []
        uuids = ''.join(str(uuid.uuid5(uuid.NAMESPACE_X500, uname)).split('-'))
        str1, str2 = uuids[::2], uuids[1::2]
        for id in zip(str1, str2):
            idx = int(id[0], 16)*settings.PROFILE_MULTI[0]+int(id[1], 16)*settings.PROFILE_MULTI[1]
            ustrid.append(settings.PROFILE_CODE[idx%IDCODE_LEN])

        return ''.join(ustrid)
        
        
    # patch, head, option, trace are not support yet

