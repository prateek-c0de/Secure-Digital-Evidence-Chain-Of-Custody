import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import Role, User, Case, Evidence, CustodyEvent, AuditLog, VerificationEvent

app = create_app()

def setup_database():
    with app.app_context():
        print("Creating database tables...")
        db.create_all()
        print("Database tables created successfully.")

if __name__ == '__main__':
    setup_database()

