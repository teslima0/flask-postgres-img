from flask import request, Blueprint
import cloudinary
from . import db,app
from .models import Product,User
import cloudinary
import cloudinary.uploader
import cloudinary.api
from flask_jwt_extended import jwt_required, get_jwt_identity
views=Blueprint('views',__name__)

@views.route("/Create_product", methods=["POST"])
@jwt_required()
def createproduct():
   
    current_user_id = get_jwt_identity()
    user = User.query.filter_by(id=current_user_id["id"]).first()
    if not user:
        return "User not found", 404

    name = request.form.get("name")
    description = request.form.get("description")
    qty = request.form.get("qty")
    price = request.form.get("price")
    image = request.files.get('image_url')

    # Validate the input data
    if not name:
        return "Product name is required", 400
    if not description:
        return "Product description is required", 400
    if not qty:
        return "Product quantity is required", 400
    if not price:
        return "Product price is required", 400
    if not image:
        return "Product image is required", 400

    # Upload the image to Cloudinary
    try:
        result = cloudinary.uploader.upload(image, folder="image")
        image_url = result["secure_url"]
    except Exception as e:
        return "Error uploading image to Cloudinary: {}".format(e), 500

    # Create a product instance and save it to the database
    try:
        product = Product(name=name, description=description, qty=qty, price=price, image_url=image_url, user=user)
        db.session.add(product)
        db.session.commit()
    except Exception as e:
        return "Error creating product: {}".format(e), 500

    return "Product created successfully", 201
