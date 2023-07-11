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
    )