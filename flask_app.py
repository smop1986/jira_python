# this file contains a small flask app

import os
import sys

from flask import Flask, render_template, flash, request

from jira_utils import JiraClient
from jira_form import JiraForm

# App configurations
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config["SECRET_KEY"] = "SjdnUends821Jsdlkvxh391ksdODnejdDw"

# set the HTML template name
HTML_TEMPLATE = "jira_form.html"

# get the environment variables
JIRA_SERVER = os.environ.get("JIRA_SERVER")
JIRA_USER = os.environ.get("JIRA_USER")
JIRA_PASSWORD = os.environ.get("JIRA_PASSWORD")
JIRA_PROJECT = os.environ.get("JIRA_PROJECT")


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
        priority = request.form["priority"]
        description = request.form["description"]
        severity = request.form["severity"]

        if not form.validate():
            flash("Error")
            return render_template(HTML_TEMPLATE, form=form)

        jira_obj = JiraClient(JIRA_SERVER)
        logged_in = jira_obj.login(JIRA_USER, JIRA_PASSWORD)
        print ("Logged in at Jira server {}".format(JIRA_SERVER))
        print name, email, summary, component, priority, description, severity
        if logged_in:
            print ("Creating issue at Jira..")
            issue_id = jira_obj.create_issue(
                project=JIRA_PROJECT,
                summary=summary,
                description=description + "\n\nFrom: {}\t{}".format(
                    name, email),
                issuetype={"name": "Task"}
            )
            print ("Created issue {} at Jira".format(issue_id))
            flash("Logged the issue at Jira!")

        sys.stdout.flush()

    return render_template(HTML_TEMPLATE, form=form)


if __name__ == "__main__":
    APP_PORT = os.environ.get("APP_PORT")
    app.run(host="0.0.0.0", port=int(APP_PORT))
