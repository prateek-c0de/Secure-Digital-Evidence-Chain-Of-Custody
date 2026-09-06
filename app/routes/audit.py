from flask import Blueprint, render_template, jsonify
from app.models import AuditLog
from app.services.audit_service import AuditService
from app.middleware.auth import login_required, role_required

audit_bp = Blueprint('audit', __name__)

@audit_bp.route('/', methods=['GET'])
@login_required
@role_required(['Administrator', 'Auditor'])
def list_logs():
    logs = AuditLog.query.order_by(AuditLog.id.desc()).limit(100).all()
    return render_template('audit.html', logs=logs)

@audit_bp.route('/verify-chain', methods=['POST'])
@login_required
@role_required(['Administrator', 'Auditor'])
def verify_chain():
    is_valid, invalid_blocks = AuditService.verify_chain()
    
    if is_valid:
        return jsonify({'success': True, 'message': 'Audit chain is fully verified and secure.'})
    else:
        return jsonify({
            'success': False, 
            'message': f'TAMPER DETECTED in audit log. Invalid blocks: {invalid_blocks}'
        }), 400

