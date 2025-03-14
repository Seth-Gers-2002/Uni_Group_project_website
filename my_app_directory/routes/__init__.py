from flask import Blueprint

# Create the blueprints for hazard management and inventory
hazard_management_bp = Blueprint('hazard_management', __name__)
inventory_bp = Blueprint('inventory', __name__)

# Import route modules so that they get registered with the blueprint objects
from . import hazard_management
from . import inventory

# Import the job intake blueprint from the job_intake module
from .job_intake import job_bp
