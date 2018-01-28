from django.conf.urls import url
from .import views

app_name = 'restaurant'

urlpatterns = [
    url(r'^test/$', views.test, name='home'),
    url(r'^$', views.home, name='home'),
    url(r'^about/$', views.about, name='home'),
    url(r'^contact/$', views.contact, name='home'),

]