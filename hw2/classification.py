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

def logistic_reg(X_train, Y_train, X_test):
  print ("logistic regression!")

def decision_tree(X_train, Y_train, X_test):
  print ("decision tree!")

def SVM(X_train, Y_train, X_test):
  print ("SVM!")

def NN(X_train, Y_train, X_test):
  print ("neural network!")
  
if __name__ == '__main__':
  X_train, Y_train, X_test = readData()
  #print (X_train, Y_train, X_test, np.shape(X_train), np.shape(Y_train), np.shape(X_test))
  if(sys.argv[1] == "R"):
     logistic_reg(X_train, Y_train, X_test)
  if(sys.argv[1] == "D"):
     decision_tree(X_train, Y_train, X_test)
  if(sys.argv[1] == "S"):
     SVM(X_train, Y_train, X_test)
  if(sys.argv[1] == "N"):
     NN(X_train, Y_train, X_test)

