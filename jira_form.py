# this file contains the jira form

from wtforms import Form, TextAreaField, validators, StringField, SubmitField, SelectField


class JiraForm(Form):
    # user info
    name = StringField(
        "Name:",
        validators=[validators.required("Please enter your name.")])

    email = StringField(
        "Email:",
        validators=[
            validators.Email("Please enter a valid email address."),
            validators.required("Please enter your email address.")])

    # summary of the issue
    summary = StringField(
        "Summary:",
        validators=[
            validators.required("Please enter issue summary"),
            validators.Length(min=10, max=50)])

    # component of the issue (drop down)
    component_choices = [("product_backlog", "Product Backlog")]
    component = SelectField(
        "Component:",
        choices=component_choices,
        validators=[
            validators.required("Please select one component.")])

    # description of the issue
    description = TextAreaField(
        "Description:",
        validators=[
            validators.required("Please enter description of the issue."),
            validators.Length(min=10, max=500)])

    # Priority of the issue
    priority_choices = [("blocker", "Blocker"),
                        ("critical", "Critical"),
                        ("major", "Major"),
                        ("minor", "Minor"),
                        ("trival", "Trivial")]

    priority = SelectField(
        "Priority:",
        choices=priority_choices,
        validators=[
            validators.required("Please select priority of the issue.")])

    # severity of the issue
    # since the choices are same
    severity_choices = priority_choices 

    severity = SelectField(
        "Severity:",
        choices=severity_choices,
        validators=[
            validators.required("Please select severity of the issue.")])

    #project = StringField('Project:', validators=[validators.required(), validators.Length(min=5, max=100)])
    #issuetype = StringField('Issuetype:', validators=[validators.required(), validators.Length(min=5, max=100)])
