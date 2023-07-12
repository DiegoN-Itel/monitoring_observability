import boto3
from utilities.AwsUtilities import AwsUtilities
from utilities.DynamoUtilities import DynamoUtilities

SERVICE = 'dynamodb'
TABLE_NAME = "format_metadata"
ITEM = {
            "pipeline": "other_pipeline2",
            "Status": 'Enable',
            "tables": {
                "nrrc": {
                    "organization" : "str",
		            "location" : "str",
		            "department" : "str",
		            "skill" : "str",
		            "language" : "str",
		            "agent_name" : "str",
		            "ps_id" : "str",
		            "date" : "date",
		            "half_hour_interval" : "date",
		            "not_ready_sec" : "int",
		            "not_ready_pct" : "int",
		            "not_ready_reason_code" : "str",
		            "not_ready_reason_count" : "int",
		            "not_ready_reason_duration" : "int",
		            "not_ready_reason_pct_duration" : "int"
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
    read_item = Dynamo_object.read_item(TABLE_KEY, SEARCH_KEY)
    print(read_item)

if __name__ == "__main__":
    main()
