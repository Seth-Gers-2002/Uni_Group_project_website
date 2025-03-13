# routes/__init__.py
from flask import Blueprint

# Define the blueprint just once for the routes package.
inventory_bp = Blueprint('inventory', __name__)

# Import the rest of the routes so they are registered with this blueprint.
from .inventory import *
