import pandas as pd
import matplotlib.pyplot as plt
from wordcloud import WordCloud
from nltk.tokenize import word_tokenize

# The CSV file should be loaded into a pandas DataFrame.
fd=pd.read_csv("C:/Users/Mohit/OneDrive/Desktop/Corona_NLP_test.csv")


# Make a cor of tex using the "OriginalTweet" column.
cor = fd['OriginalTweet']

# all tw should be combined into a single string.
tex = ' '.join(cor)

# Tokenize tex
tok = word_tokenize(tex)

# all tw should be combined into a single string.
proc_tex = ' '.join(tok)

# Build a word cloud
wordcloud = WordCloud(width=800, height=400, background_color='purple').generate(proc_tex)

# Plot word cloud
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation='bilinear')
plt.axis('off')
plt.show()