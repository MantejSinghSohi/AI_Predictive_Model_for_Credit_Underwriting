import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

# Encoding mappings
encoding_mappings = {
    'EmploymentStatus': {'Employed': 0, 'Self-Employed': 1, 'Unemployed': 2},
    'EducationLevel': {'Associate': 0, 'Bachelor': 1, 'Doctorate': 2, 'High School': 3, 'Master': 4},
    'MaritalStatus': {'Divorced': 0, 'Married': 1, 'Single': 2, 'Widowed': 3},
}

# Selected features grouped
selected_features = {
    "Personal Details": [
        'Age',
        'MaritalStatus',
        'EmploymentStatus',
        'EducationLevel'
    ],
    "Financial Details": [
        'AnnualIncome',
        'NetWorth',
        'CreditScore',
        'TotalLiabilities',
        'TotalDebtToIncomeRatio'
    ],
    "Loan Details": [
        'LoanAmount',
        'LoanDuration',
        'InterestRate'
    ]
}

# Update the feature order to match model's expectations
model_feature_order = [
    'Age',
    'MaritalStatus',
    'EmploymentStatus',
    'EducationLevel',
    'AnnualIncome',
    'NetWorth',
    'CreditScore',
    'TotalLiabilities',
    'TotalDebtToIncomeRatio',
    'LoanAmount',
    'LoanDuration',
    'InterestRate'
]

# Streamlit UI
st.set_page_config(page_title="Loan Predictor App", layout="wide")

# Sidebar navigation
menu = st.sidebar.radio(
    "Navigate",
    ["Home", "Loan Predictor Tool", "About Us"]
)

# Home Page
if menu == "Home":
    st.write("# 🔮 Welcome to the Loan Predictor App!")
    st.image("image3.jpg", use_container_width=True)
    st.write("""
    ##### 💡 Loans are financial tools that help individuals or organizations achieve their goals, whether it's buying a home, starting a business, or managing unforeseen expenses. However, lending involves a significant risk for financial institutions, as they must ensure that borrowers have the capacity and intent to repay the loan.
    """)
    st.markdown("""
    #### 🎯 This app is designed to **predict whether a loan application will be approved or denied** based on various factors, including:
    - **👤 Personal Details:** Information like age, marital status, education, and employment status.
    - **💰 Financial Details:** Key financial metrics such as income, net worth, liabilities, credit score, and debt-to-income ratio.
    - **📝 Loan Details:** Specifics about the requested loan, including amount, duration, interest rate, and a calculated risk score.
    """)

    st.write("""
    #### ⚙ How Does it Work?
    - Enter your details in the Loan Predictor Tool.
    - The app uses a trained machine learning model to analyze your inputs.
    - It predicts whether the loan is likely to be approved or denied.
    """)

    col1, col2 = st.columns([1, 1])
    with col1:
        st.image("image1.png", width=480, output_format='auto')
    with col2:
        st.image("image2.jpeg", width=340, output_format='auto')

    st.write(
        "#### 📊 A brief about the inputs that will be used to make predictions:")
    st.markdown("""
    - **👤 Personal Details**
        - Age: Age of the borrower in years.
        - Marital Status: Marital status of the borrower (Single, Married, etc.).
        - Employment Status: Employment type of the borrower.
        - Education Level: Highest level of education completed by the borrower.
    - **💰 Financial Details**
        - Annual Income: Borrower's annual income.
        - Net Worth: Borrower's total net worth.
        - Total Liabilities: Total liabilities of the borrower.
        - Total Debt to Income Ratio: Debt as a proportion of income.
    - **📝 Loan Details**
        - Loan Amount: The amount of loan requested.
        - Loan Duration: Duration of the loan in months.
        - Interest Rate: The interest rate offered for the loan.
        - Risk Score: The calculated risk score for the borrower.
    """)

# Loan Predictor Tool
elif menu == "Loan Predictor Tool":
    st.title("🔮 Loan Predictor Tool")
    st.write("### ✍️ Fill in the details below to check if the loan will be approved:")

    # User Inputs
    inputs = {}

    # Personal Details
    st.subheader("👤 Personal Details")
    inputs['Age'] = st.number_input("Age", min_value=18, max_value=80, value=40, step=1)
    inputs['MaritalStatus'] = st.selectbox("Marital Status", options=list(encoding_mappings['MaritalStatus'].keys()))
    inputs['EmploymentStatus'] = st.selectbox("Employment Status", options=list(encoding_mappings['EmploymentStatus'].keys()))
    inputs['EducationLevel'] = st.selectbox("Education Level", options=list(encoding_mappings['EducationLevel'].keys()))

    # Financial Details
    st.subheader("💰 Financial Details")
    inputs['AnnualIncome'] = st.number_input("Annual Income (in USD)", min_value= 0, max_value=500000, value=50000, step=1000)
    inputs['NetWorth'] = st.number_input("Net Worth (in USD)", min_value= 0, max_value=5000000, value=100000, step=10000)
    inputs['CreditScore'] = st.number_input("Credit Score", min_value=300, max_value=800, value=500, step= 5)
    inputs['TotalLiabilities'] = st.number_input("Total Liabilities (in USD)", min_value=0, max_value=25000, value=3000, step=100)
    inputs['TotalDebtToIncomeRatio'] = st.number_input("Total Debt to Income Ratio", min_value=0.016, max_value=4.65, value=0.30, step=0.01)

    # Loan Details
    st.subheader("📝 Loan Details")
    inputs['LoanAmount'] = st.number_input("Loan Amount (in USD)", min_value=0, max_value=500000, value=10000, step=1000)
    inputs['LoanDuration'] = st.number_input("Loan Duration (in months)", min_value=12, max_value=120, value=24, step=1)
    inputs['InterestRate'] = st.number_input("Interest Rate", min_value=0.01, max_value=0.50, value=0.05, step=0.01)

    # Convert categorical inputs to numeric
    for feature, mapping in encoding_mappings.items():
        if feature in inputs:
            inputs[feature] = mapping[inputs[feature]]
    
    try:
        # Create input array in the same order as training
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
        
        # Predict button
        if st.button("Predict"):
            import warnings
            warnings.simplefilter(action='ignore', category=FutureWarning)
            warnings.simplefilter(action='ignore', category=UserWarning)
            
            prediction = model.predict(input_array)
            if prediction[0] == 1:
                st.success("The loan is likely to be **approved**! ✅")
            else:
                st.error("The loan is likely to be **denied**. ❌")

    except Exception as e:
        st.error(f"Data preparation error: {str(e)}")

# About Us
elif menu == "About Us":
    st.title("👋 About Us")
    st.write("##### 🎓 I am Mantej Singh Sohi, a student of IIT Kharagpur, currently pursuing my B.Tech in Agricultural and Food Engineering.")
    st.write("###### 🚀 This app is developed as a Loan Predictor Tool using Machine Learning.")
    st.write("🔗 GitHub: https://github.com/MantejSinghSohi")
    st.write("📧 Email: mantejsohi2005@kgpian.iitkgp.ac.in")