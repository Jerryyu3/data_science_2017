import sys
import random
import numpy as np

data = np.genfromtxt('hw2_data/spambase.csv', delimiter=',')
#print (data)
random.shuffle(data)
#print (data)

split_num = 3999

train = data[:split_num,:]
test = data[split_num:,:-1]
test_ans = np.transpose([data[split_num:,-1]])

print (np.shape(train), np.shape(test), np.shape(test_ans))

np.savetxt(sys.argv[1], train, fmt='%f', delimiter=",")
np.savetxt(sys.argv[2], test, fmt='%f', delimiter=",")
np.savetxt(sys.argv[3], test_ans, fmt='%f', delimiter=",")
