from django.conf.urls import url
from episode import views

urlpatterns = [
    url(r'^feed.xml', views.feed, name="rss_feed"),
    url(r'^about', views.about, name="about_page"),
    url(r'^$', views.home, name="home_page")
]
