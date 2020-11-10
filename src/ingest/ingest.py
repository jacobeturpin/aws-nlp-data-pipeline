"""Forward records to Kinesis Firehose Stream"""

import json

import boto3

DELIVERY_STREAM_NAME = os.environ['STREAM_NAME']

def lambda_handler(event, context):
    
    client = boto3.client('firehose')

    response = client.put_record_batch(
        DeliveryStreamName=DELIVERY_STREAM_NAME,
        Records=[
            {
                'Data': record
            }
            for record in event['data']
        ]
    )

    return {
        'response': response
    }

