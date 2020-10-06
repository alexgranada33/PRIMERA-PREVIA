#!/usr/bin/env python
# coding: utf-8

# In[7]:


# REGRESIÓN LOGÍSTICA

# regresion_logistica_01

import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
from utilities import visualize_classifier

# Define los datos de entrada
X = np.array([[3.1, 7.2], [4, 6.7], [2.9, 8], [5.1, 4.5], [6, 5],
[5.6, 5], [3.3, 0.4], [3.9, 0.9], [2.8, 1], [0.5, 3.4], [1, 4],
[0.6, 4.9]])
y = np.array([0, 0, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3])

print("X = \n", X)
print("\ny = ", y)

# Crea el clasificador de regresión logística
clasificador = linear_model.LogisticRegression(solver='liblinear',
C=1)

# Train the classifier
clasificador.fit(X, y)

# Visualize the performance of the classifier
visualize_classifier(classifier, X, y)

