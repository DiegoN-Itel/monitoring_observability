import boto3

TABLE_NAME = "format_metadata"
KEY = "altice_invoice"

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table(TABLE_NAME)

response = table.update_item(
    Key={'pipeline':KEY},
    UpdateExpression="set #new_field=:nt",
    ExpressionAttributeNames={
        '#new_field': "tables" 
    },
    ExpressionAttributeValues={
        ':nt': {"nrrc": {
                    "organization" : "S",
		            "location" : "N",
                    }
                }
    }

)

print(response)