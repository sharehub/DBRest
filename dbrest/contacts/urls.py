from django.conf.urls import patterns, include, url
# Here, user contacts.profile will cause some 'mismatch' since contacts is also a module
from profile import ProfileView
from contacts import ContactsView

urlpatterns = patterns('',
    url(r'^api/(?P<strid>[a-zA-Z0-9]{16})/$', ProfileView.as_view()),
    url(r'^api/(?P<strid>[a-zA-Z0-9]{16})/(?P<contact>\d+)/$', ContactsView.as_view()),
    url(r'^user/(?P<strid>[a-zA-Z0-9]{16})/', ProfileView.as_view()),
    url(r'^user/(?P<strid>[a-zA-Z0-9]{16})/(?P<contact>\d+)/$', ContactsView.as_view()),
)
