# DAY 17 - LINEAR REGRESSION

import numpy as np  # Math calculator for python
from sklearn.linear_model import LinearRegression
# sklearn = AI / ML toolbox
# linear_model = Models based on lines
# LinearRegression = The brain we will train

# DATA (X = Input, Y = Output)
X = np.array([[1], [2], [3], [4], [5]])
print(np.shape(X))  # Check the shape of X
# X - (5, 1) means 5 rows and 1 column (Students, hours studied)

Y = np.array([10, 20, 30, 40, 50])
print(np.shape(Y))  # Check the shape of Y
# Y - (5,) means 5 rows (Scores)

for i in range(len(X)):
    print(f"Studied {X[i][0]} hours and scored {Y[i]} marks.")

# CREATE THE MODEL (The Brain)
model = LinearRegression()

# TRAIN THE MODEL
model.fit(X, Y)

# MAKE PREDICTIONS
prediction = model.predict([[8]])  # Predict the score for 8 hours of study
print(f"Predicted score for studying 6 hours: {prediction[0]}")