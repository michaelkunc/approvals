from django.test import TestCase
from api.models import OrderApplications


class TestViews(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.order_apps = OrderApplications.objects.create(
            application_id=1,
            status='approved',
            person_id=1,
            max_affordability_cents=20,
            max_affordability_currency='USD',
            created_at='2016-09-29T07:31:50.267984Z',
            updated_at='2016-09-29T07:31:50.267984Z',
            vehicle_reference_id='vehicle',
            locked_application={'key': 'value'},
            threatmetrix_session_id='session',
            partial_application={'key': 'value'})

    def test_response_code(self):
        response = self.client.get('/orderapplications/')
        self.assertEqual(200, response.status_code)

    def test_data(self):
        response = self.client.get('/orderapplications/')
        self.assertEqual(1, response.json()[0]['application_id'])
        self.assertEqual('approved', response.json()[0]['status'])
        self.assertEqual('2016-09-29T07:31:50.267984Z',
                         response.json()[0]['updated_at'])

    def test_application_status_y_year_month(self):
        response = self.client.get(
            '/orderapplications/status/?approved=Y&year=2016&month=9')
        self.assertEqual(1, response.json()['approved_applications'])

    def test_application_status_y_year(self):
        response = self.client.get(
            '/orderapplications/status/?approved=Y&year=2016')
        self.assertEqual(1, response.json()['approved_applications'])

    def test_application_status_y_year_month_negative(self):
        response = self.client.get(
            '/orderapplications/status/?approved=Y&year=2016&month=8')
        self.assertEqual(0, response.json()['approved_applications'])

    def test_application_status_y_year_negative(self):
        response = self.client.get(
            '/orderapplications/status/?approved=Y&year=2015')
        self.assertEqual(0, response.json()['approved_applications'])

    def test_application_status_no_year_month(self):
        response = self.client.get('/orderapplications/status/')
        self.assertEqual(0, response.json()['denied_applications'])
