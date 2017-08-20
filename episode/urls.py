from django.conf.urls import url
from episode import views

urlpatterns = [
    url(r'^$', views.home)
]
