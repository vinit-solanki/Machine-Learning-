import streamlit as st 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

@st.cache_data
def load_data():
    iris = datasets.load_iris()
    df = pd.DataFrame(iris.data, columns=iris.feature_names)
    return df, iris.target, iris.target_names

df, target, target_names = load_data()

# Splitting features and target
X = df  # Features
y = target  # Target labels

# Train the model
model = RandomForestClassifier()
model.fit(X, y)

# Sidebar for input features
st.sidebar.title("Input Features")
sepal_length = st.sidebar.slider("Sepal Length", float(df['sepal length (cm)'].min()), float(df['sepal length (cm)'].max()), float(df['sepal length (cm)'].mean()))
sepal_width = st.sidebar.slider("Sepal Width", float(df['sepal width (cm)'].min()), float(df['sepal width (cm)'].max()), float(df['sepal width (cm)'].mean()))
petal_length = st.sidebar.slider("Petal Length", float(df['petal length (cm)'].min()), float(df['petal length (cm)'].max()), float(df['petal length (cm)'].mean()))
petal_width = st.sidebar.slider("Petal Width", float(df['petal width (cm)'].min()), float(df['petal width (cm)'].max()), float(df['petal width (cm)'].mean()))

# Prepare input data
input_data = np.array([[sepal_length, sepal_width, petal_length, petal_width]])

# Prediction
prediction = model.predict(input_data)
predicted_species = target_names[prediction[0]]  # Convert numeric label to species name

# Display results
st.subheader("Prediction")
st.write(f"Predicted Species: **{predicted_species}**")
