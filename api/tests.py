from django.test import TestCase
from api.models import OrderApplications


class TestViews(TestCase):

    def test_is_this_thing_on(self):
        self.assertEqual('is this thing on?', 'this thing is on?')
