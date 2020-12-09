# Toxic-Comment-Classification


The internet has allowed individuals to connect and learn from each other. It requires a comforting and friendly environment to learn from others and simultaneously communicate one's feelings and thoughts to others. Online hate, harassment and toxicity discourage individuals from opening up and taking full advantage of the opportunities provided by online communication. In this project, six types of toxicities were predefined: toxic, severe toxic, obscene threat, insult, identity hate. The dataset of comments from Wikipedia’s talk page edits is also used. The training data includes 159,571 labeled comments for toxic actions labeled by human raters, and we split 20% of training data as validation set. The test data contains 63,978 unlabeled comments. Our goal is to classify toxicity from the six types of toxicities by using machine learning techniques. This could be used to prevent users from posting potentially toxic posts, create more respectful comments when communicating with others, and to assess the toxicity of comments from other users. 

This project aims to implement different deep learning approaches. We implemented two methods to study the effect of different models. To compare our approach, first, we convert comments to Term Frequency–Inverse Document Frequency (TF-IDF) to build Logistic Regression and Naive Bayes classification models. Then, we convert comments to word vector using the word embedding model (Word2vec, GloVe) to build Convolutional Neural Nets (CNN) and Recurrent Neural Nets (RNN) - Long Short-Term Memory (LSTM) classification models. We use accuracy metric to measuring the performance of each model. The challenging problem in this task is that one comment can have multiple types of toxicities at the same time. Therefore, this is a multi-label classification problem where one instance can have more than one target class labels.


This project concentrates on various strategies - TF-IDF and Word Embedding - to study the effects of various deep learning approaches. A summary of the tasks performed is as follows:

 \begin{enumerate}
   \item Data Pre-processing and Split the data to Train, Validation and Test
   \item Method 1:
   \begin{enumerate}
     \item Convert comments to TF-IDF on train data
     \item Build Classification Models
     \begin{enumerate}
       \item Logistic Regression
       \item Naive Bayes
     \end{enumerate}
     \item Assess the models on the validation results and tune the models
     \item Test performance of final model on Test dataset
   \end{enumerate}
   \item Method 2:
   \begin{enumerate}
     \item Train a word embedding model on a pre-trained model
     \item Using the word embedding model to transform text to word vector
     \item Build Classification Models
     \begin{enumerate}
      \item CNN - Word2Vec
      \item CNN - GolVe
      \item Long Short Term Memory Networks
     \end{enumerate}
     \item Assess the models on the validation results and tune the models. 
     \item Test performance of final model on Test dataset.
   \end{enumerate}
 \end{enumerate}
