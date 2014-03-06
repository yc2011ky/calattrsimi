#! /usr/bin/env python
# calattrsimi.py

import sys
from sets import Set
def calattrsimi(set1, set2):
    sectionset = set1 & set2
    print 'the intersection set is ', sectionset
    unionset = set1 | set2
    print 'the union set is ', unionset
    l1 = len(sectionset) + 0.0
    l2 = len(unionset) + 0.0
    print l1, l2
    simi = l1 / l2 + 0.0
    return simi

def readfile(filename, dict):
   # dict = {}
    file_object = open(filename, 'r')
    try:
        for line in file_object:
            items = line.strip('\n').split('::')
            filmid = int(items[0])
            genre = items[1]
            dict[filmid] = str(genre)
    finally:
        file_object.close()

def writeFile(filename, dict):
    file_object = open(filename, 'w')
    keys = dict.keys()
   # print keys
    length = len(keys)
    try:
        for i in range(length-1):
            key1 = dict[keys[i]].split('|')
            set1 = set(key1)
            set1.remove('')
            print 'set1 is', set1
            for j in range(i+1, length):
                key2 = dict[keys[j]].split('|')
                set2 = set(key2)
                set2.remove('')
                print 'set2 is', set2
                attrsimi = calattrsimi(set1, set2)
                string = str(keys[i]) +'::' +  str(keys[j]) + '::' + str(attrsimi) + '::' + 'a' + '\n'
                print string
                file_object.write(string)
    finally:
        file_object.close()

if __name__ == '__main__':
    dict = {}
    readfile('2.txt', dict)
    #print dict
    writeFile('attrsimi.dat', dict)
