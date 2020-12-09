import os
import pandas as pd
from googletrans import Translator

text = pd.read_csv('original_data/test.csv')
test_y = pd.read_csv("original_data/test_labels.csv")

#labels for the test data; value of -1 indicates it was not used for scoring
#we reomve those rows with no actual labels
test_y = test_y.loc[test_y['toxic'] != -1] 
text = text[text['id'].isin(test_y['id'])]

translated_comments = []

translator = Translator()

for i,t in enumerate(text.comment_text):
	if i %5 == 0:
		print(i)
	try:
		encoded = translator.translate(t, dest='fr').text
		decoded = translator.translate(encoded, dest='en').text
		translated_comments.append(decoded)
	except: 
		translated_comments.append(t)
		pass

translated_test = text
translated_test['comment_text'] = translated_comments
translated_test.to_csv('processed_data/test_translated.csv',index=None)
