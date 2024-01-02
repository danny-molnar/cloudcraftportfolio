import json
from google.cloud import firestore

db = firestore.Client()

def delete_note(request):
    try:
        note_id = request.args.get('noteId')
        if not note_id:
            return json.dumps({'error': 'Missing noteId'}), 400

        note_ref = db.collection('notes').document(note_id)
        note_ref.delete()

        return json.dumps({'result': 'Note deleted'}), 200
    except Exception as e:
        return json.dumps({'error': str(e)}), 500
