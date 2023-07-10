import boto3

dynamodb = boto3.resource('dynamodb')

table_creation_resp = dynamodb.create_table(
    TableName='DSI-Pipeline-error',
    KeySchema=[
        {
            'AttributeName': 'pipeline-error',
            'KeyType': 'HASH'  # Partition Key
        }
    ],
    AttributeDefinitions=[
        {
            'AttributeName': 'pipeline-error',
            'AttributeType': 'S'  # string data type
        }
    ],
    ProvisionedThroughput={
        'ReadCapacityUnits': 10,
        'WriteCapacityUnits': 20
    }
)