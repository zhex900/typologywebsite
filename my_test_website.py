from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import RadioField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.config["SECRET_KEY"] = "mysecret"

dichotomy_list = [["init", "resp"], ["dire", "info"], ["cont", "move"], ["abst", "conc"], ["affl", "prag"], ["syst", "intr"], ["tife", "fite"], ["sine", "nise"]]
#short for dichotomy_choices
dc = []
for i in dichotomy_list:
    dc.append([(i[0], i[0]), (i[1], i[1])])

class getForm(FlaskForm):
    dichotomy_choices0 = RadioField('init_resp', choices=dc[0])
    dichotomy_choices1 = RadioField('dire_info', choices=dc[1])
    dichotomy_choices2 = RadioField('cont_move', choices=dc[2])
    dichotomy_choices3 = RadioField('abst_conc', choices=dc[3])
    dichotomy_choices4 = RadioField('affl_prag', choices=dc[4])
    dichotomy_choices5 = RadioField('syst_intr', choices=dc[5])
    dichotomy_choices6 = RadioField('tife_fite', choices=dc[6])
    dichotomy_choices7 = RadioField('sine_nise', choices=dc[7])
    

@app.route("/", methods=["GET", "POST"])
def test():
    form = getForm()
    if form.validate_on_submit():
        print("it worked?")
    else:
        print("error")

    return render_template("website.html", form = form)

if __name__ == "__main__":
    app.run()