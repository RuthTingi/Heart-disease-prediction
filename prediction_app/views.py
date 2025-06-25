from django.shortcuts import render
import joblib
import pandas as pd

# Load model and scaler
model = joblib.load('heart_model.pkl')
scaler = joblib.load('scaler.pkl')

def predict(request):
    prediction = None
    if request.method == 'POST':
        age = int(request.POST['age'])
        gender = 1 if request.POST['gender'] == 'Male' else 0
        glucose = float(request.POST['glucose'])
        sysBP = float(request.POST['sysBP'])
        diaBP = float(request.POST['diaBP'])
        BMI = float(request.POST['BMI'])
        smoker = 1 if request.POST['smoker'] == 'Yes' else 0

        # Prepare input data
        input_df = pd.DataFrame([[gender, age, glucose, sysBP, diaBP, BMI, smoker]],
                                columns=['Gender', 'age', 'glucose', 'sysBP', 'diaBP', 'BMI', 'currentSmoker'])

        scaled_input = scaler.transform(input_df)
        result = model.predict(scaled_input)[0]

        prediction = "HIGH RISK" if result == 1 else "LOW RISK"

    return render(request, 'form.html', {'prediction': prediction})
