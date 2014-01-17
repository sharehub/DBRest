from django.conf.urls import patterns, include, url
from django.conf import settings

# Here, user contacts.profile will cause some 'mismatch' since contacts is also a module
from profile import ProfileView
from contacts import ContactsView

strid = settings.CONTACT_URL['strid']
user = settings.CONTACT_URL['user']
contact = settings.CONTACT_URL['contact']

urlpatterns = patterns('',
    url(r'^api/(?P<'+strid+r'>\w{16})/$', ProfileView.as_view()),
    url(r'^api/(?P<'+strid+r'>\w{16})/(?P<'+contact+r'>\d+)/$', ContactsView.as_view()),
    url(r'^(?P<'+user+r'>\w{5,18})/(?P<'+strid+r'>\w{16})/$', ProfileView.as_view()),
    url(r'^(?P<'+user+r'>\w{5,18})/(?P<'+strid+r'>\w{16})/(?P<'+contact+r'>\d+)/$', ContactsView.as_view()),
)
