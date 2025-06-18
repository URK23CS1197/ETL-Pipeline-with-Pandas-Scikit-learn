# task1_etl_pipeline.py
import pandas as pd
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
import joblib

# Load sample dataset
df = pd.read_csv('https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv')

# Preprocessing pipeline
numeric_features = ['age', 'fare']
numeric_transformer = Pipeline(steps=[('scaler', StandardScaler())])

categorical_features = ['sex', 'embarked']
categorical_transformer = Pipeline(steps=[('encoder', OneHotEncoder(handle_unknown='ignore'))])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ])

pipeline = Pipeline(steps=[('preprocessor', preprocessor)])

X = df[numeric_features + categorical_features].copy()
X_transformed = pipeline.fit_transform(X)

# Save the pipeline
joblib.dump(pipeline, 'etl_pipeline.pkl')
print("✅ ETL pipeline created and saved!")
