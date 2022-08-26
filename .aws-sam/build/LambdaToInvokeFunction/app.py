import json
import uuid

# import requests


def lambda_handler(event, context):

    customerId = event['CustomerId']
    
    transactionId = str(uuid.uuid1())

    # 3 do some stuff - save to s3, write to database, etc.

    # 4 format and return response
    
    return {
        'CustomerId': customerId, 
        'Success': 'SOMETHING', 
        'TransactionId': transactionId
    }
