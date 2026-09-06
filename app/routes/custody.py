from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models import Evidence, CustodyEvent, User
from app.services.custody_service import CustodyService
from app.middleware.auth import login_required

custody_bp = Blueprint('custody', __name__)

@custody_bp.route('/transfer/<evidence_id>', methods=['GET', 'POST'])
@login_required
def transfer(evidence_id):
    evidence = Evidence.query.filter_by(evidence_id=evidence_id).first_or_404()
    
    if evidence.current_custodian_id != session['user_id']:
        flash('You are not the current custodian of this evidence.', 'danger')
        return redirect(url_for('evidence.view_evidence', evidence_id=evidence_id))
        
    if request.method == 'POST':
        receiver_id = request.form.get('receiver_id')
        purpose = request.form.get('purpose')
        location = request.form.get('location')
        
        success, result = CustodyService.initiate_transfer(
            evidence.id, session['user_id'], receiver_id, purpose, location
        )
        
        if success:
            flash('Transfer initiated successfully.', 'success')
            return redirect(url_for('evidence.view_evidence', evidence_id=evidence_id))
        else:
            flash(result, 'danger')
            
    users = User.query.filter(User.id != session['user_id'], User.is_active == True).all()
    return render_template('transfer.html', evidence=evidence, users=users)

@custody_bp.route('/accept/<int:event_id>', methods=['POST'])
@login_required
def accept(event_id):
    success, result = CustodyService.accept_transfer(event_id, session['user_id'])
    
    if success:
        flash('Transfer accepted successfully.', 'success')
    else:
        flash(result, 'danger')
        
    return redirect(url_for('dashboard.index'))

