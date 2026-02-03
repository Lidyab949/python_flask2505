# Python script to act as the launch point to our Flask web application

# Import the required modules
from flask import Flask, render_template, request, url_for, flash, redirect
from flask_login import current_user, LoginManager
from flask_login import login_user, logout_user, login_required #For application authentication & authorisation
import secrets
import string

# Import the registration, login and product form modules
from registration import RegistrationForm
from login import LoginForm
from product_form import ProductionForm

#Import the database models
from models import Producr, init_db, db, User, Role, UserRole
from seed_products_users_roles import seed_all

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


# Set the route to the user's page
@app.route('/user')
@app.route('/user/<username>')
def index(username=None):
    return render_template('user.html', username=username)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Create a guest user to access our unprotcted site areas anonymously (unauthenticated access)
class GuestUser:
    def __init__(self):
        self.full_name = "Guest"
        self.is_authemticated = False
        self.is_active = False
        self.is_anonymous = True

    def is_admin_or_manager(self):
        return False

    def get_id(self):
        return None

# Function to get the user object for the current user, if the current user is authenticated, else
# it returns a Guest object
@app.context_processor
def inject_user():
    if current_user.is_authenticated:
        return {"current_user": current_user}
    else:
        return {"current_user": GuestUser()}

# Function to generate the prefix for product ids when adding new products in he product's table
def generate_product_id():
    prefix = '01H73QEWM'
    alphabet = string.ascii_uppercase + string.digits
    while True:
        suffix = "".join(secrets.choice(alphabet) for _ in range(8))
        candidate = prefix + suffix
        if Product.query.get(candidate) is None: # when the product ID doesn't exist in the 'product' table
            return candidate

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
        for field, errors in form.errors.items():
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
# 1. Handle when authentication is required and has not been provided or failed (401 error)
@app.errorhandler(401)
def unauthorised(e):
    return render_template('401.html'),401

# 2. Handle when user is authenticated but doesn't have permission to access a resource/page (403 error)
@app.errorhandler(403)
def forbidden(e):
    return render_template('403.html'),403

# 3. Handle page not found (404 error)
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

# 4. Handle internal server error(500 error)
@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'),500

# Code to somulate an internal server error by raising an exception
@app.route('/trigger-500')
def trigger_500():
    #Deliberately raise an error in our server
    raise Exception("Deliberate internal exception")

# 5. Handle when the website is overloaded or temporarily down for upgrade/maintenance (503 error)
@app.errorhandler(503)
def service_unavailable(e):
    return render_template('503.html'),503




# Set the entry point to our web application
if __name__ == "__main__":
   app.run(debug=True)
