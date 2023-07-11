import boto3

TABLE_NAME = "format_metadata"
KEY_FIELD = 'pipeline'
KEY = "altice_invoice"
field_tests = {
    'field1': 'str',
    'field2': 'str'
}

def main():
    connection = dynamo_connection()
    table = table_connection(TABLE_NAME, connection)
    object = get_object(table, KEY_FIELD, KEY)

    print(object)

    new_object = update_field_in_table(object, 'nrrc', 'date', 'int')
    print(new_object)
#    remove_nrrc_table = remove_table(object, 'nrrc')
#    add_new_table = add_table(object, 'new_test', field_tests)

    update_dynamo(table, KEY_FIELD, KEY, 'tables', new_object['tables'])

    print('do some changes')
    object1 = get_object(table, KEY_FIELD, KEY)

    print(object1)



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

def update_field_in_table(item: dict, 
               table_to_update: str,
               field_to_update: str,
               new_datatype: str) -> dict:
    
    item['tables'][table_to_update][field_to_update] = new_datatype
    
    return(item)

def remove_table(item: dict,
                 table_to_delete: str) -> dict:
    
    new_item = item['tables'].pop(table_to_delete)

    return new_item

def add_table(item:dict,
              table_new: str,
              fields: dict) -> dict:
    
    item['tables'][table_new] = fields

    print(item['tables'])

def update_dynamo(table: boto3.resources,
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