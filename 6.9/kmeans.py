import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

if __name__ == '__main__':

    data = [
        [1.33, 4.19],
        [1.94, 5.47],
        [1.31, 4.32],
        [2.48, 5.64],
        [1.84, 5.17],
        [2.75, 6.35],
        [1.45, 4.68],
        [1.33, 3.96],
        [2.63, 5.62],
        [1.95, 5.02],
        [1.13, 4.34],
        [2.64, 5.64],
        [1.86, 5.33],
        [1.25, 3.18],
        [1.30, 4.36],
        [1.94, 5.39],
    ]

    kmeans = KMeans(n_clusters=3).fit(data)
    centers = kmeans.cluster_centers_
    
    scatter = plt.scatter([i[0] for i in data], [i[1] for i in data], c=kmeans.predict(data), s=50)
    for i, j in centers:
        plt.scatter(i, j, s=50, c='red', marker='+')

    plt.show()
