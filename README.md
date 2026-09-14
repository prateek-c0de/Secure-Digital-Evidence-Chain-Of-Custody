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

```text
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
