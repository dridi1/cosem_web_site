import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from api import app, db

with app.app_context():
    db.create_all()
    print("Database tables created successfully.")
