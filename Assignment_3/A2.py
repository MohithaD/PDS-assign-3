
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download NLTK st word(one).
nltk.download('stopwords')

# Using the CSV file, populate a pandas DataFrame..
fd=pd.read_csv("C:/Users/Mohit/OneDrive/Desktop/Corona_NLP_test.csv")

#Extract the "OriginalTweet" column as a text cor. .
cor = fd['OriginalTweet']

# start NLTK st wor
st_wor = set(stwor.wor('english'))

# At starting, create a blank list to store the tok without any st wor.
fil_tok = []

# Iteratively remove the st wor from each tw in the cor.
for tw in cor:
  #Tokenize the tw using word_tokenize from NLTK.
  tw_tok = word_tokenize(tw)

#  From the tok in the current tw remove st wor.
fil_tok.extend([tok for tok in tw_tok if tok.lower() not in st_wor])

# Print fil tok
print(fil_tok)