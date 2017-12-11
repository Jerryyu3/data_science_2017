import numpy as np
import pandas as pd
import hyperopt
from catboost import Pool, CatBoostClassifier, cv
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

class GDBT_2:
    def __init__(self):
        self.model = CatBoostClassifier(custom_loss=['Logloss'], random_seed=24,iterations=300, od_type='Iter', od_wait=15, use_best_model=True, depth=4)

    def fit(self, X, y):
        #print (np.where(X.dtypes != np.float)[0])
        X.fillna(-999, inplace=True)
        X = X.drop('is_churn', axis=1)
        #X = X.drop('membership_expire_date', axis=1)
        #X = X.drop('transaction_date', axis=1) 
        #X = X.drop('registration_init_time',axis=1)
        #X = X.drop('None', axis=1)

        #print (X.dtypes)
        #categorical_features_indices = np.where(X.dtypes != np.float)[0]
        #print (categorical_features_indices)
        #print (pd.unique(X['is_cancel']))
        categorical_features_indices = np.array([0, 1, 3, 4, 14]) 

        X_train, X_validation, y_train, y_validation = train_test_split(X, y, train_size=0.9, random_state=1234)
        self.model.fit( X_train, y_train, cat_features=categorical_features_indices, eval_set=(X_validation, y_validation),plot=True )	
        print ('Early-stopped model validation accuracy: {:.4}'.format(
             accuracy_score(y_validation, self.model.predict(X_validation))
        ))

    def predict(self, X_test):
        X_test.fillna(-999, inplace=True)
        #X_test = X_test.drop('membership_expire_date', axis=1)
        #X_test = X_test.drop('transaction_date', axis=1) 
        #X_test = X_test.drop('registration_init_time',axis=1)

        #print (X_test)
        submission = pd.DataFrame()
        submission['msno'] = X_test['msno']
        #print ( self.model.predict_proba(X_test))
        submission['is_churn'] = self.model.predict_proba(X_test)[:,1]
        print ( submission['is_churn']  if submission['is_churn'] > 0.1 else 0 )
        #XDD = pd.read_csv('sample_submission_v2.csv')   
        #for element in XDD['msno']:
        #    print (element)
        
        submission.to_csv('submission.csv', index=False)

    #def fit_submission(self):
    #    with open('sample_submission_v2.csv', 'r') 

