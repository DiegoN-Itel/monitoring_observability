import boto3
import time

session = boto3.Session()
client = session.client('logs')

GROUP_NAME = "DSI-Pipelines"
STREAM_NAME = "Transform"

log_message = 'this is a test for transform' #e

log_response = client.put_log_events(
    logGroupName=GROUP_NAME,
    logStreamName=STREAM_NAME,
    logEvents=[
        {
            'timestamp': int(round(time.time()*1000)),
            'message': log_message
        }
    ]
)