import base64
import json

import boto3

print('Loading function')


def lambda_handler(event, context):
    
    client = boto3.client('comprehend')
    output = []

    for record in event['records']:
        print(record['recordId'])
        payload = base64.b64decode(record['data']).decode("utf-8") 

        print(payload)

        # Do custom processing on the payload here
        sentiment = client.detect_sentiment(Text=payload, LanguageCode='en')
        enriched = json.dumps({
            'Data': payload,
            'Sentiment': sentiment})
        
        print(enriched)
            
        output_record = {
            'recordId': record['recordId'],
            'result': 'Ok',
            'data': base64.b64encode(enriched.encode()).decode()
        }
        output.append(output_record)

    print('Successfully processed {} records.'.format(len(event['records'])))

    return {'records': output}
