from app import db
from app.models import Evidence, CustodyEvent
from app.services.audit_service import AuditService
from app.services.hash_service import HashService

class CustodyService:
    @staticmethod
    def initiate_transfer(evidence_id, sender_id, receiver_id, purpose, location):
        evidence = Evidence.query.get(evidence_id)
        if not evidence or evidence.current_custodian_id != sender_id:
            return False, "Invalid evidence or not authorized"
            
        # Get current hash for record
        current_file_hash = HashService.calculate_sha256(evidence.storage_path)
        
        # Get previous custody event hash
        last_event = CustodyEvent.query.filter_by(evidence_id=evidence.id).order_by(CustodyEvent.id.desc()).first()
        prev_hash = last_event.current_event_hash if last_event else "GENESIS"
        
        # Calculate event hash for chain
        import hashlib
        data = f"{prev_hash}{evidence_id}{sender_id}{receiver_id}TRANSFER"
        event_hash = hashlib.sha256(data.encode('utf-8')).hexdigest()
        
        event = CustodyEvent(
            evidence_id=evidence.id,
            sender_id=sender_id,
            receiver_id=receiver_id,
            action='TRANSFER_INITIATED',
            purpose=purpose,
            location=location,
            evidence_hash=current_file_hash or 'MISSING',
            previous_event_hash=prev_hash,
            current_event_hash=event_hash,
            status='PENDING'
        )
        
        evidence.status = 'TRANSFER_PENDING'
        db.session.add(event)
        db.session.commit()
        
        AuditService.create_event(
            'CUSTODY_TRANSFER_INITIATED',
            {'evidence_id': evidence.evidence_id, 'sender': sender_id, 'receiver': receiver_id, 'purpose': purpose},
            user_id=sender_id,
            evidence_id=evidence.id
        )
        return True, event

    @staticmethod
    def accept_transfer(custody_event_id, receiver_id):
        event = CustodyEvent.query.get(custody_event_id)
        if not event or event.receiver_id != receiver_id or event.status != 'PENDING':
            return False, "Invalid transfer or not authorized"
            
        evidence = Evidence.query.get(event.evidence_id)
        
        # Update current custodian
        evidence.current_custodian_id = receiver_id
        evidence.status = 'IN CUSTODY'
        event.status = 'COMPLETED'
        event.action = 'TRANSFER_ACCEPTED'
        
        # Recalculate event hash based on acceptance
        import hashlib
        data = f"{event.previous_event_hash}{evidence.id}{event.sender_id}{receiver_id}ACCEPTED"
        event.current_event_hash = hashlib.sha256(data.encode('utf-8')).hexdigest()
        
        db.session.commit()
        
        AuditService.create_event(
            'CUSTODY_TRANSFER_ACCEPTED',
            {'evidence_id': evidence.evidence_id, 'sender': event.sender_id, 'receiver': receiver_id},
            user_id=receiver_id,
            evidence_id=evidence.id
        )
        return True, event

