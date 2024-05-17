import os
import cv2
import sys
import numpy as np
from math import *

train_set_dir = sys.argv[1]
test_set_dir = sys.argv[2]

def scalar_product(x, y):
    s = 0
    N = x.shape[0]
    for i in range(N):
        s += x[i] * y[i]
    return s

def vector_length(x):
    return sqrt(scalar_product(x, x))

def vector_normalize(x):
    N = x.shape[0]
    y = np.zeros(N)
    d = vector_length(x)
    a = 1 / d

    for i in range(N):
        y[i] = a * x[i]
    return y

def image_into_array(image):
    _, image_bin = cv2.threshold(image, 128, 255, cv2.THRESH_BINARY)
    thresh = 128
    maxval = 1
    image_bin = (image > thresh) * maxval
    return np.concatenate(image_bin).ravel()

class Pattern:
    def __init__(self, x, label):
        self.x = x
        self.label = label

class PatternSet:
    def __init__(self, title):
        self.title = title
        self.patterns = []
    
    def load(self, folder_name):
        file = open(folder_name+'/description.txt', 'r')
        lines = file.read().splitlines()
        file.close()

        for line in lines:
            words = line.split(':')
            imagefile = words[0]
            label = words[1]

            image = cv2.imread(folder_name+'/'+imagefile)
            image_bin = image_into_array(image)
            
            x = vector_normalize(image_bin)
            pat = Pattern(x, label)
            self.patterns.append(pat)

    def display(self):
        print(self.title)
        N = len(self.patterns)
        for i in range(N):
            print('patter no. %d' % (i + 1))
            print('label =', self.patterns[i].label)
            print('x = ', self.patterns[i].x, sep = '')
            print('d = %.3f' % vector_length(self.patterns[i].x))
            print()

class Neuron:

    def __init__(self, w ,label):
        self.w = w
        self.label = label

    def calculate_output(self, x):
        return scalar_product(self.w, x)
    
class Network:

    def __init__(self):
        self.neurons = []
    
    def train(self, training_set):
        for i in range(len(training_set.patterns)):
            self.neurons.append(Neuron(training_set.patterns[i].x, training_set.patterns[i].label))
    
    def test(self, test_set):
        num_test_patters = len(test_set.patterns)
        num_neurons = len(self.neurons)
        for k in range(num_test_patters):
            out_max = 0
            index = 0
            for n in range(num_neurons):
                out = self.neurons[n].calculate_output(test_set.patterns[k].x)
                if out > out_max:
                    out_max = out
                    index = n

            print('%s -> %s, confidence: %f' % (test_set.patterns[k].label, self.neurons[index].label, out_max))

train = PatternSet('treningowy')
train.load(train_set_dir)
net = Network()
net.train(train)

testowy = PatternSet('testowy')
testowy.load(test_set_dir)
net.test(testowy)

#train.display()
#testowy.display()

# Manipulator stolo-kulotoczny