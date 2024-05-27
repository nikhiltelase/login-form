from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import PasswordField, SubmitField, EmailField
from wtforms.validators import Email, DataRequired, Length
from flask_bootstrap import Bootstrap5


class LoginForm(FlaskForm):
    email = EmailField('Email address',
                        validators=[
                            Email(),
                            DataRequired(),
                            ],
                       )
    password = PasswordField('Password',
                             validators=[
                                 Length(min=8, max=16),
                                 DataRequired(),
                                 ],
                             )
    submit = SubmitField("Log In")


app = Flask(__name__)
bootstrap = Bootstrap5(app)
# Add a secret key for CSRF protection
app.secret_key = 'jay shree ram'
email = "nikhiltelase@gmail.com"
password = "12345678"


@app.route("/")
def home():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        entered_email = form.email.data
        entered_pass = form.password.data

        if entered_email == email and entered_pass == password:
            user_name = entered_email.split("@")[0]
            return render_template('success.html', username=user_name)
        elif entered_email != email:
            # if email is not match then so error wrong email
            return render_template('login.html', form=form, wrong_email='wrong email address')
        elif entered_pass != password:
            # if password is not match then so error wrong password
            return render_template('login.html', form=form, wrong_password='wrong password')

    return render_template('login.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)
