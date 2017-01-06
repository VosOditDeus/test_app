from django.conf.urls import url
from . import views



urlpatterns =[
    url('^$', views.Main, name='main'),
    url('^login/$', views.Login, name='login'),
    url('^logout/$', views.Logout, name='logout'),
    url('^post/$', views.Post, name='post'),
    url('^messages/$', views.Messages, name='messages'),
    url('^registration/$', views.Register, name='register'),
]