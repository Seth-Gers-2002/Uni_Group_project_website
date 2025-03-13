"""Organise routes"""

# routes/inventory.py
from flask import Blueprint, render_template, request, redirect, url_for
from models import db, InventoryItem

inventory_bp = Blueprint('inventory', __name__)

@inventory_bp.route('/inventory', methods=['GET'])
def list_inventory():
    items = InventoryItem.query.all()
    return render_template("inventory.html", items=items)

@inventory_bp.route('/inventory/add', methods=['GET', 'POST'])
def add_inventory():
    if request.method == 'POST':
        name = request.form['name']
        quantity = request.form.get('quantity', 0)
        location = request.form.get('location', '')
        job_association = request.form.get('job_association', '')
        cleaning_method = request.form.get('cleaning_method', '')
        new_item = InventoryItem(name=name, quantity=int(quantity), location=location,
                                   job_association=job_association, cleaning_method=cleaning_method)
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('.list_inventory'))
    return render_template("add_inventory.html")

@inventory_bp.route('/inventory/remove/<int:item_id>', methods=['POST'])
def remove_inventory(item_id):
    item = InventoryItem.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('.list_inventory'))

@inventory_bp.route('/inventory/request', methods=['GET', 'POST'])
def request_inventory():
    if request.method == 'POST':
        # Process stock request
        # Implementation details go here...
        return redirect(url_for('.list_inventory'))
    return render_template("request_inventory.html")

@inventory_bp.route('/inventory/manage_requests', methods=['GET'])
def manage_requests():
    # Fetch and display stock requests
    # Implementation details go here...
    return render_template("manage_requests.html")
