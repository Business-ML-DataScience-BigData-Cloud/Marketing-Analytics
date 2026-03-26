<span style="color:#FF512F; font-size:50px; font-weight:bold;"> 📢 Marketing Analytics </span>
# <span style="color:#00D4FF; font-size:40px; font-weight:bold;"> 📈 Demand Forecasting </span>

# Classification Tasks
# Supervised Machine Learning ALgorithms
# Both Below predicts the probability of class
# Logistic Regression:                             # Multi-Nomial Logistic Regression
# 1. It is used for Binary Classification          # It is used for Multi-Class Classification
# 2. It predicts(outputs) 2 values;                # It predicts(outputs) multiple classes
# 3. It uses Sigmoid function                      # It uses Softmax function
# a. Customer Churn or Employee Attrition (Yes/No) # a. Agree/Neutral/Disagree
# b. Email Detection (Spam/Ham)                    # b. Image Classification (Dog/Cat/Horse | 0-9 digits)
# c. Disease Detection or chances (yes/No)         # c. Demand (High/Medium/Low)
# d. Fraud Detection (Fraud/No Fraud)

!pip install pandas numpy scikit-learn

import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

import warnings
warnings.filterwarnings("ignore")

# <span style="color:#FF6EC7; font-size:30px; font-weight:bold;"> Data Integration </span>
data = pd.read_excel(r"Downloads\Marketing Data.xlsx")
print(data)

x = data[['Price', 'Advertising', 'Season']]
y = data['Demand_Level']

# <span style="color:#FF69B4; font-size:30px; font-weight:bold"><b> Multinomial Logistic Regression (Softmax Function)</b></span>
model = LogisticRegression()

# <span style="color:#00F0FF; font-size:35px; font-weight:bold;"> Training Model </span>
model.fit(x_train, y_train)

# <span style="color:#00E676; font-size:35px; font-weight:bold;"> Model Testing </span>
y_pred = model.predict(x_test)

print("Predicted Prices:", y_pred)
print("Actual Prices:", y_test)

# <span style="color:#FF4500; font-size:35px; font-weight:bold">Evaluating Model Accuracy</span> using <br>
# <span style="color:#1E90FF; font-size:30px; font-weight:bold">Classification_Report</span>
print(classification_report(y_pred, y_test))

# <span style="color:#F44336; font-size:35px; font-weight:bold;"> Predicting </span>
# <span style="color:#000000; font-size:28px; font-weight:bold;"> (Demand for a new Product) </span>
from IPython.display import display, HTML

new_product = [[25, 700, 0]]
new_prediction = model.predict(new_product)

result = new_prediction[0]

if result == 'High':
    display(HTML('<span style="color:#FF0000; font-size:30px; font-weight:bold;">🔥 High Demand</span>'))
elif result == 'Medium':
    display(HTML('<span style="color:#DA00FF; font-size:30px; font-weight:bold;">⚖️ Medium Demand</span>'))
else:
    display(HTML('<span style="color:#FF8C00; font-size:30px; font-weight:bold;">💤 Low Demand</span>'))
    
