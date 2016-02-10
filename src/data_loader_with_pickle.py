
import sys
import gzip
try:
    import cPickle as pickle
except:
    import pickle
import numpy as np

def load_data(filename):
    if filename[-3:] == '.gz':
        f = gzip.open(filename, 'rb')
    elif filename[-4:] == '.pkl':
        f = open(filename, 'rb')
    else:
        print("Training data load error")
        sys.exit()
    #training_data, validation_data, test_data = pickle.load(f)
    training_data = pickle.load(f)
    f.close()
    return training_data

def load_data_wrapper(filename):
    data_num = 4800
    buf = load_data(filename)
    tr_d = ([np.array(x) for x in buf[0]], buf[1])
    va_d = tr_d[:]
    te_d = tr_d[:]
    training_inputs = [np.reshape(x, (data_num, 1)) for x in tr_d[0]]
    training_results = [vectorized_result(y) for y in tr_d[1]]
    training_data = zip(training_inputs, training_results)
    validation_inputs = [np.reshape(x, (data_num, 1)) for x in va_d[0]]
    validation_data = zip(validation_inputs, va_d[1])
    test_inputs = [np.reshape(x, (data_num, 1)) for x in te_d[0]]
    test_data = zip(test_inputs, te_d[1])
    return (training_data, validation_data, test_data)

def vectorized_result(j):
    output_num = 2
    e = np.zeros((output_num, 1))
    e[j] = 1.0
    return e

