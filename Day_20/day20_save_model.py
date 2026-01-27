# MODEL SAVING

import joblib       # 'joblib' allows us to save models
from sklearn.linear_model import LinearRegression

# Train the model
X_train = [[1000], [1500], [2000], [2500], [3000]] # square feet
y_train = [50,75,100,125,150]               # price in lakhs

model = LinearRegression()
model.fit(X_train, y_train)

print(f"Model Coefficient: {model.coef_}")

# SAVE THE MODEL
filename = 'house_price_model.pkl'
joblib.dump(model, filename)

# SIMULATE RELOADING THE MODEL IN A NEW SCRIPT
model = None  # Clear the existing model

# LOAD THE MODEL
loaded_model = joblib.load(filename)

# MAKE PREDICTIONS WITH THE LOADED MODEL
sq_ft = [[1800]]
predicted_price = loaded_model.predict(sq_ft)
print(f"Predicted price for {sq_ft[0][0]} sq ft: {predicted_price[0]} lakhs")

# print(f" Math check {sq_ft[0][0]*loaded_model.coef_[0]} lakhs")

print(f"Loaded Model Coefficient: {loaded_model.coef_}")