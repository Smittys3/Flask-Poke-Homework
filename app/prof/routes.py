from flask import Blueprint, render_template, request, redirect, url_for, flash
from .forms import EditProfile
from app.models import User
 
from app.models import db

prof = Blueprint('prof', __name__, template_folder='profiletemplates')

@prof.route('/profile')
def userProfile():
    return render_template('profile.html')


@prof.route('/editprofile', methods=["GET", "POST"])
def editProfile():
    form = EditProfile()
    if request.method == "POST":
        print('POST request made')
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data

            # add user to database
            user = User(username, email, password)

            # add instance to our db
            db.session.add(user)
            db.session.commit()
            flash("Successfully changed your profile!", 'success')
            return redirect(url_for('auth.logMeIn'))
        else:
            flash('Invalid form. Please fill it out correctly.', 'danger')
    return render_template('editprofile.html', form = form)