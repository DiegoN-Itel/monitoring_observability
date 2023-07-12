import boto3
from utilities.AwsUtilities import AwsUtilities
from utilities.DynamoUtilities import DynamoUtilities

SERVICE = 'dynamodb'
TABLE_NAME = "format_changes_logs"
ITEM = {
    "pipeline":"altice_invoice",
    "status": "Enable",
    "extraction": {

      "05-07-2023": {
        "log": "missing fields: ['fieldn']"
      },
      "01-07-2023": {
        "log": "extra fields: ['field1', 'field2']"
      }
    },
    "load": {
      "15-06-2023": {
        "log": "wrong datatype fields: ['fieldn']"
     },
      "30-06-2023": {
        "log": "Not allowed values: ['fieldn']"
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
    
    #Read Object
    #read_item = Dynamo_object.read_item(TABLE_KEY, SEARCH_KEY)
    #print(read_item)

    #Delete Object
    #delete_item = Dynamo_object.delete_item(TABLE_KEY, 'altice_invoice')

if __name__ == "__main__":
    main()
