from datetime import datetime
from itsdangerous import URLSafeTimedSerializer as Serializer
from kjindal19 import db, login_manager, app
from flask_login import UserMixin



@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))




class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    image_file = db.Column(db.String(150), nullable=False, default='default.jpg')
    password = db.Column(db.String(80), nullable=False)
    urole = db.Column(db.String(20), nullable=False, default='USER')

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])

        try:
            user_id = s.loads(token)['user_id']

        except:
            return None
        return User.query.get(user_id)

    def _repr__(self):
        return f"User('{self.username}', '{self.email}', '{self.image_file}')"


class ProjectCategory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class ProjectType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)

class Client(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    logo = db.Column(db.String(150), nullable=False, default='default.jpg')
    description = db.Column(db.String(2000), nullable=True)
    address = db.Column(db.String(100), nullable=False )
class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.Integer, nullable = False)
    type = db.Column(db.Integer, nullable = False)
    client = db.Column(db.Integer, nullable = False)
    date = db.Column(db.datetime, nullable = False)
    description1 = db.Column(db.String(2000), nullable=True)
    description2 = db.Column(db.String(2000), nullable=True)
    description3 = db.Column(db.String(2000), nullable=True)
    img1 = db.Column(db.String(150), nullable=False, default='default.jpg')
    img2 = db.Column(db.String(150), nullable=False, default='default.jpg')
    img3 = db.Column(db.String(150), nullable=False, default='default.jpg')
    img4 = db.Column(db.String(150), nullable=True)
    img5 = db.Column(db.String(150), nullable=True)


class Reviews(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    client = db.Column(db.Integer, nullable = False)
    date = db.Column(db.datetime, nullable = False)
    stars = db.Column(db.Integer, nullable = False)
    text = db.Column(db.String(2000), nullable=False)

class Mydetails(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    dob = db.Column(db.datetime, nullable = False)
    phone = db.Column(db.String(15), nullable = False)
    city = db.Column(db.String(30), nullable = False)
    linkedin = db.Column(db.String(100), unique=True, nullable=False)
    github = db.Column(db.String(100), unique=True, nullable=False)
    leetcode = db.Column(db.String(100), unique=True, nullable=False)
    instagram = db.Column(db.String(100), unique=True, nullable=False)
    website = db.Column(db.String(100), unique=True, nullable=False)
    Availablity = db.Column(db.String(100), unique=True, nullable=False)

class Education(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    provider = db.Column(db.String(100), nullable=False)
    sdate = db.Column(db.datetime, nullable = False)
    edate = db.Column(db.datetime, nullable = False)
    course = db.Column(db.String(100), nullable=False)
    grade = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(2000), nullable=False)

class Experience(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    empolyer = db.Column(db.String(100), nullable=False)
    sdate = db.Column(db.datetime, nullable = False)
    edate = db.Column(db.datetime, nullable = False)
    position = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(2000), nullable=False)



