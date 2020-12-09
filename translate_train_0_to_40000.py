import os
import pandas as pd
from googletrans import Translator

text = pd.read_csv('original_data/train.csv')
translated_comments = []

translator = Translator()
for i,t in enumerate(text.comment_text[0:40000]):
	if i % 5 ==0:
		print(i)
	try:
		encoded = translator.translate(t, dest='fr').text
		decoded = translator.translate(encoded, dest='en').text
		translated_comments.append(decoded)
	except:
		translated_comments.append(t)
		pass

translated_train = pd.read_csv('original_data/train.csv')
translated_train = translated_train[0:40000]
translated_train['comment_text'] = translated_comments
translated_train.to_csv('processed_data/train_translated_0_to_40000.csv', index = None)