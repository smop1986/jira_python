# this file contains the jira form

from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField, SelectField


class JiraForm(Form):
    # user info
    name = TextField('Name:', validators=[validators.required()])
    email = TextField('Email:', validators=[
                      validators.required(), validators.Length(min=6, max=35)])

    # issue info

    # summary of the issue
    summary = TextField(
        "Summary:",
        validators=[
            validators.required(),
            validators.Length(min=10, max=50)
        ]
    )

    # component of the issue (drop down)
    component_choices = ["Product Backlog"]
    component = SelectField(
        "Component:",
        choices=component_choices,
        validators=[
            validators.required()
        ]
    )

    # description of the issue
    description = TextAreaField(
        "Description:",
        validators=[
            validators.required(),
            validators.Length(min=10, max=500)
        ]
    )

    # Priority of the issue
    priority_choices = ["Blocker", "Critical", "Major", "Minor", "Trival"]

    prirority = SelectField(
        "Priority",
        choices=priority_choices,
        validators=[
            validators.required()
        ]
    )
    #project = TextField('Project:', validators=[validators.required(), validators.Length(min=5, max=100)])
    #issuetype = TextField('Issuetype:', validators=[validators.required(), validators.Length(min=5, max=100)])
