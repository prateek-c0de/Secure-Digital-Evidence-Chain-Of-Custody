from flask import Blueprint, redirect, url_for, flash, session, request
from app.services.verification_service import VerificationService
from app.middleware.auth import login_required

verification_bp = Blueprint('verification', __name__)

@verification_bp.route('/<evidence_id>', methods=['POST'])
@login_required
def verify(evidence_id):
    notes = request.form.get('notes', '')
    success, result = VerificationService.verify_evidence(evidence_id, session['user_id'], notes)
    
    if result == 'VERIFIED':
        flash('Verification successful. Evidence integrity confirmed.', 'success')
    elif result == 'TAMPER_DETECTED':
        flash('TAMPER DETECTED: Evidence hash mismatch!', 'danger')
    elif result == 'FILE_MISSING':
        flash('TAMPER DETECTED: Evidence file missing from storage.', 'danger')
    else:
        flash(result, 'warning')
        
    return redirect(url_for('evidence.view_evidence', evidence_id=evidence_id))

