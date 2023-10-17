# Importing modules that are required

from sklearn.datasets import load_boston
from sklearn.linear_model import LassoLars
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split

# Loading dataset
dataset = load_boston()
X = dataset.data
y = dataset.target

# Splitting training and testing data
X_train, X_test, y_train, y_test = train_test_split(X, y,
					test_size = 0.15, random_state = 42)

# Creating and fitting the regressor
regressor = LassoLars(alpha = 0.1)
regressor.fit(X_train, y_train)


# Evaluating model
prediction = regressor.predict(X_test)

print(f"r2 Score of test set : {r2_score(y_test, prediction)}")
