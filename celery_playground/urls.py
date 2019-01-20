from django.views.generic.base import TemplateView
from django.conf.urls import url, include
from tasks import views

urlpatterns = [
     url(r'^add/$', views.Add.as_view()),
     url(r'^mult/$', views.Mult.as_view()),
]
