import json
import uuid
from datetime import datetime
from google.cloud import firestore

db = firestore.Client()
notes_collection = db.collection('notes')

def create_note(request):
    try:
        # Parse request body
        request_json = request.get_json()
        note_id = str(uuid.uuid4())
        timestamp = datetime.now().isoformat()

        note = {
            'NoteID': note_id,
            'Title': request_json['title'],
            'Content': request_json['content'],
            'Timestamp': timestamp
        }

        # Add note to Firestore
        notes_collection.document(note_id).set(note)

        return json.dumps(note), 200
    except Exception as e:
        return json.dumps({'error': str(e)}), 500
