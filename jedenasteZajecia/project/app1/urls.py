from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^htmltemplate$', views.html_template, name='html_template'),
    url(r'^msg/$', views.pass_a_paramater, name='pass_a_paramater'),
    url(r'^$', views.index, name='index'),
]
