from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    return render_template("index.html")

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")


@app.route("/application_form")
def application():
    """Returns application-form.html"""

    return render_template("application-form.html")


@app.route("/application", methods=["POST"])
def return_app_info():
    """Takes in application-form.html, grabs user information, and returns application-response.html"""

    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    salary = request.form.get("salaryrequirement")
    job_title = request.form.get("job")
    fullname = first_name + " " + last_name

    return render_template("application-response.html",
                            full_name=fullname,
                            salary_amount=salary,
                            job=job_title)


if __name__ == "__main__":
    app.run(debug=True)
