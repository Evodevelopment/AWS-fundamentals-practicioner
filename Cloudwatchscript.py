
import boto3
import logging
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Create a CloudWatch Logs client
client = boto3.client('logs', region_name='us-east-1')

log_group = 'my-log-group'
log_stream = 'my-log-stream'

def create_log_group():
    try:
        client.create_log_group(logGroupName=log_group)
    except client.exceptions.ResourceAlreadyExistsException:
        pass

def create_log_stream():
    try:
        client.create_log_stream(logGroupName=log_group, logStreamName=log_stream)
    except client.exceptions.ResourceAlreadyExistsException:
        pass

def put_log_events(message, sequence_token=None):
    try:
        if sequence_token:
            response = client.put_log_events(
                logGroupName=log_group,
                logStreamName=log_stream,
                logEvents=[
                    {
                       
