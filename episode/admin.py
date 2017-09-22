from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Episode


class EpisodeAdmin(SummernoteModelAdmin):
    pass

admin.site.register(Episode, EpisodeAdmin)
