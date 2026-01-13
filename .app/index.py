# Python script to act as the launch point to our Flask web application

# Import the required modules
from flask import Flask, render_template, request, url_for, flash
import secrets

from registration import RegistrationForm

# Declaire and create/instantiate a flask object
app = Flask(__name__)
app = Flask(__name__)

#Application configuration
#1. Create the application's secret key to protect our site from CSRF attacks
app.config['SECRET_KEY'] = secrets.token_urlsafe(32) # app_key = secet.token_hex(18)

# Set the route to the index/home page
@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
    # Get the user's browser and store it in the browser variable
    browser = request.headers.get('User-Agent')

    # Determine the browser based on the browser string
    if 'Firefox' in browser:
        user_agent = 'Firefox'
    elif 'Opera' in browser:
        user_agent = 'Opera'
    elif 'Chrome'in browser:
        user_agent = 'Chrome'
    elif 'Safari' in browser:
        user_agent = 'Safari'
    else:
        user_agent = 'Unknown'

# Route to the register/signup page
@app.route('/register', methods=['GET', 'POST'])

@app.route('/sign-up',methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
       # Process the form data(e.g , save to a database & so on.)
       flash("Registration or sign-up succesful", "success")
       return redirect(url_for('success')) #Redirect to a success page
    else:
        # Flask validation errors
        for field, errors in form.errors.items()
            for error in errors:
                flash(f"Error in {getattr(fom, field), label, text}: {error}", "danger")
    return render_template('register.html')

#router to the login/sign-up page
@app.route('/login',methods=['GET', 'POST'])
@app.route('/sign-in',methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Process the form data (e.g redirect to the inbox, checkbox, view post or friend profile & so on)
        flash("Login or Sign-in Succesfully", "success")
        return redirect(url_for('success')) #Redirect to the success page
    else:
        #Flash validate errors
        for field, errors in form, errors.items():
            flash(f"Error in {getattr(form,field),label.text}: {error}", "danger")
    return render_template('login.html', form=form )
#Set the router to the user's page

@app.route('/user')
@app.route('/user/<username>')
def user(username=None):
    return render_template('user.html', username=username)

# Pages to handle site errors
# 3. Handle page not found (404 error)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404
# 2. Handle page not found (403 error)
@app.errorhandler(403)
def page_not_found(e):
    return render_template('404.html'),403
# 3. Handle page not found (404 error)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404


# Set the entry point to our web application
if __name__ == "__main__":
   app.run(debug=True)
