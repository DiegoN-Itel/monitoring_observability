import boto3

TABLE_NAME = "format_metadata"

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table(TABLE_NAME)

response = table.put_item(
        Item={
            "pipeline": "altice_invoice",
            "Status": 'Enable',
            "tables": {
                "nrrc": {
                    "organization" : "S",
		            "location" : "S",
                }
            }
            }
    )