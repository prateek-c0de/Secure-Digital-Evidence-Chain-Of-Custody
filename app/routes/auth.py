from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from werkzeug.security import check_password_hash
from app.models import User
from app.services.audit_service import AuditService

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('dashboard.index'))
        
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        if user and check_password_hash(user.password_hash, password):
            if not user.is_active:
                flash('Account is inactive.', 'danger')
                return redirect(url_for('auth.login'))
                
            session['user_id'] = user.id
            session['role'] = user.role.name
            
            AuditService.create_event('USER_LOGIN', {'email': email}, user_id=user.id)
            
            return redirect(url_for('dashboard.index'))
        else:
            flash('Invalid email or password.', 'danger')
            AuditService.create_event('FAILED_LOGIN_ATTEMPT', {'email': email})
            
    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    user_id = session.get('user_id')
    if user_id:
        AuditService.create_event('USER_LOGOUT', {}, user_id=user_id)
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for('auth.login'))

