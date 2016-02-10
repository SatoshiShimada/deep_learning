#!/usr/bin/python
# coding: utf-8

import sys
sys.path.append('src/')

import numpy as np

import neural_network as network
import mnist_loader_with_pickle as loader


if __name__ == '__main__':
    datapath = 'parameter/mnist/'

    print 'Loading...'
    training_data, validation_data, test_data = loader.load_data_wrapper()
    print 'Load done'

    ### parameters ###
    epochs = 50
    mini_batch_size = 1
    learning_rate = 0.01
    dropout_rate = (0.8, 0.9)

    net = network.Neural_Network([784, 30, 10], dropout_rate)
    net.set_test(test_data)
    net.set_validation(validation_data)

    # train_type := True or False as Train or Test
    train_type = True
    if train_type:
        #net.load_parameter(path=datapath)
        print 'Training network start'
        net.train(training_data, epochs, mini_batch_size, learning_rate)
        print 'Training done'
        #net.save_parameter(path=datapath)
    else:
        net.load_parameter(path=datapath)
        net.feed_forward(test_data)

