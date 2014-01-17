from django.views.generic.base import View
from django.http import HttpResponse

Class AuthView(View):
    """
    Deal with login/logout/register/delete
    """

    def get(self, request, *arg, **kwargs):
        """
        Logout
        """

    def post(self, request, *arg, **kwargs):
        """
        Login/Register
        """
        pass

    def put(self, request, *arg, **kwargs):
        """
        Update Profile/Password/Email
        """
        pass

    def delete(self, request, *arg, **kwargs):
        """
        Destroy account
        """
        pass
