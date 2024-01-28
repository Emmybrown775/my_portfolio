from flask import Flask, render_template, request, flash
from projects import projects
import smtplib
import os

secretKey = os.environ["SECRET_KEY"]
my_password = os.environ["PASSWORD"]

app = Flask(__name__)
app.secret_key = secretKey


@app.route('/', methods=["GET", "POST"])
def home():  # put application's code here
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message = request.form.get("message")
        my_email = "emmycodes775@gmail.com"
        password = my_password
        connection = smtplib.SMTP("smtp.gmail.com", port=587)
        try:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=my_email,
                                msg=f"Name= {name} \n Email={email} \n Message= {message} ")

            flash("Email Sent Successfully", "information")
        except Exception as e:
            flash(f"{e}", "error")
        finally:
            connection.close()

    my_projects = projects
    return render_template("index.html", projects=my_projects)


if __name__ == '__main__':
    app.run()
