from flask import Blueprint, request, jsonify

contact_bp = Blueprint('contact', __name__)
@contact_bp.route('/info/', methods=['POST'])
def contact():
    data = request.json
    contact_info = "My contact info is " + data.get("full_name") + " . Phone number is : " + data.get("phone_number")
    return contact_info