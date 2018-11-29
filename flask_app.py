# this file contains a small flask app

import os
import sys

from flask import Flask, render_template, flash, request

from jira_utils import JiraClient
from jira_form import JiraForm

# App configurations
DEBUG = True
app = Flask(__name__)

# set the HTML template name
HTML_TEMPLATE = "jira_form.html"

# get the environment variables
JIRA_SERVER = os.environ.get("JIRA_SERVER")
JIRA_USER = os.environ.get("USERNAME")
JIRA_PASSWORD = os.environ.get("PASSWORD")


@app.route("/", methods=["GET", "POST"])
def root_handler():
    """
    Controller to handle requests from /
    """
    form = JiraForm(request.form)

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        summary = request.form["summary"]
        component = request.form["component"]
        description = request.form["description"]
        project = request.form["project"]
        issuetype = request.form["issuetype"]

        if not form.validate():
            flash("All fields are required")

        jira_obj = JiraClient(JIRA_SERVER)
        jira_obj.login(JIRA_USER, JIRA_PASSWORD)
        flash("Logged at Jira!")

    return render_template(HTML_TEMPLATE, form=form)


if __name__ == "__main__":
    APP_PORT = os.environ.get("APP_PORT")
    app.run(host="0.0.0.0", port=int(APP_PORT))
