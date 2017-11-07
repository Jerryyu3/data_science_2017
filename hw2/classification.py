import sys
import numpy as np
from sklearn.neural_network import MLPClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn import svm

from sklearn.model_selection import GridSearchCV, StratifiedKFold



def readData():
  X_train = np.genfromtxt(sys.argv[2], delimiter=',')
  Y_train = [X_train[:, -1]]
  X_train = X_train[:,:-1]
  X_test = np.genfromtxt(sys.argv[3], delimiter=',')
  Y_train = np.transpose(Y_train)
  return X_train, Y_train, X_test

def computeMean_Var(X):
  length = (np.shape(X)[1]);
  table = np.zeros((2,length));
  for i in range(length):
    if(i>=0):
      table[0][i] = np.mean(X[:,i]); table[1][i] = np.std(X[:,i]);
  return table;

def normalize(lX,table):
  length = np.shape(table)[1];
  for i in range(length):
    if(table[1,i] > 0): lX[:,i] = (lX[:,i]-table[0,i])/table[1,i];

def check_answer(output, fileName):
  data = np.genfromtxt(fileName, delimiter=',')
  Y_test = np.transpose([data])
  #print (output, Y_test)
  #print ((output == Y_test)) 
  print (1-np.mean(Y_test[:,0]), np.mean(output == Y_test))

  #print(1-np.mean(Y_test[:,0]), np.mean((output != Y_test) * (output == 1)), np.mean((output != Y_test) * (output == 0)))

def predict(output):
  print ("Output predict.csv!")
  np.savetxt('predict.csv', output, fmt='%d', delimiter=",")

def logistic_reg(X_train, Y_train, X_test):
  print ("logistic regression!")
  #table = computeMean_Var(np.concatenate((X_train, X_test), axis=0)) 
  table = computeMean_Var(X_train) 
  normalize(X_train, table); normalize(X_test, table)

  parameter_gridsearch = {
    'C':[2.0, 3.0, 4.0, 5.0, 6.0],
    'max_iter':[25, 50, 75, 100],
    'solver' : ['newton-cg', 'liblinear'],
    #'class_weight':['balanced'],
    }

  logic = LogisticRegression()
  crossvalidation = StratifiedKFold(n_splits=5)

  gridsearch = GridSearchCV(logic,
    scoring='accuracy',
    param_grid=parameter_gridsearch,
    cv=crossvalidation)

  gridsearch.fit(X_train, Y_train[:,0])
  parameters = gridsearch.best_params_
  #print(parameters)

  #print(gridsearch.best_estimator_.coef_)

  #print(1-np.mean(Y_train[:,0]),'Best Score: {}'.format(gridsearch.best_score_))
                                                  
  output = gridsearch.predict(X_test); output = np.transpose([output]);
  predict(output)
  #check_answer(output, 'test_ans.csv')

  output = gridsearch.predict(X_train)
  #print (1-np.mean(Y_train[:,0]), np.mean(output==Y_train[:,0]))

  #print(np.mean((output != Y_train[:,0]) * (output == 1)), np.mean((output != Y_train[:,0]) * (output == 0)))


def decision_tree(X_train, Y_train, X_test):
  print ("decision tree!")
  table = computeMean_Var(X_train) 
  normalize(X_train, table); normalize(X_test, table)

  parameter_gridsearch = {
    'max_depth':[None, 10, 20, 30],
    'min_samples_split':[2, 3, 4],
    'min_samples_leaf' : [1, 2, 3, 4],
    'max_features':['auto', 'log2'],
    }

  DT = DecisionTreeClassifier()
  crossvalidation = StratifiedKFold(n_splits=5)

  gridsearch = GridSearchCV(DT,
    scoring='accuracy',
    param_grid=parameter_gridsearch,
    cv=crossvalidation)

  gridsearch.fit(X_train, Y_train[:,0])
  parameters = gridsearch.best_params_
  #print(parameters)

  #print(1-np.mean(Y_train[:,0]),'Best Score: {}'.format(gridsearch.best_score_))
                                                  
  output = gridsearch.predict(X_test); output = np.transpose([output]);
  predict(output)
  #check_answer(output, 'test_ans.csv')

  output = gridsearch.predict(X_train)
  #print (1-np.mean(Y_train[:,0]), np.mean(output==Y_train[:,0]))

def SVM(X_train, Y_train, X_test):
  print ("SVM!")
  table = computeMean_Var(X_train) 
  normalize(X_train, table); normalize(X_test, table)

  parameter_gridsearch = [{
    'kernel':['rbf'],
    'C':[1.0, 10.0, 100.0, 1000.0],
    'gamma':[0.001,0.0001],
    }, {'C': [1.0, 10.0, 100.0, 1000.0], 'kernel': ['linear']}]

  SVM = svm.SVC()
  crossvalidation = StratifiedKFold(n_splits=5)

  gridsearch = GridSearchCV(SVM,
    scoring='accuracy',
    param_grid=parameter_gridsearch,
    cv=crossvalidation)

  gridsearch.fit(X_train, Y_train[:,0])
  parameters = gridsearch.best_params_
  #print(parameters)

  #print(1-np.mean(Y_train[:,0]),'Best Score: {}'.format(gridsearch.best_score_))
                                                  
  output = gridsearch.predict(X_test); output = np.transpose([output]);
  predict(output)
  #check_answer(output, 'test_ans.csv')

  output = gridsearch.predict(X_train)
  #print (1-np.mean(Y_train[:,0]), np.mean(output==Y_train[:,0]))



def NN(X_train, Y_train, X_test):
  print ("NN!")
  table = computeMean_Var(X_train) 
  normalize(X_train, table); normalize(X_test, table)
  parameter_gridsearch = {
    'hidden_layer_sizes':[(100, )],
    'activation':['relu'],
    'solver':['adam'],
    'batch_size':['auto'],
    'learning_rate_init':[0.001],
    'max_iter':[300],
    'shuffle':[True],
    'momentum':[0.9],
    'alpha':[0.0001],

    } 

  NN = MLPClassifier()
  crossvalidation = StratifiedKFold(n_splits=5)

  gridsearch = GridSearchCV(NN,
    scoring='accuracy',
    param_grid=parameter_gridsearch,
    cv=crossvalidation)

  gridsearch.fit(X_train, Y_train[:,0])
  parameters = gridsearch.best_params_
  #print(parameters)

  #print(1-np.mean(Y_train[:,0]),'Best Score: {}'.format(gridsearch.best_score_))
                                                  
  output = gridsearch.predict(X_test); output = np.transpose([output]);
  predict(output)
  #check_answer(output, 'test_ans.csv')

  output = gridsearch.predict(X_train)
  #print (1-np.mean(Y_train[:,0]), np.mean(output==Y_train[:,0]))

  
if __name__ == '__main__':
  X_train, Y_train, X_test = readData()
  #print (X_train, Y_train, X_test, np.shape(X_train), np.shape(Y_train), np.shape(X_test))
  if(sys.argv[1] == "R"): logistic_reg(X_train, Y_train, X_test)
  if(sys.argv[1] == "D"): decision_tree(X_train, Y_train, X_test)
  if(sys.argv[1] == "S"): SVM(X_train, Y_train, X_test)
  if(sys.argv[1] == "N"): NN(X_train, Y_train, X_test)

