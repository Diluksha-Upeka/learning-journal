# Classification

import numpy as np
from sklearn.linear_model import LogisticRegression

# The data
X_train = np.array([
    [0, 0],     # Safe No links, no typos
    [1, 0],     # Safe One link, no typos
    [0, 1],     # Safe No links, one typo
    [10,5],     # Spam Many links, many typos
    [5,3],      # Spam
    [8,2]       # Spam
])

# Labels (0 = Safe, 1 = Spam)
y_train = np.array([0, 0, 0, 1, 1, 1])

# Model
model = LogisticRegression()
model.fit(X_train, y_train)

# Prediction
new_email = [[6,4]] # 6 links, 4 typos

# Predict probability
probability = model.predict_proba(new_email)
print(f"Probability of being Spam: {probability[0][1]*100:.2f}") 

# Predict class
prediction = model.predict(new_email)
print(f"Prediction: {prediction[0]}")