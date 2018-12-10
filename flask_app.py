# this file contains a small flask app

import os
import sys

from flask import Flask, render_template, flash, request, redirect

from jira_utils import JiraClient
from jira_form import JiraIssueHomeForm, JiraStoryForm, \
    JiraBugForm, JiraThemeForm, JiraEpicForm

# App configurations
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config["SECRET_KEY"] = "SjdnUends821Jsdlkvxh391ksdODnejdDw"

# set the HTML template name
HOME_TEMPLATE = "jira_home_form.html"
BUG_TEMPLATE = "jira_bug_form.html"
STORY_TEMPLATE = "jira_story_form.html"
EPIC_TEMPLATE = "jira_epic_form.html"
THEME_TEMPLATE = "jira_theme_form.html"

# get the environment variables
JIRA_SERVER = os.environ.get("JIRA_SERVER")
JIRA_USER = os.environ.get("JIRA_USER")
JIRA_PASSWORD = os.environ.get("JIRA_PASSWORD")
JIRA_PROJECT = os.environ.get("JIRA_PROJECT")


def grab_common_data(form):
    project = form["project"]
    name = form["name"]
    email = form["email"]
    summary = form["summary"]
    component = form["component"]
    priority = form["priority"]
    description = form["description"]
    return project, name, email, summary, component, priority, description


@app.route("/bug", methods=["GET", "POST"])
def bug_handler():
    """
    Controller to handle requests from /bug
    """
    form = JiraBugForm(request.form)

    if request.method == "POST":
        project, name, email, summary, component, priority, description = \
            grab_common_data(request.form)
        severity = request.form["severity"]
        found = request.form["found"]

        if not form.validate():
            flash("Error")
            return render_template(BUG_TEMPLATE, form=form)

        jira_obj = JiraClient(JIRA_SERVER)
        logged_in = jira_obj.login(JIRA_USER, JIRA_PASSWORD)
        print ("Logged in at Jira server {}".format(JIRA_SERVER))
        print name, email, summary, component, priority, description
        if logged_in:
            print ("Creating bug at Jira..")
            issue_id = jira_obj.create_issue(
                project=JIRA_PROJECT,
                summary=summary,
                # priority=priority,
                description=description + "\n\nFrom: {}\t{}".format(
                    name, email),
                issuetype={"name": "Bug"},
                # priority=priority,
                # severity=severity,
                # found=found
            )
            print ("Created bug {} at Jira".format(issue_id))
            flash("Logged the bug at Jira!")

        sys.stdout.flush()

    return render_template(BUG_TEMPLATE, form=form)


@app.route("/epic", methods=["GET", "POST"])
def epic_handler():
    """
    Controller to handle requests from /epic
    """
    form = JiraEpicForm(request.form)

    if request.method == "POST":
        project, name, email, summary, component, priority, description = \
            grab_common_data(request.form)
        epic_name = request.form["epic_name"]

        if not form.validate():
            flash("Error")
            return render_template(EPIC_TEMPLATE, form=form)

        jira_obj = JiraClient(JIRA_SERVER)
        logged_in = jira_obj.login(JIRA_USER, JIRA_PASSWORD)
        print ("Logged in at Jira server {}".format(JIRA_SERVER))
        print name, email, summary, component, priority, description
        if logged_in:
            print ("Creating bug at Jira..")
            issue_id = jira_obj.create_issue(
                project=JIRA_PROJECT,
                summary=summary,
                # priority=priority,
                description=description + "\n\nFrom: {}\t{}".format(
                    name, email),
                issuetype={"name": "Epic"},
                # priority=priority,
                # epic_name=epic_name
            )
            print ("Created Epic {} at Jira".format(issue_id))
            flash("Logged the Epic at Jira!")

        sys.stdout.flush()

    return render_template(EPIC_TEMPLATE, form=form)


@app.route("/story", methods=["GET", "POST"])
def story_handler():
    """
    Controller to handle requests from /
    """
    form = JiraStoryForm(request.form)

    if request.method == "POST":
        project, name, email, summary, component, priority, description = \
            grab_common_data(request.form)
        if not form.validate():
            flash("Error")
            return render_template(STORY_TEMPLATE, form=form)

        jira_obj = JiraClient(JIRA_SERVER)
        logged_in = jira_obj.login(JIRA_USER, JIRA_PASSWORD)
        print ("Logged in at Jira server {}".format(JIRA_SERVER))
        print name, email, summary, component, priority, description
        if logged_in:
            print ("Creating Story at Jira..")
            issue_id = jira_obj.create_issue(
                project=JIRA_PROJECT,
                summary=summary,
                description=description + "\n\nFrom: {}\t{}".format(
                    name, email),
                issuetype={"name": "Story"},
                # priority=priority,
            )
            print ("Created Story {} at Jira".format(issue_id))
            flash("Logged the Story at Jira!")

        sys.stdout.flush()

    return render_template(STORY_TEMPLATE, form=form)


@app.route("/theme", methods=["GET", "POST"])
def theme_handler():
    """
    Controller to handle requests from /theme
    """
    form = JiraThemeForm(request.form)

    if request.method == "POST":
        project, name, email, summary, component, priority, description = \
            grab_common_data(request.form)
        if not form.validate():
            flash("Error")
            return render_template(THEME_TEMPLATE, form=form)

        jira_obj = JiraClient(JIRA_SERVER)
        logged_in = jira_obj.login(JIRA_USER, JIRA_PASSWORD)
        print ("Logged in at Jira server {}".format(JIRA_SERVER))
        print name, email, summary, component, priority, description
        if logged_in:
            print ("Creating Theme at Jira..")
            issue_id = jira_obj.create_issue(
                project=JIRA_PROJECT,
                summary=summary,
                description=description + "\n\nFrom: {}\t{}".format(
                    name, email),
                issuetype={"name": "Theme"},
                # priority=priority,
            )
            print ("Created Theme {} at Jira".format(issue_id))
            flash("Logged the Theme at Jira!")

        sys.stdout.flush()

    return render_template(THEME_TEMPLATE, form=form)


@app.route("/", methods=["GET", "POST"])
def root_handler():
    """
    Controller to handle requests for /
    """
    form = JiraIssueHomeForm()

    if request.method == "POST":
        issue_type = request.form["issue_type"]
        print issue_type

        # if not form.validate():
        #    flash("Error")
        #    return render_template(HOME_TEMPLATE, form=form)

        return redirect("/{}".format(issue_type))

    return render_template(HOME_TEMPLATE, form=form)


if __name__ == "__main__":
    APP_PORT = os.environ.get("APP_PORT")
    app.run(host="0.0.0.0", port=int(APP_PORT))
