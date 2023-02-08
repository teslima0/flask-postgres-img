from flask import Blueprint, request
from flask_jwt_extended import jwt_required, get_jwt_identity
import cloudinary
from . import db,app
from .models import Product,User
import cloudinary
import cloudinary.uploader
import cloudinary.api

views=Blueprint('views',__name__)



def upload_image():

    file = request.files['file']
    result = cloudinary.uploader.upload(file, folder="image")
    return {"url": result["secure_url"]}


@views.route("/Create_products", methods=["POST"])
@jwt_required()
def create_product():
   
    current_user_id = get_jwt_identity()
    user = User.query.filter_by(id=current_user_id["id"]).first()
    name = request.form.get("name")
    description = request.form.get("description")
    qty = request.form.get("qty")
    price = request.form.get("price")
    #image = request.files.get("image_url")

    file = request.files['image_url']
    result = cloudinary.uploader.upload(file, folder="image")
    image_url = result["secure_url"]
    #result1=result["secure_url"]
    print(image_url)
   
    # Create a product instance and save it to the database
    try:
        product = Product(name=name, description=description, qty=qty, price=price, image_url=image_url, user=user)
        db.session.add(product)
        db.session.commit()
    except Exception as e:
        print("Error:", e)

    
    print("Product:", product.__dict__)
    return "Product created successfully", 201