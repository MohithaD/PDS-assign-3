import pandas as pd
import os
from nltk.tokenize import word_tokenize

path=os.getcwd()
print(path)

fd=pd.read_csv("C:/Users/Mohit/OneDrive/Desktop/Corona_NLP_test.csv")

cor = fd['OriginalTweet']

tok = []

# Tokenize each tw by looping through the cor
for tw in cor:
  #  From nltk utilize word_tokenize and then tokenize the tw
  tw_tok = word_tokenize(tw)

#  Add the tok from the tw to the list.
tok.extend(tw_tok)

# Print tok
print(tok)