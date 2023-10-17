import pandas as pd
import numpy as np
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from mlxtend.feature_selection import SequentialFeatureSelector

# Define the array of data
data = np.array([[1, 2, 3, 4],
				[5, 6, 7, 8],
				[9, 10, 11, 12]])

# Convert the array into a dataframe
df = pd.DataFrame(data)

# Select the features and target
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

# Perform stepwise regression
sfs = SequentialFeatureSelector(linear_model.LogisticRegression(),
								k_features=3,
								forward=True,
								scoring='accuracy',
								cv=None)
selected_features = sfs.fit(X, y)

# Create a dataframe with only the selected features
selected_columns = [0, 1, 2, 3]
df_selected = df[selected_columns]

# Split the data into train and test sets
X_train, X_test,\
	y_train, y_test = train_test_split(
		df_selected, y,
		test_size=0.3,
		random_state=42)

# Fit a logistic regression model using the selected features
logreg = linear_model.LogisticRegression()
logreg.fit(X_train, y_train)

# Make predictions using the test set
y_pred = logreg.predict(X_test)

# Evaluate the model performance
print(y_pred)

