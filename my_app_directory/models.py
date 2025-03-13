"""Define database models"""

# models.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class InventoryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    quantity = db.Column(db.Integer, default=0)
    location = db.Column(db.String(120))
    job_association = db.Column(db.String(120))
    cleaning_method = db.Column(db.String(120))

    def __repr__(self):
        return f"<InventoryItem {self.name}>"
