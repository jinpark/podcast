import datetime

from django.test import TestCase
from django.utils import timezone
from django.core.files.uploadedfile import SimpleUploadedFile

from .models import Episode


class EpisodeModel(TestCase):

    def test_episode_name_length(self):
        """
        Episode name length does not matter.
        """
        audio_file = SimpleUploadedFile('some_podcast_file.mp3', (1024).to_bytes(2, byteorder='big'))
        episode = Episode.objects.create(name="""
                extra long name that is past the max number of characters
                extra long name that is past the max number of characters
                extra long name that is past the max number of characters
                """,
                duration=datetime.timedelta(hours=1), file=audio_file)
        response = self.client.get('/')
        self.assertIs(response.status_code, 200)
