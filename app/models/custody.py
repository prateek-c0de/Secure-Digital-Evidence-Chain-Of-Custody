from app import db
from datetime import datetime

class CustodyEvent(db.Model):
    __tablename__ = 'custody_events'
    id = db.Column(db.Integer, primary_key=True)
    evidence_id = db.Column(db.Integer, db.ForeignKey('evidence.id'), nullable=False)
    
    sender_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    receiver_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    
    action = db.Column(db.String(50), nullable=False) # e.g., 'REGISTERED', 'TRANSFERRED', 'ACCEPTED'
    purpose = db.Column(db.String(255))
    location = db.Column(db.String(255))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    
    evidence_hash = db.Column(db.String(64), nullable=False) # Hash of evidence at time of transfer
    digital_signature = db.Column(db.Text)
    
    previous_event_hash = db.Column(db.String(64))
    current_event_hash = db.Column(db.String(64))
    
    status = db.Column(db.String(50), default='COMPLETED') # 'PENDING', 'COMPLETED', 'REJECTED'

    sender = db.relationship('User', foreign_keys=[sender_id])
    receiver = db.relationship('User', foreign_keys=[receiver_id])

    def __repr__(self):
        return f'<CustodyEvent {self.action} on Evidence {self.evidence_id}>'

