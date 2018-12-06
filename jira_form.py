# this file contains the jira form

from wtforms import Form, TextAreaField, validators, StringField, SubmitField, SelectField


class IssueCreationHomeForm(Form):
    """
    Form to be used at home page for Jira Issue creation
    """
    pass


class JiraIssueBaseForm(Form):
    pass

class JiraForm(Form):
    # user info
    name = StringField(
        "Name:",
        validators=[
            validators.required(
                message="Name: Please enter your name")],
        render_kw={"placeholder": "Enter your name here"})

    email = StringField(
        "Email:",
        validators=[
            validators.Email(
                message="Email: Please enter a valid email address"),
            ],
        render_kw={"placeholder": "Enter your email here"})

    # summary of the issue
    summary = StringField(
        "Summary:",
        validators=[
            validators.Length(
                message="Summary: Please enter minimum 10 characters summary",
                min=10,
                max=50)],
        render_kw={"placeholder": "Enter issue summary here"})

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
            validators.Length(
        message="Description: Please enter minimum 10 characters description",
        min=10,
        max=500)],
        render_kw={"placeholder": "Enter issue description here"})

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



    #project = StringField('Project:', validators=[validators.required(), validators.Length(min=5, max=100)])
    #issuetype = StringField('Issuetype:', validators=[validators.required(), validators.Length(min=5, max=100)])


class JiraEpicForm(JiraIssueBaseForm):
    pass

class JiraBugForm(JiraIssueBaseForm):
    pass

class JiraStoryForm(JiraIssueBaseForm):
    pass

class JiraTaskForm(JiraIssueBaseForm):
    pass
