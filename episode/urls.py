from django.conf.urls import url
from episode import views

urlpatterns = [
    url(r'^$', views.home, name='home_page'),
    url(r'^about', views.about, name='about_page')
]
