"""
    @Author:        Guillermo Rodriguez
    @Created:       10.17.2018
    @Purpose:       k-means clustering class
"""

import pandas as pd
import numpy as np
import operator 
import copy

class kmeans():

    def __init__(self, x, y, k):
        np.random.seed(100)

        self.data = pd.DataFrame({
            'x': x,
            'y': y
        })

        self.max_x = max(enumerate(x))[1] * 1.1
        self.min_x = min(enumerate(x))[1] - abs(0.9*min(enumerate(x))[1])
        self.max_y = max(enumerate(y))[1] * 1.1
        self.min_y = min(enumerate(y))[1] - abs(0.9*min(enumerate(y))[1])
        
        self.k = k

        self.centroids = {}
        for counter in range(self.k):
            self.centroids[counter] = [
                                        np.random.randint(self.min_x, self.max_x),
                                        np.random.randint(self.min_y, self.max_y)
                                       ]
        self.kmeans = {}

    def plot(self):
        # Scatter Plot
        pass

    def set_means(self):
        
        for key, value in self.centroids.items():
            # Displacement Factor to Centroids
            self.data["Distance_to_Center_%i" % key] = ( 
                np.sqrt( (self.data['x'] - value[0])**2 + (self.data['y'] -value[1])**2 )
            )

        data_delta = []
        for column in range(self.k):
            data_delta.append("Distance_to_Center_%i" % column)
        
        self.data['owner'] = self.data.loc[:, data_delta].idxmin(axis=1)
        self.data['owner'] = self.data['owner'].map(lambda x: int(x.lstrip('Distance_to_Center_')))

    def update_centroid(self):
        for counter in range(self.k):
            self.centroids[counter][0] = np.mean(self.data[self.data['owner'] == counter]['x'])
            self.centroids[counter][1] = np.mean(self.data[self.data['owner'] == counter]['y']) 



_kmeans = kmeans(
            [12, 20, 28, 18, 29, 33, 24, 45, 45, 52, 51, 52, 55, 53, 55, 61, 64, 69, 72],
            [39, 36, 30, 52, 54, 46, 55, 59, 63, 70, 66, 63, 58, 23, 14, 8, 19, 7, 24],
            2
)

print(_kmeans.centroids)
_kmeans.set_means()
print(_kmeans.data.head())

while True:
    present = _kmeans.data['owner'].copy(deep=True)
    _kmeans.update_centroid()

    print(_kmeans.centroids)
    _kmeans.set_means()
    print(_kmeans.data.head())

    if present.equals(_kmeans.data['owner']):
        print("K-Means Tabulated")
        break
