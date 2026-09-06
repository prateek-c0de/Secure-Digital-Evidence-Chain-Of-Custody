import hashlib
import os

class HashService:
    @staticmethod
    def calculate_sha256(file_path):
        sha256 = hashlib.sha256()
        try:
            with open(file_path, 'rb') as f:
                for chunk in iter(lambda: f.read(1024 * 1024), b""):
                    sha256.update(chunk)
            return sha256.hexdigest()
        except FileNotFoundError:
            return None

    @staticmethod
    def verify_hash(original_hash, current_hash):
        if not original_hash or not current_hash:
            return False
        return original_hash.lower() == current_hash.lower()

