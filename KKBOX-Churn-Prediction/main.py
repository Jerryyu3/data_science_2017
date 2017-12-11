import sys
from Parser import *
from GDBT import *

def main(args):
    trainX, trainY, testX = parseData(args)
    #print(trainX, trainY)
    model = GDBT_2()
    model.fit(trainX, trainY)
    model.predict(testX)

if __name__ == '__main__':
    args = sys.argv[1:]
    main(args)
