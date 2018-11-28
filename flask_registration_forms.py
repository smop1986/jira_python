from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
 
# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = 'key'
 
class ReusableForm(Form):
    name = TextField('Name:', validators=[validators.required()])
    email = TextField('Email:', validators=[validators.required(), validators.Length(min=6, max=35)])
    password = TextField('Password:', validators=[validators.required(), validators.Length(min=3, max=35)])
    description = TextField('Description:', validators=[validators.required(), validators.Length(min=10, max=100)])
    project = TextField('Project:', validators=[validators.required(), validators.Length(min=5, max=100)])
    issuetype = TextField('Issuetype:', validators=[validators.required(), validators.Length(min=5, max=100)])
 
@app.route("/", methods=['GET', 'POST'])
def hello():
    form = ReusableForm(request.form)
 
    print form.errors
    if request.method == 'POST':
        name=request.form['name']
        password=request.form['password']
        email=request.form['email']
        description=request.form['description']
        project=request.form['project']
        issuetype=request.form['issuetype']
        print name, " ", email, " ", password," ",description," ",project," ",issuetype," "
        import sys
        sys.stdout.flush()
 
        if form.validate():
            # Save the comment here.
            flash('Thanks for registration ' + name)
        else:
            flash('Error: All the form fields are required. ')
 
    return render_template('hellor.html', form=form)
 
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
