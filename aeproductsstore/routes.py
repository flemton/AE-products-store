from flask import Flask, render_template, flash, redirect, request, session, url_for
from aeproductsstore import app, db
from flask_sqlalchemy import SQLAlchemy

from aeproductsstore.forms import LoginForm, RegisterForm
from aeproductsstore.models import Staff, Customers
import secrets

from werkzeug.security import generate_password_hash, check_password_hash

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/staff/login/', methods = ['GET', 'POST'])
def staff_login():

    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate:

        staff = Staff.query.filter_by(email = form.email.data).first()

        if staff:

            if check_password_hash(staff.password, form.password.data):

                flash('You have successfully logged in.', "success")
                
                session['logged_in'] = True

                session['email'] = staff.email

                session['first_name'] = staff.first_name

                return redirect(url_for('home'))

            else:

                flash('Username or Password Incorrect', "Danger")

                return redirect(url_for('user_login'))

    return render_template('login.html', form = form)

@app.route('/user/login/', methods = ['GET', 'POST'])
def user_login():

    form = LoginForm(request.form)

    if request.method == 'POST' and form.validate:

        user = Customers.query.filter_by(email = form.email.data).first()

        if user:

            if check_password_hash(user.password, form.password.data):

                flash('You have successfully logged in.', "success")
                
                session['logged_in'] = True

                session['email'] = user.email

                session['first_name'] = user.first_name 

                return redirect(url_for('home'))

            else:

                flash('Username or Password Incorrect', "Danger")

                return redirect(url_for('user_login'))

    return render_template('login.html', form = form)

@app.route('/register/', methods = ['GET', 'POST'])
def register():
    
    form = RegisterForm(request.form)
    
    if request.method == 'POST' and form.validate():
    
        hashed_password = generate_password_hash(form.password.data, method='sha256')

        new_user = Customers(
            
            first_name = form.first_name.data,

            last_name = form.last_name.data,
            
            email = form.email.data, 
            
            password = hashed_password)
    
        db.session.add(new_user)
    
        db.session.commit()
    
        flash('You have successfully registered', 'success')
    
        return redirect(url_for('user_login'))
    
    else:
    
        return render_template('register.html', form = form)

@app.route('/logout/')
def logout():
    
    session['logged_in'] = False

    return redirect(url_for('home'))
