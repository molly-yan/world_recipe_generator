#from django.conf.urls import url
from NewApp import views
from django.urls import re_path


urlpatterns=[

    re_path(r'^employee/$',views.employeeApi),
    re_path(r'^employee/([0-9]+)$',views.employeeApi)
    

] 