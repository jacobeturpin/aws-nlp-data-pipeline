"""Load and stream data"""

import json

import boto3
import pandas as pd


DATA = 'tweets.csv'

def load_data(fn):
    return pd.read_csv(fn) 

def push_to_lambda(records):
    client = boto3.client('lambda', region_name='us-east-1')
    client.invoke(
        FunctionName='IngestStack-handler',
        InvocationType='RequestResponse',
        Payload=json.dumps(
            {
                'data': records
            }
        )
    )

def main():
    df = pd.read_csv(DATA, engine='python', quoting=1)
    df = df.head(250)

    print(df.head())

    def chunker(seq, size):
        return (seq[pos:pos + size] for pos in range(0, len(seq), size))

    for i in chunker(df,5):
        records = i.to_json(orient='records')
        push_to_lambda(records)

if __name__ == '__main__':
    main()
