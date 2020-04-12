from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    url(r'^login/$', LoginView.as_view(), {'template_name': 'users/login.html'},
        name='login'),
    url(r'^register', views.register, name='register'),
    url(r'^logout/$', LogoutView.as_view(), name='logout'),
]
