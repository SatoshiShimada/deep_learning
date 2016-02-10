#!/usr/bin/python
# coding: utf-8

import numpy as np

import sys
sys.path.append('./src')
import neural_network as network

class Logic(object):
    def __init__(self):
        self.logic_and  = [[[0, 0], 0], [[0, 1], 0], [[1, 0], 0], [[1, 1], 1]]
        self.logic_or   = [[[0, 0], 0], [[0, 1], 1], [[1, 0], 1], [[1, 1], 1]]
        self.logic_exor = [[[0, 0], 0], [[0, 1], 1], [[1, 0], 1], [[1, 1], 0]]

    def vectorize(self, x):
        ret = np.zeros((2, 1))
        ret[x] = 1
        return ret

    def training_data(self, datatype=''):
        if datatype == 'and':
            data = self.logic_and
        elif datatype == 'or':
            data = self.logic_or
        elif datatype == 'exor':
            data = self.logic_exor
        else:
            data = []
            return []
        ret = [(np.array(x), self.vectorize(y)) for x, y in data]
        return ret

    def test_data(self, datatype=''):
        if datatype == 'and':
            data = self.logic_and
        elif datatype == 'or':
            data = self.logic_or
        elif datatype == 'exor':
            data = self.logic_exor
        else:
            data = []
            return []
        ret = [(np.array(x), y) for x, y in data]
        return ret

if __name__ == '__main__':
    datapath = 'parameter/logic/and/'
    logic = Logic()

    training_data = logic.training_data('and')
    test_data     = logic.test_data('and')

    ### parameters ###
    epochs = 300
    mini_batch_size = 1
    learning_rate = 0.5

    net = network.Neural_Network([2, 3, 2])
    # training network
    net.train(training_data, epochs, mini_batch_size, learning_rate)
    #net.save_parameter(datapath)
    # evaluate network
    net.feed_forward(test_data)

