# import libraries
import pandas as pd
# used to analyse data

import nltk
# main libary for sentiment analysis

from nltk.sentiment.vader import SentimentIntensityAnalyzer
#a pre-trained model for sentiment analysis

from nltk.corpus import stopwords
#contains a list of common words that are usually removed from text during processing.

from nltk.tokenize import word_tokenize
#is used to split text into individual words.

from nltk.stem import WordNetLemmatizer
#is used to convert words to their base form.


# download nltk corpus (first time only)
import nltk

#nltk.download('all')




# Load the amazon review dataset

df = pd.read_csv('https://raw.githubusercontent.com/pycaret/pycaret/master/datasets/amazon.csv')

df
