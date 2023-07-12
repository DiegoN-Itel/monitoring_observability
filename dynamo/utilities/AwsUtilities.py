import boto3

class AwsUtilities:

    def __init__(self, service):
        self.service = service

    def service_connection(self) -> boto3.resources:

        dynamodb = boto3.resource(self.service)

        return dynamodb

    def dynamo_table_connection(self,
                         table_name: str,
                         connection: boto3.resources) -> boto3.resources:

        table = connection.Table(table_name)

        return table