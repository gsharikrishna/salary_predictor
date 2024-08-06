from django.shortcuts import render
import joblib
import pandas as pd
from .forms import SalaryPredictionForm

# Load the pre-trained model and label encoders
model = joblib.load('salary_model.pkl')
label_encoders = joblib.load('label_encoders.pkl')

def home(request):
    return render(request, 'home.html')

def predict_salary(request):
    if request.method == 'POST':
        form = SalaryPredictionForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            # Ensure the values are in the correct format and case
            try:
                encoded_data = {}
                for field in ['education_level', 'job_title', 'geographic_location', 'company_size', 'skills_and_abilities']:
                    value = data[field].strip().lower()  # Convert to lowercase
                    if value not in label_encoders[field].classes_:
                        return render(request, 'error.html', {'message': f'Invalid value for {field}: {data[field]}'})
                    encoded_data[field] = label_encoders[field].transform([value])[0]

                # Prepare the input data for prediction
                input_data = {
                    'years_of_experience': [int(data['years_of_experience'])],
                    'age': [int(data['age'])],
                    'education_level': [encoded_data['education_level']],
                    'job_title': [encoded_data['job_title']],
                    'geographic_location': [encoded_data['geographic_location']],
                    'company_size': [encoded_data['company_size']],
                    'skills_and_abilities': [encoded_data['skills_and_abilities']]
                }
                
                input_df = pd.DataFrame(input_data)
                predicted_salary = model.predict(input_df)[0]
                
                # Format the salary as INR
                formatted_salary = f'₹{predicted_salary:,.2f}'

                return render(request, 'result.html', {'predicted_salary': formatted_salary})
            except ValueError as e:
                return render(request, 'error.html', {'message': f'Invalid value for a category: {e}'})
    else:
        form = SalaryPredictionForm()

    return render(request, 'predict.html', {'form': form})
