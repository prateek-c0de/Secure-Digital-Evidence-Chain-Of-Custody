import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import Role, User, Case
from app.services.audit_service import AuditService
from werkzeug.security import generate_password_hash

app = create_app()

def seed_data():
    with app.app_context():
        print("Seeding roles...")
        roles = ['Administrator', 'Evidence Collector', 'Investigating Officer', 'Evidence Custodian', 'Forensic Analyst', 'Auditor']
        role_objs = {}
        for role_name in roles:
            if not Role.query.filter_by(name=role_name).first():
                role = Role(name=role_name)
                db.session.add(role)
                role_objs[role_name] = role
        db.session.commit()

        # Refetch roles if they already existed
        for role_name in roles:
            role_objs[role_name] = Role.query.filter_by(name=role_name).first()

        print("Seeding users...")
        users_data = [
            {'name': 'Admin User', 'email': 'admin@example.com', 'role': 'Administrator'},
            {'name': 'John Collector', 'email': 'collector@example.com', 'role': 'Evidence Collector'},
            {'name': 'Jane Officer', 'email': 'officer@example.com', 'role': 'Investigating Officer'},
            {'name': 'Mike Custodian', 'email': 'custodian@example.com', 'role': 'Evidence Custodian'},
            {'name': 'Dr. Analyst', 'email': 'analyst@example.com', 'role': 'Forensic Analyst'},
            {'name': 'Sarah Auditor', 'email': 'auditor@example.com', 'role': 'Auditor'}
        ]

        # Use a safe demo password
        default_password = 'Password123!'
        
        for u in users_data:
            if not User.query.filter_by(email=u['email']).first():
                user = User(
                    name=u['name'],
                    email=u['email'],
                    password_hash=generate_password_hash(default_password),
                    role_id=role_objs[u['role']].id
                )
                db.session.add(user)
        db.session.commit()

        print("Seeding sample cases...")
        cases = ['CASE-2026-001', 'CASE-2026-002']
        for case_num in cases:
            if not Case.query.filter_by(case_number=case_num).first():
                case = Case(case_number=case_num, title=f"Investigation {case_num}", description="Initial investigation details.")
                db.session.add(case)
        db.session.commit()
        
        # We also need to record a genesis audit event if none exists
        from app.models import AuditLog
        if not AuditLog.query.first():
            print("Creating genesis audit log...")
            AuditService.create_event('SYSTEM_INITIALIZED', {'info': 'System initialization and seeding complete'})

        print("Seeding complete! Default password for all users is: Password123!")

if __name__ == '__main__':
    seed_data()

