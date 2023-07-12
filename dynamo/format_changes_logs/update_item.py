import boto3
from datetime import date

TABLE_NAME = "format_changes_logs"
KEY_FIELD = 'pipeline'
KEY = "altice_invoice"

def main():
    connection = dynamo_connection()
    table = table_connection(TABLE_NAME, connection)
    object = get_object(table, KEY_FIELD, KEY)

    new_object = add_extraction_log(object, 'example of log')

    #Add extraction log to Dynamo
    update_dynamo_field(table, KEY_FIELD, KEY, 'extraction', new_object['extraction'])

def dynamo_connection() -> boto3.resources:

    dynamodb = boto3.resource('dynamodb')

    return dynamodb

def table_connection(table_name: str,
                      connection: boto3.resources) -> boto3.resources:

    table = connection.Table(table_name)

    return table

def get_object(table: boto3.resources,
               key_field: str,
               key: str) -> dict:
    
    response = table.get_item(
                Key={
                    key_field: key,
                }
            )
    
    return response['Item']

def add_extraction_log(object: dict,
                       log_value: str) -> dict:
    
    today = date.today()
    object['extraction'][str(today)] = {'log': log_value}

    return object

def add_load_log(object: dict,
                 log_key: str,
                 log_value: str) -> dict:
    
    today = date.today()
    object['load'][str(today)] = {'log': log_value}

    return object

def update_dynamo_field(table: boto3.resources,
                  key_field: str,
                  key: str,
                  field: str,
                  new_object: dict):
    
    response = table.update_item(
                    Key={key_field:key},
                    UpdateExpression="set #new_field=:nt",
                    ExpressionAttributeNames={
                            '#new_field': field 
                        },
                    ExpressionAttributeValues={
                            ':nt': new_object
                        }
                )
    
    print(type(response))

    return response

if __name__ == "__main__":
    main()