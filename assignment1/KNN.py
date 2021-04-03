from math import sqrt 
import csv
def euclidean_distance(row1, row2):
    distance = 0.0
    for i in range(len(row1)-1):
        distance += (row1[i] - row2[i])**2
    return sqrt(distance)
dataset = [[2,45,25,500000],
        [3,65,30, 800000,],
        [6,100,40, 1000000],
        [2,30,20,350000],
        [2,25,20, 100000]]


def get_neighbors(train, test_row, num_neighbors):
    distances = list()
    for train_row in train:
        distance = euclidean_distance(test_row, train_row)
        distances.append((train_row, distance))
    distances.sort(key=lambda tup: tup[1])
    neighbors = list()
    for i in range(num_neighbors):
        neighbors.append(distances[i][0])
    return neighbors

# Make a classification prediction with neighbors
def predict_classification(train, test_row, num_neighbors):
    neighbors = get_neighbors(train, test_row, num_neighbors)
    output_values = [row[-1] for row in neighbors]
    prediction = max(set(output_values), key=output_values.count)
    return prediction

test = [[4,100,25],[1,60,20]]

prediction0 = predict_classification(dataset, test[0] , 5)
prediction1 = predict_classification(dataset, test[0] , 2)
prediction2 = predict_classification(dataset, test[1] , 1)
prediction3 = predict_classification(dataset, test[1] , 2)
print(prediction0,prediction1)
print(prediction2,prediction3)

