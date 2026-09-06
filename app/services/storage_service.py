import os
import shutil
from werkzeug.utils import secure_filename
from flask import current_app

class StorageService:
    def __init__(self):
        # We can implement a cloud adapter here later (e.g. AWS S3)
        self.storage_type = 'local'
        
    def _get_storage_path(self):
        return current_app.config['UPLOAD_FOLDER']

    def save(self, file, evidence_id):
        if not file:
            return None
        
        filename = secure_filename(file.filename)
        # We prepend evidence_id to ensure uniqueness in local storage
        stored_filename = f"{evidence_id}_{filename}"
        filepath = os.path.join(self._get_storage_path(), stored_filename)
        
        file.save(filepath)
        return filepath

    def get(self, filepath):
        if os.path.exists(filepath):
            return filepath
        return None

    def delete(self, filepath):
        if os.path.exists(filepath):
            os.remove(filepath)
            return True
        return False

