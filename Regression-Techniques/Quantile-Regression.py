# Python program to visualize quantile regression

# Importing libraries
import numpy as np
import pandas as pd
import statsmodels.api as sm
import statsmodels.formula.api as smf
import matplotlib.pyplot as plt

np.random.seed(0)

# Number of rows
rows = 20

# Constructing Distance column
Distance = np.random.uniform(1, 10, rows)

# Constructing Emission column
Emission = 40 + Distance + np.random.normal(loc=0,
											scale=.25*Distance, 
											size=20)

# Creating a dataset
df = pd.DataFrame({'Distance': Distance, 
				'Emission': Emission})

# #fit the model
model = smf.quantreg('Emission ~ Distance', 
					df).fit(q=0.7)

# define figure and axis
fig, ax = plt.subplots(figsize=(10, 8))

# get y values
y_line = lambda a, b: a + Distance
y = y_line(model.params['Intercept'],
		model.params['Distance'])

# Plotting data points with the help
# pf quantile regression equation
ax.plot(Distance, y, color='black')
ax.scatter(Distance, Emission, alpha=.3)
ax.set_xlabel('Distance Traveled', fontsize=20)
ax.set_ylabel('Emission Generated', fontsize=20)

# Save the plot
fig.savefig('quantile_regression.png')
