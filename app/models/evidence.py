from app import db
from datetime import datetime
import uuid

class Evidence(db.Model):
    __tablename__ = 'evidence'
    id = db.Column(db.Integer, primary_key=True)
    evidence_id = db.Column(db.String(50), unique=True, nullable=False, default=lambda: f"EV-{datetime.utcnow().year}-{uuid.uuid4().hex[:6].upper()}")
    case_id = db.Column(db.Integer, db.ForeignKey('cases.id'), nullable=False)
    name = db.Column(db.String(255), nullable=False)
    type = db.Column(db.String(50), nullable=False)
    description = db.Column(db.Text)
    original_filename = db.Column(db.String(255))
    storage_path = db.Column(db.String(512))
    mime_type = db.Column(db.String(100))
    file_size = db.Column(db.Integer)
    sha256_hash = db.Column(db.String(64), nullable=False)
    
    collector_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    collection_location = db.Column(db.String(255))
    collection_device = db.Column(db.String(255))
    collection_timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    status = db.Column(db.String(50), default='PENDING')
    current_custodian_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    collector = db.relationship('User', foreign_keys=[collector_id])
    current_custodian = db.relationship('User', foreign_keys=[current_custodian_id])
    
    custody_events = db.relationship('CustodyEvent', backref='evidence', lazy=True)
    verification_events = db.relationship('VerificationEvent', backref='evidence', lazy=True)

    def __repr__(self):
        return f'<Evidence {self.evidence_id}>'
