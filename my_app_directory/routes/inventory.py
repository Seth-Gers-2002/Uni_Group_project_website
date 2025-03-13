"""Organise routes"""

from flask import render_template, request, redirect, url_for
from models import db, InventoryItem
from . import inventory_bp  # Import the blueprint defined in __init__.py

@inventory_bp.route('/inventory', methods=['GET'])
def list_inventory():
    items = InventoryItem.query.all()
    return render_template("inventory.html", items=items)

@inventory_bp.route('/inventory/add', methods=['GET', 'POST'])
def add_inventory():
    if request.method == 'POST':
        name = request.form['name']
        quantity = int(request.form.get('quantity', '0') or '0')
        location = request.form.get('location', '')
        job_association = request.form.get('job_association', '')
        cleaning_method = request.form.get('cleaning_method', '')
        new_item = InventoryItem(name=name, quantity=int(quantity),
                                 location=location, job_association=job_association,
                                 cleaning_method=cleaning_method)
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('inventory.list_inventory'))
    return render_template("add_inventory.html")

@inventory_bp.route('/inventory/remove/<int:item_id>', methods=['POST'])
def remove_inventory(item_id):
    item = InventoryItem.query.get_or_404(item_id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('inventory.list_inventory'))

@inventory_bp.route('/inventory/request', methods=['GET', 'POST'])
def request_inventory():
    if request.method == 'POST':
        # Process stock request
        return redirect(url_for('inventory.list_inventory'))
    return render_template("request_inventory.html")

@inventory_bp.route('/inventory/manage_requests', methods=['GET'])
def manage_requests():
    # Fetch and display stock requests
    return render_template("manage_requests.html")
