from .. import db
import datetime

class UserModel(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    mobile = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    role = db.Column(db.String(7), nullable=False)


class UserAddressesModel(db.Model):
    __tablename__ = 'user_addresses'
    id = db.Column(db.Integer, primary_key=True)
    address1 = db.Column(db.String(150), nullable=False)
    address2 = db.Column(db.String(150))
    address3 = db.Column(db.String(150))
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)


class ProductModel(db.Model):
    __tablename__ = 'products'
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(50), nullable=False)
    product_price = db.Column(db.Integer)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=False)


class ProductMetaModel(db.Model):
    __tablename__ = 'products_meta'
    id = db.Column(db.Integer, primary_key=True)
    product_image = db.Column(db.String(150), nullable=True)
    in_stock = db.Column(db.String(10), nullable=False)
    star_rating = db.Column(db.Integer, nullable=True)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)


class CategoryModel(db.Model):
    __tablename__ = 'categories'
    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(50), nullable=False)

