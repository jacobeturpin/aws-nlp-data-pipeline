"""Load and stream data"""

import json

import boto3


def load_data(fn):
    return pd.read_csv(fn) 

def push_to_lambda(records):
    client = boto3.client('lambda')
    lambda.invoke(
        FunctionName='IngestStack-handler',
        InvocationType='RequestResponse',
        Payload=json.dumps(
            {
                'data': records
            }
        )
    )

def main():
    pass

if __name__ == '__main__':
    main()
