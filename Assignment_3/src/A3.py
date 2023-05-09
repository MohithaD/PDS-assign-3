import pandas as pd
from collections import Counter
from nltk.tokenize import word_tokenize

# Using the CSV file, populate a pandas DataFrame.
fd=pd.read_csv("C:/Users/Mohit/OneDrive/Desktop/Corona_NLP_test.csv")

# Make a cor of text using the "OriginalTweet" column.
cor = fd['OriginalTweet']

# To hold the tok, create a blank list.
tok = []

#By iterating over each tw in the cor, tokenize it. 
for tw in cor:
  #Tokenize the tw using word_tokenize from NLTK.
  tw_tok = word_tokenize(tw)

# Add the current tweet's tokens to the list.
tok.extend(tw_tok)

# Determine word frequency.
word_frequencies = Counter(tok)

# Print word frequencies
for word, frequency in word_frequencies.items():
  print(f'{word}: {frequency}')