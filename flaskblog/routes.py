from flask import render_template, url_for, flash, redirect
from flaskblog import app
from flaskblog.models import User, Post
from flaskblog.form import RegistrationForm, LoginForm


# the sample data at the home page
posts = [
    {
        'author' : 'Corey Schafer',
        'title' : 'Blog Post 1',
        'content' : 'First post content',
        'date_posted' : 'April 20, 2018'
    },
    {
        'author' : 'Jane Doe',
        'title' : 'Blog Post 2',
        'content' : 'Second post content',
        'date_posted' : 'April 21, 2018'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts) # transfer here posts to the html's posts

@app.route("/about")
def about():
    return render_template('about.html', title='About') # module setting the title name

@app.route("/register", methods=['GET', 'POST']) # methods : used for the 'form' submit
def register():
    form = RegistrationForm() # declare our form
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success') # flash : add a new item
        return redirect(url_for('home')) # redirect : redirect to another page
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)
