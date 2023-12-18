import json
import boto3

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('NotesTable')

def lambda_handler(event, context):
    try:
        data = json.loads(event['body'])
        note_id = event['pathParameters']['noteId']

        response = table.update_item(
            Key={'NoteID': note_id},
            UpdateExpression="set Title=:t, Content=:c",
            ExpressionAttributeValues={
                ':t': data['title'],
                ':c': data['content']
            },
            ReturnValues="UPDATED_NEW"
        )

        return {
            'statusCode': 200,
            'body': json.dumps(response)
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(str(e))
        }
