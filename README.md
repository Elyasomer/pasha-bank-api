
# PASHA Bank API Client

A Python client for interacting with PASHA Bank's API.

## Installation

First, ensure you have Poetry installed.

To set up the project, run the following commands:


```poetry install```


## Usage

### Initialization

To use the library, you first need to initialize the `PashaBankAPI` class with the necessary credentials.

```python
from pasha_bank_api import PashaBankAPI, Currency, Language

api = PashaBankAPI(
    base_url='https://ecomm.pashabank.az:18443/ecomm2/MerchantHandler',
    ssl_cert='path/to/cert.pem',
    ssl_key='path/to/key.pem',
    ssl_pass='your_password'
)
````

### Methods

#### Start SMS Transaction

Register a financial transaction without given card data for the purchase.

```python
response = api.start_sms_transaction(
    amount='100',
    currency=Currency.AZN,
    client_ip_addr='192.168.1.1',
    terminal_id='123456',
    description='Purchase description',
    language=Language.EN
)
print(response)
```

#### Start Card SMS Transaction

Register a financial transaction with given card data.

```python
response = api.start_card_sms_transaction(
    amount='100',
    currency=Currency.AZN,
    client_ip_addr='192.168.1.1',
    cardname='John Doe',
    pan='4111111111111111',
    expiry='1225',
    cvv2='123',
    description='Purchase description',
    language=Language.EN
)
print(response)
```

#### Start DMS Authorization

Register a DMS authorization.

```python
response = api.start_dms_authorization(
    amount='100',
    currency=Currency.AZN,
    client_ip_addr='192.168.1.1',
    description='Authorization description',
    language=Language.EN
)
print(response)
```

#### DMS Transaction

Perform a DMS transaction.

```python
response = api.dms_transaction(
    trans_id='12345',
    amount='100',
    currency=Currency.AZN,
    client_ip_addr='192.168.1.1',
    description='DMS transaction description',
    language=Language.EN
)
print(response)
```

#### Reversal

Perform a transaction reversal.

```python
response = api.reversal(
    trans_id='12345',
    amount='100',
    suspected_fraud='1'
)
print(response)
```

#### Refund

Perform a transaction refund.

```python
response = api.refund(
    trans_id='12345',
    amount='100'
)
print(response)
```

#### Recurring Payment Registration

Register a recurring payment.

```python
response = api.recurring_payment_registration(
    command='e',
    amount='100',
    currency=Currency.AZN,
    client_ip_addr='192.168.1.1',
    biller_client_id='biller123',
    perspayee_expiry='1225',
    description='Recurring payment registration',
    language=Language.EN,
    perspayee_gen=1,
    perspayee_overwrite=0
)
print(response)
```

#### Recurring Payment Execution

Execute a recurring payment.

```python
response = api.recurring_payment_execution(
    biller_client_id='biller123',
    amount='100',
    currency=Currency.AZN,
    client_ip_addr='192.168.1.1',
    description='Recurring payment execution'
)
print(response)
```

#### Recurring Payment Deletion

Delete a recurring payment.

```python
response = api.recurring_payment_deletion(
    biller_client_id='biller123'
)
print(response)
```

#### Transaction Result

Get the result of a transaction.

```python
response = api.transaction_result(
    trans_id='12345'
)
print(response)
```

## Running Tests

To run the tests, ensure you are in the Poetry shell, and run:

```
pytest
```

## License

This project is licensed under the MIT License.
