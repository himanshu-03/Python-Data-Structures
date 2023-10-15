import numpy as np
import matplotlib.pyplot as plt

# Function to accept data from the user


def get_user_data():
    num_points = int(input("Enter the number of data points: "))
    data = []
    for i in range(num_points):
        x = float(input(f"Enter x-coordinate for data point {i+1}: "))
        y = float(input(f"Enter y-coordinate for data point {i+1}: "))
        data.append([x, y])
    return np.array(data)

# Function to plot data points and centroids


def plot(data, centroids, cluster):
    plt.scatter(data[:, 0], data[:, 1], c=cluster)
    plt.scatter(centroids[:, 0], centroids[:, 1], c='r')
    plt.show()

# Function to assign each data point to the closest centroid


def assign_cluster(data, centroids):
    cluster = []
    # Looping through each data point
    for i in range(len(data)):
        distances = []
        # Looping through each centroid
        for j in range(len(centroids)):
            # Calculating the distance between the data point and the centroid
            distances.append(np.linalg.norm(data[i] - centroids[j]))
        # Assigning the data point to the closest centroid
        cluster.append(np.argmin(distances))
    return cluster

# Function to update centroids based on the assigned clusters


def update_centroids(data, cluster, k):
    centroids = []
    # Looping through each cluster
    for i in range(k):
        # Calculating the new centroid
        centroids.append(np.mean(data[np.array(cluster) == i], axis=0))
    return np.array(centroids)


# Get user input for data points
data = get_user_data()

# Plot the initial data points
plt.scatter(data[:, 0], data[:, 1])

# Get user input for the number of clusters (k)
k = int(input("Enter the number of clusters (k): "))

# Get user input for initial centroids
centroids = []
for i in range(k):
    x = float(input(f"Enter initial x-coordinate for centroid {i+1}: "))
    y = float(input(f"Enter initial y-coordinate for centroid {i+1}: "))
    centroids.append([x, y])
centroids = np.array(centroids)

# Run the k-means algorithm for a specified number of iterations
num_iterations = 10
for i in range(num_iterations):
    cluster = assign_cluster(data, centroids)
    centroids = update_centroids(data, cluster, k)

# Plot the final clusters and centroids
plot(data, centroids, cluster)

# Display the final clusters
print("Final clusters:", cluster)
