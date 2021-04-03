from sklearn.cluster import KMeans
from numpy import sqrt, array, random, argsort,argmin,newaxis,sort
from sklearn.preprocessing import scale
import matplotlib.pyplot as plt

x = array([7845,778,942,143,0.75,7956,810,976,146,0.76,8215,825,1002,152,0.78,8542,847,1038,157,0.78,8150,100587,807,1015,150,0.72,8386,884,101964,1085,138,0.82,8219,827,995,158,0.82,7500,745,948,135,0.67,9257,901,120967,1154,148,0.72,8553,811,1218,175,0.84])
print(x.max())
print(x.min())
x = x.reshape(-1,1)
x_ax = range(53)
kmeans = KMeans(n_clusters = 4).fit(x)
def closest_centroid(points, centroids):
    distances = sqrt(((points - centroids[:, newaxis])**2).sum(axis=2))
    return argsort(distances, axis=1)


center = kmeans.cluster_centers_
order_index = closest_centroid(x,center)

indexes = set()
for i in order_index:
    indexes = i[-3:]
    indexes = [*indexes,*indexes]
values = x[indexes].flat[0:100]
print(values)

