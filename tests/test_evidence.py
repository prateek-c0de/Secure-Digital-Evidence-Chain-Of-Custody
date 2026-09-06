import io
from app.models import Evidence

def test_register_evidence(client):
    # Login first
    client.post('/auth/login', data={'email': 'test@example.com', 'password': 'password'})
    
    # Register evidence
    data = {
        'case_number': 'TEST-001',
        'name': 'Test Evidence',
        'type': 'DOCUMENT',
        'description': 'Test file',
        'collection_location': 'Lab',
        'collection_device': 'PC',
        'file': (io.BytesIO(b'my test file content'), 'test.txt')
    }
    
    response = client.post('/evidence/register', data=data, content_type='multipart/form-data', follow_redirects=True)
    assert response.status_code == 200
    assert b'Evidence registered successfully' in response.data
    
    # Verify in DB
    from app import db
    evidence = Evidence.query.filter_by(name='Test Evidence').first()
    assert evidence is not None
    assert evidence.case.case_number == 'TEST-001'
    assert evidence.status == 'REGISTERED'

