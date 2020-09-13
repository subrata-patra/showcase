from flask import Blueprint
from ..models.UserModel import *
from flask import Flask
import jwt
import time

user = Blueprint('user', __name__)


@user.route('/')
def home():
    return 'user Home'

# Add User:
@user.route('/add_user/<name>/<mobile>/<email>/<password>/<role>')
def add_user(name, mobile, email, password, role):
    user = UserModel(name = name, mobile = mobile, email = email, password = password, role = role)
    db.session.add(user)
    db.session.commit()
    return '<h1>New User Added!</h1>'

    
# User Login:
@user.route('/login/<mobile>/<password>')
def user_login(mobile, password):
    try:    
        user = UserModel.query.filter_by(mobile=mobile).first()
        if user.password == password:
            payload = {'mobile': user.mobile, 'pri_key': user.id, 'role': user.role, 'expire': time.time()+3600*24}
            key = 'secret'
            encode_jwt = jwt.encode(payload, key)
            return {'auth_token': encode_jwt.decode(), 'message': 'sucessfully logged in'}
        else:
            return f'<h1>incorrect credential</h1>'
    except:
        return f'<h1>Not a registered user!</h1>'


# Add User Address: Only User Can Do
@user.route('/add_address/<mobile>/<address1>/<address2>/<address3>')
def add_address(mobile, address1, address2=None, address3=None):
    key = 'secret'
    auth_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtb2JpbGUiOiI4ODg4ODAwMDAwIiwicHJpX2tleSI6Nywicm9sZSI6InVzZXIiLCJleHBpcmUiOjE1OTU1OTA0NjAuMjY0MTY5NX0.NT1uFhRydlkZYHiovj4YqTGex36jTkfWy-f95HUD_IY"
    #auth_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtb2JpbGUiOiI4ODg4ODExMTExIiwicHJpX2tleSI6OCwicm9sZSI6InVzZXIiLCJleHBpcmUiOjE1OTU1OTA1MTAuNDE5Nzc2N30.ZoNDE7TVU0uNiP4CddqKQLmJ2fGvNhO8TulxCWq4sJM"
    #auth_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtb2JpbGUiOiI4ODg4ODIyMjIyIiwicHJpX2tleSI6OSwicm9sZSI6InVzZXIiLCJleHBpcmUiOjE1OTU1OTA1NjAuNTY1NTE0fQ.31C4VXtCJoKsKrGn4wzTGwTOnF5DJNckzy826S0AzXk"
    try:
        data = jwt.decode(auth_token, key)
    except:
        return 'invalid JWT token'
    if data['expire'] >= time.time():
        if data['mobile'] == mobile and data['role'] == 'user': 
            user_id = data['pri_key']
            customer = UserAddressesModel(address1 = address1, address2 = address2, address3 = address3, user_id = user_id)
            db.session.add(customer)
            db.session.commit()
            return f'<h1>New User Address Added!</h1>'
        return f'<h1>Not a valid user!</h1>'
    return f'<h1>Timeout, login again!</h1>'


# Add Product: Only Valid Owner Can Add
@user.route('/add_product/<mobile>/<product_name>/<product_price>/<category_id>')
def add_product(mobile, product_name, product_price, category_id):
    key = 'secret'      # Below are owner auth tokens
    auth_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtb2JpbGUiOiI5OTk5OTAwMDAwIiwicHJpX2tleSI6NCwicm9sZSI6Im93bmVyIiwiZXhwaXJlIjoxNTk1NTg5ODY2Ljk2MzMxODN9.0_0VoWfAwlTTpOFSFfMrI8pYmWbGp_vNrir6rFQWALI"
    #auth_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtb2JpbGUiOiI5OTk5OTExMTExIiwicHJpX2tleSI6NSwicm9sZSI6Im93bmVyIiwiZXhwaXJlIjoxNTk1NTg5OTE3LjE4NjIwOTJ9.1DpU3J-B68st-M-SXTQpo7mGGcJCC8sTrQpEi8WumfI"
    #auth_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtb2JpbGUiOiI5OTk5OTIyMjIyIiwicHJpX2tleSI6Niwicm9sZSI6Im93bmVyIiwiZXhwaXJlIjoxNTk1NTg5OTY5LjA3NTI4Mzh9.ATBHXa8MO1_JbMYTsPvOA7kBcBLcugd15Bk2AoOHFXk"
    try:
        data = jwt.decode(auth_token, key)
    except:
        return 'invalid JWT token'
    if data['expire'] >= time.time():
        if data['mobile'] == mobile and data['role'] == 'owner': 
            owner_id = data['pri_key']
            product = ProductModel(product_name = product_name, product_price = product_price, owner_id = owner_id, category_id = category_id)
            db.session.add(product)
            db.session.commit()
            return f'<h1>New Product Added!</h1>'
        return f'<h1>Not a valid user!</h1>'
    return f'<h1>Timeout, login again!</h1>'


