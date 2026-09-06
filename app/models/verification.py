from app import db
from datetime import datetime

class VerificationEvent(db.Model):
    __tablename__ = 'verification_events'
    id = db.Column(db.Integer, primary_key=True)
    evidence_id = db.Column(db.Integer, db.ForeignKey('evidence.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    original_hash = db.Column(db.String(64), nullable=False)
    calculated_hash = db.Column(db.String(64), nullable=False)
    result = db.Column(db.String(50), nullable=False) # 'VERIFIED', 'TAMPER_DETECTED'
    
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    notes = db.Column(db.Text)

    user = db.relationship('User')

    def __repr__(self):
        return f'<VerificationEvent {self.result} on Evidence {self.evidence_id}>'

