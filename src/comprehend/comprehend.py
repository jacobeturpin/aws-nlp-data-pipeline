import base64
import json

import boto3

print('Loading function')


def lambda_handler(event, context):
    
    client = boto3.client('comprehend')
    output = []

    for record in event['records']:

        print(record['data'])

        payload = json.loads(
            base64.b64decode(record['data'])
        )

        sentiment = client.detect_sentiment(Text=payload['text'], LanguageCode='en')
        sentiment.pop('ResponseMetadata')
        payload.update(sentiment)
        enriched = json.dumps(payload)
            
        output_record = {
            'recordId': record['recordId'],
            'result': 'Ok',
            'data': enriched.encode()
        }
        output.append(output_record)

    print('Successfully processed {} records.'.format(len(event['records'])))

    return {'records': output}
