# PIPELINE WITH MULTIPLE TRANSFORMATIONS
# This is a sample code need to learn more about ColumnTransformer and Pipeline with multiple transformations

from sklearn.compose import ColumnTransformer
from sklearn.neighbors import KNeighborsClassifier
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder

preprocesor = ColumnTransformer([
    ('num', StandardScaler(), ['Age', 'Salary']),   # Numerical features
    ('cat', OneHotEncoder(), ['Gender'])            # Categorical feature
])

pipeline = Pipeline([
    ('preprocessor', preprocesor),                  # Step 1: Preprocessing
    ('knn_classifier', KNeighborsClassifier())      # Step 2: KNN Classifier
])

pipeline.fit(X_train, y_train)
prediction = pipeline.predict(X_new)

# Column Transformer applies different transformations to specified columns
# ColumnTransformer allows for separate preprocessing of numerical and categorical data
# Pipeline chains multiple steps together for streamlined processing

pipeline.fit(X_train, y_train)
pipeline.predict(X_new)
pipeline.named_steps['preprocessor']