from sklearn.isotonic import IsotonicRegression
import matplotlib.pyplot as plt 
from matplotlib.collections import LineCollection
 
ir = IsotonicRegression() # create an instance of the IsotonicRegression class 

# Fit isotonic regression model 
y_ir = ir.fit_transform(x, y) # fit the model and transform the data 
print('Isotonic Regression Predictions :\n',y_ir)

# Create LineCollection for the isotonic regression line
lines = [[[i, y_ir[i]] for i in range(n)]]

# Line to measure the difference between actual and target value
lc = LineCollection(lines)

plt.plot(x, y_ir, '-', markersize=10, label='isotonic regression')

plt.gca().add_collection(lc)
plt.legend()  # add a legend

plt.title("Isotonic Regression")
plt.show()
