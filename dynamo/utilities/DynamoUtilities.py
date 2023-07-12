import boto3

class DynamoUtilities:

    def __init__(self, connection, table_connection):
        self.connection = connection
        self.table_connection = table_connection

    def create_item(self,
                    new_item: dict) -> dict:
    
        response = self.table_connection.put_item(
            Item= new_item
        )

        return response
    
    def read_item(self,
                  table_key: str,
                  search_key: str) -> dict:
        
        response = self.table_connection.get_item(
            Key={
                table_key: search_key,
                }
                )

        return response['Item']