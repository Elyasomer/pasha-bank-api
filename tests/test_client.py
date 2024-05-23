import unittest
from pasha_bank_api.client import PashaBankAPI
from pasha_bank_api.constants import Language, Currency


class TestPashaBankAPI(unittest.TestCase):
    def setUp(self):
        self.api = PashaBankAPI(
            base_url='https://ecomm.pashabank.az:18443/ecomm2/MerchantHandler',
            ssl_cert='.certs/certificate.0030938.pem',
            ssl_key='.certs/server.key',
            ssl_pass=None
        )

    def test_start_sms_transaction(self):
        response = self.api.start_sms_transaction(
            amount='100', currency=Currency.AZN, client_ip_addr='192.168.1.1', terminal_id='123456', language=Language.EN)
        self.assertIsInstance(response, dict)

    def test_start_card_sms_transaction(self):
        response = self.api.start_card_sms_transaction(amount='100', currency=Currency.AZN, client_ip_addr='192.168.1.1',
                                                       cardname='John Doe', pan='4111111111111111', expiry='1225', cvv2='123', language=Language.EN)
        self.assertIsInstance(response, dict)

    def test_start_dms_authorization(self):
        response = self.api.start_dms_authorization(
            amount='100', currency=Currency.AZN, client_ip_addr='192.168.1.1', language=Language.EN)
        self.assertIsInstance(response, dict)

    def test_dms_transaction(self):
        response = self.api.dms_transaction(
            trans_id='12345', amount='100', currency=Currency.AZN, client_ip_addr='192.168.1.1', language=Language.EN)
        self.assertIsInstance(response, dict)

    def test_reversal(self):
        response = self.api.reversal(trans_id='12345', amount='100')
        self.assertIsInstance(response, dict)

    def test_refund(self):
        response = self.api.refund(trans_id='12345', amount='100')
        self.assertIsInstance(response, dict)

    def test_recurring_payment_registration(self):
        response = self.api.recurring_payment_registration(
            command='z', amount='100', currency=Currency.AZN, client_ip_addr='192.168.1.1', biller_client_id='biller123', perspayee_expiry='1225', language=Language.EN)
        self.assertIsInstance(response, dict)

    def test_recurring_payment_execution(self):
        response = self.api.recurring_payment_execution(
            biller_client_id='biller123', amount='100', currency=Currency.AZN, client_ip_addr='192.168.1.1')
        self.assertIsInstance(response, dict)

    def test_recurring_payment_deletion(self):
        response = self.api.recurring_payment_deletion(
            biller_client_id='biller123')
        self.assertIsInstance(response, dict)

    def test_transaction_result(self):
        response = self.api.transaction_result(trans_id='12345')
        self.assertIsInstance(response, dict)


if __name__ == '__main__':
    unittest.main()
