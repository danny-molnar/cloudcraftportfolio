import json
from google.cloud import firestore

db = firestore.Client()

def update_note(request):
    try:
        request_json = request.get_json()
        note_id = request.args.get('noteId')

        if not note_id or 'title' not in request_json or 'content' not in request_json:
            return json.dumps({'error': 'Missing noteId or title or content'}), 400

        note_ref = db.collection('notes').document(note_id)
        note_ref.update({
            'Title': request_json['title'],
            'Content': request_json['content']
        })

        return json.dumps({'result': 'Note updated'}), 200
    except Exception as e:
        return json.dumps({'error': str(e)}), 500
