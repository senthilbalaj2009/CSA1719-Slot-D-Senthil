
from sklearn.tree import DecisionTreeClassifier

# Get training data from user
n = int(input("Enter number of training samples: "))

X = []
y = []

for i in range(n):
    outlook = int(input("Enter outlook (0=Rainy, 1=Sunny): "))
    temperature = int(input("Enter temperature (0=Cool, 1=Hot): "))
    play = int(input("Play cricket? (0=No, 1=Yes): "))

    X.append([outlook, temperature])
    y.append(play)

# Train Decision Tree
model = DecisionTreeClassifier()
model.fit(X, y)

# Predict using user input
print("\nEnter values for prediction:")
outlook = int(input("Outlook (0=Rainy, 1=Sunny): "))
temperature = int(input("Temperature (0=Cool, 1=Hot): "))

prediction = model.predict([[outlook, temperature]])

if prediction[0] == 1:
    print("Prediction: Play Cricket")
else:
    print("Prediction: Do Not Play Cricket")
