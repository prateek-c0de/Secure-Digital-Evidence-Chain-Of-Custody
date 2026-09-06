import io
from app.models import Evidence, CustodyEvent, User
from app.services.custody_service import CustodyService
from app import db

def test_transfer_workflow(app, client):
    with app.app_context():
        # First register an evidence
        user1 = User.query.filter_by(email='test@example.com').first()
        
        # Create user 2
        from werkzeug.security import generate_password_hash
        user2 = User(name='User Two', email='two@example.com', password_hash=generate_password_hash('password'), role_id=1)
        db.session.add(user2)
        db.session.commit()
        
        evidence = Evidence(
            case_id=1, name='Test', type='IMAGE', 
            sha256_hash='hash', collector_id=user1.id, current_custodian_id=user1.id
        )
        db.session.add(evidence)
        db.session.commit()
        
        evidence_id = evidence.id
        evidence_public_id = evidence.evidence_id
        
        # Initiate transfer
        success, event = CustodyService.initiate_transfer(evidence_id, user1.id, user2.id, 'Testing', 'Lab')
        assert success == True
        assert event.status == 'PENDING'
        assert evidence.status == 'TRANSFER_PENDING'
        
        event_id = event.id
        
        # Accept transfer
        success, event_accepted = CustodyService.accept_transfer(event_id, user2.id)
        assert success == True
        assert event_accepted.status == 'COMPLETED'
        assert evidence.status == 'IN CUSTODY'
        assert evidence.current_custodian_id == user2.id