# Add Product Metadata: Only Valid Owner Can Do
@user.route('/add_product_meta/<mobile>/<product_image>/<in_stock>/<star_rating>/<product_id>')
def add_product_meta(mobile, product_image, in_stock, star_rating, product_id):
    key = 'secret'      # Below are owner auth tokens
    auth_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtb2JpbGUiOiI5OTk5OTAwMDAwIiwicHJpX2tleSI6NCwicm9sZSI6Im93bmVyIiwiZXhwaXJlIjoxNTk1NTg5ODY2Ljk2MzMxODN9.0_0VoWfAwlTTpOFSFfMrI8pYmWbGp_vNrir6rFQWALI"
    #auth_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtb2JpbGUiOiI5OTk5OTExMTExIiwicHJpX2tleSI6NSwicm9sZSI6Im93bmVyIiwiZXhwaXJlIjoxNTk1NTg5OTE3LjE4NjIwOTJ9.1DpU3J-B68st-M-SXTQpo7mGGcJCC8sTrQpEi8WumfI"
    #auth_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtb2JpbGUiOiI5OTk5OTIyMjIyIiwicHJpX2tleSI6Niwicm9sZSI6Im93bmVyIiwiZXhwaXJlIjoxNTk1NTg5OTY5LjA3NTI4Mzh9.ATBHXa8MO1_JbMYTsPvOA7kBcBLcugd15Bk2AoOHFXk"
    try:
        data = jwt.decode(auth_token, key)
    except:
        return 'invalid JWT token'
    if data['expire'] >= time.time():
        if data['mobile'] == mobile and data['role'] == 'owner': 
            product = ProductModel.query.filter_by(id=product_id).first()
            if product.owner_id == data['pri_key']:
                product_meta = ProductMetaModel(product_image = product_image, in_stock = in_stock, star_rating = star_rating, product_id = product_id)
                db.session.add(product_meta)
                db.session.commit()
                return f'<h1>New Product Metadata Added!</h1>'
            return f'<h1>Operation not allowed, choose your product to add metadata!</h1>'
        return f'<h1>Not a valid user!</h1>'
    return f'<h1>Timeout, login again!</h1>'


# View Product Details: Anyone Can View Products
@user.route('/view_products/<category_name>')
def get_user_details(category_name):
    try:
        category = CategoryModel.query.filter_by(category_name=category_name).first()
        category_id = category.id
        product_all = ProductModel.query.filter_by(category_id=category_id).all()
        list1 = []
        for product in product_all:
            product_profile = ProductMetaModel.query.filter_by(product_id=product.id).first()
            list1.append({'ID': product.id, 'Name': product.product_name, 'Rs.': product.product_price, 'Image': product_profile.product_image, 'In-stock': product_profile.in_stock, 'Star-rating': product_profile.star_rating})    
        return {'Product Details:': list1}    
    except:
        return f'<h1>No Such Category Exists</h1>'


