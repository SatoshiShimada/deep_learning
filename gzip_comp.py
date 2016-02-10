#!/usr/bin/python
# encode: utf-8

import gzip
import sys

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print '{0} [filename]'.format(sys.argv[0])
        sys.exit()
    else:
        gzip_compression(sys.argv[1])

def gzip_compression(filename):
        fin = open(filename, 'rb')
        fout = gzip.open(filename + '.gz', 'wb')
        fout.writelines(fin)
        fout.close()
        fin.close()

