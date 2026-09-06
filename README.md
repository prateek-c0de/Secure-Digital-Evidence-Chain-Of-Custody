# Secure Digital Evidence Chain-of-Custody

This is a secure digital evidence management and chain-of-custody platform developed for the Smart India Hackathon (SIH) 2026.

## Features
- **Evidence Registration**: Register digital evidence with metadata.
- **SHA-256 Hashing**: Generates a cryptographic fingerprint of evidence for integrity verification.
- **QR Code Tracking**: Generates QR codes for evidence tracking.
- **Chain of Custody**: Tracks handover and custody events securely.
- **Tamper-Evident Audit Log**: Hash-linked audit trail for operations.
- **Integrity Verification**: Compare original SHA-256 hash with current file state.

## Setup Instructions
1. Setup a Python virtual environment.
2. Install dependencies: pip install -r requirements.txt.
3. Copy .env.example to .env and configure your database settings.
4. Setup database: python scripts/setup_db.py.
5. Seed demo data: python scripts/seed_data.py.
6. Run the app: python run.py.

