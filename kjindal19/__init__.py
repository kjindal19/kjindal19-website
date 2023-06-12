import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail




app = Flask(__name__)
app.config['SECRET_KEY'] = ""

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://"user":"pass"@"host"/"database"'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager =  LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'
app.config['MAIL_SERVER'] = "host"
app.config['MAIL_PORT'] = "465"
app.config['MAIL_USE_SSL'] = "True"
app.config['MAIL_USERNAME'] = ""
app.config['MAIL_PASSWORD'] = ""
mail = Mail(app)
app.app_context().push()


from kjindal19 import routes