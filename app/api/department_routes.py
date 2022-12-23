from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from app.models import Department, Product

department_routes = Blueprint( 'departments', __name__,  )


# Get all Departments 
@department_routes.route('')
def all_departments():
    departments =  Department.query.all()
    department_dict = [ department.to_dict() for department in departments ]
    return jsonify(department_dict)


# Get department by id
@department_routes.route('/<int:department_id>')
def department_by_id(department_id):
    department = Department.query.get(department_id)
    if department:
        return jsonify(department.to_dict())
    else: 
        return {'errors': ['That department Id does not exist'] }


# Get all products by a department
@department_routes.route('/<int:department_id>/products')
def department_products(department_id):
    department_products = Product.query.filter(Product.department_id == department_id)
    if department_products:
        products = [ product.to_dict() for product in department_products ]
        return jsonify(products)   