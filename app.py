from flask import Flask
from endpoints.home import home_bp
from endpoints.contact import contact_bp
app = Flask(__name__)
app.register_blueprint(home_bp, url_prefix='/home')
app.register_blueprint(contact_bp, url_prefix='/contact')
app.run()