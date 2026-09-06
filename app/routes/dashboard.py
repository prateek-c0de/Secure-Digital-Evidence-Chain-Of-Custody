from flask import Blueprint, render_template, session
from app.models import Evidence, CustodyEvent, Case, User
from app.middleware.auth import login_required

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/')
@login_required
def index():
    user = User.query.get(session['user_id'])
    
    # Stats
    total_evidence = Evidence.query.count()
    my_evidence = Evidence.query.filter_by(current_custodian_id=user.id).count()
    pending_transfers = CustodyEvent.query.filter_by(receiver_id=user.id, status='PENDING').count()
    
    # Recent activity
    recent_evidence = Evidence.query.order_by(Evidence.id.desc()).limit(5).all()
    
    # Pending items for this user
    my_pending_transfers = CustodyEvent.query.filter_by(
        receiver_id=user.id, status='PENDING'
    ).order_by(CustodyEvent.id.desc()).all()
    
    return render_template(
        'dashboard.html', 
        user=user,
        stats={
            'total_evidence': total_evidence,
            'my_evidence': my_evidence,
            'pending_transfers': pending_transfers
        },
        recent_evidence=recent_evidence,
        my_pending_transfers=my_pending_transfers
    )

