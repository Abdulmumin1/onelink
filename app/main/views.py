from . import main
from flask import render_template, request, redirect, url_for
from app.models import Profile, Link
from .forms import Register
from app.models import db
from flask_login import login_user, current_user

def create_username(field, number=0):
    
    user = Profile.query.filter_by(username=field).first()
    if user:
        number += 1
        create_username(f'{field}{number}', number=number) 
    else:
        return field

@main.route('/')
def index():
    return render_template('profile.html')

@main.route('/signup', methods=['GET', 'POST'])
def signup():
    form  = Register()
    if request.method == 'POST':
        if form.validate_on_submit():
            user = Profile(name=form.name.data, password=form.password.data)
            # username = create_username(form.name.data.split(' '[0]))
            # user.username = username
            db.session.add(user)
            db.session.commit()
            login_user(user, 1)
            next = request.args.get('next')
            if next is None or not next.startswith('/'):
                next = url_for('main.index')
            return redirect(next)


    return render_template('auth/signup.html', form=form)