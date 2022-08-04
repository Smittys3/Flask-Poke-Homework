from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import current_user, login_required
from app.models import User, db
from .forms import EditProfileForm

prof = Blueprint('prof', __name__, template_folder='profiletemplates')

@prof.route('/profile')
def userProfile():
    return render_template('profile.html')


@prof.route('/editprofile', methods=["GET", "POST"])
def editProfile():
    form = EditProfileForm()
    user = User.query.get(current_user.id)
    # add/edit user to database
    if request.method == "POST":
        print('POST request made')
        if form.validate():
            email = form.email.data

            # add instance to our db
            # db.session.add(user)
            user.email=email
            db.session.commit()
            flash("Successfully changed your profile!", 'success')
            return redirect(url_for('auth.logMeIn'))
        else:
            flash('Invalid form. Please fill it out correctly.', 'danger')
    return render_template('editprofile.html', form = form, user = user)
# def editProfile():
#     form = EditProfileForm()
#     user = User.query.get(current_user.id)
#     if request.method == "POST":
#         if form.validate():
#             first_name = form.first_name.data
#             last_name = form.last_name.data
#             email = form.email.data

#             user.first_name=first_name
#             user.last_name=last_name
#             user.email=email
#             db.session.commit()
#             flash("Profile changed.", 'success')
#         return redirect(url_for('prof.editProfile'))
#     return render_template('editprofile.html', form = form,user = user)