import os
from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv('SECRET_KEY', 'for dev')

THIS_DIR = os.path.abspath(os.path.dirname(__file__))

# Database related
DATABASE_CSV = os.path.join(THIS_DIR, 'app', 'static', 'Dataset-Hackathon.csv')
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(THIS_DIR, 'app.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False