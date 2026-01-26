# SCALING AND PIPELINES

# Problem : Salary(50000) is huge compared to Age(25)
# The model will ignore Age feature

import numpy as np                                  # For numerical operations
from sklearn.pipeline import Pipeline               # For creating ML pipelines
from sklearn.preprocessing import StandardScaler    # For feature scaling
from sklearn.neighbors import KNeighborsClassifier  # For KNN classification

# The data
# [Age, Salary]
X_train = np.array([
    [20, 20000],   # Young, Low salary -> No buy(0)
    [25, 25000],   # Young, Low salary -> No buy(0)
    [35, 80000],   # Middle-aged, Medium salary -> Buy(1)
    [40, 120000],  # Middle-aged, High salary -> Buy(1)
    [45, 150000],  # Old, High salary -> Buy(1)
    [50, 200000]   # Old, Very high salary -> No buy(0)
])

y_train = np.array([0, 0, 1, 1, 1, 0])  # Labels: 0 = No buy, 1 = Buy

# THE PIPELINE 
model_pipeline = Pipeline([
    ('scaler', StandardScaler()),               # Step 1: Scale features
    ('knn_classifier', KNeighborsClassifier())  # Step 2: KNN Classifier
])

# Train the model
model_pipeline.fit(X_train, y_train)

# New customer data for prediction
new_customer = [[32, 85000]]  # Age: 32, Salary: 85000

# Predict using the pipeline
prediction = model_pipeline.predict(new_customer)
print(f"Prediction for new customer: {prediction}")

scaler_step = model_pipeline.named_steps['scaler'] # Access the scaler step
scaler_input = scaler_step.transform(new_customer)  # Scale the new customer data
print(f"Scaled features for new customer: {scaler_input}")
