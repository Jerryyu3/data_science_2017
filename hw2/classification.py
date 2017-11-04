import sys
import numpy as np
from sklearn.neural_network import MLPClassifier

def readData():
  X_train = np.genfromtxt(sys.argv[2], delimiter=',')
  Y_train = [X_train[:, -1]]
  X_train = X_train[:,:-1]
  X_test = np.genfromtxt(sys.argv[3], delimiter=',')
  Y_train = np.transpose(Y_train)
  return X_train, Y_train, X_test

def NN(X_train, Y_train, X_test):
  

if __name__ == '__main__':
  X_train, Y_train, X_test = readData()
  #print (X_train, Y_train, X_test, np.shape(X_train), np.shape(Y_train), np.shape(X_test))
  
