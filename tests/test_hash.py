import os
import tempfile
from app.services.hash_service import HashService

def test_calculate_sha256():
    with tempfile.NamedTemporaryFile(delete=False) as f:
        f.write(b'hello world')
        temp_path = f.name
        
    hash_val = HashService.calculate_sha256(temp_path)
    os.remove(temp_path)
    
    # 'hello world' sha256 is b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9
    assert hash_val == 'b94d27b9934d3e08a52e52d7da7dabfac484efe37a5380ee9088f7ace2efcde9'

def test_verify_hash():
    assert HashService.verify_hash('abc', 'abc') == True
    assert HashService.verify_hash('abc', 'ABC') == True
    assert HashService.verify_hash('abc', 'def') == False
    assert HashService.verify_hash(None, 'abc') == False

