from app import db
from datetime import datetime

class Product(db.Model):
    __tablename__ = 'products'
    
    id = db.Column(db.Integer, primary_key=True)
    code = db.Column(db.String(50), unique=True, nullable=False)
    name = db.Column(db.String(200), nullable=False)
    unit = db.Column(db.String(20), nullable=False)
    quantity = db.Column(db.Float, nullable=False, default=0.0)
    location = db.Column(db.String(100))
    min_stock = db.Column(db.Float, default=5.0)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class ConsumptionBill(db.Model):
    __tablename__ = 'consumption_bills'
    
    id = db.Column(db.Integer, primary_key=True)
    bill_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    employee_name = db.Column(db.String(100), nullable=False)
    employee_signature = db.Column(db.String(100))
    is_finished = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship to bill items
    items = db.relationship('BillItem', backref='bill', lazy=True, cascade='all, delete-orphan')

class BillItem(db.Model):
    __tablename__ = 'bill_items'
    
    id = db.Column(db.Integer, primary_key=True)
    bill_id = db.Column(db.Integer, db.ForeignKey('consumption_bills.id'), nullable=False)
    item_number = db.Column(db.Integer, nullable=False)
    product_code = db.Column(db.String(50), nullable=False)
    product_name = db.Column(db.String(200), nullable=False)
    unit = db.Column(db.String(20), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(100))

class ReceptionSheet(db.Model):
    __tablename__ = 'reception_sheets'
    
    id = db.Column(db.Integer, primary_key=True)
    reception_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    supplier = db.Column(db.String(200), nullable=False)
    document_number = db.Column(db.String(100))
    notes = db.Column(db.Text)
    is_finished = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    # Relationship to reception items
    items = db.relationship('ReceptionItem', backref='reception', lazy=True, cascade='all, delete-orphan')

class ReceptionItem(db.Model):
    __tablename__ = 'reception_items'
    
    id = db.Column(db.Integer, primary_key=True)
    reception_id = db.Column(db.Integer, db.ForeignKey('reception_sheets.id'), nullable=False)
    item_number = db.Column(db.Integer, nullable=False)
    product_code = db.Column(db.String(50), nullable=False)
    product_name = db.Column(db.String(200), nullable=False)
    unit = db.Column(db.String(20), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(100))
    entry_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

class DraftBill(db.Model):
    __tablename__ = 'draft_bills'
    
    id = db.Column(db.Integer, primary_key=True)
    employee_name = db.Column(db.String(100))
    employee_signature = db.Column(db.String(100))
    last_updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationship to draft items
    items = db.relationship('DraftBillItem', backref='draft', lazy=True, cascade='all, delete-orphan')

class DraftBillItem(db.Model):
    __tablename__ = 'draft_bill_items'
    
    id = db.Column(db.Integer, primary_key=True)
    draft_id = db.Column(db.Integer, db.ForeignKey('draft_bills.id'), nullable=False)
    item_number = db.Column(db.Integer, nullable=False)
    product_code = db.Column(db.String(50), nullable=False)
    product_name = db.Column(db.String(200), nullable=False)
    unit = db.Column(db.String(20), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(100))

class DraftReception(db.Model):
    __tablename__ = 'draft_receptions'
    
    id = db.Column(db.Integer, primary_key=True)
    supplier = db.Column(db.String(200))
    document_number = db.Column(db.String(100))
    notes = db.Column(db.Text)
    last_updated = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    # Relationship to draft items
    items = db.relationship('DraftReceptionItem', backref='draft', lazy=True, cascade='all, delete-orphan')

class DraftReceptionItem(db.Model):
    __tablename__ = 'draft_reception_items'
    
    id = db.Column(db.Integer, primary_key=True)
    draft_id = db.Column(db.Integer, db.ForeignKey('draft_receptions.id'), nullable=False)
    item_number = db.Column(db.Integer, nullable=False)
    product_code = db.Column(db.String(50), nullable=False)
    product_name = db.Column(db.String(200), nullable=False)
    unit = db.Column(db.String(20), nullable=False)
    quantity = db.Column(db.Float, nullable=False)
    location = db.Column(db.String(100))