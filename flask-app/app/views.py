import logging
import json

from flask import Flask, render_template
from flask_wtf import FlaskForm
from flask import request
from wtforms import fields
from wtforms import DateField
from wtforms import SelectField
from wtforms import IntegerField
from wtforms.validators import InputRequired, Optional
from datetime import date
#from wtforms.fields.html5 import DateField

from . import app, estimator, target_names

app = Flask(__name__)
app.config['SECRET_KEY'] = 'you-will-never-guess'

logger = logging.getLogger('app')

class PredictForm(FlaskForm):
    GENDER_CHOICES = [('0','Male'),('1','Female')]
    SIGNUP_FLOW = [('2', 'Page ID 0'),('1', 'Page ID 1'),('2','Page ID 2'),('3','Page ID 3'),('4','Page ID 4'),('5','Page ID 5'),
               ('8','Page ID 8'),('10','Page ID 10'),('12','Page ID 12'),('15','Page ID 15'),('16','Page ID 16'),
               ('20','Page ID 20'),('21','Page ID 21'),('23','Page ID 23'),('24','Page ID 24'),('25','Page ID 25')]

    """Fields for Predict"""
    dt = DateField('Pick date:',format="%m/%d/%Y",validators=[InputRequired()])
    #day = fields.SelectField('Day:',choices=[(i, i) for i in range(1,31)])
    #month = fields.SelectField('Month:',choices=[(i, i) for i in range(1,13)])
    age = fields.DecimalField('Age:',validators=[InputRequired()])
    #age = fields.SelectField('Age:',choices=[(i, i) for i in range(18,101)])
    number_of_searches = fields.DecimalField('Number of searches:',validators=[InputRequired()])
    #number_of_searches = fields.SelectField('Number of searches:',choices=[(i, i) for i in range(1,200)])
    gender = fields.SelectField('Gender:', choices=GENDER_CHOICES,validators=[InputRequired()])
    signup = fields.SelectField('Signup Page:', choices=SIGNUP_FLOW,validators=[InputRequired()])
    
    submit = fields.SubmitField('Submit')


@app.route('/', methods=['GET', 'POST'])
def index():
    """Index page"""
    
    predicted = None
    # if request.method == 'POST':
    #     form = PredictForm(request.form)
    #     print(type(request.data))
    #     print(request.data)
    #     submitted_data = json.loads(str(request.data))
    #     #submitted_data = json.dumps(request.data)#, default=lambda o: o.__dict__)
    #     #submitted_data = json.loads(str(request.data))
    #     #submitted_data = request.data.decode('utf-8')
    #     print(submitted_data, 'a')

    # else:
    #     form = PredictForm()
    #     submitted_data = {'dt':'04/01/2014','age':23,'number_of_searches':123,'gender':0,'signup':8}
    #     print(submitted_data, 'b')

    #form = PredictForm(request.form)
    form = PredictForm()
    #submitted_data = json.loads(request.data.decode('utf-8'))
    print(form.validate_on_submit())
    #if request.method == 'POST': #and form.validate_on_submit():
    if form.validate_on_submit():
        # store the submitted values
        print(request.data)
        submitted_data = form.data
        print(submitted_data)

        # Retrieve values from form
        #dt = form.dt.data.strftime('%x')
        #dat = submitted_data['dt'].strftime('%x')
        
        day = float(submitted_data['dt'].day)
        #day = float(submitted_data['day'])
        print(day)
        month = float(submitted_data['dt'].month)
        #month = float(submitted_data['month'])
        print(month)
        age = float(submitted_data['age'])
        print(age)
        number_of_searches = float(submitted_data['number_of_searches'])
        print(number_of_searches)
        gender = float(submitted_data['gender'])
        print(gender)
        signup = float(submitted_data['signup'])
        print(signup)
        
        # Create array from values
        #flower_instance = [sepal_length, sepal_width, petal_length, petal_width]
        #information = [age, gender, signup, number_of_searches, 50, 70, 20, 30, 300, 1000, month, 1, month, 2014, 15]
        #information = [number_of_searches, 50, 70, month, 20, 11, signup, day, 50, 40, 1, 2014, age, 0, 1000]
        information = [month,number_of_searches,age,day,gender,signup]
        print(information)
        my_prediction = estimator.predict(information)
        # Return only the Predicted iris species
        predicted = target_names[my_prediction[0]]
        #predicted = my_prediction
        print(predicted[0])
        
    return render_template('index.html',
        form=form,
        prediction=predicted)



# Start the app server on port 80
# (The default website port)
#app.run(host='0.0.0.0')
if __name__ == '__main__':
    app.run(debug=True)
