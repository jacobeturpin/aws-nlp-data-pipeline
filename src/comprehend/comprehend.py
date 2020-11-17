import base64
import json

import boto3

print('Loading function')


def lambda_handler(event, context):
    
    client = boto3.client('comprehend')
    output = []

    for record in event['records']:

        print(record['data'])

        payload = record['data']

        # Do custom processing on the payload here
        sentiment = client.detect_sentiment(Text=payload['text'], LanguageCode='en')
        payload.update(sentiment)
        enriched = json.dumps(payload)
        
        print(enriched)
            
        output_record = {
            'recordId': record['recordId'],
            'result': 'Ok',
            'data': base64.b64encode(enriched.encode()).decode()
        }
        output.append(output_record)

    print('Successfully processed {} records.'.format(len(event['records'])))

    return {'records': output}
