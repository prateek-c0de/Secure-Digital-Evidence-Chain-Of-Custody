from app import db
from app.models import Evidence, VerificationEvent
from app.services.hash_service import HashService
from app.services.audit_service import AuditService

class VerificationService:
    @staticmethod
    def verify_evidence(evidence_id, user_id, notes=None):
        evidence = Evidence.query.filter_by(evidence_id=evidence_id).first()
        if not evidence:
            return False, "Evidence not found"
            
        current_hash = HashService.calculate_sha256(evidence.storage_path)
        
        if not current_hash:
            result_status = 'FILE_MISSING'
        elif HashService.verify_hash(evidence.sha256_hash, current_hash):
            result_status = 'VERIFIED'
        else:
            result_status = 'TAMPER_DETECTED'
            
        event = VerificationEvent(
            evidence_id=evidence.id,
            user_id=user_id,
            original_hash=evidence.sha256_hash,
            calculated_hash=current_hash or 'NONE',
            result=result_status,
            notes=notes
        )
        
        db.session.add(event)
        
        # Update evidence status based on verification result
        if result_status == 'TAMPER_DETECTED':
            evidence.status = 'TAMPER_DETECTED'
        elif result_status == 'VERIFIED' and evidence.status != 'TAMPER_DETECTED':
            evidence.status = 'VERIFIED'
            
        db.session.commit()
        
        AuditService.create_event(
            'VERIFICATION_PERFORMED',
            {'evidence_id': evidence.evidence_id, 'result': result_status, 'current_hash': current_hash},
            user_id=user_id,
            evidence_id=evidence.id
        )
        
        return result_status == 'VERIFIED', result_status

