from flask import Flask, render_template,redirect, flash, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import joblib
import pandas as pd
import csv
import os 

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cattle_diseases.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# Load the trained model
model = joblib.load('model.pkl')

symptoms = [
    'itching', 'skin_rash', 'nodal_skin_eruptions', 'continuous_sneezing', 'shivering',
    'chills', 'joint_pain', 'stomach_pain', 'acidity', 'ulcers_on_tongue', 'muscle_wasting',
    'vomiting', 'burning_micturition', 'spotting_urination', 'fatigue', 'weight_gain',
    'anxiety', 'cold_hands_and_feets', 'mood_swings', 'weight_loss', 'restlessness',
    'lethargy', 'patches_in_throat', 'irregular_sugar_level', 'cough', 'high_fever',
    'sunken_eyes', 'breathlessness', 'sweating', 'dehydration', 'indigestion', 'headache',
    'yellowish_skin', 'dark_urine', 'nausea', 'loss_of_appetite', 'pain_behind_the_eyes',
    'back_pain', 'constipation', 'abdominal_pain', 'diarrhoea', 'mild_fever', 'yellow_urine',
    'yellowing_of_eyes', 'acute_liver_failure', 'fluid_overload', 'swelling_of_stomach',
    'swelled_lymph_nodes', 'malaise', 'blurred_and_distorted_vision', 'phlegm', 'throat_irritation',
    'redness_of_eyes', 'sinus_pressure', 'runny_nose', 'congestion', 'chest_pain',
    'weakness_in_limbs', 'fast_heart_rate', 'pain_during_bowel_movements', 'pain_in_anal_region',
    'bloody_stool', 'irritation_in_anus', 'neck_pain', 'dizziness', 'cramps', 'bruising',
    'obesity', 'swollen_legs', 'swollen_blood_vessels', 'puffy_face_and_eyes', 'enlarged_thyroid',
    'brittle_nails', 'swollen_extremeties', 'excessive_hunger', 'extra_marital_contacts',
    'drying_and_tingling_lips', 'slurred_speech', 'knee_pain', 'hip_joint_pain', 'muscle_weakness',
    'stiff_neck', 'swelling_joints', 'movement_stiffness', 'spinning_movements', 'loss_of_balance',
    'unsteadiness', 'weakness_of_one_body_side', 'loss_of_smell', 'bladder_discomfort',
    'foul_smell_of_urine', 'continuous_feel_of_urine', 'passage_of_gases', 'internal_itching',
    'toxic_look_(typhos)', 'depression', 'irritability', 'muscle_pain', 'altered_sensorium',
    'red_spots_over_body', 'belly_pain', 'abnormal_menstruation', 'dischromic_patches',
    'watering_from_eyes', 'increased_appetite', 'polyuria', 'family_history', 'mucoid_sputum',
    'rusty_sputum', 'lack_of_concentration', 'visual_disturbances', 'receiving_blood_transfusion',
    'receiving_unsterile_injections', 'coma', 'stomach_bleeding', 'distention_of_abdomen',
    'history_of_alcohol_consumption', 'blood_in_sputum', 'prominent_veins_on_calf', 'palpitations',
    'painful_walking', 'pus_filled_pimples', 'blackheads', 'scurring', 'skin_peeling',
    'silver_like_dusting', 'small_dents_in_nails', 'inflammatory_nails', 'blister',
    'red_sore_around_nose', 'yellow_crust_ooze'
]

class CattleDisease(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cattle_id = db.Column(db.String, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    breed = db.Column(db.String, nullable=False)
    weight = db.Column(db.Float, nullable=False)
    symptoms = db.Column(db.String, nullable=False)
    diagnosis = db.Column(db.String, nullable=False)
    treatment = db.Column(db.String, nullable=False)
    date_of_entry = db.Column(db.Date, nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            data = {
                'age': request.form.get('age'),
                'breed': request.form.get('breed'),
                'weight': request.form.get('weight'),
                'symptom1': request.form.get('symptom1'),
                'symptom2': request.form.get('symptom2'),
                'symptom3': request.form.get('symptom3'),
                'symptom4': request.form.get('symptom4'),
                'symptom5': request.form.get('symptom5'),
            }

            # Combine symptoms into one feature
            symptoms_combined = [
                data.get(f'symptom{i}', '') for i in range(1, 6)
            ]

            # Create a DataFrame for prediction
            features = pd.DataFrame([{
                symptom: (symptom in symptoms_combined) for symptom in symptoms
            }])

            # Print features for debugging
            print("Features for model:", features)

            # Make prediction
            prediction = model.predict(features)
            print("Prediction:", prediction)

            return render_template('predict.html', prediction=prediction[0], symptoms=symptoms_combined)
        
        except Exception as e:
            print("An error occurred during prediction:", e)
            return "Internal Server Error", 500

    return render_template('predict.html', symptoms=symptoms)
@app.route('/reviews')
def reviews():
    return render_template('review.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        first_name = request.form['firstName']
        last_name = request.form['lastName']
        email = request.form['email']
        mobile = request.form['mobile']
        message = request.form['message']

        # Ensure the CSV file is in a writable directory
        file_path = os.path.join(os.path.dirname(__file__), 'contact_data.csv')

        with open(file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([first_name, last_name, email, mobile, message])

        flash('Your information has been recorded successfully!')
        return redirect(url_for('contact'))

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
