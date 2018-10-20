"""
    @Author:        Guillermo Rodriguez
    @Created:       10.17.2018
    @Purpose:       Hiearchial clustering class
"""

import numpy as np

class hiearchialClustering():

    def __init__(self, x, y):
        self.data = []
        self.clusters = {}

        _max = len(x) if len(x) > len(y) else len(y)        
        for counter in range(_max):
            self.data.append([x[counter], y[counter]])

    def set_cluster(self):
        
        while len(self.data) > 0:
            
            self.deltas = {}                # Displacement Hash
            _min_node = []                  # Minimal Node Pair Group

            # Get Minimal Distance Between Non Paired Nodes
            for parent in range(len(self.data) - 1):
                child = parent + 1
                while child < len(self.data):
                    self.deltas["%i-%i" % (parent, child)] = np.sqrt(   (self.data[parent][0] - self.data[child][0])**2 + 
                                                                        (self.data[parent][1] - self.data[child][1])**2 )
                    if len(_min_node) == 0 or self.deltas["%i-%i" % (parent, child)] < self.deltas["%i-%i" % (_min_node[0], _min_node[1])]:
                        _min_node = [parent, child]
                    
                    child += 1

            print( "Minimum Delta %f" % self.deltas["%i-%i" % (_min_node[0], _min_node[1])] )
            print(_min_node)

            if len(self.clusters) == 0:
                # Initialize Add Nodes to Cluster Group 
                self.clusters[0] = []
                self.clusters[0].append([self.data[_min_node[0]][0], self.data[_min_node[0]][1]])
                self.clusters[0].append([self.data[_min_node[1]][0], self.data[_min_node[1]][1]])
            
                # Remove Second Node
                del self.data[_min_node[1]]
                # Remove First Node
                del self.data[_min_node[0]]
                
            else:
                # Alternative Clusters
                means = {}
                for key, value in self.clusters.items():
                    # Find Cluster Means
                    average_x = 0
                    average_y = 0
                    nodes = 0
                    for node in value:
                        average_x += node[0] 
                        average_y += node[1]
                        nodes += 1.0
                    means[key] = [average_x/nodes, average_y/nodes]
            
                # Loop Through Active Nodes and Cluster Means
                _min_distance_to_cluster = self.deltas["%i-%i" % (_min_node[0], _min_node[1])] * 2
                _min_cluster = -1
                _min_data_node = -1
                _min_node = []
                for index in range(len(self.data)):
                    # Hash of Means
                    for key, value in means.items():
                        _distance = np.sqrt( ( self.data[index][0] - value[0] )**2 + ( self.data[index][1] - value[1] )**2 )
                        if _min_cluster == -1:
                            _min_cluster = key
                            _min_data_node = index
                            _min_distance_to_cluster = _distance
                            _min_node = [self.data[index][0], self.data[index][1]]
                        elif _min_distance_to_cluster > _distance:
                            _min_cluster = key
                            _min_data_node = index
                            _min_distance_to_cluster = _distance
                            _min_node = [self.data[index][0], self.data[index][1]]
                                                   
                if _min_distance_to_cluster < self.deltas["%i-%i" % (_min_node[0], _min_node[1])]:
                    # Minimum Distance is to Cluster
                    self.clusers[_min_cluster].append(_min_node)

                else:
                    # New Cluster
                    
            
            print(self.clusters)
            print(self.data)

_hc = hiearchialClustering(
        [12, 20, 28, 18, 29, 33, 24, 45, 45, 52, 51, 52, 55, 53, 55, 61, 64, 69, 72],
        [39, 36, 30, 52, 54, 46, 55, 59, 63, 70, 66, 63, 58, 23, 14, 8, 19, 7, 24]
)

print(_hc.data)

_hc.set_cluster()


#_hc.data.drop(_hc.data.index[0], inplace=True)
#print(_hc.data)