import boto3
from utilities.AwsUtilities import AwsUtilities
from utilities.DynamoUtilities import DynamoUtilities

SERVICE = 'dynamodb'
TABLE_NAME = "data_quality_logs"
ITEM = {
        "pipeline":"altice_invoice",
        "status": "Enable",
        "extraction": {
          "05-07-2023": "ok",
        "load": {
          "15-06-2023": {
                "register_amount": 55,
                "column_amount": 10,
                "column_names": ['field1', 'field2', 'field3']
                },
            }
        }
    }

TABLE_KEY = 'pipeline'
SEARCH_KEY = 'altice_invoice'

def main():

    ##Service Connection
    AWSObject = AwsUtilities(SERVICE)
    connection = AWSObject.service_connection()
    table = AWSObject.dynamo_table_connection(TABLE_NAME, connection)


    ##Dynamo
    Dynamo_object = DynamoUtilities(connection, table)
    
    #Create object
    create_item = Dynamo_object.create_item(ITEM) 
    print(type(create_item))

    #Read Object
    #read_item = Dynamo_object.read_item(TABLE_KEY, SEARCH_KEY)
    #print(read_item)

    #Delete Object
    #delete_item = Dynamo_object.delete_item(TABLE_KEY, 'other_pipeline')

if __name__ == "__main__":
    main()
