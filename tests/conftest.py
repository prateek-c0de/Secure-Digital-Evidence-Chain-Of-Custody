import pytest
import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import create_app, db
from app.models import Role, User, Case
from werkzeug.security import generate_password_hash

class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'test-secret'
    STORAGE_TYPE = 'local'
    STORAGE_PATH = 'test_uploads'
    UPLOAD_FOLDER = os.path.abspath(os.path.join(os.path.dirname(__file__), 'test_uploads'))
    WTF_CSRF_ENABLED = False

@pytest.fixture
def app():
    app = create_app(TestConfig)
    
    with app.app_context():
        db.create_all()
        
        # Seed test data
        role = Role(name='Administrator')
        db.session.add(role)
        db.session.commit()
        
        user = User(name='Test Admin', email='test@example.com', password_hash=generate_password_hash('password'), role_id=role.id)
        db.session.add(user)
        
        case = Case(case_number='TEST-001', title='Test Case')
        db.session.add(case)
        db.session.commit()
        
        yield app
        
        db.session.remove()
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def runner(app):
    return app.test_cli_runner()

