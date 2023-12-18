import json
import boto3
import uuid
from datetime import datetime

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('NotesTable')

def lambda_handler(event, context):
    try:
        data = json.loads(event['body'])
        note_id = str(uuid.uuid4())
        timestamp = datetime.now().isoformat()

        item = {
            'NoteID': note_id,
            'Title': data['title'],
            'Content': data['content'],
            'Timestamp': timestamp
        }

        table.put_item(Item=item)

        return {
            'statusCode': 200,
            'body': json.dumps(item)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(str(e))
        }
