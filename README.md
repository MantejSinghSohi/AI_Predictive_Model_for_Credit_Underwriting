# 🔮 Loan Predictor App

![Loan Predictor App](image3.jpg)

A machine learning-powered web application that predicts loan approval probability based on personal, financial, and loan-specific parameters.

## 📌 Features

### Interactive Web Interface with:
- Clean and intuitive UI built with Streamlit and Flask (separate interfaces)
- Responsive design with wide layout
- Easy navigation through menus

#### 🎯 Loan Predictor Tool
Collects and analyzes three categories of information:

**👤 Personal Details**
- Age (18-80 years)
- Marital Status (Single/Married/Divorced/Widowed)
- Employment Status (Employed/Self-Employed/Unemployed)
- Education Level (High School/Associate/Bachelor/Master/Doctorate)

**💰 Financial Details**
- Annual Income (0-500,000 USD)
- Net Worth (0-5,000,000 USD)
- Credit Score (300-800)
- Total Liabilities (0-25,000 USD)
- Total Debt to Income Ratio (0.016-4.65)

**📝 Loan Details**
- Loan Amount (0-500,000 USD)
- Loan Duration (12-120 months)
- Interest Rate (10%-50%)

## 🛠️ Technical Stack

- **Frontend:** 
  - Streamlit (Web Interface)
  - Flask (API Interface)
- **Backend:** Python
- **Machine Learning:** Pickle (for model deployment)
- **Data Processing:** NumPy, Pandas, Scikit-Learn, Matplotlib, Seaborn

## 🌐 Available Interfaces

### Streamlit Web Application
- Interactive web interface with form inputs
- Real-time predictions
- Visual feedback and explanations
- Access at `http://localhost:8501` when running locally

### Flask REST API
- RESTful API endpoint for predictions
- Suitable for integration with other applications
- JSON request/response format
- Access at `http://localhost:5000/predict` when running locally
- API documentation available at `http://localhost:5000/docs`

## 📊 Model Information

The application uses a pre-trained machine learning model (`model.pkl`) that considers 12 different features to make predictions about loan approval probability.

## 🔄 Input Processing

- Categorical variables (Marital Status, Employment Status, Education Level) are encoded using predefined mappings
- Numerical inputs are validated within specified ranges
- Features are processed in a specific order to match the model's training configuration


## 📂 Requirements
- **Python 3.x**  
- Required Libraries:  
  - `pandas`  
  - `numpy`  
  - `scikit-learn`  
  - `matplotlib`  
  - `seaborn`  
  - `streamlit`  
  - `flask`  

## 🚀 Installation & Setup

1. Clone the repository
```bash
git clone https://github.com/MantejSinghSohi/AI_Predictive_Models_for_Credit_Underwriting.git
cd AI_Predictive_Models_for_Credit_Underwriting
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the application
  
For Streamlit Web Interface: 
- Navigate to the "Streamlit App Resources" folder and run the "Streamlit_App.py" file.
```bash
cd Streamlit_App_Resources
python Streamlit_App.py
```

For Flask API:
- Navigate to the "Flask App Resources" folder and run the "Flask_App.py" file.
```bash
cd Flask_App_Resources
python Flask_App.py
```

## 👨‍💻 Developer

- **Name:** Mantej Singh Sohi
- **Institution:** IIT Kharagpur
- **Program:** B.Tech in Agricultural and Food Engineering
- **GitHub:** [MantejSinghSohi](https://github.com/MantejSinghSohi)
- **Email:** mantejsohi2005@kgpian.iitkgp.ac.in