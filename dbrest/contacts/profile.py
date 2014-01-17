from django.views.generic.base import View
from django.http import HttpResponse
import uuid
import string

# code avaiable for USTRID
IDCODE='aZbY9cXdW8eVfU7gThS6iRjQ5kPlO4mNnM3oLpK2qJrI1sHtG0uFvEwDxCyBzA'
IDCODE_LEN=len(IDCODE)

class ProfileView(View):
    """
    Handler the contacts GET/PUT/POST/DELETE request
    """
    def get(self, request, *arg, **kwargs):
        return HttpResponse("Hello Get Profile")

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
        ustrid = []
        uuids = string.join(str(uuid.uuid5(uuid.NAMESPACE_X500, uname)).split('-'), '')
        str1, str2 = uuids[::2], uuids[1::2]
        for id in zip(str1, str2):
            ustrid.append(IDCODE[(int(id[0], 16)*2+int(id[1], 16)*3)%IDCODE_LEN]) 


        return string.join(ustrid, '')
        
        
    # patch, head, option, trace are not support yet

