import datetime

from django.test import TestCase
from django.utils import timezone

from .models import Episode


class EpisodeModel(TestCase):

    def test_episode_name_length(self):
        """
        was_published_recently() returns False for questions whose pub_date
        is in the future.
        """

        episode = Episode(name="""
                extra long name that is past the max number of characters
                extra long name that is past the max number of characters
                extra long name that is past the max number of characters
                """)
        response = self.client.get(Episode.objects.all())
        self.assertIs(response.status_code, 200)
