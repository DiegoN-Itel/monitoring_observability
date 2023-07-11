import boto3

TABLE_NAME = "format_metadata"
KEY_FIELD = 'pipeline'
KEY = "altice_invoice"

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table(TABLE_NAME)

response = table.get_item(
    Key={
        'pipeline': 'altice_invoice',
    }
)

print(response['Item'])
