from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from restExample.views import FirstView, NewPersonView, DetailPersonView, ListPersonView

urlpatterns = [
    url(r'admin/', admin.site.urls),
    url(r'ping/', FirstView.as_view()),
    url(r'new-person', NewPersonView.as_view(), name="new_person"),
    url(r'^detail-person/(?P<pk>[0-9]+)$', DetailPersonView.as_view(), name="person_detail"),	
    url(r'list-person/', ListPersonView.as_view(), name="person_list")
]
