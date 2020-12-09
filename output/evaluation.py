import pandas as pd
import numpy as np
from sklearn import metrics


logR_output = pd.read_csv('LogisticRegressionOutput.csv')
nB_output = pd.read_csv('NaiveBayesOutput.csv')
word2vec_output = pd.read_csv('word2vecOutput.csv')
glove_output = pd.read_csv('gloveOutput.csv')
lstm_output = pd.read_csv('lstmOutput.csv')
test_y = pd.read_csv("test_labels_cleaned.csv")

col = ['toxic', 'severe_toxic', 'obscene', 'threat','insult', 'identity_hate']

#show results for logistics
total_score = 0
output = logR_output
print('###################Logistic Regression###################')
for i,x in enumerate(col):
    print("Accuracy Score for ",x," on Test is: ",metrics.accuracy_score(test_y[x], output[x]))
    score = metrics.accuracy_score(test_y[x], output[x])
    total_score= total_score + score
print('The average accuracy score for six toxicities is: ', round(total_score/6 , 4) )
print('#########################################################\n')


#show results for Naive Bayes
total_score = 0
output = nB_output
print('#######################Naive Bayes#######################')
for i,x in enumerate(col):
    print("Accuracy Score for ",x," on Test is: ",metrics.accuracy_score(test_y[x], output[x]))
    score = metrics.accuracy_score(test_y[x], output[x])
    total_score= total_score + score
print('The average accuracy score for six toxicities is: ', round(total_score/6 , 4) )
print('#########################################################\n')


#show results for CNN -- Wrod2Vec
total_score = 0
output = word2vec_output
print('#####################CNN -- Wrod2Vec#####################')
for i,x in enumerate(col):
    print("Accuracy Score for ",x," on Test is: ",metrics.accuracy_score(test_y[x], output[x]))
    score = metrics.accuracy_score(test_y[x], output[x])
    total_score= total_score + score
print('The average accuracy score for six toxicities is: ', round(total_score/6 , 4) )
print('#########################################################\n')



#show results for CNN -- GloVe
total_score = 0
output = glove_output
print('#####################CNN -- GloVe########################')
for i,x in enumerate(col):
    print("Accuracy Score for ",x," on Test is: ",metrics.accuracy_score(test_y[x], output[x]))
    score = metrics.accuracy_score(test_y[x], output[x])
    total_score= total_score + score
print('The average accuracy score for six toxicities is: ', round(total_score/6 , 4) )
print('#########################################################\n')



#show results for RNN -- LSTM
total_score = 0
output = lstm_output
print('#######################RNN -- LSTM#######################')
for i,x in enumerate(col):
    print("Accuracy Score for ",x," on Test is: ",metrics.accuracy_score(test_y[x], output[x]))
    score = metrics.accuracy_score(test_y[x], output[x])
    total_score= total_score + score
print('The average accuracy score for six toxicities is: ', round(total_score/6 , 4) )
print('#########################################################\n')




