import json
import uuid
import boto3

client = boto3.client('lambda')

def lambda_handler(event, context):
    inputForInvoker = {'CustomerId': event['queryStringParameters']['customerId'], 'Amount': '50'}

    response = client.invoke(
        FunctionName = 'arn:aws:lambda:us-east-1:505176038322:function:sam-app-LambdaToInvokeFunction-jI5OahBlpPp2',
        InvocationType='RequestResponse', # Event
        Payload=json.dumps(inputForInvoker)
    )

    responseJson = json.load(response['Payload'])
    
    print('\n')
    print(responseJson)
    print('\n')

    return {
        "statusCode": 200,
        "body": json.dumps(responseJson),
    }

    
