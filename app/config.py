import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-fallback'
    
    # Database Config
    db_url = os.environ.get('DATABASE_URL')
    
    # Construct DB URL from individual MYSQL_ vars if DATABASE_URL is not set to mysql
    if not db_url or db_url.startswith('sqlite'):
        mysql_user = os.environ.get('MYSQL_USER')
        mysql_pass = os.environ.get('MYSQL_PASSWORD', '')
        mysql_host = os.environ.get('MYSQL_HOST', 'localhost')
        mysql_db = os.environ.get('MYSQL_DATABASE')
        if mysql_user and mysql_db:
            db_url = f"mysql+pymysql://{mysql_user}:{mysql_pass}@{mysql_host}/{mysql_db}"
            
    if db_url and db_url.startswith('mysql'):
        # Ensure pymysql is used if mysql is specified
        if db_url.startswith('mysql://'):
            db_url = db_url.replace('mysql://', 'mysql+pymysql://')
            
    SQLALCHEMY_DATABASE_URI = db_url or 'sqlite:///evidence.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Storage Config
    STORAGE_TYPE = os.environ.get('STORAGE_TYPE', 'local')
    STORAGE_PATH = os.environ.get('STORAGE_PATH', 'uploads')
    MAX_CONTENT_LENGTH = int(os.environ.get('MAX_UPLOAD_SIZE', 50 * 1024 * 1024))
    
    # Ensure upload path is absolute
    BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    UPLOAD_FOLDER = os.path.join(BASE_DIR, STORAGE_PATH)

