# Test Design Document

Project Title: Fake News Detection using Social Media Data  
Author: Souparnika P S

## 1. Objective
The objective of testing is to verify that the Fake News Detection system correctly analyzes input news text and classifies it as Fake News or Real News using the trained machine learning model.

## 2. Scope of Testing
The testing process covers the following components:
- Data preprocessing
- Feature extraction using TF-IDF
- Machine learning model predictions
- Streamlit frontend user interface
- Input validation

## 3. Testing Types

### Functional Testing
Ensures that the system produces correct predictions based on user input.

### Model Testing
Validates the machine learning model's performance using evaluation metrics such as accuracy, precision, recall, and F1-score.

### Interface Testing
Verifies that the Streamlit web interface accepts user input and displays results correctly.

### Input Validation Testing
Ensures the system handles empty inputs or incorrect inputs properly.

## 4. Tools Used
- Python
- scikit-learn
- Streamlit
- Google Colab / Local Python environment

## 5. Expected Outcome
The system should:
- Accept user input text and topic
- Process the input through the trained model
- Display a prediction result indicating whether the news is Fake or Real