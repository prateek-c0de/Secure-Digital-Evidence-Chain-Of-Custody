from app import create_app, db
from app.models import user, role, case, evidence, custody, audit, verification

app = create_app()

if __name__ == '__main__':
    import os
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() in ('true', '1', 't')
    app.run(debug=debug_mode)

