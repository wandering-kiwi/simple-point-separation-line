from data import *
import numpy as np

M=np.random.random()*3
C = np.random.random()*4

def vert_dist_to_line(m, c, pos):
    x = pos[0]
    y=pos[1]
    return m*x + c - y
def cost(m, c):
    avg_red_dist = 0
    avg_blue_dist = 0
    for i in range(len(red)):
        avg_red_dist += vert_dist_to_line(m, c, red[i])
        avg_blue_dist += vert_dist_to_line(m, c, blue[i])
    avg_red_dist /= len(red)
    avg_blue_dist /= len(blue)
    return avg_red_dist * avg_blue_dist

def dist_to_line(m, c, pos):
    x1 = pos[0]
    y1 = pos[1]
    d = m * y1 + x1
    x2 = (d - c*m)/(m**2+1)
    y2 = m* x2 + c
    vert_comp = y2 - y1
    sign = abs(vert_comp)/vert_comp
    dist = np.sqrt((x2 - x1)**2 + (y2-y1)**2)

    return sign * dist

def better_cost(m, c):
    avg_red_dist = 0
    avg_blue_dist = 0
    for i in range(len(red)):
        avg_red_dist +=  dist_to_line(m, c, red[i])
        avg_blue_dist += dist_to_line(m, c, blue[i])
    avg_red_dist /= len(red)
    avg_blue_dist /= len(blue)
    return avg_red_dist * avg_blue_dist

def derive(func, x, delta=0.01):
    return (func(x+delta) - func(x))/delta

def sigmoid(x):
    return 1/(np.exp(-x) + 1)

def tweak(m, c, iters=100, learning_rate=0.001, delta=0.0001, cost_func = cost):
    return_lst = [[m, c, cost(m, c)]]
    m_ = m
    c_ = c
    for i in range(iters-1):
        dm = derive(lambda x: sigmoid(cost_func(x, c_)), m_, delta) * learning_rate
        dc = derive(lambda x: sigmoid(cost_func(m_, x)), c_, delta) * learning_rate
        m_ -= dm
        c_ -= dc
        return_lst.append([m_, c_, sigmoid(cost(m_, c_))])
    return return_lst