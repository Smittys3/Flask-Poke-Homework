from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from app.models import User

from app.models import db
from .forms import EditProfileForm

prof = Blueprint('prof', __name__, template_folder='profiletemplates')

@prof.route('/profile')
def userProfile():
    return render_template('profile.html')


@prof.route('/editprofile', methods=["GET", "POST"])
def editProfile():
    form = EditProfileForm()
    # add/edit user to database
    user = User.query.filter_by(id = current_user.id).first()
    if request.method == "POST":
        print('POST request made')
        if form.validate():
            username = form.username.data
            email = form.email.data
            password = form.password.data

            # add instance to our db
            db.session.add(user)
            db.session.commit()
            flash("Successfully changed your profile!", 'success')
            return redirect(url_for('auth.logMeIn'))
        else:
            flash('Invalid form. Please fill it out correctly.', 'danger')
    return render_template('editprofile.html', form = form)