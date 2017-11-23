from django.shortcuts import render
from django.conf import settings
from .models import Episode

def home(request, template="home.html"):
    context = {'episodes': Episode.objects.all().order_by('-order')}
    return render(request, template, context)

def about(request, template="about.html"):
    return render(request, template)

def feed(request, template="feed.xml"):
    return render(request, template,
        {"podcast_data": settings.PODCAST_DATA, "episodes": Episode.objects.all().order_by('order')},
        content_type='text/xml')
