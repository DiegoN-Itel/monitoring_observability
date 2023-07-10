import boto3

session = boto3.Session()
client = session.client('logs')

GROUP_NAME = "DSI-Pipelines"
STREAM_NAME1 = "Extract"
STREAM_NAME2 = "Transform"
STREAM_NAME3 = "Load"

group_name_creation = client.create_log_group(logGroupName=GROUP_NAME)
stream_name_creation1 = client.create_log_stream(logGroupName=GROUP_NAME, logStreamName=STREAM_NAME1)
stream_name_creation2 = client.create_log_stream(logGroupName=GROUP_NAME, logStreamName=STREAM_NAME2)
stream_name_creation3 = client.create_log_stream(logGroupName=GROUP_NAME, logStreamName=STREAM_NAME3)

