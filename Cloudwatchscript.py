
import boto3
import time
import logging
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger()

# Create a CloudWatch Logs client
client = boto3.client('logs', region_name='us-east-1')

log_group = 'my-log-group'
log_stream = 'my-log-stream'

def create_log_group():
    try:
        client.create_log_group(logGroupName=log_group)
        logger.info(f"Created log group: {log_group}")
    except client.exceptions.ResourceAlreadyExistsException:
        logger.info(f"Log group {log_group} already exists")

def create_log_stream():
    try:
        client.create_log_stream(logGroupName=log_group, logStreamName=log_stream)
        logger.info(f"Created log stream: {log_stream}")
    except client.exceptions.ResourceAlreadyExistsException:
        logger.info(f"Log stream {log_stream} already exists")

def get_sequence_token():
    response = client.describe_log_streams(logGroupName=log_group, logStreamNamePrefix=log_stream)
    return response['logStreams'][0].get('uploadSequenceToken')

def put_log_events(message, sequence_token=None):
    log_event = {
        'logGroupName': log_group,
        'logStreamName': log_stream,
        'logEvents': [
            {
                'timestamp': int(time.time() * 1000),
                'message': message
            }
        ],
    }
    if sequence_token:
        log_event['sequenceToken'] = sequence_token

    response = client.put_log_events(**log_event)
    return response.get('nextSequenceToken')

def main():
    create_log_group()
    create_log_stream()
    sequence_token = get_sequence_token()
    
    try:
        message = "Log message:"
        sequence_token = put_log_events(message, sequence_token)
        logger.info(f"Successfully sent log message to {log_group}/{log_stream}")
    except (NoCredentialsError, PartialCredentialsError):
        logger.error("AWS credentials not found.")
    except Exception as e:
        logger.error(f"Failed to send log message: {e}")

if __name__ == "__main__":
    main()

def fuction():
    sequence_token = put_log_events(message, sequence_token)
    logger.error("AWS credentials not found.")
    return response['logStreams'][1].get('uploadSequenceToken')

print(sequence_token)
    