# Delete Product: Valid Owner or Admin Can Do
@user.route('/delete_product/<mobile>/<product_id>')
def delete_product(mobile, product_id):
    key = 'secret'      # Below are owner auth tokens
    auth_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtb2JpbGUiOiI5OTk5OTAwMDAwIiwicHJpX2tleSI6NCwicm9sZSI6Im93bmVyIiwiZXhwaXJlIjoxNTk1NTg5ODY2Ljk2MzMxODN9.0_0VoWfAwlTTpOFSFfMrI8pYmWbGp_vNrir6rFQWALI"
    #auth_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtb2JpbGUiOiI5OTk5OTExMTExIiwicHJpX2tleSI6NSwicm9sZSI6Im93bmVyIiwiZXhwaXJlIjoxNTk1NTg5OTE3LjE4NjIwOTJ9.1DpU3J-B68st-M-SXTQpo7mGGcJCC8sTrQpEi8WumfI"
    #auth_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtb2JpbGUiOiI5OTk5OTIyMjIyIiwicHJpX2tleSI6Niwicm9sZSI6Im93bmVyIiwiZXhwaXJlIjoxNTk1NTg5OTY5LjA3NTI4Mzh9.ATBHXa8MO1_JbMYTsPvOA7kBcBLcugd15Bk2AoOHFXk"
    # Below are admin auth tokens
    #auth_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtb2JpbGUiOiI5OTgwMjAwNzk1IiwicHJpX2tleSI6MSwicm9sZSI6ImFkbWluIiwiZXhwaXJlIjoxNTk1NTg4OTQ1LjkyNjA0OX0.clWSVphWSaWQ7D93PfKqz0EqmiV2bOw1Gnvhzxf7d0U"
    #auth_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtb2JpbGUiOiI5ODQ1MDUwNzk1IiwicHJpX2tleSI6Miwicm9sZSI6ImFkbWluIiwiZXhwaXJlIjoxNTk1NTg5MTI3LjM2NzkwMjh9.dmPPOSRGCh3B1x8NrSFfKJmmviw-mxww01p50NxZiPQ"
    #auth_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtb2JpbGUiOiI3ODk5ODEyMjAwIiwicHJpX2tleSI6Mywicm9sZSI6ImFkbWluIiwiZXhwaXJlIjoxNTk1NTg5MTg5LjkzNDA1MzR9.1zPZS-HAvsK4k_C5juBwlszt_2ePmemEt3vMmJPybl4"

    try:
        data = jwt.decode(auth_token, key)
    except:
        return 'invalid JWT token'
    if data['expire'] >= time.time():
        if data['mobile'] == mobile and data['role'] == 'owner': 
            product = ProductModel.query.filter_by(id=product_id).first()
            if product.owner_id == data['pri_key']:
                db.session.delete(product)
                db.session.commit()
                return f'<h1>Product Deleted!</h1>'
            return f'<h1>Not a valid user!</h1>'

        elif data['mobile'] == mobile and data['role'] == 'admin':
            product = ProductModel.query.filter_by(id=product_id).first()
            db.session.delete(product)
            db.session.commit()
            return f'<h1>Product Deleted!</h1>'
        return f'<h1>Not a registered or valid user!</h1>'
    return f'<h1>Timeout, login again!</h1>'


# Edit/update Product: Only Admin Can Do
@user.route('/edit_product/<mobile>/<product_id>/<new_price>')
def edit_product(mobile, product_id, new_price):
    key = 'secret'      # Below are admin auth tokens
    auth_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtb2JpbGUiOiI5OTgwMjAwNzk1IiwicHJpX2tleSI6MSwicm9sZSI6ImFkbWluIiwiZXhwaXJlIjoxNTk1NTg4OTQ1LjkyNjA0OX0.clWSVphWSaWQ7D93PfKqz0EqmiV2bOw1Gnvhzxf7d0U"
    #auth_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtb2JpbGUiOiI5ODQ1MDUwNzk1IiwicHJpX2tleSI6Miwicm9sZSI6ImFkbWluIiwiZXhwaXJlIjoxNTk1NTg5MTI3LjM2NzkwMjh9.dmPPOSRGCh3B1x8NrSFfKJmmviw-mxww01p50NxZiPQ"
    #auth_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtb2JpbGUiOiI3ODk5ODEyMjAwIiwicHJpX2tleSI6Mywicm9sZSI6ImFkbWluIiwiZXhwaXJlIjoxNTk1NTg5MTg5LjkzNDA1MzR9.1zPZS-HAvsK4k_C5juBwlszt_2ePmemEt3vMmJPybl4"
    try:
        data = jwt.decode(auth_token, key)
    except:
        return 'invalid JWT token'
    
    if data['expire'] >= time.time():
        if data['mobile'] == mobile and data['role'] == 'admin':
            product = ProductModel.query.filter_by(id=product_id).first()
            product.product_price = new_price
            db.session.commit()
            return f'<h1>Product Updated!</h1>'
        return f'<h1>Not a valid user!</h1>'
    return f'<h1>Timeout, login again!</h1>'


