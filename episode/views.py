from django.shortcuts import render
from .models import Episode

def home(request, template="home.html"):
    context = {'episodes': Episode.objects.all().order_by('order')}
    context['episodes'] = Episode.objects.all()
    return render(request, template, context)

def about(request, template="about.html"):
    return render(request, template)

def feed(request, template="feed.xml"):
    return render(request, template, content_type='text/xml')
