import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('NotesTable')

def lambda_handler(event, context):
    try:
        note_id = event['pathParameters']['noteId']
        table.delete_item(Key={'NoteID': note_id})

        return {
            'statusCode': 200,
            'body': json.dumps('Note deleted successfully')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(str(e))
        }
