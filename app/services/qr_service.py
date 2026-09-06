import qrcode
import os
from flask import current_app

class QRService:
    @staticmethod
    def generate_qr(evidence_id):
        # We encode the evidence ID as required (no sensitive data)
        data = f"EVIDENCE_ID:{evidence_id}"
        
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        
        # Save to static/qr directory
        filename = f"{evidence_id}.png"
        qr_dir = os.path.join(current_app.config['UPLOAD_FOLDER'], '..', 'app', 'static', 'qr')
        os.makedirs(qr_dir, exist_ok=True)
        
        filepath = os.path.abspath(os.path.join(qr_dir, filename))
        img.save(filepath)
        
        return f"/static/qr/{filename}"

