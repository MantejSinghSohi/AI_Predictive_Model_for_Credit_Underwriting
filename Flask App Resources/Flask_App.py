from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Encoding mappings
encoding_mappings = {
    'EmploymentStatus': {'Employed': 0, 'Self-Employed': 1, 'Unemployed': 2},
    'EducationLevel': {'Associate': 0, 'Bachelor': 1, 'Doctorate': 2, 'High School': 3, 'Master': 4},
    'MaritalStatus': {'Divorced': 0, 'Married': 1, 'Single': 2, 'Widowed': 3},
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form data
        inputs = {
            'Age': float(request.form['age']),
            'MaritalStatus': request.form['maritalStatus'],
            'EmploymentStatus': request.form['employmentStatus'],
            'EducationLevel': request.form['educationLevel'],
            'AnnualIncome': float(request.form['annualIncome']),
            'NetWorth': float(request.form['netWorth']),
            'CreditScore': float(request.form['creditScore']),
            'TotalLiabilities': float(request.form['totalLiabilities']),
            'TotalDebtToIncomeRatio': float(request.form['totalDebtToIncomeRatio']),
            'LoanAmount': float(request.form['loanAmount']),
            'LoanDuration': float(request.form['loanDuration']),
            'InterestRate': float(request.form['interestRate'])
        }

        # Convert categorical inputs to numeric
        for feature, mapping in encoding_mappings.items():
            if feature in inputs:
                inputs[feature] = mapping[inputs[feature]]

        # Create input array
        input_array = np.array([
            inputs['Age'],
            inputs['MaritalStatus'],
            inputs['EmploymentStatus'],
            inputs['EducationLevel'],
            inputs['AnnualIncome'],
            inputs['NetWorth'],
            inputs['CreditScore'],
            inputs['TotalLiabilities'],
            inputs['TotalDebtToIncomeRatio'],
            inputs['LoanAmount'],
            inputs['LoanDuration'],
            inputs['InterestRate']
        ], dtype=np.float32).reshape(1, -1)

        # Make prediction
        prediction = model.predict(input_array)
        result = "approved" if prediction[0] == 1 else "denied"

        return jsonify({
            'success': True,
            'prediction': result
        })

    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        })

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
