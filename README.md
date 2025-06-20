# ETL-Pipeline-with-Pandas-Scikit-learn
An automated ETL pipeline using Pandas and Scikit-learn to load data, scale numeric features, encode categorical columns, and save the preprocessing steps using joblib. Ensures consistent and reusable data transformation for machine learning workflows.

*COMPANY*: CODTECH IT SOLUTIONS

*NAME*: NIRANSON CDK

*INTERN ID* : CT04DG534

*DOMAIN*: DATA SCIENCE

*DURATION*: 4 WEEKS

*MENTOR*: NEELA SANTOSH

In this task, I developed a complete ETL (Extract, Transform, Load) pipeline using Python, leveraging powerful libraries such as Pandas and Scikit-learn. The goal of this project was to automate the data preprocessing workflow commonly used in data science and machine learning projects. A clean and consistent ETL pipeline helps ensure that raw data is converted into a structured, machine-readable format suitable for model training or analytics.

Extraction (E)
The pipeline begins with the extraction of data. I used the Titanic dataset available publicly from the Seaborn data repository (https://raw.githubusercontent.com/mwaskom/seaborn-data/master/titanic.csv). This dataset contains various passenger information such as age, fare, gender, and port of embarkation, and serves as a common benchmark dataset for classification tasks (survived or not). It was read using pandas.read_csv(), a reliable method for ingesting structured CSV data into a DataFrame.

 Transformation (T)
The transformation stage is the most important and involved part of the ETL pipeline. I selected the relevant columns (age, fare, sex, embarked) for transformation, as they represent both numerical and categorical data that require different preprocessing techniques.

 Numerical Features
The numeric features (age, fare) were scaled using StandardScaler from Scikit-learn. Standard scaling transforms these features into a standardized distribution with a mean of 0 and a standard deviation of 1. This is essential for many machine learning algorithms that rely on distance metrics or gradient-based learning.

 Categorical Features
The categorical features (sex, embarked) were handled using OneHotEncoder, which converts categories into binary vectors. This ensures that the model treats them as independent and non-ordinal categories.

 ColumnTransformer
To combine both types of transformations in one step, I used Scikit-learn's ColumnTransformer, which allows applying different preprocessing steps to different columns. This modular approach ensures reusability and scalability across datasets with mixed types of features.

Loading (L)
After preprocessing, the transformed dataset was ready for downstream use. Instead of saving the transformed data, I saved the entire pipeline using joblib as a .pkl file (etl_pipeline.pkl). This file can later be loaded and used to preprocess new, unseen data in the exact same way as the original data — ensuring consistency and avoiding data leakage.

*OUTPUT*

This task resulted in a clean, reusable, and automated ETL pipeline capable of processing any Titanic-like dataset with numerical and categorical inputs. The saved pipeline (.pkl) can be integrated directly into machine learning training scripts or deployed into production for real-time inference workflows.This hands-on task not only demonstrated the importance of preprocessing but also gave me practical experience in writing modular, scalable, and industry-standard data pipelines using Python. It forms the foundational step of any serious machine learning project.

