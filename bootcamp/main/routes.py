from flask import Blueprint, flash, render_template, redirect, url_for, request
from bootcamp import db
from bootcamp.main.forms import RegistrationForm
from bootcamp.models import User, Contact
from bootcamp.utils import send_email

main = Blueprint('main', __name__)


@main.route('/', methods=['GET'])
def home():
    form = RegistrationForm()
    return render_template('index.html', title='Python Bootcamp', form=form)

@main.route('/register', methods=['POST'], endpoint='register')
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = User(first_name = form.fname.data, last_name = form.lname.data,
                        email = form.email.data, program = form.program.data,
                        area_of_interest = form.area_of_interest.data)
        db.session.add(new_user)
        db.session.commit()
        html = render_template('thanks.html', name = form.lname.data)
        subject = "Thank you for registering"
        send_email(new_user.email, subject, html)
        flash("Thanks for registering. We've sent an email for payment instructions.", category='success')
        return redirect(url_for('main.home'))

@main.route('/submit_form', methods=['POST'], endpoint='submit_form')
def submit_form():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    new_contact = Contact(name=name, email=email, message=message)

    db.session.add(new_contact)
    db.session.commit()
    flash("Your message has been sent! We'll be in touch soon", 'success')
    return redirect(url_for('main.home'))