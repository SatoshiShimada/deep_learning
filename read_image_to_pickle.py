#!/usr/bin/python
# encode: utf-8

try:
    import cPickle as pickle
except:
    import pickle
import sys
import math
try:
    import Image
except:
    from PIL import Image

imgsize = (40, 40)

if __name__ == '__main__':
    labeling_data = []
    label = []
    train = []

    filenamelist = 'filename.list'
    fp = open(filenamelist, 'r')
    for name in fp.readlines():
        filename, class_label = name.split()
        img = Image.open(filename)
        img = img.resize(imgsize)
        data = []
        for y in xrange(img.size[1]):
            for x in xrange(img.size[0]):
                p = img.getpixel((x, y)) 
                R = p[0]
                G = p[1]
                B = p[2]
                # change range to 0~1.0 from 0~255.0
                data.append(R / 255.0)
                data.append(G / 255.0)
                data.append(B / 255.0)
        train.append(data)
        label.append(class_label)

# Normalization of data
    Normalize = False
    if Normalize:
        x = []
        N = len(labeling_data)
        for i in xrange(40 * 40):
            x.append(0.)
            for n in xrange(N):
                x[i] = x[i] + labeling_data[n][0][i]
            x[i] = x[i] / N
        index = 0
        for data, desire in labeling_data[:]:
            i = 0
            new_data = []
            for buf in data:
                new_data.append(buf - x[i])
                i += 1
            labeling_data[index][0] = new_data
            index += 1

        sigma = []
        for i in xrange(40 * 40):
            buf = 0.
            for data, desire in labeling_data:
                buf += (data[i] - x[i]) ** 2
            sigma.append(math.sqrt(buf / N))
        for i in xrange(40 * 40):
            index = 0
            for data, desire in labeling_data[:]:
                labeling_data[index][0][i] = (data[i] - x[i]) / N
                index += 1

    outputfilename = 'out.pkl'
    f = open(outputfilename, 'w')
    pickle.dump(labeling_data, f)
    f.close()

