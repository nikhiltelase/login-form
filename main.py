from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, validators, EmailField
from flask_bootstrap import Bootstrap


class LoginForm(FlaskForm):
    email = EmailField('email',
                        validators=[
                            validators.Email(),
                            validators.DataRequired(),
                            ])
    password = PasswordField('password',
                             validators=[
                                 validators.Length(min=8, max=10),
                                 validators.DataRequired(),
                                 ])
    submit = SubmitField("Log In")


app = Flask(__name__)
bootstrap = Bootstrap(app)

# Add a secret key for CSRF protection
app.secret_key = 'jay shree ram'
email = "nikhiltelase@gmail.com"
password = "12345678"


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    login_form = LoginForm()

    if login_form.validate_on_submit():
        entered_email = login_form.email.data
        entered_pass = login_form.password.data

        if entered_email == email and entered_pass == password:
            user_name = entered_email.split("@")[0]
            return render_template('success.html', username=user_name)
        elif entered_email != email:
            # if email is not match then so error wrong email
            return render_template('login.html', form=login_form, wrong_email='wrong email address')
        elif entered_pass != password:
            # if password is not match then so error wrong password
            return render_template('login.html', form=login_form, wrong_password='wrong password')

    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
