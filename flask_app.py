# this file contains a small flask app

import os
import sys

from flask import Flask, render_template, flash, request

from jira_utils import JiraClient
from jira_form import JiraForm


JIRA_SERVER = os.environ.get("JIRA_SERVER")
JIRA_USER = os.environ.get("USERNAME")
JIRA_PASSWORD = os.environ.get("PASSWORD")

# App configurations
DEBUG = True
app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])
def root_handler():
    """
    Controller to handle requests from /
    """
    form = JiraForm(request.form)

    print form.errors
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        summary = request.form["summary"]
        component = request.form["component"]
        description = request.form["description"]
        project=request.form["project"]
        issuetype=request.form["issuetype"]
        print name, " ", email, " ", password," ",description," ",project," ",issuetype," "
        sys.stdout.flush()

        if form.validate():
            # Save the comment here.
            jira_obj = JiraClient(JIRA_SERVER)
            jira_obj.login(JIRA_USER, JIRA_PASSWORD)
            flash("Thanks for registration " + name)
        else:
            flash("Error: All the form fields are required. ")

    return render_template("hellor.html", form=form)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
