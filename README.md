# 🔐 Secure Digital Evidence Chain of Custody

A secure web-based platform for managing digital evidence and investigation documents while maintaining **integrity, traceability, and a verifiable chain of custody**.

## 🎯 Problem

Digital evidence can pass through multiple people during an investigation. Without proper tracking, it becomes difficult to verify:

- Who collected the evidence
- Who transferred or received it
- When it was handled
- Whether the file was modified

## 💡 Solution

Our platform provides a centralized system to register, store, transfer, track, and verify digital evidence.

### Key Features

- 🔐 Secure authentication & role-based access
- 📁 Case and evidence management
- #️⃣ SHA-256 evidence hashing
- 📱 QR-based evidence identification
- 🔄 Digital chain-of-custody tracking
- 🧾 Tamper-evident audit logs
- 🔎 Evidence/document search
- ⚠️ Automatic hash mismatch detection
- 🔒 Secure storage and access control

## 🔄 Workflow
'''text
Evidence Collection
        ↓
Evidence Registration
        ↓
Metadata + SHA-256 Hash
        ↓
Secure Storage
        ↓
QR Generation
        ↓
Transfer / Handover
        ↓
Audit Log
        ↓
Hash Verification
        ↓
Verified / Tamper Detected

🛠️ Tch Stack
'''text
Component	  Technology
Frontend	  HTML, CSS, JavaScript
Backend	Python,   Flask
Database	  MySQL
Integrity	  SHA-256
Identification	  QR Code
Storage	          Local / Cloud Storage
Security	  Authentication, RBAC, Encryption
Audit	          Hash-linked Audit Log

🏗️ Architecture
'''text
Frontend
   ↓
Flask Backend
   ↓
MySQL + Secure Storage
   ↓
SHA-256 Integrity Verification
   ↓
QR / Evidence Tracking
   ↓
Audit & Chain of Custody

🔒 Evidence Verification
'''text
When evidence is registered, a SHA-256 hash is generated.
Original Hash == Current Hash
        ↓
    ✓ VERIFIED
If the evidence is modified:
Original Hash != Current Hash
        ↓
  ⚠ TAMPER DETECTED
  
🚀 Future Improvements
- Digital signatures
- Advanced document version control
- AI-assisted document classification
- Permissioned blockchain integration
- Inter-agency collaboration
- Automated case report generation
  
🎓 Project
Smart India Hackathon 2026
Team: Error:404
Secure. Traceable. Verifiable.

⚠️ Disclaimer
This project is an academic/SIH prototype and is not intended for direct production use with real confidential or legal evidence without appropriate security, compliance, and legal validation.
