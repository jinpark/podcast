from django.db import models
from django.utils import timezone


class Episode(models.Model):
    name = models.CharField(max_length=200)
    file = models.FileField(upload_to='audio/podcast')
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(default=timezone.now)
    duration = models.DurationField()
    description = models.TextField()
    number = models.PositiveIntegerField(default=1, help_text="The episode number")
    order = models.PositiveIntegerField(default=1, help_text="Order of the episode")
    show_notes = models.TextField(help_text="Show notes here!")
