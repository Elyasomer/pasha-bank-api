import requests
from typing import Dict, Optional, Any
from .constants import Language, Currency


class PashaBankAPI:
    def __init__(self, base_url: str, ssl_cert: str, ssl_key: str, ssl_pass: str) -> None:
        """
        Initialize the PashaBankAPI client.

        Args:
            base_url (str): Base URL for the API.
            ssl_cert (str): Path to the SSL certificate file.
            ssl_key (str): Path to the SSL key file.
            ssl_pass (str): SSL password.
        """
        self.base_url = base_url
        self.ssl_cert = ssl_cert
        self.ssl_key = ssl_key
        self.ssl_pass = ssl_pass
        self.session = requests.Session()
        self.session.verify = False

    def parse_response(self, response: requests.Response) -> Dict[str, str]:
        """
        Parse the text response from the API.

        Args:
            response (requests.Response): The response object.

        Returns:
            Dict[str, str]: Parsed response as a dictionary.
        """
        result = response.text.strip()
        parsed_result = {}
        for line in result.split("\n"):
            if ": " in line:
                key, value = line.split(": ", 1)
                parsed_result[key.strip()] = value.strip()
        return parsed_result

    def make_request(self, payload: Dict[str, Any]) -> Dict[str, str]:
        """
        Make a request to the API.

        Args:
            payload (Dict[str, Any]): The payload for the request.

        Returns:
            Dict[str, str]: The parsed response from the API.
        """
        response = self.session.post(
            url=self.base_url,
            data=payload,
            cert=(self.ssl_cert, self.ssl_key),
            headers={"Content-Type": "application/x-www-form-urlencoded"}
        )
        response.raise_for_status()
        return self.parse_response(response)

    def start_sms_transaction(self, amount: str, currency: Currency, client_ip_addr: str, terminal_id: Optional[str] = None, description: Optional[str] = None, language: Optional[Language] = None) -> Dict[str, str]:
        """
        Start an SMS transaction.

        Args:
            amount (str): Amount of the transaction.
            currency (Currency): Currency code.
            client_ip_addr (str): Client IP address.
            terminal_id (Optional[str]): Terminal ID provided by the bank.
            description (Optional[str]): Description of the transaction.
            language (Optional[Language]): Language code.

        Returns:
            Dict[str, str]: The response from the API.
        """
        payload = {
            'command': 'v',
            'amount': amount,
            'currency': currency.value,
            'client_ip_addr': client_ip_addr,
            'msg_type': 'SMS',
            'terminal_id': terminal_id
        }
        if description:
            payload['description'] = description
        if language:
            payload['language'] = language.value

        return self.make_request(payload)

    def start_card_sms_transaction(self, amount: str, currency: Currency, client_ip_addr: str, cardname: str, pan: str, expiry: str, cvv2: str, description: Optional[str] = None, language: Optional[Language] = None) -> Dict[str, str]:
        """
        Start a card SMS transaction.

        Args:
            amount (str): Amount of the transaction.
            currency (Currency): Currency code.
            client_ip_addr (str): Client IP address.
            cardname (str): Cardholder name.
            pan (str): Primary Account Number (card number).
            expiry (str): Expiry date of the card.
            cvv2 (str): CVV2 code of the card.
            description (Optional[str]): Description of the transaction.
            language (Optional[Language]): Language code.

        Returns:
            Dict[str, str]: The response from the API.
        """
        payload = {
            'command': 'i',
            'amount': amount,
            'currency': currency.value,
            'client_ip_addr': client_ip_addr,
            'cardname': cardname,
            'pan': pan,
            'expiry': expiry,
            'cvv2': cvv2,
            'msg_type': 'SMS'
        }
        if description:
            payload['description'] = description
        if language:
            payload['language'] = language.value

        return self.make_request(payload)

    def start_dms_authorization(self, amount: str, currency: Currency, client_ip_addr: str, description: Optional[str] = None, language: Optional[Language] = None) -> Dict[str, str]:
        """
        Start a DMS authorization.

        Args:
            amount (str): Amount of the transaction.
            currency (Currency): Currency code.
            client_ip_addr (str): Client IP address.
            description (Optional[str]): Description of the transaction.
            language (Optional[Language]): Language code.

        Returns:
            Dict[str, str]: The response from the API.
        """
        payload = {
            'command': 'a',
            'amount': amount,
            'currency': currency.value,
            'client_ip_addr': client_ip_addr,
            'msg_type': 'DMS'
        }
        if description:
            payload['description'] = description
        if language:
            payload['language'] = language.value

        return self.make_request(payload)

    def dms_transaction(self, trans_id: str, amount: str, currency: Currency, client_ip_addr: str, description: Optional[str] = None, language: Optional[Language] = None) -> Dict[str, str]:
        """
        Perform a DMS transaction.

        Args:
            trans_id (str): Transaction ID.
            amount (str): Amount of the transaction.
            currency (Currency): Currency code.
            client_ip_addr (str): Client IP address.
            description (Optional[str]): Description of the transaction.
            language (Optional[Language]): Language code.

        Returns:
            Dict[str, str]: The response from the API.
        """
        payload = {
            'command': 't',
            'trans_id': trans_id,
            'amount': amount,
            'currency': currency.value,
            'client_ip_addr': client_ip_addr,
            'msg_type': 'DMS'
        }
        if description:
            payload['description'] = description
        if language:
            payload['language'] = language.value

        return self.make_request(payload)

    def reversal(self, trans_id: str, amount: Optional[str] = None, suspected_fraud: Optional[str] = None) -> Dict[str, str]:
        """
        Perform a transaction reversal.

        Args:
            trans_id (str): Transaction ID.
            amount (Optional[str]): Amount of the transaction.
            suspected_fraud (Optional[str]): Suspected fraud indicator.

        Returns:
            Dict[str, str]: The response from the API.
        """
        payload = {
            'command': 'r',
            'trans_id': trans_id
        }
        if amount:
            payload['amount'] = amount
        if suspected_fraud:
            payload['suspected_fraud'] = suspected_fraud

        return self.make_request(payload)

    def refund(self, trans_id: str, amount: Optional[str] = None) -> Dict[str, str]:
        """
        Perform a transaction refund.

        Args:
            trans_id (str): Transaction ID.
            amount (Optional[str]): Amount of the transaction.

        Returns:
            Dict[str, str]: The response from the API.
        """
        payload = {
            'command': 'k',
            'trans_id': trans_id
        }
        if amount:
            payload['amount'] = amount

        return self.make_request(payload)

    def recurring_payment_registration(self, command: str, amount: str, currency: Currency, client_ip_addr: str, biller_client_id: str, perspayee_expiry: str, description: Optional[str] = None, language: Optional[Language] = None, perspayee_gen: int = 1, perspayee_overwrite: int = 0) -> Dict[str, str]:
        """
        Register a recurring payment.

        Args:
            command (str): Command for the recurring payment.
            amount (str): Amount of the transaction.
            currency (Currency): Currency code.
            client_ip_addr (str): Client IP address.
            biller_client_id (str): Biller client ID.
            perspayee_expiry (str): Perspayee expiry date.
            description (Optional[str]): Description of the transaction.
            language (Optional[Language]): Language code.
            perspayee_gen (int): Perspayee generation.
            perspayee_overwrite (int): Perspayee overwrite.

        Returns:
            Dict[str, str]: The response from the API.
        """
        payload = {
            'command': command,
            'amount': amount,
            'currency': currency.value,
            'client_ip_addr': client_ip_addr,
            'biller_client_id': biller_client_id,
            'perspayee_expiry': perspayee_expiry,
            'perspayee_gen': perspayee_gen,
            'perspayee_overwrite': perspayee_overwrite
        }
        if description:
            payload['description'] = description
        if language:
            payload['language'] = language.value

        return self.make_request(payload)

    def recurring_payment_execution(self, biller_client_id: str, amount: str, currency: Currency, client_ip_addr: str, description: Optional[str] = None) -> Dict[str, str]:
        """
        Execute a recurring payment.

        Args:
            biller_client_id (str): Biller client ID.
            amount (str): Amount of the transaction.
            currency (Currency): Currency code.
            client_ip_addr (str): Client IP address.
            description (Optional[str]): Description of the transaction.

        Returns:
            Dict[str, str]: The response from the API.
        """
        payload = {
            'command': 'e',
            'amount': amount,
            'currency': currency.value,
            'client_ip_addr': client_ip_addr,
            'biller_client_id': biller_client_id
        }
        if description:
            payload['description'] = description

        return self.make_request(payload)

    def recurring_payment_deletion(self, biller_client_id: str) -> Dict[str, str]:
        """
        Delete a recurring payment.

        Args:
            biller_client_id (str): Biller client ID.

        Returns:
            Dict[str, str]: The response from the API.
        """
        payload = {
            'command': 'x',
            'biller_client_id': biller_client_id
        }

        return self.make_request(payload)

    def transaction_result(self, trans_id: str) -> Dict[str, str]:
        """
        Get the result of a transaction.

        Args:
            trans_id (str): Transaction ID.

        Returns:
            Dict[str, str]: The response from the API.
        """
        payload = {
            'command': 'c',
            'trans_id': trans_id
        }

        return self.make_request(payload)