# Add Category: Only Admin Can Do
@user.route('/add_category/<mobile>/<category_name>')
def add_category(mobile, category_name):
    key = 'secret'      # Below are admin auth tokens
    auth_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtb2JpbGUiOiI5OTgwMjAwNzk1IiwicHJpX2tleSI6MSwicm9sZSI6ImFkbWluIiwiZXhwaXJlIjoxNTk1NTg4OTQ1LjkyNjA0OX0.clWSVphWSaWQ7D93PfKqz0EqmiV2bOw1Gnvhzxf7d0U"
    #auth_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtb2JpbGUiOiI5ODQ1MDUwNzk1IiwicHJpX2tleSI6Miwicm9sZSI6ImFkbWluIiwiZXhwaXJlIjoxNTk1NTg5MTI3LjM2NzkwMjh9.dmPPOSRGCh3B1x8NrSFfKJmmviw-mxww01p50NxZiPQ"
    #auth_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtb2JpbGUiOiI3ODk5ODEyMjAwIiwicHJpX2tleSI6Mywicm9sZSI6ImFkbWluIiwiZXhwaXJlIjoxNTk1NTg5MTg5LjkzNDA1MzR9.1zPZS-HAvsK4k_C5juBwlszt_2ePmemEt3vMmJPybl4"
    try:
        data = jwt.decode(auth_token, key)
    except:
        return 'invalid JWT token'
    
    if data['expire'] >= time.time():
        if data['mobile'] == mobile and data['role'] == 'admin':
            category = CategoryModel(category_name = category_name)
            db.session.add(category)
            db.session.commit()
            return f'<h1>New Category Added!</h1>'
        return f'<h1>Not a valid user!</h1>'
    return f'<h1>Timeout, login again!</h1>'


# Delete User (Owner or User): Only Admin Can Do
@user.route('/delete_user/<mobile>/<user_id>')
def delete_user(mobile, user_id):
    key = 'secret'      # Below are admin auth tokens
    auth_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtb2JpbGUiOiI5OTgwMjAwNzk1IiwicHJpX2tleSI6MSwicm9sZSI6ImFkbWluIiwiZXhwaXJlIjoxNTk1NTg4OTQ1LjkyNjA0OX0.clWSVphWSaWQ7D93PfKqz0EqmiV2bOw1Gnvhzxf7d0U"
    #auth_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtb2JpbGUiOiI5ODQ1MDUwNzk1IiwicHJpX2tleSI6Miwicm9sZSI6ImFkbWluIiwiZXhwaXJlIjoxNTk1NTg5MTI3LjM2NzkwMjh9.dmPPOSRGCh3B1x8NrSFfKJmmviw-mxww01p50NxZiPQ"
    #auth_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtb2JpbGUiOiI3ODk5ODEyMjAwIiwicHJpX2tleSI6Mywicm9sZSI6ImFkbWluIiwiZXhwaXJlIjoxNTk1NTg5MTg5LjkzNDA1MzR9.1zPZS-HAvsK4k_C5juBwlszt_2ePmemEt3vMmJPybl4"
    try:
        data = jwt.decode(auth_token, key)
    except:
        return 'invalid JWT token'
    if data['expire'] >= time.time():
        if data['mobile'] == mobile and data['role'] == 'admin':
            user = UserModel.query.filter_by(id=user_id).first()
            if user.role == 'owner' or user.role == 'user':
                db.session.delete(user)
                db.session.commit()
                return f'<h1>User Deleted!</h1>'
            return f'<h1>User is an Admin, cannot be deleted!</h1>'
        return f'<h1>Not a registered or valid user!</h1>'
    return f'<h1>Timeout, login again!</h1>'
