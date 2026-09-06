from app.services.audit_service import AuditService
from app.models import AuditLog
from app import db

def test_audit_chain_creation(app):
    with app.app_context():
        # Create multiple events
        event1 = AuditService.create_event('TEST_EVENT_1', {'data': 1})
        event2 = AuditService.create_event('TEST_EVENT_2', {'data': 2})
        
        assert event1.previous_hash == 'GENESIS'
        assert event2.previous_hash == event1.current_hash
        
        # Verify chain
        is_valid, invalid_blocks = AuditService.verify_chain()
        assert is_valid == True
        assert len(invalid_blocks) == 0

def test_audit_chain_tampering(app):
    with app.app_context():
        AuditService.create_event('TEST_EVENT_1', {'data': 1})
        event2 = AuditService.create_event('TEST_EVENT_2', {'data': 2})
        AuditService.create_event('TEST_EVENT_3', {'data': 3})
        
        # Tamper with event 2
        event2.event_data = {'data': 99}
        db.session.commit()
        
        is_valid, invalid_blocks = AuditService.verify_chain()
        assert is_valid == False
        assert event2.id in invalid_blocks

