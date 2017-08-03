from test_plus.test import TestCase
from app.models import Document,PrintJob
# fro
# Create your tests here.

class BaseTestCase(TestCase):

    def setUp(self):
        self.d = Document()
        self.d.title="My new doc"
        self.d.brief = "this doc"
        self.d.save()

    # Testing the URLs

    def test_user_can_register(self):
        respose = self.client.get('/signup/')
        self.response_200(respose)

    def test_homepage_loads_without_errors(self):
        respose = self.client.get('/')
        self.response_200(respose)

    def test_pricing_is_fecthed_correctly(self):
        response = self.client.get('/pricing/')
        self.response_200(response)

    def test_document_can_be_created(self):
        
        self.assertIn(self.d,Document.objects.all())


    def test_print_job_can_be_created(self):
        # printjob = PrintJob()
        # printjob.document = self.d
        # printjob.copies = 3
        # printjob.cost = 40

        # printjob.save()
        
        # self.assertIsNotNone(printjob)

        pass


