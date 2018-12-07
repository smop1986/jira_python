# this file contains the jira form

from wtforms import Form, TextAreaField, validators, \
        StringField, SubmitField, SelectField, \
        RadioField


class JiraIssueHomeForm(Form):
    """
    Form to be used at home page for Jira Issue creation
    """

    issue_choices = [("bug", "Bug"),
                     ("story", "Story"),
                     ("epic", "Epic"),
                     ("theme", "Theme")]

    issue_type = RadioField(
        "Issue type:",
        choices=issue_choices)


class JiraIssueBaseForm(Form):
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

    project_choices = [("IDD", "ISG-DBA-DEVOPS")]

    project = SelectField(
        "Project:",
        choices=project_choices,
        validators=[
            validators.required("Please select the Project")])

    # component of the issue (drop down)
    component_choices = [("product_backlog", "Product Backlog")]

    component = SelectField(
        "Component:",
        choices=component_choices,
        validators=[
            validators.required("Please select one component.")])


class JiraEpicForm(JiraIssueBaseForm):
    epic_name = StringField(
        "Epic Name:",
        validators=[
            validators.required(
                message="Epic Name: Please enter Epic name here")],
        render_kw={"placeholder": "Enter Epic name here"})

    # summary of the issue
    summary = StringField(
        "Summary:",
        validators=[
            validators.Length(
                message="Summary: Please enter minimum 10 characters summary",
                min=1,
                max=50)],
        render_kw={"placeholder": "Enter issue summary here"})

    # description of the issue
    description = TextAreaField(
        "Description:",
        validators=[
            validators.Length(
        message="Description: Please enter minimum 10 characters description",
        min=1,
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


class JiraBugForm(JiraIssueBaseForm):

    # summary of the issue
    summary = StringField(
        "Summary:",
        validators=[
            validators.Length(
                message="Summary: Please enter minimum 10 characters summary",
                min=1,
                max=50)],
        render_kw={"placeholder": "Enter issue summary here"})

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

    # description of the issue
    description = TextAreaField(
        "Description:",
        validators=[
            validators.Length(
        message="Description: Please enter some description",
        min=1,
        max=500)],
        render_kw={"placeholder": "Enter issue description here"})

    # severity of the issue
    severity_choices = [(None, "None"),
                        ("blocker", "Blocker"),
                        ("critical", "Critical"),
                        ("major", "Major"),
                        ("minor", "Minor"),
                        ("trival", "Trivial")]

    severity = SelectField(
        "Severity:",
        choices=severity_choices,
        validators=[
            validators.required("Please select severity of the bug")])


    found_choices = [(None, "None"),
                     ("in_sprint", "In Sprint"),
                     ("outside_of_sprint", "Outside of Sprint"),
                     ("in_production", "In Production"),
                     ("uat", "UAT"),
                     ("deferred", "Deferred - Push into Production"),
                    ]

    found = SelectField(
        "Found:",
        choices=found_choices,
        validators=[
            validators.required("Please select Found for bug")])


class JiraThemeForm(JiraIssueBaseForm):
    # summary of the Theme
    summary = StringField(
        "Summary:",
        validators=[
            validators.Length(
                message="Summary: Please enter some Theme summary",
                min=1,
                max=50)],
        render_kw={"placeholder": "Enter Theme summary here"})

    # description of the issue
    description = TextAreaField(
        "Description:",
        validators=[
            validators.Length(
        message="Description: Please enter some Theme description here",
        min=1,
        max=500)],
        render_kw={"placeholder": "Enter Theme description here"})

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
            validators.required("Please select priority of the Theme.")])


class JiraStoryForm(JiraIssueBaseForm):
    # summary of the Theme
    summary = StringField(
        "Summary:",
        validators=[
            validators.Length(
                message="Summary: Please enter some Story summary here",
                min=1,
                max=50)],
        render_kw={"placeholder": "Enter Story summary here"})

    # description of the issue
    description = TextAreaField(
        "Description:",
        validators=[
            validators.Length(
        message="Description: Please enter some Story description here",
        min=1,
        max=500)],
        render_kw={"placeholder": "Enter Story description here"})

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
            validators.required("Please select priority of the Story.")])
