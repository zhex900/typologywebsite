from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import RadioField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"

questions = {
 'Initiating or responding?':['initiating', 'responding'],
 'Direct or informative?':['direct', 'informative'],
 'Control or movement?':['control', 'movement'],
 'Least confident answer?':['init/resp', 'dire/info', 'cont/move'],
 'Abstract or concrete?':['abstract', 'concrete'],
 'Affiliative or pragmatic?':['affiliative', 'pragmatic'],
 'Systematic or interest?':['systematic', 'interest'],
 'Least confident answer? ':['abs/conc', 'affl/prag', 'syst/intr']
}

@app.route("/", methods=["GET", "POST"])
def quiz():
    return render_template('website.html', questions = questions)

if __name__ == "__main__":
    app.run()