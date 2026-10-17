
import numpy as np
from sklearn.neural_network import MLPClassifier

# Get training data
n = int(input("Enter number of training samples: "))
X = []
y = []

for i in range(n):
    a = int(input("Enter input 1 (0 or 1): "))
    b = int(input("Enter input 2 (0 or 1): "))
    target = int(input("Enter target output (0 or 1): "))
    X.append([a, b])
    y.append(target)

# Create and train neural network
model = MLPClassifier(
    hidden_layer_sizes=(4,),
    activation="relu",
    solver="lbfgs",
    max_iter=2000,
    random_state=1
)
model.fit(X, y)

# Predict output
a = int(input("Enter test input 1: "))
b = int(input("Enter test input 2: "))

result = model.predict([[a, b]])
print("Predicted Output:", result[0])
