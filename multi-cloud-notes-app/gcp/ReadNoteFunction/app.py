import json
from google.cloud import firestore

db = firestore.Client()

def read_note(request):
    try:
        note_id = request.args.get('noteId')
        if not note_id:
            return json.dumps({'error': 'Missing noteId'}), 400

        note_ref = db.collection('notes').document(note_id)
        note = note_ref.get()

        if note.exists:
            return json.dumps(note.to_dict()), 200
        else:
            return json.dumps({'error': 'Note not found'}), 404
    except Exception as e:
        return json.dumps({'error': str(e)}), 500
