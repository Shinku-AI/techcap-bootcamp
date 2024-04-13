from flask import Flask
from flask_admin import Admin
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SECRET_KEY'] = '1cde88b02b6a28101be1b74c286e359a' #check heroku for environmental variable setup
#app.config['FLASK_ADMIN_SWATCH'] = 'yeti'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bootcamp.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://u4rtu0quchkr3e:p1fc160365f34ebab7284b9eedb1924dbde78ff1d36d317541924a0450cb1356a@cb4l59cdg4fg1k.cluster-czrs8kj4isg7.us-east-1.rds.amazonaws.com:5432/d5vbd6f1ueslmf'
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = 'techcapinitiative@gmail.com'
app.config['MAIL_PASSWORD'] = 'dghpmuqaobwfzutc'



admin = Admin(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)

from bootcamp.main.routes import main
from bootcamp.user.routes import user
from bootcamp.errors.routes import errors

app.register_blueprint(user)
app.register_blueprint(main)
app.register_blueprint(errors)
