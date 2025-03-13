from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Hazard(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    hazard_type = db.Column(db.String(120), nullable=False)
    hazard_description = db.Column(db.Text, nullable=False)
    hazard_location = db.Column(db.String(120), nullable=False)
    risk_level = db.Column(db.String(50), nullable=False)
    likelihood = db.Column(db.String(50), nullable=False)
    severity = db.Column(db.String(50), nullable=False)
    potential_impact = db.Column(db.Text)
    exposure_details = db.Column(db.Text)
    recommended_equipment = db.Column(db.Text)

    def __repr__(self):
        return f"<Hazard {self.hazard_type}>"

class InventoryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    quantity = db.Column(db.Integer, default=0)
    location = db.Column(db.String(120))
    job_association = db.Column(db.String(120))
    cleaning_method = db.Column(db.String(120))

    def __repr__(self):
        return f"<InventoryItem {self.name}>"
