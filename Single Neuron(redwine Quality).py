# -*- coding: utf-8 -*-
"""Untitled8.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AB1Tr9Jv5ImYI2syHYy-OOL8xjgzuJ5T

# **A SINGLE NEURON**
"""

# adding all the libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense

data = pd.read_csv("winequality-red.csv")

print("Dataset Preview:")
print(data.head())

print("\nDataset Shape:", data.shape)

X = data.drop(columns=['quality'])  # Features (11 columns)
y = data['quality']                 # Target (wine quality)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

#Step 3: Build the Neural Network
model = Sequential([
    Dense(64, activation='relu', input_shape=(11,)),  # Input layer (11 features)
    Dense(32, activation='relu'),                     # Hidden layer
    Dense(1)                                          # Output layer (regression)
])

#compile
model.compile(optimizer='adam', loss='mse', metrics=['mae'])

#training
history = model.fit(X_scaled, y, epochs=50, validation_split=0.2, verbose=1)

#plotting
plt.figure(figsize=(10, 5))
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.xlabel("Epochs")
plt.ylabel("Loss")
plt.legend()
plt.title("Model Training Performance")
plt.show()

#final model evaluation
loss, mae = model.evaluate(X_scaled, y, verbose=0)
print(f"\nFinal Model Loss: {loss:.4f}, Mean Absolute Error: {mae:.4f}")