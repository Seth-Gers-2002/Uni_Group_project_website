from flask import render_template, request, redirect, url_for
from . import inventory_bp
from models import db, InventoryItem

@inventory_bp.route('/inventory_dashboard')
def inventory_dashboard():
    # The main “Stock Manager” page with big icons for add/remove/request
    return render_template("inventory_dashboard.html")

@inventory_bp.route('/inventory/add', methods=['GET', 'POST'])
def add_inventory():
    if request.method == 'POST':
        name = request.form['name']
        quantity = int(request.form.get('quantity', '0') or '0')
        location = request.form.get('location', '')
        job_association = request.form.get('job_association', '')
        cleaning_method = request.form.get('cleaning_method', '')

        new_item = InventoryItem(
            name=name,
            quantity=quantity,
            location=location,
            job_association=job_association,
            cleaning_method=cleaning_method
        )
        db.session.add(new_item)
        db.session.commit()

        return redirect(url_for('inventory.inventory_dashboard'))
    return render_template("add_inventory.html")

@inventory_bp.route('/inventory/remove', methods=['GET', 'POST'])
def remove_inventory():
    if request.method == 'POST':
        item_id = request.form.get('item_id')
        item = InventoryItem.query.get_or_404(item_id)
        db.session.delete(item)
        db.session.commit()
        return redirect(url_for('inventory.inventory_dashboard'))
    # Or you could pass a list of items to choose from:
    items = InventoryItem.query.all()
    return render_template("remove_inventory.html", items=items)

@inventory_bp.route('/inventory/request', methods=['GET', 'POST'])
def request_inventory():
    if request.method == 'POST':
        # Process the stock request
        return redirect(url_for('inventory.inventory_dashboard'))
    return render_template("request_inventory.html")

@inventory_bp.route('/inventory/manage_requests')
def manage_requests():
    # Display or handle logic for stock requests
    return render_template("manage_requests.html")
