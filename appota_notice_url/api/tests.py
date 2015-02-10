from django.test import TestCase
from django.test import Client
# Create your tests here.

class NoticeUrlTestCase(TestCase):
    def test_notice_url(self):
        client = Client()
        post_data = {
            'status':1,
            'sandbox':1,
            'transaction_id':'trans_id',
            'transaction_type':'CARD',
            'card_code':'1234567890',
            'card_serial':'1234567890',
            'card_vendor':'VIETTEL',
            'amount':50000,
            'currency':'VND',
            'state':'State|User|Server',
            'target':'userid:1|username:mancityclub123',
            'country_code':'VN',
            'hash':'AppotaHash',
        }
        response = client.post('/api/notice_url_ios_appvn', post_data)