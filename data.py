import numpy as np
from sklearn.model_selection import train_test_split
import random as r

def points_within_circle(radius, 
                         center=(0, 0),
                         number_of_points=100):
    center_x, center_y = center
    r = radius * np.sqrt(np.random.random((number_of_points,)))
    theta = np.random.random((number_of_points,)) * 2 * np.pi
    x = center_x + r * np.cos(theta)
    y = center_y + r * np.sin(theta)
    return x, y

red_x, red_y = points_within_circle(1.9, (2, 8), 100)
blue_x, blue_y = points_within_circle(1.6, (5, 3), 100)

red = list(zip(red_x, red_y))
blue = list(zip(blue_x, blue_y))

# labelling red with 0 and blue with 1:
labelled_data = list(zip(red + blue, 
                         [0] * len(red) + [1] * len(blue)))
r.shuffle(labelled_data)

data, labels = zip(*labelled_data)

res = train_test_split(data, labels, 
                       train_size=0.8,
                       test_size=0.2,
                    #    random_state=42
                       )
train_data, test_data, train_labels, test_labels = res
