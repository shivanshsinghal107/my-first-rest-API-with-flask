import app from app
import db from db

db.init_app()

@app.before_first_request
def create_table():
    db.create_all()
