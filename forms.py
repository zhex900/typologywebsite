from flask_wtf import FlaskForm
from wtforms import RadioField
from wtforms.validators import DataRequired

class DichotomyForm(FlaskForm):
    dichotomies = [("a", "a"), ("b", "b")]
    dichotomy = RadioField("yes", choices=dichotomies)