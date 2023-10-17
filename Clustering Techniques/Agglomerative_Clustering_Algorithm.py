from numpy import unique
from numpy import where
from matplotlib import pyplot
from sklearn.datasets import make_classification
from sklearn.cluster import AgglomerativeClustering

# initialize the data set we'll work with
training_data, _ = make_classification(
    n_samples=1000,
    n_features=2,
    n_informative=2,
    n_redundant=0,
    n_clusters_per_class=1,
    random_state=4
)

# define the model
agglomerative_model = AgglomerativeClustering(n_clusters=2)

# assign each data point to a cluster
agglomerative_result = agglomerative_model.fit_predict(training_data)

# get all of the unique clusters
agglomerative_clusters = unique(agglomerative_result)

# plot the clusters
for agglomerative_cluster in agglomerative_clusters:
    # get data points that fall in this cluster
    index = where(agglomerative_result == agglomerative_clusters)
    # make the plot
    pyplot.scatter(training_data[index, 0], training_data[index, 1])

# show the Agglomerative Hierarchy plot
pyplot.show()
