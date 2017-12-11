import numpy as np
import pandas as pd

def parseData(args):
    train_path = args[0]
    test_path = args[1]

    #train = parseTrain(train_path)
    #testID, test = parseTest(test_path)

    train = parseDataToPandas(train_path)
    test = parseDataToPandas(test_path)

    return train, train['is_churn'], test

def parseTrain(path):
    with open(path, 'r', encoding='UTF-8') as file:
        train_raw = file.read()
        train_raw = train_raw.split('\n')
        train_raw = train_raw[1:]
        for idx, value in enumerate(train_raw):
            train_raw[idx] = value.split(',')
            train_raw[idx] = train_raw[idx][1:]
        return train_raw        

def parseTest(path):
    with open(path, 'r', encoding='UTF-8') as file:
        test_raw = file.read()
        test_raw = test_raw.split('\n')
        test_raw = test_raw[1:]
        testID = []
        for idx, value in enumerate(test_raw):
            test_raw[idx] = value.split(',')
            testID.append(test_raw[idx][0])
            test_raw[idx] = test_raw[idx][1:]
        return testID, test_raw    

def parseDataToPandas(path):
    return pd.read_csv(path)

