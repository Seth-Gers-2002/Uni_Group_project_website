# routes/__init__.py
from flask import Blueprint

# Initialize the blueprint for routes
inventory_bp = Blueprint('inventory', __name__)

from .inventory import list_inventory, add_inventory, remove_inventory, request_inventory, manage_requests
