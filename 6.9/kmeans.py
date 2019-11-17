import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

if __name__ == '__main__':

	# read data from text file
    data_file = open('data.txt', 'r')
    data = []

    for line in data_file.readlines():
    	data.append(list(map(float, line.strip().split(' '))))

    data_file.close()

    # apply K-Means algorithm to fit the data set, and get cluster centers
    kmeans = KMeans(n_clusters=3).fit(data)
    centers = kmeans.cluster_centers_

    # draw the scatter diagram to illustrate the result
    scatter = plt.scatter([i[0] for i in data], [i[1] for i in data], c=kmeans.predict(data), s=50)
    for i, j in centers:
        plt.scatter(i, j, s=50, c='red', marker='+')

    plt.show()
